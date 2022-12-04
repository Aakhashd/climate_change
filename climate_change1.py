#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:26:37 2022

@author: aakhashd
"""
import matplotlib.pyplot as plt
import pandas as pd

# Reading data from the Csv file 
def reading_csv(filename):
    csv_dataframe=pd.read_csv(filename)
    cleaned_dataframe=csv_dataframe.replace(' ',0)
    countries=['France','Australia','Brazil','China',
               'United Kingdom','India']
    filt=cleaned_dataframe['Country Name'].isin(countries)
    filtered_dataframe=cleaned_dataframe.loc[filt]
    filtered_dataframe=filtered_dataframe.groupby(['Country Name'], 
                                                  as_index=False).sum()
    #print(df2_group)
    #df2t=filtered_dataframe.T
    #print(df2t)
    return filtered_dataframe

def climate_change_barchart(filename):
    climate_change_df=reading_csv(filename)
    plt.figure(figsize=(30,10))
    dataframe=climate_change_df.iloc[:,[0,1,21,41,51,61,62]]
    dataframe.plot(kind="bar", x= 'Country Name', rot=0, align='center',width=1.5)
    plt.xticks(rotation = 20)
    plt.title("Total Estimated climate change (1960-2021)")
    plt.ylabel("Amount of climate changes")


def co2_emission_linechart(filename):
    co2_emission=reading_csv(filename)
    plt.Figure(figsize=(10,10))
    co2_emission.plot(x="Country Name", y=["1960","1980","2000","2010","2020","2021"],
                  kind="line", linestyle='-.')
    plt.title("Total Estimated number of co2 emission (1960-2021)")
    plt.ylabel("total values for co2 emission")

def renewable_enegy_linechart(filename):
    renewable_energy=reading_csv(filename)
    print(renewable_energy)
    plt.figure(figsize=(20,20))
    renewable_energy.plot(x="Country Name", y=["1960","1980","2000","2010","2020","2021"],
                          kind="line", linestyle='-.')
    plt.title("Total Estimated number of Renewable energy(1960-2021)")
    plt.ylabel("total values for Renewable energy")
climate_change_barchart("climate_change2.csv")
co2_emission_linechart("co2_emmision.csv")
renewable_enegy_linechart("renewable_enegy.csv")
plt.show()