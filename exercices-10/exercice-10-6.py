# exo 10.6
# La formule suivante permet de convertir des mètres en miles :
#
#       miles = meters / 1609.344
#
# La formule suivante permet de faire l'inverse :
#
#       meters = miles * 1609.344
#
# Créez une fonction nommée :
#
# - meters_to_miles() permettant de convertir des mètres en miles
# - miles_to_meters() permettant de convertir des miles en mètres
#
# Ensuite convertissez les valeurs :
#
# - 1 Km en miles
# - 10 miles en mètres
#
# Appelez les fonctions et affichez les résultats

# réponse 10.6

def meters_to_miles (a: float):
    a /= 1609.344
    return a

def miles_to_meters (a: float):
    a *= 1609.344
    return a

print ("1km en miles = ", meters_to_miles(1000))
print ("10 miles en metres = ", miles_to_meters(10))


a = float(input("entrer une distande en metres svp : "))
print ("la distance en miles est", meters_to_miles(a))

a = float(input("entrer une distande en miles svp : "))
print ("la distance en miles est", miles_to_meters(a))