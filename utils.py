import numpy as np
import pandas as pd
#read files
youtube_df = pd.read_csv("youtube_analytics_2-11-24_2-9-25.csv")
days_df = pd.read_csv("days_of_week_2-11-24_2-9-25.csv")

#confirming dates
youtube_df.set_index("Date")
days_df.set_index("Date")

# Get start and end dates from the user input
start_date = input("Enter start date (MM/DD/YY) [Note if the month or date is single digit only enter that single digit]: ")
end_date = input("Enter end date (MM/DD/YY) [Note if the month or date is single digit only enter that single digit]: ")

date_slice_df = youtube_df.loc[start_date:end_date]
#currently working
column_name = input("Please enter in one of the following column name to calculate a value for: Views\nAverage percentage viewed (%)\nUnique viewers\nSubscribers\nWatch time (hours)\nAverage view duration\nShares\nLikes\nDislikes\nComments added\nImpressions\nImpressions click-through rate (%)\n")
column_date_slice_df = date_slice_df.loc[:, column_name]

#sum, mean, standard deviation, median, smallest value, and largest value
def calculate_sum(column_date_slice_df):
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

calculate_sum(column_date_slice_df)