import requests

#Stadt aussuchen
def getTemperature(city: str):

    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "language": "de"}

    response1 = requests.get(url, params)


    latitude = response1.json()["results"][0]["latitude"]
    longitude = response1.json()["results"][0]["longitude"]

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m",
    }

    response = requests.get(url, params)

    print(f"Die Temperatur in {city} beträgt: ")
    print(response.json()['current']['temperature_2m'])

if __name__ == "__main__":
    getTemperature("Berlin")
    getTemperature("New York")







