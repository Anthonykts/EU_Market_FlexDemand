# Demo – Flexible Demand in the European Day-Ahead Electricity Market

This folder contains a small-scale demonstration of a flexible demand model for the European day-ahead electricity market.
The demo allows users to quickly run the optimization and see how demand flexibility affects market prices, generation schedules, and social welfare.

The demo is designed to be lightweight and self-contained, ideal for educational purposes or for testing flexibility scenarios on small datasets.


## 📌 Overview
Flexible demand in electricity markets allows consumers to shift their electricity consumption in time, responding to price signals. This demo illustrates:

- How shifting demand from high-price to low-price periods can impact the market.

- How energy neutrality ensures total consumption remains constant.

- The effect on social welfare, calculated as the sum of consumer utility and producer profit.

- How optional discomfort costs can influence shifting decisions.

The model is implemented using Pyomo and can be solved using open-source solvers such as GLPK or CBC.

##  🔑 Key Features

- Flexible demand shifting across multiple time periods
- Energy-neutral adjustments – total daily consumption remains constant
- Optional discomfort costs – simulate consumer preferences for convenience
- Social welfare calculation – sum of consumer utility and producer profit

 ## 📊 Example Outputs

- Shifted Demand – visualizing consumption movement from high-price to low-price hours
- Market Prices – hourly clearing prices considering flexible demand
- Social Welfare Impact – comparison with baseline scenario (no flexibility)
- Producer Profit – how revenues change with demand flexibility
- Consumer Utility – quantifying satisfaction from shifting consumption

💡 Notes & Tips

- The demo uses a small dataset for fast computation; for larger studies, update the input Excel file.
- Ensure your solver (GLPK) is installed and accessible in your system path.
- Adjust flexibility parameters (a_d, B_d_sh_away, B_d_sh_towards) in flexi.xlsx to explore different scenarios.

## 🗂 Folder Structure
```bash
demo/
├── code/
│ └── demo.py Main script to run the demo
├── input/
│ └── flexi.xlsx Sample input data
├── output/
│ ├── results_demo.xlsx Demo results
│ └── sensitivity_analysis/ Optional: results from sensitivity runs
└── README.md This file
```
---

## 🚀 Running the Project

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```
2. Run the demo optimization:
```bash
python scripts/Eumarket_flexdemand_demo.py
```
3. View the results
```bash
output/eu_market_results.xlsx
```
## 📄 License / Credits

This demo is provided for educational and illustrative purposes.
You are free to use, modify, and share it under the MIT License. See the LICENSE file for details.
The model and code were developed as part of a flexible demand study in the European day-ahead electricity market.

## 🔬 Sensitivity Analysis

The output/sensitivity_analysis/ folder contains results from varying the flexibility parameter α.
- A separate README.md inside that folder explains how increasing or decreasing α affects demand shifting, market prices, and social welfare.
- To run your own sensitivity analysis, modify a_d in flexi.xlsx and rerun the demo script.

## 📚 Dependencies

The project requires the following Python packages and tools:

- **Python ≥ 3.8** – Recommended for compatibility with all dependencies.  
- **pandas** – For reading, writing, and manipulating Excel and tabular data.  
- **numpy** – For numerical operations and array handling.  
- **pyomo** – To formulate and solve optimization models.  
- **xlsxwriter** – For exporting results to formatted Excel files.  
- **openpyxl** – For reading and writing Excel `.xlsx` files.  
- **GLPK** – Open-source solver for linear and mixed-integer programming (alternative to Gurobi).  


