import random

Elements = ["Rock", "Paper", "Scissors"]

while(True):
    my_choice= input("Enter the Rock,Paper or scissors(or'quit' to stop)")
    
    if my_choice == "quit":
        print("Thanks for Playing!")
        break
    
    if my_choice not in Elements:
        print("Invalid Choice,Try Again!")
        continue
    
    computer_choice=random.choice(Elements)
    print(f"Computer choose: {computer_choice}")
        
    if my_choice == computer_choice:
        print("It's Tie!")
        
    elif(
        
        (my_choice == "Rock" and computer_choice == "Scissors")or
        (my_choice == "Scissors" and computer_choice == "Paper")or
        (my_choice == "Paper" and computer_choice == "Rock")
        
    ):
            
        print("Hurray!,You win")
        
    
        
    else:
        print("Oops!, You Lose")
        
        
print()