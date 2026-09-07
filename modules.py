'''
modules
-------
-->A module is a python file (.py) that written using function,variables,operators, etc.
1.built in modules
------------------
--> The modules are developed by the programmer and those comes with installation
eg
--
1.math
------

2.os
3.sys
4.random
2.user-defined modules

'''
'''
import math
print(math.pow(2,3))

import os
print(os.getcwd())


import sys
print(sys.path)
print(sys.version)


import random
print(random.randint(1000,9999))
'''
'''
2.User-defined modules
----------------------
-->
importing
'''
'''
import lokesh
print(lokesh.mul(3,7))

math
-----

import math
print(math.pi)
print(math.ceil(4.3))
print(math.floor(5.6))
print(math.sqrt(25))
print(math.sin(2))
print(math.pow(2,3))
print(math.cos(5)
'''
'''
import random
print(random.randint(1,100))
print(random.randrange(1,100))
color = ['red','blue','green','yellow','orange']
print(random.choice(color))
random.shuffle(color)
print(color)

import platform
print(platform.python_version())
print(platform.system())
print(platform.platform())
print(platform.processor()

import collections
data_ = ['banana','apple','banana','orange','orange']
print(collections.Counter(data_))
all_ = collections.Counter(data_)
print(all_.most_common())
'''
'''
from collections import defaultdict
data_ = defaultdict(list)
data_['Python'].append('Surya')
data_['Python'].append('lokesh')
data_['Java'].append('sony')
print(data_)

from datetime import datetime
today = datetime.today()
now = datetime.now()
print(today.month)
print(today.year)
print(today.hour)
print(today.day)
print(today.minute)
'''
'''
from datetime import datetime
now = datetime.now()
print(now.strftime('%d-%m-%y'))
print(now.strftime('%H:%M:%S'))
print(now.strftime('%M'))

import random
attemp_ = 1
num = random.randrange(1,100)
print(num)
while attemp_ > 0:
    game_ = int(input('Enter a number between 1 and 100: '))
    if game_ == num:
        print("Your guess is correct")
        break
    else:
        attemp_ -= 1
if attemp_ == 3:
    print('Print money is 500')
elif attemp_ == 2:
    print('Print money is 200')
elif attemp_ == 1:
     print('Print money is 100')
else:
     print('Better luck next time')
'''
'''
import itertools
a = itertools.count(45)
print(next(a))
print(next(a))
b = itertools.repeat('python',6)
for j in b:
      print(j)

c = itertools.cycle(['Python','java','C'])
print(next(c))
'''
import itertools

n = itertools.chain([1,2,3],[4,5,6])
print(list(n))



      


