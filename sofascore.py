from selenium import webdriver
from bs4 import BeautifulSoup
import threading
import requests
import psutil
import time

f = open('surname.txt', 'r')
surname_file = f.read()
if 'п»ї' in surname == True: # Возможная ошибка кодирования
    surname = surname[3:]
f.close()

def timer_1():
    page_source_set = driver.page_source
    flag = True
    
    while flag == True:
        f = open('global_prog.txt', 'r')
        flag_txt = f.read()
        f.close()
        if flag_txt == 'True':
            time.sleep(5)
            f = open('html_code_set.txt', mode='w', encoding='utf8')
            f.write(page_source_set)
            f.close()
            os.system(r'parser_set.py')
        else:
            flag = False

def timer_2():
    driver.find_element_by_xpath('//*[@id="pjax-container-main"]/div/div[2]/div/div[3]/div/div/div[1]/div[1]/a').click()
    time.sleep(3)
    
    pars_score = ''
    flag = True

    while flag == True:
        f = open('global_prog.txt', 'r')
        flag_txt = f.read()
        f.close()
        if flag_txt == 'True':

            time.sleep(8)
            print('Загружаю новую информацию!')
            page_source = driver.page_source

            f = open('html_code_score.txt', mode='w', encoding='utf8')
            f.write(page_source)
            f.close()
            
            os.system (r'parser_score.py')

            f = open('all_score.txt','r')
            new_pars_score = f.read()
            f.close()

            if pars_score == new_pars_score:
                print('Новой информации нет!')
            else:
                pars_score = new_pars_score
                f = open('flag_sofascore.txt', 'w')
                f.write('True')
                f.close()
                print('Новая информация сохранена!')
            
            time.sleep(8)
            
        else:
            flag = False

    for proc in psutil.process_iter(): 
        if proc.name() == 'firefox.exe': 
            proc.kill()

tim1 = threading.Timer(0.0, timer_1)
tim2 = threading.Timer(0.0, timer_2)
            
driver = webdriver.Firefox()
driver.get('https://www.sofascore.com/ru/tennis/livescore')
time.sleep(4)
driver.find_element_by_partial_link_text(surname).click()
time.sleep(2)
tim1.start()
time.sleep(1)
tim2.start()
