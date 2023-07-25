import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data(location, api_key):
    url = f"{API_URL}?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def get_temperature(data, date):
    for forecast in data["list"]:
        if forecast["dt_txt"] == date:
            return forecast["main"]["temp"]
    return None

def get_wind_speed(data, date):
    for forecast in data["list"]:
        if forecast["dt_txt"] == date:
            return forecast["wind"]["speed"]
    return None

def get_pressure(data, date):
    for forecast in data["list"]:
        if forecast["dt_txt"] == date:
            return forecast["main"]["pressure"]
    return None

def main():
    location = "London"
    api_key = "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"
    data = get_weather_data(location, api_key)
    
    if data:
        while True:
            print("Options:")
            print("1. Get weather")
            print("2. Get Wind Speed")
            print("3. Get Pressure")
            print("0. Exit")
            option = int(input("Enter your choice: "))

            if option == 1:
                date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
                temperature = get_temperature(data, date)
                if temperature is not None:
                    print(f"Temperature on {date} is {temperature}°K")
                else:
                    print("Data not available for the given date.")

            elif option == 2:
                date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
                wind_speed = get_wind_speed(data, date)
                if wind_speed is not None:
                    print(f"Wind speed on {date} is {wind_speed} m/s")
                else:
                    print("Data not available for the given date.")

            elif option == 3:
                date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
                pressure = get_pressure(data, date)
                if pressure is not None:
                    print(f"Pressure on {date} is {pressure} hPa")
                else:
                    print("Data not available for the given date.")

            elif option == 0:
                print("Exiting program.")
                break

            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
