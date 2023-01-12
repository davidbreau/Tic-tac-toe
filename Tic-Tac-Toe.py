import random
random_int = random.randint(0,1)
grille = { "A1" : "  ", "A2" : "  ", "A3" : "  ",
    "B1" : "  ", "B2" : "  ", "B3" : "  ",
    "C1" : "  ", "C2" : "  ", "C3" : "  "
}

def tictactoe():
    print("### TICTACTOE ###")
    premier_joueur_aleatoire()
    
def afficher_la_grille():
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

def premier_joueur_aleatoire() -> str:
    """_summary_
    Détermine aléatoirement quel joueur doit commencer
    Returns:
        str: _description_
    Renvoie un texte précisant quel joueur commence
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
    ch_x = input("C'est aux ❌ de jouer.\nSur quelle case voulez-vous jouer ? : ")
    if grille.get(ch_x) == None:
        print("### SAISIE NON VALIDE ###")
        croix_joue()
    elif grille.get(ch_x) != "  ":
        print("### CASE DEJA JOUÉE ###")
        croix_joue()
    else:    
        grille[ch_x] = "❌"
        afficher_la_grille()
        si_victoire()
        rond_joue()
        
def rond_joue():
    ch_r = input("C'est aux ⭕ de jouer.\nSur quelle case voulez-vous jouer ? : ")
    if grille.get(ch_r) == None:
        print("### SAISIE NON VALIDE ###")
        rond_joue()
    elif grille.get(ch_r) != "  ":
        print("### CASE DEJA JOUÉE ###")
        rond_joue()
    else:    
        grille[ch_r] = "⭕"
        afficher_la_grille()
        si_victoire()
        croix_joue()
        
def si_victoire():
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
            
tictactoe()