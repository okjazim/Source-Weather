import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from datetime import datetime
import ttkbootstrap as ttk
from dotenv import load_dotenv
import os


def configure_env():
    load_dotenv()


def kelvin_to_celsius(k):
    return k - 273.15


def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32


def format_unix_time(timestamp, tz_offset):
    dt = datetime.utcfromtimestamp(timestamp + tz_offset)
    return dt.strftime("%H:%M")


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Source Weather")

        try:
            self.root.iconbitmap("cloudy_DIU_icon.ico")
        except Exception as e:
            print(f"Warning: Could not load icon: {e}")

        self.root.geometry('800x600')
        self.root.minsize(800, 600)

        self.fullscreen = False

        self.style = self.root.style

        self.api_key = os.getenv('API_key')
        if not self.api_key:
            messagebox.showerror("API Key Error", "API key not found in .env file!")
            self.root.destroy()
            return

        self.top_frame = ttk.Frame(root, padding=15)
        self.top_frame.pack(side='top', fill='x')

        self.city_var = tk.StringVar(value="Berlin")
        self.city_entry = ttk.Entry(self.top_frame, textvariable=self.city_var, font=("Segoe UI", 18))
        self.city_entry.pack(side='left', fill='x', expand=True)
        self.city_entry.bind("<Return>", self.fetch_weather)

        self.search_btn = ttk.Button(self.top_frame, text="Search", command=self.fetch_weather, bootstyle='warning')
        self.search_btn.pack(side='left', padx=10)

        self.theme_btn = ttk.Button(self.top_frame, text="Toggle Theme", command=self.toggle_theme)
        self.theme_btn.pack(side='right')

        self.fs_toggle_btn = ttk.Button(self.top_frame, text="Toggle Fullscreen", command=self.toggle_fullscreen)
        self.fs_toggle_btn.pack(side='right', padx=10)

        self.weather_frame = ttk.Frame(root, padding=20)
        self.weather_frame.pack(fill='both', expand=True)

        self.location_label = ttk.Label(self.weather_frame, font=("Segoe UI", 30, "bold"))
        self.location_label.pack(pady=10)

        self.icon_temp_frame = ttk.Frame(self.weather_frame)
        self.icon_temp_frame.pack(pady=10)

        self.icon_label = ttk.Label(self.icon_temp_frame)
        self.icon_label.pack(side='left', padx=20)

        self.temp_label = ttk.Label(self.icon_temp_frame, font=("Segoe UI", 40))
        self.temp_label.pack(side='left')

        self.desc_label = ttk.Label(self.weather_frame, font=("Segoe UI", 20, "italic"))
        self.desc_label.pack(pady=10)

        self.details_frame = ttk.Frame(self.weather_frame)
        self.details_frame.pack(pady=20, fill='x')

        labels = ["Humidity: ", "Wind Speed: ", "Sunrise: ", "Sunset: "]
        self.detail_vars = {}
        for label in labels:
            frame = ttk.Frame(self.details_frame)
            frame.pack(side='left', expand=True, fill='both', padx=15)
            ttk.Label(frame, text=label, font=("Segoe UI", 16, "bold")).pack(anchor='w')
            var = tk.StringVar(value="-")
            self.detail_vars[label] = var
            ttk.Label(frame, textvariable=var, font=("Segoe UI", 16)).pack(anchor='w')

        self.unit_celsius = True
        self.unit_btn = ttk.Button(root, text="Show °F", command=self.toggle_unit, bootstyle="info")
        self.unit_btn.pack(side='bottom', pady=15)

        self.weather_data = None
        self.fetch_weather()

    def toggle_theme(self):
        current_theme = self.root.style.theme.name
        new_theme = "superhero" if current_theme == "darkly" else "darkly"
        self.root.style.theme_use(new_theme)

    def toggle_unit(self):
        self.unit_celsius = not self.unit_celsius
        self.unit_btn.config(text="Show °C" if not self.unit_celsius else "Show °F")
        if self.weather_data:
            self.update_temperature_display()

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)

    def fetch_weather(self, event=None):
        city = self.city_var.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        try:
            self.location_label.config(text="Loading...")
            self.temp_label.config(text="")
            self.desc_label.config(text="")
            for var in self.detail_vars.values():
                var.set("-")
            self.icon_label.config(image='')
            self.root.update()

            response = requests.get(url, timeout=8)
            response.raise_for_status()
            data = response.json()

            if "weather" not in data or "main" not in data or "sys" not in data:
                raise ValueError("Incomplete data received")

            self.weather_data = data
            self.update_display()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to get weather data: {str(e)}")

    def update_temperature_display(self):
        temp_k = self.weather_data['main']['temp']
        if self.unit_celsius:
            temp = kelvin_to_celsius(temp_k)
            temp_str = f"{temp:.1f} °C"
        else:
            temp = kelvin_to_fahrenheit(temp_k)
            temp_str = f"{temp:.1f} °F"
        self.temp_label.config(text=temp_str)

    def update_display(self):
        name = self.weather_data.get("name", "")
        country = self.weather_data['sys'].get("country", "")
        self.location_label.config(text=f"{name}, {country}")

        weather = self.weather_data['weather'][0]
        desc = weather.get("description", "").title()
        self.desc_label.config(text=desc)

        icon_code = weather.get("icon", "")
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@4x.png"
        try:
            icon_resp = requests.get(icon_url, stream=True, timeout=6)
            icon_resp.raise_for_status()
            image = Image.open(icon_resp.raw).resize((150, 150), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.icon_label.config(image=photo)
            self.icon_label.image = photo
        except Exception:
            self.icon_label.config(image='')
            self.icon_label.image = None

        self.update_temperature_display()

        self.detail_vars["Humidity: "].set(f"{self.weather_data['main'].get('humidity','-')} %")
        self.detail_vars["Wind Speed: "].set(f"{self.weather_data.get('wind', {}).get('speed','-')} m/s")

        tz_offset = self.weather_data.get("timezone", 0)
        sunrise = self.weather_data['sys'].get("sunrise", 0)
        sunset = self.weather_data['sys'].get("sunset", 0)
        self.detail_vars["Sunrise: "].set(format_unix_time(sunrise, tz_offset))
        self.detail_vars["Sunset: "].set(format_unix_time(sunset, tz_offset))


if __name__ == "__main__":
    configure_env()
    root = ttk.Window(themename="darkly")
    app = WeatherApp(root)
    root.mainloop()

