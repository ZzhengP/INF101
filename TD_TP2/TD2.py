# 1.3.1

i = 0
while i <= 10:
  print("i est %i" %i)
  i += 1

print("------------------")
i = 10

while i >= 0:
  print("i est %i" %i)
  i -= 1

i = 0
print("------------------")

while i < 30:
    if i %3 == 0:
        print("%i est un multiple de trois" %i)
    i +=1 ;

print("------------------")
i = 1
while i < 300:
    if i %3 == 0:
        print("%i est un multiple de trois" %i)
    i +=1 ;
    
while True:
    x = int(input('Veuillez entrer une valeur  inférieur ou égale à 0 \n'))
    if ( x <= 0 ):
         break;
    else:
        print("La valeur est strictement supérieur à 0")
    
print("----- test voyelle -----")
voyelle = "aoeuiy"
saisie = True
while(saisie):
    c = input("Entrez un caractere \n")
    saisie = not (c in voyelle)
    
i = 20
j = 0
while i < 100:
    if i%2 != 0:
        j+=1
    i = i + 1
print("total étoile : ", j)



# 1.3.2

i = 1
j = 0
while i <= 16:
    print('*')
    j += 1
    i *= 2
print(j)

# 1.3.4 Dé pipé

import random

x = random.randint(1,6)
quite_loop = False
while not quite_loop:
    print("x, ", x)
    if (x %2 != 0):
        x = random.randint(1,6)
    else:
        quite_loop = True
        
# 1.3.5
# Avec break
voyelle = "aoeuiy"
while True:
    c = input("Entrez un caractere")
    if (c in voyelle):
        break
        
    
Not_Saisie = False
voyelle = "aoeuiy"

while (not Not_Saisie):
    c = input("Entrez un caractere")
    if (c in voyelle):
        Not_Saisie = True

# 1.3.7

somme = 0
count = 0
while True:
    x = int(input("Entrez un entier "))
    somme = somme + x
    count += 1
    c = input("Une nouvelle valeur ? y or n ")
    if (c == 'n'):
        break
print("La somme des %i entiers est : %i" %(count, somme))

#1
n = int(input("Entrez un entier"))
i = 0
somme = 0
while i <= n:
    somme += i
    i += 1
print("somme est %i"  %somme)


#2
n = int(input("Entrez un entier"))
i = 0
somme = 0
while i <= n:
    if (i%2!= 0):
        somme += i
    i += 1
print("somme est %i"  %somme)

#3
n = int(input("Entrez un entier"))
i = 0
somme = 0
while i < n:
    x = int(input("Entrez un entier à ajouter à la somme"))
    somme += x
    i += 1
print(somme)

#4
n = int(input("Entrez un entier"))
i = 0
somme = 0
while i < n:
    x = int(input("Entrez un entier à multipiler à la somme"))
    somme *= x
    i += 1
print(somme)

n = int(input("Entrez un entier"))
i = 0
croissant = True
while i < n:
    print("Entrez un pair d'entier pour %i pair" %(i+1))
    a = int(input("La première valeur est :"))
    b = int(input("La deuxième valeur est :"))

    if(a > b):
        croissant = False
    i += 1
if (croissant):
    print("Tous les pairs sont en ordre croissant")
else:
    print("Tous les pairs ne sont pas en ordre croissant")
    
    
# 1.3.8

Not_Saisie = False
nbr_totale_note = 0
note_max = 0
note_min = 10
somme = 0
while(not Not_Saisie):
    x = float(input("Entrez une note entre 0 et 20, tout autre valeur signifie fin de la saisie"))
    if (0 <= x <= 20):
        nbr_totale_note += 1
        somme += x
        if (x > note_max):
            note_max = x
        if (x < note_min):
            note_min = x
    else:
        print("Vous avez entrer une valeur non correcte.")
        Not_Saisie = True
print("la moyenne est %d la note maximale est %d la note minimale est %d" %(somme/nbr_totale_note ,note_max ,note_min))

# 1.3.14

def Fibonaci(n):
    f_0 = 1
    f_1 = 1
    i = 2
    fib = 0
    while i <= n :
        fib = f_0 + f_1
        temp = f_1
        f_1 = fib
        f_0 = temp
        i += 1
    return fib

nbor = 1.618033988749895
precision = float(input("donnez une précision entre le nombre d'or et valeur calculé par programm"))
is_precis = False
n = 3
while (not is_precis):
    estimated_nbor = Fibonaci(n)/Fibonaci(n-1)
    if(abs(nbor - estimated_nbor) < precision):
        print("Le term %i de Fib divise %i permet obtenir une valeur estimée de Fib avec la précision %f" %(n,n-1,precision))
        is_precis = True
    else:
        n += 1

# 1.3.15

A = int(input("Entrez la valeur initiale de la suite Syracuse: \n"))
n = 1
Un = A
Un_max = A
count_descente = 1
count_descente_max = 2
Un_prev = Un
while (Un != 1):
    if(Un %2 ==0):
        Un = Un/2
    else:
        Un = 3*Un + 1

    if (Un > Un_max):
        Un_max = Un
    
    if(Un < Un_prev):
        count_descente += 1
    else:
        count_descente = 1
    Un_prev = Un

    if(count_descente > count_descente_max):
        count_descente_max = count_descente
        
    print("Un à l'étape %i est égale à %i" %(n,Un))
    n += 1
print("Un = 1 lorsque n est égale à %i et la plus grande valeur atteint par Un est %i " %(n , Un_max))
print("La plus longue descente est égale à ", count_descente_max )






