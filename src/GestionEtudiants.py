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



class GestionEtudiants:
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
        title_label = Label(self.root, text="GESTION DES ETUDIANTS", bd=2,
                    relief=GROOVE, font=("ubuntu", 20, "bold"), padx=20, bg="#DF73FF") # #0584FB
        title_label.pack(side=TOP, fill=X)
        
        
        ############ setting this variables as global ################ 
        global ine_etudiant_entry, ville_etudiant_entry, adresse_etudiant_entry, email_etudiant_entry, name_etudiant_entry, prenom_etudiant_entry, recherche_entry
        
        ##################################################
        # space frame for main menu  TOP#
        menu_frame = Frame(self.root, bd=2, relief=GROOVE, bg="#191970") # #323232
        menu_frame.place(x=20, y=50, width=0.97*screen_width, height=80)
        
        manage_formation_button = Button(menu_frame, text="GESTION DES FORMATIONS", font=("ubuntu", 13, 'bold'), width=25, height=2, cursor='hand2', command=self.gestion_formation, bg="#0584FB")
        manage_formation_button.grid(row=0, column=1, padx=10, pady=10)
        
        manage_inscription_button = Button(menu_frame, bg="purple", text="GESTION DES INSCRIPTIONS", font=("ubuntu", 13, 'bold'), width=25, height=2, cursor='hand2', command=self.gestion_inscription)
        manage_inscription_button.grid(row=0, column=2, padx=10, pady=10)
        
        manage_enseignant_button = Button(menu_frame, text="GESTION DES ENSEIGNANTS", bg="#369c1a", font=("ubuntu", 13, 'bold'), width=25, height=2, cursor='hand2', command=self.gestion_enseignants)
        manage_enseignant_button.grid(row=0, column=3, padx=10, pady=10)
        
        
        
        # Frame for the students data entry form  at the left of the screen#
        manage_frame = Frame(self.root, bd=2, relief=GROOVE, bg="#323232")
        manage_frame.place(x=20, y=130, width=0.32*screen_width, height=560)
        
        title_manage_frame = Label(manage_frame, text="INFORMATIONS SUR LES ETUDIANTS",
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
        
        
        adresse_etudiant_label = Label(manage_frame, text="Adresse* : ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        adresse_etudiant_label.grid(row=5, column=0, pady=10, sticky='w')
        
        adresse_etudiant_entry = Text(manage_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30, height=3)
        adresse_etudiant_entry.grid(row=5, column=1, padx= 10, pady=10, sticky='w')
        
        
        
        ville_etudiant_label = Label(manage_frame, text="VILLE* : ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        ville_etudiant_label.grid(row=6, column=0, pady=10, sticky='w')
        
        ville_etudiant_entry = Entry(manage_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        ville_etudiant_entry.grid(row=6, column=1, padx= 10, pady=10, sticky='w')
        
        
        
        #########################################################
        # buttons bottom manage_frame #
        button_manage_frame = Frame(manage_frame, bd=2, relief=GROOVE, bg="#323232")
        button_manage_frame.place(x=15, y=450, width=0.27*screen_width, height=80)
        
        register_button = Button(button_manage_frame, text="Enregistrer", width=8, height=3, command=self.enregistrer_etudiant, cursor="hand2")
        register_button.grid(row=0, column=0, padx=10, pady=10)
        
        global modifier_button, detail_frame
        modifier_button = Button(button_manage_frame, text="Modifier", width=8, height=3, command=self.modifier_etudiant, cursor="hand2")
        modifier_button.grid(row=0, column=1, padx=10, pady=10)
        
        supprimer_student_button = Button(button_manage_frame, text="Supprimer l'étudiant", width=16, height=3, command=self.delete_etudiant, cursor="hand2")
        supprimer_student_button.grid(row=0, column=2, padx=10, pady=10)
        
        refresh_student_button = Button(button_manage_frame, text="Rafraîchir", width=11, height=3, command=self.refresh_etudiant, cursor="hand2")
        refresh_student_button.grid(row=0, column=3, padx=10, pady=10)
        
        
        
        ############ right frame printing students data ################  
        detail_frame = Frame(self.root, bd=2, relief=GROOVE, bg="#434448")
        detail_frame.place(x=0.35*screen_width, y=130, width=0.633*screen_width, height=560)
        
        recherche_label = Label(detail_frame, text="RECHERCHE AUTO PAR NOM OU PAR MAIL:", font=("ubuntu", 14, 'bold', 'underline'), bg='#434448', fg="white")
        recherche_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        recherche_entry = Entry(detail_frame, font=("Times new roman", 13), bd=2, relief=GROOVE, width=30)
        recherche_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        
        # DYNAMIQUE RECHERCHE
        recherche_entry.bind("<KeyRelease>", self.chercher_by)
        
        
       
        recherche_button = Button(detail_frame, text="Rechercher", width=10, cursor="hand2", command=self.chercher_by)
        #recherche_button.grid(row=0, column=2, pady=10, padx=10)
        
        afficher_tout_button = Button(detail_frame, text="Afficher tous les étudiants", width=20, cursor="hand2", command=self.afficher_etudiants)
        afficher_tout_button.grid(row=0, column=3, pady=10, padx=10)
        
        
        table_frame = Frame(detail_frame, bd=2, relief=GROOVE, bg="#434448")
        table_frame.place(x=10, y=50, width=0.626*screen_width, height=500)
        
            ##### scrolle bar ########
        scroll_bar_x = Scrollbar(table_frame, orient=HORIZONTAL)
        
        scroll_bar_y = Scrollbar(table_frame, orient=VERTICAL)
        
            ##### table that will display the data after registration, creat a view
        self.etudiant_table = ttk.Treeview(table_frame, columns=("INE", "Nom", "Prénom", "Email", "Adresse", "Ville"),
                                      xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)
        
            #### Place the scrollbars x and y 
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

            #### scroll bar command
        scroll_bar_x.config(command=self.etudiant_table.xview)
        scroll_bar_y.config(command=self.etudiant_table.yview)
        
            #### the text(title) colums headers that will be displayed 
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
        
            ##### Pack the treeview
        self.etudiant_table.pack(fill=BOTH, expand=TRUE)
        
        ## Fill in the data as soon as the application is opened with the
        self.afficher_etudiants()
        
        
        ### "ButtonRelease" is the type of event (button release), 
        # and -1 is the source of the event (the left mouse button)
        self.etudiant_table.bind("<ButtonRelease-1>", self.recup_selected_data)  ## ---> calling the recup_selected_data/ -->evenementiel programmation
   

   
    ############# METHODES ############## 
    def recup_selected_data(self, event):  # sourcery skip: extract-method
        #debock ine_entry:
        ine_etudiant_entry['state'] = 'normal'
        
        selected_row = self.etudiant_table.focus() ## ----> get a select data in student table detail
        contain = self.etudiant_table.item(selected_row) # return a dict with a selected values
        
        row = contain['values'] ## row is a list that equal ["ine", "name", "prenom", "mail", "adresse", "ville"]
        
        ## delete all before inserting
        ine_etudiant_entry.delete(0, END)
        name_etudiant_entry.delete(0, END)
        prenom_etudiant_entry.delete(0, END)
        email_etudiant_entry.delete(0, END)
        adresse_etudiant_entry.delete('1.0', END)
        ville_etudiant_entry.delete(0, END)
        
        ## insert data but checking if exist data before insertion
        if len(row): 
            ine_etudiant_entry.insert(END, row[0])
            name_etudiant_entry.insert(END, row[1])
            prenom_etudiant_entry.insert(END, row[2])
            email_etudiant_entry.insert(END, row[3])
            adresse_etudiant_entry.insert(END, row[4])
            ville_etudiant_entry.insert(END, row[5])
            
        
        
        ine_etudiant_entry['state'] = 'disabled' ### ---> block the ine entry cause we can'not change it
        
        
    def enregistrer_etudiant(self):  # sourcery skip: extract-method, use-fstring-for-concatenation
        is_valide = validate_email(email=email_etudiant_entry.get()) # --> to check if the entry email is valide
        
        champs = []
        if ine_etudiant_entry.get()  == "":
            champs.append(ine_etudiant_entry)
                
        if name_etudiant_entry.get() == "":
            champs.append(name_etudiant_entry)
            
        if prenom_etudiant_entry.get() == "":
            champs.append(prenom_etudiant_entry)
            
        if email_etudiant_entry.get() == "":
            champs.append(email_etudiant_entry)
                
        if len(adresse_etudiant_entry.get(1.0, END + '-1c')) == 0:
            champs.append(adresse_etudiant_entry)
            
        if ville_etudiant_entry.get() == "":
            champs.append(ville_etudiant_entry)
        
        # giving a bg to the empty label 'if exist ofcourse    
        if champs != []:
            for champ in champs:
                champ['bg'] = "#FF0000"
                
            messagebox.showerror("Erreur", "Les champs marqués par (*) sont obligatoires!")               
            champs.clear()                
            return champs 
        
        if not(is_valide): #--> checking if the entry email is valide
            messagebox.showerror("Erreur", "L'email saisi n'est pas valide!")
            email_etudiant_entry['bg'] = "#FF0000"
            
        else:
           bdd_file = "bdd/bdd_gestion_formation.db" 
           con = sqlite3.connect(bdd_file)
           cursor = con.cursor()
           
           ########### ATTENTION ###############
           n = ine_etudiant_entry.get()
           ine_query = "SELECT* FROM etudiants WHERE ine_etudiant = :ine"
           cursor.execute(ine_query, {'ine' : n}) # --> dict
           
           result = cursor.fetchall()
           ########### ATTENTION ###############
            
           if len(result) > 0:
               messagebox.showerror("Erreur", "Un étudiant existe déjà avec ce numéro INE!")
           else:
                student_data = (ine_etudiant_entry.get(), name_etudiant_entry.get(), prenom_etudiant_entry.get(), email_etudiant_entry.get(), adresse_etudiant_entry.get(1.0, END), ville_etudiant_entry.get())
                query = "INSERT INTO etudiants(ine_etudiant, nom_etudiant, prenom_etudiant, email_etudiant, adresse, ville) VALUES (?, ?, ?, ?, ?, ?)"
                cursor.execute(query, student_data)
                
                con.commit()
                cursor.close()
                con.close()
                
                messagebox.showinfo("Enregistrement de l'étudiant", f"Enregistrement de l'étudiant {name_etudiant_entry.get()} {prenom_etudiant_entry.get()} a été effectué avec succes! ")
                
                self.refresh_etudiant()
                
                #Fill in the data as soon as the application is opened with the
                self.afficher_etudiants()
                
            
            
    def modifier_etudiant(self):  # sourcery skip: extract-method, inline-variable, use-fstring-for-concatenation
        is_valide = validate_email(email=email_etudiant_entry.get()) # --> to check if the entry email is valide
        
        champs = []        
        if name_etudiant_entry.get() == "":
            champs.append(name_etudiant_entry)
            
        if prenom_etudiant_entry.get() == "":
            champs.append(prenom_etudiant_entry)
            
        if email_etudiant_entry.get() == "":
            champs.append(email_etudiant_entry)
                
        if len(adresse_etudiant_entry.get(1.0, END + '-1c')) == 0:
            champs.append(adresse_etudiant_entry)
            
        if ville_etudiant_entry.get() == "":
            champs.append(ville_etudiant_entry)
        
        # giving a bg to the empty label 'if exist ofcourse    
        if champs != [] and modifier_button:
            for champ in champs:
                champ['bg'] = "#FF0000"
                
            messagebox.showerror("Erreur", "Veuillez sélectionner un étudiant avant!\nRassurez vous d'avoir tout rempli.")
            
            champs.clear()                
            return champs 
        
        if not(is_valide): #--> checking if the entry email is valide
            messagebox.showerror("Erreur", "L'email saisi n'est pas valide!")
            email_etudiant_entry['bg'] = "#FF0000"
            
        else:
           bdd_file = "bdd/bdd_gestion_formation.db" 
           con = sqlite3.connect(bdd_file)
           cursor = con.cursor()
           
           ########### ATTENTION ###############
           get_ine = ine_etudiant_entry.get()
           get_email = email_etudiant_entry.get()
           ine_query = "SELECT* FROM etudiants WHERE ine_etudiant <> :ine AND email_etudiant = :email"
           cursor.execute(ine_query, {'ine' : get_ine, 'email':get_email}) # --> dict
           
           result = cursor.fetchall()
           ########### ATTENTION ###############
            
            # can't change email with this block 
           '''if len(result) > 0:
               messagebox.showerror("Erreur", "Un étudiant existe déjà avec l'adresse email saisie!")
           else:
               
                student_data = (name_etudiant_entry.get(), prenom_etudiant_entry.get(), email_etudiant_entry.get(), adresse_etudiant_entry.get(1.0, END), ville_etudiant_entry.get(), ine_etudiant_entry.get())
                query = "UPDATE etudiants SET nom_etudiant = ?, prenom_etudiant = ?, email_etudiant = ?, adresse = ?, ville = ? WHERE ine_etudiant = ?"
                cursor.execute(query, student_data)
                
                con.commit()
                cursor.close()
                con.close()
                
                messagebox.showinfo("Modification d'un étudiant", f"La modification de l'étudiant {name_etudiant_entry.get()} {prenom_etudiant_entry.get()} a été effectué avec succes! ")
                
                self.refresh_etudiant()
                
                #Fill in the data as soon as the application is opened with the
                self.afficher_etudiants()'''
                
        ### we need to change email too, so check this block code 
        student_data = (name_etudiant_entry.get(), prenom_etudiant_entry.get(), email_etudiant_entry.get(), adresse_etudiant_entry.get(1.0, END), ville_etudiant_entry.get(), ine_etudiant_entry.get())
        query = "UPDATE etudiants SET nom_etudiant = ?, prenom_etudiant = ?, email_etudiant = ?, adresse = ?, ville = ? WHERE ine_etudiant = ?"
        cursor.execute(query, student_data)
                
        con.commit()
        cursor.close()
        con.close()
                
        messagebox.showinfo("Modification d'un étudiant", f"La modification de l'étudiant {name_etudiant_entry.get()} {prenom_etudiant_entry.get()} a été effectué avec succes! ")
                
        #refresh data
        self.refresh_etudiant()        
        #Fill in the data as soon as the application is opened with the
        self.afficher_etudiants()
        
        
        
    def delete_etudiant(self):
        # sourcery skip: extract-method, hoist-statement-from-if, inline-variable, remove-pass-body
        #check firstly if  one student is selected before delete him just with the ine_entry
        if ine_etudiant_entry.get() != "":
            
            ask_to_delete=  messagebox.askyesno("Suppression", f"Voulez vous vraiment supprimer\n{name_etudiant_entry.get()} {prenom_etudiant_entry.get()} de la base de données?")
            ### messagebox.askyesno provides to values 'YES' = 1 and 'NO' = 0
            ## so if user press in the 'YES' Button, that means 1 or > 0. --->

            if ask_to_delete > 0: ### if it's 'YES' then we can delete else,  nothing will happen.
                bdd_file = "bdd/bdd_gestion_formation.db"
                con = sqlite3.connect(bdd_file)
                cursor = con.cursor()

                data_to_delete = (ine_etudiant_entry.get(),)
                query = "DELETE FROM etudiants WHERE ine_etudiant = ?"

                cursor.execute(query, data_to_delete)
                con.commit()

                #close db
                cursor.close()
                con.close()

                messagebox.showinfo("Confirmation", f"l'étudiant {name_etudiant_entry.get()} {prenom_etudiant_entry.get()}\na bien été supprimé(e)")
                ### again this methods, you know what they 
                self.refresh_etudiant()
                self.afficher_etudiants()
        else:
            messagebox.showerror("Sélection vide", "Vous devez sélectionner un étudiant avant")
    
    
    def refresh_etudiant(self):
        ##deblock ine_etudiant
        ine_etudiant_entry['state'] = 'normal'
        
        ine_etudiant_entry.delete(0, END)
        name_etudiant_entry.delete(0, END)
        prenom_etudiant_entry.delete(0, END)
        email_etudiant_entry.delete(0, END)
        ville_etudiant_entry.delete(0, END)
        adresse_etudiant_entry.delete(1.0, END) ## this is an text area, not an Entry 
        
        #
        ine_etudiant_entry.focus_set()
        
        
        #reset bg 
        ine_etudiant_entry['bg'] = "white"
        name_etudiant_entry['bg'] = "white"
        prenom_etudiant_entry['bg'] = "white"
        email_etudiant_entry['bg'] = "white"
        ville_etudiant_entry['bg'] = "white"
        adresse_etudiant_entry['bg'] = "white"
        
        #deselect with this
        self.afficher_etudiants()
        
        
        
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
            for row in result:
                self.etudiant_table.insert('', END, values=row) ## we can insert this data in our detail table
        else:
            #messagebox.showinfo("Recherche", "Cet étudiant n'existe pas.\nRassurez vous d'avoir tapé un NOM ou une ADRESSE MAIL valide!")
        
        ## close connection to db after operations
            cursor.close()
            con.close()
        
    def afficher_etudiants(self):  # sourcery skip: extract-method
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
            
            recherche_entry.delete(0,END)
            
            ine_etudiant_entry['state'] = 'normal'
            ine_etudiant_entry.delete(0, END)
            prenom_etudiant_entry.delete(0, END)
            name_etudiant_entry.delete(0, END)
            email_etudiant_entry.delete(0, END)
            adresse_etudiant_entry.delete(1.0, END)
            ville_etudiant_entry.delete(0, END)
       
        ## close connection to db after operations
        cursor.close()
        con.close()
    
    def gestion_formation(self):
        self.root.destroy()
        os.system("python GestionFormations.py")
    def gestion_inscription(self):
        self.root.destroy()
        os.system("python GestionInscription.py")
    def gestion_enseignants(self):
        self.root.destroy()
        os.system("python GestionEnseignant.py")
    
        
root = Tk()
application = GestionEtudiants(root=root)


bar_theme_menu = Menu()
root.config(menu=bar_theme_menu)
        
theme_menu = Menu(bar_theme_menu, font=("arial, 12"), tearoff=False) # tearoff == NE pas détacher le menu 
def col():
    root.config(bg='white')
def black():
    root.config(bg="#191970")
theme_menu.add_command(label="white", command=col)
theme_menu.add_command(label='black', command=black)
        
bar_theme_menu.add_cascade(label="Thèmes", menu=theme_menu)

root.mainloop()