
import random

# Fonction pour afficher le début et la présentation des joueurs.
def supermorpion():
    print("Bienvenue dans le Super Morpion !")
    print("Le premier joueur est : ❌") 
    print("Le deuxième joueur est : ⭕️\n ") 

# Fonction pour choisir un coup pour l'ordinateur (ennemi).
def choisir_coup_ordinateur(grille):
    cases_vides = [(i,j) for i in range(3) for j in range(3) if grille[i][j] == " "]
    return random.choice(cases_vides)

# Fonction pour afficher la grille.
def afficher_grille(grille):
    for ligne in grille:
        print("|".join(ligne)) # représente les | lignes pour séparer les colonnes.
        print("-" * 5)   # représente les - pour les rangées 

# Fonction pour vérifier la victoire (X ou O).
def verifier_victoire(grille, joueur):
    for ligne in grille:
        if all(symbol == joueur for symbol in ligne):
            return True
    for col in range(3):
        if all(grille[i][col] == joueur for i in range(3)):
            return True
    if all(grille[i][i] == joueur for i in range(3)) or all(grille[i][2 - i] == joueur for i in range(3)):
        return True
    return False

# Fonction pour lancer le tour à tour avec l'ordinateur.
def jouer_supermorpion():
    grille = [[" "]*3 for _ in range(3)]
    joueur = "X"
    while True:
        afficher_grille(grille)
        if joueur == "X":
            print("C'est à votre tour.")
            ligne = int(input("Saisir une ligne : ")) - 1
            colonne = int(input("Saisir une colonne : ")) - 1
        else:
            print("C'est au tour de l'ennemi.")
            ligne, colonne = choisir_coup_ordinateur(grille)
            print(f"L'ennemi joue en ligne {ligne + 1} et colonne {colonne + 1}.")
        
        if grille[ligne][colonne] == " ":
            grille[ligne][colonne] = joueur
            if verifier_victoire(grille, joueur):
                afficher_grille(grille)
                print(f"Le joueur {joueur} a gagné !")
                break
            elif all(symbol != " " for ligne in grille for symbol in ligne):
                afficher_grille(grille)
                print("Match nul !")
                break
            joueur = "O" if joueur == "X" else "X"
        else:
            print("Cette case est déjà occupée, veuillez choisir une autre case.")

# Fonction principale pour lancer le jeu.
def main(): 
    supermorpion()
    jouer_supermorpion()

# Appel de la fonction principale.
if __name__ == "__main__":
    main() 
