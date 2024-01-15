import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from validate_email import validate_email
import sqlite3

class GestionEnseignant:
    def __init__(self, master):
        self.master = master
        
        self.master.title("Système de gestion d'un établissement de formation")
        
        
        
        #application  width and  height
        screen_width = master.winfo_screenwidth() #-->  get the sreen width and set it to the application
        screen_height = master.winfo_screenheight() #-->  get the sreen height and set it to the application
        
        self.master.geometry("%dx%d"% (screen_width, screen_height))
        self.master.config(bg="#576f9c")
        
        # creat the title label window for students manage
        title_label = Label(self.master, text="GESTION DES ENSEIGNANTS", bd=2,
                    relief=GROOVE, font=("ubuntu", 20, "bold"), padx=20, bg="#369c1a") # #0584FB
        title_label.pack(side=TOP, fill=X)
        
        ####### TOP MENU FRAME ##########
        top_frame = Frame(self.master, bd=2, relief=GROOVE, bg="#191970") # #323232
        top_frame.place(x=20, y=50, width=0.97*screen_width, height=80)
        
        formation_button = Button(top_frame, text="GESTION DES FORMATIONS", font=("ubuntu", 13, 'bold'), width=25, height=2, cursor='hand2', command=self.gestion_formation, bg="#0584FB")
        formation_button.grid(row=0, column=1, padx=10, pady=10)
        
        inscription_button = Button(top_frame, text="GESTION DES INSCRIPTIONS", font=("ubuntu", 13, 'bold'), width=25, height=2, cursor='hand2', command=self.gestion_inscription, bg="purple")
        inscription_button.grid(row=0, column=2, padx=10, pady=10)
        
        etudiant_button = Button(top_frame, text="GESTION DES ETUDIANTS", font=("ubuntu", 13, 'bold'), width=25, height=2, cursor='hand2', bg="#DF73FF", command=self.gestion_etudiant)
        etudiant_button.grid(row=0, column=3, padx=10, pady=10)
        
        ################# ENSEIGNANT DATA ###################
        enseignant_manage_frame = Frame(self.master, bd=2, relief=GROOVE, bg="#323232")
        enseignant_manage_frame.place(x=20, y=130, width=0.32*screen_width, height=560)
        
        title_enseignant_label = Label(enseignant_manage_frame,text="INFORMATIONS SUR LES ENSEIGNANTS",
                      font=("ubuntu", 15, 'bold', "underline"), bg="#323232", fg="white")
        title_enseignant_label.grid(row=0, columnspan=2, pady=15, padx=15)
        
        ############### ENSEIGNANT DATA ENTRY FORM ###############
        self.nom_enseignant_label = Label(enseignant_manage_frame, text="NOM* : ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        self.nom_enseignant_label.grid(row=1, column=0, pady=10, sticky='w')
        
        self.nom_enseignant_entry = Entry(enseignant_manage_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        self.nom_enseignant_entry.grid(row=1, column=1, padx= 10, pady=10, sticky='w')
        
        
        self.prenom_enseignant_label = Label(enseignant_manage_frame, text="PRENOM* : ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        self.prenom_enseignant_label.grid(row=2, column=0, pady=10, sticky='w')
        
        self.prenom_enseignant_entry = Entry(enseignant_manage_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        self.prenom_enseignant_entry.grid(row=2, column=1, padx= 10, pady=10, sticky='w')
        
        
        self.tel_enseignant_label =  Label(enseignant_manage_frame, text="TELEPHONE* : ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        self.tel_enseignant_label.grid(row=3, column=0, pady=10, sticky='w')
        
        self.tel_enseignant_entry =  Entry(enseignant_manage_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        self.tel_enseignant_entry.grid(row=3, column=1, padx= 10, pady=10, sticky='w')
        
        
        self.mail_enseignant_label = Label(enseignant_manage_frame, text="E_mail* : ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        self.mail_enseignant_label.grid(row=4, column=0, pady=10, sticky='w')
        
        self.mail_enseignant_entry = Entry(enseignant_manage_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        self.mail_enseignant_entry.grid(row=4, column=1, padx= 10, pady=10, sticky='w')
        
        
        self.intitule_formation_label = Label(enseignant_manage_frame, text="FORMATION DONNEE* : ", font=("ubuntu", 12, 'bold'), bg="#323232", fg="white")
        self.intitule_formation_label.grid(row=5, column=0, pady=10, sticky='w')
        
        self.intitule_formation_entry = Entry(enseignant_manage_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        self.intitule_formation_entry.grid(row=5, column=1, padx= 10, pady=10, sticky='w')
        
        
        self.niveau_formation_label = Label(enseignant_manage_frame, text="NIVEAU FORMATION* : ", font=("ubuntu", 12, 'bold'), bg="#323232", fg="white")
        self.niveau_formation_label.grid(row=6, column=0, pady=10, sticky='w')
        
        self.niveau_formation_entry = Entry(enseignant_manage_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        self.niveau_formation_entry.grid(row=6, column=1, padx= 10, pady=10, sticky='w')
        
        
        ############### BOTTOM FRAME IN enseignant_manage_frame #################
        enseignant_bottom_frame = Frame(enseignant_manage_frame, bd=2, relief=GROOVE, bg="#323232")
        enseignant_bottom_frame.place(x=15, y=450, width=0.27*screen_width, height=80)
        
        ##### button into enseignant_bottom_frame
        self.register_button = Button(enseignant_bottom_frame, text="Enregistrer", width=8, height=3, command=self.enregistrer_enseignant, cursor="hand2")
        self.register_button.grid(row=0, column=0, padx=10, pady=10)
        
        
        self.modifier_button = Button(enseignant_bottom_frame, text="Modifier", width=8, height=3, command=self.modifier_enseignant, cursor="hand2")
        self.modifier_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.supprimer_enseignat_button = Button(enseignant_bottom_frame, text="Supprimer l'enseignant", width=18, height=3, command=self.delete_enseignant, cursor="hand2")
        self.supprimer_enseignat_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.refresh_button = Button(enseignant_bottom_frame, text="Rafraîchir", width=8, height=3, command=self.refresh_enseignant, cursor="hand2")
        self.refresh_button.grid(row=0, column=3, padx=10, pady=10)
        
        ################## now here we go in the detail frame to the right of our GUI ################
        detail_frame = Frame(self.master, bd=2, relief=GROOVE, bg="#434448")
        detail_frame.place(x=0.35*screen_width, y=130, width=0.633*screen_width, height=560)
        
        recherche_label = Label(detail_frame, text="RECHERCHE AUTO PAR NOM OU PAR MAIL:", font=("ubuntu", 14, 'bold', 'underline'), bg='#434448', fg="white")
        recherche_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        self.recherche_entry = Entry(detail_frame, font=("Times new roman", 13), bd=2, relief=GROOVE, width=30)
        self.recherche_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        
        # DYNAMIQUE RECHERCHE
        self.recherche_entry.bind("<KeyRelease>", self.chercher_by)
        
        
       
        recherche_button = Button(detail_frame, text="Rechercher", width=10, cursor="hand2", command=self.chercher_by)
        #recherche_button.grid(row=0, column=2, pady=10, padx=10)
        
        afficher_tout_button = Button(detail_frame, text="Afficher tous les enseignants", width=22, cursor="hand2", command=self.afficher_enseignants)
        afficher_tout_button.grid(row=0, column=3, pady=10, padx=10)
        
        
        table_frame = Frame(detail_frame, bd=2, relief=GROOVE, bg="#434448")
        table_frame.place(x=10, y=50, width=0.626*screen_width, height=500)
        
            ##### scrolle bar ########
        scroll_bar_x = Scrollbar(table_frame, orient=HORIZONTAL)
        
        scroll_bar_y = Scrollbar(table_frame, orient=VERTICAL)
        
            ##### table that will display the data after registration, creat a view
        self.enseignant_table = ttk.Treeview(table_frame, columns=("Nom", "Prénom", "Téléphone", "Mail", "Formation enseignée", "Niveau"),
                                      xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)
        
            #### Place the scrollbars x and y 
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

            #### scroll bar command
        scroll_bar_x.config(command=self.enseignant_table.xview)
        scroll_bar_y.config(command=self.enseignant_table.yview)
        
            #### the text(title) colums headers that will be displayed 
        self.enseignant_table.heading("Nom", text="Nom")
        self.enseignant_table.heading("Prénom", text="Prénom")
        self.enseignant_table.heading("Mail", text="Email")
        self.enseignant_table.heading("Téléphone", text="Numéro de téléphone")
        self.enseignant_table.heading("Formation enseignée", text="Formation enseignée")
        self.enseignant_table.heading("Niveau", text="Niveau")
        
        #### Just show the heandings not something else 
        self.enseignant_table['show'] = 'headings'
        
        self.enseignant_table.column("Nom", width=80)
        self.enseignant_table.column("Prénom", width=100)
        self.enseignant_table.column("Mail", width=100)
        self.enseignant_table.column("Téléphone", width=100)
        self.enseignant_table.column("Formation enseignée", width=250)
        self.enseignant_table.column("Niveau", width=140)
        
            ##### Pack the treeview
        self.enseignant_table.pack(fill=BOTH, expand=TRUE)
        
        ## Fill in the data as soon as the application is opened with the
        self.afficher_enseignants()
        
        
        ### "ButtonRelease" is the type of event (button release), 
        # and -1 is the source of the event (the left mouse button)
        self.enseignant_table.bind("<ButtonRelease-1>", self.recup_selected_data)  ## ---> calling the recup_selected_data/ -->evenementiel programmation
        
         
 
     
    def recup_selected_data(self, event):  # sourcery skip: extract-method
        self.nom_enseignant_entry['state'] = 'normal'
        self.prenom_enseignant_entry['state'] = 'normal'
        
        selected_row = self.enseignant_table.focus()
        contain =self.enseignant_table.item(selected_row)
        
        row = contain['values'] ## row is a list that equal [enseignant data ]
        
        self.nom_enseignant_entry.delete(0, END)
        self.prenom_enseignant_entry.delete(0, END)
        self.tel_enseignant_entry.delete(0, END)
        self.mail_enseignant_entry.delete(0, END)
        self.intitule_formation_entry.delete(0, END)
        self.niveau_formation_entry.delete(0, END)
        
        if len(row):
            self.nom_enseignant_entry.insert(END, row[0])
            self.prenom_enseignant_entry.insert(END, row[1])
            self.tel_enseignant_entry.insert(END, row[2])
            self.mail_enseignant_entry.insert(END, row[3])
            self.intitule_formation_entry.insert(END, row[4])
            self.niveau_formation_entry.insert(END, row[5])
        
        self.nom_enseignant_entry['state'] = 'disabled'
        self.prenom_enseignant_entry['state'] = 'disabled'
     
     
    def enregistrer_enseignant(self):  
    # sourcery skip: extract-method, use-fstring-for-concatenation
        is_valide = validate_email(email=self.mail_enseignant_entry.get()) # --> to check if the entry email is valide
        
        champs = []
        if self.nom_enseignant_entry.get()  == "":
            champs.append(self.nom_enseignant_entry)
                
        if self.prenom_enseignant_entry.get() == "":
            champs.append(self.prenom_enseignant_entry)
           
        if self.niveau_formation_entry.get() == "":
            champs.append(self.niveau_formation_entry)
            
        if self.mail_enseignant_entry.get() == "":
            champs.append(self.mail_enseignant_entry)
            
        if self.tel_enseignant_entry.get() == "":
            champs.append(self.tel_enseignant_entry)
            
        if self.intitule_formation_entry.get() =="":
            champs.append(self.intitule_formation_entry)       
    
        # giving a bg to the empty label 'if exist ofcourse    
        if champs != []:
            for champ in champs:
                champ['bg'] = "#FF6F7D"
            messagebox.showerror("Erreur", "Les champs marqués par (*) sont obligatoires!")               
            champs.clear()                
            return champs 
        
        if not(is_valide): #--> checking if the entry email is valide
            messagebox.showerror("Erreur", "L'email saisi n'est pas valide!")
            self.mail_enseignant_entry['bg'] = "#FF6F7D" 
        else:
            bdd_file = "bdd/bdd_gestion_formation.db" 
            con = sqlite3.connect(bdd_file)
            cursor = con.cursor()
            
            nom_prenom = (self.nom_enseignant_entry.get(), self.prenom_enseignant_entry.get())
            query = "SELECT * FROM enseiignants WHERE nom_enseignant = ? AND prenom_enseignant = ?"
            cursor.execute(query, nom_prenom)
            
            if len(cursor.fetchall()) > 0:
                messagebox.showerror("Erreur", f"L'enseignant {self.nom_enseignant_entry.get()} existe déjà!")
            else:
                data = (self.nom_enseignant_entry.get(), self.prenom_enseignant_entry.get(), self.tel_enseignant_entry.get(), self.mail_enseignant_entry.get(), self.intitule_formation_entry.get(), self.niveau_formation_entry.get())
                requete = "INSERT INTO enseiignants(nom_enseignant, prenom_enseignant, tel_enseignant, mail_enseignant, intitule_formation, niveau_formation) VALUES (?,?,?,?,?,?)"
                cursor.execute(requete, data)
                
                con.commit()
                
                messagebox.showinfo("Enregistrement", f"Vous avez enregistré l'enseignant {self.nom_enseignant_entry.get()} avec succès!")
            cursor.close()
            con.close()
            
            
            self.refresh_enseignant()   
                #Fill in the data as soon as the application is opened with the
            self.afficher_enseignants() 
            
    
    def afficher_enseignants(self):
        bdd_file = "bdd/bdd_gestion_formation.db"
        con = sqlite3.connect(bdd_file)
        cursor = con.cursor()
        
        query = "SELECT * FROM enseiignants"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) > 0:
            self.enseignant_table.delete(*self.enseignant_table.get_children())
            
            for row in result:
                self.enseignant_table.insert('', END, values=row)
         
               
        self.recherche_entry.delete(0, END)
        
        self.nom_enseignant_entry['state'] = 'normal'
        self.prenom_enseignant_entry['state'] = 'normal'
        self.nom_enseignant_entry.delete(0, END)  
        self.prenom_enseignant_entry.delete(0, END)  
        self.tel_enseignant_entry.delete(0, END)  
        self.intitule_formation_entry.delete(0, END)  
        self.niveau_formation_entry.delete(0, END)
        self.mail_enseignant_entry.delete(0, END)   
        cursor.close()
        con.close()
        
    def modifier_enseignant(self):
        # sourcery skip: extract-method, inline-variable
        is_valide = validate_email(email=self.mail_enseignant_entry.get()) # --> to check if the entry email is valide
        
        champs = []
        if self.nom_enseignant_entry.get()  == "":
            champs.append(self.nom_enseignant_entry)
                
        if self.prenom_enseignant_entry.get() == "":
            champs.append(self.prenom_enseignant_entry)
           
        if self.niveau_formation_entry.get() == "":
            champs.append(self.niveau_formation_entry)
            
        if self.mail_enseignant_entry.get() == "":
            champs.append(self.mail_enseignant_entry)
            
        if self.tel_enseignant_entry.get() == "":
            champs.append(self.tel_enseignant_entry)
            
        if self.intitule_formation_entry.get() =="":
            champs.append(self.intitule_formation_entry)       
    
        # giving a bg to the empty label 'if exist ofcourse    
        if champs != []:
            for champ in champs:
                champ['bg'] = "#FF6F7D"
            messagebox.showerror("Erreur", "Veuillez sélectionner un enseignant avant!\nRassurez vous d'avoir rempli tous les champs!")               
            champs.clear()                
            return champs 
        
        if not(is_valide): #--> checking if the entry email is valide
            messagebox.showerror("Erreur", "L'email saisi n'est pas valide!")
            self.mail_enseignant_entry['bg'] = "#FF6F7D" 
        else:
            bdd_file = "bdd/bdd_gestion_formation.db" 
            con = sqlite3.connect(bdd_file)
            cursor = con.cursor()
            
            data = (self.tel_enseignant_entry.get(), self.mail_enseignant_entry.get(), self.intitule_formation_entry.get(), self.niveau_formation_entry.get(), self.nom_enseignant_entry.get(), self.prenom_enseignant_entry.get())
            requete = "UPDATE enseiignants SET tel_enseignant = ?, mail_enseignant=?, intitule_formation = ?, niveau_formation = ?  WHERE nom_enseignant=? AND prenom_enseignant=?"
            cursor.execute(requete, data)
                
            con.commit()
                
            messagebox.showinfo("Modification", f"Vous avez modifié les informations de {self.prenom_enseignant_entry.get()} {self.nom_enseignant_entry.get()}")
            cursor.close()
            con.close()
            
        self.refresh_enseignant()   
                #Fill in the data as soon as the application is opened with the
        self.afficher_enseignants() 
    
    def delete_enseignant(self):
        # sourcery skip: extract-method, inline-variable, last-if-guard
        if self.nom_enseignant_entry.get() != "":
            ask_to_delete = messagebox.askyesno("Suppression", f"Voulez vous vraiment supprimer\n{self.prenom_enseignant_entry.get()} {self.nom_enseignant_entry.get()} de la liste des enseignants?")

            if ask_to_delete > 0:
                bdd_file = "bdd/bdd_gestion_formation.db"
                con = sqlite3.connect(bdd_file)
                cursor = con.cursor()
                
                data = (self.nom_enseignant_entry.get(), self.prenom_enseignant_entry.get())
                query = "DELETE FROM enseiignants WHERE nom_enseignant = ? AND prenom_enseignant=?"
                
                cursor.execute(query, data)
                con.commit()
                
                cursor.close()
                con.close()
                
                messagebox.showinfo("Confirmation", f"Vous avez supprimé {self.prenom_enseignant_entry.get()} {self.nom_enseignant_entry.get()} avec succès!")
                
                self.refresh_enseignant()
                
                self.afficher_enseignants()
        else:
            messagebox.showerror("Sélection vide", "Vous devez sélectionner une ligne avant de cliquer sur supprimer!")
    
    def refresh_enseignant(self):
        self.nom_enseignant_entry['state'] = 'normal'
        self.prenom_enseignant_entry['state'] = 'normal'
        
        self.nom_enseignant_entry.delete(0, END)
        self.prenom_enseignant_entry.delete(0, END)
        self.tel_enseignant_entry.delete(0, END)
        self.mail_enseignant_entry.delete(0, END)
        self.niveau_formation_entry.delete(0, END)
        self.intitule_formation_entry.delete(0, END)
        
        # reset bg
        self.nom_enseignant_entry['bg'] = 'white'
        self.prenom_enseignant_entry['bg'] = 'white'
        self.tel_enseignant_entry['bg'] = 'white'
        self.mail_enseignant_entry['bg'] = 'white'
        self.niveau_formation_entry['bg'] = 'white'
        self.intitule_formation_entry['bg'] = 'white'
        
        self.afficher_enseignants()    
    
    def chercher_by(self,event):
        bdd_file = "bdd/bdd_gestion_formation.db" 
        con = sqlite3.connect(bdd_file)
        cursor = con.cursor()
        
        ## récup data in recherche_entry
        entree = self.recherche_entry.get()
        
        query = "SELECT * FROM enseiignants WHERE nom_enseignant = :entree_nom  or mail_enseignant = :entree_email"
        
        ## save it in a dict 
        cursor.execute(query, {'entree_nom': entree, 'entree_email':entree})
        
        result = cursor.fetchall()
        if len(result) > 0: ## if exist student in bdd
            ## delete all data before printing ...
            # * = decompress list or tuple 
            self.enseignant_table.delete(*self.enseignant_table.get_children()) ## get_children() Returns a tuple of children belonging to item
            for row in result:
                self.enseignant_table.insert('', END, values=row) ## we can insert this data in our detail table
        
    def gestion_formation(self):
        self.master.destroy()
        os.system("python GestionFormations.py")
    def gestion_etudiant(self):
        self.master.destroy()
        os.system("python GestionEtudiants.py")
    def gestion_inscription(self):
        self.master.destroy()
        os.system("python GestionInscription.py")        
        
        
 
 
 
 
 
 
     
        
master = Tk()

mon_app = GestionEnseignant(master=master)
master.iconbitmap("images/moi_2.ico")

'''img = PhotoImage(file="moi_2.png")
background_label = Label(master, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.lower()'''

master.mainloop()