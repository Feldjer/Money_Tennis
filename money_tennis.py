import os
import time
import progressbar

print('\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\00\0\0\0\0\0\0\0\0\0\0\0Money Tennis (ver 0.0.9)')
print('\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\00\0\0\0\0\0\0\0\0\0\0\0Alpha Test')

bar = progressbar.ProgressBar(maxval=100, widgets=[
    'Loading: ',
    progressbar.Bar(left='[', marker='|', right=']'),
]).start()

t = 0
while t != 101:
    bar.update(t)
    time.sleep(0.04)
    t += 1

os.system(r'launch_clear.py')
os.system(r'launch_tennis.py')
