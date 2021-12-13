# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from scipy.stats import shapiro
import scipy.stats as stats
from matplotlib import pyplot
from scipy.stats import ttest_ind

# dataframe 
diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

timeinhospital = diabetes['time_in_hospital']
labprocedures = diabetes['num_lab_procedures'] 
gender = diabetes['gender']

# Sample of dataframe
diabetes_small = diabetes.sample(100)

timeinhospital = diabetes['time_in_hospital']
labprocedures = diabetes['num_lab_procedures'] 

##Total count of procedures
diabetes['totalCountProcedures'] = diabetes['num_procedures'] + diabetes['num_lab_procedures']
diabetes['totalCountProcedures'].describe()
totalCountProcedures = diabetes['totalCountProcedures'].array

### Example T-Test

# Is there a difference between sex (M:F) and the number of lab procedures performed?
# Gender and Total Count Procedures

list(diabetes)

Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']
ttest_ind(Female['totalCountProcedures'], Male['totalCountProcedures'])

## Ttest_indResult(statistic=-0.6747218803792331, pvalue=0.4998540133474586)
## We fail to reject the null hypothesis because there is not a difference between the average number of procedures 
## between males and females due to the P-value being greater than 0.05 



# 1. Is there a difference between gender (M:F) and the number of days in hospital?

ttest_ind(Female['time_in_hospital'], Male['time_in_hospital'])
#### statistic=9.542637042242887, pvalue=1.4217299655114968e-21

## There is a significant difference in time in hospital between males and females 
## because the p-value is less than 0.05, which allows us to reject the null hypothesis 


## 2. Is there a difference between RACE (Caucasian and African American) and the number of days in hospital?

list(diabetes)
Caucasian = diabetes[diabetes['race']=='Caucasian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Caucasian['time_in_hospital'], AfricanAmerican['time_in_hospital'])
## Ttest_indResult(statistic=-5.0610017032095325, pvalue=4.178330085585203e-07)

# There is a significant difference in time in hospital between Caucasians and African Americans
## because the p-value is less than 0.05, which allows us to reject the null hypothesis 


#3. Is there a difference between RACE (Asian and African American) and the number of lab procedures performed?

list(diabetes)
Asian = diabetes[diabetes['race']=='Asian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Asian['num_lab_procedures'], AfricanAmerican['num_lab_procedures'])
##Ttest_indResult(statistic=-3.9788715315360292, pvalue=6.948907528800307e-05)

## There is a significant difference with the number of lab procedures for African Americans and Asian population
##since the P-value is less than 0.05 we can reject the null hypothesis.