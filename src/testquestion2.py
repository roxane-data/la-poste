import re
f = open('input\connexion.log', 'r')
liste_h=[]

for line in f:
    #print(line)
    line=re.split(";| ", line)
    #print(line)
    #if line[1]<8 or line[1]>19:
        #print(line)
    liste_h.append(line) #la fonction .strip() permet de retirer le '\n' dans la liste 
#print(liste_h)
#liste_he=[[a, b, c, int(d), e] for a, b, c, d, e in liste_h]
#print(liste_he)
for ligne in liste_h:
    #print(ligne)
    for elmt in ligne:
        if elmt<"8:00" and elmt>="19:00":
            print(ligne)
# Fermeture du fichier prenoms.txt
f.close()