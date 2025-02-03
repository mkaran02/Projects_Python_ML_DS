#tkinter  (python standard library for creating  GUI)
#open weather map api (Provide weather data for any location in the world)#need to create an account on
#openweathermap.org to get the api key

import tkinter as tk
import requests

def get_weather(city,api_key):
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response=requests.get(url)

    #response.status_code==200
    if response.status_code==200:
        data = response.json()
        weather=data['weather'][0]['description']
        temperature=data['main']['temp']
        humidity=data['main']['humidity']
        wind_speed=data['wind']['speed']
        return f'weather : {weather.capitalize()}\nTemperature : {temperature}°C \nHumidity : {humidity}%\n Wind Speed : {wind_speed} m/s'
    else:
        return "City not found or API error."
    
def show_weather():
    city = city_entry.get()
    api_key= '0e6c54973c75a0295469041b83aafde1'
    weather_info= get_weather(city,api_key)
    result_label.config(text=weather_info)


window =tk.Tk()    
window.title('Weather App')

city_label=tk.Label(window, text="Enter City Name")
city_label.pack()

city_entry=tk.Entry(window)
city_entry.pack()

get_weather_button = tk.Button(window, text="get weather", command= show_weather)
get_weather_button.pack()

result_label = tk.Label(window , text="", justify= tk.LEFT)
result_label.pack()

window.mainloop()

#lets see Output