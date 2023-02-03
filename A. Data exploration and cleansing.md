# 🛒 Case Study - Bellabeat Fitbit 
# A. Data Exploration and Cleansing

<p align="right"> Using Python - Pycharm and Power BI </p>

## :books: Table of Contents <!-- omit in toc -->

<!-- TOC -->
  * [👩🏼‍💻 PYTHON - PYCHARM](#-python---pycharm)
   * [🔤 IMPORT LIBRARY AND DATASET](#-import-library-and-dataset)
   * [🔎 EXPLORE, CLEAN & TRANSFORM DATA](#-explore-clean--transform-data)
     * [:one: daily_activity dataset](#-one--daily_activity-dataset)
     * [:two: daily_sleep dataset](#-two--daily_sleep-dataset)
     * [:three: hourly_calories dataset](#-three--hourly_calories-dataset)
     * [:four: hourly_intensities dataset](#-four--hourly_intensities-dataset)
  * [📊 POWER BI](#-power-bi)
    * [1. Transform Data](#1-transform-data)
    * [2. New Column](#2-new-column)
    * [3. Create New Table](#3-create-new-table)
<!-- TOC -->

## 👩🏼‍💻 PYTHON - PYCHARM

## 🔤 IMPORT LIBRARY AND DATASET   

<details><summary> Click to expand :arrow_down: </summary>
  
```python
#Import librory
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from matplotlib import dates
import datetime
from pydoc import describe
print('Completed import lib')
```

```python
#Upload datasets
daily_activity = pd.read_csv('Fitabase Data/dailyActivity_merged.csv')
daily_sleep = pd.read_csv('Fitabase Data/sleepDay_merged.csv')
weight_log = pd.read_csv('Fitabase Data/weightLogInfo_merged.csv')
```
</details>

## 🔎 EXPLORE, CLEAN & TRANSFORM DATA   

### :one: daily_activity dataset

- There are 3 things I would check in daily_activity dataset:
  - The overall info 
  - Duplicated line
  - Distinct value of Id and ActivityDate columns

<details><summary> Set Display Option </summary>
  
```python
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
```

 </details>

<details><summary> The  Overall Infomation </summary>
  
```python
print(daily_activity.head()) 
```
![daily_activity_head](https://user-images.githubusercontent.com/95112831/213157353-e9a08593-43da-4cd8-b376-7ac98eca3a9b.PNG)
```python
print(daily_activity.info())
```
![daily_activity_info](https://user-images.githubusercontent.com/95112831/213187782-bef7cfd4-5ea2-425d-85f4-f50c954b3e0e.PNG)
:arrow_right:  There are no null values in the dataset 


 </details>

<details><summary> Remove duplicated line (if there are any) </summary>
  
```python
daily_activity = daily_activity.drop_duplicates(ignore_index=True)
print(daily_activity.info())
```
![daily_activity_info](https://user-images.githubusercontent.com/95112831/213187782-bef7cfd4-5ea2-425d-85f4-f50c954b3e0e.PNG)
:arrow_right:  There are no duplicated line in the dataset 


 </details>

 <details><summary> Checking distinct values of Id and ActivityDate columns </summary>

 ```python
#Id column
print('Number of distinct Id: ', daily_activity['Id'].nunique())
#ActivityDate column
print('Number of distinct Date: ', daily_activity['ActivityDate'].nunique())
print('Dates: ', daily_activity['ActivityDate'].unique())
 ```
![daily_activity_checking_Id_and_date](https://user-images.githubusercontent.com/95112831/213207456-20061f3f-fedf-4281-8b0a-cab47a8a8d09.PNG)
:arrow_right: There are 33 users logging in during 31 consecutive days from 04/12/2016 to 05/12/2016
</details>

 <details><summary> Save clean dataset </summary>

 ```python
 daily_activity.to_csv("daily_activity_cleaned.csv", index=False)
 ```
</details>
 
### :two: daily_sleep dataset

- There are 3 things I would check in daily_sleep dataset:
  - The overall info 
  - Duplicated line
  - Distinct value of Id and SleepDay columns

<details><summary> The  Overall Infomation </summary>
  
```python
print(daily_sleep.head()) 
```
![daily_sleep_head](https://user-images.githubusercontent.com/95112831/213217565-c8897313-11e7-4c3f-a5a9-c83dcf4d0625.PNG)
```python
print(daily_sleep.info())
```
![daily_sleep_info](https://user-images.githubusercontent.com/95112831/213225117-c8b60b22-e233-40cf-bcc3-605df03c6049.PNG)
:arrow_right:  There are no null values in the dataset 

 </details>

<details><summary> Remove duplicated line (if there are any) </summary>
  
```python
daily_sleep = daily_sleep.drop_duplicates(ignore_index=True)
print(daily_sleep.info())
```
![daily_sleep_remove_duplicated_line](https://user-images.githubusercontent.com/95112831/215437451-701cc3e2-2e86-4bfa-916b-d8606d3f2f3e.PNG)
:arrow_right:  There are 3 duplicated line in the dataset and they have been removed


 </details>

 <details><summary> Checking distinct values of Id and SleepDay columns </summary>

 ```python
#Id column
print('Number of distinct Id: ', daily_sleep['Id'].nunique())
#SleepDay column
print('Number of distinct Date: ', daily_sleep['SleepDay'].nunique())
print('Dates: ', daily_sleep['SleepDay'].unique())
 ```
![daily_sleep_checking_Id_and_date](https://user-images.githubusercontent.com/95112831/213231928-76c56590-4399-4808-83a3-83f2bf8a43c3.PNG)
:arrow_right: There are 24 users logging in during 31 consecutive days from 04/12/2016 to 05/12/2016
</details>

 <details><summary> Save clean dataset </summary>

 ```python
 daily_sleep.to_csv("daily_sleep_cleaned.csv", index=False)
 ```
</details>

### :three: hourly_calories dataset

- There are 3 things I would check in hourly_calories dataset:
  - The overall info 
  - Duplicated line
  - Distinct value of Id and ActivityHour columns

<details><summary> The  Overall Infomation </summary>
  
```python
print(hourly_calories.head()) 
```
![hourly_calories_head](https://user-images.githubusercontent.com/95112831/215440187-843439ee-0843-4b98-8269-a13104254a58.PNG)
```python
print(hourly_calories.info())
```
![hourly_calories_info](https://user-images.githubusercontent.com/95112831/215441748-748121c3-9a65-4e07-9563-8ccad2ad2ca0.PNG)
:arrow_right:  There are no null values in the dataset 

 </details>

<details><summary> Remove duplicated line (if there are any) </summary>
  
```python
hourly_calories = hourly_calories.drop_duplicates(ignore_index=True)
print(hourly_calories.info())
```
![hourly_calories_info](https://user-images.githubusercontent.com/95112831/215441748-748121c3-9a65-4e07-9563-8ccad2ad2ca0.PNG)
:arrow_right:  There are no duplicated line in the dataset

 </details>

 <details><summary> Checking distinct values of Id and ActivityHour columns </summary>

 ```python
#Id column
print('Number of distinct Id: ', hourly_calories['Id'].nunique())
#SleepDay column
print('Number of distinct Date: ', pd.to_datetime(hourly_calories['ActivityHour']).dt.date.nunique())
print('Dates: ', pd.to_datetime(hourly_calories['ActivityHour']).dt.date.unique())
 ```
![hourly_calories_checking_Id_and_date](https://user-images.githubusercontent.com/95112831/215452221-61c272ea-4d00-463d-952e-ad15d2c8ec2c.PNG)
:arrow_right: There are 33 users logging in during 31 consecutive days from 04/12/2016 to 05/12/2016
</details>

 <details><summary> Save clean dataset </summary>

 ```python
 hourly_calories.to_csv("hourly_calories_cleaned.csv", index=False)
 ```
</details>

### :four: hourly_intensities dataset

- There are 3 things I would check in hourly_intensities dataset:
  - The overall info 
  - Duplicated line
  - Distinct value of Id and ActivityHour columns

<details><summary> The  Overall Infomation </summary>
  
```python
print(hourly_intensities.head()) 
```
![hourly_intensities_head](https://user-images.githubusercontent.com/95112831/215454206-878250a6-9385-4383-9797-9924115ccf5c.PNG)
```python
print(hourly_intensities.info())
```
![hourly_intensities_info](https://user-images.githubusercontent.com/95112831/215454354-86d9d79f-0423-4b59-a38d-f87246df947a.PNG)
:arrow_right:  There are no null values in the dataset 

 </details>

<details><summary> Remove duplicated line (if there are any) </summary>
  
```python
hourly_intensities = hourly_intensities.drop_duplicates(ignore_index=True)
print(hourly_intensities.info())
```
![hourly_intensities_info](https://user-images.githubusercontent.com/95112831/215454354-86d9d79f-0423-4b59-a38d-f87246df947a.PNG)
:arrow_right:  There are no duplicated line in the dataset

 </details>

 <details><summary> Checking distinct values of Id and ActivityHour columns </summary>

 ```python
#Id column
print('Number of distinct Id: ', hourly_intensities['Id'].nunique())
#SleepDay column
print('Number of distinct Date: ', pd.to_datetime(hourly_intensities['ActivityHour']).dt.date.nunique())
print('Dates: ', pd.to_datetime(hourly_intensities['ActivityHour']).dt.date.unique())
 ```
![hourly_intensities_checking_Id_and_date](https://user-images.githubusercontent.com/95112831/215454859-2468311d-b26e-4c5b-8289-2e791bc09c71.PNG)
:arrow_right: There are 33 users logging in during 31 consecutive days from 04/12/2016 to 05/12/2016
</details>

 <details><summary> Save clean dataset </summary>

 ```python
 hourly_intensities.to_csv("hourly_intensities_cleaned.csv", index=False)
 ```
</details>   

---
## 📊 POWER BI

### 1. Transform Data

After import datasets, we need to transform them. 

<details><summary> daily_activity dataset  </summary>
 
 - Transformed 
  
![powerbi_daily_activity_transformed](https://user-images.githubusercontent.com/95112831/215505930-5d0b7355-2bca-424e-9369-d3481d45e181.PNG)

</details>  

<details><summary> daily_sleep dataset  </summary>
 
- Transformed
  
![powerbi_daily_sleep_transformed](https://user-images.githubusercontent.com/95112831/215507156-a1458c4c-dc6b-42e0-ae54-01fe4060d7c2.PNG)

</details>  

<details><summary> hourly_calories dataset  </summary>
 
- Transformed

![powerbi_hourly_calories_transformed](https://user-images.githubusercontent.com/95112831/215508069-6b491e6e-c0ac-495e-a52b-b11412f5f276.PNG)

Create a new column from merging 2 columns (Id and ActivityHour) to become primary key

</details>  

<details><summary> hourly_intensities dataset  </summary>

- Transformed
![powerbi_hourly_intensities_transformed](https://user-images.githubusercontent.com/95112831/215509035-8811f64a-c1ce-49a5-9982-98e777c875b7.PNG)

Create a new column from merging 2 columns (Id and ActivityHour) to become primary key

</details>

Model tab: Power BI automatically joins 2 datasets hourly_calories and hourly_intensities through primary key which is the new column 'Id and ActivityHour'

### 2. New Column

We need to create following column:

<details><summary> daily_activity dataset  </summary>

- NameOfTheDay: to get the name of the day  
```
NameOfTheDay = FORMAT('daily_activity'[ActivityDate],"dddd") 
```  
- Weekday: assign each day with a number so that we can arrange them in order
```
Weekday = WEEKDAY('daily_activity'[ActivityDate] - 1)
```
:heavy_check_mark: In tab model, NameOfTheDay -> Properties -> Advanced -> Sort by column -> Choose Weekday
- TotalHourUsing: get total hour that user use device  
```
TotalHourUsing = (daily_activity[VeryActiveMinutes] + daily_activity[FairlyActiveMinutes] + daily_activity[LightlyActiveMinutes] + daily_activity[SedentaryMinutes])/60
```

</details>  

<details><summary> daily_sleep dataset  </summary>

- NameOfTheDay: to get the name of the day  
```
NameOfTheDay = FORMAT('daily_sleep'[SleepDay],"dddd") 
```  
- Weekday: assign each day with a number so that we can arrange them in order
```
Weekday = WEEKDAY('daily_sleep'[SleepDay] - 1)
```
- TimeToSleep: get time user use to sleep  
```
TimeToSleep = daily_sleep[TotalTimeInBed] - daily_sleep[TotalMinutesAsleep]
```

</details>  

<details><summary> hourly_intensities dataset  </summary>

- NameOfTheDay: to get the name of the day  
```
NameOfTheDay = FORMAT('hourly_intensities'[ActivityHour],"dddd") 
```  
- Weekday: assign each day with a number so that we can arrange them in order
```
Weekday = WEEKDAY('hourly_intensities'[ActivityHour] - 1)
```
- Time: get time user use device 
```
Time = FORMAT('hourly_intensities'[ActivityHour],"hh:mm:ss")
```

</details>  

### 3. Create New Table

To analyze data based on each user, I create a new table

```
GroupById = GROUPBY(
  daily_activity,
  daily_activity[Id],
  "AverageHourUsingADay",AVERAGEX(CURRENTGROUP(),daily_activity[TotalHourUsing]),
  "AverageStepADay",AVERAGEX(CURRENTGROUP(),daily_activity[TotalSteps]),
  "AverageDistanceADay",AVERAGEX(CURRENTGROUP(),daily_activity[TotalDistance])
)
```
<details><summary> Some new columns helping to divide user into groups  </summary>

- UserUseTimeStatus: divide users into 2 groups - use device over 20 hours and under 20 hours
```
HighOrLowUse = if(GroupById[AverageHourUsingADay]>=20,"Over 20 hours","Under 20 hours")
```
- UserStepStatus: divide users into 2 groups - over 10000 steps and under 10000 steps
```
UserStepStatus = if(GroupById[AverageStepADay]>=10000,"Over 10000 Steps","Under 10000 Steps")
```
- UserDistanceStatus: divide users into 2 groups - over 8 km and under 8 km
```
UserDistanceStatus = if(GroupById[AverageDistanceADay]>=8,"Over 8 km","Under 8 km")
```
  
</details>

<details><summary> First few columns  </summary>

![powerbi_groupbyid_head](https://user-images.githubusercontent.com/95112831/215530036-e3b538e0-444f-40db-a5b8-8734654fed99.PNG)

</details>
