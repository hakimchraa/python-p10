# exo 3.9
# Charly fait ses courses.
# Il compare le prix de deux marques différentes de chocolat.
# La marque Alpha propose une tablette à 2,00 euros (pour 120 g).
# La marque Beta propose une tablette à 1,70 euros (pour 100 g).
# Charly a l'intuition que la marque Alpha est plus avantageuse.
# A-t-il raison ?
# Calculez d'abord le poid au kilo (convertir les grammes en kilo donc) et stockez les résultats dans les variables `weight_alpha` et `weight_beta`.
# Puis calculez le prix au kilo avec les variables `price_alpha` et `weight_alpha`, et `price_beta` et `weight_beta` respectivement puis stockez les résultat dans les variables `price_per_kilo_alpha` et `price_per_kilo_beta`.
# Utilisez un opérateur de comparaison (qui doit donc renvoyer une valeur booléenne) pour vérifier si Charly a raison.
# Affichez le résultat booléen.

price_alpha = 2.00
price_beta = 1.70

# réponse 3.9

price_kilo_1 = (1.79 / 120) * 1000
price_kilo_2 = (1.7 / 100) * 1000
print ("le prix au kilo de la 1er marque est :",price_kilo_1 )
print ("le prix au kilo de la 2eme marque est :",price_kilo_2 )
if price_kilo_1 < price_kilo_2 : print ("la 1er marque est moins cher, Charly a raison") 
elif price_kilo_1 == price_kilo_2 : print ("les 2 marques sont au meme prix, Charly a tort")
else : print ("la 2eme marque est moins cher, Charly a tort")
print (price_kilo_1 < price_kilo_2)