from tkinter import Tk
from tkinter import Label
import time

sursa= Tk()
sursa.title("ceas digital")

def timp_curent():
    afisare_ceas=time.strftime("%I:%M:%S %p") #afisare timp curent
    ceas_digital.config(text=afisare_ceas)
    ceas_digital.after(200,timp_curent) 


ceas_digital= Label(sursa,font=("Calibri",120),bg="white",fg="black")  #bg-background color, fg-culoare text(foreground color)
ceas_digital.pack()


timp_curent()


sursa.mainloop()


