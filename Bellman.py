import numpy as np

M = np.array([[0, 3, 4, 0, 0, 0],
              [0, 0, 9, 2, 2, 0],
              [0, 0, 0, -5, 0, 0],
              [0, -2, 0, 0, 0, 3],
              [0, 0, 0, 0, 3, 1],
              [0, 0, 0, 0, 0, 0]])

M = np.array([[0, 3, 4, 0, 0, 0],
              [0,0,9,2,2,0],
              [0,0,0,-5,0,0],
              [0,-2,0,0,0,3],
              [0,0,0,0,3,1],
              [0,0,0,0,0,0]])

# Étape 1 : Initialiser un tableau de taille indéfini qui récupèrera la trace des étapes de bellman


def initBell(matrice):
    bellman = {}
    bellman[0] = np.ones(len(matrice)) * np.inf
    print(matrice)
    depart = int(input("Choisissez le point de départ pour le graphe :"))
    if depart not in range(len(bellman[0])):
        print("Vérifiez la valeur (Entrez un chiffre entre 0 et {})".format(len(bellman[0])))
        initBell(matrice)
    else:
        bellman[0][depart] = depart

    return bellman

def afficherBellman(bellmanTab):
    for key in bellmanTab.keys():
        print("Etape", key, ":", bellmanTab[key])


bellman = initBell(M)
afficherBellman(bellman)

def Bellman(matrice):
    bellman = initBell(matrice)
    i = len(bellman)
    while i < 100:  # Boucle Normalement infini, maximisé à 100 pour l'exercice
        bellman[i] = bellman[i - 1].copy()
        for bellmanColonne in range(len(bellman[0])):
            if bellman[i - 1][bellmanColonne] != np.inf:  # Si la colonne vérifiée est déjà définie
                for matriceCol in range(len(matrice[bellmanColonne])):  # Pour chaque colonne associée au sommet en cours
                    if matrice[bellmanColonne][matriceCol] != 0: # Si la valeur n'est pas nulle, s'il y a un chemin
                        possibleVal = matrice[bellmanColonne][matriceCol] + bellman[i - 1][bellmanColonne] # Nouvelle valeur possible
                        if possibleVal < bellman[i - 1][matriceCol]:
                            bellman[i][matriceCol] = possibleVal

        if np.array_equal(bellman[i], bellman[i - 1]):  # Si la ligne actuelle est égale à la ligne précédente, fin de l'algo
            break

        i += 1
    return bellman

bellmanFin = Bellman(M)
print("___________________________________")
afficherBellman(bellmanFin)


J = np.array([
    [0,6,7,0,0],
    [0,0,8,5,-4],
    [0,0,0,3,9],
    [0,-2,0,0,0],
    [-2,0,0,7,0]
])

bellmanJ = Bellman(J)
print("___________________________________")
afficherBellman(bellmanJ)
