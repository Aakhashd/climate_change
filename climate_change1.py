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
    final_filtered_Dataframe=filtered_dataframe.filter(
        items=['Country Name','1960', '1980','2000','2010','2018','2019'])
    transpose_data=final_filtered_Dataframe.set_index(['Country Name']).T
    return (final_filtered_Dataframe,transpose_data)

def population(filename):
    population,population_transposeddf=reading_csv(filename)
    plt.figure(figsize=(30,10))
    population.plot(kind="bar", x='Country Name', rot=0, align='center',
                    width=0.5)
    plt.xticks(rotation = 20)
    plt.title("Total Estimated population (1960-2019)")
    plt.ylabel("Population growth (annual %)")

def agricultural_land(filename):
    agricultural,agricultural_transposeddf=reading_csv(filename)
    plt.figure(figsize=(30,10))
    agricultural.plot(kind="bar", x='Country Name', rot=0, align='center',
                      width=0.5)
    plt.xticks(rotation = 20)
    plt.title("Total Estimated agricultural land (1960-2019)")
    plt.ylabel("Agricultural land (sq. km)")
    
def co2_emission_linechart(filename):
    co2_emission,co2_transposed=reading_csv(filename)
    plt.Figure(figsize=(10,10))
    co2_transposed.plot(kind="line", linestyle='-.', 
             title ="Total Estimated amount of co2 emission (1960-2019)", 
             ylabel="Amount of co2 emission (kt)", xlabel="Period")
    
def methane_emission(filename):
    renewable_energy,renewable_transposeddf=reading_csv(filename)   
    plt.figure(figsize=(20,20))
    renewable_transposeddf.plot(kind="line", linestyle='-.')
    plt.title("Total Estimated amount of Methane emmission(1960-2019)")
    plt.ylabel("Amount of Methane emissions (kt)")
    plt.xlabel("Period")

population("population1.csv")
agricultural_land("Agricultural_land.csv")
co2_emission_linechart("co2_emmision.csv")
methane_emission("methane_emission.csv")
plt.show()
 




