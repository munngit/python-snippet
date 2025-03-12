#assigning values to multiple variables in one line
a,b,c=11,20,30
print(a)
print(b)
print(c)

#assigning same value to multiple variables
cat=dog=horse='animal'
print(cat)
print(dog)
print(horse)
#swapping values without temporary variable
a,b=5,10
print(a)
print(b)
a,b=b,a
print(a)
print(b)
#unpacking list or tuple
numbers=(1,2,3)
x,y,z=numbers #unpacking tuple and assigning it to variables
print(x)
print(y)
print(z)

# '*' operator for variable length assignment

a,*b=[5,9,20,22,11]
print(a)
print(b)

*a,b=[3,2,78,12,55]
print(a)
print(b)

# ignoring values using underscore

x,_,y=[12,4,22]
print(x)
print(y)

#multiple assignment in loops

pairs=[(1,'one'),(2,'two'),(3,'three')]
for num,words in pairs:
    print(num,words)