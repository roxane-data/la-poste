from collections import Counter
with open("input\warning.txt","r") as f1, open("input\connexion.log","r") as f2, open("suspect.txt","w") as f3:
    ip_danger=[]
    occurence=[]
    for line in f1:
    #print(line)
        ip_danger.append(line.strip())
    print(ip_danger)
    for ligne in f2:
        for elmt in ip_danger:
            if elmt in ligne:
                ligne=ligne.strip()
                ligne=ligne.split(";")
                #print(ligne)
                occurence.append(ligne[1])
    #print(occurence)
    suspects=[[x,occurence.count(x)] for x in set(occurence)]
    print(suspects)
    for l in suspects:
        print(l)
        f3.write("%s\n" % l)
    #occurence=Counter(occurence)
    #print(occurence)
    #print(*suspects,sep="\n")
    #f3.write("%s\n" % suspects)
              
                

                
                
        

