#logical operators
from tkinter.font import names

x=True
y=False
print(f"x and y:{x and y}")
print(f"x or y:{x or y}")
print(f"not x:{not x}")
#identity operators
list1=[1,3,4,5]
list2=list1
print(list1 is list2)

fruits=['apple','strawberries']
name=['ali','sana']
print(name is fruits)

list3=[4,5,6]
list4=[4,5,6]
print(f"list3 and list4:{list3 is list4}") #both the variables are pointing to different objects in memory so it will return a false
fav_food="cheese"
lunch_today="cheese"
print(f"favourite food is lunch today:{fav_food is lunch_today}")

alphatbets=['a','b','c']
other_alphabets=['a','b','c']
print(f"alphabets is other alphabets:{alphatbets is other_alphabets}")

#membership operators
print('apple' in fruits)
print('bnana' not in fruits)

