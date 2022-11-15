import numpy as np


# Entrer le nombre de sommets

# Tant que toutes les valeurs ne sont pas entrées

# Demander la saisie pour la ligne concernée


Z = np.array([[0,1,0], [1,0,2], [0,2,0]])



#print(Z)

# Algo de Kruskal
# Exo 1 : 

# Saisir une matrice et réordonné chaques arc par ordre croissant de poids

# Function (X,Y) = Trie(Z)

# Z est la matrice d'incidence concernée

"""""
nbSommet = int(input ('Saisir le nombre de sommet :\n'))

nbVal = nbSommet*nbSommet
triPoids = []
Y = [] #poids
X = [] #arcs
i=0
ligne=1
print('Saisir votre matrice :\n')
for x in range(0,nbVal):
    print("x = "+str(x))
    print("i = "+str(i))
    if (i==nbSommet):
        ligne+=1
        i=0
    print("Ligne : "+str(ligne)+"\nSommet: "+str(i+1))
    sommetSaisi = int(input('Saisir votre sommet\n'))
    if (sommetSaisi>0):
        triPoids.append(sommetSaisi)
        X.append(i)
    else:
        triPoids.append("L'arc n'existe pas")
        X.append("L'arc n'existe pas")
    i+=1
print(triPoids)

nbSommet = int(input ('Saisir le nombre de sommet :\n'))
i = 0
while (0 < nbSommet**2):
    
    a = int(input("Saisir valeur sommet"))
    i+=1
"""""
#Ex 1 Trie Z
def trie(Z):
#Obtenir vecteur format 2 sorties : X = les chemins, Y = la taille
    nbRow, nbCol = Z.shape #Récupérer la taille de la matrice, soit le nombre de sommets
    print(nbRow)
    print(nbCol)
    X = []
    Y = []
    for row in range(0,nbRow):
        for col in range(0,nbCol):
            if Z[row,col] != 0:
                print("Ligne : ",row)
                print("Colonne : ", col)
                X += ["{}{}".format(row,col)]
                Y += [Z[row,col]]
    render = "X = ", X,"Y = ",Y

    return render



print("Matrice : ", Z)
print("Taille : ",Z.shape)
print(trie(Z))
nbRow, nbCol = Z.shape
print(nbRow)
print(nbCol)

# Ex 2 vérifier pas de cycles