#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:26:37 2022

@author: aakhashd
"""
import matplotlib.pyplot as plt
import pandas as pd

# Reading data & cleaning data from the Csv file 
def reading_csv(filename):
    read_df=pd.read_csv(filename)
    # cleaning of data
    cleaned_dataframe=read_df.replace(' ',0)
    # filtering based on the countries
    countries=['France','Australia','Brazil','China',
               'United Kingdom','India','Ireland']
    filt=cleaned_dataframe['Country Name'].isin(countries)
    filtered_dataframe=cleaned_dataframe.loc[filt]
    filtered_dataframe=filtered_dataframe.groupby(
                        ['Country Name'], as_index=False).sum()
    final_filtered_Dataframe=filtered_dataframe.filter(
        items=['Country Name','1960', '1980','2000','2010','2018','2019'])
    # Transposing the data so plot the graph based on countries
    transpose_data=final_filtered_Dataframe.set_index(['Country Name']).T
    return (final_filtered_Dataframe,transpose_data)

# defining a bar plot for population
def population(filename):
    # Fetcing the dataframe for population of data
    population,population_transposeddf=reading_csv(filename)
    plt.figure(figsize=(30,10))
    #Plotting the population data on bar plot
    population.plot(kind="bar", x='Country Name', rot=0, align='center',
                    width=0.5)
    plt.xticks(rotation = 20)
    plt.title("Total Estimated population (1960-2019)")
    plt.ylabel("Population growth (annual %)")
    plt.savefig("population.png")

#defining the function for energy usage  bar chart
def energy_use(filename):
    # Fetcing the dataframe for Energy use of data
    energy_use,energy_use_transposeddf=reading_csv(filename)
    plt.figure(figsize=(30,10))
    energy_use.plot(kind="bar", x='Country Name', rot=0, align='center',
                      width=0.5)
    plt.xticks(rotation = 20)
    plt.title("Estimated energy usage (1960-2019)")
    plt.ylabel("Energy use (kg of oil equivalent per capita)")
    plt.savefig("energy_use.png")

#defining the function for co2_emission usage line chart
def co2_emission_linechart(filename):
    co2_emission,co2_transposed=reading_csv(filename)
    plt.Figure(figsize=(10,10))
    plt.legend()
    # ploting the transposed dataframe with line chart
    co2_transposed.plot(kind="line", linestyle='-.', 
             title ="Estimated amount of co2 emission (1960-2019)", 
             ylabel="Amount of co2 emission (kt)", xlabel="Period")
    plt.savefig("co2_emission.png")

#defining the function for methane_emission usagebarline chart
def methane_emission(filename):
    methane_emission,methane_emissiondf=reading_csv(filename)   
    plt.figure(figsize=(20,20))
    # ploting the transposed dataframe with line chart
    methane_emissiondf.plot(kind="line", linestyle='-.')
    plt.title("Estimated amount of Methane emmission(1960-2019)")
    plt.ylabel("Amount of Methane emissions (kt)")
    plt.xlabel("Period")
    plt.savefig("methane_emission.png")

#defining a function for ploting heatmap
def map_corr(df, size=10):
    #Finding the correlation for the dataframe
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr, cmap='coolwarm')
    ax.set_title("China")
    fig.tight_layout()
    fig.set_size_inches(11.03, 3.5)
    # setting ticks to column names
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.savefig("heat_map.png",dpi =400)

# defining a function for ploting heatmap
def heatmap(filename):
    d=pd.read_csv(filename)
    df1=d.replace(' ',0)
    #Filtering the data based on country
    countries=['China']
    filt=df1['Country Name'].isin(countries)
    df2=df1.loc[filt]
    #Filtering the data based on Indicators
    indicator_name=['Urban population','CO2 emissions (kt)'
                    ,'Forest area (sq. km)','Agricultural land (sq. km)'
                    ,'Energy use (kg of oil equivalent per capita)',
                    'Electric power consumption (kWh per capita)'
                    'Methane emissions (kt of CO2 equivalent)',
                    'Total greenhouse gas emissions (kt of CO2 equivalent)'
                    'Population, total','Agricultural land (sq. km)']
    filtered=df2['Indicator Name'].isin(indicator_name)
    df=df2.loc[filtered]
    df.drop(['Country Name', 'Country Code'], axis=1, inplace=True)
    df9=df[['Indicator Name','1960','1980','2000','2010','2018','2019']]
    dft=df9.set_index(['Indicator Name']).T
    map_corr(dft)
    plt.show()
    dft = dft.fillna(0)
 
heatmap("climate_change2.csv")
population("population1.csv")
energy_use("energy_use.csv")
co2_emission_linechart("co2_emmision.csv")
methane_emission("methane_emission.csv")
plt.show()
 




