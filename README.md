# Flexible Demand in the European Day-Ahead Electricity Market

---

## 📑 Table of Contents

1. [Introduction](#introduction)  
2. [Key Features of the Model](#key-features-of-the-model)  
3. [Model Overview](#model-overview)  
4. [Key Model Components](#key-model-components)
5. [Project Structure](#project-structure)
6. [Main Project Overview](#main-project-overview)  
7. [Demo Overview](#demo-overview)  
8. [Case Studies & Results](#case-studies--results)  
   - [Case Study 1 – Sensitivity Analysis on Flexibility Factor (α)](#case-study-1--sensitivity-analysis-on-flexibility-factor-α)  
   - [Case Study 2 – Sensitivity Analysis on Discomfort Costs (Bd_sh_away--bd_sh_towards)](#case-study-2--sensitivity-analysis-on-discomfort-costs-bd_sh_away--bd_sh_towards)  
9. [General Model Summary](#general-model-summary) 
10. [Requirements & Dependencies](#dependencies)  
11. [License / Credits](#license--credits)

---

## Introduction

The **Day-Ahead Market** clears electricity generation and consumption based on hourly price–quantity bids. This project integrates **flexible demand**, allowing consumers to **shift part of their consumption** from high-price hours to low-price hours while maintaining **total daily energy neutrality**.  

It focuses on the **European day-ahead wholesale electricity market**, with a detailed case study for the **Greek market (May 17, 2024)**. The model is **general and agnostic**, meaning it does not rely on technical details of individual loads or consumers.This approach enables **scenario-based analyses** and the evaluation of **demand response strategies** without requiring detailed consumer-level data.  

The main objective is to **maximize social welfare**, accounting for both **production costs** and **consumer discomfort costs** arising from temporal load shifting.

---

## Key Features of the Model

**1. Independence from specific loads**  
The model does not require knowledge of technical characteristics of loads (e.g., device type, load curves, or operational constraints). Instead, demand is represented using general flexibility parameters, such as the maximum shiftable fraction of demand (flexibility parameter α) and optional discomfort costs for load shifting.

**2. Temporal (time-shifting) flexibility**  
Demand changes are allowed only within a predefined time horizon (e.g., 24 hours) while maintaining energy neutrality. Total daily consumption remains constant, but the timing of consumption can be adapted to market conditions to maximize social welfare or reduce peak prices.

**3. Generality and agnostic approach**  
The model can be applied to any market or system with available supply and demand data, without assumptions about the technical features of consumers. This allows:  
- Simulations at country or regional level without detailed consumer data  
- Easy extension to other European markets with different time steps or demand structures  
- Integration into strategic scenarios for pricing, demand management, and social welfare estimation

**4. Integration of discomfort costs**  
Optional discomfort cost parameters allow quantifying the trade-off between cost or social welfare optimization and consumer convenience.

**5. Flexible participation in market offers**  
- Buyers submit Hourly Orders (HO) including price, quantity, flexibility percentage, and discomfort costs  
- The model computes the optimal market clearing and pricing, considering demand shifts and energy balance

**6. Linear and convex structure**  
- Objective function and constraints are linear, enabling fast solution using LP solvers (GLPK, CBC, Gurobi)  
- Sensitivity analysis for different α values (flexibility levels) is straightforward

---

## Model Overview

The European market is typically cleared based on hourly price-quantity bids, where participants submit their supply and demand offers for each hour. To incorporate demand flexibility, the model allows shifting part of the demand from high-price hours to low-price hours without changing the total daily energy consumption. This shift is energy-neutral, meaning total consumption over the day remains constant, but the timing of consumption can adapt to market conditions.

### 1. Theoretical Framework
- Traditional utility functions: increasing, convex, quadratic → decreasing marginal utility  
- Low demand elasticity → price spikes, potential market power  
- Time-based flexibility is more realistic than pure price elasticity  

### 2. Flexible Demand Representation
- **Baseline demand**  
- **Temporal shift decision variables**  
- **Energy-neutral shifts** (total daily consumption constant)  
- **Discomfort costs** model consumer dissatisfaction from load shifting  

### 3. European Market Model
- Clears market considering buyers' ability to shift demand  
- Participants submit multi-parameter offers: price, maximum quantity, flexibility factor, discomfort costs  
- Optimization maximizes **social welfare**  

### 4. Assumptions
- 24-hour market clearing  
- Offers reflect actual economic and technical characteristics  
- Temporal shifting affects consumer satisfaction, modeled via discomfort costs  

---

## Key Model Components

This section summarizes the main elements of the flexible demand model:

| Element | Description |
|---------|-------------|
| **αd (Flexibility Parameter)** | Maximum fraction of baseline demand that can be shifted across hours |
| **Bd_sh_AWAY / Bd_sh_TOWARDS** | Discomfort costs for shifting demand away from or towards preferred consumption hours |
| **Objective Function** | Maximize **social welfare** (sum of consumer and producer surplus) |
| **Energy Neutrality** | Ensures total daily consumption remains constant |

### Key Points
- **Demand Flexibility (αd):** Controls the extent to which demand can be shifted across hours.  
- **Discomfort Costs:** Reflect consumer dissatisfaction for moving consumption from preferred hours.  
- **Objective:** Achieves a balance between **market efficiency** and **consumer comfort**.  
- **Sensitivity Analysis:** Allows exploration of different flexibility levels (α) and their impact on market outcomes.

---

## Project Structure

```bash
EU_Market_FlexDemand/
├── README.md
├── LICENSE
│
├── demo/
│   ├── README.md           
│   ├── code/
│   │   └── Eumarket_flexdemand_demo.py
│   ├── input/
│   │   └── flexi.xlsx
│   └── output/
│       ├── eu_market_results.xlsx
│       └── sensitivity_analysis/
│
└── main/
    ├── code/
    │   └── GR-MARKET_FLEXDEMAND.py
    ├── input/
    │   └── ENTSO-E_data_MODIFIED.png
    └── output/
        ├── Sensitive Analysis on Discomfort Cost
        └── Sensitive Analysis on flexibility factor
```
---

## Main Project Overview

The **main model** applies the flexible demand framework to the **Greek Day-Ahead Electricity Market (May 17, 2024)**, using real market data from **ENTSO-E**.  
To represent demand flexibility and consumer behavior, three additional fields were introduced in the input dataset:

- **α (Flexibility Parameter):** Maximum fraction of demand that can be shifted across hours  
- **Bd_sh_AWAY (Discomfort Cost – Away from preferred hours):** Penalty for reducing consumption in preferred periods  
- **Bd_sh_TOWARDS (Discomfort Cost – Towards preferred hours):** Penalty for increasing consumption in non-preferred periods  

---

### Model Functionality
The optimization model:
- **Determines hourly generation schedules** under market equilibrium  
- **Identifies shifted demand patterns** while maintaining total daily energy neutrality  
- **Maximizes social welfare**, defined as the sum of consumer and producer surplus  
- **Quantifies trade-offs** between market efficiency and consumer discomfort  

> ⚖️ **Energy Neutrality Constraint:**  
> Total daily demand remains constant — only the timing of consumption is adjusted across hours.

---

### Data and Privacy
For confidentiality reasons, the **full input Excel dataset** is not publicly shared.  
Instead, a **data screenshot** is provided to illustrate the input structure, showing:
- Baseline demand  
- Flexibility parameters (α)  
- Discomfort costs (Bd_sh_AWAY, Bd_sh_TOWARDS)  

This enables other users to **replicate the workflow** with their own data and explore flexibility scenarios.

---

### Insights
The model provides key insights into:
- How **temporal demand flexibility** influences market prices  
- The impact of **consumer discomfort costs** on participation and welfare  
- The **balance** between economic efficiency and behavioral realism  

It forms the foundation for comparative analyses across **European** and **U.S. market structures** within the thesis.

## Demo Overview

The demo provides a small-scale, self-contained illustration of the flexible demand model. It allows users to quickly explore how shifting demand (through the flexibility parameter α) affects market prices, generation schedules, and social welfare. The demo is ideal for educational purposes, testing different flexibility scenarios, or verifying the model workflow on a lightweight dataset. Results from the demo, including sensitivity analysis for α, are available in the Demo/output/ and Demo/output/sensitivity_analysis/ folder.

All demo-related files are contained in the `demo/` folder:
- `demo/code/` contains the main script `Eumarket_flexdemand_demo.py`.  
- `demo/input/` includes the sample input file `flexi.xlsx`.  
- `demo/output/` stores the demo results (`results_demo.xlsx`) and a `sensitivity_analysis/` folder with results from varying α.  

Users can run the demo to quickly observe the effect of demand flexibility on market outcomes and social welfare.

## Case Studies & Results  

This section presents the results of two sensitivity analyses conducted on the **Greek Day-Ahead Market (May 17, 2024)**:  
- **Case Study 1:** Flexibility Factor (α)  
- **Case Study 2:** Discomfort Costs (Bd_sh_AWAY / Bd_sh_TOWARDS)  

The purpose of these analyses is to examine how variations in demand flexibility and discomfort costs affect market outcomes, demand redistribution, and social welfare.

---

### Case Study 1 – Sensitivity Analysis on Flexibility Factor (α)

This study analyzes how increasing the flexibility parameter (α) — the maximum share of baseline demand that can be shifted across hours — influences market outcomes, electricity prices, and welfare.

---

#### Key Figures  
*(all figures generated from `main/output/Sensitive Analysis on flexibility factor/` folder)*  

**Figure 1 – Demand Curve under Different Flexibility Levels**  
<img width="832" height="477" alt="image" src="https://github.com/user-attachments/assets/11b9e9dd-59c0-4bd7-b857-ff28b5874754" />

**Figure 2 – Electricity Prices under Different Flexibility Levels**  
<img width="712" height="398" alt="image" src="https://github.com/user-attachments/assets/98c3a215-49bb-4304-bfd7-0c44744f68ab" />

**Figure 3 – Shifted Load Distribution under Different Flexibility Levels**  
<img width="867" height="472" alt="image" src="https://github.com/user-attachments/assets/21abca60-c918-40a7-84b1-c7131d478b9f" />

**Figure 4 – Producer Profits**  
<img width="866" height="490" alt="image" src="https://github.com/user-attachments/assets/09467277-2806-4af4-9bd9-bafa09399f4d" />

**Figure 5 – Consumer Utility**  
<img width="760" height="462" alt="image" src="https://github.com/user-attachments/assets/e6ad2a84-5f02-4b89-aa80-42d311bb5802" />

**Figure 6 – Social Welfare**  
<img width="872" height="442" alt="image" src="https://github.com/user-attachments/assets/3179b1f9-1325-4340-89cb-3d5026f3c634" />

#### Key Observations
- As **α increases**, demand becomes smoother across hours, reducing consumption peaks.  
- **Electricity prices** stabilize, showing reduced volatility and a flatter price profile.  
- **Shifted load** indicates redistribution of consumption from high-price to low-price hours.  
- **Producer profits decrease** as higher flexibility lowers market prices and reduces producer revenue.  
- **Consumer utility** increases, as more flexible consumption captures price advantages.  
- **Social welfare** improves significantly for α ≤ 0.5 and then stabilizes, showing diminishing marginal benefits.

#### Summary
The results confirm that moderate demand flexibility (**α ≈ 0.3–0.5**) yields the most efficient and stable market outcomes, achieving a balance between price smoothing and consumer comfort. Higher α values provide limited additional benefits.

---

### Case Study 2 – Sensitivity Analysis on Discomfort Costs (Bd_sh_AWAY / Bd_sh_TOWARDS)

This case study examines how discomfort costs — the penalties reflecting consumers’ aversion to shifting consumption — affect the degree of flexibility and overall market performance.

---

#### Key Figures  
*(all figures generated from `main/output/Sensitive Analysis on Discomfort Cost/` folder)*  

**Figure 1 – Demand Curve under Different Flexibility Levels**  
<img width="657" height="313" alt="image" src="https://github.com/user-attachments/assets/ece4a8f8-48b1-40c6-9141-9eda66bc944c" />

**Figure 2 – Electricity Prices under Different Flexibility Levels**  
<img width="788" height="388" alt="image" src="https://github.com/user-attachments/assets/e683f0f0-3248-415e-b2ee-f2235d997bcb" />

**Figure 3 – Shifted Load Distribution under Different Flexibility Levels**  
<img width="717" height="408" alt="image" src="https://github.com/user-attachments/assets/c1eeb4f5-83ef-468a-b6fe-99887c2d63bb" />

**Figure 4 – Producer Profits**  
<img width="662" height="368" alt="image" src="https://github.com/user-attachments/assets/ec6e447b-8bbf-4ff0-be79-c12f3b9b385d" />

**Figure 5 – Consumer Utility**  
<img width="677" height="377" alt="image" src="https://github.com/user-attachments/assets/f8d9bc7b-7405-4276-b7d1-391940cd9b5a" />

**Figure 6 – Social Welfare**  
<img width="651" height="367" alt="image" src="https://github.com/user-attachments/assets/4409baa0-6d92-40a8-9e1f-628c9a4336c2" />

#### Key Observations
- Increasing **discomfort costs** reduces the extent of load shifting and limits flexibility participation.  
- **Electricity prices** rise slightly as flexibility decreases.  
- **Producer profits** **increase**, as less flexible demand reduces competition on the supply side.  
- **Consumer utility** declines due to lower participation in flexibility schemes.  
- **Social welfare** decreases with higher Bd, illustrating the trade-off between **economic efficiency** and **consumer comfort**.  

#### Summary
At higher discomfort cost levels (**Bd > 15 €/MWh**), flexibility participation drops sharply, resulting in reduced welfare gains.  
An optimal range is observed for **Bd ≤ 10–15 €/MWh**, where both welfare and consumer satisfaction are balanced.

---

## General Model Summary

The model allows shifting part of the baseline demand from high-price hours to low-price hours without changing the total daily consumption. This shift is energy-neutral, maintaining total consumption over the day while adapting the timing of consumption to market conditions. By including parameters such as α (maximum fraction of shiftable demand) and optional discomfort costs, the model provides a flexible, general, and agnostic framework to study the effects of demand flexibility on market prices, generation schedules, and social welfare in the European day-ahead electricity market.

---

## Dependencies
- Python ≥ 3.8 
- pandas – Data handling
- numpy – Numerical operations
- pyomo – Optimization modeling
- xlsxwriter / openpyxl – Excel file export and read
- GLPK / CBC / Gurobi – Linear/Mixed-Integer solvers

---

## License / Credits

This project is provided for educational and research purposes. You are free to use, modify, and share it under the MIT License. See the LICENSE file for details.  

The code and models were developed as part of the **Diploma Thesis titled _"Analysis of the Impact of Flexible Demand on the Day-Ahead Wholesale Electricity Market"_**, conducted at the **University of Patras**, School of Electrical and Computer Engineering.  

The research focuses on the **optimization and market integration of flexible demand** in **modern Day-Ahead Wholesale Electricity Markets**, analyzing both **European (simple bidding)** and **U.S. (complex bidding)** market mechanisms. It examines how different clearing strategies can incorporate time flexibility of demand, assess their impact on market efficiency, system operation, and social welfare, and proposes optimal frameworks that account for temporal coupling constraints.

![Python Version](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

