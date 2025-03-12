#primitive datatypes
#int
from contextlib import nullcontext

x=5
y=-10
print(x+y)
print (type(y))
#float
x=4.6
y=7.9
print(y-x)
#boolean
is_active=True
is_deleted=False
print(is_active)
print(type(is_active))
#strings
name='munaza'
print(name)
print(type(name))
#complex
z=2+3j
y=1+7j
print(z+y)
print(type(z))
#null
x=None
print(type(x))
#non primitive datatypes
#lists
mixed_list=['apple',1,45.5,True] #mixed list
print(mixed_list)
fruits=['apple','mango','banana']
print(fruits)
fruits[1]='kiwi'
print(fruits)
#tuple
coordinates=(4,5)
print(coordinates)

#set
numbers={1,2,3,4,5}
print(numbers)
#frozensets
numbers=frozenset({1,2,5,9,3})
print(numbers)
#dictionary
city={
     'name':'peshawar',
     'postal_code':25000
 }
print(city)
print(city['name'])