# Greek Day-Ahead Electricity Market Sensitivity Analysis (17/05/2024)

This repository contains the results of a sensitivity analysis performed on the Greek day-ahead electricity market. The analysis focuses on two key parameters:

- **Flexibility Factor (α)** – the flexibility of each buyer in shifting energy consumption between periods.  
- **Discomfort Cost** – the cost perceived by consumers when their flexible loads are shifted.

---

## Folder Structure

```bash
└── main/
    ├── code/
    │   └── GR-MARKET_FLEXDEMAND.py
    ├── input/
    │   └── ENTSO-E_data_MODIFIED.png
    └── output/
        ├── Sensitive Analysis on Discomfort Cost
        └── Sensitive Analysis on flexibility factor
```


* **Sensitive Analysis on Flexibility Factor**:  
  * Includes charts and tables showing the impact of different α values on market outcomes.
* **Sensitive Analysis on Discomfort Cost**:  
  * Includes charts showing the effect of different discomfort costs on consumer welfare and social surplus.

---

## Charts and Analysis

* **Total Demand Curve**
  * Shows the total accepted demand for each hour of the day for different α values.
  * Higher flexibility (α) allows consumers to shift loads from peak hours to periods with abundant renewable generation, smoothing the demand curve.

* **Electricity Prices**
  * Illustrates hourly electricity prices for varying α values.
  * As α increases, price fluctuations are reduced.
  * For α ≥ 0.8, prices stabilize, indicating a balance between demand and supply.

* **Producers’ Profit**
  * Displays hourly and total profit for electricity producers under different α values.
  * Initially, higher flexibility reduces profit due to increased production cost, but profit stabilizes for α ≥ 0.6.

* **Consumers’ Welfare**
  * Shows consumer welfare throughout the day.
  * Increased flexibility improves welfare during peak hours.
  * For α ≥ 0.6, welfare gains plateau.

* **Social Surplus**
  * Shows the total social surplus (sum of producers’ profit and consumers’ welfare).
  * Social surplus increases with higher α, reaching its maximum once full system balance is achieved.

* **Net Demand Curve and Uniformity Coefficient**
  * Presents the approximated net demand curve (total demand minus renewable generation) and its uniformity coefficient.
  * As α increases, the curve flattens and the uniformity coefficient improves.
  * Indicates better utilization of renewable generation and reduced system costs.

* **Sensitivity Analysis on Discomfort Costs**
  * Evaluates the impact of different discomfort costs on market outcomes.
  * **Total Demand Curve**  
    * As discomfort costs increase, consumers are less willing to shift loads.
    * This leads to more pronounced peaks in demand.
  * **Electricity Prices**  
    * Higher discomfort costs increase price volatility, especially during peak hours.
    * Lower discomfort costs smooth prices and improve market efficiency.
  * **Producers’ Profit**  
    * Profit is higher when consumers face higher discomfort costs, as less load shifting allows for more stable production schedules.
    * Lower discomfort costs may reduce profit due to increased load flexibility.
  * **Consumers’ Welfare**  
    * Welfare decreases as discomfort costs increase because consumers are less able to optimize their load shifting.
    * Welfare is maximized when discomfort costs are low.
  * **Social Surplus**  
    * Social surplus is sensitive to discomfort costs: higher discomfort reduces overall surplus.
    * Balancing flexibility and discomfort costs is key to maximizing societal benefits.

---

## Summary of Key Observations

* Gradual increase in α smooths demand and prices.
* Producers’ profit initially decreases but stabilizes at higher α values.
* Consumers’ welfare increases, particularly during peak hours.
* Social surplus reaches a maximum as flexibility allows optimal use of renewable resources.
* Fixing the baseline accepted quantity limits total social gains compared to allowing adaptive demand with increasing α.
* Increasing discomfort costs reduces consumer flexibility, leading to higher price volatility and lower social surplus.

---

This README provides a structured overview of all output charts, making it easier to interpret the effects of flexibility and discomfort costs on the Greek electricity market.
