with open("input\warning.txt","r") as f1, open("input\connexion.log","r") as f2, open("output/suspect.txt","w") as f3:
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
    #print(*suspects,sep="\n")
    for l in suspects:
        l=str(l).strip("[]")
        print(l)
        f3.write("%s\n" % l)
    
   