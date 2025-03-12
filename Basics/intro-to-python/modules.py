# import os
# os.chdir() #change directory
# current_directory=os.getcwd() #gives current working directory
# directory_files=os.listdir() #list what's inside current working directory
#s.chdir('..')
# filepath=os.path.join(current_directory,'exceptions.py')
# exception_stats=os.stat(filepath) #gives metadata
# print('current working directory:',current_directory)
# print('my files are:',directory_files)
# print('current filepath is:',filepath)
# print('my exception file:',exception_stats)

from datetime import datetime,timedelta
today=datetime.now()
first_of_the_year=datetime(2025,1,1)
how_many_days=first_of_the_year-today
day_increment=timedelta(days=1,seconds=300)
tomorrow=today+day_increment
print(tomorrow)
print(how_many_days)