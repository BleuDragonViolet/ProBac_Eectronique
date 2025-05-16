import tkinter as tk
from tkinter import messagebox
import random
import webbrowser
import os

# Couleurs & Style
COULEUR_FOND = '#1e1e2f'
COULEUR_TEXTE = '#f8f8f2'
COULEUR_VALID = '#38b000'
COULEUR_FAUX = '#d00000'
COULEUR_BOUTON = '#52b788'
COULEUR_BOUTON_CORRIGE = '#ef476f'
COULEUR_REPONSE_AUTO = '#ffa200'
POLICE = ("Segoe UI", 14)
POLICE_TITRE = ("Segoe UI", 16, "bold")
COULEUR_REPONSE_AUTO = '#ffa200'
COULEUR_NEON = '#9d4edd' 
POLICE = ("Segoe UI", 14)



# Questions extraites du PDF 2022 corrigé – version simplifiée
questions_reponses = [
    {"question": "Question 1 - Compléter la référence du commutateur de cœur.", "bonnes_reponses": ["s4148f-on", "dell s4148", "s4148", "commutateur dell"]},
    {"question": "Question 2 - Puissance max consommée par un commutateur de cœur.", "bonnes_reponses": ["370w", "370 w"]},
    {"question": "Question 3 - Ports SFP+ et QSFP28 disponibles.", "bonnes_reponses": ["12 sfp+", "3 qsfp28", "12 et 3", "sfp+ qsfp28"]},
    {"question": "Question 4 - Puissance consommée par S4112F-ON.", "bonnes_reponses": ["180w", "180 w"]},
    {"question": "Question 5 - Avantage liaison VLTi.", "bonnes_reponses": ["redondance", "disponibilité", "continuité"]},
    {"question": "Question 6 - Interfaces à paramétrer pour VLTi.", "bonnes_reponses": ["1/1/11", "1/1/12"]},
    {"question": "Question 7 - Adresse IP et masque de SW2.", "bonnes_reponses": ["10.2.255.2", "255.255.0.0"]},
    {"question": "Question 8 - Port de management.", "bonnes_reponses": ["1/1/1"]},
    {"question": "Question 9 - Erreur IP et correction.", "bonnes_reponses": ["ip incorrecte", "changer ip", "mauvais réseau"]},
    {"question": "Question 10 - Avantage LAG.", "bonnes_reponses": ["bande passante", "redondance", "agrégation"]},
    {"question": "Question 11 - Tracer VLTi et LAG.", "bonnes_reponses": ["vlt", "lag", "liaison"]},
    {"question": "Question 12 - Compléter le bilan de puissance.", "bonnes_reponses": ["4540w", "5044va"]},
    {"question": "Question 13 - Choisir l’onduleur adapté.", "bonnes_reponses": ["eaton 9px6kibp", "6000va"]},
    {"question": "Question 14 - Temps de fonctionnement sans batterie.", "bonnes_reponses": ["3min", "3 min", "3 minutes"]},
    {"question": "Question 15 - Capacité et nb de batteries.", "bonnes_reponses": ["5ah", "15"]},
    {"question": "Question 16 - Capacité totale.", "bonnes_reponses": ["75ah"]},
    {"question": "Question 17 - Temps avec 6 modules.", "bonnes_reponses": ["39min", "39 minutes"]},
    {"question": "Question 18 - Temps conforme.", "bonnes_reponses": ["oui", "conforme"]},
    {"question": "Question 19 - Type de fibre QSFP+.", "bonnes_reponses": ["multimode", "om5"]},
    {"question": "Question 20 - Type fibre selon distance.", "bonnes_reponses": ["om5"]},
    {"question": "Question 21 - Image pigtail.", "bonnes_reponses": ["pigtail"]},
    {"question": "Question 22 - Réf module SFP+.", "bonnes_reponses": ["j9150d"]},
    {"question": "Question 23 - Traversées tiroir.", "bonnes_reponses": ["adaptateur lc"]},
    {"question": "Question 24 - Ordre soudure pigtail.", "bonnes_reponses": ["1 à 9", "dénuder", "souder"]},
    {"question": "Question 25 - Décrire les soudures.", "bonnes_reponses": ["arc", "non soudée", "fibre décalée"]},
    {"question": "Question 26 - Repère commutateur bureau étude.", "bonnes_reponses": ["sw12-r12-b1"]},
    {"question": "Question 27 - Nb liaisons fibres.", "bonnes_reponses": ["2", "sw3", "sw4"]},
    {"question": "Question 28 - Réf commutateur HP.", "bonnes_reponses": ["6200f", "jl726a"]},
    {"question": "Question 29 - VLANs à configurer.", "bonnes_reponses": ["3", "11", "12", "20"]},
    {"question": "Question 30 - VLAN imprimante + IP.", "bonnes_reponses": ["11", "10.11.255.128/25"]},
    {"question": "Question 31 - Bits hôtes disponibles.", "bonnes_reponses": ["7", "126"]},
    {"question": "Question 32 - Nb imprimantes possibles.", "bonnes_reponses": ["126"]},
    {"question": "Question 33 - Compléter tableau VLAN/prises.", "bonnes_reponses": ["s24", "s25", "s26", "s10", "s12"]},
    {"question": "Question 34 - Tracer connexions baie.", "bonnes_reponses": ["liaisons", "connexion"]},
    {"question": "Question 35 - Poste compatible IP.", "bonnes_reponses": ["alcatel sp 2503"]},
    {"question": "Question 36 - Norme SIP téléphone.", "bonnes_reponses": ["rfc 3261", "sip v2"]},
    {"question": "Question 37 - Compatibilité serveur.", "bonnes_reponses": ["compatible", "sip"]},
    {"question": "Question 38 - Téléphone pour déplacement.", "bonnes_reponses": ["ip2215"]},
    {"question": "Question 39 - Paramétrage LAN OmniPCX.", "bonnes_reponses": ["vlan 2", "vlan 20"]},
    {"question": "Question 40 - Connecteur caméra.", "bonnes_reponses": ["usb c"]},
    {"question": "Question 41 - Connecteur speaker.", "bonnes_reponses": ["usb 2"]},
    {"question": "Question 42 - Dock compatible.", "bonnes_reponses": ["panacast hub"]},
    {"question": "Question 43 - Connecteurs câbles.", "bonnes_reponses": ["usb", "hdmi", "rj45"]},
    {"question": "Question 44 - Badge RFID.", "bonnes_reponses": ["seos", "125khz"]},
    {"question": "Question 45 - Ordre contrôles carte.", "bonnes_reponses": ["visuel", "multimètre", "oscilloscope", "fusibles"]},
    {"question": "Question 46 - Associer composants.", "bonnes_reponses": ["pont de diodes", "condensateur", "transformateur"]},
    {"question": "Question 47 - Composant défectueux.", "bonnes_reponses": ["condensateur"]},
    {"question": "Question 48 - Oscillogramme correct.", "bonnes_reponses": ["filtré", "stable"]},
]

class CodeCheckApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Accès au Quiz")
        self.root.geometry("400x300")
        self.root.configure(bg=COULEUR_FOND)

        tk.Label(root, text="Entrez le code (2021 ou 2022) :", fg=COULEUR_TEXTE, bg=COULEUR_FOND, font=POLICE_TITRE).pack(pady=20)
        self.code_entry = tk.Entry(root, font=POLICE, width=20)
        self.code_entry.pack(pady=10)
        tk.Button(root, text="Valider", command=self.verifier_code, font=POLICE, bg="#0077b6", fg="white", width=15).pack(pady=10)

        self.label_erreur = tk.Label(root, text="", fg='red', bg=COULEUR_FOND, font=("Segoe UI", 12))
        self.label_erreur.pack()

    def ouvrir_pdf(self, nom_fichier):
        chemin = os.path.abspath(nom_fichier)
        webbrowser.open_new(chemin)

    def verifier_code(self):
        code = self.code_entry.get().strip()
        if code in ["2021", "2022"]:
            self.root.destroy()
            racine = tk.Tk()
            app = QuizApp(racine)
            racine.mainloop()
        else:
            self.label_erreur.config(text="❌ Code incorrect.")

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz BAC PRO")
        self.root.geometry("1000x700")
        self.root.configure(bg=COULEUR_FOND)

        self.current_question = 0
        self.nb_corriges = 0
        self.nb_corrects = 0
        self.a_corrige = False
        self.nb_clicks_pseudo = 0

        # Top bar (score + menu + ressources)
        self.top_bar = tk.Frame(root, bg=COULEUR_FOND)
        self.top_bar.pack(anchor='nw', pady=10, padx=10, fill='x')

        self.label_score = tk.Label(self.top_bar, text="Score : 0 / 0", fg=COULEUR_TEXTE, bg=COULEUR_FOND, font=("Segoe UI", 12, "bold"))
        self.label_score.pack(side='left', padx=(0, 10))

        self.btn_menu = tk.Button(self.top_bar, text="Menu", font=("Segoe UI", 10), bg="#5f0f40", fg="white", command=self.ouvrir_menu)
        self.btn_menu.pack(side='left')

        self.btn_ressources = tk.Button(self.top_bar, text="Ressources", font=("Segoe UI", 10), bg="#3a0ca3", fg="white", command=self.ouvrir_ressources)
        self.btn_ressources.pack(side='left', padx=(10, 0))

        self.label_question = tk.Label(root, text="", fg=COULEUR_TEXTE, bg=COULEUR_FOND, wraplength=700, font=POLICE_TITRE)
        self.label_question.pack(pady=(30, 20))

        self.entry = tk.Entry(root, font=POLICE, width=60, bd=2, relief="solid")
        self.entry.pack(pady=10)

        self.frame_boutons = tk.Frame(root, bg=COULEUR_FOND)
        self.frame_boutons.pack(pady=10)

        self.btn_valider = tk.Button(self.frame_boutons, text="Valider", command=self.verifier_reponse, font=POLICE, bg=COULEUR_BOUTON, fg="white", width=12)
        self.btn_valider.grid(row=0, column=0, padx=10)

        self.btn_corrige = tk.Button(self.frame_boutons, text="Corrigé", command=self.corriger, font=POLICE, bg=COULEUR_BOUTON_CORRIGE, fg="white", width=12)
        self.btn_corrige.grid(row=0, column=1, padx=10)

        self.label_feedback = tk.Label(root, text="", fg='orange', bg=COULEUR_FOND, font=("Segoe UI", 12))
        self.label_feedback.pack()

        # 👑 Pseudo néon
        self.label_pseudo = tk.Label(root, text="👑 Evan 👑", fg=COULEUR_NEON, bg=COULEUR_FOND,
                                     font=("Segoe UI", 10, "italic"), bd=2, relief="groove", padx=10, pady=2)
        self.label_pseudo.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)
        self.label_pseudo.bind("<Button-1>", self.compter_clicks)

        self.afficher_question()

    def afficher_question(self):
        self.a_corrige = False
        q = questions_reponses[self.current_question]
        self.label_question.config(text=f"{q['question']}")
        self.entry.delete(0, tk.END)
        self.entry.config(bg='white')
        self.label_feedback.config(text="")
        if hasattr(self, 'btn_javais_bon'):
            self.btn_javais_bon.destroy()
        self.btn_corrige.config(state="normal")
        self.mettre_a_jour_score()

    def verifier_reponse(self):
        reponse = self.entry.get().strip().lower()
        bonnes = [r.lower() for r in questions_reponses[self.current_question]['bonnes_reponses']]
        if any(b in reponse for b in bonnes):
            self.entry.config(bg=COULEUR_VALID)
            if not self.a_corrige:
                self.nb_corrects += 1
            if hasattr(self, 'btn_javais_bon'):
                self.btn_javais_bon.destroy()
            self.root.after(1000, self.suivant)
        else:
            self.entry.config(bg=COULEUR_FAUX)
            self.root.bell()
            self.label_feedback.config(text="❌ Mauvaise réponse !")
        self.mettre_a_jour_score()

    def corriger(self):
        self.nb_corriges += 1
        self.a_corrige = True
        bonne = questions_reponses[self.current_question]['bonnes_reponses'][0]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, bonne)
        self.entry.config(bg=COULEUR_REPONSE_AUTO)
        self.label_feedback.config(text="Réponse insérée automatiquement.")
        self.btn_javais_bon = tk.Button(self.root, text="J'avais bon", command=self.annuler_corrige, font=("Segoe UI", 12), bg="#06d6a0", fg="white")
        self.btn_javais_bon.pack(pady=5)
        self.btn_corrige.config(state="disabled")
        self.mettre_a_jour_score()

    def annuler_corrige(self):
        self.nb_corriges -= 1
        self.nb_corrects += 1
        self.a_corrige = False
        self.btn_javais_bon.destroy()
        self.btn_corrige.config(state="normal")
        self.label_feedback.config(text="✅ Correction annulée, réponse validée comme correcte.")
        self.mettre_a_jour_score()

    def suivant(self):
        self.current_question += 1
        if self.current_question >= len(questions_reponses):
            self.fin_quiz()
        else:
            self.afficher_question()

    def fin_quiz(self):
        score = f"""✅ Quiz terminé !
Réponses justes sans aide : {self.nb_corrects}
Réponses affichées avec "Corrigé" : {self.nb_corriges}"""
        messagebox.showinfo("Résultat final", score)
        self.root.quit()

    def mettre_a_jour_score(self):
        total = self.current_question + 1
        self.label_score.config(text=f"Score : {self.nb_corrects} / {total}")

    def ouvrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        login_app = CodeCheckApp(root)
        root.mainloop()

    def ouvrir_pdf(self, nom_fichier):
        chemin = os.path.abspath(nom_fichier)
        webbrowser.open_new(chemin)

    def ouvrir_ressources(self):
        fenetre = tk.Toplevel(self.root)
        fenetre.title("📁 Ressources disponibles")
        fenetre.geometry("400x200")
        fenetre.configure(bg=COULEUR_FOND)

        tk.Label(fenetre, text="📄 Documents à consulter :", fg=COULEUR_TEXTE, bg=COULEUR_FOND, font=POLICE_TITRE).pack(pady=15)

        for nom in ["2021.pdf", "2022.pdf"]:
            lien = tk.Label(fenetre, text=nom, fg="#00b4d8", cursor="hand2", bg=COULEUR_FOND, font=("Segoe UI", 12, "underline"))
            lien.pack()
            lien.bind("<Button-1>", lambda e, f=nom: self.ouvrir_pdf(f))

        tk.Button(fenetre, text="Fermer", command=fenetre.destroy, font=POLICE, bg="#ef476f", fg="white").pack(pady=10)

    def compter_clicks(self, event):
        self.nb_clicks_pseudo += 1
        if self.nb_clicks_pseudo == 5:
            self.afficher_ressource_secrete()

    def afficher_ressource_secrete(self):
        fenetre = tk.Toplevel(self.root)
        fenetre.title("🔐 Accès secret")
        fenetre.geometry("400x250")
        fenetre.configure(bg=COULEUR_FOND)

        tk.Label(fenetre, text="🎁 Corrigés secrets :", fg=COULEUR_TEXTE, bg=COULEUR_FOND, font=POLICE_TITRE).pack(pady=15)
        for nom in ["2021 corriger.pdf", "2022 corriger.pdf"]:
            lien = tk.Label(fenetre, text=nom, fg="#00b4d8", cursor="hand2", bg=COULEUR_FOND, font=("Segoe UI", 12, "underline"))
            lien.pack()
            lien.bind("<Button-1>", lambda e, f=nom: self.ouvrir_pdf(f))

        tk.Button(fenetre, text="Fermer", command=fenetre.destroy, font=POLICE, bg="#ef476f", fg="white").pack(pady=10)


        

if __name__ == "__main__":
    
    root = tk.Tk()
    login_app = CodeCheckApp(root)
    root.mainloop()