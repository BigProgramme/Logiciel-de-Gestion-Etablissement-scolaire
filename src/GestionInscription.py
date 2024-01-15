""" 
    Author
    ------
    Saint Heraud MBOUMA 
    Date
    ----
    02/02/2023
"""
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from validate_email import validate_email
import sqlite3
from datetime import date



class GestionInscription:
    def __init__(self, root):
        self.root = root

        # setting title 
        self.root.title("Système de gestion d'un établissement de formation")

        #application  width and  height
        screen_width = root.winfo_screenwidth() #-->  get the sreen width and set it to the application
        screen_height = root.winfo_screenheight() #-->  get the sreen height and set it to the application

        # setting goemetry for the window to fit the screen size
        self.root.geometry("%dx%d"% (screen_width, screen_height))

        #back groung color
        self.root.configure(bg="#191970") # #434448

        # creat the title label window for students manage
        title_label = Label(self.root, text="GESTION DES INSCRIPTIONS", bd=2,
                    relief=GROOVE, font=("ubuntu", 20, "bold"), padx=20, bg="purple") # #0584FB
        title_label.pack(side=TOP, fill=X)


        ############ setting this variables as global ################ 
        global ine_etudiant_entry, ville_etudiant_entry, adresse_etudiant_entry, email_etudiant_entry, name_etudiant_entry, prenom_etudiant_entry, recherche_entry, formation_liste, desinscrire_button, detail_frame, recherche_formation_box
        ########============================================================================================################################################################################
        ##################################################
        # space frame for main menu  TOP#
        menu_frame = Frame(self.root, bd=2, relief=GROOVE, bg="#191970") # #323232
        menu_frame.place(x=20, y=50, width=0.97*screen_width, height=80)

        manage_formation_button = Button(menu_frame, text="GESTION DES FORMATIONS", font=("ubuntu", 13, 'bold'), width=25, height=2, cursor='hand2', command=self.gestion_formation, bg="#0584FB")
        manage_formation_button.grid(row=0, column=1, padx=10, pady=10)

        manage_etudiant_button = Button(menu_frame, bg="#DF73FF", text="GESTION DES ETUDIANTS", font=("ubuntu", 13, 'bold'), width=25, height=2, cursor='hand2', command=self.gestion_etudiant)
        manage_etudiant_button.grid(row=0, column=2, padx=10, pady=10)

        manage_enseignant_button = Button(menu_frame, text="GESTION DES ENSEIGNANTS", bg="#369c1a",font=("ubuntu", 13, 'bold'), width=25, height=2, cursor='hand2', command=self.gestion_enseignants)
        manage_enseignant_button.grid(row=0, column=3, padx=10, pady=10)



        # Frame for the formation data entry form  at the left of the screen#
        manage_frame = Frame(self.root, bd=2, relief=GROOVE, bg="#323232")
        manage_frame.place(x=20, y=130, width=0.32*screen_width, height=410)

        title_manage_frame = Label(manage_frame, text="INSCRIPTION A UNE FORMATION",
                      font=("ubuntu", 15, 'bold', "underline"), bg="#323232", fg="white")
        title_manage_frame.grid(row=0, columnspan=2, pady=15)

        ##### student data entry form ####
        ine_etudiant_label = Label(manage_frame, text="INE* : ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        ine_etudiant_label.grid(row=1, column=0, pady=10, sticky='w')

        ine_etudiant_entry = Entry(manage_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        ine_etudiant_entry.grid(row=1, column=1, padx= 10, pady=10, sticky='w')


        name_etudiant_label = Label(manage_frame, text="NOM* : ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        name_etudiant_label.grid(row=2, column=0, pady=10, sticky='w')

        name_etudiant_entry = Entry(manage_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        name_etudiant_entry.grid(row=2, column=1, padx= 10, pady=10, sticky='w')


        prenom_etudiant_label = Label(manage_frame, text="PRENOM* : ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        prenom_etudiant_label.grid(row=3, column=0, pady=10, sticky='w')

        prenom_etudiant_entry = Entry(manage_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        prenom_etudiant_entry.grid(row=3, column=1, padx= 10, pady=10, sticky='w')


        email_etudiant_label = Label(manage_frame, text="Email* : ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        email_etudiant_label.grid(row=4, column=0, pady=10, sticky='w')

        email_etudiant_entry = Entry(manage_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        email_etudiant_entry.grid(row=4, column=1, padx= 10, pady=10, sticky='w')


        ##### LISTE  DES FORMATIONS##### 
        formation_label = Label(manage_frame, text="Formations:",  font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        formation_label.grid(row=5, column=0, pady=10, sticky='w')


        
        formation_liste = ttk.Combobox(manage_frame, font=("ubuntu", 14, 'bold'))
        formation_liste['values'] = (self.get_formations())
        formation_liste.grid(row=5, column=1, padx=10, pady=10, sticky='w')


        #########################################################
        # buttons bottom manage_frame #
        button_manage_frame = Frame(manage_frame, bd=2, relief=GROOVE, bg="#323232")
        button_manage_frame.place(x=120, y=330, width=0.18*screen_width, height=70)

        inscrire_button = Button(button_manage_frame, text="Inscrire", width=8, height=3, command=self.inscrire_etudiant, cursor="hand2")
        inscrire_button.grid(row=0, column=1, padx=30, pady=5)

        
        desinscrire_button = Button(button_manage_frame, text="Désinscrire", width=8, height=3, command=self.desinscrire_etudiant, cursor="hand2")
        desinscrire_button.grid(row=0, column=2, padx=10, pady=10)


        ########================ FRAME D'AFFICHAGE DES FORMATIONS################
        formation_etudiant_frame = Frame(self.root, bd=2, relief=GROOVE, bg='#323232')
        formation_etudiant_frame.place(x=20, y=550, width=0.32*screen_width, height=220)

        formation_etudiant_label = Label(
            formation_etudiant_frame,
            text=f"FORMATIONS AUXQUELLES EST INSCRIT: {name_etudiant_entry.get()}",
            font=("ubuntu", 10, 'bold'),
            bg='#323232', 
            fg="white"
        )
        
        formation_etudiant_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
            
        
        formation_table_frame = Frame(formation_etudiant_frame, bd=2, relief=GROOVE, bg="#434448")
        formation_table_frame.place(x=5, y=50, width=0.31*screen_width, height=500)

        scroll_bar_x = Scrollbar(formation_table_frame, orient=HORIZONTAL)

        scroll_bar_y = Scrollbar(formation_table_frame, orient=VERTICAL)

        ##### table that will display the data after registration, creat a view
        self.formation_table = ttk.Treeview(formation_table_frame, columns=("code", "Intitule formation", "date_inscription"),
                                      xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)

        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x.config(command=self.formation_table.xview)
        scroll_bar_y.config(command=self.formation_table.yview)

        self.formation_table.heading("code", text="Code")
        self.formation_table.heading("Intitule formation", text="Intitulé de la formation")
        self.formation_table.heading("date_inscription", text="Date d'inscription")
    
        #### Just show the heandings not something else 
        self.formation_table['show'] = 'headings'

        self.formation_table.column("code", width=40)
        self.formation_table.column("Intitule formation", width=160)
        self.formation_table.column("date_inscription", width=70)
        
    
        self.formation_table.pack(fill=BOTH, expand=TRUE)

        ############====== right frame printing students data =============################  
        detail_frame = Frame(self.root, bd=2, relief=GROOVE, bg="#434448")
        detail_frame.place(x=0.35*screen_width, y=130, width=0.633*screen_width, height=650)

        recherche_label = Label(detail_frame, text="RECHERCHE AUTO PAR NOM OU PAR MAIL:", font=("ubuntu", 14, 'bold', 'underline'), bg='#434448', fg="white")
        recherche_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        recherche_entry = Entry(detail_frame, font=("Times new roman", 13), bd=2, relief=GROOVE, width=25)
        recherche_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        # DYNAMIQUE RECHERCHE (Auto)
        recherche_entry.bind("<KeyRelease>", self.chercher_by)



        ## On n'a plus besoin de ce button puisqu'on va faire une rechecher automatique
        recherche_button = Button(detail_frame, text="Rechercher", width=10, cursor="hand2", command=self.chercher_by)
        #recherche_button.grid(row=0, column=2, pady=10, padx=10)

        afficher_tout_button = Button(detail_frame, text="Afficher tous les étudiants", width=25, cursor="hand2", command=self.afficher_etudiants)
        afficher_tout_button.grid(row=0, column=2, pady=10, padx=10)
        
        
        formation_recherche_label = Label(detail_frame, text="RECHERCHE ETUDIANT PAR FORMATION:", font=("ubuntu", 14, 'bold', 'underline'), bg='#434448', fg="white")
        formation_recherche_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        
        

        recherche_formation_box = ttk.Combobox(detail_frame, font=("ubuntu", 14, 'bold', 'underline'))
        recherche_formation_box['values'] = (self.get_formations())
        recherche_formation_box.grid(row=1, column=1, pady=10, padx=5, sticky='w')
        
        # dynamique recherche
        #recherche_formation_box.bind("<KeyRelease>", self.chercher_par_formation)
        
        recherche_formation_button = Button(detail_frame, command=self.chercher_par_formation, text="Rechercher", width=10, cursor='hand2')
        recherche_formation_button.grid(row=1, column=2, padx=5, pady=10)        

        table_frame = Frame(detail_frame, bd=2, relief=GROOVE, bg="#434448")
        table_frame.place(x=10, y=100, width=0.626*screen_width, height=540)

        scroll_bar_x = Scrollbar(table_frame, orient=HORIZONTAL)

        scroll_bar_y = Scrollbar(table_frame, orient=VERTICAL)

        ##### table that will display the data after registration, creat a view
        self.etudiant_table = ttk.Treeview(table_frame, columns=("INE", "Nom", "Prénom", "Email", "Adresse", "Ville"),
                                      xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)

        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x.config(command=self.etudiant_table.xview)
        scroll_bar_y.config(command=self.etudiant_table.yview)

        self.etudiant_table.heading("INE", text="INE")
        self.etudiant_table.heading("Nom", text="Nom")
        self.etudiant_table.heading("Prénom", text="Prénom")
        self.etudiant_table.heading("Email", text="Email")
        self.etudiant_table.heading("Adresse", text="Adresse")
        self.etudiant_table.heading("Ville", text="Ville")

        #### Just show the heandings not something else 
        self.etudiant_table['show'] = 'headings'

        self.etudiant_table.column("INE", width=70)
        self.etudiant_table.column("Nom", width=100)
        self.etudiant_table.column("Prénom", width=100)
        self.etudiant_table.column("Email", width=100)
        self.etudiant_table.column("Adresse", width=250)
        self.etudiant_table.column("Ville", width=100)

        self.etudiant_table.pack(fill=BOTH, expand=TRUE)

        ## Fill in the data as soon as the application is opened with the
        self.afficher_etudiants()


        ### "ButtonRelease" is the type of event (button release), 
        # and -1 is the source of the event (the left mouse button)
        self.etudiant_table.bind("<ButtonRelease-1>", self.recup_selected_data)  ## ---> calling the recup_selected_data/ -->evenementiel programmation

    
    
    
    
    def inscrire_etudiant(self):  # sourcery skip: extract-method
        bdd_file = "bdd/bdd_gestion_formation.db" 
        con = sqlite3.connect(bdd_file)
        cursor = con.cursor()
        
        #verify is formation is selected or not
        if formation_liste.get() =="":
            messagebox.showerror("Erreur", "Veuillez choisir une formation!")
            
        #vérification si l'étudiant est déjà inscrit ou pas
        else:
            data1 = (ine_etudiant_entry.get(), formation_liste.get())
            query1 = "SELECT * FROM inscriptions WHERE ine_etudiant = ? and code_formation=?"
            cursor.execute(query1, data1)
            
            result1 = cursor.fetchall()
            
            if  len(result1) > 0:
                messagebox.showerror("Erreur", f"L'étudint ayant pour INE {ine_etudiant_entry.get()}\n est déjà inscrit(e) à la formation sélectionée!")
                '''elif  not(self.recup_selected_data(evenement=Event)): #ine_etudiant_entry.get() =="" or name_etudiant_entry.get() == "" or prenom_etudiant_entry.get() == "" or formation_liste.get()== "" or email_etudiant_entry.get() =="":  
                messagebox.showerror("Erreur", "Vous devez sélectionner un étudiant avant de l'ajouter à une formation!")''' 
            else:
                date_today = date.today()
                date_today_split = date_today.strftime("%d/%m/%y")
                
                data2 = (ine_etudiant_entry.get(), formation_liste.get(), date_today_split)
                
                query2 = "INSERT INTO inscriptions(ine_etudiant, code_formation, date_inscription) VALUES (?, ?, ?)"
                
                cursor.execute(query2, data2)             
                con.commit()
                
                
                messagebox.showinfo("INSCRIPTION", f"L'étudiant {name_etudiant_entry.get()}\na été inscrit(e) à la formation ayant pour code {formation_liste.get()} avec succès!")
                
                self.afficher_etudiants()
                
                self.afficher_formation_etudiant()
                
        cursor.close()
        con.close()
        
        
                
    
    def desinscrire_etudiant(self):  # sourcery skip: extract-method
        bdd_file = "bdd/bdd_gestion_formation.db"
        con = sqlite3.connect(bdd_file)
        cursor = con.cursor() 

        if formation_liste.get() =="":
            messagebox.showerror("Erreur", "Vous devez sélectionner une formation pour désinscrire un étudiant!")
        else:
            #on doit s'assurer que l'étudiant est bien inscrit à la bdd avant de le désinscrire
            data = (ine_etudiant_entry.get(), formation_liste.get())
            query = "SELECT * FROM  inscriptions WHERE ine_etudiant =? AND code_formation = ?"

            cursor.execute(query, data)

            result1 = cursor.fetchall()

            if len(result1) == 0: # vérifier si l'étudiant sélectionné est inscrit à la formation choisie
                messagebox.showerror("Erreur", f"Létudiant(e) {name_etudiant_entry.get()} n'est pas inscrit(e) à la formation choisie.\nVeuillez Choisir la formation à laquelle l'étudiant est inscrit!")
            else:
                yes_no = messagebox.askyesno("Désinscription", f"Voulez vous vraiment désinscrire cet étudiant à la formation {formation_liste.get()}?")
                if yes_no != 0:
                    query1 = "DELETE FROM inscriptions WHERE ine_etudiant = ? and code_formation = ?"

                    cursor.execute(query1, data)
                    con.commit()
                    
                    messagebox.showinfo("Confirmation de désinscription", f"La désinscription de l'étudiant {name_etudiant_entry.get()} à la formation\n {formation_liste.get()} a été effectuée avec succès!")

            self.afficher_formation_etudiant()
            #toujours fermé le cursor avant la connexion
        cursor.close()
        con.close()  
        
    def chercher_par_formation(self):
        bdd_file = "bdd/bdd_gestion_formation.db"
        con = sqlite3.connect(bdd_file)
        cursor = con.cursor() 

        if recherche_formation_box.get() =="":
            messagebox.showerror("Erreur", "Vous devez sélectionner une formation dans la liste!")
        else:
            data = (recherche_formation_box.get(),)
            query = """ 
                        SELECT etudiants.ine_etudiant, etudiants.nom_etudiant, etudiants.prenom_etudiant,
                        etudiants.email_etudiant, etudiants.adresse, etudiants.ville
                        From etudiants inner Join
                        inscriptions ON 
                        etudiants.ine_etudiant  = inscriptions.ine_etudiant
                        AND inscriptions.code_formation = ? 
                    """
            cursor.execute(query, data)
            result = cursor.fetchall()
            if len(result) > 0 :
                self.etudiant_table.delete(*self.etudiant_table.get_children())
                for line in result:
                    self.etudiant_table.insert('', END, values=line)
            else:
                messagebox.showinfo("Résultat de recherche", "Il n'existe aucun étudiant inscrit à la formation choisie!")
            
            
        cursor.close()
        con.close()
            
    def afficher_formation_etudiant(self): ## 
        bdd_file = "bdd/bdd_gestion_formation.db" 
        con = sqlite3.connect(bdd_file)
        cursor = con.cursor()  
        
        data = (ine_etudiant_entry.get(),)
        
        query = """SELECT f.code_formation, f.intitule_formation, i.date_inscription 
        FROM ((formations AS f INNER JOIN inscriptions AS i ON f.code_formation = i.code_formation) 
        INNER JOIN etudiants AS e ON e.ine_etudiant = i.ine_etudiant  AND i.ine_etudiant = ?)"""
        
        cursor.execute(query, data)
        result = cursor.fetchall()
        
        if len(result) > 0:
            #il faut d'abor supprimer le contenu de la table avant l'insertion
            self.formation_table.delete(*self.formation_table.get_children())  #decompresse
            
            #NOW insert result values in formation table
            for line in result:
                self.formation_table.insert('', END, values=line)
            
            cursor.close()
            con.close()
            
          
    def chercher_by(self, event):
        bdd_file = "bdd/bdd_gestion_formation.db" 
        con = sqlite3.connect(bdd_file)
        cursor = con.cursor()
        
        ## récup data in recherche_entry
        entree = recherche_entry.get()
        
        query = "SELECT * FROM etudiants WHERE nom_etudiant = :entree_nom or email_etudiant = :entree_email"
        
        ## save it in a dict 
        my_dict= {'entree_nom': entree, 'entree_email':entree}
        cursor.execute(query, my_dict)
        
        result = cursor.fetchall()
        if len(result) > 0: ## if exist student in bdd
            ## delete all data before printing ...
            # * = decompress list or tuple 
            self.etudiant_table.delete(*self.etudiant_table.get_children()) ## get_children() Returns a tuple of children belonging to item
            for row in result: ##---->  insert 
                self.etudiant_table.insert('', END, values=row) ## we can insert this data in our detail table
        else:
            #messagebox.showinfo("Recherche", "Cet étudiant n'existe pas.\nRassurez vous d'avoir tapé un NOM ou une ADRESSE MAIL valide!")
        
        ## close connection to db after operations
            cursor.close()
            con.close()
        
    
    def afficher_etudiants(self):
        bdd_file = "bdd/bdd_gestion_formation.db" 
        con = sqlite3.connect(bdd_file)
        cursor = con.cursor()
        
        query = "SELECT * FROM etudiants"
        cursor.execute(query)
        
        result = cursor.fetchall()
        
        if len(result) > 0: ## if exist student in bdd
            ## delete all data before printing ...
            # * = decompress list or tuple 
            self.etudiant_table.delete(*self.etudiant_table.get_children()) ## get_children() Returns a tuple of children belonging to item
            for row in result:
                self.etudiant_table.insert('', END, values=row) ## we can insert this data in our detail table
                
        ## close connection to db after operations
        cursor.close()
        con.close()
    
    def get_formations(self):
        bdd_file = "bdd/bdd_gestion_formation.db"
        con = sqlite3.connect(bdd_file)
        cursor = con.cursor()

        query = "SELECT * FROM formations"
        cursor.execute(query)

        result = [data[0] for data in cursor]  ## ---> data[0] is code_formation in formations table
        
        cursor.close()
        con.close()
        return result
    
    def recup_selected_data(self,evenement):  # sourcery skip: extract-duplicate-method, extract-method
        #debock ine_entry:
        ine_etudiant_entry['state'] = 'normal' ### ---> deblock the ine entry 
        name_etudiant_entry['state'] = 'normal'
        prenom_etudiant_entry['state'] = 'normal'
        email_etudiant_entry['state'] = 'normal'
        
        selected_row = self.etudiant_table.focus() ## ----> get a select data in student table detail
        contain = self.etudiant_table.item(selected_row) # return a dict with a selected values
        
        row = contain['values'] ## row is a list that equal ["ine", "name", "prenom", "mail", "adresse", "ville"]
        
        ## delete all before inserting
        ine_etudiant_entry.delete(0, END)
        name_etudiant_entry.delete(0, END)
        prenom_etudiant_entry.delete(0, END)
        email_etudiant_entry.delete(0, END)
         
        ## insert data but checking if exist data before insertion
        if len(row): 
            ine_etudiant_entry.insert(END, row[0])
            name_etudiant_entry.insert(END, row[1])
            prenom_etudiant_entry.insert(END, row[2])
            email_etudiant_entry.insert(END, row[3])
            
        
        ine_etudiant_entry['state'] = 'disabled' ### ---> block the ine entry cause we can'not change it
        name_etudiant_entry['state'] = 'disabled'
        prenom_etudiant_entry['state'] = 'disabled'
        email_etudiant_entry['state'] = 'disabled'
        
        
        self.formation_table.delete(*self.formation_table.get_children())
        self.afficher_formation_etudiant()
    
    def gestion_formation(self):
        self.root.destroy()
        os.system('python GestionFormations.py')
    def gestion_enseignants(self):
        self.root.destroy()
        os.system("python GestionEnseignant.py")
    def gestion_etudiant(self):
        self.root.destroy()
        os.system("python GestionEtudiants.py")
   
   
   
   
   
   
   
   
root = Tk()
application = GestionInscription(root=root)


'''bar_theme_menu = Menu()
root.config(menu=bar_theme_menu)
        
theme_menu = Menu(bar_theme_menu, font=("arial, 12"), tearoff=False) # tearoff == NE pas détacher le menu 
def col():
    root.config(bg='white')
def black():
    root.config(bg="#191970")
theme_menu.add_command(label="white", command=col)
theme_menu.add_command(label='black', command=black)
        
bar_theme_menu.add_cascade(label="Thèmes", menu=theme_menu)'''

root.mainloop()