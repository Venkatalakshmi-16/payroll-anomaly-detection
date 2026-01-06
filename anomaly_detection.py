import pandas as pd
from sklearn.ensemble import IsolationForest

# -------------------------------
# 1. Load payroll data (Batch)
# -------------------------------
df = pd.read_csv("payroll_data.csv")

# -------------------------------
# 2. Feature Engineering
# -------------------------------
df["overtime_ratio"] = df["overtime_pay"] / df["base_salary"]
df["salary_ratio"] = df["total_salary"] / df["base_salary"]

features = df[["base_salary", "overtime_ratio", "salary_ratio"]]

# -------------------------------
# 3. Train Isolation Forest
# (Unsupervised Learning)
# -------------------------------
model = IsolationForest(
    n_estimators=100,
    contamination=0.2,   # ~20% anomalies expected
    random_state=42
)

model.fit(features)

# -------------------------------
# 4. Detect anomalies (Batch)
# -------------------------------
df["anomaly_flag"] = model.predict(features)

# -1 = anomaly, 1 = normal
anomalies = df[df["anomaly_flag"] == -1]

print("\n🚨 Detected Payroll Anomalies:\n")
print(anomalies[[
    "employee_id",
    "base_salary",
    "overtime_hours",
    "overtime_pay",
    "total_salary",
    "month"
]])

# -------------------------------
# 5. Real-time example
# -------------------------------
new_entry = pd.DataFrame({
    "base_salary": [30000],
    "overtime_pay": [15000],
    "total_salary": [45000]
})

new_entry["overtime_ratio"] = new_entry["overtime_pay"] / new_entry["base_salary"]
new_entry["salary_ratio"] = new_entry["total_salary"] / new_entry["base_salary"]

prediction = model.predict(
    new_entry[["base_salary", "overtime_ratio", "salary_ratio"]]
)

print("\nReal-time Check:")
if prediction[0] == -1:
    print("🚨 Anomaly detected in new payroll entry")
else:
    print("✅ Payroll entry is normal")
