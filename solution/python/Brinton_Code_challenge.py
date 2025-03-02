#!/usr/bin/env python
# coding: utf-8

# # Brinton Code Challenge Solution
# 

# ### I will be using a Notebook for documentation and development. My process for building the solution will be as follows:
# * I will write ewach section in the notebook.
# * I will debug and validate in the notebook.
# * The final results will be deployed into an exacutable service.
# * All deliverables will be uploaded into GIT. -- add director and link

# ## Imports and Definitiions

# In[88]:


# import libraries for data manipulation
import json
import pandas as pd
import numpy as np
import rfc3339 as rfc




# ## Helper Functions:

# In[89]:


def check_missing_data(df):
    if df.isnull().sum().sum() > 0:
    ## Build purge and reporting function
      print('Missing values found')
      ## Purge the missing values
      df = df.dropna()
    ## Report the missing values
      df.to_csv('missing_values.csv')
      print('Missing values have been purged and reported in missing_values.csv')
    else:
      print('No missing values found')

    


# In[90]:


def check_invalid_shifts_times(df):
## Check if the shift is valid
  invalid_shifts = df[df['StartTime'] > df['EndTime']]
  
  if invalid_shifts.shape[0] > 0:
    ## Build purge and reporting function for invalid shifts
    print('Invalid shifts found', invalid_shifts)
  else:
    print('No invalid shifts found')
        


# In[92]:


## This function uses merge instead of a nested loop to find overlapping shifts and return the DF with the overlapping shifts

## INPUTS:  DF
## OUTPUT: DF with overlapping shifts

def find_overlapping_shifts(df):
    ## Perform self-join on EmployeeId to compare shifts
    overlapping_shifts = df.merge(df, on="EmployeeID", suffixes=("_A", "_B"))
    ## Filter overlapping shifts
    overlapping_shifts = overlapping_shifts[
    (overlapping_shifts["ShiftID_A"] < overlapping_shifts["ShiftID_B"]) &  # Avoid duplicate comparisons
    (overlapping_shifts["StartTime_A"] < overlapping_shifts["EndTime_B"]) &
    (overlapping_shifts["StartTime_B"] < overlapping_shifts["EndTime_A"])
    ]
    ## Select relevant columns
    overlapping_shifts = overlapping_shifts[["ShiftID_A", "ShiftID_B", "EmployeeID"]]
    return overlapping_shifts


# In[93]:


def mergeoverlapshifts(resultsdf, overlapdf):
    
    ## need to add in shift week   
    # Combine ShiftID_A and ShiftID_B into a single column
    overlapdf_melted = (overlapdf.melt(id_vars=["EmployeeID"], value_vars=["ShiftID_A", "ShiftID_B"], value_name="ShiftID"))

    # Group shifts into lists per EmployeeID
    shifts_per_employee = overlapdf_melted.groupby("EmployeeID")["ShiftID"].unique().reset_index()

    # Convert NumPy array to a list for readability
    shifts_per_employee["ShiftID"] = shifts_per_employee["ShiftID"].apply(list)
    
    # Merge shift lists into resultsdf
    resultsdf = resultsdf.merge(shifts_per_employee, on="EmployeeID", how="left")

    # Rename column for clarity
    resultsdf.rename(columns={"ShiftID": "InvalidShifts"}, inplace=True)

    # Fill missing values with empty lists
    resultsdf["InvalidShifts"] = resultsdf["InvalidShifts"].apply(lambda x: x if isinstance(x, list) else [])
    
    return resultsdf
    
    


# In[94]:


def dropinvalidshifts(df, overlapdf):
    # Get ShiftIDs to drop
    invalid_shifts = set(overlapdf["ShiftID_A"]).union(set(overlapdf["ShiftID_B"]))
    print('number overlap shifts:', len(invalid_shifts))

    # Drop invalid shifts
    print('number of shifts before drop:', df.shape[0])
    df = df[~df["ShiftID"].isin(invalid_shifts)]
    print('number of shifts after drop:', df.shape[0])
    
    return df


# In[95]:


def assign_hours_worked(df):
  # Calculate hours worked per shift
  df["HoursWorked"] = (df["EndTime"] - df["StartTime"]).dt.total_seconds() / 3600

  # Get StartOfWeek for each shift (Monday of that week)
  df["StartOfWeek"] = df['StartTime'].dt.to_period('W').dt.start_time

  # Group by EmployeeID and StartOfWeek
  weekly_hours = df.groupby(["EmployeeID", "StartOfWeek"])["HoursWorked"].sum().reset_index()

  # Split into RegularHours and OvertimeHours
  weekly_hours["RegularHours"] = weekly_hours["HoursWorked"].clip(upper=40)  # Max 40 regular hours
  weekly_hours["OvertimeHours"] = (weekly_hours["HoursWorked"] - 40).clip(lower=0)  # Overtime is extra hours

  # Drop total hours (not needed)
  weekly_hours.drop(columns=["HoursWorked"], inplace=True)

  return weekly_hours
  
  


# ## Create Main execution of the program
# ### This code will call funcitons for dependent services.
# 

# In[97]:


## Open the json data file.
with open('dataset.json', 'r') as f:
    data = json.load(f)
    
## Create a dataframe out of input source
df = pd.DataFrame(data)
## df.head()
## Define output source data frame
resultdf = pd.DataFrame(columns=['EmployeeID', 'StartOfWeek', 'RegularHours', 'OvertimeHours'])


## Process the data for errors
## Check for missing values
check_missing_data(df)

## convert RFC3339 to timestamp in pandas.
## This is my first experience with the RFC33339 format, So I am not sure of the best practice to using this format.  I am converting for the sake of time.
df['StartTime'] = pd.to_datetime(df['StartTime'])
df['EndTime'] = pd.to_datetime(df['EndTime'])

## Check for invalid shifts
check_invalid_shifts_times(df)

## sort df by employeeID and StartTime
df = df.sort_values(by=['EmployeeID', 'StartTime']) 

## build base of reults dataframe
##resultdf['EmployeeID'] = df['EmployeeID'].unique()
##resultdf['StartOfWeek'] = df['StartTime'].dt.to_period('W').dt.start_time

## find shifts that overlap
dfoverlap = find_overlapping_shifts(df)

## add overlap shifts to results dataframe
##resultdf = mergeoverlapshifts(resultdf, dfoverlap)

## Drop the invalid shifts from the dataframe
df = dropinvalidshifts(df, dfoverlap)

## Calculate hours worked and assign to the output dataframe
hoursworked = assign_hours_worked(df)

## merge hours worked to the output dataframe
resultdf = mergeoverlapshifts(hoursworked, dfoverlap)

## Write the output to a csv file
resultdf.to_csv('output.csv', index=False)
print('Output file created')   

## Missing validations for the following:
## 1.  Check for shifts that carry over sunday intot he next week
## 2.  Need to clean up the Invalid Shifts list to remove the data type in the list.
## 3.  I never touched on the day light savings issue. 
## 4.  There is no test suit to validate the code. 



