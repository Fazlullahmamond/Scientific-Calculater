from tkinter import*
import math
import tkinter.messagebox

root = Tk()
root.title("Standard Calculator")
root.configure(background = "gray90")
root.resizable(width = False, height = False)
root.geometry("344x320")

#___________________________________Scientific Function_______________________________#
def Sine():
    global expression
    try:
        expression = str(eval(expression))
        expression=math.sin(math.radians(float(expression)))
        display.set(expression)
        expression = str(expression)
    except:
        display.set("Result is undefined")
        expression ="0"

def Cose():
    global expression
    try:
        expression = str(eval(expression))
        expression= math.cos(math.radians(float(expression)))
        display.set(expression)
        expression = str(expression)
    except:
        display.set("Result is undefined")
        expression ="0"

def Tane():
    global expression
    try:
        if expression == '90':
            display.set("Result is undefined")
        else:
            expression = str(eval(expression))
            expression=math.tan(math.radians(float(expression)))
            display.set(expression)
            expression = str(expression)
    except:
        display.set("Result is undefined")
        expression ="0"

def Log():
    global expression
    try:
        expression = str(eval(expression))
        expression=math.log10(float(expression))
        display.set(expression)
        expression = str(expression)
    except:
        display.set("Result is undefined")
        expression ="0"



def asin():
    global expression
    try:
        expression = str(eval(expression))
        expression= math.asin(math.radians(float(expression)))
        display.set(expression)
        expression = str(expression)
    except:
        display.set("Result is undefined")
        expression ="0"

def acos():
    global expression
    try:
        expression = str(eval(expression))
        expression= math.acos(math.radians(float(expression)))
        display.set(expression)
        expression = str(expression)
    except:
        display.set("Result is undefined")
        expression ="0"

def atan():
    global expression
    try:
        expression = str(eval(expression))
        expression= math.atan(math.radians(float(expression)))
        display.set(expression)
        expression = str(expression)
    except:
        display.set("Result is undefined")
        expression ="0"

def Mod():
    global expression
    expression = expression + " % "
    display.set(expression)

def XY():
    global expression
    expression = expression + "  **  "
    display.set(expression)
        
def Ftl():
    global expression
    try:
        expression = math.factorial(float(expression))
        display.set(expression)
    except:
        display.set("Result is undefined")
        expression ="0"

def Br1():
    global expression
    expression = expression + " ("
    display.set(expression)

def Br2():
    global expression
    expression = expression + ") "
    display.set(expression)

def PI():
    global expression
    py = math.pi
    display.set(py)
    expression = str(py)

def E():
    global expression
    Ee = math.e
    display.set(Ee)
    expression = str(Ee)

def Sqr():
    global expression
    try:
        sq = float(expression)**(1/3)
        display.set(sq)
        expression = str(sq)
    except:
        display.set("Result is undefined")
        expression ="0"

def expp():
    global expression
    try:
        xp = (math.e) ** (float(expression))
        display.set(xp)
        expression = str(xp)
    except:
        display.set("Result is undefined")
        expression ="0"

def pitwo():
    global expression
    TU = math.tau
    display.set(TU)
    expression = str(TU)

def xten():
    global expression
    try:
        Xten = 10 ** float(expression)
        display.set(Xten)
        expression = str(Xten)
    except:
        display.set("Result is undefined")
        expression ="0"

def Degg():
    global expression
    try:
        degg = math.degrees(float(expression))
        display.set(degg)
        expression = str(degg)
    except:
        display.set("Result is undefined")
        expression ="0"

def Radd():
    global expression
    try:
        radd = math.radians(float(expression))
        display.set(radd)
        expression = str(radd)
    except:
        display.set("Result is undefined")
        expression ="0"
#___________________________________Standard Function_________________________________#
expression = "0"

def evaluate():
    global expression
    
    current_txt = display.get()
    
    try:
        b=['+','-','/','*','%',' ']
        if expression[-1] in b:
            display.set(expression)
        else:
            expression = str(eval(current_txt))
            display.set(expression)
            
            file = open("history.txt","a")
            data = current_txt + " = " + expression + "\n"
            History = file.write(data)
            History = file.close()
    except:
        display.set("Result is undefined")
        expression ="0"

def history():
    file = open('history.txt', 'r')
    his = file.readline()
    if his == "" :
        clean = tkinter.messagebox.showinfo("History","History is clean")
    else:
        win = Tk()
        win.title("History")
        win.resizable(width = True, height = True)
        win.geometry("321x322")
        while his != "":
            label = Label(win, text=his, font=('Arial',16,'bold'))
            his = file.readline()
            label.pack()
        win.mainloop()
    file.close  

def chistory():
    file = open('history.txt','w')
    file.write("")
    file.close
    cleared = tkinter.messagebox.showinfo(title="Clear history",message="History cleared")
    
def press(input_value):
    global expression
    if expression == "0":
        expression = ""
        expression = expression + str(input_value)
        display.set(expression)
    else:
        expression = expression + str(input_value)
        display.set(expression)

def firstmath(add):
    global expression
    a=['+','-','/','*','.']
    if expression[-1] in a:
        expression = expression[:-1]
        expression = expression + add
        display.set(expression)
    else:
        expression = expression + add
        display.set(expression)

def sqr():
    global expression
    try:
        expression = str(eval(expression))
        if expression[:1] == "-":
            display.set("Result is undefined")
            expression = "0"
        else:
            expression = float(expression)**(0.50)
            display.set(expression)
            expression = str(expression)
            expression = "0"
    except:
        display.set("Result is undefined")
    
def clear():
    global expression
    if len(expression) == 1:
        expression = " "
        display.set('')
    else:
        expression = expression[:-1]
        display.set(expression)
    
def clearall():
    global expression
    expression = "0"
    display.set('0')

def btnPN():
    global expression
    if expression[:1] != "-":
        if expression == '0':
            expression = '-'
            display.set(expression)
        else:
            expression = "-" + expression
            display.set(expression)
    else:
        expression = expression[1:]
        display.set(expression)
def credit():
    friends = Tk()
    friends.title("Credits")
    friends.resizable(width = False, height = False)
    friends.geometry("321x322+0+0")
    friends.configure(background = "gray94")
    creditss = Label(friends,text="\n \n Credits : \n \n Fazlullah \n www.facebook.com/MAM0ND \n Youtube : Pashto Byte \n \n",font=('candara',15,'bold'))
    creditss.pack()
    friends.mainloop()

def Scientific():
    root.title("Scientific Calculator")
    root.resizable(width = False, height = False)
    root.geometry("344x566")

def Standard():
    root.title("Standard Calculator")
    root.resizable(width = False, height = False)
    root.geometry("344x320")


def iExit():
    iExit = tkinter.messagebox.askyesno("Calculator","Do you want to Exit")
    if iExit > 0:
        root.destroy()
        return

#________________________________Entry Box__________________________________#

display = StringVar()

txtDisplay = Entry(root, textvariable=display, font = ('calibri',20,'bold'),bg='gray90',bd=0,width=22,justify=RIGHT)
txtDisplay.grid(row=0 ,column=0 ,columnspan=4 ,pady=20)
txtDisplay.insert(0,"0")
#_______________________________123456789 Buttons____________________________#
btnZero =Button(root,text="0",width=6,height=1,font=('candara',18),bd=0,bg='gray97',fg='gray25',command=lambda:press(0)).grid(row=5,column=1,pady=1,padx=1)
btnone =Button(root,text="1",width=6,height=1,font=('candara',18),bd=0,bg='gray97',fg='gray25',command=lambda:press(1)).grid(row=4,column=0,pady=1,padx=1)
btntwo =Button(root,text="2",width=6,height=1,font=('candara',18),bd=0,bg='gray97',fg='gray25',command=lambda:press(2)).grid(row=4,column=1,pady=1,padx=1)
tbnthree =Button(root,text="3",width=6,height=1,font=('candara',18),bd=0,bg='gray97',fg='gray25',command=lambda:press(3)).grid(row=4,column=2,pady=1,padx=1)

tbnfour =Button(root,text="4",width=6,height=1,font=('candara',18),bd=0,bg='gray97',fg='gray25',command=lambda:press(4)).grid(row=3,column=0,pady=1,padx=1)
btnfive =Button(root,text="5",width=6,height=1,font=('candara',18),bd=0,bg='gray97',fg='gray25',command=lambda:press(5)).grid(row=3,column=1,pady=1,padx=1)
btnsix =Button(root,text="6",width=6,height=1,font=('candara',18),bd=0,bg='gray97',fg='gray25',command=lambda:press(6)).grid(row=3,column=2,pady=1,padx=1)

btnseven =Button(root,text="7",width=6,height=1,font=('candara',18),bd=0,bg='gray97',fg='gray25',command=lambda:press(7)).grid(row=2,column=0,pady=1,padx=1)
btneight =Button(root,text="8",width=6,height=1,font=('candara',18),bd=0,bg='gray97',fg='gray25',command=lambda:press(8)).grid(row=2,column=1,pady=1,padx=1)
btnnine =Button(root,text="9",width=6,height=1,font=('candara',18),bd=0,bg='gray97',fg='gray25',command=lambda:press(9)).grid(row=2,column=2,pady=1,padx=1)

#____________________________Standard Buttons_____________________________________#
btnClearAll =Button(root,text=chr(67)+chr(69),width=6,height=1,font=('candara',18,'bold'),bd=0,bg='gray94',fg='tomato3',command=clearall).grid(row=1,column=0,pady=1,padx=1)
btnClear =Button(root,text=chr(9003),width=6,height=1,font=('candara',18),bd=0,bg='gray94',command=clear,fg='steelblue3').grid(row=1,column=1,pady=1,padx=1)
btnSQ =Button(root,text=chr(8730),width=6,height=1,font=('candara',18),bd=0,bg='gray94',command=sqr,fg='steelblue3').grid(row=1,column=2,pady=1,padx=1)
btnDiv =Button(root,text=chr(247),width=6,height=1,font=('candara',18),bd=0,bg='gray94',command=lambda:firstmath("/"),fg='steelblue3').grid(row=1,column=3,pady=1,padx=1)
btnMulti =Button(root,text="x",width=6,height=1,font=('candara',18),bd=0,bg='gray94',command=lambda:firstmath("*"),fg='steelblue3').grid(row=2,column=3,pady=1,padx=1)
btnSubt =Button(root,text="-",width=6,height=1,font=('candara',18),bd=0,bg='gray94',command=lambda:firstmath("-"),fg='steelblue3').grid(row=3,column=3,pady=1,padx=1)
btnAdd =Button(root,text="+",width=6,height=1,font=('candara',18),bd=0,bg='gray94',command=lambda:firstmath("+"),fg='steelblue3').grid(row=4,column=3,pady=1,padx=1)
btneql =Button(root,text="=",width=6,height=1,font=('candara',18),bd=0,bg='steelblue3',command=evaluate,fg='white').grid(row=5,column=3,pady=1,padx=1)
btnDot =Button(root,text=".",width=6,height=1,font=('candara',18),bd=0,bg='gray94',command=lambda:firstmath("."),fg='gray25').grid(row=5,column=2,pady=1,padx=1)
btnPn =Button(root,text=chr(177),width=6,height=1,font=('candara',18),bd=0,bg='gray94',command=btnPN,fg='gray25').grid(row=5,column=0,pady=1,padx=1)
#_______________________________Scientific Buttons______________________________#

btnsin =Button(root,text="sin",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=Sine).grid(row=6,column=0,pady=1,padx=1)
btncos =Button(root,text="cos",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=Cose).grid(row=6,column=1,pady=1,padx=1)
btntan =Button(root,text="tan",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=Tane).grid(row=6,column=2,pady=1,padx=1)
btnasin =Button(root,text="asin",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=asin).grid(row=7,column=0,pady=1,padx=1)
btnacos =Button(root,text="acos",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=acos).grid(row=7,column=1,pady=1,padx=1)
btnatan =Button(root,text="atan",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=atan).grid(row=7,column=2,pady=1,padx=1)
btnlog =Button(root,text="log",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=Log).grid(row=6,column=3,pady=1,padx=1)
btnmod =Button(root,text="Mod",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=Mod).grid(row=7,column=3,pady=1,padx=1)
btnpwr =Button(root,text="x^y",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=XY).grid(row=8,column=0,pady=1,padx=1)
btnftl =Button(root,text="n!",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=Ftl).grid(row=8,column=1,pady=1,padx=1)
btnbc1 =Button(root,text="(",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=Br1).grid(row=8,column=2,pady=1,padx=1)
btn2bc2 =Button(root,text=")",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=Br2).grid(row=8,column=3,pady=1,padx=1)
btnpi =Button(root,text=chr(960),width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=PI).grid(row=9,column=0,pady=1,padx=1)
btne =Button(root,text="e",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=E).grid(row=9,column=1,pady=1,padx=1)
btnnsqr =Button(root,text="3"+chr(8730),width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=Sqr).grid(row=9,column=2,pady=1,padx=1)
btnExp =Button(root,text="Exp",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=expp).grid(row=9,column=3,pady=1,padx=1)
btn2pi =Button(root,text='2'+chr(960),width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=pitwo).grid(row=10,column=0,pady=1,padx=1)
btn10x =Button(root,text="10^x",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=xten).grid(row=10,column=1,pady=1,padx=1)
btn1x =Button(root,text="Degree",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=Degg).grid(row=10,column=2,pady=1,padx=1)
btnRad =Button(root,text="Radians",width=6,height=1,font=('candara',18),bd=0,bg='gray94',fg='gray25',command=Radd).grid(row=10,column=3,pady=1,padx=1)

#______________________________________Menu__________________________________#
menubar = Menu()

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Standard",command=Standard)
filemenu.add_command(label = "Scientific",command=Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)


editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "History",command=history)
editmenu.add_command(label = "Clear history",command=chistory)

helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "About", menu = helpmenu)
helpmenu.add_command(label = "About Calculator",command=credit)



root.config(menu = menubar)
root.mainloop()
