import numpy as np
import pandas as pd
#dataframe empty with strings used
# i will be udsing pd.to_datetime to se eif this resoves the issue
youtube_df = pd.read_csv("youtube_analytics_2-11-24_2-9-25.csv")
days_df = pd.read_csv("days_of_week_2-11-24_2-9-25.csv")

youtube_df.set_index("Date")
days_df.set_index("Date")

start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

df_slice = youtube_df.loc[start_date:end_date].copy()

print(df_slice)