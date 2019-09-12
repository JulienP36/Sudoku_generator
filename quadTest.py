import os
import random
import time

'''
Visualisation
{
        ----------------------------------
        | 1  2  3  | 10 11 12 | 19 20 21 |
        | 4  5  6  | 13 14 15 | 22 23 24 |
        | 7  8  9  | 16 17 18 | 25 26 27 |
        |--------------------------------|
        | 28 29 30 | 37 38 39 | 46 47 48 |
        | 31 32 33 | 40 41 42 | 49 50 51 |
        | 34 35 36 | 43 44 45 | 52 53 54 |
        |--------------------------------|
        | 55 56 57 | 64 65 66 | 73 74 75 |
        | 58 59 60 | 67 68 69 | 76 77 78 |
        | 61 62 63 | 70 71 72 | 79 80 81 |
        ----------------------------------
}
'''

def generateGrid():
    #Setup grille 2D
    Grille = [[0] * 9 for z in range(9)]
    total_reset_counter = 0
    i = 0
    
    while i < 3: #Horizontal
        j = 0
        while j < 3: #Vertical
            x = 0
            while x < 3: #Vertical
                y = 0
                while y < 3: #Horizontal
                    compteur = 0
                    
                    #Boucle de tests pour arranger correctement les chiffres
                    while Grille[(i*3)+y][(j*3)+x] == 0 and compteur < 90:
                        alea_test = random.randint(1,9)
                        
                        #Test 3x3
                        for a in range(3):
                            for b in range(3):
                                if Grille[(i*3)+b][(j*3)+a] == alea_test:
                                    alea_test = 0
                                    a = 2
                                    b = 2
                                    compteur += 1
                        
                        #Test horizontal
                        if alea_test != 0:
                            for c in range(9):
                                if Grille[(i*3)+y][c] == alea_test:
                                        alea_test = 0
                                        c = 8
                                        compteur += 1
                        
                        #Test vertical
                        if alea_test != 0:  
                            for d in range(9):
                                if Grille[d][(j*3)+x] == alea_test:
                                        alea_test = 0
                                        d = 8
                                        compteur += 1
                                        
                        #Set du chiffre si pas de problemes avec sa position
                        if alea_test != 0:
                            Grille[(i*3)+y][(j*3)+x] = alea_test
                            compteur = 0
                            
                    #Soft reset de la grille 3x3 actuelle
                    if compteur >= 90:
                        x = -1
                        y = 3
                        for a in range(3):
                            for b in range(3):
                                Grille[(i*3)+b][(j*3)+a] = 0
                        total_reset_counter += 1
                    
                    #hard reset si la generation est bloquee 
                    if total_reset_counter == 60:
                        return 0

                    y += 1
                x += 1
            j += 1
        i += 1

    #boucle d'affichage final de la grille
    for i in range(9):
        ligne = "  "
        
        for j in range(9):
            if j == 2 or j == 5:
                ligne = ligne + str(Grille[i][j]) + " | "
            else:
                ligne = ligne + str(Grille[i][j]) + " "
            
        print(ligne)
        if i == 2 or i == 5:
            print("  ---------------------")

#Boucle principale
def main():
    test = 0
    condition = 0

    print("Nombre de grilles a generer : ")
    nbr_grilles = input()
    timer_start = time.time()

    #Boucle pour generer plus de grilles
    while condition < nbr_grilles:
        test = generateGrid()
        if test != 0:
            condition += 1
            print("")
    timer_end = time.time()
    print(timer_end - timer_start)
    os.system("pause")
        
main()