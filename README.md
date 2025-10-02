# Flexible Demand in the European Day-Ahead Electricity Market

This project focuses on the role of flexible demand in the European day-ahead wholesale electricity market, with a detailed case study for the Greek market. The aim is to model how temporal demand flexibility can affect market prices, supply-demand balance, and overall social welfare.

---

## 📌 Model Overview

The European market is typically cleared based on hourly price-quantity bids, where participants submit their supply and demand offers for each hour. To incorporate demand flexibility, the model allows shifting part of the demand from high-price hours to low-price hours **without changing the total daily energy consumption**. This shift is **energy-neutral**, meaning total consumption over the day remains constant, but the timing of consumption can adapt to market conditions.

### Key Features

- **Demand Flexibility Parameter (αd):** Maximum fraction of baseline demand that can be shifted across hours.  
- **Discomfort Costs:** Optional penalties that model the inconvenience of shifting consumption from preferred hours.  
- **Objective:** Maximize **social welfare**, defined as the sum of consumer surplus and producer surplus.  
- **Energy Neutrality:** Ensures total daily consumption remains constant.  
- **Sensitivity Analysis:** Study how varying α affects market outcomes, prices, and social welfare.

---

## 🏗️ Project Structure

```bash
EU_Market_FlexDemand/
│
├── README.md
├── LICENSE
│
demo/
├── code/
│   └── Eumarket_flexdemand_demo.py
├── input/
│   └── flexi.xlsx
├── output/
│   ├── eu_market_results.xlsx
│   └── sensitivity_analysis/
└── README.md
│
└── main/
├── code/
│ ├── main.py
│ └── utils.py
├── input/
│ └── ENTSO-E_data_MODIFIED.png
├── output/
│ ├── results.xlsx
│ └── plots/
└── README.md
```
---
## Main Project Overview

The main project demonstrates the flexible demand model using real market data from the Greek day-ahead electricity market for a selected day (May 17, 2024). To capture demand flexibility and consumer preferences, three additional columns were added to the input dataset: the flexibility parameter α and optional discomfort costs for shifting consumption.

For privacy reasons, the full input Excel file cannot be shared. Instead, a screenshot of the first few rows of the dataset is provided for reference, illustrating the structure of the data, the flexibility parameters, and the cost information. This allows users to understand the input format and replicate the workflow with their own data if desired.

The model uses these inputs to optimize hourly generation schedules, shifted demand, and social welfare while respecting energy neutrality constraints, providing insights into how flexible demand affects the Greek day-ahead market.

## Demo Overview

The demo provides a small-scale, self-contained illustration of the flexible demand model. It allows users to quickly explore how shifting demand (through the flexibility parameter α) affects market prices, generation schedules, and social welfare. The demo is ideal for educational purposes, testing different flexibility scenarios, or verifying the model workflow on a lightweight dataset. Results from the demo, including sensitivity analysis for α, are available in the Demo/output/ and Demo/output/sensitivity_analysis/ folder.


## 📚 Dependencies
- Python ≥ 3.8 
- pandas – Data handling
- numpy – Numerical operations
- pyomo – Optimization modeling
- xlsxwriter / openpyxl – Excel file export and read
- GLPK / CBC / Gurobi – Linear/Mixed-Integer solvers

## 📄 License / Credits

This project is provided for educational and research purposes. You are free to use, modify, and share it under the MIT License. See the LICENSE file for details.
The code and models were developed as part of a study on flexible demand in the European day-ahead electricity market.
