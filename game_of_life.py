# on crée une matrice de départ n
# on ajoute les cases
# on regarde la matrice de départ pour créer la matrice suivante n+1 en respectant les règles du jeu de la vie
# etc

import time
import os
    
def add_case(matrice, x, y):
    matrice[x][y] = 1
    return matrice

def create_matrice(n):
    matrice = []
    for i in range(n):
        matrice.append([0]*n)
    return matrice

def print_matrice(matrice):
    for line in matrice:
        print(line)
        
def count_neighbours(matrice, x, y):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x+i >= 0 and x+i < len(matrice) and y+j >= 0 and y+j < len(matrice):
                if matrice[x+i][y+j] == 1:
                    neighbours += 1
    return neighbours

def next_matrice(matrice):
    new_matrice = create_matrice(len(matrice))
    new_matrice_neighbours = create_matrice(len(matrice))
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            neighbours = count_neighbours(matrice, i, j)
            new_matrice_neighbours[i][j] = neighbours
            if matrice[i][j] == 1:
                if neighbours ==3 :
                    new_matrice[i][j] = 1
                else:
                    new_matrice[i][j] = 0
            elif matrice[i][j] == 0:
                if neighbours == 3:
                    new_matrice[i][j] = 1
                else:
                    new_matrice[i][j] = 0
    return new_matrice

def main():
    n = 5
    matrice = create_matrice(n)
    matrice = add_case(matrice, 1, 2)
    matrice = add_case(matrice, 2, 2)
    matrice = add_case(matrice, 3, 2)
    
    nbCycle = 4
    x=0
    while x < nbCycle: 
        print("\n\ngénération n°", x)
        print_matrice(matrice)
        matrice = next_matrice(matrice)
        time.sleep(1)
        x+=1
        
    
main()