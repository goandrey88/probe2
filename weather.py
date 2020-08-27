#easy_waether
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here
owm = OWM('my_api', config_dict)

city_name = input("Введите город/страну: ")
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city_name)
w = observation.weather

print("В " + city_name + " сейчас " + w.detailed_status)

wind_speed = w.wind()["speed"]
#temp_min = w.temperature('celsius')["temp_min"]
#temp_max = w.temperature('celsius')["temp_max"]
temp = w.temperature('celsius')["temp"]
print("Текущая темпереатура: " + str(temp) + "C")
#print("Минимальная темпереатура: " + str(temp_min))
#print("Максимальная темпереатура: " + str(temp_max))
print("Скорость ветра: " + str(wind_speed) + " м/с ")
