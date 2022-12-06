# exercice-02-variables.py

# exo 2.1
# Affectez :
# - le nombre 42 à une variable
# - le nombre d'or 1,61 à une variable
# - votre nom et prénom à une variable
# - la valeur booléenne vrai si nous sommes le matin, sinon la valeur booléenne faux, à une variable
# - la valeur nulle `None` à une variable
# Affichez ces variables

# réponse 2.1
a = 42
b = 1.61
nom = "chraa"
prenom = "hakim"
booleen1 = True
booleen2 = False
valeurnul = None

print(a)
print(b)
print(nom)
print(prenom)
print(booleen1)
print(booleen2)
print(valeurnul)

# code 2.1
# la fonction `round()` permet d'arrondir un float en un integer
# 0,1 est arrondi à la valeur inférieur
print(round(0.1))
# 0,9 est arrondi à la valeur supérieur
print(round(0.9))
# la fonction `round()` permet aussi d'arrondir en précisant le nombre de chiffres après la virgule
# arrondir à un nombre décimal à 4 chiffres après la virgule
print(round(1 / 3, 4))

# exo 2.2
# Stockez les valeurs suivantes dans une variable et transtypez-les :
# - integer 2 en un float
# - float 1,62 en un integer
# - float 1,62 en un float arrondi à zéro chiffre après la virgule, puis en un integer
# - float 1,62 en un float arrondi à un chiffre après la virgule
# À chaque fois stockez le résultat dans une variable et affichez le résultat.

# réponse 2.2
x = 2
print (type(x))
x = float(x)
print (type (x))

y = 1.62
print (type(y))
y = int (y)
print (type(y))

z = 1.62
z = round (z,0)
print (z)
print (type(z))
z = int (z)
print(z)
print (type(z))

w = 1.62
print (type(w))
w = round (w,1)
print(w)
