#Groupe :
#Barnabot Edwin
#Lorterville Styvan
#Duhamel Jorane
# Musu Mattéo
import numpy as np
import math
# Matrice Exemple 1 du cours
Z = np.array([[0, 3, 4, 0, 0, 0], [0,0,9,2,2,0],[0,0,0,-5,0,0],[0,-2,0,0,0,3],[0,0,0,0,3,1],[0,0,0,0,0,0]])
sommetStart = [0,0]

def belmanFord(Z):
    Z2 = Z.copy()
    step = 0
    poidsFinal = 0
    i = 0

    # initialisation du tableau
    Z2.fill(100)
    #Z2.fill(math.inf)
    for i in range(0, len(Z2)):
        #le poids des
        Z2[i][0] = 0
        i+=1
    # fin initialisation du tableau


    print("Etape : ", step)
    print(Z2,"\n")
    step+=1
    if (step>0):
        #print(Z)
        #print(Z2)
        for vals in Z2 :
            # vérification si le sommet actual a des voisins dans la matrice d'incidence
            #lecture de la ligne précédente
            for index, sommet in enumerate(Z[step-1]):
                print(index)
                # Si le sommet lu dans la matrice != 0
                if sommet != 0 :
                    #ajout des valeurs des voisins du sommet S
                    if (step == 1):
                        Z2[step][index] = sommet

                    #À partir de l'étape 2
                    elif (step > 1):
                        #Si la valeur lu
                        if (sommet < Z2[step-1][index]):
                            Z2[step][index] = sommet
                        else:
                            Z2[step][index] = Z2[step-1][index]

                #cas ou le sommet actif n'est pas voisin
                elif sommet == 0:
                    # À partir de l'étape 2
                    if (step == 1):
                        Z2[step][index] = sommet
                        print(index)
                    elif (step > 1):
                        print(index)
                        Z2[step][index] = Z2[step-1][index]

            print("Étape : "+str(step)+"\n"+str(Z2)+"\n")
            step+=1

    render = poidsFinal
    return render

print ("Matrice d'incidence : \n",Z)

print ('\n')
print(belmanFord(Z))

