import random

life_score = 20
monster_count = 0


def generate_fight(difficulty):
    number_rolled = random.randint(1, 6)
    print("=" * 10)
    print(f"Lancé de dé : {number_rolled}")
    print("=" * 10)


def generate_new_fight():
    pass


def settings():
    pass


def quit():
    pass


def choice(string):
    isChoice = False
    difficulty = random.randint(1, 6)
    while not isChoice:
        choice = input(string)
        try:
            choice = int(choice)
            isChoice = True
        except:
            print("Erreur. Veuillez choisir un nombre.")

    if choice == 1:
        monster_count += 1
        generate_fight(difficulty)
    elif choice == 2:
        generate_new_fight()
    elif choice == 3:
        settings()
    elif choice == 4:
        quit()


def main():
    difficulty = random.randint(1, 5)
    choice(f"1: Combattre le monstre \n2: Fuir le combat et aller a une nouvelle porte\n3: Afficher les regles du jeu \n4: Quitter la partie\nDifficulté du monstre : {difficulty}\nChoix :  ")



if __name__ == "__main__":
    main()
