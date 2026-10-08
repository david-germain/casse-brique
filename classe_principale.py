# Classe principale pour l'interface graphique du jeu
# Fait par @david-germain | david-germain.ndiaye@cpe.fr
# Fait le 08/10/2026
# To do: 
#   - Gérer les collisions avec les bords gauche/droite/haut (rebond)
#   - Faire en sorte que si la balle atteint le bas du canevas → vie perdue
#   - Gérer la collision balle-raquette : la balle rebondit vers le haut en respectant la loi de Descartes
#   - Ajouter une première rangée de briques (rectangles colorés) sur la partie haute du canevas
#   - Faire en sorte que lorsqu’une balle touche une brique, la brique disparaît et la balle rebondit
#   - Faire en sorte que le joueur marque des points
#   - Ajouter plusieurs rangées de briques
#   - Implémenter la notion de vies (par exemple 3 vies affichées quelque part dans la fenêtre)
#   - Faire la fin de partie :
#       . Victoire si toutes les briques sont détruites
#       . Défaite si toutes les vies sont perdues

# On importe Tkinter et toutes les autres classes
import tkinter as tk
from raquette import Raquette
from balle import Balle


# On définit l'Interface de départ
class CasseBrique(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Casse Brique") # Titre de la fenêtre
        self.geometry("700x500") # Taille de la fenêtre par défaut

        self.initialiser_interface()

    # On initialise tous les éléments graphiques
    def initialiser_interface(self):
        # Menu déroulant
        # Barre du menu
        barre_menu = tk.Menu(self)

        # Création du menu
        menu_options = tk.Menu(barre_menu, tearoff = 0) # Le tearoff empêche le menu de se détacher

        # Ajout des options du menu
        menu_options.add_command(label = "Nouvelle Partie", command = self.nouvelle_partie)
        menu_options.add_separator() # On ajoute une ligne de séparation (esthétique)
        menu_options.add_command(label = "Quitter", command = self.quitter)

        # Ajout du menu dans la fenêtre
        barre_menu.add_cascade(label = "Options", menu = menu_options)

        # Configuration de la fenêtre pour qu'on puisse utiliser ce menu
        self.config(menu = barre_menu)



        # Zone de jeu (Canevas)
        self.zone_de_jeu = tk.Canvas(self, width = 700, height = 470, bg = "black")
        self.zone_de_jeu.pack()

    
        # Zone de texte pour les vies
        self.zone_de_jeu.create_text(40, 20, text = "Vies: 3", fill = "yellow", font = ("Arial", 13))

        # Zone de texte pour le score
        self.zone_de_jeu.create_text(500, 20, text = "Score: 0", fill = "yellow", font = ("Arial", 13))


        # On initialise la raquette dans le canevas
        # On passe l'objet canevas et la largeur de la fenêtre
        self.raquette = Raquette(self.zone_de_jeu, 700)

        # On initialise la balle au milieu du canevas
        self.balle = Balle(self.zone_de_jeu, 350, 250)

        # Gestion des déplacements de la raquette
        # On fait un dictionnaire des touches pour savoir quelles touches sont enfoncées
        self.touches = {"Left": False, "Right": False}

        # Association "bind" des flèches directionnelles du clavier
        # On utilise "KeyPress" pour dectecter une touche enfoncée et "KeyRelease" pour une touche relâchér
        self.bind("<KeyPress-Left>", self.touche_pressee)
        self.bind("<KeyRelease-Left>", self.touche_relachee)

        self.bind("<KeyPress-Right>", self.touche_pressee)
        self.bind("<KeyRelease-Right>", self.touche_relachee)

        # On lance la boucle de jeu
        self.boucle_jeu()


        # Frame pour regrouper les boutons "Commencer" et "Quitter"
        self.frame_boutons = tk.Frame(self)
        self.frame_boutons.pack()

        # Boutton "Commencer"
        self.bouton_commencer = tk.Button(self.frame_boutons, text = "Commencer")
        self.bouton_commencer.pack(side = tk.LEFT, padx = 10) # On met à gauchhe et on espace de 10

        # Bouton "Quitter"
        self.bouton_quitter = tk.Button(self.frame_boutons, text = "Quitter", command = self.quitter)
        self.bouton_quitter.pack(side = tk.LEFT, padx = 10)



    # Fonction d'initialisation d'une nouvelle partie
    def nouvelle_partie(self):
            print("Lancement d'une nouvelle partie !")

    # Fonctions pour gérer les tohces directionnelles (enfoncée ou relâchée)
    def touche_pressee(self, event):
         self.touches[event.keysym] = True # On met "True" à l'état où la touche est enfoncée

    def touche_relachee(self, event):
             self.touches[event.keysym] = False # On met "False" à l'état où la touche est relâchée

    # Fonction en boucle qui permet de mettre à jour le jeu
    def boucle_jeu(self):
         # On vérifie l'état des touches à chaque tour de la boucle
         if self.touches.get("Left"):
              self.raquette.aller_a_gauche()

         if self.touches.get("Right"):
              self.raquette.aller_a_droite()

        # On fait bouger la balle
         self.balle.deplacer()

        # On utilise self.after pour rappeler la méthode utilisé à chaque 20 ms
         self.after(20, self.boucle_jeu)

    # Fonction qui permet de fermer la fenêtre et qutter le programme
    def quitter(self):
        self.quit() # Quitte le programme
        self.destroy() # Ferme la fenêtre

# Execution du programme
if __name__ == "__main__":
    app = CasseBrique()
    app.mainloop()

