import random


if True:
    print("la condition est vrai")
    print("ce code est executé")

if False:
    print ("le condition est fausse")
    print ("ce code est pas excécuté")



condition_vente = True

if condition_vente == True:
    print("l'utilisateur a acppeté les conditions de vente")
else:
    print("l'utilisateur n'a pas accepté les conditions de vente")

if  not condition_vente:
    print("l'utilisateur n'a pas accepté les conditions de vente")
else:
    print  ("l'utilisateur a accpeté les conditions de vente")

emails = random.randint (0, 3)
print(emails)

# elif c'est la meme chose else if

if emails==1 :
    print("Vous avez un nouveau mail")
elif emails>1:
    print (f"vous avez {emails} nouveaux mails")
else:
    print("vous n'avez pas de nouveaux mails")


windows_closed  =   bool(random.randint(0,1))
electricity_off =   bool(random.randint(0,1))

print(f'{windows_closed = }')
print(f'{electricity_off = }')

if windows_closed and electricity_off:
    print ("les fenetres sont fermées")
    print ("l'electrecité est coupée")
elif not windows_closed and electricity_off:
    print ("les fenetres ne sont pas fermées")
    print ("l'electrecité est coupée")
elif windows_closed and not electricity_off:
    print ("les fenetres sont fermées")
    print ("l'electrecité n'est pas coupée")
else:
    print ("les fenetres ne sont pas fermées")
    print ("l'electrecité n'est pas coupée")


bank_card=True
cash=True
if bank_card or cash:
    print("On a un moyen de paiement")
else: 
    print("On a aucun moyen de paiement")


ticket = bool(random.randint(0,1))
vip = bool(random.randint(0,1))
Registration = bool(random.randint(0,1))
print(f'{ticket = }')
print(f'{vip = }')
print(f'{Registration = }')


if Registration and (ticket or vip):
    print("accés autorisé")
else:
    print ("accés denied")


product_count = random.randint(0,50)

if product_count > 20:
    print ("il y a plus de 20 articles")
    print ("ras")
    
elif 5 < product_count <= 20:
    print("il y a plus de 5 articles")
    print("alerte approvisionement")

elif 0 < product_count <= 5:
    print("il y a plus 0 article")
    print("alerte rupture immente")
else:
    print ("il n'y a plus d'article")
    print ("Alerte rupture")
