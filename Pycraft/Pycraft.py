"Numpy arrays now implimented better in map loading to allow for rast in future"
"Version alterations made"
"issues with converting PIL image to bytes for pygame"

print("--Running Pycraft")
try:
    import tkinter as tk
    import tkinter.ttk
    from PIL import Image, ImageTk
    import pygame
    from pygame.locals import *
    import numpy
    import os
    import sys
    import random
    import time
    pygame.init()
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
    import pyautogui
    import psutil
    import pywavefront
    import timeit
    import collisionTheory
    import traceback
    import socket
    import threading
    import datetime
except Exception as error:
    import os, traceback
    base_folder = os.path.dirname(__file__)
    error = ''.join(traceback.format_exception(None, error, error.__traceback__))
    with open(os.path.join(base_folder,("Data_Files\\errorREPORT.txt")), "w") as errorFILE:
        errorFILE.write(str(f"base_folder lines 3&4 and opening error log failed fataly: {error}")+"\n")
try:
    save = 0
    base_folder = os.path.dirname(__file__)
    SaveConfigFile = open(os.path.join(base_folder,("Data_Files\\SaveGameConfig.txt")), "r")
    exec(SaveConfigFile.read())
    SaveConfigFile.close()
    numOFerrors = open(os.path.join(base_folder,("Data_Files\\errorREPORT.txt")), "w")
    Display = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption(f"Pycraft | Pick your theme")
    theme = save["theme"]
    clock = pygame.time.Clock()
    TitleFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 60)
    Title = TitleFont.render("Pycraft", True, (255,255,255))
    MiddleFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30)
    DarkModeFont = MiddleFont.render("Dark", True, (255,255,255))
    LightModeFont = MiddleFont.render("Light", True, (255,255,255))
    icon = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Icon.jpg")))
    pygame.display.set_icon(icon)
    mousebuttondown = False
    while theme == "False":
        Display.fill([30,30,30])
        mX, mY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousebuttondown = True
            if event.type == pygame.MOUSEBUTTONUP:
                mousebuttondown = False
            
        Display.blit(Title,(540,0))
        Display.blit(DarkModeFont, (320, 360))
        Display.blit(LightModeFont, (890, 360))
        DarkRect = pygame.Rect(260, 300, 200, 160)
        pygame.draw.rect(Display, (80,80,80), DarkRect, 3)
        LightRect = pygame.Rect(820, 300, 200, 160)
        pygame.draw.rect(Display, (80,80,80), LightRect, 3)
        if mX >= 260 and mX <= 460 and mY >= 300 and mY <= 460:
            if mousebuttondown == True:
                theme = "dark"
                base_folder = os.path.dirname(__file__)
                pygame.mixer.music.load(os.path.join(base_folder,("Resources\\General_Resources\\Click.mp3")))
                
                pygame.mixer.music.set_volume(50)
                
                pygame.mixer.music.play()
                mousebuttondown = False
        elif mX >= 820 and mX <= 980 and mY >= 300 and mY <= 460:
            if mousebuttondown == True:
                theme = "light"
                base_folder = os.path.dirname(__file__)
                pygame.mixer.music.load(os.path.join(base_folder,("Resources\\General_Resources\\Click.mp3")))
                
                pygame.mixer.music.set_volume(50)
                
                pygame.mixer.music.play()
                mousebuttondown = False
        pygame.display.update()
        clock.tick(60)
    themeArray = [[(255, 255, 255), [30, 30, 30], (80, 80, 80), (237, 125, 49)], [(0, 0, 0), [255, 255, 255], (80, 80, 80), (237, 125, 49)]]
    if theme == "dark":
        FontCol = themeArray[0][0]
        BackgroundCol = themeArray[0][1]
        ShapeCol = themeArray[0][2]
        AccentCol = themeArray[0][3]
    elif theme == "light":
        FontCol = themeArray[1][0]
        BackgroundCol = themeArray[1][1]
        ShapeCol = themeArray[1][2]
        AccentCol = themeArray[1][3]
    pygame.display.set_caption(f"Pycraft | Loading")
    Display.fill(BackgroundCol)
    TitleFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 60)
    Title = TitleFont.render("Pycraft", True, FontCol)
    TitleLoadingFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 35)
    TitleLoading = TitleLoadingFont.render("Loading", True, FontCol)
    Display.blit(Title, (540,0))
    Display.blit(TitleLoading, (593,45))
    pygame.display.flip()


    def LoadingCaption(num, version):
        if num == 0:
            pygame.display.set_caption(f"Pycraft: v{version} | Loading (-)")
        elif num == 1:
            pygame.display.set_caption(f"Pycraft: v{version} | Loading (\)")
        elif num == 2:
            pygame.display.set_caption(f"Pycraft: v{version} | Loading (|)")
        elif num == 3:
            pygame.display.set_caption(f"Pycraft: v{version} | Loading (\)")
        else:
            pygame.display.set_caption(f"Pycraft: v{version} | Loading")


    pygame.display.set_caption(f"Pycraft | Loading (-)")
    version = save["version"]
    LoadingCaption(1, version)
    defLargeOctagon = [(205,142),(51,295),(51,512),(205,666),(422,666),(575,512),(575,295),(422,142)]
    pygame.draw.polygon(Display, ShapeCol, defLargeOctagon, width=2)
    pygame.display.update()
    base_folder = os.path.dirname(__file__)
    LoadingCaption(2, version)
    pygame.display.update()
    pygame.draw.line(Display, ShapeCol, (205,142), (51,512), width=2)
    pygame.display.update()
    LoadingCaption(3, version)
    pygame.display.update()
    rendis = 80
    LoadingCaption(0, version)
    pygame.display.update()
    FPS = save["FPS"]
    LoadingCaption(1, version)
    pygame.draw.line(Display, ShapeCol, (205,142), (205,666), width=2)
    pygame.display.update()
    FOV = save["FOV"]
    LoadingCaption(2, version)
    pygame.display.update()
    cameraANGspeed = save["cameraANGspeed"]
    LoadingCaption(3, version)
    pygame.draw.line(Display, ShapeCol, (205,142), (422,666), width=2)
    pygame.display.update()
    aa = save["aa"]
    LoadingCaption(0, version)
    pygame.display.update()
    RenderFOG = save["RenderFOG"]
    LoadingCaption(1, version)
    pygame.draw.line(Display, ShapeCol, (205,142), (422,666), width=2)
    pygame.display.update()
    FanSky = save["FanSky"]
    LoadingCaption(2, version)
    pygame.display.update()
    FanPart = save["FanPart"]
    LoadingCaption(3, version)
    pygame.draw.line(Display, ShapeCol, (205,142), (575,512), width=2)
    pygame.display.update()
    sound = save["sound"]
    LoadingCaption(0, version)
    pygame.display.update()
    soundVOL = save["soundVOL"]
    LoadingCaption(1, version)
    pygame.draw.line(Display, ShapeCol, (205,142), (575,295), width=2)
    pygame.display.update()
    music = save["music"]
    LoadingCaption(2, version)
    pygame.display.update()
    musicVOL = save["musicVOL"]
    lastRun = save["lastRun"]
    LoadingCaption(3, version)
    pygame.draw.line(Display, ShapeCol, (51,295), (51,512), width=2)
    pygame.display.update()
    devmode = 1
    LoadingCaption(0, version)
    pygame.display.update()
    width, height = 1280, 720
    LoadingCaption(1, version)
    pygame.draw.line(Display, ShapeCol, (51,295), (205,666), width=2)
    pygame.display.update()
    camera_x, camera_y, camera_z = 0,0,0
    LoadingCaption(2, version)
    pygame.display.update()
    G3Dscale = 600000
    LoadingCaption(3, version)
    pygame.draw.line(Display, ShapeCol, (51,295), (422,666), width=2)
    pygame.display.update()
    size = pyautogui.size()
    current_time = datetime.datetime.now() 
    currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"
    if not currentDate == lastRun:
        LoadingCaption(1, version)
        defLargeOctagon = [(205,142),(51,295),(51,512),(205,666),(422,666),(575,512),(575,295),(422,142)]
        pygame.draw.polygon(Display, ShapeCol, defLargeOctagon, width=2)
        pygame.display.update()
        LoadingCaption(2, version)
        pygame.display.update()
        pygame.draw.line(Display, ShapeCol, (205,142), (51,512), width=2)
        pygame.display.update()
        LoadingCaption(3, version)
        pygame.display.update()
        LoadingCaption(0, version)
        pygame.display.update()
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (205,142), (205,666), width=2)
        pygame.display.update()
        LoadingCaption(2, version)
        pygame.display.update()
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (205,142), (422,666), width=2)
        pygame.display.update()
        LoadingCaption(0, version)
        pygame.display.update()
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (205,142), (422,666), width=2)
        pygame.display.update()
        LoadingCaption(2, version)
        pygame.display.update()
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (205,142), (575,512), width=2)
        pygame.display.update()
        LoadingCaption(0, version)
        pygame.display.update()
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (205,142), (575,295), width=2)
        pygame.display.update()
        LoadingCaption(2, version)
        pygame.display.update()
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (51,295), (51,512), width=2)
        pygame.display.update()
        LoadingCaption(0, version)
        pygame.display.update()
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (51,295), (205,666), width=2)
        pygame.display.update()
        LoadingCaption(2, version)
        pygame.display.update()
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (51,295), (422,666), width=2)
        pygame.display.update()
        LoadingCaption(0, version)
        pygame.display.update()
        data = open(os.path.join(base_folder,("Data_Files\\data.txt")),"r+")
        data.close()
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (51,295), (575,512), width=2)
        pygame.display.update()
        data = open(os.path.join(base_folder,("Data_Files\\errorREPORT.txt")),"r+")
        data.close()
        LoadingCaption(2, version)
        try:
            data = open(os.path.join(base_folder,("Data_Files\\SaveGameConfig.txt")), mode ="r+")
            data.close()
        except Exception as error:
            errorIMG = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Saving_ERROR.jpg")))
            Display.blit(errorIMG, (0,-5))
            pygame.display.update()
            pygame.time.wait(4000)
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (51,295), (575,295), width=2)
        pygame.display.update()
        for i in range(60):
            data = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), i)
        LoadingCaption(0, version)
        pygame.display.update()
        data = pygame.image.load(os.path.join(base_folder, "Resources\\Error_Resources\\Error_Message.jpg"))
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (51,295), (422,142), width=2)
        pygame.display.update()
        data = pygame.image.load(os.path.join(base_folder, "Resources\\Error_Resources\\Icon.jpg"))
        LoadingCaption(2, version)
        pygame.display.update()
        data = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\front.jpg"))) # duplicate
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (51,512), (51,295), width=2)
        pygame.display.update()
        data = Image.open(os.path.join(base_folder,("Resources\\Folder_Resources\\FolderIcon.ico")))
        LoadingCaption(0, version)
        pygame.draw.line(Display, ShapeCol, (575,512), (422,142), width=2)
        pygame.display.update()
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (51,512), (205,666), width=2)
        pygame.draw.line(Display, ShapeCol, (51,512), (575,512), width=2)
        pygame.display.update()
        data = pywavefront.Wavefront(os.path.join(base_folder,("Resources\\G3_Resources\\Player\\Man v2.obj")), create_materials=True, collect_faces=True)
        LoadingCaption(2, version)
        pygame.draw.line(Display, ShapeCol, (51,512), (575,295), width=2)
        pygame.display.update()
        data = pywavefront.Wavefront(os.path.join(base_folder,("Resources\\G3_Resources\\Sun\\Sun.obj")), create_materials=True, collect_faces=True)
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (51,512), (422,666), width=2)
        pygame.display.update()
        data = pywavefront.Wavefront(os.path.join(base_folder,("Resources\\G3_Resources\\worldGUI\\Heart_FULL1.obj")), create_materials=True, collect_faces=True)
        LoadingCaption(0, version)
        pygame.draw.line(Display, ShapeCol, (422,666), (575,295), width=2)
        pygame.display.update()
        data = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\front.jpg")))
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (51,512), (422,142), width=2)
        pygame.display.update()
        data = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\back.jpg")))
        LoadingCaption(2, version)
        pygame.draw.line(Display, ShapeCol, (422,666), (422,142), width=2)
        pygame.display.update()
        data = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\left.jpg")))
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (205,666), (51,512), width=2)
        pygame.display.update()
        data = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\right.jpg")))
        LoadingCaption(0, version)
        pygame.draw.line(Display, ShapeCol, (51,295), (422,142), width=2)
        pygame.display.update()
        data = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\top.jpg")))
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (205,666), (51,295), width=2)
        pygame.display.update()
        data = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\bottom.jpg")))
        LoadingCaption(2, version)
        pygame.draw.line(Display, ShapeCol, (51,295), (575,295), width=2)
        pygame.display.update()
        data = pygame.image.load(os.path.join(base_folder, "Resources\\General_Resources\\Icon.jpg"))
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (205,666), (575,512), width=2)
        pygame.display.update()
        data = pygame.image.load(os.path.join(base_folder, "Resources\\General_Resources\\Icon.jpg"))
        LoadingCaption(0, version)
        pygame.draw.line(Display, ShapeCol, (51,295), (575,512), width=2)
        pygame.display.update()
        data = pygame.image.load(os.path.join(base_folder, f"Resources\\General_Resources\\selectorICONlight.jpg"))
        data = pygame.image.load(os.path.join(base_folder, f"Resources\\General_Resources\\selectorICONdark.jpg"))
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (205,666), (575,295), width=2)
        pygame.display.update()
        data = pygame.image.load(os.path.join(base_folder, "Resources\\General_Resources\\Saving_ERROR.jpg"))
        LoadingCaption(2, version)
        pygame.draw.line(Display, ShapeCol, (51,295), (422,666), width=2)
        pygame.display.update()
        data = pygame.image.load(os.path.join(base_folder, "Resources\\General_Resources\\Pycraft_Long_Loading.jpg"))
        pygame.mixer.music.load(os.path.join(base_folder,("Resources\\General_Resources\\InventoryGeneral.mp3")))
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (51,295), (51,512), width=2)
        pygame.display.update()
        data = pygame.image.load(os.path.join(base_folder, "Resources\\General_Resources\\Pycraft_Short_Loading.jpg"))
        data = pygame.mixer.music.load(os.path.join(base_folder,("Resources\\General_Resources\\Click.mp3")))
        data = 0
        LoadingCaption(0, version)
        pygame.draw.line(Display, ShapeCol, (51,295), (205,666), width=2)
        pygame.display.update()
    else:
        defLargeOctagon = [(205,142),(51,295),(51,512),(205,666),(422,666),(575,512),(575,295),(422,142)] # 
        pygame.draw.polygon(Display, ShapeCol, defLargeOctagon, width=2) # 
        pygame.draw.line(Display, ShapeCol, (205,142), (51,512), width=2) # 
        pygame.draw.line(Display, ShapeCol, (205,142), (205,666), width=2) # 
        pygame.draw.line(Display, ShapeCol, (205,142), (422,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (205,142), (575,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (205,142), (575,295), width=2) #

        pygame.draw.line(Display, ShapeCol, (51,295), (51,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (205,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (422,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (575,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (575,295), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (422,142), width=2) #

        pygame.draw.line(Display, ShapeCol, (51,512), (51,295), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,512), (205,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,512), (422,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,512), (575,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,512), (575,295), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,512), (422,142), width=2) #

        pygame.draw.line(Display, ShapeCol, (205,666), (51,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (205,666), (51,295), width=2) # 
        pygame.draw.line(Display, ShapeCol, (205,666), (422,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (205,666), (575,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (205,666), (575,295), width=2) #
        pygame.draw.line(Display, ShapeCol, (205,666), (422,142), width=2) #

        pygame.draw.line(Display, ShapeCol, (51,295), (51,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (205,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (422,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (575,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (575,295), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (422,142), width=2) #

        pygame.draw.line(Display, ShapeCol, (422,666), (422,142), width=2)
        pygame.draw.line(Display, ShapeCol, (422,666), (575,295), width=2)

        pygame.draw.line(Display, ShapeCol, (575,512), (422,142), width=2)

    def Start(FontCol, BackgroundCol, ShapeCol):
        base_folder = os.path.dirname(__file__)
        data = open(os.path.join(base_folder,("Data_Files\\data.txt")),"r+")
        if sys.platform == "win32" or sys.platform == "win64":
            os.environ["SDL_VIDEO_CENTERED"] = "1"
        if data.read() == "False":
            data.seek(0)
            data.truncate()
            data.close()
            data = open(os.path.join(base_folder,("Data_Files\\data.txt")),"r+")
            data.write("True")
            data.close()
            Display = pygame.display.set_mode((width, height))
            fade = pygame.Surface((width, height))
            LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg")))
            Display.blit(LoadingImage, (0,0))
            Display.fill(BackgroundCol)
            pygame.display.set_caption(f"Pycraft: v{version} | Welcome")
            PresentsFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 20)
            PycraftFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 60)
            NameFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 45)
            Display.fill(BackgroundCol)
            pygame.time.wait(2000)
            name = NameFont.render("Thomas Jebson",True,(255,255,255))
            Display.blit(name,(520,360))
            pygame.display.flip()
            pygame.time.wait(2000)
            pygame.event.get()
            name = PresentsFont.render("presents",True,(255,255,255))
            Display.blit(name,(600,400))
            pygame.display.flip()
            pygame.time.wait(4000)
            pygame.event.get()
            Display.fill(BackgroundCol)
            name = PycraftFont.render("Pycraft",True,(255,255,255))
            Display.blit(name,(540,360))
            pygame.display.flip()
            pygame.time.wait(2000)
            pygame.event.get()
            for a in range(360):
                Display.fill(BackgroundCol)
                Display.blit(name,(540,(360-a)))
                pygame.display.flip()
                pygame.time.wait(5)
                pygame.event.get()
            return True
        elif data.read() == "True":
            data.close()
            Display = pygame.display.set_mode((width, height))
            pygame.display.set_caption(f"Pycraft: v{version} | Loading")
            LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg")))
            Display.blit(LoadingImage, (0,0))
            pygame.display.flip()
            return True
        else:
            data.seek(0)
            data.truncate()
            data.close()
            data = open(os.path.join(base_folder,("Data_Files\\data.txt")),"r+")
            data.write("False")
            data.close()
            Display = pygame.display.set_mode((width, height))
            pygame.display.set_caption(f"Pycraft: v{version} | Loading")
            LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg")))
            Display.blit(LoadingImage, (0,0))
            pygame.display.flip()
            return False


    def PlayClickSound(soundVOL):
        base_folder = os.path.dirname(__file__)
        pygame.mixer.music.load(os.path.join(base_folder,("Resources\\General_Resources\\Click.mp3")))
        pygame.mixer.music.set_volume(soundVOL/100)
        pygame.mixer.music.play()


    def PlayInvSound(musicVOL):
        base_folder = os.path.dirname(__file__)
        pygame.mixer.music.load(os.path.join(base_folder,("Resources\\General_Resources\\InventoryGeneral.mp3")))
        if musicVOL >= 50:
            pygame.mixer.music.set_volume((musicVOL-25)/100)
        else:
            pygame.mixer.music.set_volume(musicVOL/100)
        pygame.mixer.music.play()

    
    def PlayAmbientSound(soundVOL):
        base_folder = os.path.dirname(__file__)
        pygame.mixer.music.load(os.path.join(base_folder,("Resources\\G3_Resources\\GameSounds\\FieldAmb.mp3")))
        pygame.mixer.music.set_volume(soundVOL/100)
        pygame.mixer.music.play()


    def settings(themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, FanSky, FanPart, sound, soundVOL, music, musicVOL, theme):
        base_folder = os.path.dirname(__file__)
        Display = pygame.display.set_mode((width, height))
        LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg")))
        Display.blit(LoadingImage, (0,0))
        pygame.display.flip()
        if devmode == 10 or devmode-10 == 0:
            pygame.display.set_caption(f"Pycraft: v{version}: Settings | Developer Mode")
        else:
            pygame.display.set_caption(f"Pycraft: v{version}: Settings")
        VersionFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        MainTitleFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 60)
        LOWFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")),15)
        MEDIUMFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        HIGHFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        ADAPTIVEFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        LightThemeFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        DarkThemeFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        DataFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        data1 = []
        icon = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Icon.jpg")))
        pygame.display.set_icon(icon)
        data2 = []
        data3 = []
        data4 = []
        run = 0
        rerun = 0
        TempMx = 0
        Mx, My = 0,0
        mousebuttondown = False
        aFPS = FPS
        iteration = 1

        LightThemeSelectedColour = FontCol
        DarkThemeSelectedColour = FontCol
        LowModeSelectedColour = FontCol
        MediumModeSelectedColour = FontCol
        HighModeSelectedColour = FontCol
        AdaptiveModeSelectedColour = FontCol
        FPSsliderSelectedColour = FontCol
        FOVsliderSelectedColour = FontCol
        CameraRotationSpeedSliderSelectedColour = FontCol
        AAselectorSelectedColour = FontCol
        RenderFOGSelectorSelectedColour = FontCol
        FancySkiesSelectorSelectedColour = FontCol
        FancyParticlesSelectorSelectedColour = FontCol
        SoundSelectorSelectedColour = FontCol
        SoundSliderSelectedColour = FontCol
        MusicSelectorSelectedColour = FontCol
        MusicSliderSelectedColour = FontCol

        ThemeTimeOut = 0
        ModeTimeOut = 0
        FPSTimeOut = 0
        FOVTimeOut = 0
        CameraRotationSpeedTimeOut = 0
        AATimeOut = 0
        RenderFogTimeOut = 0
        FancySkiesTimeOut = 0
        FancyParticlesTimeOut = 0
        SoundTimeOut = 0
        SoundVolTimeOut = 0
        MusicTimeOut = 0
        MusicVolTimeOut = 0

        SettingsInformationFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)

        while True:
            TempMx = Mx
            iteration += 1
            Mx, My = pygame.mouse.get_pos()
            eFPS = clock.get_fps()
            aFPS += eFPS
            run += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if sound == True:
                        if sound == True:
                            PlayClickSound(soundVOL)
                    return themeArray, FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, FanSky, FanPart, sound, soundVOL, music, musicVOL, theme
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and devmode < 10:
                        devmode += 1
                        if devmode >= 5 and devmode <= 9:
                            pygame.display.set_caption(f"Pycraft: v{version}: Settings | you are: {10-devmode} steps away from being a developer")
                        elif devmode == 10:
                            pygame.display.set_caption(f"Pycraft {version}: Settings | Developer mode | V: 0,00 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
                        else:
                            pygame.display.set_caption(f"Pycraft: v{version}: Settings")
                    if event.key == pygame.K_x:
                        devmode = 1
                        pygame.display.set_caption(f"Pycraft: v{version}: Settings") # sets the caption to default
                    if event.key == pygame.K_q: # detects if "q" key pressed
                        DataWindow = tk.Tk() # sets the tkinter root
                        DataWindow.title("Player Information") # sets the display (window) caption
                        DataWindow.configure(width = 500, height = 300) # sets the window size (not needed (?))
                        DataWindow.configure(bg="lightblue") # sets the background colour
                        VersionData = f"Pycraft: v{version}" # adds the curent version if caption fails
                        CoordinatesData = f"Coordinates: x: {Mx} y: {My} z: 0.0 FacinE: 0.0,0.0,0.0" # gives information about the coordinates of the user
                        FPSData = f"FPS: Actual: {eFPS} Max: {FPS}" # gives the FPS unsimplified before menu opens (pauses everything)
                        VersionData = tk.Label(DataWindow, text=VersionData) # loads this to the currently active Tk window
                        CoordinatesData = tk.Label(DataWindow, text=CoordinatesData) # loads the coordinates data to the GUI
                        FPSData = tk.Label(DataWindow, text=FPSData) # loads the fps data to the window
                        VersionData.grid(row = 0, column = 0, columnspan = 2) # coordinates are given
                        CoordinatesData.grid(row = 1, column = 0, columnspan = 2)
                        FPSData.grid(row = 2, column = 0, columnspan = 2)# END OF COORDINATES SPECIFIED
                        DataWindow.mainloop() # Tkinter will run what happens next until
                        DataWindow.quit() # it is ordered to quit
                    if event.key == pygame.K_x: # detects if x key is pressed
                        devmode = 1 # resets devmode to 1
                        pygame.display.set_caption(f"Pycraft: v{version}: Settings") # and the caption
                elif event.type == pygame.MOUSEBUTTONDOWN: # if the mouse button is down (left)
                    mousebuttondown = True # this variable is set to True
                elif event.type == pygame.MOUSEBUTTONUP: # if the mouse button is up (left)
                    mousebuttondown = False # this variable is set to False
            titletFont = MainTitleFont.render("Pycraft", aa, FontCol) # main title with colour defined with developer mode
            FPStFont = VersionFont.render(f"FPS: Actual: {int(eFPS)} Max: {int(FPS)} Adverage: {int((aFPS/iteration))}",aa, FontCol)
            FOVtFont = VersionFont.render(f"FOV: {FOV}",aa, FontCol)
            CamRottFont = VersionFont.render(f"Camera Rotation Speed: {round(cameraANGspeed,1)}",aa, FontCol) # END OF SETTING TITLE + DATA
            ModetFont = VersionFont.render("Mode;         ,                 ,            ,          .",aa, FontCol) # gives the pre defined settings a location
            AAtFont = VersionFont.render(f"Anti-Aliasing: {aa}",aa, FontCol) # setting title plus data part 2
            RenderFogtFont = VersionFont.render(f"Render Fog: {RenderFOG}",aa, FontCol)
            FancySkytFont = VersionFont.render(f"Fancy Skies: {FanSky}",aa, FontCol)
            FancyParticletFont = VersionFont.render(f"Fancy Partices: {FanPart}",aa, FontCol)
            SoundtFont = VersionFont.render(f"Sound: {sound}",aa, FontCol)
            SoundVoltFont = VersionFont.render(f"Sound Volume: {soundVOL}%",aa, FontCol)
            MusictFont = VersionFont.render(f"Music: {music}",aa, FontCol)
            MusicVoltFont = VersionFont.render(f"Music Volume: {musicVOL}%",aa, FontCol) # END OF SETTING TITLE + DATA 2
            ThemeFont = VersionFont.render(f"Theme:          ,          | Current Theme: {theme}", aa, FontCol)
            ThemeInformationFont = SettingsInformationFont.render("Gives you control over which theme you can use", aa, AccentCol)
            ModeInformationFont = SettingsInformationFont.render("Gives you 4 separate per-sets for settings, Adaptive mode will automatically adjust your settings", aa, AccentCol)
            FPSInformationFont = SettingsInformationFont.render("Controls the maximum frame rate the game will limit to, does not guarantee that FPS unfortunately", aa, AccentCol)
            FOVInformationFont = SettingsInformationFont.render("Controls the FOV of the camera in-game", aa, AccentCol)
            CameraRotationSpeedInformationFont = SettingsInformationFont.render("Controls the rotation speed of the camera in-game (1 is low, 5 is high)", aa, AccentCol)
            AAInformationFont = SettingsInformationFont.render("Enables/Disables anti-aliasing in game and in the GUI, will give you a minor performance improvement, mainly for low powered devices", aa, AccentCol)
            RenderFogInformationFont = SettingsInformationFont.render("Enables/Disables fog effects in game, for a small performance benefit", aa, AccentCol)
            FancySkiesInformationFont = SettingsInformationFont.render("Enables/Disables a fancy sky box for better visuals in game, does not control anti aliasing for the sky box", aa, AccentCol)
            FancyParticlesInformationFont = SettingsInformationFont.render("Enables/Disables particles in game as particles can have a significant performance decrease", aa, AccentCol)
            SoundInformationFont = SettingsInformationFont.render("Enables/Disables sound effects in game, like for example the click sound and footsteps in game", aa, AccentCol)
            SoundVolInformationFont = SettingsInformationFont.render("Controls the volume of the sound effects, where 100% is maximum and 0% is minimum volume", aa, AccentCol)
            MusicInformationFont = SettingsInformationFont.render("Enables/Disables music in game, like for example the GUI music", aa, AccentCol)
            MusicVolInformationFont = SettingsInformationFont.render("Controls the volume of the music, where 100% is maximum and 0% is minimum volume", aa, AccentCol)
            Display.fill(BackgroundCol)
            Display.blit(titletFont, (540,0)) # then the title font
            FPS_rect = pygame.Rect(50, 180, 450, 10)
            FOV_rect = pygame.Rect(50, 230, 450, 10)
            CAM_rect = pygame.Rect(50, 280, 450, 10)
            sound_rect = pygame.Rect(50, 580, 450, 10)
            music_rect = pygame.Rect(50, 680, 450, 10)
            aa_rect = pygame.Rect(50, 330, 50, 10)
            RenderFOG_Rect = pygame.Rect(50, 380, 50, 10)
            Fansky_Rect = pygame.Rect(50, 430, 50, 10)
            FanPart_Rect = pygame.Rect(50, 480, 50, 10)
            sound_Rect = pygame.Rect(50, 530, 50, 10)
            music_Rect = pygame.Rect(50, 630, 50, 10)# end of pygame.Rect()
            pygame.draw.rect(Display, ShapeCol, FPS_rect, 0)
            pygame.draw.rect(Display, ShapeCol, FOV_rect, 0)
            pygame.draw.rect(Display, ShapeCol, CAM_rect, 0)
            pygame.draw.rect(Display, ShapeCol, sound_rect, 0)
            pygame.draw.rect(Display, ShapeCol, music_rect, 0)
            pygame.draw.rect(Display, ShapeCol, aa_rect, 0)
            pygame.draw.rect(Display, ShapeCol, RenderFOG_Rect, 0)
            pygame.draw.rect(Display, ShapeCol, Fansky_Rect, 0)
            pygame.draw.rect(Display, ShapeCol, FanPart_Rect, 0)
            pygame.draw.rect(Display, ShapeCol, sound_Rect, 0)
            pygame.draw.rect(Display, ShapeCol, music_Rect, 0)# end of pygame.draw.rect()]
            if pygame.mixer.get_busy() == True:
                pygame.mixer.music.stop()
            if mousebuttondown == True:
                if My > 180 and My < 190: # same as before but for the FPS slider
                    if Mx > TempMx and FPS < 445: # with a maximum refresh rate of 240 as tech limited
                        FPS += 1
                    elif Mx < TempMx and FPS > 15: # below this number things begin to break...
                        FPS -= 1
                    if FPS < 15:
                        FPS = 16
                    elif FPS > 445:
                        FPS = 444
                    pygame.draw.circle(Display, AccentCol, (int(FPS+45), 185), 9)
                else:
                    pygame.draw.circle(Display, (255,255,255), (int(FPS+45), 185), 9)

                if My > 230 and My < 240:
                    if Mx > TempMx and FOV < 98:
                        FOV += 1
                    elif Mx < TempMx and FOV > 12:
                        FOV -= 1
                    if FOV < 12:
                        FOV = 13
                    elif FOV > 98:
                        FOV = 97
                    pygame.draw.circle(Display, AccentCol, (int(FOV*5), 235), 9)
                else:
                    pygame.draw.circle(Display, (255,255,255), (int(FOV*5), 235), 9)

                if My > 280 and My < 290:
                    if Mx > TempMx and cameraANGspeed < 5.0:
                        cameraANGspeed += 0.1
                    elif Mx < TempMx and cameraANGspeed > 0.0:
                        cameraANGspeed -= 0.1
                    if cameraANGspeed > 5.0:
                        cameraANGspeed = 4.9
                    elif cameraANGspeed < 0:
                        cameraANGspeed = 0.1
                    pygame.draw.circle(Display, AccentCol, (int(cameraANGspeed*89)+45, 285),9)
                else:
                    pygame.draw.circle(Display, (255,255,255), (int(cameraANGspeed*89)+45, 285),9)

                if My > 580 and My < 590 and sound == True:
                    if Mx > TempMx and soundVOL < 100:
                        soundVOL += 1
                    elif Mx < TempMx and soundVOL > 0:
                        soundVOL -= 1
                    if soundVOL > 100:
                        soundVOL = 100
                    elif soundVOL < 0:
                        soundVOL = 0
                    pygame.draw.circle(Display, AccentCol, (int(soundVOL*4.4)+50, 585), 9)
                else:
                    pygame.draw.circle(Display, (255,255,255), (int(soundVOL*4.4)+50, 585), 9)

                if My > 680 and My < 690 and music == True: # there is no point adjusting the music vol when there is none!
                    if Mx > TempMx and musicVOL < 100:
                        musicVOL += 1
                    elif Mx < TempMx and musicVOL > 0:
                        musicVOL -= 1
                    if musicVOL > 100:
                        musicVOL = 100
                    elif musicVOL < 0:
                        musicVOL = 0
                    pygame.draw.circle(Display, AccentCol, (int(musicVOL*4.4)+50, 685), 9)
                else:
                    pygame.draw.circle(Display, (255,255,255), (int(musicVOL*4.4)+50, 685), 9)

                if My > 330 and My < 340: # END OF SLIDER, start of on/off switches, anti-aliasing
                    if aa == True: # if on switch off
                        aa = False # switches off
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                    elif aa == False: # if off switch on
                        aa = True # switches on 
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                if aa == True: # sets the dial/indicator position to 90,335 (x,y) when on
                    pygame.draw.circle(Display, (255, 255, 255), (90, 335), 9)
                    pygame.draw.circle(Display, ShapeCol, (90, 335), 6)
                elif aa == False: # sets the dial/indicator position to 60,335 (x,y) when off
                    pygame.draw.circle(Display, (255, 255, 255), (60, 335), 9)
                    pygame.draw.circle(Display, ShapeCol, (60, 335), 6)

                if My > 380 and My < 390:
                    if RenderFOG == True:
                        RenderFOG = False
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                    elif RenderFOG == False:
                        RenderFOG = True
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                # render fog selection
                if RenderFOG == True:
                    pygame.draw.circle(Display, (255,255,255), (90, 385), 9)
                    pygame.draw.circle(Display, ShapeCol, (90, 385), 6)
                elif RenderFOG == False:
                    pygame.draw.circle(Display, (255,255,255), (60, 385), 9)
                    pygame.draw.circle(Display, ShapeCol, (60, 385), 6)

                if My > 430 and My < 440:
                    if FanSky == True:
                        FanSky = False
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                    elif FanSky == False:
                        FanSky = True
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False

                if FanSky == True:
                    pygame.draw.circle(Display, (255,255,255), (90, 435), 9)
                    pygame.draw.circle(Display, ShapeCol, (90, 435), 6)
                elif FanSky == False:
                    pygame.draw.circle(Display, (255,255,255), (60, 435), 9)
                    pygame.draw.circle(Display, ShapeCol, (60, 435), 6)

                if My > 480 and My < 490:
                    if FanPart == True:
                        FanPart = False
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                    elif FanPart == False:
                        FanPart = True
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False

                if FanPart == True:
                    pygame.draw.circle(Display, (255,255,255), (90, 485), 9)
                    pygame.draw.circle(Display, ShapeCol, (90, 485), 6)
                elif FanPart == False:
                    pygame.draw.circle(Display, (255,255,255), (60, 485), 9)
                    pygame.draw.circle(Display, ShapeCol, (60, 485), 6)

                if My > 530 and My < 540:
                    if sound == True:
                        sound = False
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                    elif sound == False:
                        sound = True
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False

                if sound == True:
                    pygame.draw.circle(Display, (255,255,255), (90, 535), 9)
                    pygame.draw.circle(Display, ShapeCol, (90, 535), 6)
                elif sound == False:
                    pygame.draw.circle(Display, (255,255,255), (60, 535), 9)
                    pygame.draw.circle(Display, ShapeCol, (60, 535), 6)

                if My > 630 and My < 640:
                    if music == True:
                        music = False
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                    elif music == False:
                        music = True
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False

                if music == True:
                    pygame.draw.circle(Display, (255,255,255), (90, 635), 9)
                    pygame.draw.circle(Display, ShapeCol, (90, 635), 6)
                elif music == False:
                    pygame.draw.circle(Display, (255,255,255), (60, 635), 9)
                    pygame.draw.circle(Display, ShapeCol, (60, 635), 6)
            else:
                pygame.draw.circle(Display, (255,255,255), (int(soundVOL*4.4)+50, 585), 9)
                pygame.draw.circle(Display, (255,255,255), (int(FPS+45), 185), 9)
                pygame.draw.circle(Display, (255,255,255), (int(cameraANGspeed*89)+45, 285),9)
                pygame.draw.circle(Display, (255,255,255), (int(FOV*5), 235), 9)
                pygame.draw.circle(Display, (255,255,255), (int(musicVOL*4.4)+50, 685), 9)

                if aa == True: # sets the dial/indicator position to 90,335 (x,y) when on
                    pygame.draw.circle(Display, (255,255,255), (90, 335), 9)
                    pygame.draw.circle(Display, ShapeCol, (90, 335), 6)
                elif aa == False: # sets the dial/indicator position to 60,335 (x,y) when off
                    pygame.draw.circle(Display, (255,255,255), (60, 335), 9)
                    pygame.draw.circle(Display, ShapeCol, (60, 335), 6)

                if RenderFOG == True:
                    pygame.draw.circle(Display, (255,255,255), (90, 385), 9)
                    pygame.draw.circle(Display, ShapeCol, (90, 385), 6)
                elif RenderFOG == False:
                    pygame.draw.circle(Display, (255,255,255), (60, 385), 9)
                    pygame.draw.circle(Display, ShapeCol, (60, 385), 6)

                if FanSky == True:
                    pygame.draw.circle(Display, (255,255,255), (90, 435), 9)
                    pygame.draw.circle(Display, ShapeCol, (90, 435), 6)
                elif FanSky == False:
                    pygame.draw.circle(Display, (255,255,255), (60, 435), 9)
                    pygame.draw.circle(Display, ShapeCol, (60, 435), 6)

                if FanPart == True:
                    pygame.draw.circle(Display, (255,255,255), (90, 485), 9)
                    pygame.draw.circle(Display, ShapeCol, (90, 485), 6)
                elif FanPart == False:
                    pygame.draw.circle(Display, (255,255,255), (60, 485), 9)
                    pygame.draw.circle(Display, ShapeCol, (60, 485), 6)

                if sound == True:
                    pygame.draw.circle(Display, (255,255,255), (90, 535), 9)
                    pygame.draw.circle(Display, ShapeCol, (90, 535), 6)
                elif sound == False:
                    pygame.draw.circle(Display, (255,255,255), (60, 535), 9)
                    pygame.draw.circle(Display, ShapeCol, (60, 535), 6)

                if music == True:
                    pygame.draw.circle(Display, (255,255,255), (90, 635), 9)
                    pygame.draw.circle(Display, ShapeCol, (90, 635), 6)
                elif music == False:
                    pygame.draw.circle(Display, (255,255,255), (60, 635), 9)
                    pygame.draw.circle(Display, ShapeCol, (60, 635), 6)

                if My > 330 and My < 340:
                    AATimeOut += 1
                    if int(AATimeOut/(aFPS/iteration)) >= 1:
                        Display.blit(AAInformationFont, (120, 325))
                    if aa == True:
                        pygame.draw.circle(Display, AccentCol, (90, 335), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 335), 6)
                    elif aa == False:
                        pygame.draw.circle(Display, AccentCol, (60, 335), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 335), 6)
                else:
                    AATimeOut = 0

                if My > 380 and My < 390:
                    RenderFogTimeOut += 1
                    if int(RenderFogTimeOut/(aFPS/iteration)) >= 1:
                        Display.blit(RenderFogInformationFont, (120, 375))
                    if RenderFOG == True:
                        pygame.draw.circle(Display, AccentCol, (90, 385), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 385), 6)
                    elif RenderFOG == False:
                        pygame.draw.circle(Display, AccentCol, (60, 385), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 385), 6)
                else:
                    RenderFogTimeOut = 0

                if My > 430 and My < 440:
                    FancySkiesTimeOut += 1
                    if int(FancySkiesTimeOut/(aFPS/iteration)) >= 1:
                        Display.blit(FancySkiesInformationFont, (120, 425))
                    if FanSky == True:
                        pygame.draw.circle(Display, AccentCol, (90, 435), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 435), 6)
                    elif FanSky == False:
                        pygame.draw.circle(Display, AccentCol, (60, 435), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 435), 6)
                else:
                    FancySkiesTimeOut = 0

                if My > 480 and My < 490:
                    FancyParticlesTimeOut += 1
                    if int(FancyParticlesTimeOut/(aFPS/iteration)) >= 1:
                        Display.blit(FancyParticlesInformationFont, (120, 475))
                    if FanPart == True:
                        pygame.draw.circle(Display, AccentCol, (90, 485), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 485), 6)
                    elif FanPart == False:
                        pygame.draw.circle(Display, AccentCol, (60, 485), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 485), 6)
                else:
                    FancyParticlesTimeOut = 0

                if My > 530 and My < 540:
                    SoundTimeOut += 1
                    if int(SoundTimeOut/(aFPS/iteration)) >= 1:
                        Display.blit(SoundInformationFont, (120, 525))
                    if sound == True:
                        pygame.draw.circle(Display, AccentCol, (90, 535), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 535), 6)
                    elif sound == False:
                        pygame.draw.circle(Display, AccentCol, (60, 535), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 535), 6)
                else:
                    SoundTimeOut = 0

                if My > 630 and My < 640:
                    MusicTimeOut += 1
                    if int(MusicTimeOut/(aFPS/iteration)) >= 1:
                        Display.blit(MusicInformationFont, (120, 625))
                    if music == True:
                        pygame.draw.circle(Display, AccentCol, (90, 635), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 635), 6)
                    elif music == False:
                        pygame.draw.circle(Display, AccentCol, (60, 635), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 635), 6)
                else:
                    MusicTimeOut = 0

            if My >= 65 and My <= 75:
                ThemeTimeOut += 1
                if int(ThemeTimeOut/(aFPS/iteration)) >= 1:
                    Display.blit(ThemeInformationFont, (300, 67))
            else:
                ThemeTimeOut = 0

            if My >= 65 and My <= 75 and Mx >= 55 and Mx <= 95:
                LightTheme = LightThemeFont.render("Light", aa, AccentCol)
                LightThemeFont.set_underline(True)
                if mousebuttondown == True:
                    theme = "light"
                    FontCol = themeArray[1][0]
                    BackgroundCol = themeArray[1][1]
                    ShapeCol = themeArray[1][2]
                    AccentCol = themeArray[1][3]
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
            else:
                LightTheme = LightThemeFont.render("Light", aa, FontCol)
                LightThemeFont.set_underline(False)

            if My >= 65 and My <= 75 and Mx >= 95 and Mx <= 135:
                DarkTheme = DarkThemeFont.render("Dark", aa, AccentCol)
                DarkThemeFont.set_underline(True)
                if mousebuttondown == True:
                    theme = "dark"
                    FontCol = themeArray[0][0]
                    BackgroundCol = themeArray[0][1]
                    ShapeCol = themeArray[0][2]
                    AccentCol = themeArray[0][3]
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
            else:
                DarkTheme = DarkThemeFont.render("Dark", aa, FontCol)
                DarkThemeFont.set_underline(False)

            if My >= 85 and My <= 95:
                ModeTimeOut += 1
                if int(ModeTimeOut/(aFPS/iteration)) >= 1:
                    Display.blit(ModeInformationFont, (300, 85))
            else:
                ModeTimeOut = 0

            if My > 680 and My < 690:
                MusicVolTimeOut += 1
                if int(MusicVolTimeOut/(aFPS/iteration)) >= 1:
                    Display.blit(MusicVolInformationFont, (520, 675))
            else:
                MusicVolTimeOut = 0

            if My > 580 and My < 590:
                SoundVolTimeOut += 1
                if int(SoundVolTimeOut/(aFPS/iteration)) >= 1:
                    Display.blit(SoundVolInformationFont, (520, 575))
            else:
                SoundVolTimeOut = 0

            if My > 280 and My < 290:
                CameraRotationSpeedTimeOut += 1
                if int(CameraRotationSpeedTimeOut/(aFPS/iteration)) >= 1:
                    Display.blit(CameraRotationSpeedInformationFont, (520, 275))
            else:
                CameraRotationSpeedTimeOut = 0

            if My > 230 and My < 240:
                FOVTimeOut += 1
                if int(FOVTimeOut/(aFPS/iteration)) >= 1:
                    Display.blit(FOVInformationFont, (520, 225))
            else:
                FOVTimeOut = 0

            if My > 180 and My < 190:
                FPSTimeOut += 1
                if int(FPSTimeOut/(aFPS/iteration)) >= 1:
                    Display.blit(FPSInformationFont, (520, 175))
            else:
                FPSTimeOut = 0

            if My >= 85 and My <= 95 and Mx >= 40 and Mx <= 80:
                LOWtFont = LOWFont.render("Low",aa, AccentCol)
                LOWFont.set_underline(True)
                if mousebuttondown == True:
                    rendis = 60
                    FPS = random.randint(15,30)
                    aa = False
                    RenderFOG = False
                    FanSky = False
                    FanPart = False
                    mousebuttondown = False
                    if sound == True:
                        PlayClickSound(soundVOL)
            else:
                LOWtFont = LOWFont.render("Low",aa, FontCol)
                LOWFont.set_underline(False)

            if My >= 85 and My <= 95 and Mx >= 90 and Mx <= 155:
                MEDIUMtFont = MEDIUMFont.render("Medium",aa, AccentCol)
                MEDIUMFont.set_underline(True)
                if mousebuttondown == True:
                    rendis = 80
                    FPS = random.randint(30,60)
                    aa = True
                    RenderFOG = False
                    FanSky = True
                    FanPart = False
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
            else:
                MEDIUMtFont = MEDIUMFont.render("Medium",aa, FontCol)
                MEDIUMFont.set_underline(False)

            if My >= 85 and My <= 95 and Mx >= 165 and Mx <= 205:
                HIGHFontText = HIGHFont.render("High",aa, AccentCol)
                HIGHFont.set_underline(True)
                if mousebuttondown == True:
                    rendis = 100
                    FPS = random.randint(60, 120)
                    aa = True
                    RenderFOG = True
                    FanSky = True
                    FanPart = True
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
            else:
                HIGHFontText = HIGHFont.render("High",aa, FontCol)
                HIGHFont.set_underline(False)

            if My >= 85 and My <= 95 and Mx >= 215 and Mx <= 300:
                ADAPTIVEtFont = ADAPTIVEFont.render("Adaptive",aa, AccentCol)
                ADAPTIVEFont.set_underline(True)
                if mousebuttondown == True:
                    rendis = (psutil.cpu_freq(percpu=True)[0][2])/20
                    FPS = (psutil.cpu_freq(percpu=True)[0][2])/35
                    if (psutil.cpu_freq(percpu=True)[0][2])/10 > 300 and psutil.virtual_memory().total > 8589934592:
                        aa = True
                        RenderFog = True
                        FanSky = True
                        FanPart = True
                    elif (psutil.cpu_freq(percpu=True)[0][2]) > 200 and psutil.virtual_memory().total > 4294967296:
                        aa = True
                        RenderFog = True
                        FanSky = True
                        FanPart = False
                    elif (psutil.cpu_freq(percpu=True)[0][2]) > 100 and psutil.virtual_memory().total > 2147483648:
                        aa = False
                        RenderFog = False
                        FanSky = True
                        FanPart = False
                    elif (psutil.cpu.frequ(percpu=True)[0][2]) < 100 and (psutil.cpu.freq(percpu=True)[0][2]) > 75 and psutil.virtual_memory().total > 1073741824:
                        aa = False
                        RenderFog = False
                        FanSky = False
                        FanPart = False
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
            else:
                ADAPTIVEtFont = ADAPTIVEFont.render("Adaptive",aa, FontCol)
                ADAPTIVEFont.set_underline(False)

            Display.blit(FPStFont, (0,150))
            Display.blit(FOVtFont, (0,200))
            Display.blit(CamRottFont, (0,250))
            Display.blit(ModetFont, (0,85)) # then the pre set modes
            Display.blit(LOWtFont, (48,85))
            Display.blit(MEDIUMtFont, (90,85))
            Display.blit(HIGHFontText, (165,85))
            Display.blit(ADAPTIVEtFont, (215,85)) # then continues with the settings 
            Display.blit(AAtFont, (0,300))
            Display.blit(RenderFogtFont, (0,350))
            Display.blit(FancySkytFont, (0,400))
            Display.blit(FancyParticletFont, (0,450))
            Display.blit(SoundtFont, (0,500))
            Display.blit(SoundVoltFont, (0,550))
            Display.blit(MusictFont, (0,600))
            Display.blit(MusicVoltFont, (0,650))
            Display.blit(ThemeFont, (0, 65))
            Display.blit(LightTheme, (55, 65))
            Display.blit(DarkTheme, (95, 65))
            pygame.draw.circle(Display, ShapeCol, (int(FPS+45), 185), 6)
            pygame.draw.circle(Display, ShapeCol, (int(FOV*5), 235), 6)
            pygame.draw.circle(Display, ShapeCol, (int(cameraANGspeed*89)+45, 285), 6)
            pygame.draw.circle(Display, ShapeCol, (int(soundVOL*4.4)+50, 585), 6)
            pygame.draw.circle(Display, ShapeCol, (int(musicVOL*4.4)+50, 685), 6)
            if devmode == 10 or devmode-10 == 0:
                pygame.display.set_caption(f"Pycraft: v{version}: Settings | Developer mode | V: 0,0,0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Settings")

            if run >= 1000:
                run = 0
                rerun += 1
            if rerun >= 1:
                try:
                    data1[run] = ([((run/5)+1000), ((450-(eFPS/4))-250)])
                    data2[run] = ([((run/5)+1000), ((450-((psutil.cpu_percent())))-250)])
                    data3[run] = ([((run/5)+1000), ((200-psutil.virtual_memory().percent))+25])
                    data4[run] = ([((run/5)+1000), ((450-((aFPS/iteration)+80)/4)-250)])
                except Exception as error:
                    numOFerrors.write(str(error)+"\n")
            else:
                data1.append([((run/5)+1000), ((450-(eFPS/4)-250))])
                data2.append([((run/5)+1000), ((450-((psutil.cpu_percent())))-250)])
                data3.append([((run/5)+1000), ((200-psutil.virtual_memory().percent))+25])
                data4.append([((run/5)+1000), ((450-(((aFPS/iteration)+80)/4)-250))]) # <- adverage FPS ner metric added!
            if devmode == 10: # checks if devmode is equal to 10
                dev_Rect = pygame.Rect(1000,0,200, 200)
                pygame.draw.rect(Display, (80,80,80), dev_Rect)
                if run >= 10:
                    pygame.draw.lines(Display, (0,255,0), False, (data2))
                    pygame.draw.lines(Display, (255,0,0), False, (data1))
                    pygame.draw.lines(Display, (0,0,255), False, (data3))
                    pygame.draw.lines(Display, (255,0,255), False, (data4))
                    pygame.draw.line(Display, (255,255,255), (((run/5)+1000), 20), (((run/5)+1000), 200))
                runFont = DataFont.render(f"{psutil.virtual_memory().percent} | {str(psutil.cpu_percent())} | {str(run)} | {str(rerun)} | {str(round(eFPS, 2))}", False, (255,255,255)) # stores the advanced data to be used when devmode is enabled
                Display.blit(runFont, (1000,0)) # displays the data in the top left
            pygame.display.flip() # updates the display
            clock.tick(FPS) # sets the refresh rate to cap out at 30 fps


    def Character_Customiser(FontCol, BackgroundCol, ShapeCol, devmode):
        base_folder = os.path.dirname(__file__)
        Home_Screen(devmode) # as nothing is happening here it takes you back to the home screen
        clock.tick(30) # continues the 30 fps rule


    def Achievements(FontCol, BackgroundCol, ShapeCol, devmode):
        base_folder = os.path.dirname(__file__)
        Home_Screen(devmode) # goes back to the home screen
        clock.tick(30) # just continues


    def Credits(FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, aa, FPS, theme, AccentCol):
        base_folder = os.path.dirname(__file__)
        Display = pygame.display.set_mode((width, height))# sets the GUI size
        LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg"))) # load the loading screen (ironic?)
        Display.blit(LoadingImage, (0,0)) # displays the image to the GUI
        pygame.display.flip() # updates the display
        if devmode == 10 or devmode-10 == 0: # if developer mode is enabled
            pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log | Developer Mode | V: 0,00 | FPS: {clock.get_fps()} aFPS: {clock.get_fps()} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())}") # sets the caption to developer mode for the user
        else:# if the developer mode is not enabled then it is set to default
            pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log") # sets the display caption
        VersionFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15) # loads the version font for the pre-sets
        MainTitleFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 60) # loads the main title font
        DataFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        Mx, My = pygame.mouse.get_pos() # gets the mouse position
        data1 = []
        data2 = []
        data3 = []
        data4 = []        
        icon = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Icon.jpg")))
        pygame.display.set_icon(icon)
        run = 0
        rerun = 0
        aFPS = 0
        iteration = 1
        TitleFont = MainTitleFont.render("Pycraft", aa, FontCol) # main title with colour defined with developer mode
        Credits1 = VersionFont.render("Head of Development: Thomas Jebson", aa, FontCol) # start of long font for credits and change-log
        Credits2 = VersionFont.render("Music By: Thomas Jebson", aa, FontCol)
        Credits3 = VersionFont.render("Other Programmers:", aa, FontCol)
        Credits4 = VersionFont.render(" - Pygame: illume, pygameci, takowl", aa, FontCol)
        Credits5 = VersionFont.render(" - PyOpenGL: mcfletch", aa, FontCol)
        Credits6 = VersionFont.render(" - OpenGL: Silicon Graphics, Khronos  Group", aa, FontCol)
        Credits7 = VersionFont.render(" - Python: Python Software Foundation", aa, FontCol)
        Credits8 = VersionFont.render(" - Numpy: ahaldane, charlesr.harris, matthew.brett, mattip, rgommers, teoliphant", aa, FontCol)
        Credits9 = VersionFont.render(" - PIL / pillow / Python Imaging Libary: aclark, hugovk, radarhere, wiredfool", aa, FontCol)
        Credits10 = VersionFont.render(" - PyAutoGUI: AlSweigart", aa, FontCol)
        Credits11 = VersionFont.render(" - Matplotlib: ivanov, matthew.brett, mdbloom, QuLogic, Thomas.Caswell", aa, FontCol)
        Credits12 = VersionFont.render(" - Kiwisolver: mdartiaih, sccolbert", aa, FontCol)
        Credits13 = VersionFont.render(" - Six: gutworth", aa, FontCol)
        Credits14 = VersionFont.render(" - cycler: matthew.brett, mdbloom2, Thomas.Caswell", aa, FontCol)
        Credits15 = VersionFont.render(" - pyparsing: ptmcg", aa, FontCol)
        Credits16 = VersionFont.render(" - python-dateutil: dateutilbot, jarondl, pganssle, tpievila", aa, FontCol)
        Credits17 = VersionFont.render(" - mouseinfo: AlSweigart", aa, FontCol)
        Credits18 = VersionFont.render(" - pygetwindow: AlSweigart", aa, FontCol)
        Credits19 = VersionFont.render(" - pymsgbox: AlSweigart", aa, FontCol)
        Credits20 = VersionFont.render(" - pyperclip: AlSweigart, cblgh", aa, FontCol)
        Credits21 = VersionFont.render(" - pyrect: AlSweigart", aa, FontCol)
        Credits22 = VersionFont.render(" - pyscreeze: AlSweigart", aa, FontCol)
        Credits23 = VersionFont.render(" - pytweening: AlSweigart", aa, FontCol)
        Credits24 = VersionFont.render(" - pywavefront: einarf, greenmoss", aa, FontCol)
        ChangeLog1 = VersionFont.render("Pre-release (alpha, a):", aa, FontCol)
        ChangeLog2 = VersionFont.render(" - 1 - Created New presentation and experimented with a concept idea about minecraft with curves, along with a story-line and side projects!", aa, FontCol)
        ChangeLog3 = VersionFont.render(" - 2 - Started an online search for a 3d rendering engine and found pythonprogramming.net", aa, FontCol)
        ChangeLog4 = VersionFont.render(" - 3 - started making and understaning OpenGL and my video game", aa, FontCol)
        ChangeLog5 = VersionFont.render(" - 4 - started making multiple cubes on the screen and a jump animation along with w, a, s, d keys for movement", aa, FontCol)
        ChangeLog6 = VersionFont.render(" - 5 - New naming system, day of the month, first letter of the game, version, month, -, year, version (a/b)", aa, FontCol)
        ChangeLog7 = VersionFont.render(" - 28p0606-20a - added a home screen, credits and changelog along with buttons", aa, FontCol)
        ChangeLog8 = VersionFont.render(" - 04p0707-20a - added a settings menu, started on sounds and a (very) rudimentary physics engine, it's been 7 days since programming started", aa, FontCol)
        ChangeLog9 = VersionFont.render(" - 07p0807-20a - completely re-programmed the entire program, cleaned it up, comments and +10 FPS", aa, FontCol)
        ChangeLog10 = VersionFont.render(" - 17p0907-20a - added skybox, better keypresses, started work on OpenGL .obj rendering and CAD of Map", aa, FontCol) # END OF LONG FONT FOR CREDITS AND CHANGE-LOG
        ChangeLog11 = VersionFont.render(" - 21p1003-21a - Big update, better graphics, rudimentary working inventory, themes, performance improvements, better graphics, smaller file size, and a bunch more!", aa, FontCol)
        VisualYdisplacement = 0
        while True: # main game loop
            eFPS = clock.get_fps()
            aFPS += eFPS # gets the current FPS limmited to 30
            Mx, My = pygame.mouse.get_pos() # gets the mouse position
            run += 1
            iteration += 1
            if pygame.mixer.music.get_busy() == False:
                if music == True:
                    PlayInvSound(musicVOL)
            for event in pygame.event.get(): # detects events, (keypresses, display interactions, mousebutton presses, ect.)
                if event.type == pygame.QUIT or VisualYdisplacement <= -556: # if the "x" in the corner is pressed then;
                    if sound == True:
                        PlayClickSound(soundVOL)
                    Home_Screen(themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, musicVOL, camera_x, camera_y, camera_z, size, theme, lastRun) # goes back to the home screen
                elif event.type == pygame.KEYDOWN: # detects keypresses
                    if event.key == pygame.K_SPACE and devmode < 10: # if developer mode is getting enabled...
                        devmode += 1 # increases the devmode value
                        if devmode >= 5 and devmode <= 9: # if devmode is getting enabled then 
                            pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log | you are: {10-devmode} steps away from being a developer") # tells the user that they are enabling devmode
                        elif devmode == 10: # if devmode is enabled then 
                            pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log | Developer mode | V: 0,00 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())}") # tells the user
                        else:# if the developer mode is not enabled then it is set to default
                            pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log") # sets the display caption
                    if event.key == pygame.K_q: # detects if "q" key pressed
                        DataWindow = tk.Tk() # sets the tkinter root
                        DataWindow.title("Player Information") # sets the display (window) caption
                        DataWindow.configure(width = 500, height = 300) # sets the window size (not needed (?))
                        DataWindow.configure(bg="lightblue") # sets the background colour
                        VersionData = f"Pycraft: v{version}" # adds the curent version if caption fails
                        CoordinatesData = f"Coordinates: x: {Mx} y: {My} z: 0.0 FacinE: 0.0,0.0,0.0" # gives information about the coordinates of the user
                        FPSData = f"FPS: Actual: {eFPS} Max: {FPS}" # gives the FPS unsimplified before menu opens (pauses everything)
                        VersionData = tk.Label(DataWindow, text=VersionData) # loads this to the currently active Tk window
                        CoordinatesData = tk.Label(DataWindow, text=CoordinatesData) # loads the coordinates data to the GUI
                        FPSData = tk.Label(DataWindow, text=FPSData) # loads the fps data to the window
                        VersionData.grid(row = 0, column = 0, columnspan = 2) # coordinates are given
                        CoordinatesData.grid(row = 1, column = 0, columnspan = 2)
                        FPSData.grid(row = 2, column = 0, columnspan = 2)# END OF COORDINATES SPECIFIED
                        DataWindow.mainloop() # Tkinter will run what happens next until
                        DataWindow.quit() # it is ordered to quit
                    if event.key == pygame.K_x: # detects if x key is pressed
                        devmode = 1 # resets devmode to 1
                        pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log") # and the caption
            Display.fill(BackgroundCol)
            Display.blit(Credits1, (0,100+VisualYdisplacement))
            Display.blit(Credits2, (0,115+VisualYdisplacement))
            Display.blit(Credits3, (0,130+VisualYdisplacement))
            Display.blit(Credits4, (0,145+VisualYdisplacement))
            Display.blit(Credits5, (0,160+VisualYdisplacement))
            Display.blit(Credits6, (0,175+VisualYdisplacement))
            Display.blit(Credits7, (0,190+VisualYdisplacement))
            Display.blit(Credits8, (0,205+VisualYdisplacement))
            Display.blit(Credits9, (0,220+VisualYdisplacement))
            Display.blit(Credits10, (0,235+VisualYdisplacement))
            Display.blit(Credits11, (0,250+VisualYdisplacement))
            Display.blit(Credits12, (0,265+VisualYdisplacement))
            Display.blit(Credits13, (0,280+VisualYdisplacement))
            Display.blit(Credits14, (0,295+VisualYdisplacement))
            Display.blit(Credits15, (0,310+VisualYdisplacement))
            Display.blit(Credits16, (0,325+VisualYdisplacement))
            Display.blit(Credits17, (0,340+VisualYdisplacement))
            Display.blit(Credits18, (0,355+VisualYdisplacement))
            Display.blit(Credits19, (0,370+VisualYdisplacement))
            Display.blit(Credits20, (0,385+VisualYdisplacement))
            Display.blit(Credits21, (0,400+VisualYdisplacement))
            Display.blit(Credits22, (0,415+VisualYdisplacement))
            Display.blit(Credits23, (0,430+VisualYdisplacement))
            Display.blit(Credits24, (0,445+VisualYdisplacement))
            Display.blit(ChangeLog1, (0,470+VisualYdisplacement))
            Display.blit(ChangeLog2, (0,485+VisualYdisplacement))
            Display.blit(ChangeLog3, (0,500+VisualYdisplacement))
            Display.blit(ChangeLog4, (0,515+VisualYdisplacement))
            Display.blit(ChangeLog5, (0,530+VisualYdisplacement))
            Display.blit(ChangeLog6, (0,545+VisualYdisplacement))
            Display.blit(ChangeLog7, (0,560+VisualYdisplacement))
            Display.blit(ChangeLog8, (0,575+VisualYdisplacement))
            Display.blit(ChangeLog9, (0,590+VisualYdisplacement))
            Display.blit(ChangeLog10, (0,605+VisualYdisplacement)) # END OF ADDING DATA TO THE DISPLAY  
            Display.blit(ChangeLog11, (0,620+VisualYdisplacement))
            VisualYdisplacement -= 0.2
            cover_Rect = pygame.Rect(0,0,1280, 80)
            pygame.draw.rect(Display, (BackgroundCol), cover_Rect)
            Display.blit(TitleFont, (540,0))
            if devmode == 10 or devmode-10 == 0:
                pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log | Developer mode | V: 0,0,0 | FPS: {int(eFPS)} aFPS {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())}")
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log")
            if run >= 1000:
                run = 0
                rerun += 1
            if rerun >= 1:
                try:
                    data1[run] = ([((run/5)+1000), ((450-(eFPS/4))-250)])
                    data2[run] = ([((run/5)+1000), ((450-((psutil.cpu_percent())))-250)])
                    data3[run] = ([((run/5)+1000), ((200-psutil.virtual_memory().percent))+25])
                    data4[run] = ([((run/5)+1000), ((450-((aFPS/iteration))/4)-250)])
                except Exception as error:
                    numOFerrors.write(str(error)+"\n")
            else:
                data1.append([((run/5)+1000), ((450-(eFPS/4))-250)])
                data2.append([((run/5)+1000), ((450-((psutil.cpu_percent())))-250)])
                data3.append([((run/5)+1000), ((200-psutil.virtual_memory().percent))+25])
                data4.append([((run/5)+1000), ((450-((aFPS/iteration))/4)-250)])
            if devmode == 10: # checks if devmode is equal to 10
                dev_Rect = pygame.Rect(1000,0,200, 200)
                pygame.draw.rect(Display, (80,80,80), dev_Rect)
                if run >= 10:
                    pygame.draw.lines(Display, (0,255,0), False, (data2))
                    pygame.draw.lines(Display, (255,0,0), False, (data1))
                    pygame.draw.lines(Display, (0,0,255), False, (data3))
                    pygame.draw.lines(Display, (255,0,255), False, (data4))
                    pygame.draw.line(Display, (255,255,255), (((run/5)+1000), 20), (((run/5)+1000), 200))
                runFont = DataFont.render(f"{psutil.virtual_memory().percent} | {str(psutil.cpu_percent())} | {str(run)} | {str(rerun)} | {str(round(eFPS, 2))}", False, (255,255,255)) # stores the advanced data to be used when devmode is enabled
                Display.blit(runFont, (1000,0)) # displays the data in the top left
            pygame.display.flip() # updates the display
            clock.tick(FPS) # limmists the FPS to 30


    def CreateRose(FontCol, BackgroundCol, ShapeCol, Display):
        defLargeOctagon = [(205,142),(51,295),(51,512),(205,666),(422,666),(575,512),(575,295),(422,142)] # 
        pygame.draw.polygon(Display, ShapeCol, defLargeOctagon, width=2) # 
        pygame.draw.line(Display, ShapeCol, (205,142), (51,512), width=2) # 
        pygame.draw.line(Display, ShapeCol, (205,142), (205,666), width=2) # 
        pygame.draw.line(Display, ShapeCol, (205,142), (422,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (205,142), (575,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (205,142), (575,295), width=2) #

        pygame.draw.line(Display, ShapeCol, (51,295), (51,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (205,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (422,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (575,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (575,295), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (422,142), width=2) #

        pygame.draw.line(Display, ShapeCol, (51,512), (51,295), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,512), (205,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,512), (422,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,512), (575,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,512), (575,295), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,512), (422,142), width=2) #

        pygame.draw.line(Display, ShapeCol, (205,666), (51,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (205,666), (51,295), width=2) # 
        pygame.draw.line(Display, ShapeCol, (205,666), (422,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (205,666), (575,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (205,666), (575,295), width=2) #
        pygame.draw.line(Display, ShapeCol, (205,666), (422,142), width=2) #

        pygame.draw.line(Display, ShapeCol, (51,295), (51,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (205,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (422,666), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (575,512), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (575,295), width=2) #
        pygame.draw.line(Display, ShapeCol, (51,295), (422,142), width=2) #

        pygame.draw.line(Display, ShapeCol, (422,666), (422,142), width=2)
        pygame.draw.line(Display, ShapeCol, (422,666), (575,295), width=2)

        pygame.draw.line(Display, ShapeCol, (575,512), (422,142), width=2)


    def LoadQuickText():
        LoadingTextFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        LoadingText = ["Use W,A,S,D to move", "Use W to move forward", "Use S to move backward", "Use A to move left", "Use D to move right", "Access your inventory with E", "Access your map with R", "Use SPACE to jump", "Did you know there is a light mode?", "Did you know there is a dark mode?", "Check us out on GitHub", "Use ESC to remove camera movement", "Hold W to sprint", "Did you know you can change the sound volume in settings?", "Did you know you can change the music volume in settings?"]
        locat = random.randint(0, (len(LoadingText)-1))
        text = LoadingText[locat]
        return text


    def Home_Screen(themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, MusicVOL, camera_x, camera_y, camera_z, size, theme, lastRun): # creates the home screen module used after the startup
        base_folder = os.path.dirname(__file__)
        data = open(os.path.join(base_folder,("Data_Files\\data.txt")),"r+")
        if data.read() == "True":
            startUP = True
        elif data.read() == "False":
            startUP = Start(FontCol, BackgroundCol, ShapeCol)
        else:
            startUP = Start(FontCol, BackgroundCol, ShapeCol)
        if startUP == False:
            raise Exception("startUP module ran into an error; please try again")
        data.close()
        if sys.platform == "win32" or sys.platform == "win64":
            os.environ["SDL_VIDEO_CENTERED"] = "1"
        Display = pygame.display.set_mode((width, height)) # sets the window size
        LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg"))) # loads the loading screen
        Display.blit(LoadingImage, (0,0)) # renders the loading screen to the display at the position (0,0)
        pygame.display.flip() # updates the display
        if devmode == 10 or devmode-10 == 0: # if developer mode is enabled
            pygame.display.set_caption(f"Pycraft: v{version}: Home Screen | Developer Mode | V: 0,0,0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}") # sets the caption to developer mode for the user
        else:# if the developer mode is not enabled then it is set to default
            pygame.display.set_caption(f"Pycraft: v{version}: Home Screen") # sets the display caption
        icon = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Icon.jpg")))
        pygame.display.set_icon(icon)
        Selector = pygame.image.load(os.path.join(base_folder,(f"Resources\\General_Resources\\selectorICON{theme}.jpg")))
        hover1 = False # sets the underline value of the first button font to false
        hover2 = False # sets the underline value of the seccond button font to false
        hover3 = False # sets the underline value of the third button font to false
        hover4 = False # sets the underline value of the fourth button font to false
        hover5 = False # sets the underline value of the fith button font to false
        mousebuttondown = False # used to tell the if statements later on weather the mouse button is down or not
        current_time = datetime.datetime.now() 
        currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"
        MainTitleFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 60) # loads the title / heading font
        SideFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 24) # loads the "By Thomas Jebson" font
        VersionFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15) # loads the font that displays the version
        ButtonFont1 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # play
        ButtonFont2 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # settings
        ButtonFont3 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # character custom
        ButtonFont4 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # achievements
        ButtonFont5 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # credits and change-log
        DataFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15) # loads the font used for the graph
        LoadingTextFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        data1 = [] # stores the FPS
        data2 = [] # CPU Usage
        data3 = [] # RAM usage
        data4 = [] # stores the adverage fps
        run = 0
        rerun = 0 # defines how many times the run has been greater than 2000
        LoadingGameImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Long_Loading.jpg")))
        if devmode == 10 or devmode-10 == 0: # if developer mode is enabled
            pygame.display.set_caption(f"Pycraft: v{version}: Home | Developer Mode | V: 0,0,0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}") # sets the caption to developer mode for the user
        iteration = 1
        aFPS = FPS
        counter = 0
        oldTHEME = theme
        RErun = True
        while True: # main game loop
            if not oldTHEME == theme:
                Selector = pygame.image.load(os.path.join(base_folder,(f"Resources\\General_Resources\\selectorICON{theme}.jpg")))
                oldTHEME = theme
            if pygame.mixer.music.get_busy() == False:
                if music == True:
                    PlayInvSound(musicVOL)
            counter += 1
            Display.fill(BackgroundCol)
            eFPS = clock.get_fps()
            aFPS += eFPS # gets the refresh rate
            iteration += 1
            Mx, My = pygame.mouse.get_pos() # gets the mouse position
            run += 1 # increases the run value by 1
            PycraftTitle = MainTitleFont.render("Pycraft", aa, FontCol) # loads the title font text
            Name = SideFont.render("By Thomas Jebson", aa, FontCol) # loads the creator name text
            Version = VersionFont.render(f"Version: {version}", aa, FontCol) # loads the version text
            Play = ButtonFont1.render("Play", aa, FontCol) # loads the play text
            Settings = ButtonFont2.render("Settings", aa, FontCol) # loads the settings text
            Character_Customisations = ButtonFont3.render("Character Customisations", aa, FontCol) # loads the char custom text
            Achievements = ButtonFont4.render("Achievements", aa, FontCol) # loads the achievements text
            Credits_and_Change_Log = ButtonFont5.render("Credits and Change-Log", aa, FontCol) # loads the chedits font
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    try:
                        with open(os.path.join(base_folder,("Data_Files\\SaveGameConfig.txt")), mode ="w") as SaveGameConfig:
                            SaveGameConfigDict = {"theme":theme, "version":version, "FPS":FPS, "eFPS":eFPS, "aFPS":(aFPS/counter), "FOV":FOV, "cameraANGspeed":cameraANGspeed, "aa":aa, "RenderFOG":RenderFOG, "FanSky":FanSky, "FanPart":FanPart, "sound":sound, "soundVOL":soundVOL, "music":music, "musicVOL":musicVOL, "X":camera_x, "Y":camera_y, "Z":camera_z, "lastRun":currentDate}
                            SaveGameConfig.write("save = "+str(SaveGameConfigDict))
                    except Exception as error:
                        errorIMG = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Saving_ERROR.jpg")))
                        Display.blit(errorIMG, (0,-5))
                        pygame.display.update()
                        pygame.time.wait(1000)
                    pygame.quit()
                    sys.exit("Thanks for playing")
                    quit()
                elif event.type == pygame.KEYDOWN: # detects keypresses
                    if event.key == pygame.K_SPACE and devmode < 10: # if developer mode is getting enabled...
                        devmode += 1 # increases the devmode value
                        if devmode >= 5 and devmode <= 9: # if devmode is getting enabled then 
                            pygame.display.set_caption(f"Pycraft: v{version}: Home | you are: {10-devmode} steps away from being a developer") # tells the user that they are enabling devmode
                        elif devmode == 10: # if devmode is enabled then 
                            pygame.display.set_caption(f"Pycraft: v{version}: Home | Developer mode | V: 0,0,0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}") # tells the user
                        else:# if the developer mode is not enabled then it is set to default
                            pygame.display.set_caption(f"Pycraft: v{version}: Home") # sets the display caption
                    if event.key == pygame.K_q: # detects if "q" key pressed
                        DataWindow = tk.Tk() # sets the tkinter root
                        DataWindow.title("Player Information") # sets the display (window) caption
                        DataWindow.configure(width = 500, height = 300) # sets the window size (not needed (?))
                        DataWindow.configure(bg="lightblue") # sets the background colour
                        VersionData = f"Pycraft: v{version}" # adds the curent version if caption fails
                        CoordinatesData = f"Coordinates: x: {Mx} y: {My} z: 0.0 FacinE: 0.0,0.0,0.0" # gives information about the coordinates of the user
                        FPSData = f"FPS: Actual: {eFPS} Max: {FPS}" # gives the FPS unsimplified before menu opens (pauses everything)
                        VersionData = tk.Label(DataWindow, text=VersionData) # loads this to the currently active Tk window
                        CoordinatesData = tk.Label(DataWindow, text=CoordinatesData) # loads the coordinates data to the GUI
                        FPSData = tk.Label(DataWindow, text=FPSData) # loads the fps data to the window
                        VersionData.grid(row = 0, column = 0, columnspan = 2) # coordinates are given
                        CoordinatesData.grid(row = 1, column = 0, columnspan = 2)
                        FPSData.grid(row = 2, column = 0, columnspan = 2)# END OF COORDINATES SPECIFIED
                        DataWindow.mainloop() # Tkinter will run what happens next until
                        DataWindow.quit() # it is ordered to quit
                    if event.key == pygame.K_x: # detects if x key is pressed
                        devmode = 1 # resets devmode to 1
                        pygame.display.set_caption(f"Pycraft: v{version}: Home") # and the caption
                if event.type == pygame.MOUSEBUTTONDOWN: # if the mouse button down
                    mousebuttondown = True # mouse button down is set to True (yes)
                if event.type == pygame.MOUSEBUTTONUP: # if the mouse button is up
                    mousebuttondown = False # this variable is set to no (False)    
            ButtonFont1.set_underline(hover1) # applies an underline value to each button 
            ButtonFont2.set_underline(hover2) # when hovering over it
            ButtonFont3.set_underline(hover3)
            ButtonFont4.set_underline(hover4)
            ButtonFont5.set_underline(hover5)
            if devmode == 10 or devmode-10 == 0:
                pygame.display.set_caption(f"Pycraft: v{version}: Home | Developer mode | V: 0,0,0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Home")

            if My >= 202 and My <= 247 and Mx >= 1155:
                hover1 = True
                if mousebuttondown == True:
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
                    pygame.mixer.music.fadeout(2000)
                    Display.blit(LoadingGameImage, (0,0))
                    pygame.display.flip()
                    if devmode == 10 or devmode-10 == 0:
                        pygame.display.set_caption(f"Pycraft: v{version}: Playing | Developer mode | V: 0,0,0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
                    else:
                        pygame.display.set_caption(f"Pycraft: v{version}: Playing")
                    Load3D = True
                    Map = 0
                    Map_box = 0
                    min_v = 0
                    max_v = 0
                    Map_scale = 0
                    Map_trans = 0
                    Map_size = 0
                    max_Map_size = 0
                    text = LoadQuickText()
                    TextFontRendered = LoadingTextFont.render(f"{text}", aa, FontCol)
                    Display.blit(TextFontRendered, (588,160))
                    main(FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, Display, LoadingGameImage, G3Dscale, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D) # loads the command that happens when clicked
            else: # if you are not hovering over the font
                hover1 = False # hover os set to false
            
            if My >= 252 and My <= 297 and Mx >= 1105: # this repeats for each button
                hover2 = True
                if mousebuttondown == True:
                    Display.blit(LoadingImage, (0,0))
                    pygame.display.flip()
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
                    themeArray, FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, FanSky, FanPart, sound, soundVOL, music, MusicVOL, theme = settings(themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, FanSky, FanPart, sound, soundVOL, music, musicVOL, theme)
            else:
                hover2 = False

            if My >= 302 and My <= 347 and Mx >= 865:
                hover3 = True
                if mousebuttondown == True:
                    print("Character Custom")
                    Display.blit(LoadingImage, (0,0))
                    pygame.display.flip()
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
                    # Char_Custom(FPS)
            else:
                hover3 = False

            if My >= 402 and My <= 447 and Mx >= 1035:
                hover4 = True
                if mousebuttondown == True:
                    print("Achievements")
                    Display.blit(LoadingImage, (0,0))
                    pygame.display.flip()
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
                    #Achievements(FPS)
            else:
                hover4 = False

            if My >= 352 and My <= 397 and Mx >= 880:
                hover5 = True
                if mousebuttondown == True:
                    Display.blit(LoadingImage, (0,0))
                    pygame.display.flip()
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
                    Credits(FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, aa, FPS, theme, AccentCol)
            else:
                hover5 = False

            Display.fill(BackgroundCol)
            Display.blit(PycraftTitle, (540,0))
            Display.blit(Name, (0,690))
            VersionXCalculation = (1280-(len(str(version))*((15*2))))
            Display.blit(Version, (VersionXCalculation, 700))
            Display.blit(Play, (1207, 200))
            
            if hover1 == True:
                Display.blit(Selector, (1155,200))
                #
            Display.blit(Settings, (1160, 250))
            if hover2 == True:
                Display.blit(Selector, (1105,250))
                #
            Display.blit(Character_Customisations, (923, 300))
            if hover3 == True:
                Display.blit(Selector, (865,300))
                #
            Display.blit(Credits_and_Change_Log, (935, 350))
            if hover4 == True:
                Display.blit(Selector, (1033,400)) #1035
                #
            Display.blit(Achievements, (1080, 400))
            if hover5 == True:
                Display.blit(Selector, (888,350)) # credits & change log
                #
            if run >= 1000:
                run = 0
                rerun += 1
            if rerun >= 1:
                try:
                    data1[run] = ([((run/5)+1000), ((450-(eFPS/4))-250)])
                    data2[run] = ([((run/5)+1000), ((450-((psutil.cpu_percent())))-250)])
                    data3[run] = ([((run/5)+1000), ((200-psutil.virtual_memory().percent))+25])
                    data4[run] = ([((run/5)+1000), ((450-((aFPS/iteration))/4)-250)])
                except Exception as error:
                    with open(os.path.join(base_folder,("Data_Files\\errorREPORT.txt")), "w") as errorFILE:
                        errorFILE.write(str(error)+"\n")
            else:
                data1.append([((run/5)+1000), ((450-(eFPS/4))-250)])
                data2.append([((run/5)+1000), ((450-((psutil.cpu_percent())))-250)])
                data3.append([((run/5)+1000), ((200-psutil.virtual_memory().percent))+25])
                data4.append([((run/5)+1000), ((450-((aFPS/iteration))/4)-250)])
            if devmode == 10: # checks if devmode is equal to 10
                dev_Rect = pygame.Rect(1000,0,200, 200)
                pygame.draw.rect(Display, (80,80,80), dev_Rect)
                if run >= 10:
                    pygame.draw.lines(Display, (0,255,0), False, (data2))
                    pygame.draw.lines(Display, (255,0,0), False, (data1))
                    pygame.draw.lines(Display, (0,0,255), False, (data3))
                    pygame.draw.lines(Display, (255,0,255), False, (data4))
                    pygame.draw.line(Display, (255,255,255), (((run/5)+1000), 20), (((run/5)+1000), 200))
                runFont = DataFont.render(f"{psutil.virtual_memory().percent} | {str(psutil.cpu_percent())} | {str(run)} | {str(rerun)} | {str(round(eFPS, 2))}", False, (255,255,255)) # stores the advanced data to be used when devmode is enabled
                Display.blit(runFont, (1000,0)) # displays the data in the top left
            CreateRose(FontCol, BackgroundCol, ShapeCol, Display)
            pygame.display.flip()
            clock.tick(FPS)


    def MapModel(Map, Map_scale, Map_trans, map_vertices):
        glPushMatrix() # creates a new matrix
        glScalef(*Map_scale) # and creates a scale vector (*Map_scale)
        glTranslatef(*Map_trans) # and translates the mesh into view
        for mesh in Map.mesh_list: # then creates the mesh 3D locations
            # here use the array of; mesh.faces to perform rasterisation
            glBegin(GL_TRIANGLES) # loads a oGL file for triangle handling
            MeshFaces = numpy.array(mesh.faces)
            for i in range(0, len(map_vertices), 3):
                glVertex3f(map_vertices[i], map_vertices[i+1], map_vertices[i+2])
            glEnd() # closes the oGL file GL_TRIANGLES
        glPopMatrix() # adds the entire thing to the 3D "world"


    def LoadMapTexture(aa):
        base_folder = os.path.dirname(__file__)
        if aa == True:
            file = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\Map\\GrassTexture.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512,512), Image.ANTIALIAS) # GrassTexture.jpg
            texture = file.tobytes() # converts the loaded and edited image to binary
        if aa == False:
            file = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\Map\\GrassTexture.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512,512))
            texture = file.tobytes() # converts the loaded and edited image to binary
        glGenTextures(7, texture) # loads the texture
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, 7) # binds the texture to the cube
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1) # alligns the texture to the cube
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT) # glues the corners to the face vertices top left.
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT) # glues the other side to the face bottom right.
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_R, GL_MIRRORED_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) # makes sure the texture moves and rotates correctly
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        color = [0.0, 1.0, 0.0]
        glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, color)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture) # 512
        glGenerateMipmap(GL_TEXTURE_2D)


    def LoadSkyBox(aa):
        base_folder = os.path.dirname(__file__)
        if aa == True:
            im1 = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\front.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512,512), Image.ANTIALIAS) # loads the image specified, rotates it, then flips it from left to right then resizes it to fit the cube (google a skybox if you don"t understand)
            texture1 = im1.tobytes() # converts the loaded and edited image to binary
            im2 = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\left.jpg"))).rotate(180).resize((512,512)) # loads the image specified and rotates it 180" and resizes it to fit the cube
            texture2 = im2.tobytes() # and again.
            im3 = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\top.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512,512), Image.ANTIALIAS)
            texture3 = im3.tobytes()# and again..
            im4 = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\back.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512,512), Image.ANTIALIAS)
            texture5 = im4.tobytes() # and again...
            im5 = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\right.jpg"))).rotate(180).resize((512,512), Image.ANTIALIAS)
            texture4 = im5.tobytes() # and again....
            im6 = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\bottom.jpg"))).resize((512,512), Image.ANTIALIAS)
            texture6 = im6.tobytes() # and again.....
        if aa == False:
            im1 = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\front.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512,512)) # loads the image specified, rotates it, then flips it from left to right then resizes it to fit the cube (google a skybox if you don"t understand)
            texture1 = im1.tobytes() # converts the loaded and edited image to denary
            im2 = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\left.jpg"))).rotate(180).resize((512,512)) # loads the image specified and rotates it 180" and resizes it to fit the cube
            texture2 = im2.tobytes() # and again.
            im3 = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\top.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512,512))
            texture3 = im3.tobytes()# and again..
            im4 = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\back.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512,512))
            texture5 = im4.tobytes() # and again...
            im5 = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\right.jpg"))).rotate(180).resize((512,512))
            texture4 = im5.tobytes() # and again....
            im6 = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\bottom.jpg"))).resize((512,512))
            texture6 = im6.tobytes() # and again.....
        # clamps the texture 1 (img1, front) to the cube face
        glGenTextures(1) # loads the texture
        glBindTexture(GL_TEXTURE_2D, 1) # binds the texture to the cube
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1) # alligns the texture to the cube
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP) # glues the corners to the face vertices top left
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP) # glues the other side to the face bottom right.
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) # makes sure the texture moves and rotates correctly
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture1) # blits the texture to the cube (renders)
        # clamps the texture 2 (img2, left) to the correct face
        glGenTextures(2)
        glBindTexture(GL_TEXTURE_2D, 2)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture2)
        # clamps the texture 3 (img3, top) to the correct face
        glGenTextures(3)
        glBindTexture(GL_TEXTURE_2D, 3)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture3)
        # clams the texture 4 (img4, back) to the correct face
        glGenTextures(4)
        glBindTexture(GL_TEXTURE_2D, 4)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture4)
        # clamps the texture 5 (img 5, right) to the correct face
        glGenTextures(5)
        glBindTexture(GL_TEXTURE_2D, 5)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture5)
        # clamps the texture 6 (img6, bottom) to the correct face
        glGenTextures(6)
        glBindTexture(GL_TEXTURE_2D, 6)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture6)


    def DrawMapTexture(camera_x, camera_y, camera_z):
        glEnable(GL_TEXTURE_2D)
        glColor3f(1, 1, 1)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, 7)


    def DrawSkyBox():
        glEnable(GL_TEXTURE_2D) # allows 2D images
        glColor3f(1,1,1) # sets the colour of all the surface to white (clears the cube of all texture)
        # c1 Front
        glBindTexture(GL_TEXTURE_2D, 1) # binds the texture to the cube
        glBegin(GL_QUADS) # opens the oGL file
        glTexCoord2f(0, 0) # sets the image coords to 0,0
        glVertex3f(-10.0, -10.0-50000, -10.0) # loads the image at the points 
        glTexCoord2f(1, 0) # takes a 3D location and converts the coords into a 2D location
        glVertex3f(10.0, -10.0-50000, -10.0)
        glTexCoord2f(1, 1)
        glVertex3f(10.0, 10.0-50000, -10.0)
        glTexCoord2f(0, 1)
        glVertex3f(-10.0, 10.0-50000, -10.0)
        glEnd() # closes the file

        glBindTexture(GL_TEXTURE_2D, 0) # empties the RAM of the image as it is now stored in an oGL file
        # c2 Left Side
        glBindTexture(GL_TEXTURE_2D, 2)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-10.0, -10.0-50000, -10.0)
        glTexCoord2f(1, 0)
        glVertex3f(-10.0, -10.0-50000, 10.0)
        glTexCoord2f(1, 1)
        glVertex3f(-10.0, 10.0-50000, 10.0)
        glTexCoord2f(0, 1)
        glVertex3f(-10.0, 10.0-50000, -10.0)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        # c3 Top
        glBindTexture(GL_TEXTURE_2D, 3)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-10.0, 10.0-50000, -10.0)
        glTexCoord2f(1, 0)
        glVertex3f(10.0, 10.0-50000, -10.0)
        glTexCoord2f(1, 1)
        glVertex3f(10.0, 10.0-50000, 10.0)
        glTexCoord2f(0, 1)
        glVertex3f(-10.0, 10.0-50000, 10.0)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        # c4 Right Side
        glBindTexture(GL_TEXTURE_2D, 4)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(10.0, -10.0-50000, 10.0)
        glTexCoord2f(1, 0)
        glVertex3f(10.0, -10.0-50000, -10.0)
        glTexCoord2f(1, 1)
        glVertex3f(10.0, 10.0-50000, -10.0)
        glTexCoord2f(0, 1)
        glVertex3f(10.0, 10.0-50000, 10.0)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        # c5 Back
        glBindTexture(GL_TEXTURE_2D, 5)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(10.0, -10.0-50000, 10.0)
        glTexCoord2f(1, 0)
        glVertex3f(-10.0, -10.0-50000, 10.0)
        glTexCoord2f(1, 1)
        glVertex3f(-10.0, 10.0-50000, 10.0)
        glTexCoord2f(0, 1)
        glVertex3f(10.0, 10.0-50000, 10.0)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        # c6 Bottom
        glBindTexture(GL_TEXTURE_2D, 6)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-10.0, -10.0-50000, -10.0)
        glTexCoord2f(1, 0)
        glVertex3f(10.0, -10.0-50000, -10.0)
        glTexCoord2f(1, 1)
        glVertex3f(10.0, -10.0-50000, 10.0)
        glTexCoord2f(0, 1)
        glVertex3f(-10.0, -10.0-50000, 10.0)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, 0)


    def Inventory(FontCol, BackgroundCol, ShapeCol, width, height, aa, version, FPS, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D):
        base_folder = os.path.dirname(__file__)
        Display = pygame.display.set_mode((width, height), pygame.SRCALPHA)
        LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg"))) # loads the loading screen
        Display.blit(LoadingImage, (0,0))
        pygame.display.update()
        MainInventoryFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 60) # loads the title / heading font
        PycraftTitle = MainInventoryFont.render("Pycraft", aa, FontCol) # loads the title font text
        LoadingGameImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Long_Loading.jpg")))
        icon = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Icon.jpg")))
        pygame.display.set_icon(icon)
        AlphaSurface = pygame.Surface((1280,720), HWSURFACE|SRCALPHA) # the size of your rect
        AlphaSurface.set_alpha(204) # alpha level
        AlphaSurface.fill(BackgroundCol) # this fills the entire surface
        Selector = pygame.image.load(os.path.join(base_folder,(f"Resources\\General_Resources\\selectorICON{theme}.jpg")))
        hover1 = False # sets the underline value of the first button font to false
        hover2 = False # sets the underline value of the seccond button font to false
        hover3 = False # sets the underline value of the third button font to false
        hover4 = False # sets the underline value of the fourth button font to false
        hover5 = False # sets the underline value of the fith button font to false
        hover6 = False # sets the underline value of the sixth button font to false
        hover7 = False # sets the underline value of the seventh button font to false
        mousebuttondown = False # used to tell the if statements later on weather the mouse button is down or not
        ButtonFont1 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Weapons
        WeaponsText = ButtonFont1.render("Weapons", aa, FontCol)
        ButtonFont2 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Ranged Weapons
        RangedWeaponsText = ButtonFont2.render("Ranged Weapons", aa, FontCol)
        ButtonFont3 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Shields
        ShieldsText = ButtonFont3.render("Shields", aa, FontCol)
        ButtonFont4 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Armour
        ArmourText = ButtonFont4.render("Armour", aa, FontCol)
        ButtonFont5 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Food
        FoodText = ButtonFont5.render("Food", aa, FontCol)
        ButtonFont6 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Items
        ItemsText = ButtonFont6.render("Items", aa, FontCol)
        ButtonFont7 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Special Items
        SpecialItemsText = ButtonFont7.render("Special Items", aa, FontCol)
        pygame.display.set_caption(f"Pycraft: v{version}: Playing | Inventory")
        storage = Map
        while True:
            Mx, My = pygame.mouse.get_pos() # gets the mouse position
            Display.fill(BackgroundCol)
            PauseIMG = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\PauseIMG.jpg")))
            Display.blit(PauseIMG, (0,0))
            Display.blit(AlphaSurface, (0,0)) # (0,0) are the top-left coordinates
            Display.blit(PycraftTitle, (540,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Load3D = False
                    if sound == True:
                        PlayClickSound(soundVOL)
                    main(FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, Display, LoadingGameImage, G3Dscale, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D)
                if event.type == pygame.MOUSEBUTTONDOWN: # if the mouse button down
                    mousebuttondown = True # mouse button down is set to True (yes)
                if event.type == pygame.MOUSEBUTTONUP: # if the mouse button is up
                    mousebuttondown = False # this variable is set to no (False)
            #
            if My >= 202 and My <= 247 and Mx >= 1155:
                hover1 = True
                if mousebuttondown == True: # if the button is clicked
                    Display.blit(LoadingGameImage, (0,0)) # renders the loading screen
                    pygame.display.flip() # updates the display
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
                    print("")
            else: # if you are not hovering over the font
                hover1 = False # hover is set to false
            if My >= 252 and My <= 297 and Mx >= 1105: # this repeats for each button
                hover2 = True
                if mousebuttondown == True:
                    Display.blit(LoadingImage, (0,0))
                    pygame.display.flip()
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
                    print("")
            else:
                hover2 = False
            if My >= 302 and My <= 347 and Mx >= 865:
                hover3 = True
                if mousebuttondown == True:
                    Display.blit(LoadingImage, (0,0))
                    pygame.display.flip()
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
                    print("")
            else:
                hover3 = False
            if My >= 402 and My <= 447 and Mx >= 1035:
                hover4 = True
                if mousebuttondown == True:
                    Display.blit(LoadingImage, (0,0))
                    pygame.display.flip()
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
                    print("")
            else:
                hover4 = False
            if My >= 352 and My <= 397 and Mx >= 880:
                hover5 = True
                if mousebuttondown == True:
                    Display.blit(LoadingImage, (0,0))
                    pygame.display.flip()
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
                    print("")
            else:
                hover5 = False
            if My >= 502 and My <= 547 and Mx >= 1095:
                hover6 = True
                if mousebuttondown == True:
                    Display.blit(LoadingImage, (0,0))
                    pygame.display.flip()
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
                    print("")
            else:
                hover6 = False
            if My >= 452 and My <= 497 and Mx >= 1095:
                hover7 = True
                if mousebuttondown == True:
                    Display.blit(LoadingImage, (0,0))
                    pygame.display.flip()
                    if sound == True:
                        PlayClickSound(soundVOL)
                    mousebuttondown = False
                    print("")
            else:
                hover7 = False
            #
            ButtonFont1.set_underline(hover1) # applies an underline value to each button
            ButtonFont2.set_underline(hover2) # when hovering over it
            ButtonFont3.set_underline(hover3)
            ButtonFont4.set_underline(hover4)
            ButtonFont5.set_underline(hover5)
            ButtonFont6.set_underline(hover6)
            ButtonFont7.set_underline(hover7)
            AlphaSurface.fill(BackgroundCol) # this fills the entire surface
                #
            Display.blit(WeaponsText, (1150, 200))
            if hover1 == True: # 1
                AlphaSurface.blit(Selector, (1100,200))
                #
            Display.blit(RangedWeaponsText, (1040, 250))
            if hover2 == True: # 2
                AlphaSurface.blit(Selector, (990,250))
                #
            Display.blit(ShieldsText, (1175, 300))
            if hover3 == True: # 3
                AlphaSurface.blit(Selector, (1125,300))
                #
            Display.blit(ArmourText, (1165, 350))
            if hover4 == True: # 5
                AlphaSurface.blit(Selector, (1150,400))
                #
            Display.blit(FoodText, (1205, 400))
            if hover5 == True: # 4
                AlphaSurface.blit(Selector, (1110,350))
                #  
            Display.blit(ItemsText, (1200, 450))
            if hover6 == True: # 7
                AlphaSurface.blit(Selector, (1045, 500))
                #
            Display.blit(SpecialItemsText, (1095, 500))
            if hover7 == True: # 6
                AlphaSurface.blit(Selector, (1150, 450))
            pygame.display.update()
            clock.tick(FPS)
    

    def GetMapPos(camera_x, camera_z):
        x = 0
        z = 0
        if camera_x == 0:
            x = 640
        if camera_z == 0:
            z = 360
        x -= 6
        z -= 19
        return (x,z)


    def MapLoader(FontCol, BackgroundCol, ShapeCol, width, height, aa, version, FPS, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D):
        base_folder = os.path.dirname(__file__)
        Display = pygame.display.set_mode((1280,720))
        LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg"))) # loads the loading screen
        Display.blit(LoadingImage, (0,0))
        pygame.display.update()
        icon = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Icon.jpg")))
        pygame.display.set_icon(icon)
        LoadingGameImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Long_Loading.jpg")))
        MapPIL = Image.open(os.path.join(base_folder,("Resources\\Map_Resources\\Full_Map.png")))
        Map0 = pygame.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)
        MapIcon = pygame.image.load(os.path.join(base_folder,("Resources\\Map_Resources\\Marker.jpg")))
        zoom = 0
        pygame.display.set_caption(f"Pycraft: v{version}: Playing | Map")
        MouseUnlock = True
        X,Y = 0,0
        key = ""
        while True:
            Display.fill(BackgroundCol)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Load3D = False
                    if sound == True:
                        PlayClickSound(soundVOL)
                    main(FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, Display, LoadingGameImage, G3Dscale, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        zoom = 0
                    if event.key == pygame.K_w:
                        key = "w"
                    if event.key == pygame.K_s:
                        key = "s"
                    if event.key == pygame.K_d:
                        key = "d"
                    if event.key == pygame.K_a:
                        key = "a"
                if event.type == pygame.KEYUP:
                    key = ""
                if event.type == pygame.MOUSEWHEEL:
                    if str(event.y)[0] == "-":
                        zoom -= 1
                    else:
                        zoom += 1
            if zoom >= 2:
                zoom = 2
            if zoom <= 0:
                zoom = 0
            if key == "w":
                if zoom == 1:
                    Y -= 5
                elif zoom == 2:
                    Y -= 10
            if key == "s":
                if zoom == 1:
                    Y += 5
                elif zoom == 2:
                    Y += 10
            if key == "d":
                if zoom == 1:
                    X += 5
                elif zoom == 2:
                    X += 10
            if key == "a":
                if zoom == 1:
                    X -= 5
                elif zoom == 2:
                    X -= 10
            if zoom == 0:
                MapPIL = Image.open(os.path.join(base_folder,("Resources\\Map_Resources\\Full_Map.png"))).resize((1280,720), Image.ANTIALIAS)
                Map0 = pygame.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)
                Display.blit(Map0, (0,0))
                Display.blit(MapIcon, GetMapPos(camera_x, camera_z))
                x,y = 0,0
            elif zoom == 1:
                MapPIL = Image.open(os.path.join(base_folder,("Resources\\Map_Resources\\Full_Map.png"))).resize((2240,1260), Image.ANTIALIAS) # .resize((512,512), Image.ANTIALIAS)
                Map0 = pygame.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)
                Display.blit(Map0, (X,Y))
                Display.blit(MapIcon, GetMapPos(camera_x, camera_z))
            elif zoom == 2:
                MapPIL = Image.open(os.path.join(base_folder,("Resources\\Map_Resources\\Full_Map.png"))).resize((2880,1620), Image.ANTIALIAS) # .resize((512,512), Image.ANTIALIAS)
                Map0 = pygame.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)
                Display.blit(Map0, (X,Y))
                Display.blit(MapIcon, GetMapPos(camera_x, camera_z))
            if zoom == 1:
                if X <= -955:
                    X = -955
                if Y <= -535:
                    Y = -535
                if X >= -5:
                    X = -5
                if Y >= -5:
                    Y = -5
            if zoom == 2:
                if X <= -1590:
                    X = -1590
                if Y <= -890:
                    Y = -890
                if X >= -10:
                    X = -10
                if Y >= -10:
                    Y = -10
            pygame.display.update()
            clock.tick(FPS)


    def LoadingMapGraphics(vertex, Map_box, counterFORvertex, LoadingPercent, LoadingFont, LoadingGameImage):
        counterFORvertex += 1
        COMPLETIONpercent = (100/6612)*counterFORvertex
        Init = LoadingFont.render(f"Started Resource Loading | Map: {int(COMPLETIONpercent)}% complete", aa, FontCol)
        Display.blit(LoadingGameImage, (-1,-1))
        Display.blit(Init, (100, 600))
        min_v = [min(Map_box[0][i], vertex[i]) for i in range(3)]
        max_v = [max(Map_box[1][i], vertex[i]) for i in range(3)]
        Map_box = (min_v, max_v)
        return min_v, max_v, Map_box, counterFORvertex


    def main(FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, Display, LoadingGameImage, G3Dscale, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D):
        import time
        base_folder = os.path.dirname(__file__)
        LoadingPercent = 0
        line = []
        LoadingPercent += 100
        LoadingTextFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        line.append((LoadingPercent, 620))
        LoadingPercent += 1
        aFPS = 0
        iteration = 1
        line.append((LoadingPercent, 620))
        Display.blit(LoadingGameImage, (-1,-1))
        pygame.draw.lines(Display, (30, 30, 30), aa, [(95, 620), (1200, 620)], 3)
        pygame.draw.lines(Display, (153,153,153), aa, line)
        LoadingFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        Init = LoadingFont.render("Initiating", aa, FontCol)
        text = LoadQuickText()
        TextFontRendered = LoadingTextFont.render(f"{text}", aa, FontCol)
        Display.blit(TextFontRendered, (588,160))
        Display.blit(Init, (100,640))
        pygame.display.flip()
        Jump = False # tells the game weather to run
        JumpID = 0 # part of the jump animation where the game makes sure that the camera returns to its original position
        CubeNum = 10 # the number of cubes allowed to be rendered into the game
        FOV = 70 # the FOV of the player"s camera
        MouseUnlock = False # defines weather the mouse is tracked or not
        max_distance = 0 # ?
        z = 0 # ?
        run = 0 # defines how mny times the game has been run
        y = -10 # ?
        z = 1 # ?
        x = 0 # ?
        cube_dict = {}
        repeater = True
        display = (1200,720)
        # pygame is initialised
        # diaplay is created, 1200, 720
        # the display is then configuered to allow OpenGL
        LoadingPercent += 165
        line.append((LoadingPercent, 620))
        Display.blit(LoadingGameImage, (-1,-1))
        pygame.draw.lines(Display, (60,60,60), aa, [(95, 620), (1175, 620)], 3)
        pygame.draw.lines(Display, (153,153,153), aa, line)
        Init = LoadingFont.render("Loading...", aa, FontCol)
        Display.blit(Init, (100,640))
        text = LoadQuickText()
        LoadingTextFont.render(f"{text}", aa, FontCol)
        Display.blit(TextFontRendered, (588,160))
        pygame.display.flip()
        if devmode == 10 or devmode-10 == 0:
            pygame.display.set_caption(f"Pycraft: v{version}: Playing | Developer mode | V: 0,0,0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
        else:
            pygame.display.set_caption(f"Pycraft: v{version}: Playing")
        MouseUnlock = True
        Sun_pos_x, Sun_pos_y, Sun_pos_z = 0,10,-20
        LoadingPercent += 115
        line.append((LoadingPercent, 620))
        Display.blit(LoadingGameImage, (-1,-1))
        pygame.draw.lines(Display, (60,60,60), aa, [(95, 620), (1175, 620)], 3)
        pygame.draw.lines(Display, (153,153,153), aa, line)
        Init = LoadingFont.render("Loaded Image Resources", aa, FontCol)
        Display.blit(Init, (100,640))
        text = LoadQuickText()
        LoadingTextFont.render(f"{text}", aa, FontCol)
        Display.blit(TextFontRendered, (588,160))
        pygame.display.flip()
        if devmode == 10 or devmode-10 == 0:
            pygame.display.set_caption(f"Pycraft: v{version}: Playing | Developer mode | V: 0,0,0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
        else:
            pygame.display.set_caption(f"Pycraft: v{version}: Playing")
        #LoadMapTexture()
        counter = 0
        rotationvectX, rotationvectY = 0,0
        # loads the Map
        pygame.event.get()
        LoadingPercent += 115
        line.append((LoadingPercent, 620))
        Display.blit(LoadingGameImage, (-1,-1))
        pygame.draw.lines(Display, (60,60,60), aa, [(95, 620), (1175, 620)], 3)
        pygame.draw.lines(Display, (153,153,153), aa, line)
        Init = LoadingFont.render("Beginning Resource Loading | 0% complete", aa, FontCol)
        Display.blit(Init, (100, 600))
        text = LoadQuickText()
        LoadingTextFont.render(f"{text}", aa, FontCol)
        Display.blit(TextFontRendered, (588,160))
        pygame.display.flip()

        # Map
        if Load3D == True:
            percent = 0
            Map = pywavefront.Wavefront(os.path.join(base_folder,("Resources\\G3_Resources\\Map\\map.obj")), create_materials=True, collect_faces=True) # Map v2.obj
            MapVerts = numpy.array(Map.vertices)
            Map_box = (MapVerts[0], MapVerts[0])
            counterFORvertex = 0
            for vertex in MapVerts:
                min_v, max_v, Map_box, counterFORvertex = LoadingMapGraphics(vertex, Map_box, counterFORvertex, LoadingPercent, LoadingFont, LoadingGameImage)
                
                LoadingPercentForEfficiency = (100/6612)*counterFORvertex
                
                if int(LoadingPercentForEfficiency) == percent:
                    percent += 1
                    LoadingPercent += 0.06+(165/6616)*200
                    Display.blit(TextFontRendered, (588,160))
                    line.append((LoadingPercent, 620))
                    pygame.draw.lines(Display, (60,60,60), aa, [(95, 620), (1175, 620)], 3)
                    pygame.draw.lines(Display, (153,153,153), aa, line)
                    text = LoadQuickText()
                    LoadingTextFont.render(f"{text}", aa, FontCol)
                    Display.blit(TextFontRendered, (588,160))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            StartMenu = pygame.display.set_mode((width, height))
                            LoadingScreen = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg")))
                            StartMenu.blit(LoadingScreen, (0,0))
                            pygame.display.flip()
                            camera_x = 0
                            camera_y = 0
                            camera_z = 0
                            if sound == True:
                                PlayClickSound(soundVOL)
                            Home_Screen(themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, musicVOL, camera_x, camera_y, camera_z, size, theme, lastRun)
            
            '''glGenBuffers(0, 1)
            glBindBuffer(GL_ARRAY_BUFFER, 0)
            glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW)'''
            Map_size = [Map_box[1][i]-Map_box[0][i] for i in range(3)]
            max_Map_size = max(Map_size)
            Map_size = G3Dscale # 10000
            Map_scale = [Map_size/max_Map_size for i in range(3)]
            Map_trans = [-(Map_box[1][i]+Map_box[0][i])/2 for i in range(3)]

        #
            map_vertices = []
            for mesh in Map.mesh_list: # then creates the mesh 3D locations
                for face in mesh.faces: # then creates a face location in 3D locations in oGL "world"
                    for vertex_i in face: # defines the vertex of each face
                        Data = Map.vertices[vertex_i]
                        for k in range(len(Data)):
                            map_vertices.append(Data[k])
        # end
        Display.blit(LoadingGameImage, (-1,-1))
        line.append((LoadingPercent, 620))
        pygame.draw.lines(Display, (60,60,60), aa, [(95, 620), (1175, 620)], 3)
        pygame.draw.lines(Display, (153,153,153), aa, line)
        Init = LoadingFont.render("Resource Loading | Loaded Map", aa, FontCol)
        Display.blit(Init, (100, 600))
        text = LoadQuickText()
        LoadingTextFont.render(f"{text}", aa, FontCol)
        Display.blit(TextFontRendered, (588,160))
        pygame.display.flip()
        if devmode == 10 or devmode-10 == 0:
            pygame.display.set_caption(f"Pycraft: v{version}: Playing | Developer mode | V: 0,0,0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
        else:
            pygame.display.set_caption(f"Pycraft: v{version}: Playing")
        LoadingPercent += 115
        Display.blit(LoadingGameImage, (-1,-1))
        line.append((LoadingPercent, 620))
        pygame.draw.lines(Display, (60,60,60), aa, [(95, 620), (1175, 620)], 3)
        pygame.draw.lines(Display, (153,153,153), aa, line)
        text = LoadQuickText()
        LoadingTextFont.render(f"{text}", aa, FontCol)
        Display.blit(TextFontRendered, (588,160))
        pygame.display.flip()
        run = 0
        pygame.event.get()
        pygame.mouse.set_pos(640,360)
        Total_move_x, Total_move_y, Total_move_z = 0,0,0
        if devmode == 10 or devmode-10 == 0:
            pygame.display.set_caption(f"Pycraft: v{version}: Playing | Developer mode | V: 0,0,0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
        else:
            pygame.display.set_caption(f"Pycraft: v{version}: Playing")
        WKeyPressed, AKeyPressed, SKeyPressed, DKeyPressed = False, False, False, False
        stop = False
        stop1 = False
        counterForWeather = 2
        weather = 0
        LoadingPercent = 1170
        Display.blit(LoadingGameImage, (-1,-1))
        line.append((LoadingPercent, 620))
        pygame.draw.lines(Display, (60,60,60), aa, [(95, 620), (1175, 620)], 3)
        pygame.draw.lines(Display, (153,153,153), aa, line)
        Init = LoadingFont.render("Finished Resource Loading; Rendering", aa, FontCol)
        Display.blit(Init, (100, 600))
        text = LoadQuickText()
        LoadingTextFont.render(f"{text}", aa, FontCol)
        Display.blit(TextFontRendered, (588,160))
        pygame.display.flip()
        pygame.display.set_mode((width, height), DOUBLEBUF|OPENGL)
        LoadSkyBox(aa)
        LoadMapTexture(aa)
        # creates the perspective of the player, incl FOV, render-distance
        gluPerspective(FOV, (display[0]/display[1]), 1, (rendis*100000))
        firstRUN = 0
        pygame.mouse.set_pos(640,360)
        camera_x = 0
        camera_y = 0
        camera_z = 0

        prev_camera_x = camera_x
        prev_camera_y = camera_y
        prev_camera_z = camera_z

        prev_collisions = 0

        collisions = [False, 0]
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_MODELVIEW)
        if aa == True:
            glEnable(GL_MULTISAMPLE)
        elif aa == False:
            glDisable(GL_MULTISAMPLE)
        glEnable(GL_FRAMEBUFFER_SRGB)
        while True:
            eFPS = clock.get_fps()
            aFPS += eFPS
            iteration += 1
            firstRUN += 1
            mX, mY = pygame.mouse.get_pos()
            x = glGetDoublev(GL_MODELVIEW_MATRIX)
            camera_x = x[3][0]
            camera_y = (x[3][1]-71407.406)
            camera_z = (x[3][2]+2)
            run += 1
            counter += 1
            # pygame events
            if camera_y <= 0 and camera_y <= 300 and pygame.mixer.music.get_busy() == False:
                PlayAmbientSound(musicVOL)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    StartMenu = pygame.display.set_mode((width, height))
                    LoadingScreen = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg")))
                    StartMenu.blit(LoadingScreen, (0,0))
                    pygame.display.flip()
                    if sound == True:
                        PlayClickSound(soundVOL)
                    Home_Screen(themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, musicVOL, camera_x, camera_y, camera_z, size, theme, lastRun)
                # get keypresses
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        AKeyPressed = True
                    if event.key == pygame.K_d:
                        DKeyPressed = True
                    if event.key == pygame.K_e:
                        myScreenshot = pyautogui.screenshot(region=(((size.width/2)-640),((size.height/2)-360), 1280, 720))
                        myScreenshot.save(os.path.join(base_folder,("Resources\\General_Resources\\PauseIMG.jpg")))
                        Inventory(FontCol, BackgroundCol, ShapeCol, width, height, aa, version, FPS, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D)
                    if event.key == pygame.K_r:
                        MapLoader(FontCol, BackgroundCol, ShapeCol, width, height, aa, version, FPS, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D)
                    if event.key == pygame.K_w:
                        WKeyPressed = True
                    if event.key == pygame.K_s:
                        SKeyPressed = True
                    if event.key == pygame.K_SPACE and Jump == False: 
                        Jump = True
                    if event.key == pygame.K_ESCAPE:
                        # locks and unlocks the mouse to the canvas
                        if MouseUnlock == True:
                            MouseUnlock = False
                        elif MouseUnlock == False:
                            MouseUnlock = True
                    if event.key == pygame.K_q:
                        # setup extra window, root, title, size, background colour
                        DataWindow = tk.Tk()
                        DataWindow.title("Player Information")
                        DataWindow.configure(width = 500, height = 300)
                        DataWindow.configure(bg="lightblue")
                        # data is defined so it can be written to the display
                        versionData = "Pycraft: 27p085-20a: Playing"
                        versionData, CoordinatesData, FPSData, RendisData, FOVData = f"Pycraft: v{version}", f"Coordinates: x: {round(camera_x,3)} y: {round(camera_y,3)} z: {round(camera_z, 3)}", f"FPS: {eFPS}", f"Render distance: {rendis}", f"FOV: {FOV}"
                        # this data is then stored as a tkinter label
                        versionData, CoordinatesData, FPSData, RendisData, FOVData = tk.Label(DataWindow, text = versionData), tk.Label(DataWindow, text = CoordinatesData), tk.Label(DataWindow, text = FPSData), tk.Label(DataWindow, text = RendisData), tk.Label(DataWindow, text = FOVData)
                        # which is then rendered on the display at the required locations
                        versionData.grid(row = 0, column = 0, columnspan = 2)
                        CoordinatesData.grid(row = 1, column = 0, columnspan = 2)
                        FPSData.grid(row = 2, column = 0, columnspan = 2)
                        RendisData.grid(row = 3, column = 0, columnspan = 2)
                        FOVData.grid(row = 4, column = 0, columnspan = 2)
                        DataWindow.mainloop()
                        DataWindow.quit()
                        pygame.mouse.set_pos(600,360)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        WKeyPressed = False
                    if event.key == pygame.K_a:
                        AKeyPressed = False
                    if event.key == pygame.K_s:
                        SKeyPressed = False
                    if event.key == pygame.K_d:
                        DKeyPressed = False
                # zoom / change FOV
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glTranslatef(0,0,1)
                    if event.button == 5:
                        glTranslatef(0,0,-1)

            if WKeyPressed == True:
                if stop == False:
                    time = eFPS*3
                    stop = True
                if time >= 0:
                    Total_move_z += 35
                elif time <= 0:
                    Total_move_z += 100
                time -= 1
            else:
                stop = False 
            if AKeyPressed == True:
                Total_move_x += -35 # 3.5
            if SKeyPressed == True:
                Total_move_z += -35 # 3.5
            if DKeyPressed == True:
                Total_move_x += 35 # 3.5

            # jump animation
            if Jump == True:
                JumpID += 1
                if JumpID <= 20:
                    JumpID += 1
                    Total_move_y -= 10
                if JumpID >= 21:
                    JumpID += 1
                    Total_move_y += 10
                if JumpID >= 40:
                    Jump = False
                    JumpID = 0

            if MouseUnlock == True: # change x pos due to +80 window expansion
                if mX >= 680:
                    glRotatef(cameraANGspeed,0,1,0) # 0.5,0,1,0
                    rotationvectX += 0.5
                    # auto-loop
                if mX <= 600:
                    glRotatef(-cameraANGspeed,0,1,0) # -0.5,0,1,0
                    rotationvectX += -0.5
                    # auto-loop

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            x = glGetDoublev(GL_MODELVIEW_MATRIX)
            glDisable(GL_DEPTH_TEST)
            glPushMatrix()
            glDepthMask(GL_FALSE)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            glDepthMask(GL_TRUE)
            glPopMatrix()
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
            if devmode == 10:
                pygame.display.set_caption(f"Pycraft: v{version}: Playing | Developer mode | V: {Total_move_x, Total_move_y, Total_move_z} C: {round(camera_x,3)}, {round(camera_y,3)}, {round(camera_z,3)} (c: {collisions[0]} t: {collisions[1]}) | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | weather: {weather} changeIN: {round(counterForWeather/FPS)}/300 | Theme: {theme}")
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Playing")

            if camera_x == prev_camera_x and camera_y == prev_camera_y and camera_z == prev_camera_z and not firstRUN == 1:
                collisions = prev_collisions
            else:
                collisions = collisionTheory.GetCollisions(camera_x, camera_y-2, camera_z, G3Dscale)
                prev_camera_x = camera_x
                prev_camera_y = camera_y
                prev_camera_z = camera_z
                prev_collisions = collisions
            if collisions[0] == False:
                #donothing = 0
                Total_move_y -= 1
            elif not collisions[0] == True and repeater == True:
                repeater = False
                numOFerrors.write("Module.collisionTheory "+str(collisions)+"\n")
            elif collisions[0] == True:
                if collisions[1] < camera_y and collisions[1] < camera_y-1:
                    Total_move_y -= 1
                elif collisions[1] > camera_y and collisions[1] > camera_y+1:
                    Total_move_y += 1
            if firstRUN == 1:
                glTranslatef(0,50000,0)
                prev_camera_x = camera_x
                prev_camera_y = camera_y
                prev_camera_z = camera_z
            else:
                firstRUN = 2
            if camera_x >= (1150*G3Dscale) or camera_x <= (-1150*G3Dscale) or camera_z >= (700*G3Dscale) or camera_z <= (-1150*G3Dscale):
                print("World Boarder Reached")
                
            glDisable(GL_DEPTH_TEST)
            DrawSkyBox()
            DrawMapTexture(camera_x, camera_y, camera_z)
            glEnable(GL_DEPTH_TEST)
            MapModel(Map, Map_scale, Map_trans, map_vertices)
            if stop1 == False:
                counterForWeather = 1
                stop1 = True
            counterForWeather = counterForWeather + 1
            if counterForWeather/FPS >= 300:
                weather = random.randint(0,2)
                stop1 = False
            if RenderFOG == True and weather == 2: # snowing
                glEnable(GL_FOG)
                glFogfv(GL_FOG_COLOR,(239,243,245,1)) # 0.5, 0.5, 0.7, 1
                glFogi(GL_FOG_MODE, GL_LINEAR)
                glFogf(GL_FOG_START, 16000) # 160
                glFogf(GL_FOG_END, 3000000) # 2000
                glFogf(GL_FOG_DENSITY, 0.5) # 0.35
            elif RenderFOG == True and weather == 1: # rain
                glEnable(GL_FOG)
                glFogfv(GL_FOG_COLOR,(115,145,165,1)) # 0.5, 0.5, 0.7, 1
                glFogi(GL_FOG_MODE, GL_LINEAR)
                glFogf(GL_FOG_START, 16000) # 160
                glFogf(GL_FOG_END, 9000000) # 2000
                glFogf(GL_FOG_DENSITY, 0.5) # 0.35
            elif RenderFOG == True and weather == 0: # clear
                glEnable(GL_FOG)
                glFogfv(GL_FOG_COLOR,(177,194,205,1)) # 0.5, 0.5, 0.7, 1
                glFogi(GL_FOG_MODE, GL_LINEAR)
                glFogf(GL_FOG_START, 16000) # 160
                glFogf(GL_FOG_END, 30000000) # 2000
                glFogf(GL_FOG_DENSITY, 0.5) # 0.35
            elif RenderFOG == False:
                glDisable(GL_FOG)
            glEnable(GL_LIGHTING)
            glEnable(GL_LIGHT0)
            glLightfv(GL_LIGHT0,GL_POSITION,(Sun_pos_x, Sun_pos_y, Sun_pos_z))
            glLightfv(GL_LIGHT0,GL_AMBIENT,(1,0,1,1))
            glLightfv(GL_LIGHT0,GL_DIFFUSE,(1,0,1,1))
            glLightfv(GL_LIGHT0,GL_SPECULAR,(1,0,1,1))
            glEnable(GL_COLOR_MATERIAL)
            glColorMaterial(GL_FRONT_AND_BACK,GL_AMBIENT_AND_DIFFUSE)
            glMaterial(GL_FRONT_AND_BACK,GL_SPECULAR,(0,1,0,1))
            glMaterial(GL_FRONT_AND_BACK,GL_EMISSION,(0,1,0,1))

            glTranslatef(Total_move_x, Total_move_y, Total_move_z)
            PlayerModel_pos_x, PlayerModel_pos_y, PlayerModel_pos_z = -Total_move_x, -Total_move_y, -Total_move_z
            Total_move_x, Total_move_y, Total_move_z = 0,0,0

            pygame.display.flip()
            clock.tick(FPS)


    Home_Screen(themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, musicVOL, camera_x, camera_y, camera_z, size, theme, lastRun)
except Exception as error:
    import os, traceback
    base_folder = os.path.dirname(__file__)
    error = ''.join(traceback.format_exception(None, error, error.__traceback__))
    with open(os.path.join(base_folder,("Data_Files\\errorREPORT.txt")), "w") as errorFILE:
        errorFILE.write(str(error)+"\n")