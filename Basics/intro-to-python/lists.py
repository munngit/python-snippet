my_list=[]
my_list=[1,2,3,4,5]
mixed_list=[1,34.5,'fruit',True]
nested_list=[1,[2,3],4,6,['a','b']]
print(mixed_list)
print(nested_list)

numbers=[1,2,3]
print(numbers)
numbers.append(4)
print(numbers)

alphabets=['a','c','d']
print(alphabets)
alphabets.insert(1,'b')
print(alphabets)

list1=[1,2,3,4]
list2=[4,5,6,7,8]
list1.extend(list2)
print(list1)

numbers=[4,5,6,6,7,8]
numbers.remove(6) #remove element from list by passing that particular element
print(numbers)

alphabets=['a','b','c','d']
pop_element=alphabets.pop(1) #remove element of a list by passing index.it returns the pop out value too
print(alphabets)
print(pop_element)
alphabets.pop()
print(alphabets)

alphabets=['c','d','e','f','g','h']
del alphabets[0] #deleting element at specific index
print(alphabets)
del alphabets[1:3] #deleting range of element
print(alphabets)
del alphabets #deleting the entire list

numbers=[30,40,5,3,12,34,23,56,78,90]
numbers[0]=100
print(numbers)
numbers[0:2]=[200,300]
print(numbers)

numbers.reverse()
print(numbers)

numbers=[1,2,3,4,5,6]
reversed_num=numbers[::-1] #reversing a list using slicing
print(reversed_num)

numbers=[30,40,5,3,12,34,23,56,78,90]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#sorting without modifying original list
numbers=[8,9,0,2,1,4,90,]
sorted_num=sorted(numbers)
print(numbers)
print(sorted_num)

numbers=[1,2,3,4,5,6]
reversed_num=reversed(numbers)
print(numbers)
print(list(reversed_num))

numbers=[20,230,240,6,6,0,23,21]
sliced_list=numbers[::2]
print(sliced_list)
list2=numbers[0:2]
print(list2)

list3=numbers[-3:] #starts from -3 index and go to the very end
print(list3)


