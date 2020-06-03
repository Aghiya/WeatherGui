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
initial_city = 'Colorado Springs'
forecast_dates = get_weather_data.get_dates()
temperature_plots = get_weather_data.main()

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
        for F in (Date1, Date2, Date3, Date4, Date5):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Date1")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

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
