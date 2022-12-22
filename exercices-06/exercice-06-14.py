# exo 6.14
# Créez une deuxième liste nommée `new_list` ne contenant que les nombres entiers de la liste

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.14

new_list=[]
for nbre in my_list:
    if isinstance(nbre,int):
        new_list.append(nbre)
    
print (new_list)