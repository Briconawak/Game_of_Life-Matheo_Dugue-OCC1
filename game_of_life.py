# Description: Jeu de la vie de Conway

import time
import random

def add_case(matrice, x, y):
    matrice[x][y] = 1
    return matrice

def create_matrice(n):
    matrice = []
    for i in range(n):
        matrice.append([0]*n)
    return matrice

def fill_random_matrice(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            matrice[i][j] = random.randint(0, 1)
    return matrice

def print_matrice(matrice):
    print("+" + "-"*len(matrice)*2 + "+")
    for i in range(len(matrice)):
        print("|", end="")
        for j in range(len(matrice)):
            if matrice[i][j] == 1:
                print("■", end=" ")
            else:
                print(" ", end=" ")
        print("|")
    print("+" + "-"*len(matrice)*2 + "+")
        
        
def count_neighbours(matrice, x, y):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x+i >= 0 and x+i < len(matrice) and y+j >= 0 and y+j < len(matrice):
                if matrice[x+i][y+j] == 1:
                    neighbours += 1
    return neighbours

def count_number_of_ones(matrice):
    count = 0
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == 1:
                count += 1
    return count

def is_matrice_empty(matrice):
    if count_number_of_ones(matrice) == 0 :
        return True
    else:
        return False

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
    test=False
    while test == False:
        try:
            n = int(input("Quelle taille de matrice souhaitez-vous (taille nxn) ? \n"))
            if n > 0:
                test = True
            else:
                print("Veuillez entrer un nombre positif")
        except ValueError:
            print("Veuillez entrer un nombre positif")
            test=False
            
    test = False
    while test == False:
        try:
            nbCycle = int(input("Combien de génération souhaitez-vous ? \n"))
            if nbCycle > 0:
                test = True
            else:
                print("Veuillez entrer un nombre positif")
        except ValueError:
            print("Veuillez entrer un nombre positif")
            test=False

    matrice = create_matrice(n)
    matrice = fill_random_matrice(matrice)
    
    x=0
    
    while x < nbCycle: 
        
        print("\n\ngénération n°", x)
        print_matrice(matrice)
        matrice = next_matrice(matrice)
        time.sleep(1)
        x+=1
        if is_matrice_empty(matrice):
            print("\n\ngénération n°", x)
            print_matrice(matrice)
            matrice = next_matrice(matrice)
            print("\nLa matrice est vide, la génération s'arrête")
            x=nbCycle
        
        
    
main()