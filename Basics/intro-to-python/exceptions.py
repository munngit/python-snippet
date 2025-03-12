from sys import exception

total=4
count=2
try:
    average=total/count
    print('average is',average)
except ZeroDivisionError as e:
    print('cannot divide by zero',e)
except NameError as e:
    print('you have a typo',e)
except exception as e: #handle any exceptions in general
    print('unexpected error',e)
finally:
    print('save my progress')
