'''
Strings
-------
Operations
----------
1.Indexing
----------
-->Indexing is used to get char that you looking access
Types
1.Positive Indexing
positive Indexing starts from 0 to index
syntax --> print(variable_name[index_position])
2.Negative Indexing
-----------
Negative Indexing starts from -1 index
Syntax --> print(variable_name[Negative index_position])
'''
#Positive Indexing
text = 'python'
print(text[3])

#Negative Indexing
text = 'python'
print(text[-1])

#len()
'''
-----
-->len() is built-in function that is used get number of char present in the string
syntax -->
'''
txt = 'Python is a programming language'
print(txt[12:23])
print(txt[0:5])


#slicing
'''--------
--> This is used to access the particular part from the string
syntax --> variable_name[star:end]
eg
'''
'''
txt = 'Python is a programming language'
print(txt[12:1])
rev = txt[::-1]
'''
'''
upper()
-------
-->Used to convert all small char into cap
'''
txt = 'Python is programming language'
print(txt.upper())
'''
#lower()
--------
-->Used to convert all cap into small
'''
'''
txt = 'PYTHON'
print(text.lower())

index()
------
-->Used to know the index position of an char
syntax --> variable_name.index('substring')

'''
'''
txt = 'Python is programming language'
print(txt.index('i'))
print(txt[7])
#replace()
---------
-->used to replace old substring with new substring
syntax
'''

txt = 'Python is programming language'
print(txt.replace('Python','Java'))
'''
#split()
-------
-->this method is used to separate the string based on the given substring
syntax --> variable_name.split(substring
'''
txt = 'Python is a programming language'
print(txt.split(' '))
'''
count()
------
-->used to count number of occurences of an substring
syntax --> variable_name.count('substring')
eg
--
'''
txt = 'Python is a programming language'
print(txt.count('a',1,32))

'''
day 7
Indexing
--------
Positive --> 0
Negative --> -1
'''
'''
so = [1,2,3,4,'Python']
print(so[-1][-3])
all_ = [12,[1,'python',[1,4],(78,[6,7]),['java',78]]]
print(all_[1][3][1])
'''
'''
data_ = ['Python',[1,2,(90,'Details',[67,0]),(78,'Student')]]
print(data_)
print(data_[1][2][1][2])

len()
-----
--> The function is used to find the number of items present inside list
inside list
syntax--> len(variable_name)
eg
--

'''
'''
data_ = ['Python',[1,2,(90,'Details',[67,0]),(78,'Student')]]
print(len(data_))

Slicing
-------
-->
'''
'''
data_ = [1,2,3,4,5,6,7]
print(data_[2:6])

eg
--
a = [1,2]
b = [3,4]
print(a+b)


Methods
-------
append()
-------
-->append method will and new items into list at last index position
syntax -->variable_name.append(item)
'''
'''
went = [1,2]
print(went)
went.append(3)
print(went)
went.append(4)
print(went)
'''
'''
extend()
-------
--> extend() will add the items into a list at last index position, but it will give each value as one index inside list
syntax --> variable_name.extend(items)
'''
'''
go = [1,2]
print(go)
go.append(3)
print(go)
go.extend('python')
print(go)

pop()
----
--> pop() is used to remove items from the list and it will delete based on the index position

syntax --> variable_name.pop(index_position)
eg
--
'''
'''
m = [5,1,2,3,4,'python']
m.pop(5)
print(m)
remove()
-------
-->
'''
'''
m = [5,4,3,2,1,'python']
m.remove(5)
print(m)
'''
'''
prices = list(map(int, input().split()))
new_price = int(input())

prices.append(new_price)
prices.sort()

print(prices)
print(len(prices))
'''

'''
name , age = ('Teja',34)
print(name)
print(age)

Tuple
-----
--> Tuple is collection of different datatypes that separated by , and represented by ()
-->it is immutable
-->we can pass a tuple values and that can be assign to the variables, but should match same number variables and values inside the tuple


eg
--
t = (1,'Python',[3,4],[4,5])

max()
-----
--> used to find out the max value from the tuple
eg
--
'''
'''
so = (67,5,89,45)
print(max(so))
'''
'''
min()
----
--> used to find out the least value from the tuple
eg
--
so = (67,5,89,45)
print(min(so))
'''
'''
count()
------
--> used to count an item present in the tuple
eg
--
'''
'''
so = (67,5,89,45,5)
print(so.count(5))
'''

so = (67,5,89,45)
do = (45,89)
print(so + do)

'''
m = [5,1,2,3,4,'python']
m.pop(3)
print(m)
'''
    
so = (67,5,89,45)

print(min(so))

'''
difference()
------------
--->it will display the different elements from set_1, but not the set_2 elements
syntax --> set_1.difference(set_2) or set_1 -set_2
eg
--

data_ = {1,2,3,4}
nums = {4,5,6}
print(nums - data_)
print(nums.difference(data_))
'''

data_ = {1,2,3,4}
nums = {4,5,6}
print(nums ^ data_)
print(data_.symmetric_difference(nums))
'''
add() method will add only one element at a time
syntax --> set.add(element)
eg
--




'''
data_ = {1,2,3,4}
print(data_)
data_.add(7)
print(data_)
'''

update()
--------
--> we can add more one elements by using update method
syntax --> set.update([elements]) or set_1.update(set_2)
eg
---
'''
data_ = {1,2,3,4}
nums = {4,5,6}
print(data_)
data_.update([8,9])
print(data_)
data_.update(nums)
print(data_)

'''
remove() method will del the given element from 
data_ = {1,2,3,4}
data_.remove(3)
print(data_)
'''
'''
discard()
---------
The method is used to del the elements from the set,but never raise any error even the element not insidw set
syntax --> set.discard(element)
eg
--
'''

data_ = {1,2,3,4}
data_.discard(7)
print(data_)
data_.discard(1)
print(data_)
'''
'''
data_ = {1,2,3,4}
print(data_)
data_.clear()
print(data_)

'''
set_A = {9,3,8,4,7,2,6}
set_B = {1,3,5,7,9,4,2}
print(set_A & set_B)
print("union",set_A | set_B)
print("summetry",set_A ^ set_B)
'''
'''
set_A = {'S','A','G','A','R','I','E'}
set_B = {'N','A','V','E','E','N','N','K','U','M','A','R'}
print("Intersection",set_A & set_B)
print("union",set_A | set_B)
print("summetry",set_A ^ set_B)
set_A.remove('A')
print(set_A)
set_B.remove('E')
print(set_B)
'''
set_A = {'S','A','G','A','R','I','E'}
set_B = {'N','A','V','E','E','N','N','K','U','M','A','R'}

print(set_A - set_B)












