

import os
import pickle

details_list=[]
l2=[]
G = []
def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
    f = open("hotel.dat", "ab")
    a=save(NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO)
    pickle.dump(a,f,protocol=2)
    f.close()
    restart_program()


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)






class save:
    def __init__(self, NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, ROOM_NO_PRO, PRICE_PRO): 
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO
        print(self.name,self.address,self.mobile_no,self.room_no,self.price)

    def check_room(): #polymorpohism
        pass



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



class New_Toplevel(save): #inheritance

    def __init__(self):
        def check_room():
            self.rom = str(self.data.get())
            print(self.rom)
            print("\n")
            if self.rom.isdigit() == True and len(self.rom) != 0:
                self.Text1.insert(INSERT, " valid room number ""\n")
                v = int(self.rom)
                f = open("hotel.dat", "rb")
                f1 = open("hote.dat", "ab")
                n = 0
                try:
                    while True:
                        s = pickle.load(f)
                        if s.room_no == v:
                            n = 1
                            name1 = s.name

                            print(" ")
                        else:
                            pickle.dump(s, f1)
                except EOFError:
                    if n == 0:
                        self.Text1.insert(INSERT, "NO GUEST FOUND""\n")

                    elif n == 1:

                        self.Text1.insert(INSERT, "THANK YOU  " + name1.upper() + " FOR VISTING US""\n")
                    pass
                f.close()
                f1.close()
                os.remove("hotel.dat")
                os.rename("hote.dat", "hotel.dat")

            else:
                self.Text1.insert(INSERT, "invalid input please input a valid ROOM NO.""\n")

        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 23 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 24 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1011x750")
        root.title("JAF HOTELS")
        root.configure(background="#ffffff")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")
        background_image=PhotoImage(file='10.png')
        background_label=Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.04, rely=0.04, relheight=0.91, relwidth=0.91)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="cornsilk")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)
##        photo=PhotoImage(file="KK.gif")
##        self.Frame1.configure(image=photo, compound=CENTER)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.14, rely=0.12, height=46, width=442)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(background="white")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="black")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''ENTER THE ROOM NO.   :''')

        self.Entry1 = Entry(self.Frame1)
        self.data=StringVar()
        self.Entry1.place(relx=0.67, rely=0.12,height=44, relwidth=0.07)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#bfbfbf")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="black")
        self.Entry1.configure(highlightbackground="#ffffff")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#e6e6e6")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=self.data)



        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.05, rely=0.54, relheight=0.4, relwidth=0.89)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#ffffff")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=824)
        self.Text1.configure(wrap=WORD)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.34, rely=0.28, height=93, width=286)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="white")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(font=font12)
        self.Button1.configure(foreground="black")
        self.Button1.configure(highlightbackground="purple")
        self.Button1.configure(highlightcolor="pink")
        self.Button1.configure(pady="0")
        
        self.Button1.configure(text='''CHECK OUT''')
   
        
        self.Button1.configure(command=check_room)
        root.mainloop()
from __main__ import *
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

fo1=open("recipt.txt","r")
list1=fo1.readlines()

del list1[1]
del list1[2]
del list1[3]
del list1[4]
del list1[5]
list1[0]=list1[0][:-1]
list1[1]=list1[1][:-1]
list1[2]=list1[2][:-1]
list1[3]=list1[3][:-1]
list1[4]=list1[4][:-1]

p='''
@@@@@ JAF HOTELS @@@@@

@@@@@ DHA PHASE V, KARACHI @@@@@

@@@@@ SERVING    GUESTS   SINCE @@@@@

THANK YOU FOR BEING HERE!!

@@@@   ###1950###       @@@@


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


NAME-%s
ADDRESS-%s
MOBILE NO.-%s
YOUR TOTAL BILL IS Rs.-%s
YOUR ROOM NUMBER IS %s
'''%(list1[0],list1[1],list1[2],list1[4],list1[3])

        





class receipt:
    def __init__(self):
        root=Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        root.geometry("800x800")
        root.title("RECEIPT")
        root.configure(background="cornsilk")
      

        self.Label1 = Label(root)
        self.Label1.configure(background="cornsilk", font=('Times', '16','bold'))
        self.Label1.place(relx=0, rely=0, height=800, width=800)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="black")
        self.Label1.configure(text=p)
        self.Label1.configure(anchor=N)

        self.Label1.configure(wraplength=500)
        self.Label1.configure(justify =CENTER)

        self.Label1.configure(width=582)
        root.mainloop()





if __name__ == '__main__':
    out=New_Toplevel()

if __name__ == '__main__':
    receipt1=receipt()
