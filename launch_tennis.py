import threading
import os
import time

surname = ''

if surname == '':
    surname = input('Предупреждение! Не указана фамилия игрока! \nУкажите фамилию: ')
    while surname == '':
        surname = input('Укажите фамилию: ')
    f = open('surname.txt', 'w', encoding='utf8')
    f.write(surname)
    f.close()
else:
    pass

def timer_1():
    os.system (r'launch_fonbet.py')
def timer_2():
    os.system (r'launch_sofascore.py')

tim1 = threading.Timer(0.0, timer_1)
tim2 = threading.Timer(0.0, timer_2)

tim1.start()

time.sleep(30)

tim2.start()

time.sleep(30)


def timer_3():
    os.system (r'launch_threatment.py')
def timer_4():
    os.system (r'launch_bet.py')

    
tim3 = threading.Timer(0.0, timer_3)

time.sleep(5)

tim4 = threading.Timer(0.0, timer_4)

tim3.start()
tim4.start()
