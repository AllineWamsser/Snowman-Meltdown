"""
    Entry point for the Snowman Meltdown game.

"""
from game_logic import play_game

def main():
    """
    Runs the game and asks the user if they want to replay.

    """
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()

        if again == "y":
            play_game()

        elif again == "n":
            print("Goodbey!Thanks for playing!")
            break

if __name__ == "__main__":
    main()