from bs4 import BeautifulSoup
import urllib.request

scoreitog = ''

soup = BeautifulSoup(open('html_code_score.txt', encoding='utf-8'), 'html.parser')
for i in soup.find_all('div', class_='pbp__game'):
    score = i.text
    score = str(score)
    scoreitog += score

f = open('all_score.txt', 'w')
f.write(scoreitog)
f.close()
