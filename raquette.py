# Classe pour la raquette du jeu en bas du canevas
# Fait par @david-germain | david-germain.ndiaye@cpe.fr
# Fait le 08/10/2026

# On importe Tkinter
import tkinter as tk

# On définit la classe de la raquette
class Raquette:
    def __init__(self, canvas, largeur_canevas):
        self.canvas = canvas
        self.largeur_canevas = largeur_canevas

        # On définit les dimensions de la raquette
        self.largeur = 90
        self.hauteur = 15

        # On défitnit la position de départ de la raquette
        x_depart = (self.largeur_canevas / 2) - (self.largeur / 2) # On divise par deux pour correspondre au milieu de la largeur du canevas
        y_départ = 430 # Positionée en bas du canevas

        # Matérialisation de la raquette (rectangle)
        self.id = canvas.create_rectangle(
            # Dimensions et position de départ
            x_depart, y_départ,
            x_depart + self.largeur, y_départ + self.hauteur,

            # Couleur de la raquette
            fill = "blue"
        )

        # On définit la vitesse de déplacement de la raquette
        self.vitesse = 20 # Ce qui correspond au nombre de pixels parcouru à chaque mouvement


    # On définit les mouvements de la raquette avec coords qui permet de modifier les coordonées de la raquette
    def aller_a_gauche(self):
        coords = self.canvas.coords(self.id)

        if coords[0] > 0: # Cela empêche la raquette de sortir de l'écran à gauche
            self.canvas.move(self.id, -self.vitesse, 0)

    def aller_a_droite(self):
            coords = self.canvas.coords(self.id)

            # coords[2] correspond à la coordonée X du bord gauche de la raquette
            if coords[2] < self.largeur_canevas: # Cela empêche la raquette de sortir de l'écran à droite
                self.canvas.move(self.id, self.vitesse, 0)