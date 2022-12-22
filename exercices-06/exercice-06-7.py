# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7

a = my_list.index('bar')
print (a)

b = my_list.index ('lorem')
print (b)

my_list[b]='bar'
my_list[a]='lorem'

print(my_list)