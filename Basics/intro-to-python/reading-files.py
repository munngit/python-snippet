# file=open('C:/Users/devmu/OneDrive/Desktop/data.txt','r')
#
# for line in file:
#     print(line)
# file.seek(0) # move the cursor to the initial position
# for line in file:
#     print(line)

# lines=file.readlines()  #return each line as a string with a new line character
# print(lines)

# text=file.read() # print block of text
# print(text)

# file.close()

with open('C:/Users/devmu/OneDrive/Desktop/data.txt','r') as file:
    for line in file:
         print(line)
    file.seek(0)
    for line in file:
        print(line) #dont need to clos the file explicitly in this case