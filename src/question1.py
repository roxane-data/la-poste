with open("input\connexion.log","r") as f1, open("output/utilisateurs.txt","w") as f2:
    #utilisateurbis=[]
    for ligne in f1:
        ligne=ligne.split(";")
        #print(ligne)
        #print(ligne[1])
        #utilisateurbis.append(ligne[1])
        #print(utilisateurbis)
        f2.write("%s\n" % ligne[1])