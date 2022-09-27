import random

life_score = 20
monster_count = 0

def generateFight(difficulty):
    monster_count += 1
    print(f"")
    number_rolled = random.randint(1, 6)
    print(f"Lancé de dé : {number_rolled}")
def generateNewFight():
    pass
def settings():
    pass
def quit():
    pass
def choice(string):
    isChoice = False
    difficulty = random.randint(1, 6)
    while not isChoice :
        choice = input(string)
        try:
            choice = int(choice)
            isChoice = True
        except:
            print("Erreur. Veuillez choisir un nombre.")

    if choice == 1:
        generateFight(difficulty)
    elif choice == 2:
        generateNewFight()
    elif choice == 3:
        settings()
    elif choice == 4:
        quit()

def main():
    choice("1: Combattre le monstre \n2: Fuir le combat et aller a une nouvelle porte\n3: Afficher les regles du jeu \n4: Quitter la partie")

if __name__ == "__main__":
    main()