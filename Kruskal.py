import numpy as np


# Entrer le nombre de sommets

# Tant que toutes les valeurs ne sont pas entrées

# Demander la saisie pour la ligne concernée

Zbase = np.array([[0,5,0], [1,0,2], [0,2,0]])

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
    trie = []
    triearc = []
    i = 0
    for row in range(0,nbRow):
        for col in range(0,nbCol):
            if Z[row,col] != 0 and col not in used: # Si la valeur n'est pas nulle, s'il y a un arc
                if row != col: # Si sommet de départ n'est pas sommet d'arrivé
                    X += ["{}{}".format(row,col)]
                    Y += [Z[row,col]]
                    used += [row]
    val = 0
    triesize = len(Y)
    while ( len(trie) != triesize ):
        i = 0
        valpos = 0
        for values in Y:
            if i == 0:
                val = Y[i]
                valpos = 0
            else:
                if Y[i] < val:
                    val = Y[i]
                    valpos = i
            i += 1
        trie.append(val)
        triearc.append(X[valpos])
        X.pop(valpos)
        Y.pop(valpos)


    X = triearc
    Y = trie
    render = X,Y


    return render



print("Matrice : \n", Z)
print("Taille : ",Z.shape)
print(trie(Z))

# Ex 2 vérifier pas de cycles

#Zcycle = np.array([[0,7,0,5,0,0,0], [7,0,6,9,7,0,0], [0,6,0,0,4,0,0],[5,9,0,0,11,6,0],[0,7,4,11,0,8,9],[0,0,0,6,8,0,10],[0,0,0,0,9,10,0]])
#print(Zcycle)
#print(trie(Zcycle))


# ACM ? Arbre couvrant minimum
# Arbre qui passe par l'ensemble des sommets avec un poids minimum

def ACM():

    return 0


import numpy as np


# Entrer le nombre de sommets

# Tant que toutes les valeurs ne sont pas entrées

# Demander la saisie pour la ligne concernée



#print(Z)

# Algo de Kruskal
# Exo 1 :

# Saisir une matrice et réordonné chaques arc par ordre croissant de poids

# Function (X,Y) = Trie(Z)


#Ex 1 Trie Z



print("Matrice : \n", Z)
print("Taille : ",Z.shape)
print(trie(Z))

X, Y = trie(Z)
print("X = ", X)
print("Y = ", Y)

# Ex 2 vérifier pas de cycles

Zcycle = np.array([[0,1,1], [1,1,1],[1,1,0]])
print(Zcycle)
print(trie(Zcycle))
print("X = ", X)
print("Y = ", Y)


def Kruskal(Z):
    lesSommets = recupSommets(Z)
    nbSommets = len(lesSommets)
    #X, Y = trie(Z)

    poids = 0
    return poids


print(trie(Z)[0][0])

s0, s2 = trie(Z)[0][0]


print(s2)

def listeSommets(Z):
    sommets = []
    for i in range(len(trie(Z)[0])):
        s1, s2 = trie(Z)[0][i]
        if s1 not in sommets:
            sommets += s1
        if s2 not in sommets:
            sommets += s2
    return sommets


print(trie(Zbase))
print(trie(Zbase)[0][0])

s0, s2 = trie(Zbase)[0][0]
print(s2)

print(listeSommets(Z))