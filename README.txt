ZENVY – AI Powered Payroll
Anomaly Detection Engine

1. Problem Statement
The objective of this project is to detect unusual payroll activities such as salary manipulation and fake overtime. Since labeled fraud data is not available, the system uses unsupervised learning to identify abnormal patterns in payroll records.

--------------------------------------------------

2. Algorithm Selection
Isolation Forest is used in this project because it does not require labeled data and is well suited for anomaly detection. It is efficient and works effectively with numerical payroll features such as salary and overtime values.

--------------------------------------------------

3. Features Used
The model is trained using the following features:
- Base Salary
- Overtime Ratio (overtime_pay / base_salary)
- Salary Ratio (total_salary / base_salary)

These features help in identifying abnormal salary increases and unusually high overtime payments.

--------------------------------------------------

4. Batch Pipeline
In the batch pipeline, payroll data is loaded from a CSV file and processed using feature engineering. The trained Isolation Forest model is then applied to detect anomalies, and the results are generated as an anomaly report for HR review.


--------------------------------------------------

5. Real-time Pipeline
For real-time processing, each new payroll entry is checked before approval. The entry goes through the same feature engineering steps and is evaluated by the trained model to decide whether it is normal or suspicious.


--------------------------------------------------

6. Concept Drift Handling
Payroll patterns can change over time due to salary hikes or policy changes. To handle this, the model is retrained periodically using recent payroll data so that it adapts to new trends and avoids incorrect anomaly detection.

--------------------------------------------------

7. Evaluation Strategy (No Labels)
Since labeled data is not available, evaluation is done by:
- Monitoring the percentage of records flagged as anomalies
- Manual HR review of flagged payroll entries
- Identifying repeated anomalies for the same employee as strong indicators of fraud

--------------------------------------------------

8. Deployment Plan
The model is trained offline using historical payroll data. After training, it can be deployed as an API to support real-time payroll validation during salary processing.

--------------------------------------------------

9. How to Run the Project

Step 1: Install required libraries
Open terminal in the project folder and run:
pip install pandas scikit-learn

Step 2: Run the anomaly detection script
Make sure payroll_data.csv and anomaly_detection.py are in the same folder.
Then run:
python anomaly_detection.py

Step 3: View results
- Detected payroll anomalies will be printed in the terminal
- A real-time payroll check result will also be displayed



