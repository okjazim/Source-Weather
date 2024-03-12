import tkinter as gui
import requests as req
from tkinter import messagebox
from PIL import Image , ImageTk
import ttkbootstrap as gui2
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_key')}"
    try:
        res = req.get(url)
        res.raise_for_status()  
    except req.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch weather data")
        return None
    
    weather = res.json()
    if 'weather' not in weather or 'main' not in weather or 'sys' not in weather:
        messagebox.showerror("Error", "Invalid weather data received")
        return None

    weather_icon = weather["weather"][0]["icon"]
    temperature_kelvin = weather['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15
    weather_desc = weather['weather'][0]['description']
    city_name = weather['name']
    country = weather['sys']['country']
    
    icon_url = f'https://openweathermap.org/img/wn/{weather_icon}.png'
    return (icon_url, temperature_celsius, weather_desc, city_name, country)
    

def search(event=None):
    configure()
    city = city_search.get()
    result = weather(city)
    if result is None:
        return
    
    icon_url, temperature_celsius, weather_desc, city_name, country = result
    location_name.config(text=f"{city_name}, {country}")
    
    try:
        image = Image.open(req.get(icon_url, stream=True).raw)
        icon = ImageTk.PhotoImage(image)
        app_icon.config(image=icon)
        app_icon.image = icon
    except req.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch icon: {str(e)}")

    location_temp.config(text=f"Temperature: {temperature_celsius:.2f}°C")
    location_descp.config(text=f"Description: {weather_desc}")
    
    city_search.focus_set()  

initial = gui2.Window(themename="solar")
initial.title("Source Weather")
initial.iconbitmap(r"cloudy_DIU_icon.ico")
initial.geometry("400x350")

city_search = gui2.Entry(initial, font="8514oem,15")
city_search.pack(pady=7)
city_search.bind("<Return>", search)

search_bar = gui2.Button(initial, text="Search City", command=search, bootstyle="warning")
search_bar.pack(pady=7)

location_name = gui.Label(initial, font="8514oem,23")
location_name.pack(pady=14)

app_icon = gui.Label(initial)
app_icon.pack()

location_temp = gui.Label(initial, font="8514oem,17")
location_temp.pack()

location_descp = gui.Label(initial, font="8514oem,17")
location_descp.pack()

initial.mainloop()


