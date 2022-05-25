"""
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

root = tk.Tk()

style = ttk.Style()
style.configure("Custom.TButton" , foreground="black" ,background="white" , padding=[10, 10, 10, 10] , font = "Verdana 12")
style.configure("Name" , foreground="white" ,background="#00000000" , padding=[10, 10, 10, 10] , font = "Verdana 12")
style.configure("List.TButton" , foreground="white" ,background="#00000000" , padding=[10, 10, 10, 10] , font = "Verdana 12")

        
add_name = ttk.Button(text = "Pridať meno", style = "Custom.TButton")
add_name.grid(row = 0  , column = 0 , sticky = "w" , padx = 15 , pady = 15)

choose_name = tk.Text(root , height=2 , width= 20 )
choose_name.grid( sticky= tk.W ,column=0 , row=1 , padx=15 , pady= 5)

numbers = tk.Text(root , height=2 , width=400)
numbers.grid(sticky= tk.E , column=1 , row=1 , padx=15 , pady= 5)

execute_button = ttk.Button(root, text = "Vylosovať!", style = "Custom.TButton")
execute_button.grid(sticky = tk.S , column = 1 , row = 50 , padx = 0 , pady = 15 )

2) ked sa klikne pridat hraca tak aby to pridalo jednu nadizajnovanu column 
3)treba spravit nejaky ratac poctu kliknuti na dlacidlo a na zaklade toho urcit polohu
4) vytvorit text area kde sa zada cislo kolko sa ma vytvorit columniek
5)to iste co v 3tom kroku
    

def AddNewPlayer():
    print("it work")

add_name.config(command=AddNewPlayer)

root.geometry("850x500")
root.columnconfigure(1 , weight = 1)
root.title("Losovanie")
root.mainloop()

"""
import random

random_number=random.sample(range(0, 13) , 3)

list_1=[1]
list_2=[2]
list_3=[3]
list_4=[4]
list_5=[5]
list_6=[6]
list_7=[7]
list_8=[8]
list_9=[9]
list_10=[10]
list_11=[11]
list_12= [12]


print(random_number)

