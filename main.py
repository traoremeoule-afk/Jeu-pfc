from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import random

Window.clearcolor = (0.1, 0.1, 0.15, 1)

class PierreFeuilleCiseauxApp(App):
    def build(self):
        self.score_joueur = 0
        self.score_ordi = 0
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        self.label_score = Label(text="Toi : 0   |   Ordinateur : 0", font_size='24sp', size_hint_y=0.15, bold=True)
        layout.add_widget(self.label_score)
        self.label_resultat = Label(text="Fais ton choix !", font_size='20sp', halign="center", valign="middle", size_hint_y=0.35)
        self.label_resultat.bind(size=self.label_resultat.setter('text_size'))
        layout.add_widget(self.label_resultat)
        layout_boutons = BoxLayout(size_hint_y=0.3, spacing=10)
        btn_pierre = Button(text="Pierre", font_size='20sp', background_color=(0.3, 0.5, 0.8, 1))
        btn_pierre.bind(on_press=lambda x: self.jouer("pierre"))
        btn_feuille = Button(text="Feuille", font_size='20sp', background_color=(0.3, 0.7, 0.4, 1))
        btn_feuille.bind(on_press=lambda x: self.jouer("feuille"))
        btn_ciseaux = Button(text="Ciseaux", font_size='20sp', background_color=(0.8, 0.4, 0.3, 1))
        btn_ciseaux.bind(on_press=lambda x: self.jouer("ciseaux"))
        layout_boutons.add_widget(btn_pierre)
        layout_boutons.add_widget(btn_feuille)
        layout_boutons.add_widget(btn_ciseaux)
        layout.add_widget(layout_boutons)
        btn_reset = Button(text="Réinitialiser le score", font_size='16sp', size_hint_y=0.15, background_color=(0.5, 0.5, 0.5, 1))
        btn_reset.bind(on_press=self.reinitialiser)
        layout.add_widget(btn_reset)
        return layout

    def jouer(self, choix_joueur):
        choix_ordi = random.choice(["pierre", "feuille", "ciseaux"])
        bat = {"pierre": "ciseaux", "feuille": "pierre", "ciseaux": "feuille"}
        if choix_joueur == choix_ordi:
            resultat = "Égalité !"
        elif bat[choix_joueur] == choix_ordi:
            resultat = "Tu gagnes la manche !"
            self.score_joueur += 1
        else:
            resultat = "L'ordinateur gagne !"
            self.score_ordi += 1
        self.label_resultat.text = f"Toi : {choix_joueur.capitalize()}\nVS\nOrdi : {choix_ordi.capitalize()}\n\n{resultat}"
        self.label_score.text = f"Toi : {self.score_joueur}   |   Ordinateur : {self.score_ordi}"

    def reinitialiser(self, instance):
        self.score_joueur = 0
        self.score_ordi = 0
        self.label_score.text = "Toi : 0   |   Ordinateur : 0"
        self.label_resultat.text = "Fais ton choix !"

if __name__ == '__main__':
    PierreFeuilleCiseauxApp().run()
    
