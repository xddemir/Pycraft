print("--Running PycraftINIT")
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import subprocess, pip, time, sys, os
global root
base_folder = os.path.dirname(__file__)
numOFerrors = open(os.path.join(base_folder,("Data_Files\\errorREPORT.txt")), "w")
numOFerrors.write("Missing modues <<Getting Fixed by Installer>>")
root = Tk()
root.title("Pycraft Setup Wizard")
root.minsize(500,500)
frame = Frame(root)
frame.pack()
leftframe = Frame(root)
leftframe.pack(side=LEFT)
rightframe = Frame(root)
rightframe.pack(side=RIGHT)
title = Label(frame, text="Pycraft", font=("Book Antiqua", 20))
title.pack()

def play():
    global root
    try:
        Display = pygame.display.set_mode((1200, 720))
        Display.fill([255,255,255])
        pygame.display.set_caption("Pycraft | Loading")
        icon = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Icon.jpg")))
        pygame.display.set_icon(icon)
        img = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.JPG"))) # update
        Display.blit(img, (0,0))
        pygame.display.update()
        root.destroy()
        import PycraftRunUtil
    except Exception as error:
        print(error)
    
def install():
    global numOFerrors
    if messagebox.askyesno("Caution!", "Are you sure you want to do that?") == True:
        root = Tk()
        root.title("Pycaft Setup Wizard | Installing Pycraft!")
        root.minsize(500,500)
        title = Label(root, text="Pycraft", font=("Book Antiqua", 20))
        title.pack()
        command = Label(root, text="Sucsessfully Installed:", font=("Book Antiqua", 10))
        command.pack()
        modules = Listbox(root, fg="Green")
        progress = Progressbar(root, orient = HORIZONTAL, length = 300, mode = "determinate")
        ModulesArray = ["pygame", "pyopengl", "numpy", "pywavefront", "timeit", "pyautogui", "matplotlib", "kiwisolver", "six", "cycler", "psutil", "pyparsing", "python-dateutil", "mouseinfo", "pygetwindow", "pymsgbox", "pyperclip", "pyrect", "pytweening", "pyscreeze"]
        for i in range(len(ModulesArray)):
            try:
                subprocess.check_call([sys.executable, "-m","pip","install",ModulesArray[i]], False)
                modules.insert(1, ModulesArray[i])
                progress["value"] += (300/len(ModulesArray))
                root.update_idletasks()
                progress.pack()
                modules.pack()
                root.after(1)
            except Exception as error:
                numOFerrors.write(str(error)+"\n")
        command = Label(root, text="Installation Complete!", font=("Book Antiqua", 10))
        restart = Label(root, text="It is recomended that you re-start your device now", font=("Book Antiqua",10))
        base_folder = os.path.dirname(__file__)
        data = open(os.path.join(base_folder,("Data_Files\\data.txt")),"r+")
        data.seek(0)
        data.truncate()
        data.close()
        data = open(os.path.join(base_folder,("Data_Files\\data.txt")),"r+")
        data.write("False")
        data.close()
        command.pack()
        restart.pack()
        root.after(1)
        time.sleep(3)
        root.destroy()
        play_button = Button(frame, text="Play", command=play)
        play_button.pack()
        root.mainloop()

def update():
    global numOFerrors
    if messagebox.askyesno("Caution!", "Are you sure you want to do that?") == True:
        root = Tk()
        root.title("Pycaft Setup Wizard | Updating Pycraft")
        root.minsize(500,500)
        
        title = Label(root, text="Pycraft", font=("Book Antiqua", 20))
        title.pack()
        command = Label(root, text="Sucsessfully Updated:", font=("Book Antiqua", 10))
        command.pack()
        
        modules = Listbox(root, fg="Red")

        progress = Progressbar(root, orient = HORIZONTAL, length = 300, mode = "determinate") 
        ModulesArray = ["pygame", "pyopengl", "numpy", "pywavefront", "timeit", "pyautogui", "matplotlib", "kiwisolver", "six", "cycler", "psutil", "pyparsing", "python-dateutil", "mouseinfo", "pygetwindow", "pymsgbox", "pyperclip", "pyrect", "pytweening", "pyscreeze"]
        for i in range(len(ModulesArray)):
            try:
                subprocess.check_call([sys.executable, "-m","pip","uninstall",ModulesArray[i]], False)
                modules.insert(1, ModulesArray[i])
                progress["value"] += (300/len(ModulesArray))
                root.update_idletasks()
                progress.pack()
                modules.pack()
                root.after(1)
            except Exception as error:
                numOFerrors.write(str(error)+"\n")
        for j in range(len(ModulesArray)):
            try:
                subprocess.check_call([sys.executable, "-m","pip","install",ModulesArray[i]], False)
                modules.insert(1, ModulesArray[i])
                progress["value"] += (300/len(ModulesArray))
                root.update_idletasks()
                progress.pack()
                modules.pack()
                root.after(1)
            except Exception as error:
                numOFerrors.write(str(error)+"\n")

        command = Label(root, text="Installation Complete!", font=("Book Antiqua", 10))
        command.pack()

        time.sleep(3)
        root.destroy()
        command = Label(root, text="Sucsessfully updated Pycraft", font=("Book Antiqua", 10))
        command.pack()

def uninstall():
    global numOFerrors
    if messagebox.askyesno("Caution!", "Are you sure you want to do that?") == True:
        root = Tk()
        root.title("Pycaft Setup Wizard | Uninstalling Pycraft")
        root.minsize(500,500)
        title = Label(root, text="Pycraft", font=("Book Antiqua", 20))
        title.pack()
        command = Label(root, text="Sucsessfully uninstalled:", font=("Book Antiqua", 10))
        command.pack()
        modules = Listbox(root, fg="Red")
        progress = Progressbar(root, orient = HORIZONTAL, length = 300, mode = "determinate")
        ModulesArray = ["pygame", "pyopengl", "numpy", "pywavefront", "timeit", "pyautogui", "matplotlib", "kiwisolver", "six", "cycler", "psutil", "pyparsing", "python-dateutil", "mouseinfo", "pygetwindow", "pymsgbox", "pyperclip", "pyrect", "pytweening", "pyscreeze"]
        for i in range(len(ModulesArray)):
            try:
                subprocess.check_call([sys.executable, "-m","pip","uninstall",ModulesArray[i]], False)
                modules.insert(1, ModulesArray[i])
                progress["value"] += (300/len(ModulesArray))
                root.update_idletasks()
                progress.pack()
                modules.pack()
                root.after(1)
            except Exception as error:
                numOFerrors.write(str(error)+"\n")
        command = Label(root, text="Sucsessfully Uninstalled", font=("Book Antiqua", 10))
        command.pack()
        time.sleep(3)
        root.destroy()
        root.mainloop()
    os.execl(sys.executable, sys.executable, * sys.argv)
install_button = Button(leftframe, text="Install", command=install)
install_button.pack(side=LEFT, padx=1)
update_button = Button(leftframe, text="Uninstall", command=uninstall)
update_button.pack(side=RIGHT)
uninstall_button = Button(leftframe, text="Update", command=update)
uninstall_button.pack(side=RIGHT, padx=200)
try:
    import pygame, numpy, PIL, timeit, time, random, tkinter, random, os, sys, pip, subprocess, time, OpenGL.GL, OpenGL.GLU, OpenGL.GLUT, pyautogui, psutil
    pygame.init()
except Exception as error:
    numOFerrors.write(str(error))
else:
    play_button = Button(frame, text="Play", command=play)
    play_button.pack()
root.mainloop()