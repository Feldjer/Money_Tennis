import os
import time

print('Module: Threatment .................................. Launch')

time.sleep(5)

flag = True
        
while flag == True:
    
    flag_sofascore = 'False'
    f = open('global_prog.txt', 'r')
    flag_txt = f.read()
    f.close()
    if flag_txt == 'True':

        while flag_sofascore == 'False':
            f = open('flag_sofascore.txt', 'r')
            flag_sofascore = f.read()
            f.close()

        print('Модуль 2 включился в работу!')
            
        f = open('flag_sofascore.txt', 'w')
        f.write('False')
        f.close()
            
        os.system (r'threatment_score.py')
        os.system (r'sample_score.py')
        os.system (r'tennis_score.py')

        f = open('flag_threatment.txt', 'w')
        f.write('True')
        f.close()

        print('Информация обработана!')
        
    else:
        flag = False
