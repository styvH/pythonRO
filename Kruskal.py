import numpy as np


# Entrer le nombre de sommets

# Tant que toutes les valeurs ne sont pas entrées

# Demander la saisie pour la ligne concernée


Z = np.array([[0,1,0], [1,0,2], [0,0,0]])



print(Z)

# Algo de Kruskal
# Exo 1 : 

# Saisir une matrice et réordonné chaques arc par ordre croissant de poids

# Function (X,Y) = Trie(Z)

# Z est la matrice d'incidence concernée

nbSommet = int(input ('Saisir le nombre de sommet :\n'))

nbVal = nbSommet*nbSommet
triPoids = []
poids = []

print('Saisir votre matrice :\n')
i=0
while (i<nbVal):
    i+=1
    for y in range (0,nbSommet-1):
        x = int(input('Saisir votre sommet\n'))
        if (x>0):
            triPoids.append(x)
            print (triPoids)
            