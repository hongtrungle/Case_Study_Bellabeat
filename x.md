# 🛒 Case Study - Bellabeat Fitbit 
# A. Data Exploration and Cleansing

<p align="right"> Using Python - Pycharm vs Power BI </p>

## :books: Table of Contents <!-- omit in toc -->


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

- There are 4 things I would check in customers dataset:
  - The overall info 
  - There is duplicated value of primary key or not (customer_id)
  - Checking unique values of city name, State.
  - Capitalize the first letter of city name.

<details><summary> Set Display Option </summary>
  
```python
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
```

 </details>

<details><summary> The  Overall Infomation </summary>
  
```python
daily_activity.head() 
```
![daily_activity_head](https://user-images.githubusercontent.com/95112831/213154621-4c2d0599-35a5-4920-98fc-bce374446f09.PNG)
```python
customers.info()
```
![image](https://user-images.githubusercontent.com/101379141/202383205-458cecd8-c962-4ca1-9d38-6b04d45a7fb6.png)

 </details>
 
 <details><summary> Checking duplicated values </summary>
  
```python
#Checking the duplicated values of primary key column (customer_id), because number of customer_id is same with total data entries (99441), so we can conclude that there is not duplicated values

customers.nunique()   
```  
![image](https://user-images.githubusercontent.com/101379141/202384243-a902b51d-6423-41ea-9028-c40731efdddc.png)
  
 </details>

 <details><summary> Checking unique values of State </summary>

 ```python
#Checking State typing 
customers['customer_state'].unique() 
 ```
![image](https://user-images.githubusercontent.com/101379141/202384543-036fe5fb-9a9b-48fb-abfb-ca6837b96d6e.png)

 </details>
 
  <details><summary>  Capitalize the first letter of city name  </summary>

 ``` python
#Capitalize the first letter of city name
customers['customer_city'] = customers['customer_city'].str.title()
 
```
```python
customers.head()
```
![image](https://user-images.githubusercontent.com/101379141/202384920-d67e7d24-75b0-47d2-b35e-28254473878b.png)

 </details>
