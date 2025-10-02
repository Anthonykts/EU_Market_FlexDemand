Flexible Demand in the European Day-Ahead Electricity Market 

This project focuses on the role of flexible demand in the European day-ahead wholesale electricity market, with a detailed case study for the Greek market. The aim is to model how temporal demand flexibility can affect market prices, supply-demand balance, and overall social welfare.

Model Overview

The European market is typically cleared based on hourly price-quantity bids, where participants submit their supply and demand offers for each hour. To incorporate demand flexibility, the model allows shifting part of the demand from high-price hours to low-price hours without changing the total daily energy consumption. This shift is energy-neutral, meaning total consumption over the day remains constant, but the timing of consumption can adapt to market conditions.

Key Features

Demand Flexibility Parameter (αd): Represents the maximum fraction of baseline demand that can be shifted across hours.

Discomfort Costs: Optional penalties that model the inconvenience of shifting consumption from preferred hours.

Objective: Maximize social welfare, defined as the sum of consumer surplus and producer surplus.

## 🏗️ Project Structure
```bash
EU_Market_FlexDemand/
│
├── README.md
├── LICENSE
│
├── demo/
│ ├── code/
│ │ └── demo.py
│ ├── input/
│ │ └── flexi.xlsx
│ ├── output/
│ │ └── results_demo.xlsx
│ └── README.md
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
