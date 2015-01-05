import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import *
from itertools import chain
 
class Window(Frame):

    def __init__(self, master=None):

        global CTR
        CTR = 0
        
        Frame.__init__(self, master)   
 
        #reference to the master widget, which is the tk window                 
        self.master = master
 
        self.init_window()
        self.displayRecord()
 
    def init_window(self):
        global NOTIF

        NOTIF = StringVar()
        NOTIF.set("To look up a word, type your search above.")
         
        # changing the title of our master widget      
        self.master.title("WORD-TO-DANEO")
 
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # load images to use
        load = Image.open("includes/img/bg.png")
        bg = ImageTk.PhotoImage(load)
        load = Image.open("includes/img/btn.png")
        btnIm = ImageTk.PhotoImage(load)
        load = Image.open("includes/img/btn_main.png")
        self.btnMain = ImageTk.PhotoImage(load)
        load = Image.open("includes/img/btn_mainH.png")
        self.btnMainH = ImageTk.PhotoImage(load)
        load = Image.open("includes/img/btn_add.png")
        self.btnAdd = ImageTk.PhotoImage(load)
        load = Image.open("includes/img/btn_addH.png")
        self.btnAddH = ImageTk.PhotoImage(load)
        load = Image.open("includes/img/btn_about.png")
        self.btnAbout = ImageTk.PhotoImage(load)
        load = Image.open("includes/img/btn_aboutH.png")
        self.btnAboutH = ImageTk.PhotoImage(load)
        
        # display background
        img = Label(self, image=bg)
        img.image = bg
        img.place(x=-2, y=-2)

        self.lbl = Label(self, bd=0, textvariable=NOTIF, bg="skyblue",  font=("Agency FB", 16), fg="red")
        self.lbl.place(x=450, y=150)

        # display search textbox
        self.txtSearch = Entry(self, bd=0, bg="skyblue", width="40")
        self.txtSearch.place(x=330, y=80)
        
        # display search button
        btn = Button(self, bd=0, bg="skyblue", cursor="hand1", image=btnIm, command=self.searchClicked)
        btn.image = btnIm
        btn.place(x=590, y=59)

        # display side buttons
        self.btn1 = Button(self, bd=0, bg="skyblue", image=self.btnMain, command=self.mainClicked)
        self.btn1.image = self.btnMain
        self.btn1.place(x=50, y=150)
        self.btn1.bind('<Enter>', self.btn1Enter)
        self.btn1.bind('<Leave>', self.btn1Leave)
        
        self.btn2 = Button(self, bd=0, bg="skyblue", image=self.btnAdd, command=self.addClicked)
        self.btn2.image = self.btnAdd
        self.btn2.place(x=50, y=230)
        self.btn2.bind('<Enter>', self.btn2Enter)
        self.btn2.bind('<Leave>', self.btn2Leave)

        self.btn3 = Button(self, bd=0, bg="skyblue", image=self.btnAbout, command=self.aboutClicked)
        self.btn3.image = self.btnAbout
        self.btn3.place(x=50, y=310)
        self.btn3.bind('<Enter>', self.btn3Enter)
        self.btn3.bind('<Leave>', self.btn3Leave)

    def btn1Enter(self, event):
        self.btn1.configure(image = self.btnMainH)
        self.btn1.configure(bd = 3)
    def btn2Enter(self, event):
        self.btn2.configure(image = self.btnAddH)
        self.btn2.configure(bd = 3)
    def btn3Enter(self, event):
        self.btn3.configure(image = self.btnAboutH)
        self.btn3.configure(bd = 3)

    def btn1Leave(self, no):
        self.btn1.configure(image = self.btnMain)
        self.btn1.configure(bd = 0)
    def btn2Leave(self, no):
        self.btn2.configure(image = self.btnAdd)
        self.btn2.configure(bd = 0)
    def btn3Leave(self, no):
        self.btn3.configure(image = self.btnAbout)
        self.btn3.configure(bd = 0)
    
    def displayInfo(self, word):
        global CURRID
        global CURRWORD
        global CURRTRANS
        global CURRHAN
        global CURRDIF
        
        CURRID = StringVar()
        CURRWORD = StringVar()
        CURRTRANS = StringVar()
        CURRHAN = StringVar()
        CURRDIF = StringVar()
        
        try:
            conn = sqlite3.connect("try.s3db")

            cur = conn.execute("SELECT * FROM daneo WHERE english_word = '"+word+"'")
            try:
                # clear the window
                self.init_window()
                NOTIF.set("")
                    
                first_row = next(cur)
                for row in chain((first_row,),cur):
                    # saving values to vars
                    CURRID.set(row[0])
                    CURRWORD.set(row[1])
                    CURRTRANS.set(row[2])
                    CURRHAN.set(row[3])
                    CURRDIF.set(row[4])
                    # word
                    self.lbl = Label(self, bd=0, text=row[1], bg="skyblue", fg="blue", font=("Agency FB", 26))
                    self.lbl.place(x=400, y=150)
                    # translation
                    self.lbl = Label(self, text="TRANSLATION:", bg="skyblue", fg="blue", font=("Agency FB", 14))
                    self.lbl.place(x=450, y=200)
                    self.lbl = Label(self, bd=0, text=row[3]+"   ["+row[2]+"]", bg="skyblue", font=("Tahoma", 12))
                    self.lbl.place(x=480, y=225)
                    # description
                    self.lbl = Label(self, text="DESCRIPTION:", bg="skyblue", fg="blue", font=("Agency FB", 14))
                    self.lbl.place(x=450, y=250)
                    self.lbl = Label(self, bd=0, text=row[4], bg="skyblue", font=("Tahoma", 12))
                    self.lbl.place(x=480, y=275)

                # load images to use
                load = Image.open("includes/img/btn_edit.png")
                btnEd = ImageTk.PhotoImage(load)
                load = Image.open("includes/img/btn_delete.png")
                btnDl = ImageTk.PhotoImage(load)

                # display buttons
                btn = Button(self, bd=0, bg="black", image=btnEd, command=self.editClicked)
                btn.image=btnEd
                btn.place(x=570, y=420)
                btn = Button(self, bd=0, bg="black", image=btnDl, command=self.deleteClicked)
                btn.image=btnDl
                btn.place(x=650, y=420)
        
            except StopIteration as e:
                    # clear the window
                    self.init_window()
                    
                    NOTIF.set("No results found.")
                    
        except sqlite3.Error as e:
            showwarning(title="Retrieving Data Failed", message=e)
        finally:
            if conn:
                conn.close()

        self.displayRecord()
        
    def displayRecord(self):
        # make a listbox
        self.lb = Listbox(self, bd=0, activestyle="dotbox", bg="lightgreen", height=16, width=13, font=("Tahoma", 12))
        self.lb.bind('<Double-Button-1>',self.lbSelected)
        self.lb.place(x=270, y=140)

##        # make a scroll bar
##        self.sb = Scrollbar(self, bd=0, orient=VERTICAL)
##        self.sb.place(x=375, y=140)
##
##        # join lb and sb
##        self.sb.configure(command = self.lb.yview)
##        self.lb.configure(yscrollcommand = self.sb.set)
        
        # put values in lb from db
        conn = sqlite3.connect("try.s3db")
        cur = conn.execute("SELECT * FROM daneo ORDER BY english_word")
        try:
            first_row = next(cur)
            for row in chain((first_row,),cur):
                self.lb.insert(END, row[1])
        except StopIteration as e:
            self.lb.insert(END,"Empty Record")

    def form(self, word, trans, han, dif):
        w = StringVar()
        t = StringVar()
        h = StringVar()
        d = StringVar()

        # set text variables
        w.set(word)
        t.set(trans)
        h.set(han)
        d.set(dif)
        
        # display input textboxes
        self.txtWord = Entry(self, bd=0, bg="lightgreen", width="37", textvariable=w, font=("Tahoma", 11))
        self.txtWord.place(x=400, y=160)

        self.txtTrans = Entry(self, bd=0, bg="lightgreen", width="33", textvariable=t, font=("Tahoma", 12))
        self.txtTrans.place(x=400, y=200)

        self.txtHan = Entry(self, bd=0, bg="lightgreen", width="33", textvariable=h, font=("Tahoma", 12))
        self.txtHan.place(x=400, y=240)

        self.txtDif = Text(self, bd=0, bg="lightgreen", width="33", height="5", font=("Tahoma", 12))# textvariable=d,
        self.txtDif.place(x=400, y=280)
        self.txtDif.insert(INSERT, d.get())

        # display labels
        Label(self, bd=0, text="English Word:", bg="skyblue", font=("Agency FB", 16)).place(x=280, y=160)
        Label(self, bd=0, text="Korean Translation:", bg="skyblue", font=("Agency FB", 16)).place(x=280, y=200)
        Label(self, bd=0, text="Korean Writing:", bg="skyblue", font=("Agency FB", 16)).place(x=280, y=240)
        Label(self, bd=0, text="Definition:", bg="skyblue", font=("Agency FB", 16)).place(x=280, y=280)

    def lbSelected(self, event):
        self.displayInfo(self.lb.get(ACTIVE))

    def searchClicked(self):
        if self.txtSearch.get() != "":
            self.displayInfo(self.txtSearch.get())
        else:
            showwarning(title="Empty Search Field", message="Search field is empty!")

    def mainClicked(self):
        # clear the window
        self.init_window()
        self.displayRecord()

    def addClicked(self):
        # clear the window
        self.init_window()
        NOTIF.set("")

        self.form("","","","")
        
        # load images to use
        load = Image.open("includes/img/btn_submit.png")
        btnSb = ImageTk.PhotoImage(load)
        load = Image.open("includes/img/btn_cancel.png")
        btnCn = ImageTk.PhotoImage(load)

        # display buttons
        btn = Button(self, bd=0, bg="black", image=btnSb, command=self.submitClicked)
        btn.image=btnSb
        btn.place(x=400, y=400)
        btn = Button(self, bd=0, bg="black", image=btnCn, command=self.mainClicked)
        btn.image=btnCn
        btn.place(x=500, y=400)
        
    def editClicked(self):
        # clear the window
        self.init_window()
        NOTIF.set("")

        self.form(CURRWORD.get(), CURRTRANS.get(), CURRHAN.get(), CURRDIF.get())

        # load images to use
        load = Image.open("includes/img/btn_submit.png")
        btnSb = ImageTk.PhotoImage(load)
        load = Image.open("includes/img/btn_cancel.png")
        btnCn = ImageTk.PhotoImage(load)

        # display buttons
        btn = Button(self, bd=0, bg="black", image=btnSb, command=self.updateClicked)
        btn.image=btnSb
        btn.place(x=400, y=400)
        btn = Button(self, bd=0, bg="black", image=btnCn, command=self.mainClicked)
        btn.image=btnCn
        btn.place(x=500, y=400)
        
    def deleteClicked(self):
        if askyesno(title="Deleting Record", message="Are you sure you want to delete "+CURRWORD.get()+"?") is True:
            try:
                conn = sqlite3.connect("try.s3db")

                conn.execute("DELETE FROM daneo WHERE english_word='"+CURRWORD.get()+"' AND daneo_id='"+CURRID.get()+"'")
                conn.commit()
                showinfo(title="Delete Successful", message="Successfully Deleted to Dictionary!")            
                self.mainClicked()
                    
            except sqlite3.Error as e:            
                showwarning(title="Adding Failed", message=e)
                
            finally:
                if conn:
                    conn.close()

    def submitClicked(self):
        if self.txtWord.get() != "" and self.txtTrans.get() != "" and self.txtDif.get(1.0,END)[:-1] != "":
            try:
                conn = sqlite3.connect("try.s3db")

                cur = conn.execute("SELECT count(*) FROM daneo WHERE english_word='"+self.txtWord.get()+"'")

                if cur.fetchone()[0]:
                    showwarning(title="Adding Failed", message="'"+self.txtWord.get()+"' is already existed in the database.")
                else:
                    conn.execute("INSERT INTO daneo (english_word, korean_word, hangeul, definition)VALUES('"+self.txtWord.get()+"', '"+self.txtTrans.get()+"', '"+self.txtHan.get()+"', '"+self.txtDif.get(1.0,END)[:-1]+"')")
                    conn.commit()
                    showinfo(title="Adding Successful", message="Successfully Added to Dictionary!")
                    self.mainClicked()

            except sqlite3.Error as e:            
                showwarning(title="Adding Failed", message=e)
                
            finally:
                if conn:
                    conn.close()
        else:
            showwarning(title="Empty Required Fields", message="All fields must be filled before submission!")

    def updateClicked(self):
        if self.txtWord.get() != "" and self.txtTrans.get() != "" and self.txtDif.get(1.0,END)[:-1] != "":
            try:
                conn = sqlite3.connect("try.s3db")

                conn.execute("UPDATE daneo SET english_word='"+self.txtWord.get()+"', korean_word='"+self.txtTrans.get()+"', hangeul='"+self.txtHan.get()+"', definition='"+self.txtDif.get(1.0,END)[:-1]+"' WHERE daneo_id='"+CURRID.get()+"'")
                conn.commit()
                showinfo(title="Updating Successful", message="Successfully Updated to Dictionary!")
                self.mainClicked()
                
            except sqlite3.Error as e:            
                showwarning(title="Editing Failed", message=e)
                
            finally:
                if conn:
                    conn.close()
        else:
            showwarning(title="Empty Required Fields", message="All fields must be filled before submission!")

    def aboutClicked(self):
        # clear the window
        self.init_window()
        NOTIF.set("")

        load = Image.open("includes/img/about.png")
        abtim = ImageTk.PhotoImage(load)
        
        abt = Label(self, bd=0, image=abtim)
        abt.image = abtim
        abt.place(x=330, y=140)
    def client_exit(self):
        exit()
 
 
# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()
 
root.geometry("800x600")
 
#creation of an instance
app = Window(root)
 
 
#mainloop 
root.mainloop() 
