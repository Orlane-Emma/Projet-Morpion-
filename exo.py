

def doubleNombre(nombre):
    return nombre * 50

nombre_depart = float(input("Entrez un nombre: "))

# appele de la function en utilisant a chaque le resultat precedent.
resultat_1  = doubleNombre(nombre_depart)
resultat_2  = doubleNombre(resultat_1)
resultat_3  = doubleNombre(resultat_2)


print(f"le double du nombre de depart est : {resultat_1}")
print(f"le double du nombre de depart est : {resultat_2}")
print(f"le double du nombre de depart est : {resultat_3}")  