# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10

#methode 1

somme = 0
for i in range (len(my_list)):
    somme =somme + my_list[i]

print (somme/len(my_list))



# methode 2

somme = 0
nbre = len (my_list)
for i in my_list:
    somme += i
moyenne = somme / nbre
print (f'{moyenne = }')