from tkinter import *
from abAlgorithm import *


window = Tk()
window.title("Computational Software")
# window.configure(background="white")
window.geometry('500x185')

def submit():
    R = int(real.get())
    I = int(imaginary.get())
    N = int(power_text.get())
    Plot = int(plot_text.get())
    XX = []
    YY = []
    algorithm(R,I,N,Plot,XX,YY)



def real_click(event):
    real.delete(0,END)
def imagine_click(event):
    imaginary.delete(0,END)

#creating a label
label1 = Label(window,text="Plotting Complex Numbers", font=('Oswald 40'),fg="#b30000",height=1)
label1.place(x=15, y=0)

label2 = Label(window,text="(            +  i           )", font=('Oswald 40'),fg="#2eb82e",height=1)
label2.place(x=15, y=65)

label3 = Label(window,text="n", font=('Oswald 25'),fg="#2eb82e",height=1)
label3.place(x=290, y=65)

real = Entry(window,bg="#bbff99",fg="navy blue",borderwidth=3)
real.insert(0,"REAL")
real.bind("<Button-1>", real_click)
real.place(x=35, y=75,height=40,width=90)

imaginary = Entry(window,bg="#bbff99",fg="navy blue",borderwidth=3)
imaginary.insert(0,"IMAGINARY")
imaginary.bind("<Button-1>", imagine_click)
imaginary.place(x=190, y=75, height=40,width=90)

# Drop down menu
# power = StringVar()
# power.set("POWER")
# drop  = OptionMenu(window,power,"SQUARE","CUBE")
# drop.place(x=15,y=150,width=150,height=40)

label4 = Label(window,text="value of n: ",font=('Script 25'),fg="#009999")
label4.place(x=15,y=135)

# spinbox for power of the equation
power_text = StringVar(window)
power_text.set("Iterations")
power = Spinbox(window,textvariable=power_text,from_=1,to=20,bg="#BFEFFF",fg="navy blue")
power.place(x=130,y=138,width=50,height=30)

label5 = Label(window,text="Number of plots: ",font=('Script 25'),fg="#009999")
label5.place(x=200,y=135)

# spinbox for number of plots
plot_text = StringVar(window)
plot_text.set("Iterations")
plots = Spinbox(window,textvariable=plot_text,from_=1,to=10,bg="#BFEFFF",fg="navy blue")
plots.place(x=385,y=138,width=50,height=30)

# submit button
submit = Button(window, text="SUBMIT",bg='red',fg="navy blue",activebackground="sky blue",padx=30, pady=30,command=submit)
submit.configure(font=("Bold"))
submit.place(x=330,y=75,height=45)


window.mainloop()
