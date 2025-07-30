# 📈 Blockhouse Quantitative Research Internship Assessment

---

## 🧠 Objective

This assessment demonstrates my ability to:
- Analyze high-frequency trade data across multiple tickers (CRWV, FROG, SOUN)
- Model **temporary market impact** using signed trade volume
- Design a **mathematical execution framework** to minimize trading cost
- Build clear and reproducible research code with strong visualizations

---

## 🔧 Methodology

### 1. 📊 Market Impact Modeling
- Parsed minute-level trade data
- Computed signed volume: `size × (+1 for Buy / -1 for Sell)`
- Aggregated trades into 1-minute buckets
- Modeled price movement as a function of signed volume using **linear regression**
- Interpreted slope (β) as the temporary market impact coefficient

### 2. 🧮 Optimal Execution Strategy
- Developed a trading framework using:
  - Linear temporary impact
  - Mean-variance cost optimization
  - Volatility-aware execution schedule
- Applied theoretical models such as:
  - **Almgren–Chriss framework**
  - VWAP-based slicing

---
### 📈 Sample Visualization
📍 Each plot shows the relationship between signed trade volume and short-term price movement, capturing market impact.

## 📈 Visual Results

### 🔹 CRWV: Market Impact Plot  
![CRWV Market Impact](https://github.com/amrita40/BlackHouse_Internship_Assessment/blob/main/crwv_result.png)

---

### 🔹 FROG: Market Impact Plot  
![FROG Market Impact](https://github.com/amrita40/BlackHouse_Internship_Assessment/blob/main/frog_result.png)

---

### 🔹 SOUN: Market Impact Plot  
![SOUN Market Impact](https://github.com/amrita40/BlackHouse_Internship_Assessment/blob/main/soun_result.png)


### 📌 Key Insights
Ticker	Market Impact (β)	Interpretation
CRWV	+0.0014 (approx)	Price positively correlates with buy pressure
FROG	+0.0023 (approx)	Higher sensitivity to signed volume
SOUN	+0.0019 (approx)	Moderate impact strength
## 📂 Repository Structure


### 🧠 Skills Demonstrated
📊 Quantitative modeling

📈 Market microstructure analysis

💻 Python, pandas, seaborn, sklearn

🧮 Execution strategy optimization

### 📄 Research communication & reporting


├── crwv_analysis.ipynb         
├── frog_analysis.ipynb        
├── soun_analysis.ipynb     
├── Datasets                   
├── report.md                   
├── README.md                   

