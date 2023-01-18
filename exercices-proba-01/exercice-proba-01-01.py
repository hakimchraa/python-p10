# exo 1.1
# Alice et Bob veulent jouer à pile ou face.
# - si la variable "head_or_tail" vaut 0, cela équivaut à pile
# - si elle vaut 1, cela équivaut à face
# Alice parie pile et Bob parie face.
# Qui gagne ? Alice ou Bob ?
# Rédigez le code qui indique le nom du gagnant.
import random
head_or_tail = random.randint(0, 1)

# réponse 1.1

alice = 0   #alice a parié sur pile(0)
bob = 1     #bob a parié sur face (1)

print (head_or_tail)

if head_or_tail == alice :
    print ("alice a gagné")
else :
    print ("bob a gagné")