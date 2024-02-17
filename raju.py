import random
print("*****************")
print("*       * PAPER * ROCK * SCISSOR *            *")
print("*****************")
print(" Lets start the game!!.... ")
point=0
ai=0
while(True):
    c=input(" Choose Paper->p  Rock->r  Scissor->s Stop->stop: ")
    if(c=="p"):
        print("paper")
        point=10+random.randint(1,3)
        match point:
            case 11:
                print("Human: Paper", "AI: Rock")
                print("Human wins","AI lost the Match")
                print("____________")
            case 12:
                print("Human: Paper", "AI: Scissor")
                print("Human Lost","AI Won the Match")
                print("____________")
            case 13:
                print("Human: Paper", "AI: Rock")
                print("Match Draw")
                print("____________")
    elif(c=="r"):
        print("Rock")
    elif(c=="s"):
        print("Scissor")
    elif(c=="stop"):
         break
print("Program End")