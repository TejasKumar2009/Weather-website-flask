#Importing Required Modules
from flask import Flask, render_template, request
import requests
from datetime import date
from datetime import datetime
import json
import datetime

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])

#Creating Home Function
def home():
    # Handling City Input
    location = request.form.get('city-input')
    # Fetch Api Data
    api_key = ""
    weather_url = f"http://api.openweathermap.org/data/2.5/find?q={location}&units=metric&appid={api_key}"
    weather_api_url = requests.get(weather_url)
    weather_data = weather_api_url.json()
    data_list = weather_data['list']
    list_of_data = data_list[0]
    main_of_list = list_of_data['main']
    sys_of_list = list_of_data['sys']
    weather_of_list = list_of_data['weather']
    weather_list = weather_of_list[0]
    wind_of_list = list_of_data['wind']
    # #Info About Weather
    temp = main_of_list['temp']
    city = list_of_data['name']
    feels_like = main_of_list['feels_like']
    temp_min = main_of_list['temp_min']
    temp_max = main_of_list['temp_max']
    hum = main_of_list['humidity']
    pressure = main_of_list['pressure']
    country = sys_of_list['country']
    temp_status = weather_list['main']
    wind_speed = wind_of_list['speed']

    current_date = date.today()
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print(current_time)

    return render_template("index.html", temp=temp, city=city, feels_like=feels_like, temp_min=temp_min, temp_max=temp_max, hum=hum, pressure=pressure, country=country, temp_status=temp_status, wind_speed=wind_speed, current_date=current_date)

if __name__ == "__main__":
   app.run(debug=True)
