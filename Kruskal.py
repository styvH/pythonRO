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


#Ex 1 Trie Z
def trie(Z):
#Obtenir vecteur format 2 sorties : X = les chemins, Y = la taille
    nbRow, nbCol = Z.shape #Récupérer la taille de la matrice, soit le nombre de sommets
    print(nbRow)
    print(nbCol)
    X = []
    Y = []
    used = []
    for row in range(0,nbRow):
        for col in range(0,nbCol):
            if Z[row,col] != 0 and row not in used:
                print("Ligne : ",row)
                print("Colonne : ", col)
                X += ["{}{}".format(row,col)]
                Y += [Z[row,col]]
                used+= [row]
                used+=[col]
    render = "X = ", X,"Y = ",Y

    return render



print("Matrice : ", Z)
print("Taille : ",Z.shape)
print(trie(Z))
nbRow, nbCol = Z.shape
print(nbRow)
print(nbCol)

# Ex 2 vérifier pas de cycles