# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur de type `int`
# - renvoie 1 si `a` est plus grand que `b`
# - renvoie -1 si `a` est plus petit que `b`
# - renvoie 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5

def compare (a: float,b: float) :
    if a > b :
        return int(1)
    elif a < b :
        return int (-1)
    else : 
        return int(0)

a = float(input("entrer le nombre a ? "))
b = float(input("entrer le nombre b ? "))

print (compare(a,b))

print ("1 pour vrai, -1 pour faux, 0 pour egal")
print ("80 > 80 = ",(compare(80,80)))
print ("56.4 > 57 = ",(compare(56.4,57)))
print ("102.85 > 102.84 = ",(compare(102.85,102.84)))
