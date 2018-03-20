#exemples pour un import d'un script vers un autre
#quand l'import se fait dans la console le script s'exécute une fois
#des import suivant depuis la même source peut produire des erreurs si modification entretemps
#le script ne se relance pas avec les imports suivants


title = 'MontyPython'
a = 'Holy'
b = 'Graal'
c = 'Arthur'

print(a,b,c)

#note: une chaîne est immuable il faut créer une nouvelle chaîne en utilisant des éléments de la chaîne précédente
# fonction join permet de concaténer une liste en chaîne de caractères