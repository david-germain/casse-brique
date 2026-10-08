# Classe pour l'interface graphique du jeu
# Fait par @david-germain | david-germain.ndiaye@cpe.fr
# Fait le 08/10/2026

# On définit la classe
class Balle:
    def __init__(self, canvas, x_depart, y_depart):
        self.canvas = canvas
        self.rayon = 10 # Rayon de 10 pixels pour la balle

        # On crée la balle (un cercle rouge)
        self.id = canvas.create_oval(
            x_depart - self.rayon, y_depart - self.rayon,
            x_depart + self.rayon, y_depart + self.rayon,
            fill = "red"
        )

        # On définit la vitesse de déplacement de la balle en X et en Y
        # Pour avoir un diagonale il faut que x soit égal à y
        self.vitesse_x = 5
        self.vitesse_y = -5 # Négatif au départ pour que la balle monte au début du jeu

        # On reprend la valeur des canvas pour gérer les rebonds
        self.largeur_canevas = int(self.canvas['width'])


    # Déplacements de la balle
    def deplacer(self):
        # On déplace la balle
        self.canvas.move(self.id, self.vitesse_x, self.vitesse_y)

        # On récupère les nouvelles coordonées de la balle
        coords = self.canvas.coords(self.id)

        # On gère les collisions avec les bords du canevas
        if coords[0] <= 0 or coords[2] >= self.largeur_canevas: # coord[0] correspond au bord gauche de la balle et coords[2] au bord droit
            self.vitesse_x = - self.vitesse_y # On inverse la direction horizontale x ===> -x

        if coords[1] <= 0: # coords[1] correspond au haut de la balle
            self.vitesse_y = - self.vitesse_x # On inverse la direction verticale y ===> -y