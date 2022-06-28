import requests

def get_weather_desc_and_temp():
    api_key = "12a229c344a61e88b0c74e05d7fc1dd6"
    city = "São Bernardo do Campo"
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

    request = requests.get(url)
    json = request.json()
    print(json)

    description = json.get("weather")[0].get("description")
    temp_actual = json.get("main").get("temp")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {"city": city,
            "description": description,
            "temp_actual": temp_actual,
            "temp_min": temp_min,
            "temp_max": temp_max}

def main():    
    weather_dict = get_weather_desc_and_temp()
    print("Today's forecast for", weather_dict.get("city"), "is", weather_dict.get("description"))
    print("The actual temperature for", weather_dict.get("city"), "is", round(weather_dict.get("temp_actual")))
    print("The minimum temperature is", round(weather_dict.get("temp_min")))
    print("The maximum temperature is", round(weather_dict.get("temp_max")))

main()