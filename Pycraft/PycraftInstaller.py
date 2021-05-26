print("--Running PycraftInstaller")

import subprocess, pip, time, sys, os

try:
    import pygame
except Exception as error:
    try:
        subprocess.run(['pip', 'install', 'pygame'])
    except Exception as error:
        print(error)
    finally:
        os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
else:
    if sys.platform == "win32" or sys.platform == "win64":
        os.environ["SDL_VIDEO_CENTERED"] = "1"

    pygame.init()
    save = 0
    base_folder = os.path.dirname(__file__)

    SaveConfigFile = open(os.path.join(base_folder,("Data_Files\\SaveGameConfig.txt")), "r")
    exec(SaveConfigFile.read())
    SaveConfigFile.close()

    version = save["version"] # what version of pycraft are we up to:
    FPS = save["FPS"] # the Frames Per Seccond is set to 60

    Display = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock() # starts running pygame's clock function
    pygame.display.set_caption("Pycraft Instaler Utility | Getting Things Ready")
    icon = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Icon.jpg")))
    pygame.display.set_icon(icon)
    PycraftShortLoading = pygame.image.load(os.path.join(base_folder,("Resources\\General_Resources\\Pycraft_Short_Loading.jpg"))) # update
    Display.blit(PycraftShortLoading, (0,0))
    pygame.display.update()

    PycraftFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 60)
    titleFont = PycraftFont.render("Pycraft", True, (255,255,255)) # main title with colour defined with developer mode

    ButtonFont1 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Play
    Play = ButtonFont1.render("Play", True, (255,255,255)) # loads the Play text

    ButtonFont2 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Install
    Install = ButtonFont2.render("Install", True, (255,255,255)) # loads the Install text

    ButtonFont3 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Update
    Update = ButtonFont3.render("Update", True, (255,255,255)) # loads the settings text

    ButtonFont4 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Uninstall
    Uninstall = ButtonFont4.render("Uninstall", True, (255,255,255)) # loads the settings text

    SideFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 24) # loads the "By Thomas Jebson" font
    VersionFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15) # loads the font that displays the version

    Name = SideFont.render("By Thomas Jebson", True, (255,255,255)) # loads the creator name text
    Version = VersionFont.render(f"Version: {version}", True, (255,255,255)) # loads the version text

    Selector = pygame.image.load(os.path.join(base_folder,(f"Resources\\General_Resources\\selectorICONdark.jpg")))

    hover1 = False # sets the underline value of the first button font to false
    hover2 = False # sets the underline value of the seccond button font to false
    hover3 = False # sets the underline value of the third button font to false
    hover4 = False # sets the underline value of the fourth button font to false

    mousebuttondown = False # used to tell the if statements later on weather the mouse button is down or not

    def CreateRose(Display):
        defLargeOctagon = [(205,142),(51,295),(51,512),(205,666),(422,666),(575,512),(575,295),(422,142)] # 
        pygame.draw.polygon(Display, (80,80,80), defLargeOctagon, width=2) # 
        pygame.draw.line(Display, (80,80,80), (205,142), (51,512), width=2) # 
        pygame.draw.line(Display, (80,80,80), (205,142), (205,666), width=2) # 
        pygame.draw.line(Display, (80,80,80), (205,142), (422,666), width=2) #
        pygame.draw.line(Display, (80,80,80), (205,142), (575,512), width=2) #
        pygame.draw.line(Display, (80,80,80), (205,142), (575,295), width=2) #

        pygame.draw.line(Display, (80,80,80), (51,295), (51,512), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,295), (205,666), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,295), (422,666), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,295), (575,512), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,295), (575,295), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,295), (422,142), width=2) #

        pygame.draw.line(Display, (80,80,80), (51,512), (51,295), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,512), (205,666), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,512), (422,666), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,512), (575,512), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,512), (575,295), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,512), (422,142), width=2) #

        pygame.draw.line(Display, (80,80,80), (205,666), (51,512), width=2) #
        pygame.draw.line(Display, (80,80,80), (205,666), (51,295), width=2) # 
        pygame.draw.line(Display, (80,80,80), (205,666), (422,666), width=2) #
        pygame.draw.line(Display, (80,80,80), (205,666), (575,512), width=2) #
        pygame.draw.line(Display, (80,80,80), (205,666), (575,295), width=2) #
        pygame.draw.line(Display, (80,80,80), (205,666), (422,142), width=2) #

        pygame.draw.line(Display, (80,80,80), (51,295), (51,512), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,295), (205,666), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,295), (422,666), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,295), (575,512), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,295), (575,295), width=2) #
        pygame.draw.line(Display, (80,80,80), (51,295), (422,142), width=2) #

        pygame.draw.line(Display, (80,80,80), (422,666), (422,142), width=2)
        pygame.draw.line(Display, (80,80,80), (422,666), (575,295), width=2)

        pygame.draw.line(Display, (80,80,80), (575,512), (422,142), width=2)
    
    def Installer(Display, titleFont, Name, Version):
        pygame.display.set_caption("Pycraft Instaler Utility | installing")
        location = 0
        base_folder = os.path.dirname(__file__)

        ButtonFont1 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Play
        Cancel = ButtonFont1.render("Cancel", True, (255,255,255)) # loads the Play text

        ButtonFont2 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Install
        Install = ButtonFont2.render("Install", True, (255,255,255)) # loads the Install text

        hover1 = False # sets the underline value of the first button font to false
        hover2 = False # sets the underline value of the seccond button font to false

        mousebuttondown = False # used to tell the if statements later on weather the mouse button is down or not

        counter = -1

        InstallerFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15) # Install

        line = [(5,125), (5, 125), (5,125)]

        while True:
            Mx, My = pygame.mouse.get_pos() # gets the mouse position
            Display.fill([30,30,30])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.MOUSEBUTTONDOWN: # if the mouse button down
                    mousebuttondown = True # mouse button down is set to True (yes)
                if event.type == pygame.MOUSEBUTTONUP: # if the mouse button is up
                    mousebuttondown = False # this variable is set to no (False)
            if location == 0:
                CautionFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 17)
                WarningMessage = CautionFont.render("Do you wish to install Pycraft and all of the external modules it requires?", True, (255,255,255))
                Display.blit(WarningMessage, (5,100))
                CautionMessage = pygame.image.load(os.path.join(base_folder,("Resources\\Installer_Resources\\WarningMessage.png")))
                Display.blit(CautionMessage, (0,125))
                Cancel = ButtonFont1.render("Cancel", True, (255,255,255))
                Install = ButtonFont2.render("Install", True, (255,255,255))
                ButtonFont1.set_underline(hover1)
                ButtonFont2.set_underline(hover2)
                # Cancel
                if Mx >= 1182 and My >= 202 and My <= 247:
                    hover1 = True
                    if mousebuttondown == True:
                        Display.blit(PycraftShortLoading, (0,0)) # renders the loading screen
                        pygame.display.flip() # updates the display
                        return True
                else:
                    hover1 = False
                if hover1 == True:
                    Display.blit(Selector, (1135,200))

                # Install
                if Mx >= 1195 and My >= 252 and My <= 297:
                    hover2 = True
                    if mousebuttondown == True:
                        Display.blit(PycraftShortLoading, (0,0)) # renders the loading screen
                        pygame.display.flip() # updates the display
                        location = 2
                else:
                    hover2 = False
                if hover2 == True:
                    Display.blit(Selector, (1135,250))

                Display.blit(titleFont, (580,0)) # then the title font
                Display.blit(Name, (0,690))
                Display.blit(Version, (1130, 700))
                
                Display.blit(Cancel, (1182, 200))
                Display.blit(Install, (1185, 250))

                pygame.display.update()

            if location == 2:
                Display.fill([30,30,30])

                Display.blit(titleFont, (580,0)) # then the title font
                Display.blit(Name, (0,690))
                Display.blit(Version, (1130, 700))
                if counter >= 0:
                    ModulesArray = ["pygame", "pyopengl", "numpy", "pywavefront", "pyautogui", "matplotlib", "psutil"]
                    temp = (5+(1000/len(ModulesArray))*counter+10)
                    line.append((temp, 125))
                    if counter == len(ModulesArray):
                        os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
                    try:
                        subprocess.check_call([sys.executable, "-m","pip","install",ModulesArray[counter]], False)
                    except Exception as error:
                        donothing = 0
                    if not counter == (len(ModulesArray)-1):
                        Progress = InstallerFont.render(f"Installing: {ModulesArray[counter+1]}, Progress: {round(((100/len(ModulesArray))*counter),2)}%", True, (255,255,255))
                else:
                    Progress = InstallerFont.render(f"Installing: Pygame, Progress: 0.0%", True, (255,255,255))
    
                counter += 1

                Display.blit(Progress, (5,100))
                pygame.draw.lines(Display, (60,60,60), True, [(5,125), (960, 125)], 3)
                pygame.draw.lines(Display, (153, 153, 153), True, line)

                pygame.display.update()
    
    def Update():
        print("Run Updater")

    def Uninstaller():
        pygame.display.set_caption("Pycraft Instaler Utility | uninstalling")
        location = 0
        base_folder = os.path.dirname(__file__)

        ButtonFont1 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Play
        Cancel = ButtonFont1.render("Cancel", True, (255,255,255)) # loads the Play text

        ButtonFont2 = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 30) # Install
        Install = ButtonFont2.render("Uninstall", True, (255,255,255)) # loads the Install text

        hover1 = False # sets the underline value of the first button font to false
        hover2 = False # sets the underline value of the seccond button font to false

        mousebuttondown = False # used to tell the if statements later on weather the mouse button is down or not

        counter = 0

        InstallerFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15) # Install

        line = [(5,125), (5, 125), (5,125)]

        filePATH = str(pygame.__file__)

        filePATH = filePATH[:54]

        print(filePATH)

        while True:
            Mx, My = pygame.mouse.get_pos() # gets the mouse position
            Display.fill([30,30,30])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.MOUSEBUTTONDOWN: # if the mouse button down
                    mousebuttondown = True # mouse button down is set to True (yes)
                if event.type == pygame.MOUSEBUTTONUP: # if the mouse button is up
                    mousebuttondown = False # this variable is set to no (False)
            if location == 0:
                CautionFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 17)
                WarningMessage = CautionFont.render("Do you wish to install Pycraft and all of the external modules it requires?", True, (255,255,255))
                Display.blit(WarningMessage, (5,100))
                CautionMessage = pygame.image.load(os.path.join(base_folder,("Resources\\Installer_Resources\\WarningMessage.png")))
                Display.blit(CautionMessage, (0,125))
                Cancel = ButtonFont1.render("Cancel", True, (255,255,255))
                Install = ButtonFont2.render("Uninstall", True, (255,0,0))
                ButtonFont1.set_underline(hover1)
                ButtonFont2.set_underline(hover2)
                # Cancel
                if Mx >= 1182 and My >= 202 and My <= 247:
                    hover1 = True
                    if mousebuttondown == True:
                        Display.blit(PycraftShortLoading, (0,0)) # renders the loading screen
                        pygame.display.flip() # updates the display
                        return True
                else:
                    hover1 = False
                if hover1 == True:
                    Display.blit(Selector, (1135,200))

                # Install
                if Mx >= 1195 and My >= 252 and My <= 297:
                    hover2 = True
                    if mousebuttondown == True:
                        Display.blit(PycraftShortLoading, (0,0)) # renders the loading screen
                        pygame.display.flip() # updates the display
                        location = 2
                else:
                    hover2 = False
                if hover2 == True:
                    Display.blit(Selector, (1100,250))

                Display.blit(titleFont, (580,0)) # then the title font
                Display.blit(Name, (0,690))
                Display.blit(Version, (1130, 700))
                
                Display.blit(Cancel, (1182, 200))
                Display.blit(Install, (1148, 250))

                pygame.display.update()

            if location == 2:
                Display.fill([30,30,30])

                Display.blit(titleFont, (580,0)) # then the title font
                Display.blit(Name, (0,690))
                Display.blit(Version, (1130, 700))
                ModulesArray = ["pygame", "pyopengl", "numpy", "pywavefront", "pyautogui", "matplotlib", "psutil", "pillow"]
                if counter == 1:
                    try:
                        os.remove(os.path.join(filePATH, ("include\pygame")))
                        os.remove(os.path.join(filePATH, ("\lib\site-packages\pygame")))
                    except:
                        donothing = 0
                    if counter < 0:
                        Progress = InstallerFont.render(f"Uninstalling: {ModulesArray[counter+1]}, Progress: {round(((100/len(ModulesArray))*counter),2)}%", True, (255,255,255))
                else:
                    Progress = InstallerFont.render(f"Uninstalling: Pygame, Progress: 0.0%", True, (255,255,255))
                
                if counter <= len(ModulesArray):
                    counter += 1
                else:
                    os.execl(sys.executable, 'python', __file__, *sys.argv[1:])


                Display.blit(Progress, (5,100))
                pygame.draw.lines(Display, (60,60,60), True, [(5,125), (960, 125)], 3)
                pygame.draw.lines(Display, (153, 153, 153), True, line)

                pygame.display.update()

    while True:
        pygame.display.set_caption("Pycraft Instaler Utility")
        Mx, My = pygame.mouse.get_pos() # gets the mouse position

        pygame.display.set_icon(icon)

        Display.fill([30,30,30])
        CreateRose(Display)

        try:
            import pygame, numpy, pyautogui, OpenGL, psutil, pywavefront, matplotlib, pillow
        except:
            PlayFontCol = (80,80,80)
            InstallFontCol = (255,255,255)
            UpdateFontCol = (80,80,80)
            UninstallFontCol = (80,80,80)
            unlock = False
        else:
            PlayFontCol = (255,255,255)
            InstallFontCol = (80,80,80)
            UpdateFontCol = (255,255,255)
            UninstallFontCol = (255,0,0)
            unlock = True

        Play = ButtonFont1.render("Play", True, PlayFontCol) # loads the play text
        Install = ButtonFont2.render("Install", True, InstallFontCol) # loads the install text
        Update = ButtonFont3.render("Update", True, UpdateFontCol) # loads the install text
        Uninstall = ButtonFont4.render("Uninstall", True, UninstallFontCol) # loads the install text

        Display.blit(titleFont, (580,0)) # then the title font
        Display.blit(Name, (0,690))
        Display.blit(Version, (1130, 700))

        Display.blit(Play, (1207, 200))
        Display.blit(Install, (1185, 250))
        Display.blit(Update, (1170, 300))
        Display.blit(Uninstall, (1148, 350))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN: # if the mouse button down
                mousebuttondown = True # mouse button down is set to True (yes)
            if event.type == pygame.MOUSEBUTTONUP: # if the mouse button is up
                mousebuttondown = False # this variable is set to no (False)
        
        ButtonFont1.set_underline(hover1) # applies an underline value to each button 
        ButtonFont2.set_underline(hover2) # when hovering over it
        ButtonFont3.set_underline(hover3)
        ButtonFont4.set_underline(hover4)

        # Play
        if Mx >= 1207 and My >= 202 and My <= 247 and unlock == True:
            hover1 = True
            if mousebuttondown == True and unlock == True:
                Display.blit(PycraftShortLoading, (0,0)) # renders the loading screen
                pygame.display.flip() # updates the display
                import PycraftRunUtil
        else:
            hover1 = False
        if hover1 == True:
            Display.blit(Selector, (1155,200))

        # Install
        if Mx >= 1185 and My >= 252 and My <= 297 and unlock == False:
            hover2 = True
            if mousebuttondown == True and unlock == False:
                Display.blit(PycraftShortLoading, (0,0)) # renders the loading screen
                pygame.display.flip() # updates the display
                Installer(Display, titleFont, Name, Version)
                os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        else:
            hover2 = False
        if hover2 == True:
            Display.blit(Selector, (1125,250))

        # Update
        if Mx >= 1170 and My >= 302 and My <= 347 and unlock == True:
            hover3 = True
            if mousebuttondown == True and unlock == True:
                Display.blit(PycraftShortLoading, (0,0)) # renders the loading screen
                pygame.display.flip() # updates the display
                Update()
                os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        else:
            hover3 = False
        if hover3 == True:
            Display.blit(Selector, (1115,300))

        # Uninstall
        if Mx >= 1148 and My >= 352 and My <= 397 and unlock == True:
            hover4 = True
            if mousebuttondown == True and unlock == True:
                Display.blit(PycraftShortLoading, (0,0)) # renders the loading screen
                pygame.display.flip() # updates the display
                Uninstaller()
                os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        else:
            hover4 = False
        if hover4 == True:
            Display.blit(Selector, (1100,350))


        pygame.display.update()
        clock.tick(FPS)