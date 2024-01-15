
from tkinter import *
import sqlite3
from tkinter import messagebox
import os

class Login:
    def __init__(self, master):
        self.master = master 
        self.master.title("Authentification")
        
        
        screen_width = master.winfo_screenwidth() #-->  get the sreen width and set it to the application
        screen_height = master.winfo_screenheight() #-->  get the sreen height and set it to the application
        
        self.master.geometry("%dx%d"% (screen_width, screen_height))
        self.master.config(bg="#576f9c", highlightbackground="black", highlightthickness=3)
        
        
        #, highlightcolor="black"
         #highlightthickness=2
        
        frame = Frame(self.master, relief=GROOVE, bg="#191970", highlightbackground="black", highlightthickness=3)
        frame.place(x=380, y=180, width=0.5*screen_width, height=0.4*screen_height)
        
        connexion_label = Label(frame, text="Connexion", bg="#191970", font=("ubuntu", 20, "bold", 'underline'), fg="#576f9c")
        connexion_label.grid(row=0, column=3, padx=80, pady=15)
        
        username_email_label = Label(frame, text="Username or Email*: ",font=("ubuntu", 15, 'bold'), bg="#191970", fg="white")
        username_email_label.grid(row=3, column=2, pady=15, padx=15)
        
        self.username_email_entry = Entry(frame, font=('Times new roman', 13, "bold"), bd=3, 
                                   relief=GROOVE, width=30)
        self.username_email_entry.grid(row=3, column=3, padx=15, pady=20, columnspan=1)
        
        password_label = Label(frame, text="Mot de passe*: ",font=("ubuntu", 15, 'bold'), bg="#191970", fg="white")
        password_label.grid(row=4, column=2, pady=20, padx=10)
        
        self.password_entry = Entry(frame, font=('Times new roman', 13, "bold"), bd=3, 
                                   relief=GROOVE, width=30, show='*')
        self.password_entry.grid(row=4, column=3, padx=15, pady=20, columnspan=1)
        
        self.show_password_var = IntVar()
        
        self.show_password_checkbox = Checkbutton(frame, text="Afficher le mot de passe", command=self.show_password, 
                                            font=('Times new roman', 10, "bold"), cursor='hand2', width=20, variable=self.show_password_var)
        self.show_password_checkbox.grid(row=4, column=4)
        
        
        
        connexion_button = Button(frame, text="Connexion", width=10, height=2, command=self.connexion, cursor="hand2", bd=2)
        connexion_button.grid(row=5, column=3, padx=10, pady=10)
        
        
        '''image = PhotoImage(file="D:\Formation\Gestion_formation\images\images.png")
        label_image = Label(self.master, image= image, height=50)
        label_image.grid(row=1, column=3, padx=650, pady=100)'''
        
    def connexion(self):  # sourcery skip: use-named-expression
        bdd_file = "bdd/bdd_gestion_formation.db"
        con = sqlite3.connect(bdd_file)
        cursor = con.cursor()
        
        user_name_mail = (self.username_email_entry.get(),self.username_email_entry.get(), self.password_entry.get())
        query = "SELECT * FROM user WHERE username = ? or adresse_mail = ? AND mot_de_pass = ?"
        cursor.execute(query, user_name_mail)
        
        result = cursor.fetchone()
        
        if result:
            self.master.destroy()
            #messagebox.showinfo("Connexion", f"Bienvenu(s) {result[1]} {result[0]}")
            os.system("python GestionEtudiants.py")
        else:
            messagebox.showerror("Erreur", "Incorrect username or password!")
            self.username_email_entry['bg'] = '#F08080'
            self.password_entry['bg'] = '#F08080'
        cursor.close()
        con.close()
        
        
    def show_password(self):
        x = self.show_password_var.get()
        if x == 1:
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')
        
        
        
        
         

master = Tk()
app = Login(master=master)

'''img = PhotoImage(file="images/images.png")
background_label = Label(master, image=img)
background_label.place(x=0, relwidth=1, relheight=1)
background_label.lower()'''
    
master.mainloop()
        