import requests
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Fetch data from the API
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print("Failed to fetch data:", response.status_code)
    exit()

# Step 2: Convert JSON to DataFrame
df = pd.DataFrame(data)

# Step 3: Select relevant columns
df = df[['country', 'cases', 'todayCases', 'deaths', 'todayDeaths', 'recovered', 'active', 'critical']]

# Step 4: Sort countries by total cases
df_sorted = df.sort_values(by='cases', ascending=False)

# Display top 10 countries with most cases
print("\nTop 10 countries with most COVID-19 cases:\n")
print(df_sorted.head(10))

# Step 5: Plotting top 10 countries by total cases
top_10 = df_sorted.head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_10['country'], top_10['cases'], color='skyblue')
plt.title('Top 10 Countries by Total COVID-19 Cases')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 6: Optional – Save Data to CSV
df_sorted.to_csv("covid_data_global.csv", index=False)
print("\nData saved to 'covid_data_global.csv'")
