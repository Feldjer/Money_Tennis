gamet = 'Гейм '
chet = ' будет счет '
dvoetochie = ':'
stavkaprint1 = ''
stavkaprint2 = ''

f = open('bet.txt', 'r', encoding='utf8')
stavka = f.read()
f.close()

stavka1 = stavka[0:67]
stavka2 = stavka[68:135]

game1 = stavka1[21:23]
game1 = int(game1)
game1 = str(game1)
chett1 = (stavka1[34:40])
yorn1 = (stavka1[42:45])

game2 = stavka2[21:23]
game2 = int(game2)
game2 = str(game2)
chett2 = (stavka2[34:39])
yorn2 = (stavka2[42:45])

stavkaprint1 = gamet + game1 + dvoetochie + chet + chett1
f = open('bet1.txt', 'w')
f.write(stavkaprint1)
f.close()

f = open('bet1yorn.txt', 'w')
f.write(yorn1)
f.close()

stavkaprint2 = gamet + game2 + dvoetochie + chet + chett2
f = open('bet2.txt', 'w')
f.write(stavkaprint2)
f.close()

f = open('bet2yorn.txt', 'w')
f.write(yorn2)
f.close()
