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
    import csv
    base_folder = os.path.dirname(__file__)
    numOFerrors = open(os.path.join(base_folder,("Data_Files\\errorREPORT.txt")), "w")
except Exception as error:
    numOFerrors.write(str(f"base_folder lines 3&4 and opening error log failed fataly: {error}")+"\n")
    numOFerrors.close()
try:
    base_folder = os.path.dirname(__file__)
    SaveConfigFile = open(os.path.join(base_folder,("Data_Files\\SaveGameConfig.txt")), "r")
    exec(SaveConfigFile.read())
    SaveConfigFile.close()
    Display = pygame.display.set_mode((1280, 720)) # sets the GUI size
    pygame.display.set_caption(f"Pycraft | Pick your theme")
    theme = save["theme"]
    clock = pygame.time.Clock() # starts running pygame"s clock function
    TitleFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 60) # loads the font used for the graph
    Title = TitleFont.render("Pycraft", True, (255,255,255))
    MiddleFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # loads the font used for the graph
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
                pygame.quit()#
            if event.type == pygame.MOUSEBUTTONDOWN: # if the mouse button down
                mousebuttondown = True # mouse button down is set to True (yes)
            if event.type == pygame.MOUSEBUTTONUP: # if the mouse button is up
                mousebuttondown = False # this variable is set to no (False)    
            
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
                # Loading the song
                base_folder = os.path.dirname(__file__)
                pygame.mixer.music.load(os.path.join(base_folder,("Resources\\General_Resources\\Click.mp3")))
                
                # Setting the volume
                pygame.mixer.music.set_volume(50)
                
                # Start playing the song
                pygame.mixer.music.play()
                mousebuttondown = False
        elif mX >= 820 and mX <= 980 and mY >= 300 and mY <= 460:
            if mousebuttondown == True:
                theme = "light"
                # Loading the song
                base_folder = os.path.dirname(__file__)
                pygame.mixer.music.load(os.path.join(base_folder,("Resources\\General_Resources\\Click.mp3")))
                
                # Setting the volume
                pygame.mixer.music.set_volume(50)
                
                # Start playing the song
                pygame.mixer.music.play()
                mousebuttondown = False
        pygame.display.update()
        clock.tick(60)
    themeArray = save["themeArray"] # font, background, shapes (dark then light)
    if theme == "dark":
        FontCol = themeArray[0][0]
        BackgroundCol = themeArray[0][1]
        ShapeCol = themeArray[0][2]
    elif theme == "light":
        FontCol = themeArray[1][0]
        BackgroundCol = themeArray[1][1]
        ShapeCol = themeArray[1][2]
    pygame.display.set_caption(f"Pycraft | Loading") # sets caption to this
    LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Medium_Loading.jpg"))) # load the loading screen (ironic?)
    Display.blit(LoadingImage, (0,0)) # displays the image to the GUI
    pygame.display.flip() # updates the display
    def LoadingCaption(num, version):
        if num == 0:
            pygame.display.set_caption(f"Pycraft {version} | Loading (-)") # sets caption to this
        elif num == 1:
            pygame.display.set_caption(f"Pycraft {version} | Loading (\)") # sets caption to this
        elif num == 2:
            pygame.display.set_caption(f"Pycraft {version} | Loading (|)") # sets caption to this
        elif num == 3:
            pygame.display.set_caption(f"Pycraft {version} | Loading (\)") # sets caption to this
        else:
            pygame.display.set_caption(f"Pycraft {version} | Loading") # sets caption to this
    pygame.display.set_caption(f"Pycraft | Loading (-)") # sets caption to this
    version = save["version"] # what version of pycraft are we up to:
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
    rendis = save["rendis"] # render distance is set to 60 by default
    LoadingCaption(0, version)
    pygame.display.update()
    FPS = save["FPS"] # the Frames Per Seccond is set to 60
    LoadingCaption(1, version)
    pygame.draw.line(Display, ShapeCol, (205,142), (205,666), width=2)
    pygame.display.update()
    FOV = save["FOV"] # the Field of View is set to 70
    LoadingCaption(2, version)
    pygame.display.update()
    cameraANGspeed = save["cameraANGspeed"] # CameraANGspeed (speed of camera panning) is set to 0.5
    LoadingCaption(3, version)
    pygame.draw.line(Display, ShapeCol, (205,142), (422,666), width=2)
    pygame.display.update()
    aa = save["aa"] # anti aliasing
    LoadingCaption(0, version)
    pygame.display.update()
    RenderFOG = save["RenderFOG"] # render fog
    LoadingCaption(1, version)
    pygame.draw.line(Display, ShapeCol, (205,142), (422,666), width=2)
    pygame.display.update()
    FanSky = save["FanSky"] # fancy skybox, moons, sun, stars, celestial events
    LoadingCaption(2, version)
    pygame.display.update()
    FanPart = save["FanPart"] # fancy particles, leaves, rain, walking, dust, HDR (?)
    LoadingCaption(3, version)
    pygame.draw.line(Display, ShapeCol, (205,142), (575,512), width=2)
    pygame.display.update()
    sound = save["sound"] # sound on/off
    LoadingCaption(0, version)
    pygame.display.update()
    soundVOL = save["soundVOL"] # sets the sound volume (%)
    LoadingCaption(1, version)
    pygame.draw.line(Display, ShapeCol, (205,142), (575,295), width=2)
    pygame.display.update()
    music = save["music"] # sets the music on/off
    LoadingCaption(2, version)
    pygame.display.update()
    musicVOL = save["musicVOL"] # sets the music volume (%)
    LoadingCaption(3, version)
    pygame.draw.line(Display, ShapeCol, (51,295), (51,512), width=2)
    pygame.display.update()
    devmode = 1 # turns off optional features by default
    LoadingCaption(0, version)
    pygame.display.update()
    width, height = 1280, 720 # defines the size of the display (res~720)
    LoadingCaption(1, version)
    pygame.draw.line(Display, ShapeCol, (51,295), (205,666), width=2)
    pygame.display.update()
    camera_x, camera_y, camera_z = 0,0,0
    LoadingCaption(2, version)
    pygame.display.update()
    G3Dscale = 1000000 #10000
    LoadingCaption(3, version)
    pygame.draw.line(Display, ShapeCol, (51,295), (422,666), width=2)
    pygame.display.update()
    size = pyautogui.size()
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
        data = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), i) # loads the font used for the graph
    LoadingCaption(0, version)
    pygame.display.update()
    data = pygame.image.load(os.path.join(base_folder, "Resources\\Error_Resources\\Error_Message.jpg"))
    LoadingCaption(1, version)
    pygame.draw.line(Display, ShapeCol, (51,295), (422,142), width=2)
    pygame.display.update()
    data = pygame.image.load(os.path.join(base_folder, "Resources\\Error_Resources\\Icon.jpg"))
    LoadingCaption(2, version)
    pygame.display.update()
    data = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\skybox\\front.jpg")))
    LoadingCaption(3, version)
    pygame.draw.line(Display, ShapeCol, (51,512), (51,295), width=2)
    pygame.display.update()
    data = Image.open(os.path.join(base_folder,("Resources\\Folder_Resources\\FolderIcon.ico")))
    LoadingCaption(0, version)
    pygame.draw.line(Display, ShapeCol, (575,512), (422,142), width=2)
    pygame.display.update()
    global Map
    Map = pywavefront.Wavefront(os.path.join(base_folder,("Resources\\G3_Resources\\Map\\map.obj")), create_materials=True, collect_faces=True) # Map v2.obj
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
    data = pygame.image.load(os.path.join(base_folder, "Resources\\General_Resources\\selectorICON.jpg"))
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


    def Start(FontCol, BackgroundCol, ShapeCol): # this procedure creates an intro, and checks all modules are installed.
        base_folder = os.path.dirname(__file__)
        data = open(os.path.join(base_folder,("Data_Files\\data.txt")),"r+") # opens a file that is used to test weather the program"s on its first run
        if sys.platform == "win32" or sys.platform == "win64":
            os.environ["SDL_VIDEO_CENTERED"] = "1"
        if data.read() == "False": # is the program is on its first run...
            data.seek(0) # navigates to the first character in the file (index = 0)
            data.truncate() # this secects all the data in the file...and clears it.
            data.close() # saves the file
            data = open(os.path.join(base_folder,("Data_Files\\data.txt")),"r+") # re opens it 
            data.write("True") # this tells the program when its next run that this is not the first run
            data.close() # this clears the file from the program as it is no longer needed, freeing up 4 bytes of RAM
            Display = pygame.display.set_mode((width, height)) # creates a GUI with the size of width and height
            fade = pygame.Surface((width, height)) # creates a temporary GUI with the size; width, height
            LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg"))) # loads a image (Loading v2.jpg) to RAM.
            Display.blit(LoadingImage, (0,0)) # renders the image (see prv line) to the GUI, Display at the position (0,0), top left
            Display.fill(BackgroundCol) # sets the display to black
            pygame.display.set_caption(f"Pycraft: {version} | Welcome") # sets the Display caption to Pycraft: {version} | Welcome
            PresentsFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 20) # loads the font; Book Antiqua and stores it in the variable PresentsFont
            PycraftFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 60)
            NameFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 45) # END OF FONT LOADING
            Display.fill(BackgroundCol) # sets the display colour to black
            pygame.time.wait(2000) # waits the program for 2000 milliseconds (2 seconds)
            name = NameFont.render("Thomas Jebson",True,(255,255,255)) # loads Thomas Jebson into the RAM with the font NameFont
            Display.blit(name,(520,360)) # renders the name variable to the screen at the position, (480,360)
            pygame.display.flip() # updates the GUI to add the current items
            pygame.time.wait(2000)
            pygame.event.get() # makes the program not crash
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
            pygame.event.get() # END OF FONT RENDERING ANIMATION
            for a in range(360): # run this 360 times:
                Display.fill(BackgroundCol) # sets the display to black
                Display.blit(name,(540,(360-a))) # re-renders the font to the GUI Display, changing the y axis each time
                pygame.display.flip() # refreshes the GUI to show the changes
                pygame.time.wait(5) # pauses for 5 milliseconds
                pygame.event.get() # makes the game not crash
            return True
        elif data.read() == "True": # if the file reads True
            data.close() # closes the file to clear up a bit of RAM
            Display = pygame.display.set_mode((width, height)) # creates a display GUI that displays the loading screen until HS is loaded
            pygame.display.set_caption(f"Pycraft: {version} | Loading") # sets caption to this
            LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg"))) # loads the image to RAM
            Display.blit(LoadingImage, (0,0)) # loads the image to the display
            pygame.display.flip() # updates the display
            return True
        else: # if the file reads something else then it will run the startup again
            data.seek(0) # goes to the position to character 0
            data.truncate() # clears the data file
            data.close() # saves the file
            data = open(os.path.join(base_folder,("Data_Files\\data.txt")),"r+")
            data.write("False") # and sets it to false so the program re-runs
            data.close() # cleans up the RAM
            Display = pygame.display.set_mode((width, height)) # does the same thing now as the previus section, loading the loading screen
            pygame.display.set_caption(f"Pycraft: {version} | Loading")
            LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg")))
            Display.blit(LoadingImage, (0,0))
            pygame.display.flip()
            return False # returns false so the program knows to re-run this


    def PlayClickSound(soundVOL):
        # Loading the song
        base_folder = os.path.dirname(__file__)
        pygame.mixer.music.load(os.path.join(base_folder,("Resources\\General_Resources\\Click.mp3")))
        
        # Setting the volume
        pygame.mixer.music.set_volume(soundVOL/100)
        
        # Start playing the song
        pygame.mixer.music.play()


    def PlayInvSound(musicVOL):
        base_folder = os.path.dirname(__file__)
        pygame.mixer.music.load(os.path.join(base_folder,("Resources\\General_Resources\\InventoryGeneral.mp3")))
        
        # Setting the volume
        pygame.mixer.music.set_volume(musicVOL/100)
        
        # Start playing the song
        pygame.mixer.music.play()


    def settings(themeArray, FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, FanSky, FanPart, sound, soundVOL, music, musicVOL, theme): # defines the setting procedure
        base_folder = os.path.dirname(__file__)
        Display = pygame.display.set_mode((width, height)) # sets the GUI size
        LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg"))) # load the loading screen (ironic?)
        Display.blit(LoadingImage, (0,0)) # displays the image to the GUI
        pygame.display.flip() # updates the display
        if devmode == 10 or devmode-10 == 0: # if developer mode is enabled
            pygame.display.set_caption(f"Pycraft: {version}: Settings | Developer Mode") # sets the caption to developer mode for the user
        else:# if the developer mode is not enabled then it is set to default
            pygame.display.set_caption(f"Pycraft: {version}: Settings") # sets the display caption
        VersionFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15) # loads the version font for the pre-sets
        MainTitleFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 60) # loads the main title font
        LOWFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")),15) # loads the fonts for the pre-sets
        MEDIUMFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        HIGHFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        ADAPTIVEFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15) # END OF PRE-SET FONT LOADING
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
        TempMx = 0 # used to get the previous mouse coordinates
        Mx, My = 0,0 # sets the current mouse pos to zero, zero
        mousebuttondown = False # the mouse button (left) is not down
        aFPS = 0
        iteration = 1
        while True: # main settings loop
            if theme == "dark":
                FontCol = themeArray[0][0]
                BackgroundCol = themeArray[0][1]
                ShapeCol = themeArray[0][2]
            elif theme == "light":
                FontCol = themeArray[1][0]
                BackgroundCol = themeArray[1][1]
                ShapeCol = themeArray[1][2]
            TempMx = Mx
            iteration += 1
            Mx, My = pygame.mouse.get_pos() # gets the current mouse position
            eFPS = clock.get_fps() # gets the current fps
            aFPS += eFPS
            run += 1
            iteration += 1
            if iteration >= 2000:
                iteration = 1
                aFPS = eFPS
            for event in pygame.event.get(): # detects events, (keypresses, display interactions, mousebutton presses, ect.)
                if event.type == pygame.QUIT: # if the "x" in the corner is pressed then;
                    PlayClickSound(soundVOL)
                    return themeArray, FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, FanSky, FanPart, sound, soundVOL, music, musicVOL, theme
                elif event.type == pygame.KEYDOWN: # detects keypresses
                    if event.key == pygame.K_SPACE and devmode < 10: # if developer mode is getting enabled...
                        devmode += 1 # increases the devmode value
                        if devmode >= 5 and devmode <= 9: # if devmode is getting enabled then 
                            pygame.display.set_caption(f"Pycraft: {version}: Settings | you are: {10-devmode} steps away from being a developer") # tells the user that they are enabling devmode
                        elif devmode == 10: # if devmode is enabled then 
                            pygame.display.set_caption(f"Pycraft {version}: Settings | Developer mode | V: 0,00 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}") # tells the user
                        else:# if the developer mode is not enabled then it is set to default
                            pygame.display.set_caption(f"Pycraft: {version}: Settings") # sets the display caption
                    if event.key == pygame.K_x: # detects if "x" key is pressed
                        devmode = 1 # restes the devmode value
                        pygame.display.set_caption(f"Pycraft: {version}: Settings") # sets the caption to default
                    if event.key == pygame.K_q: # detects if "q" key pressed
                        DataWindow = tk.Tk() # sets the tkinter root
                        DataWindow.title("Player Information") # sets the display (window) caption
                        DataWindow.configure(width = 500, height = 300) # sets the window size (not needed (?))
                        DataWindow.configure(bg="lightblue") # sets the background colour
                        VersionData = f"Pycraft: {version}" # adds the curent version if caption fails
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
                        pygame.display.set_caption(f"Pycraft: {version}: Settings") # and the caption
                elif event.type == pygame.MOUSEBUTTONDOWN: # if the mouse button is down (left)
                    mousebuttondown = True # this variable is set to True
                elif event.type == pygame.MOUSEBUTTONUP: # if the mouse button is up (left)
                    mousebuttondown = False # this variable is set to False
            titletFont = MainTitleFont.render("Pycraft", aa, FontCol) # main title with colour defined with developer mode
            RendertFont = VersionFont.render(f"Render Distance: {rendis}",aa, FontCol) # setting title plus data
            FPStFont = VersionFont.render(f"FPS: Actual: {int(eFPS)} Max: {int(FPS)} Adverage: {int((aFPS/iteration))}",aa, FontCol)
            FOVtFont = VersionFont.render(f"FOV: {FOV}",aa, FontCol)
            CamRottFont = VersionFont.render(f"Camera Rotation Speed: {round(cameraANGspeed,1)}",aa, FontCol) # END OF SETTING TITLE + DATA
            ModetFont = VersionFont.render("Mode;          ,                  ,           ,          .",aa, FontCol) # gives the pre defined settings a location
            LOWtFont = LOWFont.render("LOW",aa, FontCol) # low preset font
            MEDIUMtFont = MEDIUMFont.render("MEDIUM",aa, FontCol) # medium preset font
            HIGHtFont = HIGHFont.render("HIGH",aa, FontCol) # high preset font
            ADAPTIVEtFont = ADAPTIVEFont.render("ADAPTIVE",aa, FontCol) # adaptive preset font
            AAtFont = VersionFont.render(f"Anti-Aliasing: {aa}",aa, FontCol) # setting title plus data part 2
            RenderFogtFont = VersionFont.render(f"Render Fog: {RenderFOG}",aa, FontCol)
            FancySkytFont = VersionFont.render(f"Fancy Skies: {FanSky}",aa, FontCol)
            FancyParticletFont = VersionFont.render(f"Fancy Partices: {FanPart}",aa, FontCol)
            SoundtFont = VersionFont.render(f"Sound: {sound}",aa, FontCol)
            SoundVoltFont = VersionFont.render(f"Sound Volume: {soundVOL}%",aa, FontCol)
            MusictFont = VersionFont.render(f"Music: {music}",aa, FontCol)
            MusicVoltFont = VersionFont.render(f"Music Volume: {musicVOL}%",aa, FontCol) # END OF SETTING TITLE + DATA 2
            ThemeFont = VersionFont.render(f"Theme:          ,          | Current Theme: {theme}", aa, FontCol)
            LightTheme = LightThemeFont.render("Light", aa, FontCol)
            DarkTheme = DarkThemeFont.render("Dark", aa, FontCol)
            Display.fill(BackgroundCol)
            Display.blit(titletFont, (580,0)) # then the title font
            Display.blit(RendertFont, (0,100)) # then the setting data part 1
            Display.blit(FPStFont, (0,150))
            Display.blit(FOVtFont, (0,200))
            Display.blit(CamRottFont, (0,250))
            Display.blit(ModetFont, (0,85)) # then the pre set modes
            Display.blit(LOWtFont, (48,85))
            Display.blit(MEDIUMtFont, (90,85))
            Display.blit(HIGHtFont, (165,85))
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
            render_rect = pygame.Rect(50, 130, 450, 10) # x,y, width, height.
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
            pygame.draw.rect(Display, ShapeCol, render_rect, 0) # draws the rectangle to the display with a dark grey, filled
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
            if mousebuttondown == True:
                if My > 130 and My < 140: # if the mouse is in these positions and mousebuttondown is True
                    if Mx > TempMx and rendis < 490: # if player tries to slide the slider (ironic?)
                        rendis += 1 # rendis is raised
                    elif Mx < TempMx and rendis > 60: # if the player tries to lower the rendis
                        rendis -= 1 # rendis is lowered
                    elif Mx == TempMx: # if player hovers over the circle
                        rendis = rendis # nothing happens
                    if rendis < 60: # however if rendis is less than 60
                        rendis = 60 # this is the minimum so stops it from going lower
                    elif rendis > 490: # the opposite is also true
                        rendis = 490
                if My > 180 and My < 190: # same as before but for the FPS slider
                    if Mx > TempMx and FPS < 445: # with a maximum refresh rate of 240 as tech limited
                        FPS += 1
                    elif Mx < TempMx and FPS > 15: # below this number things begin to break...
                        FPS -= 1
                    if FPS < 15:
                        FPS = 16
                    elif FPS > 445:
                        FPS = 444
                if My > 230 and My < 240:
                    if Mx > TempMx and FOV < 98:
                        FOV += 1
                    elif Mx < TempMx and FOV > 12:
                        FOV -= 1
                    if FOV < 12:
                        FOV = 13
                    elif FOV > 98:
                        FOV = 97
                if My > 280 and My < 290:
                    if Mx > TempMx and cameraANGspeed < 5.0:
                        cameraANGspeed += 0.1
                    elif Mx < TempMx and cameraANGspeed > 0.0:
                        cameraANGspeed -= 0.1
                    if cameraANGspeed > 5.0:
                        cameraANGspeed = 4.9
                    elif cameraANGspeed < 0:
                        cameraANGspeed = 0.1
                if My > 580 and My < 590 and sound == True:
                    if Mx > TempMx and soundVOL < 100:
                        soundVOL += 1
                    elif Mx < TempMx and soundVOL > 0:
                        soundVOL -= 1
                    if soundVOL > 100:
                        soundVOL = 100
                    elif soundVOL < 0:
                        soundVOL = 0
                if My > 680 and My < 690 and music == True: # there is no point adjusting the music vol when there is none!
                    if Mx > TempMx and musicVOL < 100:
                        musicVOL += 1
                    elif Mx < TempMx and musicVOL > 0:
                        musicVOL -= 1
                    if musicVOL > 100:
                        musicVOL = 100
                    elif musicVOL < 0:
                        musicVOL = 0
                if My > 330 and My < 340: # END OF SLIDER, start of on/off switches, anti-aliasing
                    if aa == True: # if on switch off
                        aa = False # switches off
                        PlayClickSound(soundVOL)
                        mousebuttondown = False
                    elif aa == False: # if off switch on
                        aa = True # switches on 
                        PlayClickSound(soundVOL)
                        mousebuttondown = False
                if My > 380 and My < 390:
                    if RenderFOG == True:
                        RenderFOG = False
                        PlayClickSound(soundVOL)
                        mousebuttondown = False
                    elif RenderFOG == False:
                        RenderFOG = True
                        PlayClickSound(soundVOL)
                        mousebuttondown = False
                if My > 430 and My < 440:
                    if FanSky == True:
                        FanSky = False
                        PlayClickSound(soundVOL)
                        mousebuttondown = False
                    elif FanSky == False:
                        FanSky = True
                        PlayClickSound(soundVOL)
                        mousebuttondown = False
                if My > 480 and My < 490:
                    if FanPart == True:
                        FanPart = False
                        PlayClickSound(soundVOL)
                        mousebuttondown = False
                    elif FanPart == False:
                        FanPart = True
                        PlayClickSound(soundVOL)
                        mousebuttondown = False
                if My > 530 and My < 540:
                    if sound == True:
                        sound = False
                        PlayClickSound(soundVOL)
                        mousebuttondown = False
                    elif sound == False:
                        sound = True
                        PlayClickSound(soundVOL)
                        mousebuttondown = False
                if My > 630 and My < 640:
                    if music == True:
                        music = False
                        PlayClickSound(soundVOL)
                        mousebuttondown = False
                    elif music == False:
                        music = True
                        PlayClickSound(soundVOL)
                        mousebuttondown = False
            if My >= 65 and My <= 75 and Mx >= 55 and Mx <= 95:
                LightThemeFont.set_underline(True)
                if mousebuttondown == True:
                    theme = "light"
                    PlayClickSound(soundVOL)
                    mousebuttondown = False
            else:
                LightThemeFont.set_underline(False)
            if My >= 65 and My <= 75 and Mx >= 95 and Mx <= 135:
                DarkThemeFont.set_underline(True)
                if mousebuttondown == True:
                    theme = "dark"
                    PlayClickSound(soundVOL)
                    mousebuttondown = False
            else:
                DarkThemeFont.set_underline(False)
            if My >= 85 and My <= 95 and Mx >= 40 and Mx <= 80:
                LOWFont.set_underline(True)
                if mousebuttondown == True:
                    rendis = 60
                    FPS = random.randint(15,30)
                    aa = False
                    RenderFOG = False
                    FanSky = False
                    FanPart = False
                    mousebuttondown = False
                    PlayClickSound(soundVOL)
            else:
                LOWFont.set_underline(False)
            if My >= 85 and My <= 95 and Mx >= 90 and Mx <= 155:
                MEDIUMFont.set_underline(True)
                if mousebuttondown == True:
                    rendis = 80
                    FPS = random.randint(30,60)
                    aa = True
                    RenderFOG = False
                    FanSky = True
                    FanPart = False
                    PlayClickSound(soundVOL)
                    mousebuttondown = False
            else:
                MEDIUMFont.set_underline(False)
            if My >= 85 and My <= 95 and Mx >= 165 and Mx <= 205:
                HIGHFont.set_underline(True)
                if mousebuttondown == True:
                    rendis = 100
                    FPS = random.randint(60, 120)
                    aa = True
                    RenderFOG = True
                    FanSky = True
                    FanPart = True
                    PlayClickSound(soundVOL)
                    mousebuttondown = False
            else:
                HIGHFont.set_underline(False)
            if My >= 85 and My <= 95 and Mx >= 215 and Mx <= 300: 
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
                    PlayClickSound(soundVOL)
                    mousebuttondown = False
            else:
                ADAPTIVEFont.set_underline(False)
            if sound == False:
                soundVOL = 0
            if music == False:
                musicVOL = 0
            pygame.draw.circle(Display, (255,255,255), (int(rendis), 135), 9) # draws the slider outside (plan)
            pygame.draw.circle(Display, ShapeCol, (int(rendis), 135), 6) # draws the slider inside
            pygame.draw.circle(Display, (255,255,255), (int(FPS+45), 185), 9)
            pygame.draw.circle(Display, ShapeCol, (int(FPS+45), 185), 6)
            pygame.draw.circle(Display, (255,255,255), (int(FOV*5), 235), 9)
            pygame.draw.circle(Display, ShapeCol, (int(FOV*5), 235), 6)
            pygame.draw.circle(Display, (255,255,255), (int(cameraANGspeed*89)+45, 285),9)
            pygame.draw.circle(Display, ShapeCol, (int(cameraANGspeed*89)+45, 285), 6)
            pygame.draw.circle(Display, (255,255,255), (int(soundVOL*4.4)+50, 585), 9)
            pygame.draw.circle(Display, ShapeCol, (int(soundVOL*4.4)+50, 585), 6)
            pygame.draw.circle(Display, (255,255,255), (int(musicVOL*4.4)+50, 685), 9)
            pygame.draw.circle(Display, ShapeCol, (int(musicVOL*4.4)+50, 685), 6)
            if devmode == 10 or devmode-10 == 0:
                pygame.display.set_caption(f"Pycraft: {version}: Settings | Developer mode | V: 0,0,0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
            else:
                pygame.display.set_caption(f"Pycraft: {version}: Settings")
            # ani aliasing selection
            if aa == True: # sets the dial/indicator position to 90,335 (x,y) when on
                pygame.draw.circle(Display, (255,255,255), (90, 335), 9)
                pygame.draw.circle(Display, ShapeCol, (90, 335), 6)
            elif aa == False: # sets the dial/indicator position to 60,335 (x,y) when off
                pygame.draw.circle(Display, (255,255,255), (60, 335), 9)
                pygame.draw.circle(Display, ShapeCol, (60, 335), 6)
            # render fog selection
            if RenderFOG == True:
                pygame.draw.circle(Display, (255,255,255), (90, 385), 9)
                pygame.draw.circle(Display, ShapeCol, (90, 385), 6)
            elif RenderFOG == False:
                pygame.draw.circle(Display, (255,255,255), (60, 385), 9)
                pygame.draw.circle(Display, ShapeCol, (60, 385), 6)
            # fancy skies selection
            if FanSky == True:
                pygame.draw.circle(Display, (255,255,255), (90, 435), 9)
                pygame.draw.circle(Display, ShapeCol, (90, 435), 6)
            elif FanSky == False:
                pygame.draw.circle(Display, (255,255,255), (60, 435), 9)
                pygame.draw.circle(Display, ShapeCol, (60, 435), 6)
            # fancy particles selection
            if FanPart == True:
                pygame.draw.circle(Display, (255,255,255), (90, 485), 9)
                pygame.draw.circle(Display, ShapeCol, (90, 485), 6)
            elif FanPart == False:
                pygame.draw.circle(Display, (255,255,255), (60, 485), 9)
                pygame.draw.circle(Display, ShapeCol, (60, 485), 6)
            # sound selection
            if sound == True:
                pygame.draw.circle(Display, (255,255,255), (90, 535), 9)
                pygame.draw.circle(Display, ShapeCol, (90, 535), 6)
            elif sound == False:
                pygame.draw.circle(Display, (255,255,255), (60, 535), 9)
                pygame.draw.circle(Display, ShapeCol, (60, 535), 6)
            # music selection
            if music == True:
                pygame.draw.circle(Display, (255,255,255), (90, 635), 9)
                pygame.draw.circle(Display, ShapeCol, (90, 635), 6)
            elif music == False:
                pygame.draw.circle(Display, (255,255,255), (60, 635), 9)
                pygame.draw.circle(Display, ShapeCol, (60, 635), 6)
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


    def Character_Customiser(FontCol, BackgroundCol, ShapeCol, devmode): # sets up the character customiser, (not finished), (girl, women, skin colour?)
        base_folder = os.path.dirname(__file__)
        Home_Screen(devmode) # as nothing is happening here it takes you back to the home screen
        clock.tick(30) # continues the 30 fps rule


    def Achievements(FontCol, BackgroundCol, ShapeCol, devmode): # sets up the acievements (targets, score?)#
        base_folder = os.path.dirname(__file__)
        Home_Screen(devmode) # goes back to the home screen
        clock.tick(30) # just continues


    def Credits(FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, aa): # loads the credits menu
        base_folder = os.path.dirname(__file__)
        Display = pygame.display.set_mode((width, height))# sets the GUI size
        LoadingImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg"))) # load the loading screen (ironic?)
        Display.blit(LoadingImage, (0,0)) # displays the image to the GUI
        pygame.display.flip() # updates the display
        if devmode == 10 or devmode-10 == 0: # if developer mode is enabled
            pygame.display.set_caption(f"Pycraft: {version}: Credits and Change-Log | Developer Mode | V: 0,00 | FPS: {clock.get_fps()} aFPS: {clock.get_fps()} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())}") # sets the caption to developer mode for the user
        else:# if the developer mode is not enabled then it is set to default
            pygame.display.set_caption(f"Pycraft: {version}: Credits and Change-Log") # sets the display caption
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
        PlayInvSound(musicVOL)
        while True: # main game loop
            eFPS = clock.get_fps()
            aFPS += eFPS # gets the current FPS limmited to 30
            Mx, My = pygame.mouse.get_pos() # gets the mouse position
            run += 1
            iteration += 1
            for event in pygame.event.get(): # detects events, (keypresses, display interactions, mousebutton presses, ect.)
                if event.type == pygame.QUIT: # if the "x" in the corner is pressed then;
                    PlayClickSound(soundVOL)
                    Home_Screen(themeArray, FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, musicVOL, camera_x, camera_y, camera_z, size, theme) # goes back to the home screen
                elif event.type == pygame.KEYDOWN: # detects keypresses
                    if event.key == pygame.K_SPACE and devmode < 10: # if developer mode is getting enabled...
                        devmode += 1 # increases the devmode value
                        if devmode >= 5 and devmode <= 9: # if devmode is getting enabled then 
                            pygame.display.set_caption(f"Pycraft: {version}: Credits and Change-Log | you are: {10-devmode} steps away from being a developer") # tells the user that they are enabling devmode
                        elif devmode == 10: # if devmode is enabled then 
                            pygame.display.set_caption(f"Pycraft: {version}: Credits and Change-Log | Developer mode | V: 0,00 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())}") # tells the user
                        else:# if the developer mode is not enabled then it is set to default
                            pygame.display.set_caption(f"Pycraft: {version}: Credits and Change-Log") # sets the display caption
                    if event.key == pygame.K_q: # detects if "q" key pressed
                        DataWindow = tk.Tk() # sets the tkinter root
                        DataWindow.title("Player Information") # sets the display (window) caption
                        DataWindow.configure(width = 500, height = 300) # sets the window size (not needed (?))
                        DataWindow.configure(bg="lightblue") # sets the background colour
                        VersionData = f"Pycraft: {version}" # adds the curent version if caption fails
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
                        pygame.display.set_caption(f"Pycraft: {version}: Credits and Change-Log") # and the caption
            Display.fill(BackgroundCol)
            Display.blit(TitleFont, (540,0))
            Display.blit(Credits1, (0,100))
            Display.blit(Credits2, (0,115))
            Display.blit(Credits3, (0,130))
            Display.blit(Credits4, (0,145))
            Display.blit(Credits5, (0,160))
            Display.blit(Credits6, (0,175))
            Display.blit(Credits7, (0,190))
            Display.blit(Credits8, (0,205))
            Display.blit(Credits9, (0,220))
            Display.blit(Credits10, (0,235))
            Display.blit(Credits11, (0,250))
            Display.blit(Credits12, (0,265))
            Display.blit(Credits13, (0,280))
            Display.blit(Credits14, (0,295))
            Display.blit(Credits15, (0,310))
            Display.blit(Credits16, (0,325))
            Display.blit(Credits17, (0,340))
            Display.blit(Credits18, (0,355))
            Display.blit(Credits19, (0,370))
            Display.blit(Credits20, (0,385))
            Display.blit(Credits21, (0,400))
            Display.blit(Credits22, (0,415))
            Display.blit(Credits23, (0,430))
            Display.blit(Credits24, (0,445))
            Display.blit(ChangeLog1, (0,470))
            Display.blit(ChangeLog2, (0,485))
            Display.blit(ChangeLog3, (0,500))
            Display.blit(ChangeLog4, (0,515))
            Display.blit(ChangeLog5, (0,530))
            Display.blit(ChangeLog6, (0,545))
            Display.blit(ChangeLog7, (0,560))
            Display.blit(ChangeLog8, (0,575))
            Display.blit(ChangeLog9, (0,590))
            Display.blit(ChangeLog10, (0,605)) # END OF ADDING DATA TO THE DISPLAY  
            Display.blit(ChangeLog11, (0,620))
            if devmode == 10 or devmode-10 == 0:
                pygame.display.set_caption(f"Pycraft: {version}: Credits and Change-Log | Developer mode | V: 0,0,0 | FPS: {int(eFPS)} aFPS {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())}")
            else:
                pygame.display.set_caption(f"Pycraft: {version}: Credits and Change-Log")
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


    def Home_Screen(themeArray, FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, MusicVOL, camera_x, camera_y, camera_z, size, theme): # creates the home screen module used after the startup
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
            pygame.display.set_caption(f"Pycraft: {version}: Home Screen | Developer Mode | V: 0,0,0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}") # sets the caption to developer mode for the user
        else:# if the developer mode is not enabled then it is set to default
            pygame.display.set_caption(f"Pycraft: {version}: Home Screen") # sets the display caption
        icon = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Icon.jpg")))
        pygame.display.set_icon(icon)
        Selector = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\selectorICON.jpg")))
        hover1 = False # sets the underline value of the first button font to false
        hover2 = False # sets the underline value of the seccond button font to false
        hover3 = False # sets the underline value of the third button font to false
        hover4 = False # sets the underline value of the fourth button font to false
        hover5 = False # sets the underline value of the fith button font to false
        mousebuttondown = False # used to tell the if statements later on weather the mouse button is down or not
        MainTitleFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 60) # loads the title / heading font
        SideFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 24) # loads the "By Thomas Jebson" font
        VersionFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15) # loads the font that displays the version
        ButtonFont1 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # play
        ButtonFont2 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # settings
        ButtonFont3 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # character custom
        ButtonFont4 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # achievements
        ButtonFont5 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # credits and change-log
        DataFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15) # loads the font used for the graph
        data1 = [] # stores the FPS
        data2 = [] # CPU Usage
        data3 = [] # RAM usage
        data4 = [] # stores the adverage fps
        run = 0 # defines how many times the program has run
        rerun = 0 # defines how many times the run has been greater than 2000
        LoadingGameImage = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Long_Loading.jpg")))
        if devmode == 10 or devmode-10 == 0: # if developer mode is enabled
            pygame.display.set_caption(f"Pycraft: {version}: Home | Developer Mode | V: 0,0,0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}") # sets the caption to developer mode for the user
        iteration = 1
        aFPS = 0
        PlayInvSound(musicVOL)
        counter = 0
        while True: # main game loop
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
                            SaveGameConfigDict = {"themeArray":themeArray, "theme":theme, "version":version, "rendis":rendis, "FPS":FPS, "eFPS":eFPS, "aFPS":(aFPS/counter), "FOV":FOV, "cameraANGspeed":cameraANGspeed, "aa":aa, "RenderFOG":RenderFOG, "FanSky":FanSky, "FanPart":FanPart, "sound":sound, "soundVOL":soundVOL, "music":music, "musicVOL":musicVOL, "X":camera_x, "Y":camera_y, "Z":camera_z}
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
                            pygame.display.set_caption(f"Pycraft: {version}: Home | you are: {10-devmode} steps away from being a developer") # tells the user that they are enabling devmode
                        elif devmode == 10: # if devmode is enabled then 
                            pygame.display.set_caption(f"Pycraft: {version}: Home | Developer mode | V: 0,0,0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}") # tells the user
                        else:# if the developer mode is not enabled then it is set to default
                            pygame.display.set_caption(f"Pycraft: {version}: Home") # sets the display caption
                    if event.key == pygame.K_q: # detects if "q" key pressed
                        DataWindow = tk.Tk() # sets the tkinter root
                        DataWindow.title("Player Information") # sets the display (window) caption
                        DataWindow.configure(width = 500, height = 300) # sets the window size (not needed (?))
                        DataWindow.configure(bg="lightblue") # sets the background colour
                        VersionData = f"Pycraft: {version}" # adds the curent version if caption fails
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
                        pygame.display.set_caption(f"Pycraft: {version}: Home") # and the caption
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
                pygame.display.set_caption(f"Pycraft: {version}: Home | Developer mode | V: 0,0,0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
            else:
                pygame.display.set_caption(f"Pycraft: {version}: Home")
            # sets the hover value to True (underlined) when, (eh), hovering over the font
            if My >= 202 and My <= 247 and Mx >= 1155:
                hover1 = True
                if mousebuttondown == True: # if the button is clicked
                    PlayClickSound(soundVOL)
                    mousebuttondown = False
                    pygame.mixer.music.fadeout(2000)
                    Display.blit(LoadingGameImage, (0,0)) # renders the loading screen
                    pygame.display.flip() # updates the display
                    if devmode == 10 or devmode-10 == 0:
                        pygame.display.set_caption(f"Pycraft: {version}: Playing | Developer mode | V: 0,0,0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
                    else:
                        pygame.display.set_caption(f"Pycraft: {version}: Playing")
                    Load3D = True
                    Map = 0
                    Map_box = 0
                    min_v = 0
                    max_v = 0
                    Map_scale = 0
                    Map_trans = 0
                    Map_size = 0
                    max_Map_size = 0
                    main(FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, Display, LoadingGameImage, G3Dscale, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D) # loads the command that happens when clicked
            else: # if you are not hovering over the font
                hover1 = False # hover os set to false
            if My >= 252 and My <= 297 and Mx >= 1105: # this repeats for each button
                hover2 = True
                if mousebuttondown == True:
                    Display.blit(LoadingImage, (0,0))
                    pygame.display.flip()
                    PlayClickSound(soundVOL)
                    mousebuttondown = False
                    themeArray, FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, FanSky, FanPart, sound, soundVOL, music, MusicVOL, theme = settings(themeArray, FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, FanSky, FanPart, sound, soundVOL, music, musicVOL, theme)
            else:
                hover2 = False
            if My >= 302 and My <= 347 and Mx >= 865:
                hover3 = True
                if mousebuttondown == True:
                    print("Character Custom")
                    Display.blit(LoadingImage, (0,0))
                    pygame.display.flip()
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
                    PlayClickSound(soundVOL)
                    mousebuttondown = False
                    Credits(FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, aa)
            else:
                hover5 = False
            Display.fill(BackgroundCol)
            Display.blit(PycraftTitle, (540,0))
            Display.blit(Name, (0,690))
            Display.blit(Version, (1130, 700))
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
            CreateRose(FontCol, BackgroundCol, ShapeCol, Display)
            pygame.display.flip()
            clock.tick(FPS)


    def MapModel(Map, Map_scale, Map_trans): # used to create the model
        glPushMatrix() # creates a new matrix
        glScalef(*Map_scale) # and creates a scale vector (*Map_scale)
        glTranslatef(*Map_trans) # and translates the mesh into view
        for mesh in Map.mesh_list: # then creates the mesh 3D locations
            glBegin(GL_TRIANGLES) # loads a oGL file for triangle handling
            for face in mesh.faces: # then creates a face location in 3D locations in oGL "world"
                for vertex_i in face: # defines the vertex of each face
                    glVertex3f(*Map.vertices[vertex_i]) # tells OGL everything
            glEnd() # closes the oGL file GL_TRIANGLES
        glPopMatrix() # adds the entire thing to the 3D "world"


    def LoadMapTexture(aa):
        base_folder = os.path.dirname(__file__)
        if aa == True:
            file = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\Map\\GrassTexture.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512,512), Image.ANTIALIAS)
            texture = file.tobytes() # converts the loaded and edited image to binary
        if aa == False:
            file = Image.open(os.path.join(base_folder,("Resources\\G3_Resources\\Map\\GrassTexture.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512,512))
            texture = file.tobytes() # converts the loaded and edited image to binary
        glGenTextures(7) # loads the texture
        glBindTexture(GL_TEXTURE_2D, 7) # binds the texture to the cube
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1) # alligns the texture to the cube
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP) # glues the corners to the face vertices top left.
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP) # glues the other side to the face bottom right.
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) # makes sure the texture moves and rotates correctly
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture) # blits the texture to the cube (renders)
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
        glBindTexture(GL_TEXTURE_2D, 7)


    def DrawSkyBox(camera_x, camera_y, camera_z,Total_move_x, Total_move_y, Total_move_z):
        glEnable(GL_TEXTURE_2D) # allows 2D images 
        glColor3f(1,1,1) # sets the colour of all the surface to white (clears the cube of all texture)
        # c1 Front
        glBindTexture(GL_TEXTURE_2D, 1) # binds the texture to the cube
        glBegin(GL_QUADS) # opens the oGL file
        glTexCoord2f(0, 0) # sets the image coords to 0,0
        glVertex3f(camera_x-10.0, camera_y-10.0, camera_z-10.0) # loads the image at the points 
        glTexCoord2f(1, 0) # takes a 3D location and converts the coords into a 2D location
        glVertex3f(camera_x+10.0, camera_y-10.0, camera_z-10.0)
        glTexCoord2f(1, 1)
        glVertex3f(camera_x+10.0, camera_y+10.0, camera_z-10.0)
        glTexCoord2f(0, 1)
        glVertex3f(camera_x-10.0, camera_y+10.0, camera_z-10.0)
        glEnd() # closes the file

        glBindTexture(GL_TEXTURE_2D, 0) # empties the RAM of the image as it is now stored in an oGL file
        # c2 Left Side
        glBindTexture(GL_TEXTURE_2D, 2)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(camera_x-10.0, camera_y-10.0, camera_z-10.0)
        glTexCoord2f(1, 0)
        glVertex3f(camera_x-10.0, camera_y-10.0, camera_z+10.0)
        glTexCoord2f(1, 1)
        glVertex3f(camera_x-10.0, camera_y+10.0, camera_z+10.0)
        glTexCoord2f(0, 1)
        glVertex3f(camera_x-10.0, camera_y+10.0, camera_z-10.0)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        # c3 Top
        glBindTexture(GL_TEXTURE_2D, 3)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(camera_x-10.0, camera_y+10.0, camera_z-10.0)
        glTexCoord2f(1, 0)
        glVertex3f(camera_x+10.0, camera_y+10.0, camera_z-10.0)
        glTexCoord2f(1, 1)
        glVertex3f(camera_x+10.0, camera_y+10.0, camera_z+10.0)
        glTexCoord2f(0, 1)
        glVertex3f(camera_x-10.0, camera_y+10.0, camera_z+10.0)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        # c4 Right Side
        glBindTexture(GL_TEXTURE_2D, 4)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(camera_x+10.0, camera_y-10.0, camera_z+10.0)
        glTexCoord2f(1, 0)
        glVertex3f(camera_x+10.0, camera_y-10.0, camera_z-10.0)
        glTexCoord2f(1, 1)
        glVertex3f(camera_x+10.0, camera_y+10.0, camera_z-10.0)
        glTexCoord2f(0, 1)
        glVertex3f(camera_x+10.0, camera_y+10.0, camera_z+10.0)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        # c5 Back
        glBindTexture(GL_TEXTURE_2D, 5)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(camera_x+10.0, camera_y-10.0, camera_z+10.0)
        glTexCoord2f(1, 0)
        glVertex3f(camera_x-10.0, camera_y-10.0, camera_z+10.0)
        glTexCoord2f(1, 1)
        glVertex3f(camera_x-10.0, camera_y+10.0, camera_z+10.0)
        glTexCoord2f(0, 1)
        glVertex3f(camera_x+10.0, camera_y+10.0, camera_z+10.0)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        # c6 Bottom
        glBindTexture(GL_TEXTURE_2D, 6)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(camera_x-10.0, camera_y-10.0, camera_z-10.0)
        glTexCoord2f(1, 0)
        glVertex3f(camera_x+10.0, camera_y-10.0, camera_z-10.0)
        glTexCoord2f(1, 1)
        glVertex3f(camera_x+10.0, camera_y-10.0, camera_z+10.0)
        glTexCoord2f(0, 1)
        glVertex3f(camera_x-10.0, camera_y-10.0, camera_z+10.0)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, 0)
        glTranslatef(-Total_move_x, -Total_move_y, -Total_move_z)


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
        Selector = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\selectorICON.jpg")))
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
        pygame.display.set_caption(f"Pycraft: {version}: Playing | Inventory")
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
        MapIcon = pygame.image.load(os.path.join(base_folder,("Resources\\Map_Resources\\Marker.png")))
        zoom = 0
        pygame.display.set_caption(f"Pycraft: {version}: Playing | Map")
        MouseUnlock = True
        X,Y = 0,0
        key = ""
        while True:
            Display.fill([0,0,0])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Load3D = False
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


    def main(FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, Display, LoadingGameImage, G3Dscale, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D): # what requirements are needed to run this function, (are specified here)
        base_folder = os.path.dirname(__file__)
        LoadingPercent = 0
        line = []
        LoadingPercent += 100
        line.append((LoadingPercent, 620))
        LoadingPercent += 1
        aFPS = 0
        iteration = 1
        line.append((LoadingPercent, 620))
        Display.blit(LoadingGameImage, (-1,-1))
        pygame.draw.lines(Display, (30, 30, 30), aa, [(95, 620), (1200, 620)], 3)
        pygame.draw.lines(Display, (153, 153, 153), aa, line)
        LoadingFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)
        Init = LoadingFont.render("Initiating", aa, (153, 153, 153))
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
        pygame.draw.lines(Display, (153, 153, 153), aa, line)
        Init = LoadingFont.render("Loaded Variables", aa, (153, 153, 153))
        Display.blit(Init, (100,640))
        pygame.display.flip()
        if devmode == 10 or devmode-10 == 0:
            pygame.display.set_caption(f"Pycraft: {version}: Playing | Developer mode | V: 0,0,0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
        else:
            pygame.display.set_caption(f"Pycraft: {version}: Playing")
        MouseUnlock = True
        Sun_pos_x, Sun_pos_y, Sun_pos_z = 0,10,-20
        LoadingPercent += 115
        line.append((LoadingPercent, 620))
        Display.blit(LoadingGameImage, (-1,-1))
        pygame.draw.lines(Display, (60,60,60), aa, [(95, 620), (1175, 620)], 3)
        pygame.draw.lines(Display, (153, 153, 153), aa, line)
        Init = LoadingFont.render("Loaded Image Resources and Initiated next step", aa, (153, 153, 153))
        Display.blit(Init, (100,640))
        pygame.display.flip()
        if devmode == 10 or devmode-10 == 0:
            pygame.display.set_caption(f"Pycraft: {version}: Playing | Developer mode | V: 0,0,0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
        else:
            pygame.display.set_caption(f"Pycraft: {version}: Playing")
        #LoadMapTexture()
        counter = 0
        rotationvectX, rotationvectY = 0,0
        # loads the Map
        pygame.event.get()
        LoadingPercent += 115
        line.append((LoadingPercent, 620))
        Display.blit(LoadingGameImage, (-1,-1))
        pygame.draw.lines(Display, (60,60,60), aa, [(95, 620), (1175, 620)], 3)
        pygame.draw.lines(Display, (153, 153, 153), aa, line)
        Init = LoadingFont.render("Set Captions; Beginning Resource Loading (Loading world)", aa, (153, 153, 153))
        Display.blit(Init, (100, 600))
        pygame.display.flip()
        # Map
        if Load3D == True:
            Map = pywavefront.Wavefront(os.path.join(base_folder,("Resources\\G3_Resources\\Map\\map.obj")), create_materials=True, collect_faces=True) # Map v2.obj
            Map_box = (Map.vertices[0], Map.vertices[0])
            for vertex in Map.vertices:
                min_v = [min(Map_box[0][i], vertex[i]) for i in range(3)]
                max_v = [max(Map_box[1][i], vertex[i]) for i in range(3)]
                Map_box = (min_v, max_v)

                LoadingPercent += 0.06+(165/6616)
                line.append((LoadingPercent, 620))
                pygame.draw.lines(Display, (60,60,60), aa, [(95, 620), (1175, 620)], 3)
                pygame.draw.lines(Display, (153, 153, 153), aa, line)
                pygame.display.flip()
                pygame.event.get()
            Map_size = [Map_box[1][i]-Map_box[0][i] for i in range(3)]
            max_Map_size = max(Map_size)
            Map_size = G3Dscale # 10000
            Map_scale = [Map_size/max_Map_size for i in range(3)]
            Map_trans = [-(Map_box[1][i]+Map_box[0][i])/2 for i in range(3)]
        # end
        Display.blit(LoadingGameImage, (-1,-1))
        line.append((LoadingPercent, 620))
        pygame.draw.lines(Display, (60,60,60), aa, [(95, 620), (1175, 620)], 3)
        pygame.draw.lines(Display, (153, 153, 153), aa, line)
        Init = LoadingFont.render("Loaded Map", aa, (153, 153, 153))
        Display.blit(Init, (100, 600))
        pygame.display.flip()
        if devmode == 10 or devmode-10 == 0:
            pygame.display.set_caption(f"Pycraft: {version}: Playing | Developer mode | V: 0,0,0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
        else:
            pygame.display.set_caption(f"Pycraft: {version}: Playing")
        LoadingPercent += 115
        Display.blit(LoadingGameImage, (-1,-1))
        line.append((LoadingPercent, 620))
        pygame.draw.lines(Display, (60,60,60), aa, [(95, 620), (1175, 620)], 3)
        pygame.draw.lines(Display, (153, 153, 153), aa, line)
        pygame.display.flip()
        run = 0
        pygame.event.get()
        pygame.mouse.set_pos(640,360)
        Total_move_x, Total_move_y, Total_move_z = 0,0,0
        if devmode == 10 or devmode-10 == 0:
            pygame.display.set_caption(f"Pycraft: {version}: Playing | Developer mode | V: 0,0,0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
        else:
            pygame.display.set_caption(f"Pycraft: {version}: Playing")
        WKeyPressed, AKeyPressed, SKeyPressed, DKeyPressed = False, False, False, False
        stop = False
        stop1 = False
        counterForWeather = 2
        weather = 0
        LoadingPercent = 1170
        Display.blit(LoadingGameImage, (-1,-1))
        line.append((LoadingPercent, 620))
        pygame.draw.lines(Display, (60,60,60), aa, [(95, 620), (1175, 620)], 3)
        pygame.draw.lines(Display, (153, 153, 153), aa, line)
        Init = LoadingFont.render("Finished Resource Loading; Rendering", aa, (153, 153, 153))
        Display.blit(Init, (100, 600))
        pygame.display.flip()
        pygame.display.set_mode((width, height), DOUBLEBUF|OPENGL)
        LoadSkyBox(aa)
        LoadMapTexture(aa)
        # creates the perspective of the player, incl FOV, render-distance
        gluPerspective(FOV, (display[0]/display[1]), 1, 1000000)
        firstRUN = 0
        pygame.mouse.set_pos(640,360)
        while True:
            eFPS = clock.get_fps()
            aFPS += eFPS
            iteration += 1
            firstRUN += 1
            if devmode == 10 or devmode-10 == 0:
                pygame.display.set_caption(f"Pycraft: {version}: Playing | Developer mode | V: {Total_move_x, Total_move_y, Total_move_z} | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
            else:
                pygame.display.set_caption(f"Pycraft: {version}: Playing")
            
            mX, mY = pygame.mouse.get_pos()
            x = glGetDoublev(GL_MODELVIEW_MATRIX)
            camera_x = x[3][0]
            camera_y = x[3][1]
            camera_z = x[3][2]
            run += 1
            counter += 1
            # pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    StartMenu = pygame.display.set_mode((width, height))
                    LoadingScreen = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg")))
                    StartMenu.blit(LoadingScreen, (0,0))
                    pygame.display.flip()
                    PlayClickSound(soundVOL)
                    Home_Screen(themeArray, FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, musicVOL, camera_x, camera_y, camera_z, size, theme)
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
                        versionData, CoordinatesData, FPSData, RendisData, FOVData = f"Pycraft: {version}", f"Coordinates: x: {round(camera_x,3)} y: {round(camera_y,3)} z: {round(camera_z, 3)}", f"FPS: {eFPS}", f"Render distance: {rendis}", f"FOV: {FOV}"
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
                    if event.key == pygame.K_c:
                        error41741 = AttributeError("This crash has been generated to showcase how this python module excepts  errors")
                        raise error41741
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
                    Total_move_z += 3.5
                elif time <= 0:
                    Total_move_z += 10
                time -= 1
            else:
                stop = False 
            if AKeyPressed == True:
                Total_move_x += -3.5 # 3.5
            if SKeyPressed == True:
                Total_move_z += -3.5 # 3.5
            if DKeyPressed == True:
                Total_move_x += 3.5 # 3.5

            # jump animation
            if Jump == True:
                JumpID += 1
                if JumpID <= 20:
                    JumpID += 1
                    Total_move_y -= 0.01
                if JumpID >= 21:
                    JumpID += 1
                    Total_move_y += 0.01
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
                if mY <= 380 and rotationvectY < 50:
                    glRotatef(-cameraANGspeed,1,0,0) # -0.5,1,0,0
                    rotationvectY += 0.5
                    #up
                if mY >= 340 and rotationvectY > -50:
                    glRotatef(cameraANGspeed,1,0,0) # 0.5,1,0,0
                    rotationvectY += -0.5

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            x = glGetDoublev(GL_MODELVIEW_MATRIX)
            glDisable(GL_DEPTH_TEST)
            glPushMatrix()
            glDepthMask(GL_FALSE)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            glDepthMask(GL_TRUE)
            glPopMatrix()
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
            collisions = collisionTheory.GetCollisions(camera_x, camera_y-2, camera_z, G3Dscale)
            if devmode == 10 or devmode-10 == 0:
                pygame.display.set_caption(f"Pycraft: {version}: Playing | Developer mode | V: {Total_move_x, Total_move_y, Total_move_z} C: {round(camera_x,5)}, {round((camera_y),5)}, {round(camera_z,5)} c: {collisions[0]} | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | weather: {weather} changeIN: {round(counterForWeather/FPS)}/300 | Theme: {theme}")
            else:
                pygame.display.set_caption(f"Pycraft: {version}: Playing")
            if collisions[0] == False:
                #Total_move_y = 1
                donothing = 0
            elif not collisions == True and repeater == True:
                repeater = False
                numOFerrors.write("Module.collisionTheory "+str(collisions)+"\n")
            elif collisions[0] == True:
                if collisions[1] < camera_y-1999.407:
                    Total_move_y -= 0.09
                elif collisions[1] > camera_y-1999.407:
                    Total_move_y += 0.09
            if firstRUN == 1:
                glTranslatef(0,0,0)
            else:
                firstRUN = 2
            '''if not camera_y < 0:
                Total_move_y -= 9.81'''
            if camera_x >= 1150 or camera_x <= -1150 or camera_z >= 700 or camera_z <= -1150:
                print("World Boarder Reached")
                
            glTranslatef(Total_move_x, Total_move_y, Total_move_z)
            PlayerModel_pos_x, PlayerModel_pos_y, PlayerModel_pos_z = -Total_move_x, -Total_move_y, -Total_move_z
            Total_move_x, Total_move_y, Total_move_z = 0,0,0
            glDisable(GL_DEPTH_TEST)
            DrawSkyBox(camera_x, camera_y, camera_z, Total_move_x, Total_move_y, Total_move_z)
            DrawMapTexture(camera_x, camera_y, camera_z)
            glEnable(GL_DEPTH_TEST)
            MapModel(Map, Map_scale, Map_trans)
            depthMapFBO = ""
            glGenFramebuffers(1, depthMapFBO)
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
            glEnable(GL_FRAMEBUFFER_SRGB)
            if aa == True:
                glEnable(GL_MULTISAMPLE)
            elif aa == False:
                glDisable(GL_MULTISAMPLE)
            glShadeModel(GL_SMOOTH)
            
            pygame.display.flip()
            clock.tick(FPS)


    Home_Screen(themeArray, FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, musicVOL, camera_x, camera_y, camera_z, size, theme)
except Exception as error:
    numOFerrors.write(str(error)+"\n")
    numOFerrors.close()
