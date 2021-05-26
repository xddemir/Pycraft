print("--Running PycraftInstaller")

import subprocess, pip, time, sys, os
import tkinter as tk
try:
    import pygame
except Exception as error:
    from tkinter import messagebox
    from tkinter.ttk import *
    from tkinter.scrolledtext import ScrolledText

    base_folder = os.path.dirname(__file__)

    root = tk.Tk()

    root.title("Pycraft Instaler Utility | Getting Things Ready")
    root.minsize(600,600)
    root.resizable(False, False)

    title = Label(root, text="Pycraft", font=("Book Antiqua", 60))
    title.pack()

    TermsANDconditions = Label(root, text="Thank you greatly for supporting this project simply by running it, I am sorry in advance for any spelling mistakes. The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your friends however please may I have some credit, just a name would do and if you find any bugs or errors please feel free to comment in the comments section any feedback so I can improve my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo DO NOT TAKE ANY RESPONCIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXERNAL MODULES INSTALLED ONTO YOUR COMPUTER ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM RESPLONCIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVISES MAGAGER OR ADMINISTRATOR TO INSTALL AND USE COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVISE, AND AT ANY POINT NO CONNECTION TO A NETWORK IS REQUIRED, AFTER INSTALLATION, TO RUN THIS PROGRAM. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you", wraplength=900)
    TermsANDconditions.pack()

    title = Label(root, text="Do you agree to the Terms and Conditions above, AND consent to having external modules installed onto your devise?", foreground="red")
    title.pack()

    selected = tk.StringVar()
    r1 = tk.Radiobutton(root, text='Yes', value='1', variable=selected)
    r1.pack()
    r2 = tk.Radiobutton(root, text='No', value='2', variable=selected)
    r2.pack()

    def show_selected_size():
        if selected.get() == "2":
            quit()
        elif selected.get() == "1":
            try:
                subprocess.run(['pip', 'install', 'pygame'])
            except Exception as error:
                print(error)
            finally:
                os.execl(sys.executable, 'python', __file__, *sys.argv[1:])


    button = tk.Button(root, text="Continue", command=show_selected_size)
    button.pack()

    root.mainloop()
else:
    donothing = 0

print("Found Pygame!!!") # continue on with installation here through pygame graphics not crappy tkinter!

pygame.init()

display = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock() # starts running pygame's clock function

while True:
    pygame.display.update()
    clock.tick(FPS)