# Flexible Demand in the European Day-Ahead Electricity Market 

This project focuses on the role of flexible demand in the European day-ahead wholesale electricity market, with a detailed case study for the Greek market on May 17, 2024. The main feature of the model is that it is general and agnostic, meaning it does not rely on specific technical characteristics of individual loads or consumers. This provides high flexibility in analysis and allows its application across different scenarios and markets without requiring detailed technical data for each load.

## 🔑 Key Features of the General Model

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

## 🌟 Benefits of the General and Agnostic Approach
- Applicability across multiple markets: Greece, Europe, or other regions without detailed load information
- Policy analysis capabilities: Suitable for system operators, regulators, or governments to evaluate the impact of flexible demand on market stability and social welfare
- Educational and research tool: Ideal for teaching, research simulations, and scenario analysis

## 📌 Model Overview

The European market is typically cleared based on hourly price-quantity bids, where participants submit their supply and demand offers for each hour. To incorporate demand flexibility, the model allows shifting part of the demand from high-price hours to low-price hours without changing the total daily energy consumption. This shift is energy-neutral, meaning total consumption over the day remains constant, but the timing of consumption can adapt to market conditions.

## 🔎 Key Elements  

- **Demand Flexibility Parameter (αd):** Maximum fraction of baseline demand that can be shifted across hours.  
- **Discomfort Costs:** Optional penalties that model the inconvenience of shifting consumption from preferred hours.  
- **Objective:** Maximize **social welfare**, defined as the sum of consumer surplus and producer surplus.  
- **Energy Neutrality:** Ensures total daily consumption remains constant.  
- **Sensitivity Analysis:** Study how varying α affects market outcomes, prices, and social welfare.

---

## 🏗️ Project Structure


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

## 📄 Main Project Overview

The main project demonstrates the flexible demand model using real market data from the Greek day-ahead electricity market for May 17, 2024. To capture demand flexibility and consumer preferences, three additional columns were added to the input dataset:
- Flexibility parameter (α)
- Optional discomfort costs for shifting consumption

For privacy reasons, the full input Excel file cannot be shared. Instead, a screenshot of the first few rows of the dataset is provided for reference, illustrating the structure of the data, the flexibility parameters, and the cost information. This allows users to replicate the workflow with their own data if desired.

The model optimizes hourly generation schedules, shifted demand, and social welfare, respecting energy neutrality constraints, providing insights into how flexible demand affects the Greek day-ahead market.

## 🧪 Demo Overview

The demo provides a small-scale, self-contained illustration of the flexible demand model. It allows users to quickly explore how shifting demand (through the flexibility parameter α) affects market prices, generation schedules, and social welfare. The demo is ideal for educational purposes, testing different flexibility scenarios, or verifying the model workflow on a lightweight dataset. Results from the demo, including sensitivity analysis for α, are available in the Demo/output/ and Demo/output/sensitivity_analysis/ folder.


## 📌 Summary

The model allows shifting part of the baseline demand from high-price hours to low-price hours without changing the total daily consumption. This shift is energy-neutral, maintaining total consumption over the day while adapting the timing of consumption to market conditions. By including parameters such as α (maximum fraction of shiftable demand) and optional discomfort costs, the model provides a flexible, general, and agnostic framework to study the effects of demand flexibility on market prices, generation schedules, and social welfare in the European day-ahead electricity market.

---

## 📚 Dependencies
- Python ≥ 3.8 
- pandas – Data handling
- numpy – Numerical operations
- pyomo – Optimization modeling
- xlsxwriter / openpyxl – Excel file export and read
- GLPK / CBC / Gurobi – Linear/Mixed-Integer solvers

  
## 📄 License / Credits

This project is provided for educational and research purposes. You are free to use, modify, and share it under the MIT License. See the LICENSE file for details.  

The code and models were developed as part of the **Diploma Thesis titled _"Analysis of the Impact of Flexible Demand on the Day-Ahead Wholesale Electricity Market"_**, conducted at the **University of Patras**, School of Electrical and Computer Engineering.  

The research focuses on the **optimization and market integration of flexible demand** in **modern Day-Ahead Wholesale Electricity Markets**, analyzing both **European (simple bidding)** and **U.S. (complex bidding)** market mechanisms. It examines how different clearing strategies can incorporate time flexibility of demand, assess their impact on market efficiency, system operation, and social welfare, and proposes optimal frameworks that account for temporal coupling constraints.

![Python Version](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

