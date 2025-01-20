import random

def create_matrice(n):
    return [[0]*n for _ in range(n)]

def fill_random_matrice(matrice):
    n = len(matrice)
    for i in range(n):
        for j in range(n):
            matrice[i][j] = random.randint(0, 1)
    return matrice

def print_matrice(matrice):
    n = len(matrice)
    print("+" + "-"*n*2 + "+")
    for i in range(n):
        print("|", end="")
        for j in range(n):
            print("■" if matrice[i][j] == 1 else " ", end=" ")
        print("|")
    print("+" + "-"*n*2 + "+")

def count_neighbours(matrice, x, y):
    neighbours = 0
    n = len(matrice)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x + i >= 0 and x + i < n and y + j >= 0 and y + j < n:
                neighbours += matrice[x + i][y + j]
    neighbours -= matrice[x][y]  # Remove the cell itself from the count
    return neighbours

def is_matrice_empty(matrice):
    return all(all(cell == 0 for cell in row) for row in matrice)

def next_matrice(matrice):
    n = len(matrice)
    new_matrice = create_matrice(n)
    for i in range(n):
        for j in range(n):
            neighbours = count_neighbours(matrice, i, j)
            if matrice[i][j] == 1:
                if neighbours == 2 or neighbours == 3:
                    new_matrice[i][j] = 1
                else:
                    new_matrice[i][j] = 0
            elif matrice[i][j] == 0:
                if neighbours == 3:
                    new_matrice[i][j] = 1
                else:
                    new_matrice[i][j] = 0
    return new_matrice

def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Lancer la simulation")
        print("2. Paramètres")
        print("3. Quitter")
        
        choix = input("Choisissez une option (1-3) : ").strip()
        
        if choix == "1":
            main()
        elif choix == "2":
            print("\nParamètres :")
            print("Pas de paramètres configurables pour l'instant.")
        elif choix == "3":
            print("\nAu revoir !")
            break
        else:
            print("\nOption invalide. Veuillez réessayer.")

def main():
    # Saisie de la taille de la matrice avec limite à 20
    while True:
        try:
            n = int(input("Quelle taille de matrice souhaitez-vous (taille nxn, max 20) ?\n"))
            if 1 <= n <= 20:
                break
            else:
                print("Veuillez entrer une valeur entre 1 et 20.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    # Saisie du nombre de générations avec limite à 100
    while True:
        try:
            nbCycle = int(input("Combien de générations souhaitez-vous (max 100) ?\n"))
            if 1 <= nbCycle <= 100:
                break
            else:
                print("Veuillez entrer une valeur entre 1 et 100.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    # Création et remplissage aléatoire de la matrice
    matrice = create_matrice(n)
    matrice = fill_random_matrice(matrice)
    
    for x in range(nbCycle):
        print(f"\n\nGénération n° {x + 1}")
        print_matrice(matrice)
        if is_matrice_empty(matrice):
            print("\nLa matrice est vide, la simulation s'arrête.")
            break
        
        matrice = next_matrice(matrice)
        
        # Demander à l'utilisateur d'appuyer sur Entrée pour passer à la génération suivante
        input("\nAppuyez sur Entrée pour passer à la génération suivante.")

menu()
