#1 import data 
#2 clean the data 
#3 split the data trainingset/test set
#4 create a model import algo like use library
#5 check the output
#6 improve

import kagglehub
import pandas as pd
import os

# Download the dataset
path = kagglehub.dataset_download("bryanb/fifa-player-stats-database")

print("Path to dataset files:", path)

# Find CSV files in the downloaded path
csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]

# Load the first CSV file (or loop over all)
df = pd.read_csv(os.path.join(path, csv_files[0]))

print(df.head())
