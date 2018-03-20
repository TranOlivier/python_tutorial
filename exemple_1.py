#!/usr/bin/env python
# #! = shebang permet de lancer une commande shell, doit être en première ligne de script!
# ici sert à charger la version de l'utilisateur depuis son environnement python
#dans le terminal: -rw-rw-r-- droit pour les users, group puis other r=read, w=write, x= exec

#import fonctions, variables, qualifiers
import sys

#import du script mylib ou de la variable précise d'un script
import mylib
#from mylib import title


# fonction de base "hello world!"
print(sys.platform)
print("Hello world!")
print(2 ** 100)

x = 'spam!'
print(x)
print((x+'\n')*8)

x = x + ' test'
print(x)

x += '123456789'
print(x)

print(mylib.title)
print(mylib.a+mylib.b+mylib.c)
#print(title)