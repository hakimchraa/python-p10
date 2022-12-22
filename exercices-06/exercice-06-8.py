# exo 6.8
# Calculez la somme des nombres de la liste et affichez le résultat

my_list = [2.71, 42]

# réponse 6.8

# methode 1
i = len(my_list)
somme = 0

while i != 0:
    i = i - 1
    somme = somme + my_list[i]
  
print (f'{somme = }')

#methode 2
somme = 0

for i in range (len(my_list)):
    somme = somme + my_list[i]

print (f'{somme = }')

# methode 3
somme = 0
for j in my_list:
    somme += j

print (f'{somme = }')
