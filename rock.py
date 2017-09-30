while True:
    import random
    option =["rock" ,"paper", "scissors"]
    computers_choice =random.choice(option)
    print("rock!")
    print("paper!")
    print("scissors")
    print("i would go with {} ".format(computers_choice))   
    magic_word = input("enter your choice: ")
    if magic_word in option:
        if (magic_word == "rock" and computers_choice == "rock"):
            print("go again")
        elif(magic_word == "rock" and computers_choice=="scissors"):
            print("rock wins!..congragulations")
        elif(magic_word == "rock" and computers_choice == "paper"):
            print("paper wins!..congragulations")
        elif(magic_word == "paper" and computers_choice == "paper"):
            print("go again!")
        elif(magic_word == "paper" and computers_choice == "rock"):
            print("paper wins!..congragulations")
        elif(magic_word == "paper" and computers_choice == "scissors"):
            print("scissors wins!..congragulations")
        elif(magic_word == "scissors" and computers_choice == "scissors"):
            print("go again")
        elif(magic_word == "scissors" and computers_choice == "paper"):
            print("scissors wins!..congragulations")
        elif(magic_word == "scissors" and computers_choice == "rock"):
            print("rock wins!..congragulations")
    else:
        print("please enter one option from {}".format(option)) 
   
    
    
