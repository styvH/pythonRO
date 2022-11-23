import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

M = np.array([[0, 6, 3, 0, 0],
              [0, 0, 0, 8, 1],
              [0, 2, 0, 0, 0],
              [0, 1, 0, 0, -5],
              [0, 0, 2, 0, 0]])

N = np.array([[0, 3, 4, 0, 0, 0],
              [0,0,9,2,2,0],
              [0,0,0,-5,0,0],
              [0,-2,0,0,0,3],
              [0,0,0,0,3,1],
              [0,0,0,0,0,0]])
Matrix=[]
Matrix.append(M)
Matrix.append(N)
#plt.imshow(M)
#plt.colorbar()
#plt.show()

A = np.array([[1, 1], [2, 1]])
G = nx.from_numpy_matrix(A)
nx.draw(G)
#G = nx.from_numpy_array(M)

#nx.draw(M, parallel_edges=False)

# Étape 1 : Initialiser un tableau de taille indéfini qui récupèrera la trace des étapes de bellman


def initBell(matrice, sommetDepart):
    bellman = {}
    bellman[0] = np.ones(len(matrice)) * np.inf
    bellman[0][sommetDepart] = 0

    return bellman

def afficherBellman(bellmanTab):
    for key in bellmanTab.keys():
        print("Etape", key, ":", bellmanTab[key])



bellman = initBell(M, 0)
#afficherBellman(bellman)

def Bellman(matrice, sommetDepart):
    poidsMin = 0
    cheminCritique = []
    bellman = initBell(matrice, sommetDepart)
    i = len(bellman)
    while i < 100:  # Boucle Normalement infini, maximisé à 100 pour l'exercice
        bellman[i] = bellman[i - 1].copy()
        for bellmanColonne in range(len(bellman[0])):
            if bellman[i - 1][bellmanColonne] != np.inf:  # Si la colonne vérifiée est déjà définie
                for matriceCol in range(len(matrice[bellmanColonne])):  # Pour chaque colonne associée au sommet en cours
                    if matrice[bellmanColonne][matriceCol] != 0: # Si la valeur n'est pas nulle, s'il y a un chemin
                        possibleVal = matrice[bellmanColonne][matriceCol] + bellman[i - 1][bellmanColonne] # Nouvelle valeur possible
                        #print(bellman[i][bellmanColonne])
                        if possibleVal < bellman[i - 1][matriceCol]:
                            bellman[i][matriceCol] = possibleVal
                            #print(bellman[i - 1][bellmanColonne])
        if np.array_equal(bellman[i], bellman[i - 1]):  # Si la ligne actuelle est égale à la ligne précédente, fin de l'algo
            break

        i += 1
    print(M)
    return bellman


print("liste des matrices...")
for index, matrices in enumerate(Matrix) :
    print("Matrice numéro : "+str(index)+"\n"+str(matrices))
matriceSelect=int(input("Saisissez le numéro de la matrice à traiter : "))

sommetDepart = int(input("Saisissez le sommet de départ  (0,1,2,3,..): "))
bellmanFin = Bellman(Matrix[matriceSelect], sommetDepart)
print("___________________________________")
afficherBellman(bellmanFin)



