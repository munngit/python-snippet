#writing to a file
# output_filename='output.txt'
# with open(output_filename,'w') as file:
#     file.write("hi")

#   appending to an existing file
# output_filename = 'output.txt'
# with open(output_filename, 'a') as file:
#     file.write("wowwww \n")  # Adds a newline at the end of the string
#
#copying file
# output_filename = 'output.txt'
# with open('C:/Users/devmu/OneDrive/Desktop/data.txt','r') as input_file,open(output_filename,'w') as output:
#     for line in input_file: #remove existing data of output file and copy content from data.txt into output file
#         output.write(line)

#append  the content of data.txt to output file without deleting the existing content of output file
# output_filename = 'output.txt'
# with open('C:/Users/devmu/OneDrive/Desktop/data.txt','r') as input_file,open(output_filename,'a') as output:
#     for line in input_file:
#         output.write(line)


output_filename = 'output.txt'
with open('C:/Users/devmu/OneDrive/Desktop/data.txt','r') as input_file,open(output_filename,'w') as output:
    for line in input_file:
       if line != '\n':
           output.write(line)