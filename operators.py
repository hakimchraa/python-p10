import random
import math

# =  affectation
foo = 123

# + addition
foo = 123 + 42
print (foo)
foo = foo + 42
print (foo)

# += operateur d'incrementation
foo += 42
print (foo)

# operateur de décrémentation
foo = 123 - 42 
foo -= 42
print (foo)


# - soustraction
# / division
# // division entiere
foo = 123 // 42
foo //= 42
print(foo)
print(type(foo))

# % modulo
foo = 4 % 3
foo = random.randint(1, 100)
print(foo)
print(foo % 2)

# foo = ...
print(foo)


# * multiplication

# ** puissance
foo = 2 ** 2 
foo = 2 ** 3 
foo = 2 ** 4 
foo = 2 ** 5 
foo = 2 ** 6
print(foo)



# ^ puissance mais pas en python
# math.sqrt() racine carré

foo = math.sqrt(4)

# ** 0.5 racine carré 
foo = 4 ** 0.5
# 0.5 == 1/2
foo = 4 ** (1/2)

#racine cubique
foo = 8 ** (1/3)
print(foo)

my_number = 0
if not (bool(my_number)): print ("le nombre est 0")
else: print ("c'est pas un 0")

print ("---------------------------------------------------")
fruits = [0]
result = 'ananas' in fruits
print(result)

result = bool(fruits)
print (result)

if fruits:
    print ("la liste contient des elements")
else: print ("y a pas de fruit")


liste = ["ananas","pomme"]

print ('ananas' in liste)

