"""
GR-MARKET_FLEXDEMAND.py

Flexible Demand Optimization Model for European Day-Ahead Electricity Market.

This script demonstrates the flexible demand model using market data.
It prepares input data, defines optimization variables, and sets up
the structure for optimization using Gurobi.

NOTE: Requires a Gurobi license to run actual optimization.
"""
import time
import pandas as pd
from gurobipy import Model, GRB, quicksum

start_time = time.time()

data_path = "input/20240517cl.xlsx"

df = pd.read_excel(data_path, header=0, sheet_name='EL-DAM_AggrCurves')

df['Period_Index'] = df['SORT']

# --- Initialize dictionaries ---
BUY_ORDER, SELL_ORDER = {}, {}
Pd_max, Pg_max = {}, {}
B_d, C_g = {}, {}
SORT_buy, SORT_sell = {}, {}
BID_BUY_NUMBER, OFFER_SELL_NUMBER = {}, {}
B_d_shift_away, B_d_shift_towards = {}, {}

# --- Process data per period ---
for period in range(1, 25):
    period_data = df[df['Period_Index'] == period]

    # Buy Orders
    buy_data = period_data[period_data['SIDE_DESCR'] == 'Buy']
    BUY_ORDER[f'T{period}'] = buy_data['SIDE_DESCR'].tolist()
    Pd_max[f'T{period}'] = buy_data['QUANTITY'].tolist()
    B_d[f'T{period}'] = buy_data['UNITPRICE'].tolist()
    SORT_buy[f'T{period}'] = buy_data['SORT'].tolist()
    BID_BUY_NUMBER[f'T{period}'] = buy_data['AA'].tolist()
    B_d_shift_away[f'T{period}'] = buy_data['DISCOMFORT_COST_SHIFT_AWAY'].tolist()
    B_d_shift_towards[f'T{period}'] = buy_data['DISCOMFORT_COST_SHIFT_TOWARDS'].tolist()

    # Sell Orders
    sell_data = period_data[period_data['SIDE_DESCR'] == 'Sell']
    SELL_ORDER[f'T{period}'] = sell_data['SIDE_DESCR'].tolist()
    Pg_max[f'T{period}'] = sell_data['QUANTITY'].tolist()
    C_g[f'T{period}'] = sell_data['UNITPRICE'].tolist()
    SORT_sell[f'T{period}'] = sell_data['SORT'].tolist()
    OFFER_SELL_NUMBER[f'T{period}'] = sell_data['AA'].tolist()
FLEXI_data = df.loc[0:115, 'FLEXIBILITY'].tolist()
a_shift = {bid_number: FLEXI_data[bid_number-1] for bid_number in range(1, len(BID_BUY_NUMBER['T1']) + 1)}

Pgmax, Cg = {}, {}
for t in range(1, 25):
    for offer_number in range(1, len(OFFER_SELL_NUMBER[f'T{t}']) + 1):
        Pgmax[(offer_number, t)] = Pg_max[f'T{t}'][offer_number-1]
        Cg[(offer_number, t)] = C_g[f'T{t}'][offer_number-1]

Pdmax, Bd = {}, {}
for t in range(1, 25):
    for bid_number in range(1, len(BID_BUY_NUMBER[f'T{t}']) + 1):
        Pdmax[(bid_number, t)] = Pd_max[f'T{t}'][bid_number-1]
        Bd[(bid_number, t)] = B_d[f'T{t}'][bid_number-1]

Bd_shift_away, Bd_shift_towards = {}, {}
for t in range(1, 25):
    for bid_number in range(1, len(BID_BUY_NUMBER[f'T{t}']) + 1):
        Bd_shift_away[(bid_number, t)] = B_d_shift_away[f'T{t}'][bid_number-1]
        Bd_shift_towards[(bid_number, t)] = B_d_shift_towards[f'T{t}'][bid_number-1]

model = Model("EU_DayAhead_FlexDemand")

p_g = {(idx, t): model.addVar(vtype=GRB.CONTINUOUS, lb=0, name=f"p_g_{idx}_{t}")
       for t in range(1, 25)
       for idx in range(1, len(OFFER_SELL_NUMBER[f'T{t}']) + 1)}

p_d_b = {(idx, t): model.addVar(vtype=GRB.CONTINUOUS, lb=0, name=f"p_d_{idx}_{t}")
         for t in range(1, 25)
         for idx in range(1, len(BID_BUY_NUMBER[f'T{t}']) + 1)}

Pd_sh_away = {(idx, t): model.addVar(vtype=GRB.CONTINUOUS, lb=0, name=f"Pd_sh_away_{idx}_{t}")
              for t in range(1, 25)
              for idx in range(1, len(BID_BUY_NUMBER[f'T{t}']) + 1)}

Pd_sh_towards = {(idx, t): model.addVar(vtype=GRB.CONTINUOUS, lb=0, name=f"Pd_sh_towards_{idx}_{t}")
                 for t in range(1, 25)
                 for idx in range(1, len(BID_BUY_NUMBER[f'T{t}']) + 1)}
constraints = {}

for t in range(1, 25):
    for offer_number in range(1, len(OFFER_SELL_NUMBER[f'T{t}']) + 1):
        constraint_name_lower = f"Power_generation_Limit_lower_{offer_number}_{t}"
        constraint_expr_lower = p_g[offer_number, t] >= 0
        constraints[constraint_name_lower] = model.addConstr(constraint_expr_lower, name=constraint_name_lower)

        constraint_name_upper = f"Power_generation_Limit_upper_{offer_number}_{t}"
        constraint_expr_upper = p_g[offer_number, t] <= Pgmax[(offer_number, t)]
        constraints[constraint_name_upper] = model.addConstr(constraint_expr_upper, name=constraint_name_upper)

for t in range(1, 25):
    for bid_number in range(1, len(BID_BUY_NUMBER[f'T{t}']) + 1):
        constraint_name_lower = f"Power_Demand_Limit_lower_{bid_number}_{t}"
        constraint_expr_lower = p_d_b[bid_number, t] >= 0
        constraints[constraint_name_lower] = model.addConstr(constraint_expr_lower, name=constraint_name_lower)

        constraint_name_upper = f"Power_Demand_Limit_Upper_{bid_number}_{t}"
        constraint_expr_upper = p_d_b[bid_number, t] <= Pdmax[(bid_number, t)]
        constraints[constraint_name_upper] = model.addConstr(constraint_expr_upper, name=constraint_name_upper)

for t in range(1, 25):
    constraint_name = f"Power_Balance_{t}"
    constraint_expr = (
        quicksum(p_g[offer_number, t] for offer_number in range(1, len(OFFER_SELL_NUMBER[f'T{t}']) + 1)) -
        quicksum(p_d_b[bid_number, t] - Pd_sh_away[bid_number, t] + Pd_sh_towards[bid_number, t] for bid_number in range(1, len(BID_BUY_NUMBER[f'T{t}']) + 1))
    )
    constraints[constraint_name] = model.addConstr(constraint_expr == 0, name=constraint_name)

for t in range(1, 25):
    for bid_number in range(1, len(BID_BUY_NUMBER[f'T{t}']) + 1):
        constraint_name_away_lower = f"Flexibility_SH_AWAY_Lower_{bid_number}_{t}"
        constraints[constraint_name_away_lower] = model.addConstr(Pd_sh_away[bid_number, t] >= 0, name=constraint_name_away_lower)

        constraint_name_away_upper = f"Flexibility_SH_AWAY_Upper_{bid_number}_{t}"
        constraints[constraint_name_away_upper] = model.addConstr(Pd_sh_away[bid_number, t] <= a_shift[bid_number] * p_d_b[bid_number, t], name=constraint_name_away_upper)

        constraint_name_towards_lower = f"Flexibility_SH_TOWARDS_Lower_{bid_number}_{t}"
        constraints[constraint_name_towards_lower] = model.addConstr(Pd_sh_towards[bid_number, t] >= 0, name=constraint_name_towards_lower)

        constraint_name_towards_upper = f"Flexibility_SH_TOWARDS_Upper_{bid_number}_{t}"
        constraints[constraint_name_towards_upper] = model.addConstr(Pd_sh_towards[bid_number, t] <= a_shift[bid_number] * p_d_b[bid_number, t], name=constraint_name_towards_upper)

for bid_number in range(1, len(BID_BUY_NUMBER['T1']) + 1):
    constraint_name = f"Energy_Balance_{bid_number}"
    constraint_expr = quicksum(-Pd_sh_away[bid_number, t] + Pd_sh_towards[bid_number, t] for t in range(1, 25))
    constraints[constraint_name] = model.addConstr(constraint_expr == 0, name=constraint_name)

objective_expr = (
    quicksum(Bd[(bid_number, t)] * p_d_b[bid_number, t] for t in range(1, 25) for bid_number in range(1, len(BID_BUY_NUMBER[f'T{t}']) + 1)) -
    quicksum(Bd_shift_away[(bid_number, t)] * Pd_sh_away[bid_number, t] for t in range(1, 25) for bid_number in range(1, len(BID_BUY_NUMBER[f'T{t}']) + 1)) -
    quicksum(Bd_shift_towards[(bid_number, t)] * Pd_sh_towards[bid_number, t] for t in range(1, 25) for bid_number in range(1, len(BID_BUY_NUMBER[f'T{t}']) + 1)) -
    quicksum(Cg[(offer_number, t)] * p_g[offer_number, t] for t in range(1, 25) for offer_number in range(1, len(OFFER_SELL_NUMBER[f'T{t}']) + 1))
)

model.setObjective(objective_expr, GRB.MAXIMIZE)
model.optimize()
