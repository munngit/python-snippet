# def game(starting_score=15.0,player_name='player 1'):
#     print ("starting_Score:",starting_score)
#     print("player_name:",player_name)
#
# game()
# game(20,'ali')



# def example(*args,**kwargs): #handle variable number of arguments
#     # print(args)
#     # print(kwargs)
#     first_name=kwargs['first_name'] #accessing first name from kwargs dictionary
#     print(first_name)
# # example(1,2,3,4)
# example(first_name='ali',age='21')

def example2(*,starting_score=15,player_name='player 1'):# everything after * is a keyword argument and has a default value in this case
    print("score:",starting_score)
    print("player:",player_name)

example2()
example2(starting_score=20)