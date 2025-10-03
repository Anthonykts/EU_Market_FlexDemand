# Main Flexible Demand Model

This folder contains the main script for the **EU Day-Ahead Electricity Market**, incorporating **flexible demand** and **discomfort costs**.

---

## 📂 File

- **`GR-MARKET_FLEXDEMAND.py`**: Main optimization script using **Gurobi**.

---

## 1. Overview

The model incorporates **flexible demand**, where consumers can shift their electricity usage over time, reducing consumption during high-price hours and increasing it during low-price hours. The objective is **maximizing social welfare**, considering production costs and discomfort from load shifting.

### **Key Features**

- ✅ Supports **baseline demand** and **flexible shifting**  
- ✅ Includes **discomfort costs** due to temporal load shifting  
- ✅ Allows **sensitivity analysis** regarding flexibility degree and discomfort costs  
- ✅ **Generic model**, suitable for a large number of consumers without detailed technical load parameters  

---

## 2. Data Loading

- Collects market data: **buy/sell offers, maximum quantities, prices, and flexibility factors**  
- Models flexibility as the ability to **shift demand across different time periods**  

### **Data Example**

The structure of the input data is illustrated below (screenshot or table example):  

![Data Screenshot](https://github.com/Anthonykts/EU_Market_FlexDemand/blob/main/main/input/MAIN_INPUT_modified.png)  

## 3. Model Analysis and Structure

### 3.1 Theoretical Framework

- Traditional utility functions are **increasing, convex, and quadratic**, leading to decreasing marginal utility  
- Low demand elasticity causes **price spikes** and allows producers to exercise **market power**  
- **Time-based flexibility** is more realistic than price elasticity: consumers shift loads from high-price hours to low-price hours  

**Flexible demand is represented through:**

- Baseline demand  
- Temporal shift decision variables  

- Temporal shifts are **energy-neutral**, i.e., total daily consumption remains unchanged  
- Discomfort costs represent **consumer dissatisfaction** when loads are shifted in time  

---

### 3.2 European Market Model

- Solves the **market clearing and pricing problem**, considering buyers' ability to shift demand over time  
- Participants submit **multi-parameter offers**: price, maximum quantity, flexibility degree, and discomfort costs  
- The market operator clears the offers to **maximize social welfare**  

---

### 3.3 Assumptions

- The market clears for the **full 24-hour horizon simultaneously**  
- Offers fully reflect actual **economic and technical characteristics**  
- Fixed number of offers per **time period**  
- Temporal shifting affects **consumer satisfaction** and is represented through **discomfort costs**  

---

## 4. Requirements

- **Python >= 3.8**  
- **pandas**  
- **gurobipy** (requires a **Gurobi license**)  

