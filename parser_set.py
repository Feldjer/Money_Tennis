from bs4 import BeautifulSoup
import urllib.request
import time
import threading
import os

set_line = ''
set_name = ''
set_qualification = ''

def timer_1():
    os.system (r'parser_score_set.py')

tim1 = threading.Timer(0.0, timer_1)

soup = BeautifulSoup(open('html_code_set.txt', encoding='utf-8'), 'html.parser')

for i in soup.find_all('a', class_='h-interactive js-event-link'):
    name = i.text
    name = str(name)
    set_name += name
    set_name = set_name.replace('\n', '')
    set_name = set_name.replace('               ', '')

for i in soup.find_all('a', class_='js-link', rel='nofollow'):
    qual = i.text
    qual = str(qual)
    set_qualification += qual
    set_qualification = set_qualification.replace('\n', '')
    set_qualification = set_qualification.replace(' ', '')

len1 = len(set_qualification)
a2 = len1
a1 = len1-1

#ATP, WTA, ITF
while True:
    simvol = set_qualification[a1:a2]
    if (simvol == 'F') or (simvol == 'A') or (simvol == 'P') or (simvol == 'м') or (simvol == 'л'):
        simvol_dop = set_qualification[a1-2:a2]
        if (simvol_dop == 'WTA') or (simvol_dop == 'ATP'):
            game = set_qualification[a1-2:len1]
            break
        elif simvol_dop == 'ITF':
            simvol_dop = set_qualification[a1-3:a2+1]
            if simvol_dop == '-ITF-':
                a1 -= 4
                a2 -= 4
            else:
                game = set_qualification[a1-2:len1]
                break
        elif simvol_dop == 'ыйм':
            simvol_dop = set_qualification[a1-11:a2+3]
            if simvol_dop == 'Выставочныйматч':
                game = set_qualification[a1-11:len1]
                break
        elif simvol_dop == 'елл':
            simvol_dop = set_qualification[a1-3:a2+6]
            if simvol_dop == 'Челленджер':
                game = set_qualification[a1-3:len1]
                break
        else:
            a1 -= 1
            a2 -= 1
    else:
        a1 -= 1
        a2 -= 1
        
game = game.replace('ATP', 'ATP ')
game = game.replace('WTA', 'WTA ')
game = game.replace('ITF', 'ITF ')
game = game.replace('ATP Женщины', 'ATP Женщины. ')
game = game.replace('WTA', 'WTA. ')
game = game.replace('ITF Мужчины', 'ITF Мужчины. ')
game = game.replace('ITF Женщины', 'ITF Женщины. ')
game = game.replace(',', ', ')
game = game.replace('-ITF -', '-ITF-')

f = open('data.txt', 'w', encoding='utf-8')
f.write(game + '\n' + set_name)
f.close()

tim1.start()

flag = True
while flag == True:
        set_line = ''
        f = open('global_prog.txt', 'r')
        flag_txt = f.read()
        f.close()
        if flag_txt == 'True':
            for i in soup.find_all('span', class_='js-event-status-description js-event-widget-header-timer-container live '):
                line = i.text
                line = str(line)
                set_line += line
            if set_line == '1-ый сет':
                f = open('Set1.txt', 'w')
                f.write(set_line)
                f.close()
            elif set_line == '2-ой сет':
                f = open('Set2.txt', 'w')
                f.write(set_line)
                f.close()
            elif set_line == '3-ий сет':
                f = open('Set3.txt', 'w')
                f.write(set_line)
                f.close()
            elif set_line == '4-ый сет':
                f = open('Set4.txt', 'w')
                f.write(set_line)
                f.close()
            elif set_line == '5-ый сет':
                f = open('Set5.txt', 'w')
                f.write(set_line)
                f.close()
            else:
                print('Error!')
            time.sleep(15)
        else:
            flag = False
