# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:08:02 2020

@author: Akshat

Gets 5 day weather forecast temperature max and min plots for Colorado Springs.
"""
from api_key import api_key
from datetime import date
from datetime import timedelta
import matplotlib.pyplot as plt
import pandas as pd
import requests

# Values for getting data.
API_KEY = api_key
CITY_ID = 5417598
URL = 'https://api.openweathermap.org/data/2.5/forecast?id={}&appid={}'.format(CITY_ID, API_KEY)

def get_weather_forecast():
    """Get weather data from openweathermap.org, returns in JSON format."""
    response = requests.get(URL)
    return response.json()
def get_dates():
    """Get the next 5 days in the openweathermap format."""
    curr_date = date.today()
    dates = []
    for i in range(1, 6):
        dates.append((curr_date + timedelta(days=i)).strftime('%Y-%m-%d'))
    return dates 
def get_forecast_max_and_min_temps(weather_json):
    """Returns specified temperatures in list by three hour blocks for the specified date.
    
       weather_json: JSON formatted data from openweathermap.
    """
    temps = []
    for data_entry in weather_json['list']:
        temps.append({'date' : data_entry['dt_txt'][:10],
                      'hour' : data_entry['dt_txt'][12:],
                      'temp_min_K': data_entry['main']['temp_min'], 
                      'temp_max_K' : data_entry['main']['temp_max']})
    return temps

def get_temp_plot(weather_data_df, forecast_date):
    """
    Generates a plot of min and max temperature for the given date.
    
    weather_data_df: pandas dataframe of temperatures with the following columns:
        date, hour, temp_min_F, temp_max_F.
    forecast_date: date string formatted to YYYY-MM-DD
    """
    fig = plt.figure(figsize=(5,5), dpi=100)
    day_df = weather_data_df[weather_data_df['date'] == forecast_date]
    plt.plot(range(day_df.shape[0]),day_df[['temp_min_F']].values, figure=fig)
    plt.plot(range(day_df.shape[0]),day_df[['temp_max_F']].values, figure=fig)
    plt.xticks(ticks = range(day_df.shape[0]),labels=day_df['hour'].values, rotation=45, ha='right', figure=fig)
    return fig

def main():
    weather_json = get_weather_forecast()
    forecast_dates = get_dates()
    temps_per_date = get_forecast_max_and_min_temps(weather_json)
    weather_data_columns = ['date', 'hour', 'temp_min_K', 'temp_max_K']
    weather_data_df = pd.DataFrame(data=temps_per_date, 
                                   columns = weather_data_columns)
    weather_data_df['temp_min_F'] = (weather_data_df['temp_min_K'] - 273.15) * 1.8 + 32
    weather_data_df['temp_max_F'] = (weather_data_df['temp_max_K'] - 273.15) * 1.8 + 32
    temp_plots = []
    for forecast_date in forecast_dates:
        temp_plots.append(get_temp_plot(weather_data_df, forecast_dates[1]))
    
    return temp_plots
    

    
if __name__ == '__main__':
    main()


