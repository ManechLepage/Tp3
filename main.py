"""
Nom :Manech Lepage
Groupe : 306
Tp3 : Creer un systeme de combat de monstre
"""

import random

life_score = 20
monster_count = 0
defeat = 0
win = 0
win_streak = 0
win_streak_list = []
is_playing = True


def generate_fight(difficulty):
    """
    Fonction pour le systeme de combat
    :param difficulty: difficulté du monstre
    """
    global life_score
    global defeat
    global win
    global win_streak
    global win_streak_list
    number_rolled = random.randint(1, 6)
    print("=" * 50)
    print(f"Adversaire numéro {monster_count} :")
    print(f"\tDifficulté du monstre : {difficulty}")
    print(f"\tPoints de vies : {life_score}")
    print(f"\tCombat {monster_count} : {win} victoires et {defeat} défaites")
    print("=" * 50)
    print(f"Lancé de dé : {number_rolled}")
    initial_life_score = life_score
    if number_rolled <= difficulty:
        print(f"Vous avez perdu le combat : {number_rolled} vs {difficulty}")
        defeat += 1
        win_streak_list.append(win_streak)
        win_streak = 0
        life_score -= difficulty
        print(f"Points de vies : {initial_life_score} - {difficulty} = {life_score}")
        if life_score <= 0:
            death()
    else:
        print(f"Vous avez gagner le combat : {number_rolled} vs {difficulty}")
        win += 1
        win_streak += 1
        life_score += difficulty
        print(f"Points de vies : {initial_life_score} + {difficulty} = {life_score}")
    print(f"Nombres de victoires conséqutives : {win_streak}")



def generate_new_fight():
    """
    Regenerer un nouveau combat
    """
    print("=" * 50)
    difficulty = random.randint(1, 5)
    menu_choice(difficulty)


def settings():
    """
    Afficher les regles du jeu
    """
    print("=" * 50)
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  \nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. \nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  \nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire."
          "\n\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0."
          "\n\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

def death():
    """
    Finir le loop du jeu pour print le dernier message
    """
    global is_playing
    is_playing = False


def menu_choice(difficulty):
    """
    Fonction pour le choix du joueur
    :param difficulty: difficulté du monstre
    """
    global monster_count
    is_choice = False
    while not is_choice:
        choice = input(f"1: Combattre le monstre \n2: Fuir le combat et aller a une nouvelle porte\n3: Afficher les regles du jeu \n4: Quitter la partie\nDifficulté du monstre : {difficulty}\nChoix :  ")
        try:
            choice = int(choice)
            is_choice = True
            if choice == 1:
                monster_count += 1
                generate_fight(difficulty)
            elif choice == 2:
                generate_new_fight()
            elif choice == 3:
                settings()
            elif choice == 4:
                death()
        except:
            print("Erreur. Veuillez choisir un nombre.")
            print("=" * 50)


def main():
    """
    Fonction principale
    """
    global is_playing
    global monster_count
    global win
    global defeat
    global win_streak_list
    while is_playing :
        difficulty = random.randint(1, 5)
        print("=" * 50)
        menu_choice(difficulty)
    print("=" * 50)
    print(f"La partie est terminé, vous avez combattu contre {monster_count} monstres. Vous avez vaincu {win} d'entre eux et vous avez perdu contre {defeat} d'entre eux.\nvotre meilleur score de victoire conséqutive est de  : {max(win_streak_list)}")
    print("=" * 50)


if __name__ == "__main__":
    main()
