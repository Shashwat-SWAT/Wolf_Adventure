from game import GAME

def main():

    Player_name = input("Adventurer, enter you name: ")
    Instance = GAME(Player_name)
    Instance.run()

if __name__ == "__main__":
    main()