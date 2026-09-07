'''
List comprehension
------------------
--> List comprehension is the short form of syntax to create a list
syntax --> [expression loop condition]
syntax 2--> [expression condition else loop]
'''
'''
old_ = [1,2,3,4,5]
new_ = [i for i in old_ if i%2==0 ]
print(new_)
[[1,2,3],[4,5,6],[7,8,9]]

any_ = [[i*j for i in range(1,6)] for j in range(1,10)]
print(any_)
'''
'''
nested comprehension
--------------------
--> Using list comprehension generating list inside list
any_ = [[i*j for i in range(1,6)] for j in range(1,10)]
print(any_
of = [[1,2,3],
      [4,5,6],
      [7,8,9]]
data_ = [num for i in of for num in i]
print(data_)
generator
-----------
--> A generator is a special function with generate one valiue at a time
'''
def all_():
      for j in range(1,10):
          yield j
          
j = all_()
print(next(j))
print(next(j))
print(next(j))



