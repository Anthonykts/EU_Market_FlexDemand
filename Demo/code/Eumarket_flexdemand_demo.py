import pandas as pd
from pyomo.environ import ConcreteModel, Set, Var, NonNegativeReals
from pyomo.environ import Constraint, ConstraintList, Objective, maximize, SolverFactory, Suffix
from pyomo.environ import value
import pandas as pd
input_file = "input/flexi.xlsx"
df = pd.read_excel(input_file, sheet_name='Sheet1')
time_periods = [1, 2]

generators_number = df.iloc[1:8, 1].astype(int).tolist()
Cgt1 = df.loc[1:7, 'Unnamed: 3'].tolist()
Cgt2 = df.loc[9:15, 'Unnamed: 3'].tolist()
Pgmaxt1 = df.loc[1:7, 'Unnamed: 4'].tolist()
Pgmaxt2 = df.loc[9:15, 'Unnamed: 4'].tolist()

C_g = {g: {1: Cgt1[i], 2: Cgt2[i]} for i, g in enumerate(generators_number)}
Pg_max = {g: {1: Pgmaxt1[i], 2: Pgmaxt2[i]} for i, g in enumerate(generators_number)}

demand_number = df.iloc[1:7, 1].astype(int).tolist()
Bdt1 = df.loc[1:6, 'Unnamed: 7'].tolist()
Bdt2 = df.loc[9:14, 'Unnamed: 7'].tolist()
Pdmaxt1 = df.loc[1:6, 'Unnamed: 8'].tolist()
Pdmaxt2 = df.loc[9:14, 'Unnamed: 8'].tolist()

B_d = {d: {1: Bdt1[i], 2: Bdt2[i]} for i, d in enumerate(demand_number)}
Pd_max = {d: {1: Pdmaxt1[i], 2: Pdmaxt2[i]} for i, d in enumerate(demand_number)}

# ----------------- FLEXIBILITY
Bd_SWIFT_AWAY_T1 = df.loc[1:6, 'Unnamed: 10'].tolist()
Bd_SWIFT_AWAY_T2 = df.loc[9:14, 'Unnamed: 10'].tolist()
Bd_SWIFT_TOWARDS_T1 = df.loc[1:6, 'Unnamed: 11'].tolist()
Bd_SWIFT_TOWARDS_T2 = df.loc[9:14, 'Unnamed: 11'].tolist()
a_shift_t1 = df.loc[1:6, 'Unnamed: 9'].tolist()
a_shift_t2 = df.loc[9:14, 'Unnamed: 9'].tolist()
B_d_sh_away = {d: {1: Bd_SWIFT_AWAY_T1[i], 2: Bd_SWIFT_AWAY_T2[i]} for i, d in enumerate(demand_number)}
B_d_sh_towards = {d: {1: Bd_SWIFT_TOWARDS_T1[i], 2: Bd_SWIFT_TOWARDS_T2[i]} for i, d in enumerate(demand_number)}
a_d = {d: {1: a_shift_t1[i], 2: a_shift_t2[i]} for i, d in enumerate(demand_number)}

# ----------------- Pyomo Model
model = ConcreteModel()

# Sets
model.T = Set(initialize=time_periods)
model.G = Set(initialize=generators_number)
model.D = Set(initialize=demand_number)

# Decision variables
model.pg = Var(model.G, model.T, domain=NonNegativeReals)
model.pd_b = Var(model.D, model.T, domain=NonNegativeReals)
model.pd_sh_away = Var(model.D, model.T, domain=NonNegativeReals)
model.pd_sh_towards = Var(model.D, model.T, domain=NonNegativeReals)
# -----------------------------
# Constraint 1: Power Balance
def power_balance_rule(model, t):
    lhs = sum(model.pg[g, t] for g in model.G)
    rhs = sum(model.pd_b[d, t] + model.pd_sh_towards[d, t] - model.pd_sh_away[d, t] for d in model.D)
    return lhs == rhs
model.PowerBalance = Constraint(model.T, rule=power_balance_rule)

# Constraint 2: Power demand limits (0 <= pd_b <= Pd_max)
model.DemandLimits = ConstraintList()
for t in model.T:
    for d in model.D:
        model.DemandLimits.add(model.pd_b[d, t] >= 0)
        model.DemandLimits.add(model.pd_b[d, t] <= Pd_max[d][t])

# Constraint 3: Power Generation Limits (0 <= pg <= Pg_max)
model.GenerationLimits = ConstraintList()
for t in model.T:
    for g in model.G:
        model.GenerationLimits.add(model.pg[g, t] >= 0)
        model.GenerationLimits.add(model.pg[g, t] <= Pg_max[g][t])

# Constraint 4: Shifting Away Power Limits (0 <= pd_sh_away <= a_d * pd_b)
model.FlexShAway = ConstraintList()
for t in model.T:
    for d in model.D:
        model.FlexShAway.add(model.pd_sh_away[d, t] >= 0)
        model.FlexShAway.add(model.pd_sh_away[d, t] <= a_d[d][t] * model.pd_b[d, t])

# Constraint 5: Shifting Towards Power Limits (0 <= pd_sh_towards <= a_d * pd_b)
model.FlexShTowards = ConstraintList()
for t in model.T:
    for d in model.D:
        model.FlexShTowards.add(model.pd_sh_towards[d, t] >= 0)
        model.FlexShTowards.add(model.pd_sh_towards[d, t] <= a_d[d][t] * model.pd_b[d, t])

# Constraint 6: Energy Neutrality (sum over time periods = 0)
model.EnergyNeutrality = ConstraintList()
for d in model.D:
    expr = sum(model.pd_sh_towards[d, t] - model.pd_sh_away[d, t] for t in model.T)
    model.EnergyNeutrality.add(expr == 0)

# -----------------------------
# Objective Function: Social Welfare
def objective_rule(model):
    return (
        sum(B_d[d][t] * model.pd_b[d, t] for d in model.D for t in model.T)
        - sum(B_d_sh_away[d][t] * model.pd_sh_away[d, t] for d in model.D for t in model.T)
        - sum(B_d_sh_towards[d][t] * model.pd_sh_towards[d, t] for d in model.D for t in model.T)
        - sum(C_g[g][t] * model.pg[g, t] for g in model.G for t in model.T)
    )

model.Objective = Objective(rule=objective_rule, sense=maximize)

solver = SolverFactory('glpk')
model.dual = Suffix(direction=Suffix.IMPORT)

results = solver.solve(model)
results.write()


# -----------------------------

prices = {t: -model.dual[model.PowerBalance[t]] for t in model.T}
producer_profit_per_hour = {}
for t in model.T:
    profit_t = 0
    price_t = prices[t]
    for g in model.G:
        pg_val = value(model.pg[g, t])
        cost = C_g[g][t] * pg_val
        profit_t += price_t * pg_val - cost
    producer_profit_per_hour[t] = profit_t

consumer_utility_per_hour = {}
for t in model.T:
    utility_t = 0
    price_t = prices[t]
    for d in model.D:
        pd_b_val = value(model.pd_b[d, t])
        pd_away_val = value(model.pd_sh_away[d, t])
        pd_towards_val = value(model.pd_sh_towards[d, t])
        utility_t += (
            B_d[d][t] * pd_b_val
            - price_t * pd_b_val
            - B_d_sh_away[d][t] * pd_away_val
            + price_t * pd_away_val
            - B_d_sh_towards[d][t] * pd_towards_val
            + price_t * pd_towards_val
        )
    consumer_utility_per_hour[t] = utility_t

social_welfare_per_hour = {
    t: producer_profit_per_hour[t] + consumer_utility_per_hour[t] for t in model.T
}

total_producer_profit = sum(producer_profit_per_hour.values())
total_consumer_utility = sum(consumer_utility_per_hour.values())
total_social_welfare = total_producer_profit + total_consumer_utility

results_sheet1 = []
for t in model.T:
    for g in model.G:
        gen_value = value(model.pg[g, t])
        # Προσέγγιση αντιστοιχίας generator->demand αν υπάρχει
        d_index = None
        if g <= len(model.D):
            d_index = list(model.D)[list(model.G).index(g)]
            pd_b_value = value(model.pd_b[d_index, t])
            pd_away_value = value(model.pd_sh_away[d_index, t])
            pd_towards_value = value(model.pd_sh_towards[d_index, t])
        else:
            pd_b_value = pd_away_value = pd_towards_value = None

        results_sheet1.append({
            "Time Period": t,
            "Generator Participant": g,
            "Generation (MWh)": f"{gen_value} MWh" if gen_value is not None else None,
            "Demand Participant": d_index,
            "Baseline Demand (MWh)": f"{pd_b_value} MWh" if pd_b_value is not None else None,
            "Shifting Away (MWh)": f"{pd_away_value} MWh" if pd_away_value is not None else None,
            "Shifting Towards (MWh)": f"{pd_towards_value} MWh" if pd_towards_value is not None else None
        })

df_sheet1 = pd.DataFrame(results_sheet1)

summary_results = []
for t in model.T:
    total_demand = sum(value(model.pd_b[d, t]) + value(model.pd_sh_towards[d, t]) - value(model.pd_sh_away[d, t]) for d in model.D)
    total_shifting_away = sum(value(model.pd_sh_away[d, t]) for d in model.D)
    total_shifting_towards = sum(value(model.pd_sh_towards[d, t]) for d in model.D)
    total_generation = sum(value(model.pg[g, t]) for g in model.G)
    price = prices[t]

    producer_profit = producer_profit_per_hour[t]
    consumer_utility = consumer_utility_per_hour[t]
    social_welfare = social_welfare_per_hour[t]

    summary_results.append({
        "Time Period": t,
        "Total Demand Power(MWh)": f"{total_demand} MWh",
        "Total Shifting Away Power(MWh)": f"{total_shifting_away} MWh",
        "Total Shifting Towards Power (MWh)": f"{total_shifting_towards} MWh",
        "Total Generated Power (MWh)": f"{total_generation} MWh",
        "Price (€/MWh)": f"{price:.2f} €/MWh",
        "Producer Profit (€)": f"{producer_profit:.2f} €",
        "Consumer Utility (€)": f"{consumer_utility:.2f} €",
        "Social Welfare (€)": f"{social_welfare:.2f} €"
    })

df_summary = pd.DataFrame(summary_results)

totals_row = {
    "Time Period": "TOTAL",
    "Total Demand Power(MWh)": "-",
    "Total Generated Power (MWh)": "-",
    "Price (€/MWh)": "-",
    "Producer Profit (€)": f"{total_producer_profit:.2f} €",
    "Consumer Utility (€)": f"{total_consumer_utility:.2f} €",
    "Social Welfare (€)": f"{total_social_welfare:.2f} €"
}

df_summary = pd.concat([df_summary, pd.DataFrame([totals_row])], ignore_index=True)

# -----------------------------
# Write to Excel
output_file = "output/eu_market_results_clean.xlsx"
with pd.ExcelWriter(output_file) as writer:
    df_sheet1.to_excel(writer, sheet_name="Power_and_Demand", index=False)
    df_summary.to_excel(writer, sheet_name="Summary", index=False)
