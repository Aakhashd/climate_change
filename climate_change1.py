#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:26:37 2022

@author: aakhashd
"""
import matplotlib.pyplot as plt
import pandas as pd

# Reading data from the Csv file 
df1=pd.read_csv("climate_change2.csv")
df2=df1.replace(' ',0)
countries=['France','Australia','Brazil','China',
           'United Kingdom','India','United States']
filt=df2['Country Name'].isin(countries)
df2f=df2.loc[filt]
print(df2f)
df2_group=df2f.groupby(['Country Name'], as_index=False).sum()
print(df2_group)

df2t=df2_group.T
print(df2t)

plt.figure(figsize=(30,10))
dataframe=df2_group.iloc[:,[0,1,11,21,31,41,51,61,62]]
print(dataframe)

dataframe.plot(kind="bar", x= 'Country Name', rot=0, align='center',width=1.5)
plt.xticks(rotation = 30)