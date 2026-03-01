# 💳 Financial Impulse Behaviour Detection
### Behavioural Analytics Hackathon Submission

---

## 📌 Problem Statement

Young individuals often exhibit impulsive financial behaviour due to emotional or situational triggers. The objective of this project is to design a behavioural analytics system that:

- Detects impulsive spending patterns
- Predicts high-risk upcoming spending behaviour
- Generates an Impulse Risk Score (0–100)
- Provides behavioural insights and personalized intervention strategies

---

# 🗂 Dataset Information

## Dataset Type
**Synthetic Dataset**

## Why Synthetic?

Real-world financial behavioural datasets are:
- Highly sensitive
- Not publicly available due to privacy regulations
- Protected under financial compliance laws

Since no open behavioural transaction dataset was available, a synthetic dataset was generated to simulate realistic spending behaviour patterns.

---

# ⚙️ Dataset Generation Methodology

The dataset was generated using Python with controlled behavioural assumptions.

### 📊 Configuration

- Number of Users: 300
- Total Transactions: 10,000
- Time Period: Jan 2025 – Mar 2025
- Merchant Categories:
  - Groceries
  - Fashion
  - Electronics
  - Gaming
  - Food Delivery
  - Travel
  - Entertainment
  - Utilities
- Payment Methods:
  - UPI
  - Debit Card
  - Credit Card
  - Wallet

---

## 🧠 Behavioural Logic Injected

The synthetic data simulates impulsive financial behaviour using the following rules:

### 1️⃣ End-of-Month Spending Surge
- Transactions after the 25th of the month have increased spending probability.
- Simulates salary-cycle behaviour.

### 2️⃣ Late-Night Emotional Spending
- Transactions between 10PM – 2AM have increased impulse probability.
- Higher effect for discretionary categories (Gaming, Fashion, Food Delivery).

### 3️⃣ Spending Spikes
- Random 5% transactions amplified by 2x–4x.
- Simulates emotional or unplanned purchases.

### 4️⃣ Weekend Behavioural Variation
- Increased discretionary category probability on weekends.

---

# 📈 Dataset Features

### Transaction-Level Features

- `user_id`
- `transaction_timestamp`
- `transaction_amount`
- `merchant_category`
- `payment_method`
- `day_of_week`
- `hour`
- `is_weekend`
- `month`
- `day`
- `days_to_month_end`

---

# 🧮 Behavioural Feature Engineering

Transaction data was aggregated at the **user level** to derive behavioural indicators:

- Transaction Frequency
- Average Spend
- Spend Variability (Standard Deviation)
- Maximum Spend
- Weekend Spending Ratio
- Night Transaction Ratio
- End-of-Month Spending Ratio
- Spending Spike Ratio

---

# 🎯 Target Variable (Impulse Risk Label)

A rule-based scoring system was used to create ground-truth labels:

- Low Risk
- Medium Risk
- High Risk

Risk levels were assigned based on:
- Night transaction ratio
- End-of-month spending ratio
- Spending spike ratio
- Weekend spending ratio

This ensures behavioural interpretability before ML training.

---

# 🤖 Model Development

Two models were trained:

## 1️⃣ Logistic Regression
- Baseline linear classifier
- Accuracy: ~85%

## 2️⃣ Random Forest Classifier
- Final selected model
- Captures nonlinear behavioural interactions
- Accuracy: ~98%

---

# 📊 Risk Scoring Mechanism

The system outputs:

Impulse Risk Score =  
Probability of High-Risk Class × 100

Score Interpretation:
- 0–40 → Low Risk
- 40–70 → Medium Risk
- 70–100 → High Risk

---

# 📈 Behavioural Insights

Feature importance analysis shows:

- Spending Spike Ratio is the strongest predictor
- Weekend Spending Ratio influences impulsive behaviour
- Night Transactions significantly impact risk
- End-of-Month behaviour correlates with salary cycle effects

---

# 🖥 Streamlit Dashboard

The dashboard allows:
- Manual behavioural input
- Real-time risk prediction
- Risk probability breakdown
- Behavioural driver visualization
- Personalized intervention recommendations

Run locally:

```bash
pip install -r requirements.txt
python -m streamlit run streamlit_app.py