# exo 10.4
# Créer une fonction nommée `is_greater()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur booléenne
# - renvoie True si `a` est plus grand que `b`
# - renvoie False dans les autres cas
# Appelez la fonction et affichez le résultat

# réponse 10.4

def is_greater (a: float, b: float) :
    return (a > b)
   

a = float (input("entrer la valeur de a ? "))
b = float (input("entrer la valeur de b ? "))
print(type(a))
print (a,"est il plus grand que",b," la reponse est ", is_greater (a, b))


print ("20 > 50 = " , is_greater(20,50))
print ("10.2 > 9.8 = " , is_greater(10.2,9.8))
print ("7.9998 > 7.9992 = " , is_greater(7.9998,7.9992))
print ("482 > 482 = " , is_greater(482,482))