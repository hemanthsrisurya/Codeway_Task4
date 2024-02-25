import requests
import tkinter as tk
from tkinter import messagebox

def get_weather_data(location):
    api_key = '48823cc18c3b47dea2f105146242402'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no'
    
    response = requests.get(url)
    data = response.json()
    
    if 'error' not in data:
        weather_info = {
            'temperature': data['current']['temp_c'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph'],
            'description': data['current']['condition']['text']
        }
        return weather_info
    else:
        messagebox.showerror("Error", data['error']['message'])
        return None

def get_weather():
    location = location_entry.get()
    weather_data = get_weather_data(location)
    
    if weather_data:
        weather_display.config(text=f"Weather in {location}: {weather_data['description']}\nTemperature: {weather_data['temperature']}°C\nHumidity: {weather_data['humidity']}%\nWind Speed: {weather_data['wind_speed']} km/h")

app = tk.Tk()
app.title("Weather Forecast App")

location_label = tk.Label(app, text="Enter city name or zip code:", padx=10, pady=10)
location_label.grid(row=0, column=0, sticky="w")

location_entry = tk.Entry(app, width=30)
location_entry.grid(row=0, column=1, padx=10, pady=10)

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather)
get_weather_button.grid(row=1, column=0, columnspan=2, pady=10)

weather_display = tk.Label(app, text="", padx=10, pady=10, borderwidth=2, relief="groove")
weather_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="w")

app.mainloop()
