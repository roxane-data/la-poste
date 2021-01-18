import re
f = open('input\connexion.log', 'r')
liste_h=[]
for line in f:
    line=re.split(";| ", line)
    h=line[3].strip()
    if h<"08:00" or h>"19:00":
        liste_h.append(line)
        #print(line)
        del line[2] 
        print(line)
f.close()