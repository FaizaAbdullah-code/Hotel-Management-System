#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jul 07, 2018 12:12:02 PM
import os
import pickle
import sys
import os
from subprocess import call
from abc import ABCMeta,abstractmethod

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
details_list=[]

class save:
    def saves(self,NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO
#POLYMORPHISM
    
    def chk_name():
        pass
    def chk_add():
        pass
    def chk_mo():
        pass
    def chk_day():
        pass





class saving_userdetails(save):#INHERITANCE
    
    def file_save(self):
        global details_list
        NAME_PRO = details_list[0]
        ADDRESS_PRO = details_list[1]
        MOBILE_NO_PRO = details_list[2]
        ROOM_NO_PRO = details_list[3]
        PRICE_PRO = details_list[4]
        f = open("hotel.dat", "ab")
        a=save()
        a.saves(NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO)#COMPOSITION
        pickle.dump(a,f,protocol=2)
        f.close()
        listq=[str(NAME_PRO),str(ADDRESS_PRO),str(MOBILE_NO_PRO),str(ROOM_NO_PRO),str(PRICE_PRO)]
        myVars = {'A':NAME_PRO,"B":ADDRESS_PRO,"C":MOBILE_NO_PRO,"D":ROOM_NO_PRO,"E":PRICE_PRO }

        fo=open("recipt.txt","w+")
        for h in range(0,5):
            fo.write(listq[h]+"\r\n")
        fo.close()
        call(["python", "recipt.py"])
        r=restart_program()#COMPOSITION
        r.restart()






u = list()
Delux = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Semi_Delux = (16, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
General = (26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45)
Joint_Room = (46, 47, 48, 49, 50, 46, 47, 48, 49, 50)
m = [9]
G = []
class restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""

    def restart(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)




class HOTEL_MANGMENT_checkin(save):#INHERITANCE


    def __init__(self):
        self.NAME=""
        self.ADDERESS=""
        self.MOBILE=""
        self.DAYS=0
        self.price=0
        self.room=0





        def chk_name():
            while True:

                self.k = str(self.name.get())

                a = self.k.isdigit()
                if len(self.k) != 0 and a != True:
                    self.NAME=self.k
                    self.Text1.insert(INSERT, "name has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input please input a valid name""\n")

                    break

        def chk_add():
            while True:
                self.g = str(self.addr.get())


                ak = self.g.isdigit()
                if len(self.g)!= 0 and ak!=True:
                    self.ADDERESS=self.g
                    self.Text1.insert(INSERT, "address has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input please input a valid address""\n")

                    break

        def chk_mo():
            while True:

                self.h = str(self.mobile.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    self.MOBILE = self.h
                    self.Text1.insert(INSERT, "mobile number has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input please input a valid mobile number""\n")
                break

        def chk_day():
            while True:

                self.l = str(self.days.get())

                if self.l.isdigit() == True and len(self.l) != 0:
                    self.DAYS = int(self.l)
                    self.Text1.insert(INSERT, "days has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input ""\n")
                    break

        def enter(self):
            self.name = self.NAME
            self.address = self.ADDERESS
            self.mobile_no = self.MOBILE
            self.no_of_days = int(self.DAYS)

        def tor(self):

            if self.ch == 1:
                self.price = self.price + (2000 * self.no_of_days)
                m[0] = 1
            elif self.ch == 2:
                self.price = self.price + (1500 * self.no_of_days)
                m[0] = 2
            elif self.ch == 3:
                self.price = self.price + (1000 * self.no_of_days)
                m[0] = 3
            elif self.ch == 4:
                self.price = self.price + (1700 * self.no_of_days)
                m[0] = 4

        def payment_option(self):
            op = self.p
            if op == 1:
                self.Text1.insert(INSERT, "no discount""\n")
            elif op == 2:
                self.price = self.price - ((self.price * 10) / 100)
                self.Text1.insert(INSERT, "10% discount""\n")

        def bill(self):

            if m[0] == 1:
                a = Delux
            elif m[0] == 2:
                a = Semi_Delux
            elif m[0] == 3:
                a = General
            elif m[0] == 4:
                a = Joint_Room

            G = []
            f2 = open("hotel.dat", "rb")
            try:
                while True:
                    s = pickle.load(f2)

                    k = s.room_no
                    G.append(k)
                    continue

            except EOFError:
                pass

            for r in a:
                if r not in G:
                    self.room = r
                    break
                else:
                    continue
            self.room = r
            f2.close()

            details_list.append(self.name)
            details_list.append(self.address)
            details_list.append(self.mobile_no)
            details_list.append(self.room)
            details_list.append(self.price)



            d=saving_userdetails()#COMPOSITION
            d.file_save()



        def submit_clicked():
            if self.var1.get()==1 and self.var2.get()==0 and self.var3.get()==0 and self.var4.get()==0 and self.var5.get()==1 and self.var6.get()==0:
                self.ch=1
                self.p=2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)


            elif self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 1
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 2
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 1 and self.var6.get() ==0 :
                self.ch = 2
                self.p = 2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 3
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1 and self.var4.get() == 0 and self.var5.get() == 1 and self.var6.get() == 0:
                self.ch = 3
                self.p = 2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)

            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 1 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 4
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 1 and self.var5.get() == 1 and self.var6.get() == 0:
                self.ch = 4
                self.p = 2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)

            else:
                self.Text1.insert(INSERT, "invalid choice please input a valid choice""\n")





        window=Tk()
        window.title('TO DO LIST')
        root= Frame(window)
        root.pack()
        window.config(bg='silver')
        window.geometry('2000x1000')
        background_image=PhotoImage(file='10.png')
        background_label=Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.theLabel=Button(root, text='CHECK IN ', width=30, height=2, font=('Times', '24','bold'), bg='black', fg='white')
        self.theLabel.grid(pady=20, row=0, columnspan=3)


        self.Name=Button(root, text='NAME', bg='cornsilk', fg='black',width=20, font=('Times', '16','bold'))
        self.Name.grid(pady=2, row=1, column=0)


        self.Address=Button(root, text='ADDRESS', bg='cornsilk', fg='black', width=20,font=('Times', '16','bold'))
        self.Address.grid(row=2, column=0)

        self.Contact=Button(root, text='CONTACT', bg='cornsilk', fg='black', width=20,font=('Times', '16','bold'))
        self.Contact.grid(row=3, column=0)

        self.Days=Button(root, text='DAYS', bg='cornsilk', fg='black', width=20,font=('Times', '16','bold'))
        self.Days.grid(row=4, column=0)

        self.Room=Button(root, text='ROOM', bg='cornsilk', fg='black', width=20,font=('Times', '16','bold'))
        self.Room.grid(row=6, column=0)

        self.PaymentMethod=Button(root, text='PAYMENT METHOD', bg='cornsilk', fg='black', width=20,font=('Times', '16','bold'))
        self.PaymentMethod.grid(row=8, column=0)

        #########################   ENTRIES       ##################################################

        self.entry_of_Name=Entry(root)
        self.entry_of_Name.grid(row=1, column=1)
        self.name=StringVar()
        self.entry_of_Name.configure(textvariable=self.name)

        self.entry_of_Address=Entry(root)
        self.entry_of_Address.grid(row=2, column=1)
        self.addr = StringVar()
        self.entry_of_Address.configure(textvariable=self.addr)

        self.entry_of_Contact=Entry(root)
        self.entry_of_Contact.grid(row=3, column=1)
        self.mobile=StringVar()
        self.entry_of_Contact.configure(textvariable=self.mobile)

        self.entry_of_Days=Entry(root)
        self.entry_of_Days.grid(row=4, column=1)
        self.days=StringVar()
        self.entry_of_Days.configure(textvariable=self.days)


        #######################################################################

        self.Checkbutton1 = Checkbutton(root)
        self.var1 = IntVar()
        self.Checkbutton1.grid(row=6, column=1)
        self.Checkbutton1.configure(bg='black', fg='silver')
        self.Checkbutton1.configure(text='''DELUXE''')
        self.Checkbutton1.configure(variable=self.var1)

        self.Checkbutton2= Checkbutton(root)
        self.var2 = IntVar()
        self.Checkbutton2.grid(row=6, column=2)
        self.Checkbutton2.configure(text='''GENERAL''')
        self.Checkbutton2.configure(variable=self.var2)
        self.Checkbutton2.configure(bg='black', fg='silver')

        self.Checkbutton3 = Checkbutton(root)
        self.var3= IntVar()
        self.Checkbutton3.grid(row=7, column=1)
        self.Checkbutton3.configure(text='''FULL DELUXE''')
        self.Checkbutton3.configure(bg='black', fg='silver')
        self.Checkbutton3.configure(variable=self.var3)

        self.Checkbutton4= Checkbutton(root)
        self.var4 = IntVar()
        self.Checkbutton4.grid(row=7, column=2)
        self.Checkbutton4.configure(text='''JOINT''')
        self.Checkbutton4.configure(bg='black', fg='silver')
        self.Checkbutton4.configure(variable=self.var4)


        self.Checkbutton5 = Checkbutton(root)
        self.var5= IntVar()
        self.Checkbutton5.grid(row=8, column=1)
        self.Checkbutton5.configure(text='''CASH''')
        self.Checkbutton5.configure(bg='black', fg='silver')
        self.Checkbutton5.configure(variable=self.var5)


        self.Checkbutton6= Checkbutton(root)
        self.var6 = IntVar()
        self.Checkbutton6.grid(row=8, column=2)
        self.Checkbutton6.configure(text='''CARD''')
        self.Checkbutton6.configure(bg='black', fg='silver')
        self.Checkbutton6.configure(variable=self.var6)

     
######################################################################################################
        
        self.Rb1=Button(root, text='DONE',width=8,font=('Times', '11','bold'), bg='cornsilk', fg='black')
        self.Rb1.grid(pady=2, row= 1, column=2)
        self.Rb1.configure(command=chk_name)

        self.Rb2=Button(root, text='DONE',width=8,font=('Times', '11','bold'), bg='cornsilk', fg='black')
        self.Rb2.grid(pady=2, row= 2, column=2)
        self.Rb2.configure(command=chk_add)
        

        self.Rb3=Button(root, text='DONE',width=8,font=('Times', '11','bold'), bg='cornsilk', fg='black')
        self.Rb3.grid(pady=2, row= 3, column=2)
        self.Rb3.configure(command=chk_mo)

        self.Rb4=Button(root, text='DONE',width=8,font=('Times', '11','bold'), bg='cornsilk', fg='black')
        self.Rb4.grid(pady=2, row= 4, column=2)
        self.Rb4.configure(command=chk_day)


        self.Rb5=Button(root, text='SUBMIT',width=20 , height=3, font=('Times', '12','bold'), bg='black', fg='white')
        self.Rb5.grid(pady=8,row= 9, column=1)
        self.Rb5.configure(command=submit_clicked)

################################################################################
        self.Text1 = Text(root,bg='cornsilk',fg='black', width=60,height=20,font=('Times', '9','bold'))
        self.Text1.grid(row=10, column=1)
        self.Text1.configure(wrap=WORD)




        window.mainloop()


if __name__ == '__main__':
    hotel=HOTEL_MANGMENT_checkin()






