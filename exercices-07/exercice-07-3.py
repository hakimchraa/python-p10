# exo 7.3
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est égal à 1

import random

# réponse 7.3


compteur = 0

for _ in range(100) :
    r = random.randint(1,10)
    if r == 1 :
        print (r)
        compteur += 1

print ("le chiffre 1 est sorti est sorti",compteur,"fois")


