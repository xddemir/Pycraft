print("--Inventory")
from tkinter import *

root = Tk()

root.wm_title("Inventory")
root.geometry("1200x720")
root.configure(bg="#999999")

Weapons = Button(root, text="Weapons")
Weapons.place(x=130, y=0)
RWeapons = Button(root, text="Ranged Weapons")
RWeapons.place(x=260, y=0)
Shields = Button(root, text="Shields")
Shields.place(x=390, y=0)
Armour = Button(root, text="Armour")
Armour.place(x=520, y=0)
Food = Button(root, text="Food")
Food.place(x=650, y=0)
Items = Button(root, text="Items")
Items.place(x=780, y=0)
SItems = Button(root, text="Special Items")
SItems.place(x=910, y=0)

root.mainloop()