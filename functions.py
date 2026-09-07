'''
functions:
---------
-->A function is a block of code that can be executed when is called
--> A function start with def keyword and the line called as definition line,where we can define a function name
-->And if we want to execute the program in the fuction,need to call with the function name define at def line
syntax
--------
def fun_name(parameters):
    pass
fun_name(arguments)
'''
def add_(a,b):
    print(a+b)
add_(5,6)
'''
arguments
---------
-->The arguments should be same at def line and calling,incatination,if they are not same number will raise an error

def add_(a,b):
     print(a+b)
add_(5,7)

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
'''
'''
num = 0
num_2 = 1
def feb_(num,num_2): 
    print(num,num_2,end=' ')
    for i in range(1,10):
        num_3 = num + num_2
        num = num_2
        num_2 = num_3
        print(num_3,end=' ')
feb_(num,num_2)
'''
'''
default arguments
-----------------
--> The default arguments where the function will only consider the data at calling function even though data present in the def line.
'''
'''
def feb_(num,num_2):
    print(num + num_2)
feb_([1,3],[5,6])
'''
'''
def data_(a=8,b=9):
    print(a+b)
data_(1,)
data_(67,)
'''
'''
def prime(num=10,count = 1):
    for j in range(1,num+1):
        if num % j == 0:
            count += 1
            print(count)
    if count == 2:
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')
prime(num = int(input("Enter a number: ")),count=0)
keyword arguments
-----------------
-->Keyword arguments are sending arguments in a pair(a=2),and the pass order is not consider...
'''
'''
def data_(age,name,batch,location):
    print(name)
    print(age)
    print(batch)
    print(location)
data_(name='teja',age=45,location='vizag',batch=6)
'''
'''
variable length argument
------------------------
--> Adding a (* call it as args) before a variable at parameters,we can pass tuple of arguments and can be accessed with indexing
def all_(*Name):
    print(Name[2])
all_('Teja','Garikapati','Sony')
'''
'''
keyword length arguments
------------------------


def details(**data_):
     print(data_.keys())
details(Name ='Teja', age=45, location='Vizag', batch=6)

return
-----
-->The return keyword used inside the function , once the return is executed means it will get backk to calling function with certain return values
eg
--
'''
'''
def all_(a,b):
    return a-b
print(all_(7,9))
'''
'''
a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(a >> b)
print(~a)
'''
'''
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
print()
print(~b)
'''
def add_(a,b):
    print(a+b)
add_(5,6)

'''
lambda function is small anonymous function
lambda can take n number arguments,but only with one expression
the function is defined by using lambda function
'''


add_ = lambda a,b,c : a+b+c
print(add_(10,20,9))

even = lambda num : num % 2 == 0
print(even(2))

great_ = lambda a,b : a if a>b else b
print(great_(100,20))

cube_ = lambda a : a ** 3
print(cube_(3))
'''
filter()
--------
-->filter() function will perform only on selecting elements of literables
syntax --> filter(lambda arguments:expression, literable)
eg
--
'''

nums =[1,2,3,4,5,6]
data_ = filter(lambda a: a%2==0,nums)
print(list(data_))
'''
map():
------
-->map() function will perform on all elements of a literable
syntax --> map(lambda argument:expression,literable)
eg
--
'''    
nums = [1,2,3,4,5]
get_ = map(lambda a: a+4,nums)
print(list(get_))

from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,range(1,10))
print(data_)


