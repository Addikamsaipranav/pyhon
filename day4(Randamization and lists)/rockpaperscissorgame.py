#first lets decide the rules for the game
# Rock wins against scissor
# Scissor wins against Paper
# Paper wins against Rock

# rock = 0
#paper = 1
#scissor = 2

import random
user_choice = int(input("What do you wana chose ? Type 0 for Rock , 1 for paper , 2 for scissor "))
computer_choice = random.randint(0,2)
print(computer_choice)
if user_choice > 2 :
    print("invalid input please select the input in between 0 ,1 ,2")
elif(user_choice == computer_choice):
    print("tie game")
elif(user_choice==0 and computer_choice==2):
            print("you win")    
elif(user_choice==0 and computer_choice==1):
     print("you loose")        
else :
      if(user_choice != 0):
        if user_choice > computer_choice:
            print("you win")
        elif(computer_choice == 0):
            print("you loose")
          
