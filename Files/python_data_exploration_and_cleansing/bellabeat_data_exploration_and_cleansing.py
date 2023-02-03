#Import librory
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from matplotlib import dates
import datetime
from pydoc import describe

from pandas import to_datetime

print('Completed import lib')

#Upload dataset
daily_activity = pd.read_csv('Fitabase Data/dailyActivity_merged.csv') #Press Ctrl to open file
daily_sleep = pd.read_csv('Fitabase Data/sleepDay_merged.csv')
hourly_calories = pd.read_csv('Fitabase Data/hourlyCalories_merged.csv')
hourly_intensities = pd.read_csv('Fitabase Data/hourlyIntensities_merged.csv')

#Set display option
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)

#Explore, clean and transform data

#1, Daily activity dataset
#Overall info
print(daily_activity.head())
print(daily_activity.info()) #=>There are no null value in the dataset
#Checking duplicated line
daily_activity = daily_activity.drop_duplicates(ignore_index=True)
print(daily_activity.info())
#Checking distinct values of Id and ActivityDate columns
print('Number of distinct Id: ', daily_activity['Id'].nunique())
print('Number of distinct Date: ', daily_activity['ActivityDate'].nunique())
print('Dates: ', daily_activity['ActivityDate'].unique())
#Save clean dataset
daily_activity.to_csv("daily_activity_cleaned.csv", index=False)

#2, Daily sleep dataset
#Overall info
print(daily_sleep.head())
print(daily_sleep.info()) #=>There are no null value in the dataset
#Remove duplicated line
daily_sleep = daily_sleep.drop_duplicates(ignore_index=True)
print(daily_sleep.info())
#Checking distinct values of Id and SleepDay columns
print('Number of distinct Id: ', daily_sleep['Id'].nunique())
print('Number of distinct Date: ', daily_sleep['SleepDay'].nunique())
print('Dates: ', daily_sleep['SleepDay'].unique())
#Save clean dataset
daily_sleep.to_csv("daily_sleep_cleaned.csv", index=False)

#3, Hourly Calories dataset
#Overall info
print(hourly_calories.head())
print(hourly_calories.info()) #=>There are no null value in the dataset
#Remove duplicated line
hourly_calories = hourly_calories.drop_duplicates(ignore_index=True)
print(hourly_calories.info())
#Checking distinct values of Id and ActivityHour columns
print('Number of distinct Id: ', hourly_calories['Id'].nunique())
print('Number of distinct Date: ', pd.to_datetime(hourly_calories['ActivityHour']).dt.date.nunique())
print('Dates: ', pd.to_datetime(hourly_calories['ActivityHour']).dt.date.unique())
#Save clean dataset
# hourly_calories.to_csv("hourly_calories_cleaned.csv", index=False)

#3, Hourly Intensities dataset
#Overall info
print(hourly_intensities.head())
print(hourly_intensities.info()) #=>There are no null value in the dataset
#Remove duplicated line
hourly_intensities = hourly_intensities.drop_duplicates(ignore_index=True)
print(hourly_intensities.info())
#Checking distinct values of Id and ActivityHour columns
print('Number of distinct Id: ', hourly_intensities['Id'].nunique())
print('Number of distinct Date: ', pd.to_datetime(hourly_intensities['ActivityHour']).dt.date.nunique())
print('Dates: ', pd.to_datetime(hourly_intensities['ActivityHour']).dt.date.unique())
#Save clean dataset
hourly_intensities.to_csv("hourly_intensities_cleaned.csv", index=False)






