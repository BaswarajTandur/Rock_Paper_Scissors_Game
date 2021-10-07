#ROCK-PAPER-SCISSOR GAME
import random
choices=["rock","paper","scissor"]
choices_lst={1:"rock", 2:"paper", 3:"scissor" }
count_lst=[]
print("--------------------------------------------------------------------------")
print("Welcome to ASH's  ROCK-PAPER-SCISSOR GAME")
rounds=1
try:
    while rounds<=10 :
        print("--------------------------------------------------------------------------")
        print("ROUND ",rounds)
        for key,value in choices_lst.items():
            print("Press ", key ," for ", value,"\n",end="")
        u_choice=int(input())
        print("Your choice is: ",choices_lst[u_choice])
        s_choice = random.choice(choices)
        print("System choice is: ", s_choice)

        if u_choice== 1:
            if s_choice=="rock":
                count_lst.append("Tie")
                print("Match Tied")
            elif s_choice=="paper":
                count_lst.append("System Won")
                print("System Won")
            else:
                count_lst.append("User Won")
                print("User Won")

        elif u_choice== 2:
            if s_choice == "rock":
                count_lst.append("User Won")
                print("User Won")
            elif s_choice == "paper":
                count_lst.append("Tie")
                print("Match Tied")
            else:
                count_lst.append("System Won")
                print("System Won")

        else:
            if s_choice == "rock":
                count_lst.append("System Won")
                print("System Won")
            elif s_choice == "paper":
                count_lst.append("User Won")
                print("User Won")
            else:
                count_lst.append("Tie")
                print("Match Tied")
        rounds=rounds+1
except:{ print("INVALID Input"),exit()}

from collections import Counter
c=Counter(count_lst)
print("User Victories  : ",c["User Won"],"\n"
      "System Victories: ",c["System Won"],"\n"
      "Tied Matches    : ",c["Tie"],"\n" )
if c["User Won"]>c["System Won"]:
    print("YOU WON, CONGRATSSS!!!!!")
elif c["User Won"]<c["System Won"]:
    print("YOU LOST, BETTER LUCK NEXT TIME!")
else:print("Match Tied, Try Again")


# if c["User Won"]>c["System Won"] and c["User Won"]>c["Tie"]:
#     print("YOU WON, CONGRATSSS!!!!!")
# elif c["System Won"]>c["User Won"] and c["System Won"]>c["Tie"]:
#     print("YOU LOST, BETTER LUCK NEXT TIME!")
# else:print("Match Tied, Try Again")

