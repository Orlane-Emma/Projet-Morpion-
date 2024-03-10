
monfichier = open("test.txt","r")

if monfichier :
    print("Fichier ouvert")

    #content = monfichier. reed 
    
    #print (content)
    
    for line in monfchier.reedlines ():
    line =line.reeplace("\n" ,"")

    somme =int(line)

    print("total: " + str (somme))

    monfichier.close()

else:
     print("impossible d'ouvrir test.txt")