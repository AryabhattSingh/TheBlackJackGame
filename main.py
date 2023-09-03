from game_functions import clear_screen, play

game_start = ""
while game_start != "n":
    game_start = input("\nDo you want to play a game of BlackJack?\nType 'y' or 'n' : ").lower()
    if game_start == "y":
        clear_screen()
        play()
    elif game_start == "n":
        print(f"\n{'-' * 50}")
        print("                     Goodbye!")
        print(f"{'-' * 50}")
    else:
        print(f"\n{'+' * 50}")
        print("              Kindly enter a valid input!")
        print(f"{'+' * 50}")
