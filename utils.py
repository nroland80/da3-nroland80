import numpy as np
import pandas as pd
#dataframe empty with strings used
# i will be udsing pd.to_datetime to se eif this resoves the issue
#I will turn the date from the .csv file into dataframes
#tbh I am only doing the dataframe stuff as I keep getting empty tables
youtube_df = pd.read_csv("youtube_analytics_2-11-24_2-9-25.csv", parse_dates=["Date"])
days_df = pd.read_csv("days_of_week_2-11-24_2-9-25.csv", parse_dates=["Date"])

#many online examples say to set inplcae as true for set_index
youtube_df.set_index("Date", inplace=True)
days_df.set_index("Date", inplace=True)
#will attempt to convert to datetime for user input
start_date = pd.to_datetime(input("Enter start date (YYYY-MM-DD): "))
end_date = pd.to_datetime(input("Enter end date (YYYY-MM-DD): "))

df_slice = youtube_df.loc[start_date:end_date].copy()

#print(df_slice): now working as intended with datetime fix: will follow up during office hours

#sum, mean, standard deviation, median, smallest value, and largest value

def write_to_csv(df_slice):
    sum_slice = df_slice.sum()      # Sum of each column
    mean_slice = df_slice.mean()     # Mean of each column
    std_slice = df_slice.std()      # Standard deviation of each column
    med_slice = df_slice.median()   # Median of each column
    min_slice = df_slice.min()      # Minimum value of each column
    max_slice = df_slice.max()      # Maximum value of each column
    
    analytics_df = pd.DataFrame({
    #allows me t manually write header in, while printing 1 item
    'Sum': sum_slice,
    'Mean': mean_slice,
    'Standard Deviation': std_slice,
    'Median': med_slice,
    'Min': min_slice,
    'Max': max_slice
})

    
    analytics_df.to_csv("statistics.csv", header=False)   #write to csv