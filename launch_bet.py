import os
import time

print('Module: Bet ......................................... Launch')

time.sleep(5)

flag = True
old_stavka = ''

while flag == True:

    flag_threatment = 'False'
    f1 = open('global_prog.txt', 'r')
    flag_txt = f1.read()
    f1.close()
    if flag_txt == 'True':
        
        while flag_threatment == 'False':
            f = open('flag_threatment.txt', 'r')
            flag_threatment = f.read()
            f.close()

        f = open('flag_threatment.txt', 'w')
        f.write('False')
        f.close()
        
        os.system (r'game_score.py')
        os.system (r'analysis.py')
        os.system (r'bet.py')

        f = open('bet.txt', 'r')
        new_stavka = f.read()
        f.close()

        if old_stavka == new_stavka:
            pass
        else:
            old_stavka = new_stavka
            os.system (r'threatment_bet.py')
            f = open('flag_bet.txt', 'w')
            f.write('True')
            f.close()

            print('Ставка готова для выгрузки на FonBet!')

    else:
        flag = False
