import numpy as np

# Entrer le nombre de sommets

# Tant que toutes les valeurs ne sont pas entrées

# Demander la saisie pour la ligne concernée

Zbase = np.array([[0, 5, 0], [1, 0, 2], [0, 2, 0]])

Z = np.array([[0, 7, 0, 5, 0, 0, 0], [7, 0, 6, 9, 7, 0, 0], [0, 6, 0, 0, 4, 0, 0], [5, 9, 0, 0, 11, 6, 0],
              [0, 7, 4, 11, 0, 8, 9], [0, 0, 0, 6, 8, 0, 10], [0, 0, 0, 0, 9, 10, 0]])


# print(Z)

# Algo de Kruskal
# Exo 1 : 

# Saisir une matrice et réordonné chaque arc par ordre croissant de poids

# Function (X,Y) = Trie(Z)


# Ex 1 Trie Z
def trie(Z):  # Obtenir vecteur format 2 sorties : X = les chemins, Y = la taille
    nbRow, nbCol = Z.shape  # Récupérer la taille de la matrice, soit le nombre de sommets
    X = []
    Y = []
    used = []
    trie = []
    triearc = []
    i = 0
    for row in range(0, nbRow):  # pour chaque ligne
        for col in range(0, nbCol):  # pour chaque colonne
            if Z[row, col] != 0 and col not in used:  # Si la valeur n'est pas nulle, s'il y a un arc déjà existant
                # (pour éviter les doublons)
                if row != col:  # Si le sommet de départ n'est pas sommet d'arrivé
                    X += ["{}{}".format(row, col)]  # Ajout de l'arc dans un tableau
                    Y += [Z[row, col]]  # ajout de la taille correspondant à l'arc dans un deuxieme tableau
                    used += [row]  # sauvegarder l'arc utilisé pour "éviter les doublons
    # Démarrage du tri
    val = 0
    triesize = len(Y)
    while (len(trie) != triesize):
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
    render = X, Y

    return render



# Ex 2 vérifier pas de cycles

def ExistChemin(MatriceAdjacente, posA, posB):  # s'il existe un chemin allant de A vers B, retourne vrai sinon faux
    # Pour chaque sommet adjacent à 'A',
    sAdj = []  # sAdj = liste des sommets adjacents pouvant créer un chemin
    n = 0
    for i in MatriceAdjacente[posA]:

        if i != 0:  # Vérifier s'il existe nombre = 1 dans la ligne de 'A'

            # Soit vérifier s'il existe un nombre = 1 dans la ligne de chaque ligne associé
            sAdj.append(n)  # Récupérer les lignes associées (adjacentes) dans une liste

        n += 1

    # Pour chaque sommet adjacent à chaque sommet adjacent à 'a'
    nbSommets = len(MatriceAdjacente[0])  # Nombre de Sommets
    nbParcours = 1  # Nombre de sommets parcourus
    while nbParcours < nbSommets:  # Tant que l'on n'a pas exécuté la boucle plus de fois que le nombre de sommets

        for i in sAdj:
            n = 0
            for j in MatriceAdjacente[i]:
                if n not in sAdj:
                    if j != 0:  # Vérifier s'il existe nombre = 1 dans la ligne de 'A'
                        sAdj.append(n)  # Récupérer les lignes associées (adjacents) dans une liste

                n += 1
        nbParcours += 1

    # Vérifier si adjacent à 'B' (si = posB)

    for adjacent in sAdj:
        if adjacent == posB:
            return True

    return False


def detectCycle(matrice):
    for i in range(len(matrice)): #Pour chaque valeur sommet, vérifier s'il existe un cycle
        if ExistChemin(matrice, i, i):  # S'il existe un chemin allant de i vers i, il s'agit d'un cycle
            return True
    return False


# ACM : Arbre couvrant minimum
# Arbre qui passe par l'ensemble des sommets à partir des poids minimum

def ACPM(Z):
    arcs = []
    M = np.zeros(Z.shape)  # Création matrice M nulle qui sera la matrice d'adjacente du graphe
    # Démarrer boucle
    for i in range(len(trie(Z)[0])):  # Dans l'ordre du tri
        x = trie(Z)[0][i]  # arc
        y = trie(Z)[1][i]  # taille

        s1, s2 = trie(Z)[0][i]
        # Ajouter à la matrice d'adjacente

        M[int(s1)][int(s2)] = 1  # Modification - modifier 1 à la position correspondante
        M[int(s2)][int(s1)] = 1  # Modification
        print(M)
        # Verifier cycle \\ Erreur detection de cycle toujours positive
        if not detectCycle(M):  # S'il n'y a pas de cycle, on ajoute et on continue
            arcs += [[x,y]]

        else:   # S'il la chaine ajoutée crée un cycle, le retirer de la matrice d'adjacente sans l'ajouter aux arcs
            M[int(s1)][int(s2)] = 0
            M[int(s2)][int(s1)] = 0


    return arcs


testCycle = np.array([[0, 3, 0, 0, 1], [3, 0, 5, 0, 4], [0, 5, 0, 2, 6], [0, 0, 2, 0, 7], [1, 4, 6, 7, 0]])


testCycle = np.array([[0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 3, 1, 0]])

print(trie(Z))
print(ACPM(Z))

print(trie(testCycle))
print(ACPM(testCycle))
