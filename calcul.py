from main import addition, soustraction, multiplication, division

historique_calcule   = []

def afficher_menu():
    print("Choisissez l'opération à effectuer :")
    print("1 ou A - Addition")
    print("2 ou S - Soustraction")
    print("3 ou M - Multiplication")
    print("4 ou D - Division (Entière)")
    print("Q - Quitter")

def afficher_historique ():
    print("\nHistorique des calculs : ")
    for i, calcul in enumerate (historique, 1):
        print (f"{i}. {calcul}")


def main():
    while True:
        afficher_menu()
        choix = input("Votre choix : ").upper()

        if choix == 'Q':
            print("Au revoir !")
            break
        
        if choix in ['1', 'A']:
            operation = addition
        elif choix in ['2', 'S']:
            operation = soustraction
        elif choix in ['3', 'M']:
            operation = multiplication
        elif choix in ['4', 'D']:
            operation = division
        else:
            print("Choix invalide.")

        try:
            a = float(input("Entrez le premier nombre : "))
            b = float(input("Entrez le deuxième nombre : "))
            resultat = operation(a, b)
            print("Le résultat de l'opération est :", resultat)
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")

if __name__ == "__main__":
    main()
