#implicit conversion

a=5
b=3.9
sum=a+b
print(sum)
print(type(sum))

a=9
z=3-7j
result=a-z
print(result)
print(type(result))

#explicit conversions
num=10.8
converted=int(num)
print(converted)
print(type(converted))

text="123"
num=int(text)
print(num,type(num))

num=100
text=str(num)
print(text,type(text))

lst=[100,2000,2,0]
tup=tuple(lst)
print(tup,type(tup))

lst=[1,1,2,3,45,45,6,7]
new_set=set(lst) #remove duplicates
print(new_set,type(new_set))

text='hello'
lst=list(text)
print(lst,type(lst))

print(int(True))
print(int(False))

statement='True'
print(bool(statement))

statement='False'
print(bool(statement))

statement=''
print(bool(statement))

a=0
print(bool(a))

b=1
print(bool(b))

b=-12324343
print(bool(b))