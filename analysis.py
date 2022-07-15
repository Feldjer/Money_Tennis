zero = '0'
game = podacha = 0
tgame = ''
tcht15 = '\n15:15\0'
tcht30 = '\n30:30\0'
tcht40 = '\n40:40\0'
chch15 = chch30 = chch40 = 0
zero = '0'
ls = '('
rs = ')'
t1 = 'Game'
t2 = 0
t3 = '.txt'
b = '''00
15:15 (00)
30:30 (00)
40:40 (00)
'''
f = open('analysis.txt', 'wt')
for index in b:
    f.write(index)
f.close()

f = open('game_score.txt', 'r')
scorett = f.read()
scorett = int(scorett)
f.close()

for i in range(0, scorett):

    fach = open('analysis.txt', 'rt')
    q = fach.read()
    chch15 = q[10:12]
    chch15 = int(chch15)
    chch30 = q[21:23]
    chch30 = int(chch30)
    chch40 = q[32:34]
    chch40 = int(chch40)
    fach.close()

    # This code is hidden for privacy and copyright reasons

