import random

def roll_die():
    return random.randint(1,6)

def player_turn():
    round_score = 0
    
    while True:
        print("This round you have: " + str(round_score))
        choice = input("Would you like to roll or bank? ")
        
        if choice == "roll":
            roll = roll_die()
            print("You rolled a " + str(roll))
            
            if roll == 1:
                print("You rolled a 1! You get 0 points this round.")
                round_score = 0
                break
            else:
                round_score += roll
                
        elif choice == "bank":
            break
        else:
            print("Please type roll or bank.")
            
    return round_score
    
def computer_turn():
    round_score = 0
    
    while round_score <= 15:
        roll = roll_die()
        print("The computer rolled a " + str(roll))
        
        if roll == 1:
            print("Computer rolled a 1! End of turn.")
            round_score = 0
            return round_score
            
        round_score += roll
        print("This round the computer has: " + str(round_score))
        
        if round_score <= 15:
            print("The computer chooses to roll again.")
        else:
            round_score += roll
            print("The computer chooses to bank.")
            return round_score
    return round_score
def main():
    player_total = 0
    computer_total = 0
    turn = 1
    
    while player_total < 100 and computer_total < 100:
        print(turn)
        print("Your current score is: " + str(player_total))
        print("Computer current score is: " + str(computer_total))
        
        player_total += player_turn()
        computer_total += computer_turn()
        
        turn += 1
        
    if player_total >= 100 and computer_total >= 100:
        if player_total > computer_total:
            print("You win!")
        else:
            print("Computer wins!")
    if player_total >= 100:
        print("You win!")
    else:
        print("Computer wins!")
        
main()