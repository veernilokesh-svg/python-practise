'''
ran_ = int(input('Enter a number: '))
for j in range(1,ran_+1):
    if j % 2 != 0:
        print(j)
'''
'''
nums =[23,78,97,5]
for j in nums:
    if j % 2 == 0:
        print(f'{j} is a evem')
    else:
        print(f'{j} is a odd')
'''
'''
words_ = input("Enter a word: ")
vowels = 'aeiou AEIOU'
count = 0
for i in words_:
    if i in vowels:
        count += 1
        print(f'{i} is vowel')
print(count)        
'''
'''
digits_ = [1,2,3,1,5,3]
empty_ += (i)
for i in digits_:
    if i not in empty_:
        empty_.append(i)
print(empty_)

    
digits_ = (1,2,3,1,5,3)
for i in digits_:
    if i in digits_:
        print(f'{i} is a duplicate')
'''
'''
words_= ' Python is a language '
print(len(words_.strip().split()))
nested loops
'''
'''
for i in range(30,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
'''
'''
for i in range(1,6):
    for j in range(i,i+1):
        print(i,end=" ")
    print()
'''
'''
count = 1
for i in range(a,e):
     for j in range(i):
         print(count,end="")
         count += 1
     print()
'''
'''
for i in range(97, 123):
    print(chr(i), "=", i)

for i in range(1,6):
    for j in range(i):
        print(chr(65+j),end="")
    print()


n = int(input("Enter ASCII code: "))

print("C:", ch(n))
'''
'''
words = input("Enter a word :")
empty_str = ''
for i in words:
    empty_str = i + empty_str
if empty_str == words:
       print(f"{words} is a palindrome")
else:
       print(f"{words} is not a palindrome")

num = 153
length_ = len(str(num))
amstrong_ = 0
for i  in str(num):
    amstrong_ = amstrong_ + int(i)**length_
    print(amstrong_)
if amstrong_ == num:
    print(f'{num} is Amstrong Number')
else:
    print(f'{num} is not amstrong number')
'''
'''
num = int(input('Enter a Number'))
sum_ = 0
for i in range(1,num):
            if num % i == 0:
               sum_ += i
if sum_ == num:
          print("Perfect number")
else:
          print("Not a perfect number")
'''
'''
num_ = 28
sum_ = 0
for i in range(1,num_):
     if num_ % i == 0:
         sum_ += i
if num_ == sum_:
    print("perfect number")
else:
    print("not a perfect number")
'''
'''
num = 0
num_2 = 1
print(num,num_2,end=' ')
for i in range(1,10):
    num_3 = num + num_2
    num = num_2
    num_2 = num_3
    print(num_3,end=' ')
'''
print(7&2)
print(20&35)
print(5^7)






    

    
