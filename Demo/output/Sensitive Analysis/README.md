# Sensitivity Analysis – Impact of Flexibility Factor α

This folder contains results exploring how varying the flexibility parameter **α** (a_d in the model) affects market outcomes in the European day-ahead electricity market.

---

## 🔬 Key Observations

- **Demand Flexibility:** As α increases, more demand shifts from high-price to low-price periods, enabling better load distribution.

- **Price Stabilization:** Higher α leads to smoother hourly electricity prices, reducing volatility between time periods.

- **Producer Profit & Consumer Utility:** Consumer utility increases noticeably with higher flexibility, while producer profit also rises moderately.

- **Social Welfare:** Total social welfare improves and tends to stabilize once maximum flexibility is reached, demonstrating the efficiency gains from demand responsiveness.

- **Energy Neutrality:** The model ensures total consumption remains constant across scenarios, confirming that shifting does not alter overall demand.

---

## 📂 Folder Contents

- **sensitivity_results.xlsx** – Detailed results for different α values, including quantities sold/purchased, shifted demand, prices, producer profit, consumer utility, and social welfare.  
- Optional: charts or additional files showing trends for visual analysis.

---

## 📌 Notes

- Increasing α allows consumers to shift more demand, resulting in greater efficiency gains.  
- Beyond a certain α value, additional flexibility yields diminishing returns in social welfare and profit, indicating a **saturation effect**.  
- This sensitivity analysis is ideal for exploring the trade-off between flexibility and market outcomes.

---

## 📌 Summary

Increasing the flexibility parameter **α** clearly demonstrates the benefits of demand responsiveness. Higher α values enable more shifting of consumption to lower-price periods, which:

- Stabilizes market prices  
- Increases consumer utility  
- Boosts producer profit  
- Improves total social welfare  

Beyond a certain level, the gains tend to plateau, highlighting the saturation effect of additional flexibility.
