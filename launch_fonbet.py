from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os

sbros = '\n'
pusto = ''
flag = True

print('Module: Fonbet ...................................... Launch')

f = open('surname.txt', 'r')
surname = f.read()
f.close()

f = open('set.txt','r')
set_game = f.read()
f.close()

driver = webdriver.Firefox()
driver.get('https://www.fonbet.ru/#!/live/tennis')
time.sleep(7)
driver.find_element_by_xpath('//*[@id="headerContainer"]/div/header/div[2]/div[4]/div/a').click()
driver.find_element_by_xpath('//*[@id="auth_form"]/div/div/div[2]/form/div[1]/input').send_keys('79326094661')
driver.find_element_by_xpath('//*[@id="auth_form"]/div/div/div[2]/form/div[2]/input').send_keys('X5z-2wA-48G-aeS')
driver.find_element_by_xpath('//*[@id="auth_form"]/div/div/div[2]/form/div[3]/div[2]/button/div/span').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/header/div[2]/div[3]/span/a/i').click()
driver.find_element_by_xpath('/html/body/div[1]/div/header/div[2]/div[3]/span/span/a[2]/i').click()
time.sleep(4)
driver.find_element_by_partial_link_text(surname).click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/section/div[1]/div[2]/span[2]').click()
driver.find_element_by_xpath('/html/body/div[1]/div/header/div[2]/div[3]/span/a/i').click()
driver.find_element_by_xpath('/html/body/div[1]/div/header/div[2]/div[3]/span/span/a[1]/span').click()
time.sleep(2)

while flag == True:
    flag_bet = 'False'
    f = open('global_prog.txt', 'r')
    flag_txt = f.read()
    f.close()
    if flag_txt == 'True':

        f = open('flag_set.txt', 'r')
        flag = f.read()
        f.close()
        if flag == 'True':
            break
        
        while flag_bet == 'False':
            f = open('flag_bet.txt', 'r')
            flag_bet = f.read()
            f.close()

        f = open('flag_bet.txt', 'w')
        f.write('False')
        f.close()

        f = open('bet1.txt', 'r')
        stavka1 = f.read()
        print(stavka1)
        f.close()

        f = open('bet2.txt', 'r')
        stavka2 = f.read()
        print(stavka2)
        f.close()

        f = open('bet1yorn.txt', 'r')
        yorn1 = f.read()
        print(yorn1)
        f.close()

        f = open('bet2yorn.txt', 'r')
        yorn2 = f.read()
        print(yorn2)
        f.close()

        f = open('bets.txt','w')
        f.write(pusto)
        f.close()

        kchet1 = 0
        kchet2 = 0
        list_ = driver.find_elements_by_class_name('_type_head')[0].text

        if list_ == 'Геймы':
            for i in range(0,50):
                checklist = driver.find_elements_by_class_name('_type_text')[i].text
                list_2 = checklist[0:17]
                if list_2 == 'Кто выиграет гейм':
                    kchet1 += 1
                else:
                    list_2 = checklist[0:4]
                    if list_2 == 'Гейм':
                        kchet2 += 1
                    else:
                        break
                    stavka = checklist[0:24]
                    stavka = stavka + sbros
                    f = open('bets.txt', 'a')
                    f.write(stavka)
                    f.close()

            dop = kchet1 * 2
            f = open('bets.txt', 'r')
            stavki = f.read()
            f.close()
            
            stroka1 = 0
            a1 = 0
            a2 = 24
            s = 1
            for i in range (kchet2):
                if stavki[a1:a2] == stavka1:
                    stroka1 = s
                s += 1
                a1 += 25
                a2 += 25
                
            if stroka1 == 0:
                pass
            else:
                if yorn1 == 'нет':
                    str1 = (stroka1 * 2)
                else:
                    str1 = (stroka1 * 2) - 1

                schetchik1 = dop + str1

                for i in range(schetchik1):
                    if i == schetchik1 - 1:
                        typebtn = driver.find_elements_by_class_name('_type_btn')[i].click()
                        time.sleep(1)
                        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/aside/div/div[2]/div[2]/div[1]/div/div[7]/div[1]').click()
                time.sleep(5)

        #################### 2 ставка ############################

            kchet1 = 0
            kchet2 = 0

            for i in range(0,50):
                checklist = driver.find_elements_by_class_name('_type_text')[i].text
                list_2 = checklist[0:17]
                if list_2 == 'Кто выиграет гейм':
                    kchet1 += 1
                else:
                    list_2 = checklist[0:4]
                    if list_2 == 'Гейм':
                        kchet2 += 1
                    else:
                        break
                    stavka = checklist[0:24]
                    stavka = stavka + sbros
                    f = open('bets.txt', 'a')
                    f.write(stavka)
                    f.close()

            dop = kchet1 * 2
            f = open('bets.txt', 'r')
            stavki = f.read()
            f.close()

            stroka2 = 0
            a1 = 0
            a2 = 24
            s = 1
            for i in range (kchet2):
                if stavki[a1:a2] == stavka2:
                    stroka2 = s
                s += 1
                a1 += 25
                a2 += 25

            if stroka2 == 0:
                pass
            else:
                if yorn2 == 'нет':
                    str2 = (stroka2 * 2)
                else:
                    str2 = (stroka2 * 2) - 1
                                        
                schetchik2 = dop + str2

                for i in range(schetchik2):
                    if i == schetchik2 - 1:
                        typebtn = driver.find_elements_by_class_name('_type_btn')[i].click()
                        time.sleep(1)
                        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/aside/div/div[2]/div[2]/div[1]/div/div[7]/div[1]').click()
                time.sleep(5)

        else:
            score = driver.find_element_by_class_name('ev-scoreboard__comment--3u2eF').text
            line = len(score)
            line -= 1
            a4 = line
            line -= 1
            a3 = line
            line -= 1
            a2 = line
            line -= 1
            a1 = line

            scores = 14
            s1 = score[a1:a2]
            s2 = score[a3:a4]
            s1 = int(s1)
            s2 = int(s2)
            scores = scores - (s1 + s2)

            kchet1 = 0
            kchet2 = 0

            for i in range(0, 15):
                checklist = driver.find_elements_by_class_name('_type_text')[i].text
                list_2 = checklist[0:17]
                if list_2 == 'Кто выиграет гейм':
                    kchet1 += 1
                else:
                    list_2 = checklist[0:4]
                    if list_2 == 'Гейм':
                        kchet2 += 1
                    else:
                        break
                    stavka = checklist[0:24]
                    stavka = stavka + sbros
                    f = open('bets.txt', 'a')
                    f.write(stavka)
                    f.close()

            dop = kchet1 * 2

            f = open('bets.txt', 'r')
            stavki = f.read()
            f.close()


            stroka1 = 0
            a1 = 0
            a2 = 24
            s = 1
            for i in range (kchet2):
                if stavki[a1:a2] == stavka1:
                    stroka1 = s
                s += 1
                a1 += 25
                a2 += 25

            if stroka1 == 0:
                pass
            else:
                if yorn1 == 'нет':
                    str1 = (stroka1 * 2)
                else:
                    str1 = (stroka1 * 2) - 1
                    schetchik1 = scores + dop + str1
                            
                    for i in range(schetchik1):
                        if i == schetchik1 - 1:
                            typebtn = driver.find_elements_by_class_name('_type_btn')[i].click()
                            time.sleep(3)
                            driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/aside/div/div[2]/div[2]/div[1]/div/div[7]/div[1]').click()
                    time.sleep(5)

            score = driver.find_element_by_class_name('ev-scoreboard__comment--3u2eF').text
            line = len(score)
            line -= 1
            a4 = line
            line -= 1
            a3 = line
            line -= 1
            a2 = line
            line -= 1
            a1 = line

            scores = 14
            s1 = score[a1:a2]
            s2 = score[a3:a4]
            s1 = int(s1)
            s2 = int(s2)
            scores = scores - (s1 + s2)

            kchet1 = 0
            kchet2 = 0

            for i in range(0, 15):
                checklist = driver.find_elements_by_class_name('_type_text')[i].text
                list_2 = checklist[0:17]
                if list_2 == 'Кто выиграет гейм':
                    kchet1 += 1
                else:
                    list_2 = checklist[0:4]
                    if list_2 == 'Гейм':
                        kchet2 += 1
                    else:
                        break
                    stavka = checklist[0:24]
                    stavka = stavka + sbros
                    f = open('bets.txt', 'a')
                    f.write(stavka)
                    f.close()

            dop = kchet1 * 2

            f = open('bets.txt', 'r')
            stavki = f.read()
            f.close()

            stroka2 = 0
            a1 = 0
            a2 = 24
            s = 1
            for i in range (kchet2):
                if stavki[a1:a2] == stavka2:
                    stroka2 = s
                s += 1
                a1 += 25
                a2 += 25

            if stroka2 == 0:
                pass
            else:
                if yorn2 == 'нет':
                    str2 = (stroka2 * 2)
                else:
                    str2 = (stroka2 * 2) - 1
                                
                schetchik2 = scores + dop + str2

                for i in range(schetchik2):
                    if i == schetchik2 - 1:
                        typebtn = driver.find_elements_by_class_name('_type_btn')[i].click()
                        time.sleep(3)
                        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/aside/div/div[2]/div[2]/div[1]/div/div[7]/div[1]').click()
                time.sleep(5)
                           
            time.sleep(1)
    else:
        flag = False

driver.close()
