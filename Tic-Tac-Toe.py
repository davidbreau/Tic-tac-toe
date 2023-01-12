import random
random_int = random.randint(0,1)
grille = { "A1" : "  ", "A2" : "  ", "A3" : "  ",
    "B1" : "  ", "B2" : "  ", "B3" : "  ",
    "C1" : "  ", "C2" : "  ", "C3" : "  "
}

def tictactoe():
    """_summary_
    Génére le message de lancement du jeu
    """
    print("### TIC TAC TOE ###")
    premier_joueur_aleatoire()
    
def afficher_la_grille():
    """_summary_
    Affiche la grille avec contour fixe
    Affiche le contenu des cases stockées dans la grille:dict
    """
    print(
        "  ---- ---- ----", "\n", 
        "|", grille["A1"],"|",grille["B1"],"|",grille["C1"],"|", "1", "\n",
        " ---- ---- ----", "\n",
        "|", grille["A2"],"|",grille["B2"],"|",grille["C2"],"|", "2", "\n",
        " ---- ---- ----", "\n",
        "|", grille["A3"],"|",grille["B3"],"|",grille["C3"],"|", "3","\n",
        " ---- ---- ----", "\n",
        "  A    B     C","\n"
    )        

def premier_joueur_aleatoire():
    """_summary_
    Détermine aléatoirement quel joueur doit commencer
    Affiche le jouer determiner
    Lance le premier tour de joeur
    """
    if random_int == 0:
        print("\n","LES ⭕ COMMENCENT !","\n")
        afficher_la_grille()
        rond_joue()
    else:
        print("\n","LES ❌ COMMENCENT !","\n")
        afficher_la_grille()
        croix_joue()

        
def croix_joue():
    """_summary_
    Process lorsque c'est aux croix de jouer
    Attends un input valide des cases jouables
    Previent le joueur si case invalide
    """
    choix_x = input("C'est aux ❌ de jouer.\nSur quelle case voulez-vous jouer ? : ").upper()
    if grille.get(choix_x) == None:
        print("### SAISIE NON VALIDE ###")
        croix_joue()
    elif grille.get(choix_x) != "  ":
        print("### CASE DEJA JOUÉE ###")
        croix_joue()
    else:    
        grille[choix_x] = "❌"
        afficher_la_grille()
        si_victoire()
        si_egalite()
        rond_joue()
        
def rond_joue():
    """_summary_
    Process lorsque c'est aux ronds de jouer
    Attends un input valide des cases jouables
    Previent le joueur si case invalide
    """
    choix_o = input("C'est aux ⭕ de jouer.\nSur quelle case voulez-vous jouer ? : ").upper()
    if grille.get(choix_o) == None:
        print("### SAISIE NON VALIDE ###")
        rond_joue()
    elif grille.get(choix_o) != "  ":
        print("### CASE DEJA JOUÉE ###")
        rond_joue()
    else:    
        grille[choix_o] = "⭕"
        afficher_la_grille()
        si_victoire()
        si_egalite()
        croix_joue()
    
        
def si_victoire():
    """_summary_
    Vérifie les scores
    Arrête la partie en case de victoire
    Affiche le gagnant
    """
    row1 = [ grille["A1"], grille["A2"], grille["A3"]]
    row2 = [ grille["B1"], grille["B2"], grille["B3"]]
    row3 = [ grille["C1"], grille["C2"], grille["C3"]]
    col1 = [ grille["A1"], grille["B1"], grille["C1"]]
    col2 = [ grille["A2"], grille["B2"], grille["C2"]]
    col3 = [ grille["A3"], grille["B3"], grille["C3"]]
    diag1 = [ grille["A1"], grille["B2"], grille["C3"]]
    diag2 = [ grille["A3"], grille["B2"], grille["C1"]]
    
    combinaisons = [row1,row2,row3,col1,col2,col3,diag1,diag2]
    
    for comb in combinaisons:
        if comb == [ "⭕", "⭕", "⭕"]:
            print("####################################", "\n",
                  "### BRAVO ⭕ VOUS AVEZ GAGNÉ !!! ###", "\n", 
                  "####################################")
            quit()
        elif comb == [ "❌", "❌", "❌"]:
            print("####################################", "\n",
                  "### BRAVO ❌ VOUS AVEZ GAGNÉ !!! ###", "\n", 
                  "####################################")
            quit()

          
def si_egalite():
    """
    Vérifie si le jeu est encore jouable
    Arrête la partie si égalité
    """
    if grille["A1"] != "  " and grille["A2"] != "  " and grille["A3"] != "  " and grille["B1"] != "  " and grille["B2"] != "  " and grille["B3"] != "  " and grille["C1"] != "  " and grille["C2"] != "  " and grille["C3"] != "  ":
        print(" ###################", "\n",
            "### ÉGALITÉ !!! ###", "\n", 
            "###################")
        quit()
    
    
tictactoe()