from tkinter import *
from PIL import ImageTk, Image
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        city = textfield.get()

        api_key = "bf1394f8b3cc7351ef31da96f1d9b073"

        geolocator = Nominatim(user_agent="geoapiExcersises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)


        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        weather_name.config(text="CURRENT WEATHER")

        # Weather
        weather_data = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        json_data = requests.get(weather_data).json()
        condition = json_data['weather'][0]['main']
        descriptiton = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"]-273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=descriptiton)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Location")


""" Creating the search box """
search_image = ImageTk.PhotoImage(Image.open("search.png"))
search_label = Label(root, image=search_image)
search_label.place(x=20, y=20)

# Creating the textfield
textfield = Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

# Creating the search button
search_icon = ImageTk.PhotoImage(Image.open("search_icon.png"))
search_button = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
search_button.place(x=390, y=34)

""" Creating the Logo """
logo_image = ImageTk.PhotoImage(Image.open("logo.png"))
logo_label = Label(image=logo_image)
logo_label.place(x=150, y=110)


""" Creating Frame Box """
frame_image = ImageTk.PhotoImage(Image.open("box.png"))
frame_label = Label(image=frame_image)
frame_label.pack(padx=5, pady=10, side=BOTTOM)

""" TIME """
weather_name = Label(root, font=("arial", 15, "bold"))
weather_name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

""" Creating Labels for the Frame Box """
wind_label = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
wind_label.place(x=120, y=395)

humidity_label = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
humidity_label.place(x=250, y=395)

description_label = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
description_label.place(x=430, y=395)

pressure_label = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
pressure_label.place(x=650, y=395)

# I don't know what this is yet
t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=130)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)


""" Creating the actual output placeholders for boxes """
w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=425)

h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=250, y=425)

d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=430, y=425)

p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=650, y=425)


root.mainloop()