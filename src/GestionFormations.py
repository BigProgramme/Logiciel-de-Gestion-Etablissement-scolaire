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
import sqlite3
from tkinter import messagebox


class GestionFormations:
    def __init__(self, master):
        self.master = master
        
        ## set the title
        self.master.title("Système de gestion d'un établissement de formation")
        
        ## width and height for our application
        
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight() #-->  get the sreen height and set it to the application

        ## setting geometry 
        self.master.geometry("%dx%d"% (screen_width, screen_height))
        
        ## back ground 
        self.master.config(bg="#434448")
        
        ## title lable
        title_label =Label(self.master, text="GESTION DES FORMATIONS", bd=2,
                           relief=GROOVE, font=("ubuntu", 20, "bold"), padx=20, bg="#0584FB")
        title_label.pack(side=TOP, fill=X)
        
        global code_formation_entry, intitule_formation_entry, langue_formation_entry, niveau_formation_entry, objectif_formation_entry
        
      # space frame for main menu  TOP#
        menu_frame = Frame(self.master, bd=2, relief=GROOVE, bg="#323232") # #323232
        menu_frame.place(x=20, y=50, width=0.97*screen_width, height=80)
        
        manage_etudiant_button = Button(menu_frame, text="GESTION DES ETUDIANTS", font=("ubuntu", 13, 'bold'), width=25, height=2, cursor='hand2', bg="#DF73FF", command=self.gestion_etudiant)
        manage_etudiant_button.grid(row=0, column=1, padx=10, pady=10)
        
        manage_inscription_button = Button(menu_frame, text="GESTION DES INSCRIPTIONS", font=("ubuntu", 13, 'bold'), width=25, height=2, cursor='hand2', bg="purple", command=self.gestion_inscription)
        manage_inscription_button.grid(row=0, column=2, padx=10, pady=10)
        
        manage_enseignant_button = Button(menu_frame, text="GESTION DES ENSEIGNANTS", font=("ubuntu", 13, 'bold'), width=25, height=2, cursor='hand2', bg="#369c1a",command=self.gestion_enseignants)
        manage_enseignant_button.grid(row=0, column=3, padx=10, pady=10)
  
        
        # Frame for the formations data entry form  at the left of the screen#
        manage_formation_frame = Frame(self.master, bd=2, relief=GROOVE, bg="#323232")
        manage_formation_frame.place(x=20, y=130, width=0.32*screen_width, height=560)
        
        title_manage_formation_frame_label = Label(manage_formation_frame, text="Informations sur les formations",
                                            font=("ubuntu", 15, 'bold', "underline"), bg="#323232", fg="white")
        title_manage_formation_frame_label.grid(row=0,columnspan=2, pady=15)
  
  
        ############ Formation data ###############
        code_formation_label = Label(manage_formation_frame, text="CODE FORMATION*: ", font=("ubuntu", 12, 'bold'), bg="#323232", fg="white")
        code_formation_label.grid(row=1, column=0, pady=10, sticky='w')
        
        code_formation_entry = Entry(manage_formation_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        code_formation_entry.grid(row=1, column=1, padx= 10, pady=10, sticky='w')
        
        
        intitule_formation_label = Label(manage_formation_frame, text="Intitulé*: ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        intitule_formation_label.grid(row=2, column=0, pady=10, sticky='w')
        
        intitule_formation_entry = Entry(manage_formation_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        intitule_formation_entry.grid(row=2, column=1, padx= 10, pady=10, sticky='w')
        
        langue_formation_label =  Label(manage_formation_frame, text="Langue* : ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        langue_formation_label.grid(row=3, column=0, pady=10, sticky='w')
        
        langue_formation_entry = Entry(manage_formation_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        langue_formation_entry.grid(row=3, column=1, padx= 10, pady=10, sticky='w')
        
        niveau_formation_label = Label(manage_formation_frame, text="Niveau* : ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        niveau_formation_label.grid(row=4, column=0, pady=10, sticky='w')
        
        niveau_formation_entry = Entry(manage_formation_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30)
        niveau_formation_entry.grid(row=4, column=1, padx= 10, pady=10, sticky='w')
        
        objectif_formation_label = Label(manage_formation_frame, text="Objectifs : ", font=("ubuntu", 14, 'bold'), bg="#323232", fg="white")
        objectif_formation_label.grid(row=5, column=0, pady=10, sticky='w')
        
        objectif_formation_entry = Text(manage_formation_frame, font=('Times new roman', 13), bd=2, 
                                   relief=GROOVE, width=30, height=3)
        objectif_formation_entry.grid(row=5, column=1, padx= 10, pady=10, sticky='w')




        #########################################################
        # buttons bottom manage_frame #
        button_manage_formation_frame = Frame(manage_formation_frame, bd=2, relief=GROOVE, bg="#323232")
        button_manage_formation_frame.place(x=15, y=450, width=0.27*screen_width, height=80)
        
        register_button = Button(button_manage_formation_frame, text="Enregistrer", width=8, height=3, command=self.enregistrer_formation, cursor="hand2")
        register_button.grid(row=0, column=0, padx=10, pady=10)
       
        global  modifier_button
        modifier_button = Button(button_manage_formation_frame, text="Modifier", width=8, height=3, command=self.modifier_formation, cursor="hand2")
        modifier_button.grid(row=0, column=1, padx=10, pady=10)
        
        supprimer_student_button = Button(button_manage_formation_frame, text="Supprimer la formation", width=17, height=3, command=self.delete_formation, cursor="hand2")
        supprimer_student_button.grid(row=0, column=2, padx=10, pady=10)
        
        refresh_student_button = Button(button_manage_formation_frame, text="Rafraîchir", width=9, height=3, command=self.refresh_formation, cursor="hand2")
        refresh_student_button.grid(row=0, column=3, padx=10, pady=10)




        ########### RIGHT FRAME ################
        detail_frame = Frame(self.master, bd=2, relief=GROOVE, bg="#434448")
        detail_frame.place(x=0.35*screen_width, y=130, width=0.633*screen_width, height=560)
        
        recherche_label = Label(detail_frame, text="RECHERCHE AUTO PAR INTITULE OU PAR CODE:", font=("ubuntu", 14, 'bold', 'underline'), bg='#434448', fg="white")
        recherche_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        self.recherche_entry = Entry(detail_frame, font=("Times new roman", 13), bd=2, relief=GROOVE, width=23)
        self.recherche_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        
        
        
        # DYNAMIQUE RECHERCHE
        self.recherche_entry.bind("<KeyRelease>", self.chercher_by)
        
        recherche_button = Button(detail_frame, text="Rechercher", width=10, cursor="hand2", command=self.chercher_by)
        '''recherche_button.grid(row=0, column=2, pady=10, padx=10)'''
        
        
        afficher_tout_button = Button(detail_frame, text="Afficher toutes les formations", width=25, cursor="hand2", command=self.afficher_formation)
        afficher_tout_button.grid(row=0, column=3, pady=10, padx=10)
        
        #### the frame that will be contain the table ########
        table_frame = Frame(detail_frame, bd=2, relief=GROOVE, bg="#434448")
        table_frame.place(x=10, y=50, width=0.626*screen_width, height=500)
        
        ##### scrolle bar ########
        scroll_bar_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_bar_y = Scrollbar(table_frame, orient=VERTICAL)
        
         ##### table that will display the data after registration, creat a view
         
        self.formation_table = ttk.Treeview(table_frame, columns=("Code Formation", "Intitulé formation", "Langue Formation", "Niveau Formation", "Objectif Formation"),
                                      xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)
        
        #### Place the scrollbars x and y 
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)
        
        #### scroll bar command
        scroll_bar_x.config(command=self.formation_table.xview)
        scroll_bar_y.config(command=self.formation_table.yview)
        
        
        
        #### the text(title) colums headers that will be displayed 
        self.formation_table.heading("Code Formation", text="Code Formation")
        self.formation_table.heading("Intitulé formation", text="Intitulé formation")
        self.formation_table.heading("Langue Formation", text="Langue Formation")
        self.formation_table.heading("Niveau Formation", text="Niveau Formation")
        self.formation_table.heading("Objectif Formation", text="Objectif Formation")
        
        #### Just show the heandings not something else 
        self.formation_table['show'] = 'headings'
        
        self.formation_table.column("Code Formation", width=50)
        self.formation_table.column("Intitulé formation", width=100)
        self.formation_table.column("Langue Formation", width=70)
        self.formation_table.column("Niveau Formation", width=100)
        self.formation_table.column("Objectif Formation", width=300)
        
        # pack the treeview
        self.formation_table.pack(fill=BOTH, expand=TRUE)
        
        ## Fill in the data as soon as the application is opened with the
        self.afficher_formation()
        
        ### "ButtonRelease" is the type of event (button release), 
        # and -1 is the source of the event (the left mouse button)
        self.formation_table.bind("<ButtonRelease-1>", self.recup_selected_data)  ## ---> calling the recup_selected_data/ -->evenementiel programmation
         
        
        

    ############# METHODES ##############
    

    def recup_selected_data(self, event):
        #debock ine_entry:
        code_formation_entry['state'] = 'normal'
        
        selected_row = self.formation_table.focus() ## ----> get a select data in formation table detail
        contain = self.formation_table.item(selected_row) # return a dict with a selected values
        
        row = contain['values'] ## row is a list that equal ["code", "int", "lang", "niv", "obj"]
        ## delete all before inserting
        code_formation_entry.delete(0, END)
        langue_formation_entry.delete(0, END)
        intitule_formation_entry.delete(0, END)
        niveau_formation_entry.delete(0, END)
        objectif_formation_entry.delete('1.0', END)
        
        
        ## insert data but checking if exist data before insertion
        if len(row): 
           code_formation_entry.insert(0, row[0])
           intitule_formation_entry.insert(0, row[1])
           langue_formation_entry.insert(0, row[2])
           niveau_formation_entry.insert(0, row[3])
           objectif_formation_entry.insert('1.0', row[4])
        
        code_formation_entry['state'] = 'disabled' ### ---> block the ine entry cause we can'not change it
        

    def chercher_by(self, event):
        bdd_file = "bdd/bdd_gestion_formation.db" 
        con = sqlite3.connect(bdd_file)
        cursor = con.cursor()
        
        ## récup data in recherche_entry
        entree = self.recherche_entry.get()
        
        query = "SELECT * FROM formations WHERE code_formation = :entry_code or intitule_formation = :entry_intitule_formation"
        
        my_dict= {'entry_code': entree, 'entry_intitule_formation':entree}
        cursor.execute(query, my_dict)
        
        ## verify is exist:
        result = cursor.fetchall()
        if len(result) > 0: ## if exist student in bdd
            ## delete all data before printing ...
            # * = decompress list or tuple
            self.formation_table.delete(*self.formation_table.get_children()) ## get_children() Returns a tuple of children belonging to item
            for row in result:
                self.formation_table.insert('', END, values=row)
        else:
            '''messagebox.showinfo("Recherche", "La formation recherchée n'existe pas.\nRassurez vous d'avoir entré des informations correctes!")'''

        cursor.close()
        con.close()
        
    def afficher_formation(self):
        bdd_file = "bdd/bdd_gestion_formation.db" 
        con = sqlite3.connect(bdd_file)
        cursor = con.cursor()
        
        query = "SELECT * FROM formations"
        cursor.execute(query)
        
        result = cursor.fetchall()
        
        if len(result) > 0: ## if exist student in bdd
            ## delete all data before printing ...
            # * = decompress list or tuple 
            self.formation_table.delete(*self.formation_table.get_children()) ## get_children() Returns a tuple of children belonging to item
            for row in result:
                self.formation_table.insert('', END, values=row) ## we can insert this data in our detail table
            
            self.recherche_entry.delete(0, END)  
        ## close connection to db after operations
        cursor.close()
        con.close()
        

    def enregistrer_formation(self):  # sourcery skip: extract-method, use-fstring-for-concatenation
        
        list_champ = []
        
        if code_formation_entry.get() == "":
            list_champ.append(code_formation_entry)
            
        if intitule_formation_entry.get()=="":
            list_champ.append(intitule_formation_entry)
            
        if langue_formation_entry.get() == "":
            list_champ.append(langue_formation_entry)
            
        if niveau_formation_entry.get() =="":
            list_champ.append(niveau_formation_entry)
        
        if len(objectif_formation_entry.get(1.0, END + '-1c')) == 0:
            list_champ.append(objectif_formation_entry)
            
        # giving a bg to the empty label 'if exist ofcourse
        if list_champ != []:
            for champ in list_champ:
                champ['bg'] = "#F9E2E4"
            messagebox.showerror("Erreurs", "Veuillez remplir tous les champs recquis !")
            list_champ.clear()

            return list_champ
        
            
        else:
            bdd_file = "bdd/bdd_gestion_formation.db" 
            con = sqlite3.connect(bdd_file)
            cursor = con.cursor()
            

                
            code_get=  code_formation_entry.get()
            code_query = "SELECT* FROM formations WHERE code_formation = :code"    
            cursor.execute(code_query, {'code':code_get})
            
            result = cursor.fetchall()
            
            if len(result) > 0:
                messagebox.showerror("Erreur", "Une formation existe\ndéjà avec le code que vous avez saisi!")
            else:
                formation_data = (code_formation_entry.get(), intitule_formation_entry.get(),
                                  langue_formation_entry.get(), niveau_formation_entry.get(),
                                  objectif_formation_entry.get("1.0", END))
                
                query = "INSERT INTO formations(code_formation, intitule_formation, langue_formation,niveau_formation,objectif_formation) VALUES(?,?,?,?,?)"
                
                cursor.execute(query, formation_data)
                
                con.commit()
                cursor.close()
                con.close()
                
                messagebox.showinfo("Enregistrement de la foramtion", f"Enregistrement de la formation {code_formation_entry.get()} ---> {intitule_formation_entry.get()} a été effectué avec succes! ")
                    
                self.refresh_formation() 
                    #Fill in the data as soon as the application is opened with the
                self.afficher_formation()
                
        
        
        
        
    def modifier_formation(self):  # sourcery skip: use-fstring-for-concatenation
        list_champ = []
        
        if code_formation_entry.get() == "":
            list_champ.append(code_formation_entry)
            
        if intitule_formation_entry.get()=="":
            list_champ.append(intitule_formation_entry)
            
        if langue_formation_entry.get() == "":
            list_champ.append(langue_formation_entry)
            
        if niveau_formation_entry.get() =="":
            list_champ.append(niveau_formation_entry)
        
        if len(objectif_formation_entry.get(1.0, END + '-1c')) == 0:
            list_champ.append(objectif_formation_entry)
            
        # giving a bg to the empty label 'if exist ofcourse
        if list_champ != [] and modifier_button:
            for champ in list_champ:
                champ['bg'] = "#F9E2E4"
            messagebox.showerror("Erreur", "Veuillez sélectionner un étudiant avant!\nRassurez vous d'avoir tout rempli.")
            list_champ.clear()

            return list_champ
        
        else:
            bdd_file = "bdd/bdd_gestion_formation.db" 
            con = sqlite3.connect(bdd_file)
            cursor = con.cursor()
            

                
            code_get=  code_formation_entry.get()
            intitule_get = intitule_formation_entry.get()
            code_query = "SELECT* FROM formations WHERE code_formation = :code AND intitule_formation = :intitule"    
            cursor.execute(code_query, {'code':code_get, 'intitule':intitule_get})
            
            
        formation_data = (intitule_formation_entry.get(),
                        langue_formation_entry.get(), niveau_formation_entry.get(),
                        objectif_formation_entry.get("1.0", END), code_formation_entry.get())
        query = "UPDATE formations SET intitule_formation= ?, langue_formation= ?, niveau_formation=?, objectif_formation = ? WHERE code_formation =?"
        cursor.execute(query, formation_data)
        
        con.commit()
        cursor.close()
        con.close()
        
        messagebox.showinfo("Modification de la formation", f"La modification de la formation {intitule_formation_entry.get()} a été effectuée avec succes! ")
                
        #refresh data
        self.refresh_formation()        
        #Fill in the data as soon as the application is opened with the
        self.afficher_formation()
                 
    
    def delete_formation(self):  # sourcery skip: extract-method, inline-variable
        if code_formation_entry.get() != "":
            ask_to_delete = messagebox.askyesno("Suppression", f"Voulez vraiment supprimer la formation\n{intitule_formation_entry.get()} qui a pour code: {code_formation_entry.get()}?")
            ### messagebox.askyesno provides to values 'YES' = 1 and 'NO' = 0
            ## so if user press in the 'YES' Button, that means 1 or > 0. --->
            if ask_to_delete > 0:
                bdd_file = "bdd/bdd_gestion_formation.db"
                con = sqlite3.connect(bdd_file)
                cursor = con.cursor() 

                data_to_delete = (code_formation_entry.get(),)
                query = "DELETE FROM formations WHERE code_formation = ?"
                
                cursor.execute(query, data_to_delete)
                con.commit()
                
                #close db
                cursor.close()
                con.close()
                
                messagebox.showinfo("Confirmation", f"la formation de code {code_formation_entry.get()} et de nom {intitule_formation_entry.get()} a bien été supprimée!")
                
                ### again this methods, you know what they 
                self.refresh_formation()
                self.afficher_formation()
        else:
            messagebox.showinfo("Sélection vide", "Vous devez sélectionner une formation avant")
            
            
    def refresh_formation(self):
        ##deblock code_formation
        code_formation_entry['state'] = 'normal'
        
        code_formation_entry.delete(0, END)
        intitule_formation_entry.delete(0, END)
        langue_formation_entry.delete(0, END)
        niveau_formation_entry.delete(0, END)
        objectif_formation_entry.delete(1.0, END) ## this is an text area, not an Entry 

        ## being focus on code_formation after deleted data in
        code_formation_entry.focus_set()
        
        #### reset too bg color
        
        code_formation_entry['bg'] = "white"
        intitule_formation_entry['bg'] = "white"
        langue_formation_entry['bg'] = "white"
        niveau_formation_entry['bg'] = "white"
        objectif_formation_entry['bg'] = "white"
        
        ## deselect a selected formation printing all formation
        self.afficher_formation()

  
    def gestion_etudiant(self):
        self.master.destroy()
        os.system("python GestionEtudiants.py")
    def gestion_inscription(self):
        self.master.destroy()
        os.system("python GestionInscription.py")
    def gestion_enseignants(self):
        self.master.destroy()
        os.system("python GestionEnseignant.py")
    


master = Tk()
application = GestionFormations(master=master)

master.mainloop()      