f = open('global_prog.txt', 'r')
while_ = f.read()
f.close()
if while_ == 'True':
    print('Глобальный цикл находиться в работе!')
    exit()
elif while_ == 'False':
    print('Глобальный цикл отключен!')
    a = input('Включить глобальный цикл?')
    if a == 'да' or a == 'yes':
        f = open('global_prog.txt', 'w')
        f.write('True')
        f.close()
        print('Глобальный цикл запущен!')
    elif a == 'нет' or a == 'no':
        print('Глобальный цикл выключен => Программа не будет запущена!')
    else:
        pass
else:
    print('Не указан параметр! Программа отключена!')
