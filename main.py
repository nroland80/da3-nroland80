import numpy as np
import pandas as pd
import utils

from utils import calculate_values
from utils import mergeing_df
from utils import day_of_week_info


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

calculate_values(column_date_slice_df)
mergeing_df(youtube_df, days_df)
day_of_week_info (youtube_df, days_df, column_name)