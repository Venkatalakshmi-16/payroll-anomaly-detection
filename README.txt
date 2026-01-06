ZENVY – AI Powered Payroll
Anomaly Detection Engine

1. The Problem Situation
The aim of this project is the automatic identification of unusual payroll transactions like manipulated salaries and falsified overtime. With limited information on fraud available, the system will employ unsupervised learning techniques to find anomalies within the company's payroll database.

--------------------------------------------------

2. Algorithm Selection
This project used Isolation Forest for anomaly detection because it can be used on unlabelled data. Numerous payroll functions, including salaries and overtime, work effectively with it.

--------------------------------------------------

3. Features Used
The training of the model was carried out on the basis of the following criteria:
- Base Salary
Time worked overtime as a percentage of total working hours (overtime hours / total hours worked)
This job uses the following salary ratio to compare the total salaries of the employees to the base salary. 

total_salary / base_salary

The system identifies unusually high overtime payments as well as abnormal increases in salaries.

--------------------------------------------------

4. Batch Pipeline
The payroll data from a csv file is first loaded into the pipeline and then undergoes feature engineering. Following the data profiling and cleansing, an Isolation Forest model has been trained. Utilising this model, anomalies are detected and a report detailing these anomalies is generated. This report is subsequently reviewed by the HR department.

Flow:
Payroll CSV → Feature Engineering → Isolation Forest → Anomaly Report

--------------------------------------------------

5. Real-time Pipeline
Each new payroll entry has to be checked in real time before it is approved. After undergoing feature engineering, the new entry is passed through the same neural network for evaluation. The model classifies the transaction as either legitimate or suspicious.

Flow:
New Payroll Entry → Feature Engineering → Trained Model → Flag / Allow

The 1980s and 1990s

6. Concept Drift Handling
Changes in salary scales or employee benefits can lead to shifting payroll patterns. Periodically, the model is re-trained on the most recent data from payroll to prevent anomalies from being incorrectly detected due to changing trends.

--------------------------------------------------

7. Evaluation Strategy (No Labels)
In the absence of a labelled dataset, evaluation is performed by comparing the performance of the system with that of a model with the same architecture but which has been trained on a large database of text.
- Monitoring the percentage of records flagged as anomalies
- Manual HR review of flagged payroll entries
Employing repeat anomalies in the data associated with a single employee as significant indicators of potential fraud schemes.

--------------------------------------------------

8. Deployment Plan
Training of the model occurs using a review of historical payroll information. Following training, the model can be put to use through an application programming interface that facilitates immediate, real-time payroll validation.

--------------------------------------------------

9. How to Run the Project

Step 1: Install required libraries
In your terminal navigate to the project's directory and then run:
pip install pandas scikit-learn

The script was run manually. First, the expert ran the anomaly detection script to identify the transactions that needed to be looked at by the fraud detection software.
Please ensure that both payroll_data.csv and anomaly_detection.py are located in the same working directory.
Then run:
python anomaly_detection.py

Step 3: View results
Payroll discrepancies will be displayed on the screen.
The current real time status of payroll checks will be displayed.



