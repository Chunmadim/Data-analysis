# In This project I will Clean up the data and Transform it
# The Dataset I am working on is "Data science job posting in Glassdoor"
# Tasks:
# 1. Turn Salaries column into intejer
# 2. Remove number from company name
# 3. Create new features
# 4. Extract data from job descriptions

import pandas as pd 
import numpy as np 



def get_pandas_object_from_csv(path):
    df = pd.read_csv(path)
    return df 


def remove_index_column(df):
    del df["index"]


def strip_salaries(df):
    for index in range( len(df)):
        salary =  df.iloc[index]["Salary Estimate"]
        salary = salary.strip(" (Employer est.) (Glassdoor est.)")#
        salary = salary.replace("K","")
        salary = salary.replace("$", "")
        print(salary)
        df.at[index, "Salary Estimate"] = salary

    return df 


def create_min_max(df):
    min_salary = []
    max_salary = []
    for index in range(len(df)):
        salary_range = df.iloc[index]["Salary Estimate"]
        salary_range_temp = salary_range.split("-")
        min_salary.append(salary_range_temp[0])
        max_salary.append(salary_range_temp[1])
    df.insert(14,"min_salary",min_salary,True)
    df.insert(14,"max_salary",max_salary,True)



path = "Uncleaned_DS_jobs.csv"


df = get_pandas_object_from_csv(path)


remove_index_column(df)
df =strip_salaries(df)
create_min_max(df)
print(df)
