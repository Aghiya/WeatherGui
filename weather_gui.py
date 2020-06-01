# -*- coding: utf-8 -*-
"""
Created on Sun May 31 10:21:26 2020

@author: Akshat
"""
import get_weather_data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter.font

# Global variables
initial_city = 'Colorado Springs'
forecast_dates = get_weather_data.get_dates()
temperature_plots = get_weather_data.main()

# Initialize tkinter window.
root = tk.Tk()
root.state('zoomed')
root.title("Weather Forecast")

# Create frames for various elements
dates_frame = tk.Frame(root)
dates_frame.pack(side='top')
plot_frames = []
for i in range(5):
    plot_frames.append([i, tk.Frame(root).pack(side='top')])


def display_city(city):
    # create a custom font
    font = tkinter.font.Font(family="Helvetica", size=30)
    city_message_box = tk.Label(root, text=city, font=font, width=50)
    city_message_box.pack()
    
def insert_plot(i):
    plot = FigureCanvasTkAgg(temperature_plots[i], root)
    plot.get_tk_widget().pack()


def create_plot_change_buttons(dates_frame):
    for i in range(5):
        b = tk.Button(root, 
                      text = forecast_dates[i], 
                      height=1,width=8,
                      command= print('hello'))
        b.pack(in_=dates_frame, side='left')

def main():
    display_city(initial_city)
    create_plot_change_buttons(dates_frame)
    insert_plot(0)
    root.mainloop()
    
if __name__ == '__main__':
    main()
