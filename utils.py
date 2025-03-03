import numpy as np
import pandas as pd

youtube_df = pd.read_csv("youtube_analytics_2-11-24_2-9-25.csv")
days_df = pd.read_csv("days_of_week_2-11-24_2-9-25.csv")

youtube_df.set_index("Date")
days_df.set_index("Date")

# Get start and end dates from the user input
start_date = input("Enter start date (DD-MM-YY) [Note if the month or date is single digit only enter that single digit]: ")
end_date = input("Enter end date (DD-MM-YY) [Note if the month or date is single digit only enter that single digit]: ")

df_slice = youtube_df.loc[start_date:end_date].copy()
#print(df_slice)
#sum, mean, standard deviation, median, smallest value, and largest value

def write_to_csv(df_slice):
    sum_slice = df_slice.sum()      # Sum of each column
    mean_slice = df_slice.mean()    # Mean of each column
    std_slice = df_slice.std()      # Standard deviation of each column
    med_slice = df_slice.median()   # Median of each column
    min_slice = df_slice.min()      # Minimum value of each column
    max_slice = df_slice.max()      # Maximum value of each column
    sum_slice.to_csv("statistics.csv")
    mean_slice.to_csv("statistics.csv")
    std_slice.to_csv("statistics.csv")
    med_slice.to_csv("statistics.csv")
    min_slice.to_csv("statistics.csv")
    max_slice.to_csv("statistics.csv")


write_to_csv(df_slice)