# exo 3.2
# Bob veut distribuer tous ses bonbons et chocolats à ses amis.
# Il a 15 bonbons, 17 chocolats et 3 amis.
# Combien de bonbons lui restera-t-il ?
# Calculez le reste de bonbons puis stockez le résultat dans la variable `candies_rest`.
# Combien de chocolats lui restera-t-il ?
# Calculez le reste de chocolats puis stockez le résultat dans la variable `chocolates_rest`.
# Affichez ces résultats.

candies = 15
chocolates = 17
friends = 3

# réponse 3.2

candies_rest = candies % friends
chocolates_rest = chocolates % friends
print ("vous avez partagé avec vos", friends,"amis",candies,"bonbons et",chocolates,"chocolats")
print("il vous reste ",candies_rest, " bonbons et", chocolates_rest,"chocolats")