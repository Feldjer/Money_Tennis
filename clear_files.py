pusto = ''
flag = 'False'
gamet = 'Game'
scoret = 'Score'
set_ = 'Set'
txt = '.txt'

surname = ''
f = open('surname.txt', 'w')
f.write(surname)
f.close()

f0 = open('html_code_score.txt', 'w')
f0.write(pusto)
f0.close()

f1 = open('all_score.txt', 'w')
f1.write(pusto)
f1.close()

f2 = open('score.txt', 'w')
f2.write(pusto)
f2.close()

f3 = open('game_score.txt', 'w')
f3.write(pusto)
f3.close()

f4 = open('TFclear.txt', 'r')
flag_txt = f4.read()
f4.close()

for i in range(0,5):
    h = i
    h += 1
    h = str(h)
    href = set_ + h + txt
    f = open(href, 'w')
    f.write(pusto)
    f.close()
    
if flag_txt == 'True':
    f4 = open('flag_sofascore.txt', 'w')
    f4.write(flag)
    f4.close()
    f5 = open('flag_threatment.txt', 'w')
    f5.write(flag)
    f5.close()
    f6 = open('flag_bet.txt', 'w')
    f6.write(flag)
    f6.close()
    f7 = open('flag_fonbet.txt', 'w')
    f7.write(flag)
    f7.close()
    f8 = open('TFclear.txt', 'w')
    f8.write(flag)
    f8.close()

for i in range(0,40):
    h = i
    h += 1
    h = str(h)
    s = scoret + h + txt
    g = gamet + h + txt
    f = open(s, 'w')
    f.write(pusto)
    f.close()
    f = open(g, 'w')
    f.write(pusto)
    f.close()
