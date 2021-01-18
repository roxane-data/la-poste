with open("input\connexion.log","r") as fichier1, open("utilisateurs.txt","w") as fichier2:
    for ligne in fichier1:
        ligne=ligne.split(";")
        print(ligne[1])
        #fichier2.write("%s\n" % ligne[1])