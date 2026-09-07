marks = 31
if marks >= 60:
     print('pass')
else:
     print('fail')     


age = 18
if age <= 28:
    print('young')
else:
    print('youth')


age = 16

if age >= 18:
    print("You are allowed to enter the movie.")
else:
    print("You are not allowed to enter the movie.")


marks = 80

if marks >= 100:
    print('Grade A')
else:
    print('Grade B')

'''
num = int(input("Enter a number: "))

if num >= 0:
    print("Positive")
else:
    print("Negative")
'''
'''

a = 90
b = 780
c =670
if a>b and a>c:
     print(a)
elif b>a and b>c:
     print(b)
else:
     print(c)
'''
'''
num = 7
num_2 = 67
user_opt = int(input('Enter \n1.add \n2.sub \n3.mul \n4.pow: '))
if user_opt == 1:
        print(num + num_2)
elif user_opt == 2:
     print(num - num_2)
elif user_opt == 3:
     print(num * num_2)
else:
     print(num ** num_2)
'''     
'''
nested if
----------
--> if inside an if statement is called nested if
'''
'''
app_details = {'Pin':1234}
import random
user_pass = int(input("Enter your app password: "))
otp = random.randint(1000,9999)
if user_pass == app_details['Pin']:
     print('password is correct')
     print(otp)
     user_otp = int(input("Enter 4 digit OTP:  "))
     if user_otp == otp:
          print('welcome to the app')
     else:
          print('incorrect OTP')
else:
     print('password is incorrect')

'''
'''
a = int(input("Enter a number: "))
if a % 2 == 0:
     print(f'{a} is even')
else:
     print(f'{a} is odd')
'''
'''
marks_ = int(input("Enter your marks: "))
if marks_ >= 90:
     print('A+')
elif marks_ >= 80:
     print('A')
elif marks_ >= 70:
     print('B+')
elif marks_ >= 60:
     print('B')
elif marks_ >= 50:
       print('C+')
elif marks_ >= 40:
     print('C')
else:
     print('fail')

'''
'''
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
elif num % 2 == 0 and num != 2:
    print("Not a prime number")
else:
    print("Prime number")

num = [1,2,3,1,2,3]
print(num.count(2))

for loop()
--> for loop is used to iterate over a squence or iterable datatypes
'''
nums =[12,3,5,78]
for num in nums:
     print(num)
'''
else in for
-----------
-->unlike if-else, else block in for statement is executed after completed of all iterations
eg
--
'''

nums = 'Python'
for num in nums:
     print(num)
else:
     print('For ended')
'''
break
-----
-->the break is used to stop iteration based on the condition given
'''
nums = [1,2,3,4,5,8,9]
for num in nums:
     print(num)
     if num == 3:
          break

val_ = [1,2,3,4,5,8,9]
for j in val_:
     if j % 2 == 0:
          print(f'{j} is even')
     else:

          print(f'{j} is odd')
          
'''         
continue
--------
-->the continue is a keyword used to skip the current iteration based on the condition
'''
nums = [1,2,3,4,5,8,9]
for num in nums:

     if num == 5:
          continue
     print(num)
'''        
pass
----
--> A pass is called space holder, that is used after statements like (if, for, else) not to raise any error
'''
for j in range(1,33):
     if j == 82:
          print(j)
     else:
          pass
'''




assert
------
--> assert is a keyword used to check the condition, incase the condition is false,it will raise the error (Assertion error)
eg
--
'''
age = 19
assert age >= 18, 'Not eligible to vote'
print('Your eligible to vote')

marks = 96
assert marks >= 91, 'Grade A+'
print('Grade C')
'''
num = 1+while num < 5:
print(num)
     num += 1

num = 9
count =0
for i in range(1,num

'''
'''
for i in [10,20,30,40,50]:
               
     print(i)
i = 10
print(10)


for i in range(101):
    print(i-1)
    
arr = [1,2,3,4,5]
for i in range(len(arr)):
     print(i)

arr = [1,2,3,4,5]
for i in arr:
     print(i)
'''
arr = [10,20,30,40,50]

for i in range(4):
     print(arr)

num=int(input("Enter number: ")); print("Even" if num%2==0 else "Odd")


numbers = [1,2,3,4,2,3,4,7,8,8,9]
unique_numbers = list(set(numbers))
print(unique_numbers)
'''
num=int(input("Enter number: "));
print("Armstrong" if num==sum(int(d)**len(str(num)) for d in str(num)) else "Not Armstrong")
'''

num = int(input())
original = num
digit = len(str(num))
total = 0
while num>0:
     k = num % 10
     total = total + k**digits
     num = num//10
if total == original:     

     print('Armstrong number')
else:
          print('not')


 s=input("Enter string: ");print(sum(1 for ch in s.lower() if ch in "aeiou"))

 print("e",e)
 print("i",i)
 print("o"),o)
 print("u",o)
 text = input()
 count = 0
 for char in text:
      if char.lower() in "aeiou":
           count+= 1
           print(count)


