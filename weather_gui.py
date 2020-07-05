# -*- coding: utf-8 -*-
"""
Created on Sun May 31 10:21:26 2020

@author: Akshat

Note: The majority of the code was taken from the excellent example given by Bryan Oakley
primarily for his demonstration on how to quickly switch between frames.

https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
"""
import get_weather_data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter.font

# Global variables
city = 'Colorado Springs'
forecast_dates = get_weather_data.get_forecast_dates()
temperature_plots = get_weather_data.get_forecast_dates_data()
current_date_data = get_weather_data.get_current_date_data()

# Defines main GUI and every frame inside it.
class WeatherGui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkinter.font.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (CurrDate, Date1, Date2, Date3, Date4, Date5):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("CurrDate")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        
class CurrDate(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="CurrDate", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        dates_frame = tk.Frame(self)
        dates_frame.pack()
        
        weather_data = tk.Text(self, height = 5, width = 52)
        weather_data.insert("1.0","The weather is currently " + str(current_date_data['weather_desc']) + ".\n")
        weather_data.insert("2.0","The temperature is currently " 
                            + str(current_date_data['temp']) + " K, but it feels like " 
                            + str(current_date_data['temp_feeling']) + " K.\n")
        weather_data.insert("3.0", "The humidity is " + str(current_date_data['humidity']) + "%.\n")
        weather_data.insert("4.0", "The wind is blowing " + str(current_date_data['wind_speed'])
                            + " at " + str(current_date_data['wind_direct']) + " m/s.\n")
        
        button1 = tk.Button(self, text="Current Weather",
                            command=lambda: controller.show_frame("CurrDate"))
        button2 = tk.Button(self, text=forecast_dates[0],
                            command=lambda: controller.show_frame("Date1"))
        button3 = tk.Button(self, text=forecast_dates[1],
                            command=lambda: controller.show_frame("Date2"))
        button4 = tk.Button(self, text=forecast_dates[2],
                            command=lambda: controller.show_frame("Date3"))
        button5 = tk.Button(self, text=forecast_dates[3],
                            command=lambda: controller.show_frame("Date4"))
        button6 = tk.Button(self, text=forecast_dates[4],
                            command=lambda: controller.show_frame("Date5"))
        
        button1.pack(in_=dates_frame, side='left')
        button2.pack(in_=dates_frame, side='left')
        button3.pack(in_=dates_frame, side='left')
        button4.pack(in_=dates_frame, side='left')
        button5.pack(in_=dates_frame, side='left')
        button6.pack(in_=dates_frame, side='left')
        weather_data.pack()

# Frame 1.
class Date1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=forecast_dates[0], font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        dates_frame = tk.Frame(self)
        dates_frame.pack()
        
        plot = FigureCanvasTkAgg(temperature_plots[0], self)

        button1 = tk.Button(self, text="Current Weather",
                            command=lambda: controller.show_frame("CurrDate"))
        button2 = tk.Button(self, text=forecast_dates[0],
                            command=lambda: controller.show_frame("Date1"))
        button3 = tk.Button(self, text=forecast_dates[1],
                            command=lambda: controller.show_frame("Date2"))
        button4 = tk.Button(self, text=forecast_dates[2],
                            command=lambda: controller.show_frame("Date3"))
        button5 = tk.Button(self, text=forecast_dates[3],
                            command=lambda: controller.show_frame("Date4"))
        button6 = tk.Button(self, text=forecast_dates[4],
                            command=lambda: controller.show_frame("Date5"))
        
        button1.pack(in_=dates_frame, side='left')
        button2.pack(in_=dates_frame, side='left')
        button3.pack(in_=dates_frame, side='left')
        button4.pack(in_=dates_frame, side='left')
        button5.pack(in_=dates_frame, side='left')
        button6.pack(in_=dates_frame, side='left')
        plot.get_tk_widget().pack()
        plot.get_tk_widget().pack()
        
# Frame 2.
class Date2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=forecast_dates[1], font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        dates_frame = tk.Frame(self)
        dates_frame.pack()
        
        plot = FigureCanvasTkAgg(temperature_plots[1], self)

        button1 = tk.Button(self, text=forecast_dates[0],
                            command=lambda: controller.show_frame("Date1"))
        button2 = tk.Button(self, text=forecast_dates[1],
                            command=lambda: controller.show_frame("Date2"))
        button3 = tk.Button(self, text=forecast_dates[2],
                            command=lambda: controller.show_frame("Date3"))
        button4 = tk.Button(self, text=forecast_dates[3],
                            command=lambda: controller.show_frame("Date4"))
        button5 = tk.Button(self, text=forecast_dates[4],
                            command=lambda: controller.show_frame("Date5"))
        
        button1.pack(in_=dates_frame, side='left')
        button2.pack(in_=dates_frame, side='left')
        button3.pack(in_=dates_frame, side='left')
        button4.pack(in_=dates_frame, side='left')
        button5.pack(in_=dates_frame, side='left')
        plot.get_tk_widget().pack()

# Frame 3.
class Date3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=forecast_dates[2], font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        dates_frame = tk.Frame(self)
        dates_frame.pack()
        
        plot = FigureCanvasTkAgg(temperature_plots[2], self)

        button1 = tk.Button(self, text=forecast_dates[0],
                            command=lambda: controller.show_frame("Date1"))
        button2 = tk.Button(self, text=forecast_dates[1],
                            command=lambda: controller.show_frame("Date2"))
        button3 = tk.Button(self, text=forecast_dates[2],
                            command=lambda: controller.show_frame("Date3"))
        button4 = tk.Button(self, text=forecast_dates[3],
                            command=lambda: controller.show_frame("Date4"))
        button5 = tk.Button(self, text=forecast_dates[4],
                            command=lambda: controller.show_frame("Date5"))
        
        button1.pack(in_=dates_frame, side='left')
        button2.pack(in_=dates_frame, side='left')
        button3.pack(in_=dates_frame, side='left')
        button4.pack(in_=dates_frame, side='left')
        button5.pack(in_=dates_frame, side='left')
        plot.get_tk_widget().pack()
        
# Frame 4.
class Date4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=forecast_dates[3], font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        dates_frame = tk.Frame(self)
        dates_frame.pack()
        
        plot = FigureCanvasTkAgg(temperature_plots[3], self)

        button1 = tk.Button(self, text=forecast_dates[0],
                            command=lambda: controller.show_frame("Date1"))
        button2 = tk.Button(self, text=forecast_dates[1],
                            command=lambda: controller.show_frame("Date2"))
        button3 = tk.Button(self, text=forecast_dates[2],
                            command=lambda: controller.show_frame("Date3"))
        button4 = tk.Button(self, text=forecast_dates[3],
                            command=lambda: controller.show_frame("Date4"))
        button5 = tk.Button(self, text=forecast_dates[4],
                            command=lambda: controller.show_frame("Date5"))
        
        button1.pack(in_=dates_frame, side='left')
        button2.pack(in_=dates_frame, side='left')
        button3.pack(in_=dates_frame, side='left')
        button4.pack(in_=dates_frame, side='left')
        button5.pack(in_=dates_frame, side='left')
        plot.get_tk_widget().pack()
        plot.get_tk_widget().pack()
        
# Frame 5.
class Date5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=forecast_dates[4], font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        dates_frame = tk.Frame(self)
        dates_frame.pack()
        
        plot = FigureCanvasTkAgg(temperature_plots[4], self)

        button1 = tk.Button(self, text=forecast_dates[0],
                            command=lambda: controller.show_frame("Date1"))
        button2 = tk.Button(self, text=forecast_dates[1],
                            command=lambda: controller.show_frame("Date2"))
        button3 = tk.Button(self, text=forecast_dates[2],
                            command=lambda: controller.show_frame("Date3"))
        button4 = tk.Button(self, text=forecast_dates[3],
                            command=lambda: controller.show_frame("Date4"))
        button5 = tk.Button(self, text=forecast_dates[4],
                            command=lambda: controller.show_frame("Date5"))
        
        button1.pack(in_=dates_frame, side='left')
        button2.pack(in_=dates_frame, side='left')
        button3.pack(in_=dates_frame, side='left')
        button4.pack(in_=dates_frame, side='left')
        button5.pack(in_=dates_frame, side='left')
        plot.get_tk_widget().pack()
    
def main():
    gui = WeatherGui()
    gui.mainloop()
    
if __name__ == '__main__':
    main()
