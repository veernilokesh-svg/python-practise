'''
Dictionary()
-----------
--> Dict is a collection of key : value pair
--> Key must be unique and it should be immutable datatype
(int, str,tuple)
--> dict is represented in{}
details = {1 : 2,
           'name': 'Teja',
           (1,2) : [1,2]}
accesing
--------
--> dict can access by calling key, we will get value from that key
syntax --> dict['key']

--> get() method is also used to get thevalue from that key
syntax --> dict.get(key)
eg
---
update()
-------
--> Method is used update a key, incase if the key is not present inside dict then it add that key:value})
syntax --> dict.update({key:value})
There is another way to update a key
syntax -->
values()
--------
-->values() method is used get all the value

keys()
------
--> keys() method is used get all the key from the dict
syntax -->dict.keys()
items()
------
--> The method will grt the key key:value separate from the dict
syntax --> dict.items()
eg
--
clear()
-------
--> clear method is used to clear entire data from dict
syntax --> dict.clear()
eg
--
'''
'''
data_ = {'name' : 'Surya',
         'balance' : 7000,
         'Adr' : 1234567897654,
         'PANC' : 'GPXBP2890Y',
         2:[3,4]}
         
print(data_['Adr'])
print(data_.get(2))
'''
'''
data_ = {'name' : 'Surya',
         'balance' : 7000,
         'Adr' : 1234567897654,
         'PANC' : 'GPXBP2890Y',
         }
print(data_)
data_['AC'] = 12345676548
print(data_)
data_.update({'name' : 'sony'})
data_.update({'ATMPIN' :7899})
print(data_)
print(data_.values())
print(data_.keys())
print(data_.items())
data_.clear()
print(data_)
del data_['Adr']
print(data_)
'''
'''
data_ = {'name' : 'Surya',
         'balance' : 7000,
         'Adr' : 1234567897654,
         'PANC' : 'GPXBP2890Y',
         }
data_.clear()
print(data_)
del data_['Adr']
print(data_)

'''
'''
if statement
------------
--> if condition become true,then it will execute inside block of code
--> in case it becomes false, then it wil never entry inside block
'''

age = 16
if age >= 18:
    print('Eligible to vote')
else:
    print('Not eligible to vote')

'''
if else_
-------
--> else for if statement is a fall-back statement, incase if condition is false then else block will execute
'''
age = 15
if age >= 18:
    print(f'your {age}Eligible to vote')
else:
    print(f'your {age} you have to wait {18-age}')

a = 90
b = 780
if a > b:
    print(a)
else:
    print(b)
    

