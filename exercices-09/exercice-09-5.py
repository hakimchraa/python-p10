# exo 9.5
# Supprimez du dictionnaire la clé `foo`
# Puis affichez le résultat avec un simple `print()`

my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.5
print(my_dict) # affichage du dictionnaire avant la suppression
my_dict.pop('foo')
print (my_dict) # affichage apres la suppression