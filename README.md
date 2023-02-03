# :computer:  Case Study: How Can a Wellness Technology Company Play It Smart?
Bellabeat is a high-tech manufacturer of health-focused products for women. As a junior data analyst working with 
marketing analyst team at Bellabeat, a high-tech manufacturer of health-focused products for women. Bellabeat is a 
successful small company, but they have the potential to become a larger player in the global smart device market. 
Urška Sršen, cofounder and Chief Creative Officer of Bellabeat, believes that analyzing smart device fitness data 
could help unlock new growth opportunities for the company. I have been asked to focus on one of Bellabeat’s products 
and analyze smart device data to gain insight into how consumers are using their smart devices. Urška Sršen is 
confident that an analysis of non-Bellebeat consumer data (ie. FitBit fitness tracker usage data) would reveal more 
opportunities for growth. The insights from the data will help to guide marketing strategy for the company. I have 
performed analysis on data along with high level recommendations for Bellabeat’s marketing strategy.

__Business Task:__
Analyze FitBit fitness tracker data to gain insights into how consumers are using the FitBit app and discover trends 
for Bellabeat marketing strategy.
---

# :bookmark_tabs:  Example Datasets

---
### daily_activity dataset 
Provide information about user's stats on daily activity

- Id: unique Id of user 
- ActivityDate: date where user log in
- TotalSteps: total steps in one day
- TotalDistance: total distance in one day
- TrackerDistance: tracker distance
- LoggedAcitivityDistance: logger activity distance
- VeryActiveDistance: distance user are very active
- ModeratelyActiveDistance: distance user is moderately active
- LightlyActiveDistance: distance user is lightly active
- SedentaryActiveDistance: distance user is sedentary active
- VeryActiveMinutes: minutes user is very active
- FairlyActiveMinutes: minutes user is fairly active
- LightlyActiveMinutes: minutes user is lightly active
- SedentaryActiveMinutes: minutes user is sedentary active
- Calories: calories user burns 

<details>
  <summary>Click to expand daily_activity dataset</summary>

  <div align="center"> 

  **Table: daily_activity** 

  </div>

  <div align="center"> 

  First 10 rows

  </div>

| Id          |ActivityDate| TotalSteps | TotalDistance |TrackerDistance | LoggedActivityDistance |VeryActiveDistance   |ModerateActiveDistance |LightActiveDistance |SedentaryActiveDistance |VeryActiveMinutes | FairlyActiveMinutes  |LightlyActiveMinutes |SedentaryMinutes|Calories|
|:------------|:----------|:------|:----|:----|:----|:----|:----|:----|:----|:----|:---------------------|:----|:---------------|:----|
| 1503960366  | 4/12/2016 | 13162 |8.50000|8.50000|0.00000|1.88000|0.55000|6.06000|0.00000|25| 13                   |328| 728            |1985|
| 1503960366  | 4/13/2016 | 10735 |6.97000|6.97000|0.00000|1.57000|0.69000|4.71000|0.00000|21| 19                   |217| 776            |1797|
| 1503960366  | 4/14/2016 | 10460 |6.74000|6.74000|0.00000|2.44000|0.40000|3.91000|0.00000|30| 11                   |181| 1218           |1776|
| 1503960366  | 4/15/2016 | 9762  |6.28000|6.28000|0.00000|2.14000|1.26000|2.83000|0.00000|29| 34                   |209| 726            |1745|
| 1503960366  | 4/16/2016 | 12669 |8.16000|8.16000|0.00000|2.71000|0.41000|5.04000|0.00000|36| 10                   |221| 773            |1863|
| 1503960366  | 4/17/2016 | 9705  |6.48000|6.48000|0.00000|3.19000|0.78000|2.51000|0.00000|38| 20                   |164| 539            |1728|
| 1503960366  | 4/18/2016 | 13019 |8.59000|8.59000|0.00000|3.25000|0.64000|4.71000|0.00000|42| 16                   |233| 1149           |1921|
| 1503960366  | 4/19/2016 | 15506 |9.88000|9.88000|0.00000|3.53000|1.32000|5.03000|0.00000|50| 31                   |264| 775            |2035|
| 1503960366  | 4/20/2016 | 10544 |6.68000|6.68000|0.00000|1.96000|0.48000|4.24000|0.00000|28| 12                   |205| 818            |1786|
| 1503960366  | 4/21/2016 | 9819  |6.34000|6.34000|0.00000|1.34000|0.35000|4.65000|0.00000|19| 8                    |211| 838            |1775|

</details>

---
### daily_sleep dataset 
Provide information about user's daily sleep

- Id: unique Id of user
- SleepDay: day that user sleeps 
- TotalSleepRecords: count times that user sleeps 
- TotalMinutesAsleep: minutes user is asleep 
- TotalTimeInBed: minutes user is in bed 

<details>
  <summary>Click to expand daily_sleep dataset</summary>

  <div align="center"> 

  **Table: daily_sleep** 

  </div>

  <div align="center"> 

  First 10 rows

  </div>

| Id          | SleepDay | TotalSleepRecords | TotalMinutesAsleep | TotalTimeInBed  | 
|:------------|:---------|:-------|:-------|:----|
| 1503960366  |4/12/2016 12:00:00 AM|1|327|346|
| 1503960366  |4/13/2016 12:00:00 AM|2|384|407|
| 1503960366  |4/15/2016 12:00:00 AM|1|412|442|
| 1503960366  |4/16/2016 12:00:00 AM|2|340|367|
| 1503960366  |4/17/2016 12:00:00 AM|1|700|712|
| 1503960366  |4/19/2016 12:00:00 AM|1|304|320|
| 1503960366  |4/20/2016 12:00:00 AM|1|360|377|
| 1503960366  |4/21/2016 12:00:00 AM|1|325|364|
| 1503960366  |4/23/2016 12:00:00 AM|1|361|384|
|  1503960366 |4/24/2016 12:00:00 AM|1|430|449|


</details>

---

### hourly_calories dataset
Provide information about user's activity hour and calories 

- Id: unique Id of user
- ActivityHour: date time of user's activity
- Calories: amount of calories burnt 

<details>
  <summary>Click to expand hourly_calories dataset</summary>

  <div align="center"> 

  **Table: hourly_calories** 

  </div>

  <div align="center"> 

  First 10 rows

  </div>

| Id         | ActivityHour | Calories |   
|:-----------|:----|:------|
| 1503960366 |4/12/2016 12:00:00 AM|81|
| 1503960366 |4/12/2016 1:00:00 AM|61|
| 1503960366 |4/12/2016 2:00:00 AM|59|
| 1503960366 |4/12/2016 3:00:00 AM|47|
| 1503960366 |4/12/2016 4:00:00 AM|48|
| 1503960366 |4/12/2016 5:00:00 AM|48|
| 1503960366 |4/12/2016 6:00:00 AM|48|
| 1503960366 |4/12/2016 7:00:00 AM|47|
| 1503960366 |4/12/2016 8:00:00 AM|68|
| 1503960366 |4/12/2016 9:00:00 AM|141|


</details>

---

### hourly_intensities dataset
Provide information about user's activity hour and total intensity

- Id: unique Id of user
- ActivityHour: date time of user's activity
- TotalIntensity: user's total intensity during activity hour

<details>
  <summary>Click to expand hourly_intensities dataset</summary>

  <div align="center"> 

  **Table: hourly_intensities** 

  </div>

  <div align="center"> 

  First 10 rows

  </div>

| Id          | ActivityHour | TotalIntensity | AverageIntensity |   
|:------------|:----|:------|:-----|
|1503960366|4/12/2016 12:00:00 AM|20|0.33333|
|1503960366|4/12/2016 1:00:00 AM|8|0.13333|
|1503960366|4/12/2016 2:00:00 AM|7|0.11667|
|1503960366|4/12/2016 3:00:00 AM|0|0.00000|
|1503960366|4/12/2016 4:00:00 AM|0|0.00000|
|1503960366|4/12/2016 5:00:00 AM|0|0.00000|
|1503960366|4/12/2016 6:00:00 AM|0|0.00000|
|1503960366|4/12/2016 7:00:00 AM|0|0.00000|
|1503960366|4/12/2016 8:00:00 AM|13|0.21667|
|1503960366|4/12/2016 9:00:00 AM|30|0.50000|



</details>
















