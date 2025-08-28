# COVID-19 Global Data Tracker
# ---------------------------------
# This script fetches real-time COVID-19 data, analyzes it,
# and visualizes key statistics using Pandas, Matplotlib, and Seaborn.

# Step 0: Import Libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Fetch COVID-19 Global Data
try:
    url = "https://disease.sh/v3/covid-19/all"
    response = requests.get(url)
    response.raise_for_status()  # Raise error if request failed
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    exit()

# Extract relevant fields
total_cases = data['cases']
total_deaths = data['deaths']
total_recovered = data['recovered']
active_cases = data['active']
critical_condition = data['critical']
total_tests = data['tests']
population = data['population']

# Step 2: Create DataFrame
df = pd.DataFrame({
    'Total Cases': [total_cases],
    'Total Deaths': [total_deaths],
    'Total Recovered': [total_recovered],
    'Active Cases': [active_cases],
    'Critical Condition': [critical_condition],
    'Total Tests': [total_tests],
    'Population': [population]
})

# Calculate additional metrics
df['Recovery Rate (%)'] = (df['Total Recovered'] / df['Total Cases']) * 100
df['Death Rate (%)'] = (df['Total Deaths'] / df['Total Cases']) * 100

# Display Data
print("Global COVID-19 Statistics:\n")
print(df)

# Step 3: Visualizations

# 1️⃣ Pie Chart – Cases Distribution
labels = ['Total Cases', 'Total Deaths', 'Total Recovered']
sizes = [total_cases, total_deaths, total_recovered]
colors = ['gold', 'red', 'lightgreen']

plt.figure(figsize=(7,7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('COVID-19 Global Cases Distribution')
plt.axis('equal')
plt.show()

# 2️⃣ Bar Chart – Active vs Critical Cases
categories = ['Active Cases', 'Critical Condition']
values = [active_cases, critical_condition]

plt.figure(figsize=(8,6))
plt.bar(categories, values, color=['blue', 'orange'])
plt.title('Active vs Critical COVID-19 Cases')
plt.ylabel('Number of Cases')
plt.show()

# 3️⃣ Line Chart – Sample Trend Over Time
# Replace with actual historical data if available
dates = ['2025-01-01', '2025-02-01', '2025-03-01', '2025-04-01']
cases = [100000, 150000, 200000, 250000]

plt.figure(figsize=(10,6))
plt.plot(dates, cases, marker='o', linestyle='--', color='b')
plt.title('COVID-19 Cases Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 4️⃣ Scatter Plot – Active vs Critical Cases (Seaborn)
plt.figure(figsize=(6,4))
sns.scatterplot(x=[active_cases], y=[critical_condition], color='red', s=100)
plt.title('Active vs Critical Cases')
plt.xlabel('Active Cases')
plt.ylabel('Critical Condition')
plt.show()

# End of Script


