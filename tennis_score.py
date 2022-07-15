scoret = 'Score'
gamet = 'Game'
txt = '.txt'
gametp = 'Game: '

for i in range(0, 40):
    pob1 = ''
    pob2 = ''
    s15 = False
    s30 = False
    s40 = False
    TaiBreik = False
    i += 1
    i = str(i)
    href1 = scoret + i + txt
    f = open(href1, 'r')
    score = f.read()
    f.close()
    if '1515' in score:
        s15 = True
    if '3030' in score:
        s30 = True
    if '4040' in score:
        s40 = True
    if 'TaiBreik' in score:
        TaiBreik = True
    href2 = gamet + i + txt
    f = open(href2, 'w')
    if s15 == True:
        ravn15 = '\nThere is 15:15!'
    else:
        ravn15 = ''
    if s30 == True:
        ravn30 = '\nThere is 30:30!'
    else:
        ravn30 = ''
    if s40 == True:
        ravn40 = '\nThere is 40:40!'
    else:
        ravn40 = ''
    if TaiBreik == True:
        TaiBreikPR = '\nTaiBreik!'
    else:
        TaiBreikPR = ''
    line = len(score)
    if line >= 12:
        line_num = (line // 4) - 1
        mn = line_num * 4
        a1 = 0 + mn
        a2 = 2 + mn
        a3 = 4 + mn
        f1_score = score[a1:a2]
        f1_score = int(f1_score)
        f2_score = score[a2:a3]
        f2_score = int(f2_score)
        if f1_score > f2_score:
            f2_score = str(f2_score)
            pob1 = '\nVictory 1st by filing\0' + f2_score
        else:
            f1_score = str(f1_score)
            pob2 = '\nVictory 2nd by filing\0' + f1_score
    print_ = gametp + i + ravn15 + ravn30 + ravn40 + TaiBreikPR + pob1 + pob2
    f.write(print_)
    f.close()
