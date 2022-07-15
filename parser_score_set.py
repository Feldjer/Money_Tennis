from bs4 import BeautifulSoup
import urllib.request

scoreitog_set = ''
scoreitog_set_new = ''

soup = BeautifulSoup(open('html_code_score.txt', encoding='utf-8'), 'html.parser'))

for i in soup.find_all('div', class_='pbp__setcell'):
    set_score = i.text
    set_score = str(set_score)
    scoreitog_set += set_score

scoreitog_set = scoreitog_set.replace('\n', '')
scoreitog_set = scoreitog_set.replace(' ', '')

len_set_1 = len(scoreitog_set)
len_set_2 = len_set_1
a1 = 0
a2 = 2

while len_set_1 > 0:
    scoreitog_set_new = scoreitog_set[a1:a2] + scoreitog_set_new
    a1 += 2
    a2 += 2
    len_set_1 -= 2

score_old = 0
schetchik = None
a1 = 0
a2 = 1

while len_set_2 > 0:
    score_1 = scoreitog_set_new[a1]
    score_2 = scoreitog_set_new[a2]
    if score_1 == '.':
        score_1 = 0
    if score_2 == '.':
        score_2 = 0
    score_1 = int(score_1) 
    score_2 = int(score_2)
    if (score_old + 1) == (score_1 + score_2):
        score_old = score_1 + score_2
    else:
        schetchik = score_old
    a1 += 2
    a2 += 2
    len_set_2 -= 2

f = open('subtractor.txt', 'w')
f.write(schetchik)
f.close()
