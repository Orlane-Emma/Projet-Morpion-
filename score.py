


# Fonction pour charger les scores à partir d'un fichier
def charger_scores(test2):
    try:
        with open(test2, 'r') as fichier:
            scores = [int(score.strip()) for score in fichier.readlines()]
            return scores
    except FileNotFoundError:
        print("Le fichier des scores n'existe pas.")
        return []

# Fonction pour enregistrer les scores dans un fichier
def enregistrer_scores(test2, scores):
    with open(test2 , 'w') as fichier:
        for score in scores:
            fichier.write(str(score) + '\n')

# Fonction pour afficher les 5 meilleurs scores
def afficher_scores(scores):
    print("Les 5 meilleurs scores sont :")
    for i, score in enumerate(scores, 1):
        print(f"{i}. {score}")

# Fonction pour vérifier si un score est dans les 5 meilleurs
def est_dans_meilleurs(scores, nouveau_score):
    return len(scores) < 5 or nouveau_score > min(scores)

# Fonction principale
def main():
    nom_fichier_scores = "scores.txt"
    scores = charger_scores(nom_fichier_scores)
    if not scores:
        return

    afficher_scores(scores)

    try:
        nouveau_score = int(input("Entrez votre score : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return

    if est_dans_meilleurs(scores, nouveau_score):
        print("Félicitations ! Votre score fait partie des 5 meilleurs !")
        scores.append(nouveau_score)
        scores.sort(reverse=True)
        scores = scores[:5]  # Garder uniquement les 5 meilleurs scores
        enregistrer_scores(nom_fichier_scores, scores)
        afficher_scores(scores)
    else:
        print("Dommage ! Votre score ne fait pas partie des 5 meilleurs.")

if __name__ == "__main__":
    main()