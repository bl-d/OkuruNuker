import os
import random

from threading import Thread

## Number of days you want to make commits
for i in range(150):
    for i in range(1,365*2 + 1):
        for x in range(random.choice([1,2,3,4,5,6,7,8,9,10])):
            d = '{} day ago'.format(i)
            print(d)
            a = os.system('git commit --allow-empty --date="{}" -m "Bug Fixes"'.format(d))


os.system('git push')