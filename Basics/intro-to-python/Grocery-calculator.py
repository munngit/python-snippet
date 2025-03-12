
food_prompt="""
Which food you are purchasing?(Choose a letter)
A)Banana
B)Apple
C)Cheese
D)Pickles
Q)To quit
"""
while True:
    qty_prompt="""
    How many do you need(Enter a number)
    """
    food=input(food_prompt)
    if food=='Q':
        print("Goodbye! Come again")
        break

    if food not in ['A','B','C','D']:
        print("invalid option....Try again")
        continue
    else:
        quantity=int(input(qty_prompt))
        if quantity<0:
            print("quantity wrong")
            continue
        if food=='A':
            cost=0.30
            food_label='Banana'
        elif food=='B':
            cost=2.00
            food_label = 'Apple'
        elif food=='C':
            cost=3.45
            food_label = 'Cheese'
        else:
            cost=1
            food_label = 'pickles'
    total= cost * quantity
    result="you are buying {} {} for ${}".format(quantity,food_label,total)
    print(result)