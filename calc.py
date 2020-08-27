#Калькулятор

from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.RED)
what = input( "Введите операцию (+,-,*,/): " )

print(Fore.CYAN)
a = float (input("Введите первое число: "))
b = float (input("Введите второе число: "))

print(Fore.GREEN)
if what == "+":
    c = a + b
    print ("Результат: " + str(c))
elif what == "-":
    c = a - b
    print ("Результат: " + str(c))
elif what == "*":
    c = a * b
    print ("Результат: " + str(c))
elif what == "/":
    c = a / b
    print ("Результат: " + str(c))
else:
    print ("Неправильная операция")

input()