import random
x=random.randint(0,2)
option=['stone','paper','scissor']
if x==0:
    comp_pick = option[0]
elif x==1:
    comp_pick = option[1]
else :
    comp_pick = option[2]
ur_score=0
comp_score=0
i=0
while (i<=2):
    ur_option = input('\nselect:\nstone\npaper\nscissor\nenter ur option:')
    if  ur_option in option:
        if ur_option == 'stone' and comp_pick == 'scissor':
            print("you win!!")
            print("you picked", ur_option, "and computer picked", comp_pick)
            ur_score+=1
        elif ur_option == 'paper' and comp_pick == 'stone':
            print("you win!!")
            print("you picked", ur_option, "and computer picked", comp_pick)
            ur_score += 1
        elif ur_option == 'scissor' and comp_pick == 'paper':
            print("you win!!")
            print("you picked", ur_option, "and computer picked", comp_pick)
            ur_score += 1
        elif ur_option==comp_pick:
            print("No result")
            print("you picked", ur_option, "and computer picked", comp_pick)
        else:
            print("you lost!!")
            print("you picked", ur_option, "and computer picked", comp_pick)
            comp_score += 1

    else:
        print("Enter the input properly")
    i += 1

print("\nFinal result:")
if comp_score<ur_score:
    print("\nCONGRATULATION YOU WIN THE GAME!!!!!!")
elif comp_score>ur_score:
    print("\nYOU LOOSE THE GAME")
else:
    print("\nMATCH DRAWN")

print("\nFINAL SCORE:\nYou got:",ur_score,"\t Computer got:",comp_score)
