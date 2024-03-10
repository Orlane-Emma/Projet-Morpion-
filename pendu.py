import random

# Liste de mots à deviner
mots = ["Andrea", "Maison", "Bonbons", "Ecole", "Amour"]

# Choisir un mot aléatoire
mot_a_deviner = random.choice(mots)

# Nombre maximal de coups autorisés
max_coups = 7

# Liste des lettres déjà devinées
lettres_trouvees = []

# Fonction pour afficher le mot avec les lettres déjà devinées
def afficher_mot():
    mot_cache = ""
    for lettre in mot_a_deviner:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    return mot_cache

# Fonction principale du jeu
def pendu():
    print("Bienvenue dans le jeu du Pendu !")
    print("Vous devez deviner un mot en proposant des lettres.")
    print(f"Le mot à deviner contient {len(mot_a_deviner)} lettres.")

    nb_coups = 0
    while nb_coups < max_coups:
        print("\nMot à deviner :", afficher_mot())
        lettre = input("Entrez une lettre : ").upper()

        if lettre in lettres_trouvees:
            print("Vous avez déjà deviné cette lettre.")
        elif lettre in mot_a_deviner:
            print("Bravo ! Cette lettre est dans le mot.")
            lettres_trouvees.append(lettre)
            if afficher_mot() == mot_a_deviner:
                print("Félicitations ! Vous avez deviné le mot :", mot_a_deviner)
                break
        else:
            print("Dommage ! Cette lettre n'est pas dans le mot.")
            nb_coups += 1

    if nb_coups == max_coups:
        print("Vous avez atteint le nombre maximal de coups. Le mot à deviner était :", mot_a_deviner)

# Lancer le jeu
pendu()
