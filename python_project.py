# Python-Project

liste= [[2],[[4],'a'],['cat'],[6],8,'dog']
l=[]
def flatten (n):
    for i in n:
        if isinstance (i,list):
            flatten(i)
        else:
            l.append(i)
flatten (liste)
print (l)


liste_2= [[3],[6,9,12],[15],[18,21]]
liste_2.reverse()
for i in range (len(liste_2)):
    (liste_2[i])=(liste_2[i])[::-1]
    
print(liste_2)
