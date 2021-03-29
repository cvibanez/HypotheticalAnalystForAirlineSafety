# Conrad Ibanez
# DSC640 Winter 2020
# Project Task 3: Blog

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

def read_transportation_expenditures_file():
    # read the csv file
    data_df = pd.read_excel("../../data/task3/PersonalConsumptionExpenditures_USDeptCommerce.xlsx")
    return data_df

def read_trip_purpose_expenditures_file():
    # read the csv file
    data_df = pd.read_excel("../../data/task3/DOT_BureauTransportation_Trip_Purpose.xlsx")
    return data_df

def read_transportation_modes_file():
    # read the csv file
    data_df = pd.read_csv("../../data/task3/NationalHouseholdTravelSurvey2017_TransportationMode.csv")
    return data_df


# Reference- https://plotly.com/python/horizontal-bar-charts/
def create_airline_safety_horizontal_bar():
    # get data
    airline_safety_df = read_airline_safety_file()
    us_airlines = ['United / Continental',
                   'Delta / Northwest',
                   'American',
                   'Southwest Airlines',
                   'US Airways / America West',
                   'Virgin Atlantic',
                   'Alaska Airlines' ]
    
    # Sort data by available seat km
    airline_safety_df = airline_safety_df.sort_values(by=['avail_seat_km_per_week'])
    airline_safety_df = airline_safety_df[airline_safety_df['airline'].isin(us_airlines)]
    
    airline_names = airline_safety_df['airline']
    
    airlines = airline_names.tolist()
    y_pos = np.arange(len(airlines))
    quantity = airline_safety_df['fatalities_00_14'].tolist()
    
    fig, ax = plt.subplots(figsize=(6,4))

    ax.barh(y_pos, quantity)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(airlines)
    #ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Fatalities')
    #ax.set_ylabel('Airline')  # Looks better without as title also shows
    ax.set_title('Airline Fatalities 2000-2014')

    plt.show()


# https://datatofish.com/line-chart-python-matplotlib/
def create_expenditures_linechart():
    # get data
    data_df = read_transportation_expenditures_file()
    
    # Reference https://stackoverflow.com/questions/58812886/pandas-line-plot-without-transposing-the-dataframe
    x = data_df.columns.tolist()[1:]
    y = data_df.iloc[:, 1:].values
    for i, j in enumerate(y):
        plt.plot(x, j, label=data_df['Transportation'].iloc[i])
    plt.ylim(bottom=0)
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left') # 
    plt.xlabel('Year')
    plt.ylabel('U.S. dollars (millions)')  # Looks better without as title also shows
    plt.title('Transportation Expenditures 2010-2018')



# Reference- https://plotly.com/python/pie-charts/
def create_piechart():
    # get data
    data_df = read_transportation_modes_file()
    #print(data_df.head())
    
    items = ['Automobiles', 'Walking', 'Airplane', 'Other']
    values = []
    
    auto_modes = ['Car','SUV','Van','Pickup truck','RV (motor home, ATV, snowmobile)',
                  'Taxi / limo (including Uber / Lyft)','Rental car (Including Zipcar / Car2Go)']
    
    auto_df = data_df[data_df['Type'].isin(auto_modes)]
    auto_sum = auto_df['Percent'].sum()
    #print("autosum",auto_sum)
    walking_row = data_df[data_df['Type']=='Walk']
    #print(walking_row.head())
    walking_value = walking_row['Percent'].iloc[0]
    #print("walking",walking_value)
    airplane_row = data_df[data_df['Type']=='Airplane']
    #print(airplane_row.head())
    airplane_value = airplane_row['Percent'].iloc[0]
    #print("airplane",airplane_value)
    other_value = 100 - (auto_sum + walking_value + airplane_value)
    values.append(auto_sum)
    values.append(walking_value)
    values.append(airplane_value)
    values.append(other_value)
    
    
    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=items, autopct='%1.1f%%',
            shadow=True, startangle=180)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Transportation Modes')
    
    plt.show()
    
# https://datatofish.com/line-chart-python-matplotlib/
def create_trip_purpose_linechart():
    # get data
    data_df = read_trip_purpose_expenditures_file()
    
    # Reference https://stackoverflow.com/questions/58812886/pandas-line-plot-without-transposing-the-dataframe
    x = data_df.columns.tolist()[1:]
    y = data_df.iloc[:, 1:].values
    for i, j in enumerate(y):
        plt.plot(x, j, label=data_df['Trip_Purpose'].iloc[i])
    plt.ylim(bottom=0)
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left') # 
    plt.xlabel('Year')
    plt.ylabel('Average Annual Person Trips')  # Looks better without as title also shows
    plt.title('Average Annual Person Trips per Household')


def main():
    
    create_airline_safety_horizontal_bar()
    create_expenditures_linechart()
    create_piechart()
    create_trip_purpose_linechart()


 
if __name__ == '__main__':
    main()
    
