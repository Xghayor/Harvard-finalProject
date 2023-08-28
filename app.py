import requests
import datetime
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
import time
from PIL import Image, ImageTk

def handle_button_click():
    loader.place(x=750, y=380)
    x = entry.get()
    api_key = "500d8896c9f22504fa8586dea352e7f1"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={x}&units=metric&appid={api_key}"
    
    response = requests.get(url)
    weather_data = response.json()
    
    desc = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp']
    icon = weather_data['weather'][0]['icon']
    humidity = weather_data['main']['humidity']
    speed = weather_data['wind']['speed']
    
    image_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"
    images = "https://source.unsplash.com/1600x900/?landscape"
    
    weather_label.config(text=f"Weather in {x}", font=("Helvetica", 16))
    temp_label.config(text=f"{temp}°C", font=("Helvetica", 14))
    img = Image.open(requests.get(image_url, stream=True).raw)
    img = img.resize((100, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img
    humidity_label.config(text=f"Humidity: {humidity}%", font=("Helvetica", 12))
    windspeed_label.config(text=f"Wind speed: {speed} m/s", font=("Helvetica", 12))
    
    now = datetime.datetime.now()
    img_url = f"{images}?{now.timestamp()}"
    bg_img = Image.open(requests.get(img_url, stream=True).raw)
    bg_img = bg_img.resize((800, 600), Image.ANTIALIAS)
    bg_img = ImageTk.PhotoImage(bg_img)
    bg_image_label.config(image=bg_img)
    bg_image_label.image = bg_img
    
    loader.place_forget()

root = tk.Tk()
root.title("Weather App")
root.geometry("1000x600")

entry = Entry(root, width=30)
entry.place(x=350, y=20)

pressed_button = Button(root, text="Get Weather", command=handle_button_click)
pressed_button.place(x=550, y=17)

loader = Label(root, text="Loading...", font=("Helvetica", 16))
loader.place_forget()

weather_label = Label(root, text="", font=("Helvetica", 16))
weather_label.place(x=20, y=120)

temp_label = Label(root, text="", font=("Helvetica", 14))
temp_label.place(x=20, y=160)

image_label = Label(root)
image_label.place(x=20, y=200)

humidity_label = Label(root, text="", font=("Helvetica", 12))
humidity_label.place(x=20, y=320)

windspeed_label = Label(root, text="", font=("Helvetica", 12))
windspeed_label.place(x=20, y=350)

bg_image_label = Label(root)
bg_image_label.place(x=220, y=0)

root.mainloop()
