class WeatherService(object):
    API_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
    API_KEY = "2442280e6f8d5c75eae74e83495073c8"

    def __init__(self):
        pass

    def get_weather_data(self, city_name):
        r = requests.get(WeatherService.API_URL.format(city_name, WeatherService.API_KEY))
        wheather_data = (r.json())
        temp = self._extract_temp(wheather_data)
        description = self._extract_desc(weather_data)
        return "Atualmente, em {}, está {} graus com {}".format(city_name, temp, description)

    def _extract_temp(self, weatherdata):
        temp = weatherdata['main']['temp']
        return temp

    def _extract_desc(self, weatherdata)
    return weatherdata['weather'][0]['description']