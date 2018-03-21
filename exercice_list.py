# creer une liste vide   mylist = []
# for une boucle for de range(5)
# entrer des valeurs au clavier avec la fonction input()
# attention a convertir les donnees en entier
# faire un tri
# afficher la liste


#list declaration
mylist = []

#values acquisition
for x in range(5):
    Num = input('Enter an integer: ')
    if Num.isdigit():
        mylist.append(int(Num))
    else : print("That's not an integer")


#sort list
mylist.sort()

#output
print(mylist)
