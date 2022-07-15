pusto = ''
FlagTB = True
TieBreik = '2222'
score_game = ''
score_game_new = ''
score_game_new_new = ''

f = open('all_score.txt', 'r')
score = f.read()
f.close()
score = score.replace(' ', '')
score = score.replace('\n', '')
score = score.replace('A', '41')

b = len(score)
a1 = 0
a2 = 3

while b > 0:
    z = score[a1:a2]
    if z == '0':
        x = score[a1-1:a2]
        if (x == '30') or (x == '40') or  (x == '50'):
            pass
        elif x == '00':
            x = score[a1-2:a2]
            if (x == '300') or (x == '400'):
                z = z.replace('0', '00')
            else:
                pass
    z = z.replace('000', '00000')
    if z == '101':
        x = score[a1:a2+2]
        if (x == '10111') or (x == '10102'):
            pass
        else:
            x = score[a1-1:a2+1]
            if x == '41015':
                z = z.replace('101','1001')
            else:
                pass
    if z == '001':
        x = score[a1-1:a2]
        if x == '0001':
            z = z.replace('001', '00001')
        else:
            x = score[a1:a2+2]
            if (x == '00111') or (x == '00102'):
                pass
            else:
                z = z.replace('001', '0001')    
    z = z.replace('003', '0003')
    z = z.replace('004', '0004')
    if z == '150':
        x = score[a1-1:a2]
        if x == '0150':
            x = score[a1-2:a2]
            if (x == '40150') or (x == '30150'):
                z = z.replace('150', '1500')
            elif x == '50150':
                z = z.replace('150','1500')
            elif x == '00150':
                z = z.replace('150', '1500')
            elif x == '10150':
                z = z.replace('150', '1500')
            else:
                z = z.replace('150', '01500')
        else:
            x = score[a1-2:a2]
            if x == '00150':
                z = z.replace('150', '0150')
            else:
                z = z.replace('150', '1500')
    if z == '015':
        x = score[a1-1:a2]
        if (x == '3015') or (x == '4015'):
            x = score[a1-2:a2]
            if (x == '13015') or (x == '14015'):
                x = score[a1-3:a2]
                if (x == '413015') or (x == '414015'):
                    pass
                else:
                    z = z.replace('015','0015')
        elif (x == '9015') or (x == '7015') or (x == '8015'):
            z = z.replace('015', '0015')
        elif (x == '0015') or (x == '1015'):
            x = score[a1-2:a2]
            if (x == '41015') or (x == '30015') or (x == '40015') or (x == '50015'):
                z = z.replace('015','0015')
            elif x == '00015':
                x = score[a1-3:a2]
                if x == '400015':
                    z = z.replace('015','0015')
        elif (x == '5015') or (x == ''):
            z = z.replace('015', '0015')
        else:
            z = z.replace('015', '(015)?')
    if z == '300':
        x = score[a1:a2+2]
        if (x == '30011') or (x == '30010'):
            pass
        else:
            z = z.replace('300', '3000')
    if z == '030':
        x = score[a1-1:a2]
        if (x == '3030') or (x == '4030'):
            pass
        elif x == '2030':
            pass
        else:
            z = z.replace('030', '0030')
    if z == '400':
        x = score[a1:a2+2]
        if x == '40010' or x == '40011':
            pass
        else:
            z = z.replace('400','4000')
    if z == '410':
        x = score[a1:a2+2]
        if x == '41010' or x == '41011':
            pass
        else:
            z = z.replace('410','4100')
    if z == '040':
        x = score[a1-1:a2]
        if (x == '4040') or (x == '3040'):
            pass
        else:
            z = z.replace('040', '0040')
    if (z == '701') or (z == '801') or (z == '901'):
        x = score[a1:a2+1]
        if (x == '7015') or (x == '8015') or (x == '9015'):
            z = z.replace('701', '7001')
            z = z.replace('801', '8001')
            z = z.replace('901', '9001')
    z = z.replace('501', '5001')
    z = z.replace('503', '5003')
    score_game += z
    a1 += 3
    a2 += 3
    b -= 3
print(score_game)

b = len(score_game)
a1 = 0
a2 = 2

while b > 0:
    z = score_game[a1:a2]
    if (z == '10') or (z == '01'):
        print('TieBreik')
        score_game_new += TieBreik
        scores1 = 0
        scores2 = 0
        s1 = 0
        s2 = 0
        TieBreikF = True
        smeshenieF = True
        while TieBreikF == True:
            if (scores1 - 10 >= 0) and (scores2 - 10 >= 0):
                if smeshenieF == True:
                    a1 += 2
                    a2 += 4
                    smeshenieF = False
                    TB = score_game[a1:a2]
                    s1 = int(TB[0:2])
                    s2 = int(TB[2:4])
                    if (s1 - scores1 == 1) or (s2 - scores2 == 1):
                        scores1 = s1
                        scores2 = s2
                    elif ((s1 == 15) and (s2 == 0)) or ((s1 == 0) and (s2 == 15)):
                        TieBreikF = False
                        s1 = str(s1)
                        s2 = str(s2)
                        score_game_new += s1 + s2
                        s1 = int(s1)
                        s2 = int(s2)
                    elif ((s1 == 41) and (s2 == 40)) or ((s1 == 40) and (s2 == 41)) or ((s1 == 40) and (s2 == 30)) or ((s1 == 30) and (s2 == 40)):
                        TieBreikF = False
                        s1 = str(s1)
                        s2 = str(s2)
                        score_game_new += s1 + s2
                        s1 = int(s1)
                        s2 = int(s2)
                    elif ((s1 == 40) and (s2 == 15)) or ((s1 == 15) and (s2 == 40)) or ((s1 == 40) and (s2 == 0)) or ((s1 == 0) and (s2 == 40)):
                        TieBreikF = False
                        s1 = str(s1)
                        s2 = str(s2)
                        score_game_new += s1 + s2
                        s1 = int(s1)
                        s2 = int(s2)
                    else:
                        print('error!')
                else:
                    a1 += 4
                    a2 += 4
                    TB = score_game[a1:a2]
                    s1 = int(TB[0:2])
                    s2 = int(TB[2:4])
                    if (s1 - scores1 == 1) or (s2 - scores2 == 1):
                        scores1 = s1
                        scores2 = s2
                    elif ((s1 == 15) and (s2 == 0)) or ((s1 == 0) and (s2 == 15)):
                        TieBreikF = False
                    else:
                        print('!error!')
            else:
                a1 += 2
                a2 += 2
                TB = score_game[a1:a2]
                s1 = int(TB[0:1])
                s2 = int(TB[1:2])
                if (s1 == 1) and (s2 == 0):
                    x = score_game[a1:a2+1]
                    if (x == '109') or (x == '108'):
                        scores1 = int(x[0:2])
                        scores2 = int(x[2:3])
                        a1 += 1
                        a2 += 1
                    elif x == '101':
                        x = score_game[a1:a2+2]
                        if x == '1010':
                            scores1 = int(x[0:2])
                            scores2 = int(x[2:4])
                            a1 += 2
                            a2 += 2
                        else:
                            x = score_game[a1:a2+4]
                            if (x == '101111') or (x == '101110'):
                                scores1 = int(x[0:2])
                                scores2 = int(x[2:4])
                                a1 += 2
                                a2 += 2
                            else:
                                scores1 = s1
                                scores2 = s2
                    else:
                        scores1 = s1
                        scores2 = s2
                elif (s1 == 1) and (s2 == 1):
                    x = score_game[a1:a2+1]
                    if x == '119':
                        scores1 = int(x[0:2])
                        scores2 = int(x[2:3])
                        a1 += 1
                        a2 += 1
                    elif x == '111':
                        x = score_game[a1:a2+2]
                        if x == '1110':
                            scores1 = int(x[0:2])
                            scores2 = int(x[2:4])
                            a1 += 2
                            a2 += 2
                        elif x == '1112':
                            x = score_game [a1:a2+4]
                            if (x == '111212') or (x == '111211'):
                                scores1 = s1
                                scores2 = s2
                            else:
                                scores1 = s1
                                scores2 = s2
                        else:
                            scores1 = s1
                            scores2 = s2
                    else:
                        scores1 = s1
                        scores2 = s2
                elif (s1 == 0) and (s2 == 0):
                    TieBreikF = False
                    s1 = str(s1)
                    s2 = str(s2)
                    score_game_new += s1 + s2
                    s1 = int(s1)
                    s2 = int(s2)
                elif (s1 == 1) and (s2 == 5):
                    x = score_game[a1:a2+2]
                    if x == '1540' or x == '1500':
                        TieBreikF = False
                        s1 = str(s1)
                        s2 = str(s2)
                        score_game_new += s1 + s2
                        s1 = int(s1)
                        s2 = int(s2)
                    else:
                        scores1 = s1
                        scores2 = s2
                elif (s1 == 4) and (s2 == 0):
                    x = score_game[a1:a2+2]
                    if (x == '4040') or (x == '4030') or (x == '4015') or (x == '4000'):
                        TieBreikF = False
                        s1 = str(s1)
                        s2 = str(s2)
                        score_game_new += s1 + s2
                        s1 = int(s1)
                        s2 = int(s2)
                    elif x == '4041':
                        x = score_game[a1:a2+4]
                        if (x == '404142') or (x == '404151'):
                            scores1 = s1
                            scores2 = s2
                        else:
                            TieBreikF = False
                            s1 = str(s1)
                            s2 = str(s2)
                            score_game_new += s1 + s2
                            s1 = int(s1)
                            s2 = int(s2)
                    else:
                        scores1 = s1
                        scores2 = s2
                elif ((s1 == 1) and (s2 >= 6)) or ((s1 >= 6) and (s2 == 1)):
                    x = score_game[a1:a2+1]
                    x1 = x[0:2]
                    x2 = x[1:3]
                    if (x1 == '10') or (x2 == '10'):
                        x1 = int(x1)
                        x2 = int(x2)
                        if x1 - scores1 == 1:
                            scores1 = x1
                            a1 += 1
                            a2 += 1
                        elif x2 - scores2 == 1:
                            scores2 = x2
                            a1 += 1
                            a2 += 1
                        else:
                            scores1 = s1
                            scores2 = s2
                    elif (x1 == '11') or (x2 == '11'):
                        x1 = int(x1)
                        x2 = int(x2)
                        if x1 - scores1 == 1:
                            scores1 = x1
                            a1 += 1
                            a2 += 1
                        elif x2 - scores2 == 1:
                            scores2 = x2
                            a1 += 1
                            a2 += 1
                        else:
                            scores1 = s1
                            scores2 = s2
                    else:
                        scores1 = s1
                        scores2 = s2
                elif (s1 == 3) and (s2 == 0):
                    x = score_game[a1:a2+3]
                    if (x == '30403') or (x == '30401'):
                        TieBreikF = False
                        s1 = str(s1)
                        s2 = str(s2)
                        score_game_new += s1 + s2
                        s1 = int(s1)
                        s2 = int(s2)
                        #print('ok')
                    else:
                        scores1 = s1
                        scores2 = s2
                elif (s1 == 4) and (s2 == 1):
                    x = score_game[a1:a2+2]
                    if x == '4140':
                        TieBreikF = False
                        s1 = str(s1)
                        s2 = str(s2)
                        score_game_new += s1 + s2
                        s1 = int(s1)
                        s2 = int(s2)
                    else:
                        scores1 = s1
                        scores2 = s2
                elif (s1 == 0) and (s2 == 0):
                    TieBreikF = False
                    s1 = str(s1)
                    s2 = str(s2)
                    score_game_new += s1 + s2
                    s1 = int(s1)
                    s2 = int(s2)
                else:
                    if ((s1 == 1) and (s2 == 0)) or ((s1 == 0) and (s2 == 1)):
                        scores1 = s1
                        scores2 = s2
                    else:
                        if (s1 - scores1 == 1) or (s2 - scores2 == 1):
                            scores1 = s1
                            scores2 = s2
                        else:
                            print('!!error!!')
            print('scores', scores1, ':', scores2)
    else:
        score_game_new += z
        
    b -=2
    a1 += 2
    a2 += 2
    
print(score_game_new)

b = len(score_game_new)
a1 = 0
a2 = 2

while b > 0:
    z = score_game_new[a1:a2]
    score_game_new_new = z + score_game_new_new
    a1 += 2
    a2 += 2
    b -= 2

print(score_game_new_new)

f = open('score.txt', 'w')
f.write(score_game_new_new)
f.close()
