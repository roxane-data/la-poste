# Ouverture du fichier prenoms.txt
f = open('input\small_connex.txt', 'r')
utilisateurbis=[]

for line in f:
    #print(line)
    line=line.split(";")
    print(line)
    print(line[1])

    utilisateurbis.append(line[1]) #la fonction .strip() permet de retirer le '\n' dans la liste 


print(utilisateurbis)

# Fermeture du fichier prenoms.txt
f.close()

with open("input\small_connex.log","r") as fichier1, open("utilisateursbis.txt","w") as fichier2:
    #utilisateurbis=[]
    for ligne in fichier1:
        ligne=ligne.split(";")
        #print(ligne)
        #print(ligne[1])
        #utilisateurbis.append(ligne[1])
        #print(utilisateurbis)
        fichier2.write("%s\n" % ligne[1])