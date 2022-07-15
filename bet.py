proc = '%'
razdel = '\n'
golos01 = '1)'
golos02 = '2)'
golos03 = '3)'
golos1 = 'Предлагаю ставку в\0'
golos2 = '\0гейме\0'
golos3 = 'с вероятностью\0'
vstver15 = 'на (15:15 - даа)\0'
vstver30 = 'на (30:30 - даа)\0'
vstver40 = 'на (40:40 - даа)\0'
lstver15 = 'на (15:15 - нет)\0'
lstver30 = 'на (30:30 - нет)\0'
lstver40 = 'на (40:40 - нет)\0'
zero = '0'
scoret= 'Score'
txt = '.txt'
flag = False

f = open('analysis.txt', 'rt')
a = f.read()
i = 0

game = a[0:2]
game = int(game)

f23 = open('game_score.txt', 'rt')
b = f23.read()
b = int(b)
b += 1

while flag == False:
    i += 1
    i = str(i)
    href = scoret + i + txt
    f234 = open(href, 'r')
    i = int(i)
    victory = f234.read()
    f234.close()
    a1 = '0015' in victory
    a2 = '1500' in victory
    if (a1 == True) or (a2 == True):
        pass
    else:
        flag = True
        
    # This code is hidden for privacy and copyright reasons
    
    print(golosos + golos1 + golgame + golos2 + ver1istavka + golos3 + ver1stavka + proc)
    print(golos02 + golos1 + golgame + golos2 + ver2istavka + golos3 + ver2stavka + proc)


    b1 = golos01 + golos1 + golosgame + golos2 + ver1istavka + golos3 + ver1stavka + proc
    b2 = razdel + golos02 + golos1 + golosgame + golos2 + ver2istavka + golos3 + ver2stavka + proc

    stavka = b1 + b2
    
    fs = open('bet.txt', mode='w', encoding='utf8')
    for index in stavka:
        fs.write(index)
    fs.close()
    
f.close()
f23.close()
