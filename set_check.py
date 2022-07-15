import threading
import time
import os

set_ = 'Set'
txt = '.txt'

def timer_1():
    os.system (r'launch_fonbet.py')
def timer_2():
    os.system (r'parser_score_set.py')

tim1 = threading.Timer(0.0, timer_1)
tim2 = threading.Timer(0.0, timer_2)

for i in range(0,5):
    h = i
    h += 1
    h = str(h)
    href = set_ + h + txt
    f = open(href, 'r')
    set_game = f.read()
    f.close()
    if set_game != '':
        break
    else:
        print('Error!')

while flag == True:
    flag_bet = 'False'
    f = open('global_prog.txt', 'r')
    flag_txt = f.read()
    f.close()
    if flag_txt == 'True':
        while True:
            h = int(h)
            h += 1
            h = str(h)
            href = set_ + h + txt
            while set_game_new == '':
                f = open(href, 'r')
                set_game_new = f.read()
                f.close()
                if set_game_new != '':
                    f = open('flag_set.txt', 'w')
                    f.write('True')
                    f.close()
                    time.sleep(5)
                    tim1.start()
                    time.sleep(3)
                    tim2.start()
                    break
                else:
                    pass
    else:
        flag = False
