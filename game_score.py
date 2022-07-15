gamet = 'Game'
scoret = 'Score'
txt = '.txt'
chet = 0

for i in range (0, 40):
    h = i
    h += 1
    h = str(h)
    g = gamet + h + txt
    f = open (g, 'r')
    game = f.read()
    f.close()
    if 'Victory' in game:
        chet += 1
    else:
        break

chet += 1
chet = str(chet)

href = scoret + chet + txt
f = open(href, 'r')
text = f.read()
f.close()

if text == '':
    pass
else:
    chet = int(chet)
    chet += 1
    chet = str(chet)

f = open('game_score.txt', 'w')
f.write(chet)
f.close()
