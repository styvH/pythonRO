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

i = len(bellman)
while i < 10:  # Tant que l'on a pas arrêté la boucle (while True)
    bellman[i] = bellman[i-1].copy()
    valPos = 0
    for val in bellman[i-1]:
        if val != 0 and val < bellman[i-1][valPos]:
            bellman[i][valPos] = val
        valPos += 1
    i += 1
afficherBellman(bellman)

