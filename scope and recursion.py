'''
scope
1.local variable
----------------
-->A variable is defined inside the function call it as local variable, where the variable can only access with in that function
eg
--
2.Global variable can only access
-->A variable that is defined outside a function call and it can access anywhere through out program
global is keyword used to reaccess new values to variable that was already define outside the function call
eg
--

'''
'''
def display():
    name = 'Teja'
    print(name)
display()

a = 90
print(a)
def display():
    
    a = 10
    print(a)
display()
print(a)
'''
num = 7
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(num)
'''
Recursion function
------------------
-->The function call itself untill the base condition met..
'''

def Fac(a):
    if a == 1:
        return a
    return a * Fac(a-1)
print(Fac(1000))
