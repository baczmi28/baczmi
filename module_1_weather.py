# ================================================
#               MODULE 1 - WEATHER
# ================================================

import requests
import matplotlib.pyplot as plt

def find_city(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    parameters = {
        "name": city,
        "count": 1,
        "language": "pl",
        "format": "json",
        "countryCode": "PL"
    }

    response = requests.get(url, params=parameters)
    data = response.json()

    if "results" not in data:
        print("Nie znaleziono takiego miasta")
        return None

    city_data = data["results"][0]

    location = {
        "name": city_data["name"],
        "country": city_data["country"],
        "latitude": city_data["latitude"],
        "longitude": city_data["longitude"],
    }

    return location

def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    parameters = {
        "latitude": latitude,
        "longitude": longitude,

        "current": [
            "temperature_2m",        # temperatura
            "apparent_temperature",  # temperatura odczuwalna
            "relative_humidity_2m",  # wilgotność
            "cloud_cover",           # zachmurzenie
            "precipitation",         # opady
            "surface_pressure",      # ciśnienie
            "wind_speed_10m"         # prędkość wiatru
        ],

        "hourly": [
            "temperature_2m"
        ],

        "daily":[
            "sunrise",               # wschód słońca
            "sunset",                # zachód słońca
            "precipitation_sum",     # suma opadów
            "uv_index_max"           # maksymalny indeks UV
        ],

        "timezone": "auto",
        "forecast_days": 1
    }

    response = requests.get(url, params=parameters)
    weather = response.json()

    return weather


def show_chart(weather_data):

    hourly = weather_data['hourly']

    time = hourly['time']
    temperature = hourly['temperature_2m']

    # Numery kolejnych godzin
    x = list(range(len(time)))

    hours = []

    for one_time in time:
        hour = one_time.split('T')[1]
        hours.append(hour)

    date = time[0].split('T')[0]

    plt.figure(figsize=(10, 6))

    plt.plot(x, temperature)

    plt.title("Prognoza temperatury")
    plt.xlabel("Godzina")
    plt.ylabel("Temperatura [°C]")

    plt.xticks(
        [0, 3, 6, 9, 12, 15, 18, 21],
        ["00:00", "03:00", "06:00", "09:00", "12:00", "15:00", "18:00", "21:00"]
    )

    plt.tight_layout()
    plt.show()


def weather_module():
    print()
    print("=" * 50)
    print("WEATHER")
    print("=" * 50)

    city = input("Podaj nazwę miasta: ")

    location = find_city(city)

    if location is None:
        input("\nNaciśnij ENTER, aby wrócić do menu")
        return

    weather = get_weather(
        location["latitude"],
        location["longitude"]
    )

    now = weather["current"]
    today = weather["daily"]

    print()
    print("Miasto:", location["name"])
    print("Kraj:", location["country"])

    print()
    print("Temperatura:", now["temperature_2m"], "°C")
    print("Temperatura odczuwalna:", now["apparent_temperature"], "°C")
    print("Wilgotność:", now["relative_humidity_2m"], "%")
    print("Zachmurzenie:", now["cloud_cover"], "%")
    print("Opady:", now["precipitation"], "mm")
    print("Ciśnienie:", now["surface_pressure"], "hPa")
    print("Wiatr:", now["wind_speed_10m"], "km/h")

    print()
    print("Suma opadów dzisiaj:", today["precipitation_sum"][0], "mm")
    print("Wschód słońca:", today["sunrise"][0])
    print("Zachód słońca:", today["sunset"][0])
    print("Maksymalny indeks UV:", today["uv_index_max"][0])

    show_chart(weather)

    input("\nNaciśnij ENTER, aby wrócić do menu")
