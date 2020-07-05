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
CURRENT_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}'.format(city_id = CITY_ID,api_key = API_KEY)
FORECAST_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/forecast?id={city_id}&appid={api_key}'.format(city_id = CITY_ID,api_key =  API_KEY)

def get_weather_data(url):
    response = requests.get(url)
    return response.json()

def get_current_date():
    """Returns the current date in the YYYY-MM-DD format."""
    curr_date = date.today()
    return curr_date.strftime('%Y-%m-%d')

def get_forecast_dates():
    """Returns a list of the next 5 days in the YYYY-MM-DD format."""
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
    Generates a plot of minimum and maximum temperatures at various times for the given date.
    
    weather_data_df: pandas dataframe of temperatures with the following columns: date, hour, temp_min_F, temp_max_F.
    
    forecast_date: date string formatted to YYYY-MM-DD
    """
    fig = plt.figure(figsize=(5,5), dpi=100)
    day_df = weather_data_df[weather_data_df['date'] == forecast_date]
    plt.plot(range(day_df.shape[0]),day_df[['temp_min_F']].values, figure=fig)
    plt.plot(range(day_df.shape[0]),day_df[['temp_max_F']].values, figure=fig)
    plt.xticks(ticks = range(day_df.shape[0]),labels=day_df['hour'].values, rotation=45, ha='right', figure=fig)
    plt.xlabel(forecast_date)
    plt.ylabel('Temp (F)')
    plt.tight_layout()
    return fig

def get_forecast_dates_data():
    weather_json = get_weather_data(FORECAST_WEATHER_URL)
    forecast_dates = get_forecast_dates()
    temps_per_date = get_forecast_max_and_min_temps(weather_json)
    weather_data_columns = ['date', 'hour', 'temp_min_K', 'temp_max_K']
    weather_data_df = pd.DataFrame(data=temps_per_date, 
                                    columns = weather_data_columns)
    weather_data_df['temp_min_F'] = (weather_data_df['temp_min_K'] - 273.15) * 1.8 + 32
    weather_data_df['temp_max_F'] = (weather_data_df['temp_max_K'] - 273.15) * 1.8 + 32
    temp_plots = []
    for forecast_date in forecast_dates:
        temp_plots.append(get_temp_plot(weather_data_df, forecast_date))
    return temp_plots
    
def get_current_date_data():
    """Returns the following in a dictionary for the current date from openweathermap: 
        weather type, weather description, temperature, felt temperature, 
        humidity, wide speed, and wind direction"""
        
    curr_weather_json = get_weather_data(CURRENT_WEATHER_URL)
    weather = curr_weather_json['weather'][0]['main']
    weather_desc = curr_weather_json['weather'][0]['description']
    temp = curr_weather_json['main']['temp']
    temp_feeling = curr_weather_json['main']['feels_like']
    humidity = curr_weather_json['main']['humidity']
    wind_speed = curr_weather_json['wind']['speed']
    wind_direct = curr_weather_json['wind']['deg']
    
    curr_weather_data = {'weather' : weather, 
                         'weather_desc' : weather_desc, 
                         'temp' : temp, 
                         'temp_feeling' : temp_feeling, 
                         'humidity' : humidity, 
                         'wind_speed' : wind_speed, 
                         'wind_direct' : wind_direct}
    return curr_weather_data

def main():
    return get_current_date_data(), get_forecast_dates_data()

if __name__ == '__main__':
    main()


