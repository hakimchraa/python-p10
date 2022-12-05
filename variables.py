# l'operateur d'affectation = permet d'injecter une valeur 
# dans une variable

my_number1 = 123
my_number2 = -42
my_number6 = 0

print (my_number1)
print (my_number2)
print (my_number6)
print(type(my_number1))
print(type(my_number6))

# float, normbre à virgule flottante

my_number3 = 3.14
my_number4 = -2.71
# 0.0 ou 0. ou .0
my_number5 = 0.0

print (type(my_number3))
print (my_number4)
print (my_number5)
print (type(my_number5))
print (my_number1)
print (my_number2)

my_boolean1 = True
my_boolean2 = False
print(my_boolean1)
print(my_boolean2)
print(type(my_boolean1))


# None, valeur nulle
# null, nil
my_none = None
print(my_none)
print(type(my_none))


# string, chaine de caractere
# double quote ou simple quote c'est pareil
my_text1 = "ceci est une chaine de caracteres"
my_text2 = "ceci est aussi une chaine de caracteres"

print (my_text1)
print (my_text2)
print( type (my_text1))

# \ caratere d'echappement
# \n saut de ligne
my_text3 = "abc\ndef\nghi"
my_text4 = "\\"
my_text5 = "john  \"Foo\"  Doe"
print(my_text3)
print(my_text4)
print(my_text5)
print( type (my_text5))


my_text6 = """abc
def
ghi"""
print(my_text6)
print( type (my_text6))

my_text7 = '''abc
def
ghi'''
print(my_text7)
print( type (my_text7))


foo = "lorem ipsum"
# affectation de valeur à partir d'une variable
bar = foo
print(bar)


a = 123
b = 42
print (a, b)
# permutation de la valeur des variables
a, b = b, a
print (a, b)

#permutation d'une variable sans utiliser 
a = 123
b = 42
# on introduit une 3eme variable c de valeur null
c = a  
# c=123 a=123 b=42
a = b  
# c=123 a =42 b= 42
b = c  
# b=123 c=123 a =42

#variante qui marche qu'avec des nombres

c = a + b
a = c - a 
b = c - b
print(a,b)




