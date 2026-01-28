while True:
    user1_name = input("Enter user1 name: ")
    user2_name = input("Enter user2 name: ")
    user_input1 = input(f"{user1_name} -  enter your input : ").lower()
    user_input2 = input(f"{user2_name} -  enter your input : ").lower()
    if user_input1 == user_input2:
        print("Its a tie.")
    elif user_input1 == "rock" and user_input2 == "scissors":
        print(user1_name + " wins.")
    elif user_input1 == "rock" and user_input2 == "paper":
        print(user2_name + " wins.")
    elif user_input1 == "paper" and user_input2 == "rock":
        print(user1_name + " wins.")
    elif user_input1 == "paper" and user_input2 == "scissors":
        print(user2_name + " wins.")
    elif user_input1 == "scissors" and user_input2 == "paper":
        print(user1_name + " wins.")
    elif user_input1 == "scissors" and user_input2 == "rock":
        print(user2_name + " wins.")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue
    repeat = input("Do you want to play again? (yes/no): ").lower()
    if repeat == "yes":
        # Restart the game
        print("Restarting the game...")
        continue
    else:
        print("Thanks for playing!")
        break

