import pandas as pd
import os

#define path to CSV files
input = 'C:\\Users\\grant\\OneDrive\\Desktop\\Coding\\Grand Tour Portfolio Project'
output = 'C:\\Users\\grant\\OneDrive\\Desktop\\Coding\\Grand Tour Portfolio Project\\GrandTour_All.csv'

merged_data = pd.DataFrame()

for filename in os.listdir(input):
    if filename.endswith(".csv"):
        file_path = os.path.join(input, filename)
        df = pd.read_csv(file_path)
        merged_data = merged_data.append(df, ignore_index=True)


merged_data.to_csv(output, index = False)
