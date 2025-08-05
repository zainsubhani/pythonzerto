#1 import data 
#2 clean the data 
#3 split the data trainingset/test set
#4 create a model import algo like use library
#5 check the output
#6 improve

import kagglehub
import pandas as pd
import os
import seaborn as sns;
import matplotlib.pyplot as plt


# Download the dataset
path = kagglehub.dataset_download("bryanb/fifa-player-stats-database")

print("Path to dataset files:", path)

# Find CSV files in the downloaded path
csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]

# Load the first CSV file (or loop over all)
df = pd.read_csv(os.path.join(path, csv_files[0]))
#print(df.describe)
df1=pd.DataFrame(df,columns=['Name','Wage','Value'])
def parse_currency(value):
    if isinstance(value, str):
        value = value.replace('€', '').strip()
        if value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('K'):
            return float(value[:-1]) * 1_000
        else:
            try:
                return float(value)
            except:
                return None
    return None


df1['Value'] = df1['Value'].apply(parse_currency)
df1['Wage'] = df1['Wage'].apply(parse_currency)
df1['Difference'] = df1['Value'] - df1['Wage']
sns.scatterplot(data=df1, x='Wage', y='Value')
plt.title('Wage distribution by Value category')
plt.show()


# print(df1.head())


