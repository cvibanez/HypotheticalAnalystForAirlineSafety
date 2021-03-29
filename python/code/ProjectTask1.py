# Conrad Ibanez
# DSC640 Winter 2020
# Project Task 1: Dashboard

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.offline import iplot


def read_airline_safety_file():
    # read the csv file
    airline_safety_df = pd.read_csv("../../data/airline-safety.csv")
    # Remove asterisk in airline name
    airline_safety_df['airline'] = airline_safety_df['airline'].str.replace('*','')
    return airline_safety_df

def read_auto_fatalities_file():
    # read the csv file
    auto_fatalities_df = pd.read_excel("../../data/Fatalities and Fatality Rates_1899-2018_Clean.xls")
    return auto_fatalities_df

def read_us_airline_fatalities_file():
    # read the csv file
    us_airline_fatalities_df = pd.read_csv("../../data/table9_2014-accidents_ntsb-classification-1995-2014-for-u-s-air-carriers_Clean.csv")
    return us_airline_fatalities_df


# Reference- https://plotly.com/python/horizontal-bar-charts/
def create_airline_safety_horizontal_bar():
    # get data
    airline_safety_df = read_airline_safety_file()
    
    # Sort data by available seat km
    airline_safety_df = airline_safety_df.sort_values(by=['avail_seat_km_per_week'])
    
    airline_names = airline_safety_df['airline'] + ' (' + airline_safety_df['avail_seat_km_per_week'].map(str) + ')'
    
    airlines = airline_names.tolist()
    y_pos = np.arange(len(airlines))
    quantity = airline_safety_df['fatalities_00_14'].tolist()
    
    fig, ax = plt.subplots(figsize=(15,15))

    ax.barh(y_pos, quantity)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(airlines)
    #ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Fatalities')
    ax.set_ylabel('Airline (Available Seat km Per Week)')
    ax.set_title('Airlines Ordered by Available Seat km Per Week and Number of Fatalities 2000-2014')

    plt.show()

def create_top_airline_fatalities_bar():
    # get data
    airline_safety_df = read_airline_safety_file()
    
    # Sort data by available seat km
    airline_safety_df = airline_safety_df.sort_values(by=['fatalities_00_14'])
    
    # Take top 10
    #airline_safety_df = airline_safety_df[:20]
    #airline_names = airline_safety_df['airline'] + ' (' + airline_safety_df['avail_seat_km_per_week'].map(str) + ')'
    
    airlines = airline_safety_df['airline'].tolist()
    y_pos = np.arange(len(airlines))
    quantity = airline_safety_df['fatalities_00_14'].tolist()
    
    fig, ax = plt.subplots(figsize=(15,15))

    ax.barh(y_pos, quantity)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(airlines)
    #ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Fatalities')
    ax.set_title('Airlines Ordered by Available Seat km Per Week and Number of Fatalities 2000-2014')

    plt.show()
    
def create_airline_incidents_fatal_bar2():
    # get data
    airline_safety_df = read_airline_safety_file()
    
    # Sort data by available seat km
    airline_safety_df = airline_safety_df.sort_values(by=['avail_seat_km_per_week'])
    
    airlines = airline_safety_df['airline']


    y_pos = np.arange(len(airlines))
    width = 0.4
    
    fig, ax = plt.subplots(figsize=(15,15))
    
    ax.barh(y_pos, airline_safety_df['incidents_00_14'], width, color='red', label='Incidents')
    ax.barh(y_pos + width, airline_safety_df['fatal_accidents_00_14'], width, color='green', label='Fatal Accidents2')
    
    
    
    ax.set(yticks=y_pos + width, yticklabels=airlines, ylim=[2*width - 1, len(airlines)])
    ax.legend(loc='lower right')
    
    #ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Counts')
    ax.set_title('Airlines Ordered by Available Seat km Per Week and Incidents and Fatal Accidents 2000-2014')
    plt.show()
  
def create_airline_incidents_fatal_bar():
    # get data
    airline_safety_df = read_airline_safety_file()
    
    # Sort data by available seat km
    airline_safety_df = airline_safety_df.sort_values(by=['incidents_00_14'], ascending=False)
    
    # Take top 10
    #airline_safety_df = airline_safety_df[:20]
    #airline_names = airline_safety_df['airline'] + ' (' + airline_safety_df['avail_seat_km_per_week'].map(str) + ')'
    
    
    labels = airline_safety_df['airline']
    
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, airline_safety_df['incidents_00_14'], width, label='Incidents')
    rects2 = ax.bar(x + width/2, airline_safety_df['fatal_accidents_00_14'], width, label='Fatal Accidents')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Counts')
    ax.set_title('Airlines by incidents and fatal accidents')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    
    
    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    
    
    autolabel(rects1)
    autolabel(rects2)
    
    fig.tight_layout()
    
    plt.show()


def main():
    
    create_airline_safety_horizontal_bar()
    #create_top_airline_fatalities_bar()
    #create_airline_incidents_fatal_bar()
    #create_airline_incidents_fatal_bar()
    create_airline_incidents_fatal_bar2()

 
if __name__ == '__main__':
    main()
    
