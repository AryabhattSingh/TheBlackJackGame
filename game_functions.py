import random
import os
from ascii_art import logo


def clear_screen():
    """This function clears the terminal"""
    os.system('cls')


def draw_a_card():
    """The function draws a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)


def calculate_score(player_cards):
    """This function calculates the score of a player. This function also adjusts the value of Ace if the player's
    score is going over 21"""
    score = sum(player_cards)
    if score == 21 and len(player_cards) == 2:
        score = 0
    else:
        if score > 21 and 11 in player_cards:
            index_of_11 = player_cards.index(11)
            player_cards[index_of_11] = 1
            score = sum(player_cards)
    return score


def print_final_hand(user_cards, user_score, computer_cards, computer_score):
    """This function prints the final cards of user and computer"""
    print(f"\n{'*' * 85}")
    print(f"Your final hand: {user_cards}\nComputer's final hand: {computer_cards}")
    print(f"""                     
                                    Your Final Score : {user_score}
                                 Computer's Final Score : {computer_score}
    """, end="")


def compare(user_score, computer_score):
    """This function prints the result of the game with an explanation"""
    if user_score > 21:
        print("""
                                    You went over 21!
                                        You lost!
        """)
    elif computer_score > 21:
        print("""
                                    Computer went over 21!
                                          You won!
        """)
    else:
        # If computer gets blackjack, then the user loses (even if the user also has a blackjack). If the user gets a
        # blackjack, then they win (unless the computer also has a blackjack).
        if computer_score == 0:
            print("""               
                                    Computer got Black Jack!
                                          Computer won!
            """)
        elif user_score == 0:
            print("""
                                    You got Black Jack!
                                         You Won!
            """)
        elif user_score == computer_score:
            print("""
                                    You and Computer both have same score!
                                                 Game Draw!
            """)
        elif user_score == 21:
            print("""
                                    You scored perfect 21!
                                            You won!
            """)
        elif computer_score == 21:
            print("""                 
                                    Computer scored perfect 21!
                                             You lost!
            """)
        elif user_score > computer_score:
            print("""
                                    You scored higher!
                                         You won!
            """)
        else:
            print("""
                                    Computer scored higher!
                                           You lost!
            """)
    print(f"{'*' * 85}")


def play():
    """This function can be used to play the game"""
    # Creating empty lists for drawn cards and initializing scores
    computer_cards = []
    user_cards = []
    computer_score = 0
    user_score = 0
    print(logo)
    # Drawing initial 2 cards for user and computer each
    for _ in range(2):
        user_cards.append(draw_a_card())
        computer_cards.append(draw_a_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\nYour Cards: {user_cards}, Current Score : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")
        # If user or computer has Black Jack or User has gone over 21, loop will stop
        # If user doesn't want to draw another card, the loop will stop
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = ""
            # Keep asking for input unless user enter a valid entry
            while another_card != "y" and another_card != "n":
                another_card = input("\nDo you want another card?\nType 'y' to CONFIRM or Type 'n' to PASS : ").lower()
                if another_card == "y":
                    user_cards.append(draw_a_card())
                elif another_card == "n":
                    game_over = True
                else:
                    print(f"\n{'+' * 50}")
                    print("              Kindly enter a valid input!")
                    print(f"{'+' * 50}")

    # If computer doesn't have a Black Jack and has score less than 17, it will keep drawing cards until score >= 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(draw_a_card())
        computer_score = calculate_score(computer_cards)

    # Printing final cards of User and Computer
    print_final_hand(user_cards, user_score, computer_cards, computer_score)
    # Comparing user & player scores and printing who won
    compare(user_score, computer_score)
