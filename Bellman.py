import numpy as np

M = np.array([[0, 3, 4, 0, 0, 0],
              [0, 0, 9, 2, 2, 0],
              [0, 0, 0, -5, 0, 0],
              [0, -2, 0, 0, 0, 3],
              [0, 0, 0, 0, 3, 1],
              [0, 0, 0, 0, 0, 0]])


# Étape 1 : Initialiser un tableau de taille indéfini qui récupèrera la trace des étapes de bellman


def initBell(matrice, sommetDepart):
    bellman = {}

    bellman[0] = np.ones(len(matrice)) * np.inf

    j = 0
    bellman[0][sommetDepart] = 0
    bellman[1] = bellman[0].copy()
    for i in matrice[sommetDepart]:
        if i != 0:
            bellman[1][j] = i
        j += 1
    i = 2
    return bellman


def afficherBellman(bellmanTab):
    for i in range(len(bellmanTab)):
        print("Etape", i, ":", bellmanTab[i])


bellman = initBell(M, 0)

afficherBellman(bellman)

def Bellman(matrice, sommetDepart):
    bellman = initBell(matrice, sommetDepart)
    i = len(bellman)
    while i < 10:
        bellman[i] = bellman[i - 1].copy()
        for bellmanColonne in range(len(bellman[0])):

            if bellman[i - 1][bellmanColonne] != np.inf:  # Si la colonne vérifiée est déjà définie
                for matriceCol in range(len(matrice[bellmanColonne])):  # Pour chaque colonne associée au sommet en cours

                    if matrice[bellmanColonne][matriceCol] != 0: # Si la valeur n'est pas nulle, s'il y a un chemin
                        possibleVal = matrice[bellmanColonne][matriceCol] + bellman[i - 1][bellmanColonne] # Nouvelle valeur possible
                        if possibleVal < bellman[i - 1][matriceCol]:
                            bellman[i][matriceCol] = matrice[bellmanColonne][matriceCol] + bellman[i - 1][bellmanColonne]

        if np.array_equal(bellman[i], bellman[i - 1]):  # Si la ligne actuelle est égale à la ligne précédente, fin de l'algo
            break

        i += 1
    return bellman

bellmanFin = Bellman(M, 0)
print("___________________________________")
afficherBellman(bellmanFin)
