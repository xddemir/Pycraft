print("--Running PycraftRunUtil")
try: # checks all modules are installed
    import tkinter as tk
    from tkinter.ttk import *
    from PIL import Image, ImageTk
    import pygame
    import numpy
    import os
    import sys
    import random
    import time
    from pygame.locals import *
    pygame.init()
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
    import pyautogui
    import psutil
    import pywavefront
    import timeit
    import os
    import sys
    import time
    import random
    import pip
    import subprocess
except Exception as IntError: # is a module is not installed then
    print(IntError)
    try:
        import PycraftInstaller # ...and run the installer (To FIX)
    except:
        crash = True
    else:
        contINT=0
else: # if the modules are installed then:
    contINT=0 # ingnore this and move on to the rest of the program

    if sys.platform == 'win32' or sys.platform == 'win64':
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    base_folder = os.path.dirname(__file__)

    def crash(error, base_folder):
        try:
            base_folder = os.path.dirname(__file__)
            ErrorDoc = open(os.path.join(base_folder,("Data_Files\\errorREPORT.txt")), "r+")
            numOFerrors = len(ErrorDoc.readlines())
            print(numOFerrors)
            ErrorDoc.write(str(error)+"\n")
            errorTOTALforRETURNING = str(ErrorDoc.read())+"\n"+str(error)
            ErrorDoc.close()
            ErrorDoc = open(os.path.join(base_folder,("Data_Files\\errorREPORT.txt")), "r+")
            error = ErrorDoc.read()
            ErrorDoc.close()
            FontSize = int(15)
            Display = pygame.display.set_mode((1200,720))
            pygame.display.set_caption("An Error Occured")
            IconImage = pygame.image.load(os.path.join(base_folder, 'Resources\\Error_Resources\\Icon.jpg'))
            pygame.display.set_icon(IconImage)
            image = pygame.image.load(os.path.join(base_folder, 'Resources\\Error_Resources\\Error_Message.jpg'))
            MessageFont = pygame.font.Font(os.path.join(base_folder, 'Fonts\\Book Antiqua.ttf'), FontSize)
            Clock = pygame.time.Clock()
            while True:
                Display.fill((20,20,20))
                Display.blit(image, (0,0))
                ErrorMessageText = MessageFont.render(str(error), True, (255,0,0))
                ErrorMessageText1 = MessageFont.render(str(error)[0:74], True, (255,0,0))
                ErrorMessageText2 = MessageFont.render(str(error)[74:148], True, (255,0,0))
                ErrorMessageText3 = MessageFont.render(str(error)[148:222], True, (255,0,0))
                ErrorMessageText4 = MessageFont.render(str(error)[222:296], True, (255,0,0))
                ErrorMessageText5 = MessageFont.render(str(error)[296:370], True, (255,0,0))
                ErrorMessageText6 = MessageFont.render(str(error)[370:444], True, (255,0,0))
                ErrorMessageText7 = MessageFont.render(str(error)[444:], True, (255,0,0))
                numOFerrorsText = MessageFont.render(f"This many errors where encountered during the running of the program: {numOFerrors+1}", True, (255,152,0))
                GetFontPixelLengh = 10
                if len(str(error)) <= 74:
                    Display.blit(ErrorMessageText, (GetFontPixelLengh,200))
                    Display.blit(numOFerrorsText, (GetFontPixelLengh,215))
                elif len(str(error)) >= 75:
                    Display.blit(ErrorMessageText1, (GetFontPixelLengh,200))
                    Display.blit(ErrorMessageText2, (GetFontPixelLengh,215))
                    Display.blit(ErrorMessageText3, (GetFontPixelLengh,230))
                    Display.blit(ErrorMessageText4, (GetFontPixelLengh,245))
                    Display.blit(ErrorMessageText5, (GetFontPixelLengh,260))
                    Display.blit(ErrorMessageText6, (GetFontPixelLengh,275))
                    Display.blit(ErrorMessageText7, (GetFontPixelLengh,290))
                    Display.blit(numOFerrorsText, (GetFontPixelLengh,305))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.flip()
                Clock.tick(60)
        except Exception as InternalError:
            print(InternalError)
            sys.exit("Oops something didn't work as intended")
        else:
            contINT=0

    if crash == True:
        crash()
    else:
        contINT=0

    import Pycraft
    crash(error, base_folder)