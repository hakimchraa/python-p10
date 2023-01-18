# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit'] 

# réponse 6.15

i=0 
str_max=""
# print(my_list[i]);

for item1  in my_list :
    # print (item1)
    for item2 in my_list :
        # print (len(item1));
        if (len(item1) > len(item2)) :
            str_max=item1 
        else:
            if (len(item1) == len(item2)):
                str_max=item1 
            else :
                str_max=item2


#    i += 1 ;
#     print(i);
#     if item1 > item2:
#         str_max=item1 ;
#     else : 
#         str_max=item2 ;

print (str_max);
