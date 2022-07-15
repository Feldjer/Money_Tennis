vhod = True
flag = True
taibreik = ''
s = 1
all_score = ''
txt = '.txt'
scoret = 'Score'
sbros = '\n'
gamet = 'Game'
j = 0
chet = 0

f = open('score.txt', 'r')
score = f.read()
print('Счет:', score)
f.close()
b = len(score)

s = 0
a1 = 0
a2 = 2
a3 = 4
a4 = 6
a5 = 8

def sbor(s1, s2, s3, s4):
    if ((s1 == 0) or (s1 == 15) or (s1 == 30) or (s1 == 40) or (s1 == 41)) and ((s2 == 0) or (s2 == 15) or (s2 == 30) or (s2 == 40) or (s2 == 41)) and ((s3 == 0) or (s3 == 15) or (s3 == 30) or (s3 == 40) or (s3 == 41)) and ((s4 == 0) or (s4 == 15) or (s4 == 30) or (s4 == 40) or (s4 == 41)):
        if s1 + s2 < s3 + s4:
            if (s1 + s2 == 80) and (s3 + s4 == 81):
                return None
            else:
                return True
        elif (s1 + s2 == 15) and (s3 + s4 == 15):
            return None
        else:
            return False
    else:
        return '13'
 
while b > 0:
    if vhod == True:
        b -= 4
        vhod = False
    s1 = score[a1:a2]
    print('s1', s1)
    s1 = int(s1)
    s2 = score[a2:a3]
    s2 = int(s2)
    print('s2', s2)
    s3 = score[a3:a4]
    s3 = int(s3)
    print('s3', s3)
    s4 = score[a4:a5]
    s4 = int(s4)
    print('s4', s4)
    a1 += 4
    a2 += 4
    a3 += 4
    a4 += 4
    a5 += 4
    h = sbor(s1, s2, s3, s4)
    if h == True:
        s = int(s)
        s += 1
        s = str(s)
        href = scoret + s + txt
        f1 = open(href,'w')
        if s1 == 0:
            s1 = '00'
        if s2 == 0:
            s2 = '00'
        s1 = str(s1)
        s2 = str(s2)
        all_score = s2 + s1 + all_score
        print('Запись(True): ', all_score)
        f1.write(all_score)
        f1.close()
        all_score = ''
    elif h == False:
        if s1 == 0:
            s1 = '00'
        if s2 == 0:
            s2 = '00'
        s1 = str(s1)
        s2 = str(s2)
        all_score = s2 + s1 + all_score
        print('Сборка(False) :', all_score)
    elif h == None:
        if b == 4:
            if s1 == 0:
                s1 = '00'
            if s2 == 0:
                s2 = '00'
            s = str(s)
            s1 = str(s1)
            s2 = str(s2)
            href = scoret + s + txt
            f1 = open(href,'w')
            all_score = s2 + s1 + all_score
            f1.write(all_score)
            f1.close()
            s = int(s)
            s += 1
            s = str(s)
            if s3 == 0:
                s3 = '00'
            if s4 == 0:
                s4 = '00'
            s3 = str(s3)
            s4 = str(s4)
            href = scoret + s + txt
            f1 = open(href,'w')
            all_score = s4 + s3
            f1.write(all_score)
            f1.close()
            s = str(s)
        elif (s1 + s2 == 80) and (s3 + s4 == 81):
            if s1 == 0:
                s1 = '00'
            if s2 == 0:
                s2 = '00'
            s1 = str(s1)
            s2 = str(s2)
            all_score = s2 + s1 + all_score
        else:
            pass
    elif h == '13':
        if ((s1 == 0) and (s2 == 15)) or ((s1 == 15) and (s2 == 0)):
            if s1 == 0:
                s1 = '00'
            if s2 == 0:
                s2 = '00'
            s1 = str(s1)
            s2 = str(s2)
            all_score = s2 + s1 + all_score
            s = int(s)
            s += 1
            s = str(s)
            href = scoret + s + txt
            f1 = open(href,'w')
            f1.write(all_score)
            f1.close()
            all_score = ''
        if (s1 == 22) and (s2 == 22):
                s = int(s)
                s += 1
                s = str(s)
                href = scoret + s + txt
                all_score = 'TaiBreik'
                f1 = open(href,'w')
                f1.write(all_score)
                f1.close()
                all_score = ''
    b -= 4

s = int(s)
s += 1
s = str(s)
href = scoret + s + txt
f1 = open(href,'w')
f1.write(all_score)
f1.close()
all_score = ''
