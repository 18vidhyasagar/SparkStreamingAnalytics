#! /usr/bin/python
  
print("Execution starting")

import random
import time
lst1 = ['device1','device2']
lst2 = ['error', 'ok']
with open('readings', 'w') as file:
    for num in range(10):
        i = random.randint(0,1)
        j = random.randint(0,1)
        time.sleep(1)
        file.write('\n{"device":'+'"'+lst1[i]+'"'+', "status":'+'"'+lst2[j]+'"}')
        
print("Execution ends")