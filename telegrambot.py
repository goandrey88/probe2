#telegram bot weather
import telebot
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here
owm = OWM('api', config_dict)

bot = telebot.TeleBot("api")

@bot.message_handler(content_types=['text'])
def send_mes(message):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	wind_speed = w.wind()["speed"]
	temp = w.temperature('celsius')["temp"]

	answer = "В " + message.text + " сейчас " + w.detailed_status + "\n"
	answer += "Текущая темпереатура: " + str(temp) + "C" + "\n"
	answer += "Скорость ветра: " + str(wind_speed) + " м/с "

	bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True)