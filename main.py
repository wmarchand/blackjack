############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.






from art import logo
import random
from replit import clear
    
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def compare(user_final_score, dealer_final_score):
    if user_final_score == 0 and dealer_final_score == 0:
        print(logo)
        print(f"\tYour final cards: {user_cards}, final score: {user_final_score}")
        print(f"\tDealer's final cards: {dealer_cards}, final score: {dealer_final_score}")
        print("Wow what a rare occurance! You both got a Black Jack!!! It's a Draw. 🤯🤯🤯")
        print("\n\t\t\t(⓿_⓿)\n")
    elif user_final_score == dealer_final_score:
        print(logo)
        print(f"\tYour final cards: {user_cards}, final score: {user_final_score}")
        print(f"\tDealer's final cards: {dealer_cards}, final score: {dealer_final_score}")
        print("You score the same as the Dealer. Draw. 😬😬😬")
        print("\n\t\t\t(´。＿。｀)\n")
    elif dealer_final_score == 0:
        print(logo)
        print(f"\tYour final cards: {user_cards}, final score: {user_final_score}")
        print(f"\tDealer's final cards: {dealer_cards}, final score: {dealer_final_score}")
        print("The dealer has hit a Blackjack. You Lose. 😭😭😭")
        print("\n\t\t\t(╯▔皿▔)╯\n")
    elif dealer_final_score > 21:
        print(logo)
        print(f"\tYour final cards: {user_cards}, final score: {user_final_score}")
        print(f"\tDealer's final cards: {dealer_cards}, final score: {dealer_final_score}")
        print("The Dealer has went over 21 and therefore the Dealer's hand is a Bust. You WIN!!! 😁😁😁")
        print("\n\t\t\t(〃￣︶￣)人(￣︶￣〃)\n")
    elif user_final_score > dealer_final_score:
        print(logo)
        print(f"\tYour final cards: {user_cards}, final score: {user_final_score}")
        print(f"\tDealer's final cards: {dealer_cards}, final score: {dealer_final_score}")
        print("You have a higher score than the Dealer. You Win!!! 😁😁😁")
        print("\n\t\t\t(〃￣︶￣)人(￣︶￣〃)\n")
    elif user_final_score < dealer_final_score:
        print(logo)
        print(f"\tYour final cards: {user_cards}, final score: {user_final_score}")
        print(f"\tDealer's final cards: {dealer_cards}, final score: {dealer_final_score}")
        print("You have a lower score than the Dealer. You Lose. 😭😭😭")
        print("\n\t\t\t(╯▔皿▔)╯\n")
    else:
        print(f"\tYour final cards: {user_cards}, final score: {user_final_score}")
        print(f"\tDealer's final cards: {dealer_cards}, final score: {dealer_final_score}")
        print("Testing to see why this was missed.")

def calculate_score(sum_of_hand):
    total_hand = sum(sum_of_hand)
    if len(sum_of_hand) == 2 and total_hand == 21:
        return 0
    elif 11 in sum_of_hand and total_hand > 21:
        sum_of_hand.remove(11)
        sum_of_hand.append(1)
        return sum(sum_of_hand)
    else:    
        return (sum(sum_of_hand))

def play():
    user_total = calculate_score(user_cards)
    dealer_total = calculate_score(dealer_cards)

    if user_total == 0:
        print(logo)
        print(f"\tYour final cards: {user_cards}, final score: {user_total}")
        print(f"\tDealer's final cards: {dealer_cards}, final score: {dealer_total}")
        print("🎆🎆🎆 You hit a Blackjack! YOU WIN! 😁😁😁")
        print("\n\t\t\tヾ(＠⌒ー⌒＠)ノ\n")
    else:
        hit_me = True
        while hit_me:
            print(logo) 
            print(f"\tYour cards: {user_cards}, current score: {user_total}")
            print(f"\tDealer's first card: {dealer_cards[0]}")
            
            hit = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if hit == 'y':
                clear()
                user_cards.append(deal_card())
                user_total = calculate_score(user_cards)
                if user_total > 21:
                    print(logo)
                    print(f"\tYour final cards: {user_cards}, final score: {user_total}")
                    print(f"\tDealer's final cards: {dealer_cards}, final score: {dealer_total}")
                    print("You have went over 21 and therefore your hand is a Bust. You Lose. 😭😭😭")
                    print("\n\t\t\t(￣﹏￣；)\n")
                    hit_me = False
                else:
                    play()
                    hit_me = False
            elif hit == 'n':
                clear()
                while dealer_total != 0 and dealer_total < 17:
                    dealer_cards.append(deal_card())
                    dealer_total = calculate_score(dealer_cards)
                compare(user_total, dealer_total)
                hit_me = False
            else:
                clear()
                print("I did not understand your answer. Please follow instructions. ")

user_cards = []
dealer_cards = []
    
want_to_play = True
while want_to_play:
    user_cards.clear()
    dealer_cards.clear()
    for hand_dealt in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == 'y':
        clear()
        play()
    elif start == 'n':
        print("Goodbye.")
        want_to_play = False
    else:
        print("I did not understand your answer. Please follow instructions. ")
    