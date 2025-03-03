import numpy as np
import pandas as pd
#read files

#sum, mean, standard deviation, median, smallest value, and largest value
def calculate_values(column_date_slice_df):
    column_sum = column_date_slice_df.sum()
    column_mean = column_date_slice_df.mean()  
    column_std_dev = column_date_slice_df.std()  
    column_median = column_date_slice_df.median() 
    column_smallest = column_date_slice_df.min() 
    column_largest = column_date_slice_df.max()

    statistics = pd.Series({
    'Sum': column_sum,
    'Mean': column_mean,
    'StdDev': column_std_dev,
    'Median': column_median,
    'Smallest': column_smallest,
    'Largest': column_largest
})

    statistics.to_csv("statistics.csv", header=False)
#merged dataframe
def mergeing_df(youtube_df, days_df):
    complete_df = pd.merge(youtube_df, days_df, on='Date', how='outer')
    complete_df.to_csv("complete_table.csv")
#split-apply-combine
def day_of_week_info (youtube_df, days_df, column_name):
    complete_df = pd.merge(youtube_df, days_df, on='Date', how='outer')
    complete_df_grouped = complete_df.groupby("Day of Week")

    daily_means = complete_df.groupby("Day of Week")[column_name].mean()
    daily_means.to_csv("daily_breakdown.csv", header=False)