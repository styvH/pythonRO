import numpy as np


# Entrer le nombre de sommets

# Tant que toutes les valeurs ne sont pas entrées

# Demander la saisie pour la ligne concernée


Z = np.array([[0,7,0,5,0,0,0], [7,0,6,9,7,0,0], [0,6,0,0,4,0,0],[5,9,0,0,11,6,0],[0,7,4,11,0,8,9],[0,0,0,6,8,0,10],[0,0,0,0,9,10,0]])



#print(Z)

# Algo de Kruskal
# Exo 1 : 

# Saisir une matrice et réordonné chaques arc par ordre croissant de poids

# Function (X,Y) = Trie(Z)


#Ex 1 Trie Z
def trie(Z):#Obtenir vecteur format 2 sorties : X = les chemins, Y = la taille

    nbRow, nbCol = Z.shape #Récupérer la taille de la matrice, soit le nombre de sommets
    X = []
    Y = []
    used = []
    for row in range(0,nbRow):
        for col in range(0,nbCol):
            if Z[row,col] != 0 and col not in used: # Si la valeur n'est pas nulle, s'il y a un arc
                if row != col: # Si sommet de départ n'est pas sommet d'arrivé
                    X += ["{}{}".format(row,col)]
                    Y += [Z[row,col]]
                    used += [row]
    render = "X = ", X,"Y = ",Y

    return render



print("Matrice : \n", Z)
print("Taille : ",Z.shape)
print(trie(Z))

# Ex 2 vérifier pas de cycles

Zcycle = np.array([[0,7,0,5,0,0,0], [7,0,6,9,7,0,0], [0,6,0,0,4,0,0],[5,9,0,0,11,6,0],[0,7,4,11,0,8,9],[0,0,0,6,8,0,10],[0,0,0,0,9,10,0]])
print(Zcycle)
print(trie(Zcycle))
def ACPM():
    return 0