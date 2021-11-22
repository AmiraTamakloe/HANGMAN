
def jeu(mot, listesecret):
    tiret(mot)
    vivant = True
    nbchances = len(mot)
    precedent = []
    while not nbchances == 0:
        #recevoir un guess et s'assurer len==1 et une lettre
        essaie = lettre()

        #vérifier pas déjà demander
        while essaie in precedent:
            print("Lettre déjà essayée")
            essaie = lettre()
        
        #ajouter char à liste des essaies précédent
        precedent.append(essaie)

        #vérifier si nouveau char est ds mot secret
        listesecret, nbchances = verif(essaie, listesecret, mot, nbchances)
    print("Échec!") 




def verif(ess, tir, mot_s, chance):

    #Pour si bon
    if ess in mot_s:

        #Find position
        pos = [i for i, letter in enumerate(mot_s) if letter == ess]

        #Modifier les tirets
        for z in (pos):

            tir[z] = ess

        if ''.join(tir) == mot_s:
            print("Bravo!")
            quit()
        
        print(tir)
        return tir, chance
    
    #si pas bon
    else:
        chance -=1
        print("Mauvais choix!")
        print("Chance(s) restante(s): ", chance)
        print(tir)
        return tir, chance


    
def tiret(longu):
    l = len(longu)
    d = 0
    list_tirets = []
    while d < l:
        list_tirets.append("_")
        d += 1
    return list_tirets

def lettre():
    guess = input("Donner une seule lettre ")
    while not (guess.isalpha and guess == len(guess) * guess[0]):
        print("Tentative refusée") 
        guess = input("Donner une seule lettre ")
    return guess

mot_secret = input("Votre mot secret ")
while not mot_secret.isalpha:
    mot_secret = input("Votre mot secret ")

ltirets = tiret(mot_secret)

jeu(mot_secret, ltirets)

