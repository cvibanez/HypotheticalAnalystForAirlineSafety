# Conrad Ibanez
# DSC640 Winter 2020
# Project Task 1: Dashboard

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.offline import iplot
import plotly.io as pio
import plotly.express as px
pio.renderers.default='browser'


def read_airline_safety_file():
    # read the csv file
    airline_safety_df = pd.read_csv("../../data/airline-safety.csv")
    # Remove asterisk in airline name
    airline_safety_df['airline'] = airline_safety_df['airline'].str.replace('*','')
    return airline_safety_df

def read_airline_accidents_file():
    # read the csv file
    airline_accidents_df = pd.read_excel("../../data/table9_2014-accidents_ntsb-classification-1995-2014-for-u-s-air-carriers_Clean.xls")
    # Remove asterisk in airline name
    return airline_accidents_df

def read_auto_accidents_file():
    # read the csv file
    auto_accidents_df = pd.read_excel("../../data/National Statistics_Clean.xls")
    # Remove asterisk in airline name
    return auto_accidents_df

def read_airline_revenue_file():
    # read the csv file
    airline_df = pd.read_excel("../../data/Passenger_Revenue_Total_System_Operations_Clean.xls")
    return airline_df

def read_passengers_file():
    # read the csv file
    airline_df = pd.read_excel("../../data/System_Total_Enplaned_Passengers_Clean.xls")
    return airline_df


# Reference- https://plotly.com/python/horizontal-bar-charts/
def create_top_airline_fatalities_bar():
    # get data
    airline_safety_df = read_airline_safety_file()
    
    # drop na values
    airline_safety_df = airline_safety_df.dropna()
    
    # Sort data by fatalities
    airline_safety_df = airline_safety_df.sort_values(by=['fatalities_00_14'], ascending=False)
    
    # take the top 20 fatalities
    airline_safety_df = airline_safety_df[:20]
    
    # Sort data by fatalities so that the most fatalities are first
    airline_safety_df = airline_safety_df.sort_values(by=['fatalities_00_14'])
    
    # Take top 10
    #airline_safety_df = airline_safety_df[:20]
    #airline_names = airline_safety_df['airline'] + ' (' + airline_safety_df['avail_seat_km_per_week'].map(str) + ')'
    
    airlines = airline_safety_df['airline'].tolist()
    y_pos = np.arange(len(airlines))
    quantity = airline_safety_df['fatalities_00_14'].tolist()
    
    fig, ax = plt.subplots(figsize=(5,5))

    ax.barh(y_pos, quantity)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(airlines)
    #ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Fatalities')
    ax.set_title('Top 20 Airlines with Most Fatalities from 2000-2014')

    plt.show()
    
def create_top_airline_incidents_bar():
    # get data
    airline_safety_df = read_airline_safety_file()
    
    # drop na values
    airline_safety_df = airline_safety_df.dropna()
    
    # Sort data by incidents_00_14
    airline_safety_df = airline_safety_df.sort_values(by=['incidents_00_14'], ascending=False)
    
    # take the top 20 incidents_00_14
    airline_safety_df = airline_safety_df[:20]
    
    # Sort data by incidents_00_14 so that the most incidents_00_14 are first
    airline_safety_df = airline_safety_df.sort_values(by=['incidents_00_14'])
    
    # Take top 10
    #airline_safety_df = airline_safety_df[:20]
    #airline_names = airline_safety_df['airline'] + ' (' + airline_safety_df['avail_seat_km_per_week'].map(str) + ')'
    
    airlines = airline_safety_df['airline'].tolist()
    y_pos = np.arange(len(airlines))
    quantity = airline_safety_df['incidents_00_14'].tolist()
    
    fig, ax = plt.subplots(figsize=(5,5))

    ax.barh(y_pos, quantity)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(airlines)
    #ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Incidents')
    ax.set_title('Top 20 Airlines with Most Incidents from 2000-2014')

    plt.show()
    
# Reference- https://plotly.com/python/bar-charts/    
def create_accidents_stacked_bar():
    # get data
    accidents = read_airline_accidents_file()
    
    accidents['Accidents_Non_Fatal'] = accidents['Accidents_All'] - accidents['Accidents_Fatal']
    
    #years_list = accidents['Year']values.astype(int).flatten().tolist()
    years_list = accidents['Year'].values.flatten().tolist()
#    first_qty =  accidents['Accidents_Fatal'].values.flatten().values.flatten().tolist()
#    second_qty =  accidents['Accident _Non_Fatal'].values.flatten().values.flatten().tolist()
    
    first_qty =  accidents['Accidents_Fatal']
    second_qty =  accidents['Accidents_Non_Fatal']

    
#    # Heights of bars1 + bars2
#    bars_first_second = np.add(first_qty, second_qty).tolist()

    
    years = np.arange(len(years_list))    
    width = 0.8      # the width of the bars: can also be len(x) sequence
    
    plt.figure(figsize=(10, 5)) 
    
    p1 = plt.bar(years, first_qty, width)
    p2 = plt.bar(years, second_qty,  width, bottom=first_qty)
    plt.ylabel('Accidents')
    plt.title('U.S. Airline Accidents from 1983-2014')
    plt.xticks(years, years_list, rotation='vertical', fontsize = 10)
    #plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ('Fatal', 'Non-Fatal'))
    
# Reference- https://plotly.com/python/bar-charts/    
def create_auto_accidents_stacked_bar():
    # get data
    accidents = read_auto_accidents_file()
    
    #accidents['Accidents_Non_Fatal'] = accidents['Accidents_All'] - accidents['Accidents_Fatal']
    
    #years_list = accidents['Year']values.astype(int).flatten().tolist()
    years_list = accidents['Year'].values.flatten().tolist()
#    first_qty =  accidents['Accidents_Fatal'].values.flatten().values.flatten().tolist()
#    second_qty =  accidents['Accident _Non_Fatal'].values.flatten().values.flatten().tolist()
    
    first_qty =  accidents['Fatal']
    second_qty =  accidents['Injury']
    third_qty =  accidents['Property-Damage-Only']


    
#    # Heights of bars1 + bars2
    bars_first_second = np.add(first_qty, second_qty).tolist()

    
    years = np.arange(len(years_list))    
    width = 0.8      # the width of the bars: can also be len(x) sequence
    
    plt.figure(figsize=(6, 6)) 
    
    p1 = plt.bar(years, first_qty, width)
    p2 = plt.bar(years, second_qty,  width, bottom=first_qty)
    p3 = plt.bar(years, third_qty,  width, bottom=bars_first_second)
    plt.ylabel('Accidents')
    plt.title('U.S. Auto Accidents from 2010-2018')
    plt.xticks(years, years_list, rotation='vertical', fontsize = 10)
    #plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0], p3[0]), ('Fatal', 'Injury', 'Property Damage Only'))
    
# https://datatofish.com/line-chart-python-matplotlib/
def create_revenue_line_chart():
    # get data
    airline_df =  read_airline_revenue_file()
    airline_array = ['American','Delta','United','Southwest','Frontier','Alaska','Hawaiian','Spirit']
    # Need to transpose the data due to the file setup
    #https://towardsdatascience.com/transform-reality-with-pandas-96f061628030
    airline_df =  airline_df.set_index('Airline')
    airline_df = airline_df.transpose()
    #print(airline_df)  
    #print(airline_df['American'])
      
    plt.figure(figsize=(6, 4)) 
    years_list = airline_df.index.values.flatten().tolist()
    years = np.arange(len(years_list))
    
    for airline in airline_array:
        plt.plot(years, airline_df[airline])
        
    plt.title('U.S. Airline Passenger Revenue')
    plt.xlabel('Year')
    plt.ylabel('Revenue (millions USD)')
    plt.xticks(years, years_list, rotation='vertical', fontsize = 10)
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left') # 
    plt.show()
    
# https://datatofish.com/line-chart-python-matplotlib/
def create_passengers_line_chart():
    # get data
    airline_df =  read_passengers_file()
    airline_array = ['American','Delta','United','Southwest','Frontier','Alaska','Hawaiian','Spirit']
    # Need to transpose the data due to the file setup
    #https://towardsdatascience.com/transform-reality-with-pandas-96f061628030
    airline_df =  airline_df.set_index('Airline')
    airline_df = airline_df.transpose()
    #print(airline_df)  
    #print(airline_df['American'])
      
    plt.figure(figsize=(6, 4)) 
    years_list = airline_df.index.values.flatten().tolist()
    years = np.arange(len(years_list))
    
    for airline in airline_array:
        plt.plot(years, airline_df[airline])
        
    plt.title('U.S. Airline Enplaned Passengers')
    plt.xlabel('Year')
    plt.ylabel('Passengers (thousands)')
    plt.xticks(years, years_list, rotation='vertical', fontsize = 10)
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left') # 
    plt.show()
     
    
def main():
    
    create_top_airline_incidents_bar()
    create_top_airline_fatalities_bar()
    create_accidents_stacked_bar()
    create_auto_accidents_stacked_bar()
    create_revenue_line_chart()
    create_passengers_line_chart()

 
if __name__ == '__main__':
    main()
    
