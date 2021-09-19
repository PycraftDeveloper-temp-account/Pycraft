if not __name__ == "__main__":
    print("--Running Pycraft")
    try:
        import tkinter as tk
        import tkinter.ttk
        from PIL import Image, ImageTk, ImageGrab
        import pygame
        from pygame.locals import *
        import numpy
        import os
        import sys
        import random
        import time
        if sys.platform == "win32" or sys.platform == "win64":
            os.environ["SDL_VIDEO_CENTERED"] = "1" 
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
        import datetime
        import cpuinfo
        import ExBenchmark
        import CHandle
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            if str(proc.info["name"]) == "Pycraft.exe":
                quit()
    except Exception as error:
        import os, traceback
        base_folder = os.path.dirname(__file__)
        error = ''.join(traceback.format_exception(None, error, error.__traceback__))
        with open(os.path.join(base_folder, ("Data_Files\\errorREPORT.txt")), "w") as errorFILE:
            errorFILE.write(str(f"base_folder lines 3&4 and opening error log failed fataly: {error}")+"\n")
    try:
        save = 0
        base_folder = os.path.dirname(__file__)
        SaveConfigFile = open(os.path.join(base_folder, ("Data_Files\\SaveGameConfig.txt")), "r")
        test = SaveConfigFile.read()
        if len(test) <= 5:
            try:
                with open(os.path.join(base_folder, ("Data_Files\\SaveGameConfig.txt")), mode ="w") as SaveGameConfig:
                    save = {'theme': 'dark', 'FPS': 60, 'eFPS': 0, 'aFPS': 0, 'FOV': 70, 'cameraANGspeed': 4, 'aa': True, 'RenderFOG': True, 'FanSky': True, 'FanPart': True, 'sound': True, 'soundVOL': 75, 'music': True, 'musicVOL': 50, 'X': 0.0, 'Y': 0, 'Z': 0, 'lastRun': '15/7/2021', 'crash': True, 'startup': False, 'DisplayWidth':1280, 'DisplayHeight':720, 'WindowStatus':False}
                    SaveGameConfig.write("save = "+str(save))
            except Exception as FailedToRepairFile:
                import os, traceback
                base_folder = os.path.dirname(__file__)
                error = ''.join(traceback.format_exception(None, error, error.__traceback__))
                with open(os.path.join(base_folder, ("Data_Files\\errorREPORT.txt")), "w") as errorFILE:
                    errorFILE.write(str(f"An error occured whilst trying to build backup save: {FailedToRepairFile}")+"\n")
        SaveConfigFile.seek(0)
        exec(SaveConfigFile.read())
        SaveConfigFile.close()
        numOFerrors = open(os.path.join(base_folder, ("Data_Files\\errorREPORT.txt")), "w")
        Display = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption(f"Pycraft | Pick your theme")
        theme = save["theme"]
        clock = pygame.time.Clock()
        TitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 60)
        Title = TitleFont.render("Pycraft", True, (255, 255, 255))
        MiddleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30)
        DarkModeFont = MiddleFont.render("Dark", True, (255, 255, 255))
        LightModeFont = MiddleFont.render("Light", True, (255, 255, 255))
        icon = pygame.image.load(os.path.join(base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
        pygame.display.set_icon(icon)
        mousebuttondown = False
        while theme == "False":
            Display.fill([30, 30, 30])
            mX, mY = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit("Thanks for playing")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousebuttondown = True
                if event.type == pygame.MOUSEBUTTONUP:
                    mousebuttondown = False
                
            Display.blit(Title, (540, 0))
            Display.blit(DarkModeFont, (320, 360))
            Display.blit(LightModeFont, (890, 360))
            DarkRect = pygame.Rect(260, 300, 200, 160)
            pygame.draw.rect(Display, (80, 80, 80), DarkRect, 3)
            LightRect = pygame.Rect(820, 300, 200, 160)
            pygame.draw.rect(Display, (80, 80, 80), LightRect, 3)
            if mX >= 260 and mX <= 460 and mY >= 300 and mY <= 460:
                if mousebuttondown == True:
                    theme = "dark"
                    base_folder = os.path.dirname(__file__)
                    pygame.mixer.music.load(os.path.join(base_folder, ("Resources\\General_Resources\\Click.ogg")))
                    
                    pygame.mixer.music.set_volume(50)
                    
                    pygame.mixer.music.play()
                    mousebuttondown = False
            elif mX >= 820 and mX <= 980 and mY >= 300 and mY <= 460:
                if mousebuttondown == True:
                    theme = "light"
                    base_folder = os.path.dirname(__file__)
                    pygame.mixer.music.load(os.path.join(base_folder, ("Resources\\General_Resources\\Click.ogg")))
                    
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
        TitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 60)
        Title = TitleFont.render("Pycraft", True, FontCol)
        TitleLoadingFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
        TitleLoading = TitleLoadingFont.render("Loading", True, FontCol)
        Display.blit(Title, (540, 0))
        Display.blit(TitleLoading, (593, 45))
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


        def GetDisplaySetupForINIT(SavedWidth, SavedHeight):
            try:
                FullscreenX, FullscreenY = pyautogui.size()
                if Fullscreen == False:
                    pygame.display.quit()
                    pygame.init()
                    Display = pygame.display.set_mode((SavedWidth, SavedHeight))
                    keydown = False
                elif Fullscreen == True:
                    pygame.display.quit()
                    pygame.init()
                    Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF)
                    keydown = False
            except Exception as error:
                Fullscreen = True
                SavedWidth = 1280
                SavedHeight = 720
                pygame.display.quit()
                pygame.init()
                Display = pygame.display.set_mode((SavedWidth, SavedHeight))
                keydown = False

            return Display


        pygame.display.set_caption(f"Pycraft | Loading (-)")
        version = 0.9
        startUP = save["startup"]
        crash = save["crash"]
        Fullscreen = save["WindowStatus"]
        LoadingCaption(1, version)
        defLargeOctagon = [(205, 142), (51, 295), (51, 512), (205, 666), (422, 666), (575, 512), (575, 295), (422, 142)]
        pygame.draw.polygon(Display, ShapeCol, defLargeOctagon, width=2)
        pygame.display.update()
        base_folder = os.path.dirname(__file__)
        LoadingCaption(2, version)
        pygame.display.update()
        pygame.draw.line(Display, ShapeCol, (205, 142), (51, 512), width=2)
        pygame.display.update()
        LoadingCaption(3, version)
        pygame.display.update()
        rendis = 80
        LoadingCaption(0, version)
        pygame.display.update()
        FPS = save["FPS"]
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (205, 142), (205, 666), width=2)
        pygame.display.update()
        FOV = save["FOV"]
        LoadingCaption(2, version)
        pygame.display.update()
        cameraANGspeed = save["cameraANGspeed"]
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (205, 142), (422, 666), width=2)
        pygame.display.update()
        aa = save["aa"]
        LoadingCaption(0, version)
        pygame.display.update()
        RenderFOG = save["RenderFOG"]
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (205, 142), (422, 666), width=2)
        pygame.display.update()
        FanSky = save["FanSky"]
        LoadingCaption(2, version)
        pygame.display.update()
        FanPart = save["FanPart"]
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (205, 142), (575, 512), width=2)
        pygame.display.update()
        sound = save["sound"]
        LoadingCaption(0, version)
        pygame.display.update()
        soundVOL = save["soundVOL"]
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (205, 142), (575, 295), width=2)
        pygame.display.update()
        music = save["music"]
        LoadingCaption(2, version)
        pygame.display.update()
        musicVOL = save["musicVOL"]
        lastRun = save["lastRun"]
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (51, 295), (51, 512), width=2)
        pygame.display.update()
        devmode = 1
        LoadingCaption(0, version)
        pygame.display.update()
        SavedWidth, SavedHeight = save["DisplayWidth"], save["DisplayHeight"]
        yScaleFact = SavedHeight/720
        xScaleFact = SavedWidth/1280
        LoadingCaption(1, version)
        pygame.draw.line(Display, ShapeCol, (51, 295), (205, 666), width=2)
        pygame.display.update()
        camera_x, camera_y, camera_z = 0, 0, 0
        LoadingCaption(2, version)
        pygame.display.update()
        G3Dscale = 600000
        LoadingCaption(3, version)
        pygame.draw.line(Display, ShapeCol, (51, 295), (422, 666), width=2)
        pygame.display.update()
        size = pyautogui.size()
        current_time = datetime.datetime.now() 
        currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"
        if not currentDate == lastRun or crash == True:
            pygame.display.set_caption(f"Pycraft: v{version} | Loading (-) | Getting system requirements")
            import OpenGL.GL as gl
            pygame.display.set_mode((1280, 720), DOUBLEBUF|OPENGL)
            OpenGLversion = str(gl.glGetString(gl.GL_VERSION))[2:5]
            SDLversion = pygame.get_sdl_version()[0]
            RAM = (psutil.virtual_memory().total)/1000000000

            Display = GetDisplaySetupForINIT(SavedWidth, SavedHeight)

            Title = TitleFont.render("Pycraft", True, FontCol)
            TitleWidth = Title.get_width()
            Display.fill(BackgroundCol)
            Display.blit(Title, ((SavedWidth-TitleWidth)/2, 0))

            defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] 
            pygame.draw.polygon(Display, ShapeCol, defLargeOctagon, width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 

            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 

            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 

            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 

            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 

            pygame.draw.line(Display, ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)
            pygame.draw.line(Display, ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)

            pygame.draw.line(Display, ShapeCol, (575*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)

            pygame.display.update()

            if float(OpenGLversion) < 2.8:
                from tkinter import *
                from tkinter import messagebox
                try:
                    pygame.quit()
                except:
                    donothing = 0
                finally:
                    root = Tk()
                    root.withdraw()
                    messagebox.showerror("Invalid OpenGL version", f"OpenGL version: {OpenGLversion} is not supported; try a version greater than 2.7")
                    quit()
            elif SDLversion < 2:
                from tkinter import *
                from tkinter import messagebox
                try:
                    pygame.quit()
                except:
                    donothing = 0
                finally:
                    root = Tk()
                    root.withdraw()
                    messagebox.showerror("Invalid SDL version", f"SDL version: {SDLversion} is not supported; try a version greater than or equal to 2")
                    quit()
            elif RAM < 1:
                from tkinter import *
                from tkinter import messagebox
                try:
                    pygame.quit()
                except:
                    donothing = 0
                finally:
                    root = Tk()
                    root.withdraw()
                    messagebox.showerror("Minimum system requirements not met", f"Your system does not meet the minimum 500mb free memory specification needed to play this game")
                    quit()
            elif RAM < 4:
                from tkinter import *
                from tkinter import messagebox
                root = Tk()
                root.withdraw()
                messagebox.showwarning("Recommended system requirements not met", f"Your system's free memory does not meet the requirement recomended to play this game, you are still able to, however your experience may not be satisfactory")
                from PIL import Image, ImageTk, ImageGrab
            
            Display.fill(BackgroundCol)
            Display.blit(Title, ((SavedWidth-TitleWidth)/2, 0))
            LoadingCaption(1, version)
            defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] 
            pygame.draw.polygon(Display, ShapeCol, defLargeOctagon, width=2)
            pygame.display.update()
            LoadingCaption(2, version)
            pygame.display.update()
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.display.update()
            LoadingCaption(3, version)
            pygame.display.update()
            LoadingCaption(0, version)
            pygame.display.update()
            LoadingCaption(1, version)
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.display.update()
            LoadingCaption(2, version)
            pygame.display.update()
            LoadingCaption(3, version)
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.display.update()
            LoadingCaption(0, version)
            pygame.display.update()
            LoadingCaption(1, version)
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.display.update()
            LoadingCaption(2, version)
            pygame.display.update()
            LoadingCaption(3, version)
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.display.update()
            LoadingCaption(0, version)
            pygame.display.update()
            LoadingCaption(1, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.display.update()
            LoadingCaption(2, version)
            pygame.display.update()
            LoadingCaption(3, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.display.update()
            LoadingCaption(0, version)
            pygame.display.update()
            LoadingCaption(1, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.display.update()
            LoadingCaption(2, version)
            pygame.display.update()
            LoadingCaption(3, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.display.update()
            LoadingCaption(0, version)
            pygame.display.update()
            LoadingCaption(1, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.display.update()
            data = open(os.path.join(base_folder, ("Data_Files\\errorREPORT.txt")), "r+")
            data.close()
            LoadingCaption(2, version)
            try:
                data = open(os.path.join(base_folder, ("Data_Files\\SaveGameConfig.txt")), mode ="r+")
                data.close()
            except Exception as error:
                errorIMG = pygame.image.load(os.path.join(base_folder, ("Resources\\General_Resources\\Saving_ERROR.jpg"))).convert()
                Display.blit(errorIMG, (0, -5))
                pygame.display.update()
                pygame.time.wait(4000)
            LoadingCaption(3, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
            pygame.display.update()
            for i in range(60):
                data = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), i)
            LoadingCaption(0, version)
            pygame.display.update()
            data = pygame.image.load(os.path.join(base_folder, ("Resources\\Error_Resources\\Error_Message.png"))).convert()
            LoadingCaption(1, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) 
            pygame.display.update()
            data = pygame.image.load(os.path.join(base_folder, ("Resources\\Error_Resources\\Icon.jpg"))).convert()
            LoadingCaption(3, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.display.update()
            data = pygame.image.load(os.path.join(base_folder, ("Resources\\Folder_Resources\\FolderIcon.ico"))).convert()
            LoadingCaption(0, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.display.update()
            LoadingCaption(1, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.display.update()
            data = pywavefront.Wavefront(os.path.join(base_folder, ("Resources\\G3_Resources\\Player\\Man v2.obj")), create_materials=True, collect_faces=True)
            LoadingCaption(2, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
            pygame.display.update()
            data = pywavefront.Wavefront(os.path.join(base_folder, ("Resources\\G3_Resources\\Sun\\Sun.obj")), create_materials=True, collect_faces=True)
            LoadingCaption(3, version)
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.display.update()
            data = pywavefront.Wavefront(os.path.join(base_folder, ("Resources\\G3_Resources\\worldGUI\\Heart_FULL1.obj")), create_materials=True, collect_faces=True)
            LoadingCaption(0, version)
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) 
            pygame.display.update()
            data = pygame.image.load(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg"))).convert()
            LoadingCaption(1, version)
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.display.update()
            data = pygame.image.load(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg"))).convert()
            LoadingCaption(2, version)
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.display.update()
            data = pygame.image.load(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg"))).convert()
            LoadingCaption(3, version)
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.display.update()
            data = pygame.image.load(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg"))).convert()
            LoadingCaption(0, version)
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
            pygame.display.update()
            data = pygame.image.load(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg"))).convert()
            LoadingCaption(1, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.display.update()
            data = pygame.image.load(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg"))).convert()
            LoadingCaption(2, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.display.update()
            data = pygame.image.load(os.path.join(base_folder, "Resources\\General_Resources\\Icon.jpg")).convert()
            LoadingCaption(3, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.display.update()
            data = pygame.image.load(os.path.join(base_folder, "Resources\\General_Resources\\Icon.jpg")).convert()
            LoadingCaption(0, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.display.update()
            data = pygame.image.load(os.path.join(base_folder, f"Resources\\General_Resources\\selectorICONlight.jpg")).convert()
            data = pygame.image.load(os.path.join(base_folder, f"Resources\\General_Resources\\selectorICONdark.jpg")).convert()
            LoadingCaption(1, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.display.update()
            data = pygame.image.load(os.path.join(base_folder, "Resources\\General_Resources\\Saving_ERROR.jpg")).convert()
            LoadingCaption(2, version)
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
            pygame.display.update()
            pygame.mixer.music.load(os.path.join(base_folder, ("Resources\\General_Resources\\InventoryGeneral.ogg")))
            LoadingCaption(3, version)
            pygame.draw.line(Display, ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)
            pygame.display.update()
            data = pygame.mixer.music.load(os.path.join(base_folder, ("Resources\\General_Resources\\Click.ogg")))
            data = 0
            LoadingCaption(0, version)
            pygame.draw.line(Display, ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)
            pygame.display.update()
        else:
            defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] 
            pygame.draw.polygon(Display, ShapeCol, defLargeOctagon, width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)
            pygame.draw.line(Display, ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)
            pygame.draw.line(Display, ShapeCol, (575*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)


        def Start(Display, FontCol, BackgroundCol, ShapeCol, startUP):
            base_folder = os.path.dirname(__file__)
                
            Display.fill(BackgroundCol)
            pygame.display.flip()
            pygame.display.set_caption(f"Pycraft: v{version} | Welcome")
            PresentsFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
            PycraftFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 60)
            NameFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 45)

            NameText = NameFont.render("Tom Jebbo",True, FontCol)
            NameTextWidth = NameText.get_width()
            NameTextHeight = NameText.get_height()

            PresentsText = PresentsFont.render("presents",True, FontCol)
            PresentsTextWidth = PresentsText.get_width()

            PycraftText = PycraftFont.render("Pycraft",True, FontCol)
            PycraftTextWidth = PycraftText.get_width()
            PycraftTextHeight = PycraftText.get_height()

            iteration = 0
            clock = pygame.time.Clock()

            while iteration <= (60*3):
                realWidth, realHeight = pygame.display.get_window_size()
                Display.fill(BackgroundCol)
                Display.blit(NameText, ((realWidth-NameTextWidth)/2, (realHeight-NameTextHeight)/2))
                iteration += 1
                pygame.display.flip()
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit("Thanks for playing")
                        quit()
            iteration = 0

            while iteration <= (60*2):
                realWidth, realHeight = pygame.display.get_window_size()
                Display.fill(BackgroundCol)
                Display.blit(NameText, ((realWidth-NameTextWidth)/2, (realHeight-NameTextHeight)/2))
                Display.blit(PresentsText, ((((realWidth-NameTextWidth)/2)+120), ((realHeight-NameTextHeight)/2)+30))
                iteration += 1
                pygame.display.flip()
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit("Thanks for playing")
                        quit()

            iteration = 0

            while iteration <= (60*3):
                realWidth, realHeight = pygame.display.get_window_size()
                Display.fill(BackgroundCol)
                Display.blit(PycraftText, ((realWidth-PycraftTextWidth)/2, (realHeight-PycraftTextHeight)/2))
                iteration += 1
                pygame.display.flip()
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit("Thanks for playing")
                        quit()

            y = 0

            while True:
                realWidth, realHeight = pygame.display.get_window_size()
                Display.fill(BackgroundCol)
                Display.blit(PycraftText, ((realWidth-PycraftTextWidth)/2, ((realHeight-PycraftTextHeight)/2)-y))
                y += 1
                pygame.display.flip()
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit("Thanks for playing")
                        quit()
                if ((realHeight-PycraftTextHeight)/2)-y <= 0:
                    return True


        def PlayClickSound(soundVOL):
            channel1 = pygame.mixer.Channel(0)
            base_folder = os.path.dirname(__file__)
            clickMUSIC = pygame.mixer.Sound(os.path.join(base_folder, ("Resources\\General_Resources\\Click.ogg")))
            channel1.set_volume(soundVOL/100)
            channel1.play(clickMUSIC)

        def PlayFootstepsSound(soundVOL):
            channel2 = pygame.mixer.Channel(1)
            base_folder = os.path.dirname(__file__)
            file = f"Resources\\General_Resources\\footsteps{random.randint(0, 5)}.ogg"
            Footsteps = pygame.mixer.Sound(os.path.join(base_folder, (f"Resources\\G3_Resources\\GameSounds\\footsteps{random.randint(0, 5)}.ogg")))
            channel2.set_volume(soundVOL/100)
            channel2.play(Footsteps)


        def PlayInvSound(musicVOL):
            channel3 = pygame.mixer.Channel(2)
            base_folder = os.path.dirname(__file__)
            InvGen = pygame.mixer.Sound(os.path.join(base_folder, ("Resources\\General_Resources\\InventoryGeneral.ogg")))
            channel3.set_volume(musicVOL/100)
            channel3.play(InvGen)

        
        def PlayAmbientSound(soundVOL):
            channel4 = pygame.mixer.Channel(3)
            base_folder = os.path.dirname(__file__)
            LoadAmb = pygame.mixer.Sound(os.path.join(base_folder, ("Resources\\G3_Resources\\GameSounds\\FieldAmb.ogg")))
            channel4.set_volume(soundVOL/100)
            channel4.play(LoadAmb)


        def pilImageToSurface(pilImage):
            return pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode).convert()


        def settings(Display, themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, FanSky, FanPart, sound, soundVOL, music, musicVOL, theme, Fullscreen, SavedWidth, SavedHeight):
            base_folder = os.path.dirname(__file__)
            Display.fill(BackgroundCol)
            pygame.display.flip()
            VersionFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            MainTitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 60)
            InfoTitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
            LOWFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            MEDIUMFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            HIGHFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            ADAPTIVEFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            LightThemeFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            DarkThemeFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            DataFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            data1 = []
            icon = pygame.image.load(os.path.join(base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
            pygame.display.set_icon(icon)
            data2 = []
            data3 = []
            data4 = []
            run = 0
            rerun = 0
            TempMx = 0
            Mx, My = 0, 0
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

            SettingsInformationFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)

            scroll = 50

            FullscreenX, FullscreenY = pyautogui.size()

            while True:
                realWidth, realHeight = pygame.display.get_window_size()

                if realWidth < 1280:
                    Display = pygame.display.set_mode((1280, realHeight), RESIZABLE)
                if realHeight < 720:
                    Display = pygame.display.set_mode((realWidth, 720), RESIZABLE)

                yScaleFact = realHeight/720
                xScaleFact = realWidth/1280

                if pygame.mixer.get_busy() == 0:
                    if music == True:
                        PlayInvSound(musicVOL)

                TempMx = Mx
                iteration += 1
                Mx, My = pygame.mouse.get_pos()
                eFPS = clock.get_fps()
                aFPS += eFPS
                run += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        if sound == True:
                            PlayClickSound(soundVOL)

                        if Fullscreen == True:
                            Fullscreen = False
                        else:
                            Fullscreen = True
                        return themeArray, FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, FanSky, FanPart, sound, soundVOL, music, musicVOL, theme, Fullscreen
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and devmode < 10:
                            devmode += 1
                        if event.key == pygame.K_x:
                            devmode = 1
                            pygame.display.set_caption(f"Pycraft: v{version}: Settings")
                        if event.key == pygame.K_q:
                            DataWindow = tk.Tk()
                            DataWindow.title("Player Information") 
                            DataWindow.configure(width = 500, height = 300)
                            DataWindow.configure(bg="lightblue") 
                            VersionData = f"Pycraft: v{version}" 
                            CoordinatesData = f"Coordinates: x: {Mx} y: {My} z: 0.0 Facing: 0.0, 0.0, 0.0" 
                            FPSData = f"FPS: Actual: {eFPS} Max: {FPS}" 
                            VersionData = tk.Label(DataWindow, text=VersionData) 
                            CoordinatesData = tk.Label(DataWindow, text=CoordinatesData) 
                            FPSData = tk.Label(DataWindow, text=FPSData) 
                            VersionData.grid(row = 0, column = 0, columnspan = 2) 
                            CoordinatesData.grid(row = 1, column = 0, columnspan = 2)
                            FPSData.grid(row = 2, column = 0, columnspan = 2)
                            DataWindow.mainloop() 
                            DataWindow.quit()
                        if event.key == pygame.K_F11:
                            keydown = True
                            if keydown == True:
                                if Fullscreen == True:
                                    Fullscreen = False
                                    pygame.display.quit()
                                    pygame.init()
                                    Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                                    keydown = False
                                elif Fullscreen == False:
                                    Fullscreen = True
                                    Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF)
                                    keydown = False
                        if event.key == pygame.K_x: 
                            devmode = 1 
                            pygame.display.set_caption(f"Pycraft: v{version}: Settings") 
                    elif event.type == pygame.MOUSEBUTTONDOWN: 
                        mousebuttondown = True 
                    elif event.type == pygame.MOUSEBUTTONUP: 
                        mousebuttondown = False
                    if event.type == pygame.MOUSEWHEEL and realHeight <= 760:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
                        if str(event.y)[0] == "-":
                            scroll -= 5
                        else:
                            scroll += 5
                    else:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                if devmode >= 5 and devmode <= 9:
                    pygame.display.set_caption(f"Pycraft: v{version}: Settings | you are: {10-devmode} steps away from being a developer")
                elif devmode == 10:
                    pygame.display.set_caption(f"Pycraft: v{version}: Settings | Developer mode | V: 0, 0, 0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
                else:
                    pygame.display.set_caption(f"Pycraft: v{version}: Settings")

                if scroll >= 50:
                    scroll = 50
                if scroll <= 5:
                    scroll = 5

                titletFont = MainTitleFont.render("Pycraft", aa, FontCol)
                TitleWidth = titletFont.get_width()

                InfotFont = InfoTitleFont.render("Settings", aa, FontCol)
                InfoWidth = InfotFont.get_width()

                FPStFont = VersionFont.render(f"FPS: Actual: {int(eFPS)} Max: {int(FPS)} Adverage: {int((aFPS/iteration))}", aa, FontCol)
                FOVtFont = VersionFont.render(f"FOV: {FOV}", aa, FontCol)
                CamRottFont = VersionFont.render(f"Camera Rotation Speed: {round(cameraANGspeed, 1)}", aa, FontCol) 
                ModetFont = VersionFont.render("Mode;         ,                 ,            ,          .", aa, FontCol) 
                AAtFont = VersionFont.render(f"Anti-Aliasing: {aa}", aa, FontCol) 
                RenderFogtFont = VersionFont.render(f"Render Fog: {RenderFOG}", aa, FontCol)
                FancySkytFont = VersionFont.render(f"Fancy Skies: {FanSky}", aa, FontCol)
                FancyParticletFont = VersionFont.render(f"Fancy Partices: {FanPart}", aa, FontCol)
                SoundtFont = VersionFont.render(f"Sound: {sound}", aa, FontCol)
                if sound == True:
                    SoundVoltFont = VersionFont.render(f"Sound Volume: {soundVOL}%", aa, FontCol)
                else:
                    SoundVoltFont = VersionFont.render(f"Sound Volume: {soundVOL}%", aa, ShapeCol)
                MusictFont = VersionFont.render(f"Music: {music}", aa, FontCol)
                if music == True:
                    MusicVoltFont = VersionFont.render(f"Music Volume: {musicVOL}%", aa, FontCol)
                else:
                    MusicVoltFont = VersionFont.render(f"Music Volume: {musicVOL}%", aa, ShapeCol)
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
                MusicVolInformationFont = SettingsInformationFont.render("Controls the volume of the music, some effects may not apply until the game reloads", aa, AccentCol)
                Display.fill(BackgroundCol)
                FPS_rect = pygame.Rect(50, 180+scroll, 450*xScaleFact, 10)
                FOV_rect = pygame.Rect(50, 230+scroll, 450*xScaleFact, 10)
                CAM_rect = pygame.Rect(50, 280+scroll, 450*xScaleFact, 10)
                sound_rect = pygame.Rect(50, 580+scroll, 450*xScaleFact, 10)
                music_rect = pygame.Rect(50, 680+scroll, 450*xScaleFact, 10)
                aa_rect = pygame.Rect(50, 330+scroll, 50, 10)
                RenderFOG_Rect = pygame.Rect(50, 380+scroll, 50, 10)
                Fansky_Rect = pygame.Rect(50, 430+scroll, 50, 10)
                FanPart_Rect = pygame.Rect(50, 480+scroll, 50, 10)
                sound_Rect = pygame.Rect(50, 530+scroll, 50, 10)
                music_Rect = pygame.Rect(50, 630+scroll, 50, 10)
                slider_Rect = pygame.Rect(realWidth-15, scroll, 10, 665)
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
                pygame.draw.rect(Display, ShapeCol, music_Rect, 0)
                if mousebuttondown == True:
                    if My > 180+scroll and My < 190+scroll:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        if Mx > TempMx and FPS < 445: 
                            FPS += 1
                        elif Mx < TempMx and FPS > 15: 
                            FPS -= 1
                        if FPS < 15:
                            FPS = 16
                        elif FPS > 445:
                            FPS = 444
                        pygame.draw.circle(Display, AccentCol, (int(FPS+45)*xScaleFact, 185+scroll), 9)
                    else:
                        pygame.draw.circle(Display, (255, 255, 255), (int(FPS+45)*xScaleFact, 185+scroll), 9)

                    if My > 230+scroll and My < 240+scroll:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        if Mx > TempMx and FOV < 98:
                            FOV += 1
                        elif Mx < TempMx and FOV > 12:
                            FOV -= 1
                        if FOV < 12:
                            FOV = 13
                        elif FOV > 98:
                            FOV = 97
                        pygame.draw.circle(Display, AccentCol, (int(FOV*5)*xScaleFact, 235+scroll), 9)
                    else:
                        pygame.draw.circle(Display, (255, 255, 255), (int(FOV*5)*xScaleFact, 235+scroll), 9)

                    if My > 280+scroll and My < 290+scroll:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        if Mx > TempMx and cameraANGspeed < 5.0:
                            cameraANGspeed += 0.1
                        elif Mx < TempMx and cameraANGspeed > 0.0:
                            cameraANGspeed -= 0.1
                        if cameraANGspeed > 5.0:
                            cameraANGspeed = 4.9
                        elif cameraANGspeed <= 0:
                            cameraANGspeed = 0.1
                        pygame.draw.circle(Display, AccentCol, ((int(cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)
                    else:
                        pygame.draw.circle(Display, (255, 255, 255), ((int(cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)

                    if My > 580+scroll and My < 590+scroll and sound == True:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        if Mx > TempMx and soundVOL < 100:
                            soundVOL += 1
                        elif Mx < TempMx and soundVOL > 0:
                            soundVOL -= 1
                        if soundVOL > 100:
                            soundVOL = 100
                        elif soundVOL < 0:
                            soundVOL = 0
                        pygame.draw.circle(Display, AccentCol, ((int(soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)
                    else:
                        pygame.draw.circle(Display, (255, 255, 255), ((int(soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)

                    if My > 680+scroll and My < 690+scroll and music == True: 
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        if Mx > TempMx and musicVOL < 100:
                            musicVOL += 1
                        elif Mx < TempMx and musicVOL > 0:
                            musicVOL -= 1
                        if musicVOL > 100:
                            musicVOL = 100
                        elif musicVOL < 0:
                            musicVOL = 0
                        pygame.draw.circle(Display, AccentCol, ((int(musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)
                    else:
                        pygame.draw.circle(Display, (255, 255, 255), ((int(musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)

                    if My > 330+scroll and My < 340+scroll:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        if aa == True: 
                            aa = False 
                            if sound == True:
                                PlayClickSound(soundVOL)
                            mousebuttondown = False
                        elif aa == False: 
                            aa = True 
                            if sound == True:
                                PlayClickSound(soundVOL)
                            mousebuttondown = False
                    if aa == True: 
                        pygame.draw.circle(Display, (255, 255, 255), (90, 335+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 335+scroll), 6)
                    elif aa == False: 
                        pygame.draw.circle(Display, (255, 255, 255), (60, 335+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 335+scroll), 6)

                    if My > 380+scroll and My < 390+scroll:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
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
                    if RenderFOG == True:
                        pygame.draw.circle(Display, (255, 255, 255), (90, 385+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 385+scroll), 6)
                    elif RenderFOG == False:
                        pygame.draw.circle(Display, (255, 255, 255), (60, 385+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 385+scroll), 6)

                    if My > 430+scroll and My < 440+scroll:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
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
                        pygame.draw.circle(Display, (255, 255, 255), (90, 435+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 435+scroll), 6)
                    elif FanSky == False:
                        pygame.draw.circle(Display, (255, 255, 255), (60, 435+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 435+scroll), 6)

                    if My > 480+scroll and My < 490+scroll:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
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
                        pygame.draw.circle(Display, (255, 255, 255), (90, 485+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 485+scroll), 6)
                    elif FanPart == False:
                        pygame.draw.circle(Display, (255, 255, 255), (60, 485+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 485+scroll), 6)

                    if My > 530+scroll and My < 540+scroll:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
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
                        pygame.draw.circle(Display, (255, 255, 255), (90, 535+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 535+scroll), 6)
                    elif sound == False:
                        pygame.draw.circle(Display, (255, 255, 255), (60, 535+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 535+scroll), 6)

                    if My > 630+scroll and My < 640+scroll:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        if music == True:
                            music = False
                            pygame.mixer.Channel(2).stop()
                            if sound == True:
                                PlayClickSound(soundVOL)
                            mousebuttondown = False
                        elif music == False:
                            music = True
                            if sound == True:
                                PlayClickSound(soundVOL)
                            mousebuttondown = False
                    if music == True:
                        pygame.draw.circle(Display, (255, 255, 255), (90, 635+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 635+scroll), 6)
                    elif music == False:
                        pygame.draw.circle(Display, (255, 255, 255), (60, 635+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 635+scroll), 6)
                else:
                    pygame.draw.circle(Display, (255, 255, 255), ((int(soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)
                    pygame.draw.circle(Display, (255, 255, 255), ((int(FPS+45)*xScaleFact), 185+scroll), 9)
                    pygame.draw.circle(Display, (255, 255, 255), ((int(cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)
                    pygame.draw.circle(Display, (255, 255, 255), ((int(FOV*5))*xScaleFact, 235+scroll), 9)
                    pygame.draw.circle(Display, (255, 255, 255), ((int(musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)

                    if aa == True: 
                        pygame.draw.circle(Display, (255, 255, 255), (90, 335+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 335+scroll), 6)
                    elif aa == False: 
                        pygame.draw.circle(Display, (255, 255, 255), (60, 335+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 335+scroll), 6)

                    if RenderFOG == True:
                        pygame.draw.circle(Display, (255, 255, 255), (90, 385+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 385+scroll), 6)
                    elif RenderFOG == False:
                        pygame.draw.circle(Display, (255, 255, 255), (60, 385+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 385+scroll), 6)

                    if FanSky == True:
                        pygame.draw.circle(Display, (255, 255, 255), (90, 435+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 435+scroll), 6)
                    elif FanSky == False:
                        pygame.draw.circle(Display, (255, 255, 255), (60, 435+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 435+scroll), 6)

                    if FanPart == True:
                        pygame.draw.circle(Display, (255, 255, 255), (90, 485+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 485+scroll), 6)
                    elif FanPart == False:
                        pygame.draw.circle(Display, (255, 255, 255), (60, 485+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 485+scroll), 6)

                    if sound == True:
                        pygame.draw.circle(Display, (255, 255, 255), (90, 535+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 535+scroll), 6)
                    elif sound == False:
                        pygame.draw.circle(Display, (255, 255, 255), (60, 535+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 535+scroll), 6)

                    if music == True:
                        pygame.draw.circle(Display, (255, 255, 255), (90, 635+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (90, 635+scroll), 6)
                    elif music == False:
                        pygame.draw.circle(Display, (255, 255, 255), (60, 635+scroll), 9)
                        pygame.draw.circle(Display, ShapeCol, (60, 635+scroll), 6)

                    if My > 330+scroll and My < 340+scroll:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        Display.blit(AAInformationFont, (120, 325+scroll))
                        if aa == True:
                            pygame.draw.circle(Display, AccentCol, (90, 335+scroll), 9)
                            pygame.draw.circle(Display, ShapeCol, (90, 335+scroll), 6)
                        elif aa == False:
                            pygame.draw.circle(Display, AccentCol, (60, 335+scroll), 9)
                            pygame.draw.circle(Display, ShapeCol, (60, 335+scroll), 6)

                    if My > 380+scroll and My < 390+scroll:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        Display.blit(RenderFogInformationFont, (120, 375+scroll))
                        if RenderFOG == True:
                            pygame.draw.circle(Display, AccentCol, (90, 385+scroll), 9)
                            pygame.draw.circle(Display, ShapeCol, (90, 385+scroll), 6)
                        elif RenderFOG == False:
                            pygame.draw.circle(Display, AccentCol, (60, 385+scroll), 9)
                            pygame.draw.circle(Display, ShapeCol, (60, 385+scroll), 6)

                    if My > 430+scroll and My < 440+scroll:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        Display.blit(FancySkiesInformationFont, (120, 425+scroll))
                        if FanSky == True:
                            pygame.draw.circle(Display, AccentCol, (90, 435+scroll), 9)
                            pygame.draw.circle(Display, ShapeCol, (90, 435+scroll), 6)
                        elif FanSky == False:
                            pygame.draw.circle(Display, AccentCol, (60, 435+scroll), 9)
                            pygame.draw.circle(Display, ShapeCol, (60, 435+scroll), 6)

                    if My > 480+scroll and My < 490+scroll:
                        Display.blit(FancyParticlesInformationFont, (120, 475+scroll))
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        if FanPart == True:
                            pygame.draw.circle(Display, AccentCol, (90, 485+scroll), 9)
                            pygame.draw.circle(Display, ShapeCol, (90, 485+scroll), 6)
                        elif FanPart == False:
                            pygame.draw.circle(Display, AccentCol, (60, 485+scroll), 9)
                            pygame.draw.circle(Display, ShapeCol, (60, 485+scroll), 6)

                    if My > 530+scroll and My < 540+scroll:
                        Display.blit(SoundInformationFont, (120, 525+scroll))
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        if sound == True:
                            pygame.draw.circle(Display, AccentCol, (90, 535+scroll), 9)
                            pygame.draw.circle(Display, ShapeCol, (90, 535+scroll), 6)
                        elif sound == False:
                            pygame.draw.circle(Display, AccentCol, (60, 535+scroll), 9)
                            pygame.draw.circle(Display, ShapeCol, (60, 535+scroll), 6)

                    if My > 630+scroll and My < 640+scroll:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        Display.blit(MusicInformationFont, (120, 625+scroll))
                        if music == True:
                            pygame.draw.circle(Display, AccentCol, (90, 635+scroll), 9)
                            pygame.draw.circle(Display, ShapeCol, (90, 635+scroll), 6)
                        elif music == False:
                            pygame.draw.circle(Display, AccentCol, (60, 635+scroll), 9)
                            pygame.draw.circle(Display, ShapeCol, (60, 635+scroll), 6)

                if My >= 65+scroll and My <= 75+scroll:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    Display.blit(ThemeInformationFont, (300, 67+scroll))

                if My >= 65+scroll and My <= 75+scroll and Mx >= 55 and Mx <= 95:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
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

                if My >= 65+scroll and My <= 75+scroll and Mx >= 95 and Mx <= 135:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
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

                if My >= 85+scroll and My <= 95+scroll:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    Display.blit(ModeInformationFont, (300, 85+scroll))

                if My > 680+scroll and My < 690+scroll:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    Display.blit(MusicVolInformationFont, (520*xScaleFact, 675+scroll))

                if My > 580+scroll and My < 590+scroll:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    Display.blit(SoundVolInformationFont, (520*xScaleFact, 575+scroll))

                if My > 280+scroll and My < 290+scroll:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    Display.blit(CameraRotationSpeedInformationFont, (520*xScaleFact, 275+scroll))

                if My > 230+scroll and My < 240+scroll:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    Display.blit(FOVInformationFont, (520*xScaleFact, 225+scroll))

                if My > 180+scroll and My < 190+scroll:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    Display.blit(FPSInformationFont, (520*xScaleFact, 175+scroll))

                if My >= 85+scroll and My <= 95+scroll and Mx >= 40 and Mx <= 80:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    LOWtFont = LOWFont.render("Low", aa, AccentCol)
                    LOWFont.set_underline(True)
                    if mousebuttondown == True:
                        rendis = 60
                        FPS = random.randint(15, 30)
                        aa = False
                        RenderFOG = False
                        FanSky = False
                        FanPart = False
                        mousebuttondown = False
                        if sound == True:
                            PlayClickSound(soundVOL)
                else:
                    LOWtFont = LOWFont.render("Low", aa, FontCol)
                    LOWFont.set_underline(False)

                if My >= 85+scroll and My <= 95+scroll and Mx >= 90 and Mx <= 155:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    MEDIUMtFont = MEDIUMFont.render("Medium", aa, AccentCol)
                    MEDIUMFont.set_underline(True)
                    if mousebuttondown == True:
                        rendis = 80
                        FPS = random.randint(30, 60)
                        aa = True
                        RenderFOG = False
                        FanSky = True
                        FanPart = False
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                else:
                    MEDIUMtFont = MEDIUMFont.render("Medium", aa, FontCol)
                    MEDIUMFont.set_underline(False)

                if My >= 85+scroll and My <= 95+scroll and Mx >= 165 and Mx <= 205:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    HIGHFontText = HIGHFont.render("High", aa, AccentCol)
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
                    HIGHFontText = HIGHFont.render("High", aa, FontCol)
                    HIGHFont.set_underline(False)

                if My >= 85+scroll and My <= 95+scroll and Mx >= 215 and Mx <= 300:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    ADAPTIVEtFont = ADAPTIVEFont.render("Adaptive", aa, AccentCol)
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
                    ADAPTIVEtFont = ADAPTIVEFont.render("Adaptive", aa, FontCol)
                    ADAPTIVEFont.set_underline(False)

                Display.blit(FPStFont, (0, 150+scroll))
                Display.blit(FOVtFont, (0, 200+scroll))
                Display.blit(CamRottFont, (0, 250+scroll))
                Display.blit(ModetFont, (0, 85+scroll)) 
                Display.blit(LOWtFont, (48, 85+scroll))
                Display.blit(MEDIUMtFont, (90, 85+scroll))
                Display.blit(HIGHFontText, (165, 85+scroll))
                Display.blit(ADAPTIVEtFont, (215, 85+scroll)) 
                Display.blit(AAtFont, (0, 300+scroll))
                Display.blit(RenderFogtFont, (0, 350+scroll))
                Display.blit(FancySkytFont, (0, 400+scroll))
                Display.blit(FancyParticletFont, (0, 450+scroll))
                Display.blit(SoundtFont, (0, 500+scroll))
                Display.blit(SoundVoltFont, (0, 550+scroll))
                Display.blit(MusictFont, (0, 600+scroll))
                Display.blit(MusicVoltFont, (0, 650+scroll))
                Display.blit(ThemeFont, (0, 65+scroll))
                Display.blit(LightTheme, (55, 65+scroll))
                Display.blit(DarkTheme, (95, 65+scroll))
                pygame.draw.circle(Display, ShapeCol, (int(FPS+45)*xScaleFact, 185+scroll), 6)
                pygame.draw.circle(Display, ShapeCol, (int(FOV*5)*xScaleFact, 235+scroll), 6)
                pygame.draw.circle(Display, ShapeCol, ((int(cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 6)
                pygame.draw.circle(Display, ShapeCol, ((int(soundVOL*4.4)+50)*xScaleFact, 585+scroll), 6)
                pygame.draw.circle(Display, ShapeCol, ((int(musicVOL*4.4)+50)*xScaleFact, 685+scroll), 6)
                
                cover_Rect = pygame.Rect(0, 0, 1280, 100)
                pygame.draw.rect(Display, (BackgroundCol), cover_Rect)
                Display.blit(titletFont, ((realWidth-TitleWidth)/2, 0))
                Display.blit(InfotFont, (((realWidth-TitleWidth)/2)+55, 50))

                if realHeight <= 760:
                    pygame.draw.rect(Display, ShapeCol, slider_Rect, 0)

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
                    data4.append([((run/5)+1000), ((450-(((aFPS/iteration)+80)/4)-250))]) 
                if devmode == 10: 
                    dev_Rect = pygame.Rect(1000, 0, 200, 200)
                    pygame.draw.rect(Display, (80, 80, 80), dev_Rect)
                    if run >= 10:
                        pygame.draw.lines(Display, (0, 255, 0), False, (data2))
                        pygame.draw.lines(Display, (255, 0, 0), False, (data1))
                        pygame.draw.lines(Display, (0, 0, 255), False, (data3))
                        pygame.draw.lines(Display, (255, 0, 255), False, (data4))
                        pygame.draw.line(Display, (255, 255, 255), (((run/5)+1000), 20), (((run/5)+1000), 200))
                    runFont = DataFont.render(f"{psutil.virtual_memory().percent} | {str(psutil.cpu_percent())} | {str(run)} | {str(rerun)} | {str(round(eFPS, 2))}", False, (255, 255, 255)) 
                    Display.blit(runFont, (1000, 0)) 
                pygame.display.flip() 
                clock.tick(FPS) 


        def Character_Customiser(Display, FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, aa, FPS, theme, AccentCol, startUP, Fullscreen, SavedWidth, SavedHeight):
            base_folder = os.path.dirname(__file__)
            Display.fill(BackgroundCol) 
            pygame.display.flip() 
            if devmode == 10 or devmode-10 == 0: 
                pygame.display.set_caption(f"Pycraft: v{version}: Character Customiser | Developer Mode | V: 0, 0, 0 | FPS: {clock.get_fps()} aFPS: {clock.get_fps()} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())}") 
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Character Customiser")
            VersionFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15) 
            MainTitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 60) 
            InfoTitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
            DataFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            Mx, My = pygame.mouse.get_pos()
            data1 = []
            data2 = []
            data3 = []
            data4 = []
            icon = pygame.image.load(os.path.join(base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
            pygame.display.set_icon(icon)
            run = 0
            rerun = 0
            aFPS = 0
            iteration = 1
            TitleFont = MainTitleFont.render("Pycraft", aa, FontCol)
            TitleWidth = TitleFont.get_width()

            CharCustFont = InfoTitleFont.render("Character Customiser", aa, FontCol)
            tempFPS = FPS

            FullscreenX, FullscreenY = pyautogui.size()

            while True:
                realWidth, realHeight = pygame.display.get_window_size()

                if realWidth < 1280:
                    Display = pygame.display.set_mode((1280, realHeight), RESIZABLE)
                if realHeight < 720:
                    Display = pygame.display.set_mode((realWidth, 720), RESIZABLE)

                yScaleFact = realHeight/720
                xScaleFact = realWidth/1280

                eFPS = clock.get_fps()
                aFPS += eFPS 
                Mx, My = pygame.mouse.get_pos() 
                run += 1
                iteration += 1
                if pygame.display.get_active() == False:
                    tempFPS = 15
                else:
                    tempFPS = FPS

                if pygame.mixer.get_busy() == 0:
                    if music == True:
                        PlayInvSound(musicVOL)

                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                        if sound == True:
                            PlayClickSound(soundVOL)
                        return Fullscreen
                    elif event.type == pygame.KEYDOWN: 
                        if event.key == pygame.K_SPACE and devmode < 10: 
                            devmode += 1 
                        if event.key == pygame.K_q:
                            DataWindow = tk.Tk()
                            DataWindow.title("Player Information") 
                            DataWindow.configure(width = 500, height = 300) 
                            DataWindow.configure(bg="lightblue") 
                            VersionData = f"Pycraft: v{version}" 
                            CoordinatesData = f"Coordinates: x: {Mx} y: {My} z: 0.0 Facing: 0.0, 0.0, 0.0" 
                            FPSData = f"FPS: Actual: {eFPS} Max: {FPS}" 
                            VersionData = tk.Label(DataWindow, text=VersionData) 
                            CoordinatesData = tk.Label(DataWindow, text=CoordinatesData) 
                            FPSData = tk.Label(DataWindow, text=FPSData) 
                            VersionData.grid(row = 0, column = 0, columnspan = 2) 
                            CoordinatesData.grid(row = 1, column = 0, columnspan = 2)
                            FPSData.grid(row = 2, column = 0, columnspan = 2)
                            DataWindow.mainloop() 
                            DataWindow.quit()
                        if event.key == pygame.K_F11:
                            keydown = True
                            if keydown == True:
                                if Fullscreen == True:
                                    Fullscreen = False
                                    pygame.display.quit()
                                    pygame.init()
                                    Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                                    keydown = False
                                elif Fullscreen == False:
                                    Fullscreen = True
                                    Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF)
                                    keydown = False
                        if event.key == pygame.K_x: 
                            devmode = 1 
                            pygame.display.set_caption(f"Pycraft: v{version}: Character Customiser")
                if devmode >= 5 and devmode <= 9: 
                    pygame.display.set_caption(f"Pycraft: v{version}: Character Customiser | you are: {10-devmode} steps away from being a developer") 
                elif devmode == 10: 
                    pygame.display.set_caption(f"Pycraft: v{version}: Character Customiser | Developer mode | V: 0, 0, 0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())}") 
                else:
                    pygame.display.set_caption(f"Pycraft: v{version}: Character Customiser") 

                Display.fill(BackgroundCol)

                cover_Rect = pygame.Rect(0, 0, 1280, 90)
                pygame.draw.rect(Display, (BackgroundCol), cover_Rect)
                Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))
                Display.blit(CharCustFont, (((realWidth-TitleWidth)/2)+60, 50))
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
                if devmode == 10: 
                    dev_Rect = pygame.Rect(1000, 0, 200, 200)
                    pygame.draw.rect(Display, (80, 80, 80), dev_Rect)
                    if run >= 10:
                        pygame.draw.lines(Display, (0, 255, 0), False, (data2))
                        pygame.draw.lines(Display, (255, 0, 0), False, (data1))
                        pygame.draw.lines(Display, (0, 0, 255), False, (data3))
                        pygame.draw.lines(Display, (255, 0, 255), False, (data4))
                        pygame.draw.line(Display, (255, 255, 255), (((run/5)+1000), 20), (((run/5)+1000), 200))
                    runFont = DataFont.render(f"{psutil.virtual_memory().percent} | {str(psutil.cpu_percent())} | {str(run)} | {str(rerun)} | {str(round(eFPS, 2))}", False, (255, 255, 255)) 
                    Display.blit(runFont, (1000, 0)) 
                pygame.display.flip() 
                clock.tick(tempFPS) 


        def Achievements(Display, FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, aa, FPS, theme, AccentCol, Fullscreen, SavedWidth, SavedHeight):
            base_folder = os.path.dirname(__file__)
            Display.fill(BackgroundCol) 
            pygame.display.flip()
            if devmode == 10 or devmode-10 == 0: 
                pygame.display.set_caption(f"Pycraft: v{version}: Achievements | Developer Mode | V: 0, 0, 0 | FPS: {clock.get_fps()} aFPS: {clock.get_fps()} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())}") 
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Achievements")
            VersionFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15) 
            MainTitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 60) 
            InfoTitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
            DataFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            Mx, My = pygame.mouse.get_pos()
            data1 = []
            data2 = []
            data3 = []
            data4 = []
            icon = pygame.image.load(os.path.join(base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
            pygame.display.set_icon(icon)
            run = 0
            rerun = 0
            aFPS = 0
            iteration = 1
            TitleFont = MainTitleFont.render("Pycraft", aa, FontCol)
            TitleWidth = TitleFont.get_width()

            AchievementsFont = InfoTitleFont.render("Achievements", aa, FontCol)
            tempFPS = FPS

            FullscreenX, FullscreenY = pyautogui.size()

            while True:
                realWidth, realHeight = pygame.display.get_window_size()

                if realWidth < 1280:
                    Display = pygame.display.set_mode((1280, realHeight), RESIZABLE)
                if realHeight < 720:
                    Display = pygame.display.set_mode((realWidth, 720), RESIZABLE)

                yScaleFact = realHeight/720
                xScaleFact = realWidth/1280

                eFPS = clock.get_fps()
                aFPS += eFPS 
                Mx, My = pygame.mouse.get_pos() 
                run += 1
                iteration += 1
                if pygame.display.get_active() == False:
                    tempFPS = 15
                else:
                    tempFPS = FPS

                if pygame.mixer.get_busy() == 0:
                    if music == True:
                        PlayInvSound(musicVOL)

                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                        if sound == True:
                            PlayClickSound(soundVOL)
                        return Fullscreen
                    elif event.type == pygame.KEYDOWN: 
                        if event.key == pygame.K_SPACE and devmode < 10: 
                            devmode += 1 
                        if event.key == pygame.K_q:
                            DataWindow = tk.Tk()
                            DataWindow.title("Player Information") 
                            DataWindow.configure(width = 500, height = 300) 
                            DataWindow.configure(bg="lightblue") 
                            VersionData = f"Pycraft: v{version}" 
                            CoordinatesData = f"Coordinates: x: {Mx} y: {My} z: 0.0 Facing: 0.0, 0.0, 0.0" 
                            FPSData = f"FPS: Actual: {eFPS} Max: {FPS}" 
                            VersionData = tk.Label(DataWindow, text=VersionData) 
                            CoordinatesData = tk.Label(DataWindow, text=CoordinatesData) 
                            FPSData = tk.Label(DataWindow, text=FPSData) 
                            VersionData.grid(row = 0, column = 0, columnspan = 2) 
                            CoordinatesData.grid(row = 1, column = 0, columnspan = 2)
                            FPSData.grid(row = 2, column = 0, columnspan = 2)
                            DataWindow.mainloop() 
                            DataWindow.quit()
                        if event.key == pygame.K_F11:
                            keydown = True
                            if keydown == True:
                                if Fullscreen == True:
                                    Fullscreen = False
                                    pygame.display.quit()
                                    pygame.init()
                                    Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                                    keydown = False
                                elif Fullscreen == False:
                                    Fullscreen = True
                                    Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF)
                                    keydown = False
                        if event.key == pygame.K_x: 
                            devmode = 1 
                            pygame.display.set_caption(f"Pycraft: v{version}: Achievements")
                if devmode >= 5 and devmode <= 9: 
                    pygame.display.set_caption(f"Pycraft: v{version}: Achievements | you are: {10-devmode} steps away from being a developer") 
                elif devmode == 10: 
                    pygame.display.set_caption(f"Pycraft: v{version}: Achievements | Developer mode | V: 0, 0, 0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())}") 
                else:
                    pygame.display.set_caption(f"Pycraft: v{version}: Achievements") 
                        
                Display.fill(BackgroundCol)

                cover_Rect = pygame.Rect(0, 0, 1280, 90)
                pygame.draw.rect(Display, (BackgroundCol), cover_Rect)
                Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))
                Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))
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
                if devmode == 10: 
                    dev_Rect = pygame.Rect(1000, 0, 200, 200)
                    pygame.draw.rect(Display, (80, 80, 80), dev_Rect)
                    if run >= 10:
                        pygame.draw.lines(Display, (0, 255, 0), False, (data2))
                        pygame.draw.lines(Display, (255, 0, 0), False, (data1))
                        pygame.draw.lines(Display, (0, 0, 255), False, (data3))
                        pygame.draw.lines(Display, (255, 0, 255), False, (data4))
                        pygame.draw.line(Display, (255, 255, 255), (((run/5)+1000), 20), (((run/5)+1000), 200))
                    runFont = DataFont.render(f"{psutil.virtual_memory().percent} | {str(psutil.cpu_percent())} | {str(run)} | {str(rerun)} | {str(round(eFPS, 2))}", False, (255, 255, 255)) 
                    Display.blit(runFont, (1000, 0)) 
                pygame.display.flip() 
                clock.tick(tempFPS)


        def Benchmark(Display, FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, aa, FPS, theme, AccentCol, Fullscreen, SavedWidth, SavedHeight):
            pygame.mixer.music.stop()
            base_folder = os.path.dirname(__file__)
            Display.fill(BackgroundCol) 
            pygame.display.flip()
            pygame.display.set_caption(f"Pycraft: v{version}: Benchmark")
            VersionFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15) 
            MainTitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 60) 
            InfoTitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
            DataFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            DetailsFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 20)
            InfoDetailsFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            TitleFont = MainTitleFont.render("Pycraft", aa, FontCol)
            TitleWidth = TitleFont.get_width()

            BenchmarkFont = InfoTitleFont.render("Benchmark", aa, FontCol)
            FPSinfoTEXT = DetailsFont.render("FPS benchmark results", aa, FontCol)
            FPSinfoTEXTWidth = FPSinfoTEXT.get_width()
            FILEinfoTEXT = DetailsFont.render("Read test results", aa, FontCol)
            FILEinfoTEXTWidth = FILEinfoTEXT.get_width()
            HARDWAREinfoTEXT = DetailsFont.render("Hardware results", aa, FontCol)
            HARDWAREinfoTEXTwidth = HARDWAREinfoTEXT.get_width()

            SixtyFPSData = DataFont.render("60 Hz", aa, AccentCol)
            OneFourFourFPSData = DataFont.render("144 Hz", aa, AccentCol)
            TwoFourtyFPSData = DataFont.render("240 Hz", aa, AccentCol)

            InfoFont1 = DataFont.render("Welcome to Benchmark mode, press the SPACE bar to continue or press ANY other key to cancel, or press 'X'", aa, FontCol)
            InfoFont2 = DataFont.render("Benchmark mode is used to make the 'ADAPTIVE' feature in settings function and also to give an indication of the experience you are likely to get on this device", aa, FontCol)
            InfoFont3 = DataFont.render("Benchmark mode consists of several stages:", aa, FontCol)
            InfoFont4 = DataFont.render("First it will gather some basic information about your system", aa, FontCol)
            InfoFont5 = DataFont.render("Then it will test your maximum frame rate on a blank screen, then with a basic animation, and finally in a 3D OpenGL space", aa, FontCol)
            InfoFont6 = DataFont.render("After its done that the focus moves on to a quick storage test, before finishing", aa, FontCol)
            InfoFont7 = DataFont.render("Your results will then be displayed on screen with your frame rate scores on a line graph and the rest detailed to the right", aa, FontCol)
            InfoFont8 = DataFont.render("During the time the benchmark is running the window may appear unresponsive, don't panic this can be expected.", aa, FontCol)
            InfoFont9 = DataFont.render("In addition to achieve the best scores try to avoid doing anything else on the computer whilst the benchmark runs", aa, FontCol)
            InfoFont10 = DataFont.render("This benchmark may show some system instability or cause your device to get warm, you use this at your own risk!", aa, (255, 0, 0))

            tempFPS = FPS
            Mx, My = pygame.mouse.get_pos()

            iteration = 0
            stage = 0
            icon = pygame.image.load(os.path.join(base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
            pygame.display.set_icon(icon)

            FullscreenX, FullscreenY = pyautogui.size()

            resize = False

            while True:
                realWidth, realHeight = pygame.display.get_window_size()

                if realWidth < 1280:
                    Display = pygame.display.set_mode((1280, realHeight), RESIZABLE)
                if realHeight < 720:
                    Display = pygame.display.set_mode((realWidth, 720), RESIZABLE)

                yScaleFact = realHeight/720
                xScaleFact = realWidth/1280

                if stage == 0:
                    Display.fill(BackgroundCol)
                    cover_Rect = pygame.Rect(0, 0, 1280, 90)
                    pygame.draw.rect(Display, (BackgroundCol), cover_Rect)
                    Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))
                    Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))
                    Display.blit(InfoFont1, (3, 100))
                    Display.blit(InfoFont2, (3, 130))
                    Display.blit(InfoFont3, (3, 145))
                    Display.blit(InfoFont4, (3, 160))
                    Display.blit(InfoFont5, (3, 175))
                    Display.blit(InfoFont6, (3, 190))
                    Display.blit(InfoFont7, (3, 220))
                    Display.blit(InfoFont8, (3, 235))
                    Display.blit(InfoFont9, (3, 250))
                    Display.blit(InfoFont10, (3, 280))

                if stage == 1:
                    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Getting System Information")
                    CPUid = f"{cpuinfo.get_cpu_info()['brand_raw']} w/{psutil.cpu_count(logical=False)} cores @ {psutil.cpu_freq().max} MHz"
                    RAMid = f"{round((((psutil.virtual_memory().total)/1000)/1000/1000),2)} GB of memory, with {psutil.virtual_memory().percent}% used"
                    CPUhwINFO = DataFont.render(CPUid, aa, (255, 255, 255))
                    CPUhwINFOwidth = CPUhwINFO.get_width()

                    RAMhwINFO = DataFont.render(RAMid, aa, (255, 255, 255))
                    RAMhwINFOwidth = RAMhwINFO.get_width()
                    stage += 1

                if stage == 2: # actually 2
                    try:
                        SavedWidth, SavedHeight = pygame.display.get_window_size()
                        FPSlistX, FPSlistY, FPSlistX2, FPSlistY2 = ExBenchmark.run(version, BackgroundCol, ShapeCol)
                        try:
                            FullscreenX, FullscreenY = pyautogui.size()
                            if Fullscreen == False:
                                #Fullscreen = True
                                pygame.display.quit()
                                pygame.init()
                                Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                                keydown = False
                            elif Fullscreen == True:
                                #Fullscreen = False
                                pygame.display.quit()
                                pygame.init()
                                Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF)
                                keydown = False
                        except Exception as error:
                            SavedWidth = 1280
                            SavedHeight = 720
                            pygame.display.quit()
                            pygame.init()
                            Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                            keydown = False
                    except:
                        pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Cancelled benchmark")
                        Home_Screen(Display, themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, musicVOL, camera_x, camera_y, camera_z, size, theme, lastRun, startUP, Fullscreen, SavedWidth, SavedHeight)
                    else:
                        pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Finished FPS based benchmarks")
                    stage += 1

                if stage == 3: # actually 3
                    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Starting disk read test")
                    aTime = 0
                    ReadIteration = 50
                    for i in range(ReadIteration):
                        start = time.perf_counter()
                        with open(os.path.join(base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:
                            Benchdata = Bench.read()
                        aTime += time.perf_counter()-start
                    aTime = aTime/(ReadIteration+1)
                    ReadSpeed = (1/(aTime))
                    stage += 1
                
                if stage == 4:
                    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Processing Results.")
                    Max1 = 0
                    Min1 = 60
                    for i in range(len(FPSlistY)):
                        if FPSlistY[i] > Max1:
                            Max1 = FPSlistY[i]
                        if FPSlistY[i] < Min1:
                            Min1 = FPSlistY[i]

                    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Processing Results..")
                    Max2 = 0
                    Min2 = 60
                    for i in range(len(FPSlistY2)):
                        if FPSlistY2[i] > Max2:
                            Max2 = FPSlistY[i]
                        if FPSlistY2[i] < Min2:
                            Min2 = FPSlistY[i]

                    if Max2 > Max1:
                        GlobalMax = Max2
                    else:
                        GlobalMax = Max1

                    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Processing Results...")
                    multiplier = len(FPSlistY)/(realWidth-20)
                    temp = []
                    for i in range(len(FPSlistY)):
                        temp.append(130+(300-((300/GlobalMax)*FPSlistY[i])))
                    FPSListY = temp

                    temp = []
                    for i in range(len(FPSlistY2)):
                        temp.append(130+(300-((300/GlobalMax)*FPSlistY2[i])))
                    FPSListY2 = temp

                    Results1 = []
                    for i in range(len(FPSlistY)):
                        Results1.append([(FPSlistX[i]/multiplier), FPSListY[i]])

                    Results2 = []
                    for i in range(len(FPSlistY2)):
                        Results2.append([(FPSlistX2[i]/multiplier), FPSListY2[i]])

                    stage += 1

                if stage == 5:
                    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Results")

                    Display.fill(BackgroundCol)

                    Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))
                    Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))

                    FPSRect = pygame.Rect(10, 130, realWidth-20, 300)
                    pygame.draw.rect(Display, ShapeCol, FPSRect, 0)

                    pygame.draw.line(Display, AccentCol, (10, int(130+(300-((300/GlobalMax)*60)))), (realWidth-20, int(130+(300-((300/GlobalMax)*60)))))
                    Display.blit(SixtyFPSData, (13, int(130+(300-((300/GlobalMax)*60)))))

                    pygame.draw.line(Display, AccentCol, (10, int(130+(300-((300/GlobalMax)*144)))), (realWidth-20, int(130+(300-((300/GlobalMax)*144)))))
                    Display.blit(OneFourFourFPSData, (13, int(130+(300-((300/GlobalMax)*140)))))

                    pygame.draw.line(Display, AccentCol, (10, int(130+(300-((300/GlobalMax)*240)))), (realWidth-20, int(130+(300-((300/GlobalMax)*240)))))
                    Display.blit(TwoFourtyFPSData, (13, int(130+(300-((300/GlobalMax)*240)))))

                    pygame.draw.lines(Display, (0, 255, 0), False, Results1)
                    pygame.draw.lines(Display, (0, 0, 255), False, Results2)

                    HideRect = pygame.Rect(0, 110, realWidth, 330)
                    pygame.draw.rect(Display, BackgroundCol, HideRect, 20)
                    
                    Display.blit(FPSinfoTEXT, ((realWidth-FPSinfoTEXTWidth)-3, 100))
                    Display.blit(FILEinfoTEXT, ((realWidth-FILEinfoTEXTWidth)-3, 430))

                    FileResults = DataFont.render(f"Your device achieved a score of: {round(ReadSpeed, 2)}/100 ({round((100/100)*ReadSpeed)}%)", aa, FontCol)
                    FileResultsWidth = FileResults.get_width()
                    Display.blit(FileResults, ((realWidth-FileResultsWidth)-3, 460))
                    
                    Display.blit(HARDWAREinfoTEXT, ((realWidth-HARDWAREinfoTEXTwidth)-3, 480))

                    Display.blit(CPUhwINFO, ((realWidth-CPUhwINFOwidth)-3, 500))
                    Display.blit(RAMhwINFO, ((realWidth-RAMhwINFOwidth)-3, 516))

                    GreenInfo = InfoDetailsFont.render(f"Blank screen test; Minimum: {round(Min1, 4)}, Maximum: {round(Max1, 4)}", aa, FontCol)
                    BlueInfo = InfoDetailsFont.render(f"Drawing test; Minimum: {round(Min2, 4)}, Maximum: {round(Max2, 4)}", aa, FontCol)
                    Display.blit(GreenInfo, (3, 430))
                    Display.blit(BlueInfo, (3, 445))

                    if resize == True:
                        stage = 4
                        resize = False



                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE) and stage <= 3) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                        if sound == True:
                            PlayClickSound(soundVOL)
                        return Fullscreen
                    if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) and stage == 0:
                        stage += 1
                    if event.type == pygame.VIDEORESIZE:
                        resize = True

                pygame.display.flip()
                clock.tick(FPS)


        def Credits(Display, FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, aa, FPS, theme, AccentCol, Fullscreen, SavedWidth, SavedHeight):
            base_folder = os.path.dirname(__file__)
            Display.fill(BackgroundCol)
            pygame.mixer.Channel(2).stop()
            pygame.display.flip() 
            if devmode == 10 or devmode-10 == 0: 
                pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log | Developer Mode | V: 0, 0, 0 | FPS: {clock.get_fps()} aFPS: {clock.get_fps()} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())}") 
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log") 
            VersionFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            LargeCreditsFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 20)
            SmallCreditsFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15) 
            MainTitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 60) 
            InfoTitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
            DataFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            Mx, My = pygame.mouse.get_pos() 
            data1 = []
            data2 = []
            data3 = []
            data4 = []        
            icon = pygame.image.load(os.path.join(base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
            pygame.display.set_icon(icon)
            run = 0
            rerun = 0
            aFPS = 0
            iteration = 1
            TitleFont = MainTitleFont.render("Pycraft", aa, FontCol)
            TitleWidth = TitleFont.get_width()
            TitleHeight = TitleFont.get_height()

            CreditsFont = InfoTitleFont.render("Credits", aa, FontCol) 
            Credits1 = LargeCreditsFont.render("Pycraft: v0.9", aa, FontCol)
            Credits1Width = Credits1.get_width()
            Credits2 = LargeCreditsFont.render("Game Director: Tom Jebo", aa, FontCol)
            Credits2Width = Credits2.get_width()
            Credits3 = LargeCreditsFont.render("Art and Music Lead: Tom Jebbo", aa, FontCol)
            Credits3Width = Credits3.get_width()
            Credits4 = LargeCreditsFont.render("Other Music Credits:", aa, FontCol)
            Credits4Width = Credits4.get_width()
            Credits5 = LargeCreditsFont.render("Freesound: - Erokia's 'ambient wave compilation' @ https://freesound.org/s/473545", aa, FontCol)
            Credits5Width = Credits5.get_width()
            Credits6 = LargeCreditsFont.render("Freesound: - Soundholder's 'ambient meadow near forest' @ https://freesound.org/s/425368", aa, FontCol)
            Credits6Width = Credits6.get_width()
            Credits7 = LargeCreditsFont.render("Freesound: - monte32's 'Footsteps_6_Dirt_shoe' @ https://freesound.org/people/monte32/sounds/353799", aa, FontCol)
            Credits7Width = Credits7.get_width()
            Credits8 = LargeCreditsFont.render("With thanks to the developers of:", aa, FontCol)
            Credits8Width = Credits8.get_width()
            Credits9 = LargeCreditsFont.render("PSutil", aa, FontCol)
            Credits9Width = Credits9.get_width()
            Credits10 = LargeCreditsFont.render("Python", aa, FontCol)
            Credits10Width = Credits10.get_width()
            Credits11 = LargeCreditsFont.render("Pygame", aa, FontCol)
            Credits11Width = Credits11.get_width()
            Credits12 = LargeCreditsFont.render("Numpy", aa, FontCol)
            Credits12Width = Credits12.get_width()
            Credits13 = LargeCreditsFont.render("Nuitka", aa, FontCol)
            Credits13Width = Credits13.get_width()
            Credits14 = LargeCreditsFont.render("CPUinfo", aa, FontCol)
            Credits14Width = Credits14.get_width()
            Credits15 = LargeCreditsFont.render("PyInstaller", aa, FontCol)
            Credits15Width = Credits15.get_width()
            Credits16 = LargeCreditsFont.render("PyAutoGUI", aa, FontCol)
            Credits16Width = Credits16.get_width()
            Credits17 = LargeCreditsFont.render("PyWaveFront", aa, FontCol)
            Credits17Width = Credits17.get_width()
            Credits18 = LargeCreditsFont.render("Microsoft's Visual Studio Code", aa, FontCol)
            Credits18Width = Credits18.get_width()
            Credits19 = LargeCreditsFont.render("PIL (Pillow/Python Imaging Libary)", aa, FontCol)
            Credits19Width = Credits19.get_width()
            Credits20 = LargeCreditsFont.render("PyOpenGL (and PyOpenGL-accelerate)", aa, FontCol)
            Credits20Width = Credits20.get_width()
            Credits21 = LargeCreditsFont.render("For more in depth accreditation please check the GitHub Page @ https://github.com/PycraftDeveloper/Pycraft", aa, FontCol)
            Credits21Width = Credits21.get_width()
            Credits22 = LargeCreditsFont.render("With thanks to:", aa, FontCol)
            Credits22Width = Credits22.get_width()
            Credits23 = LargeCreditsFont.render("All my wonderful followers on Twitter, and you for installing this game, that's massively appreciated!", aa, FontCol)
            Credits23Width = Credits23.get_width()
            Credits24 = LargeCreditsFont.render("For full change-log please visit my aforementioned GitHub profile", aa, FontCol)
            Credits24Width = Credits24.get_width()
            Credits25 = LargeCreditsFont.render("Disclaimer:", aa, FontCol)
            Credits25Width = Credits25.get_width()
            Credits26 = VersionFont.render("The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your", aa, AccentCol)
            Credits26Width = Credits26.get_width()
            Credits27 = VersionFont.render("friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve", aa, AccentCol)
            Credits27Width = Credits27.get_width()
            Credits28 = VersionFont.render("my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo", aa, AccentCol)
            Credits28Width = Credits28.get_width()
            Credits29 = VersionFont.render("DOES NOT TAKE ANY RESPONCIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXERNAL MODULES INSTALLED ONTO", aa, AccentCol)
            Credits29Width = Credits29.get_width()
            Credits30 = VersionFont.render("YOUR COMPUTER (WHEN NOT CHOOSING THE RECOMMENDED EXECUTABLE VERSION) ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM", aa, AccentCol)
            Credits30Width = Credits30.get_width()
            Credits31 = VersionFont.render(" RESPONCIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVICES MAGAGER OR ADMINISTRATOR TO INSTALL AND USE", aa, AccentCol)
            Credits31Width = Credits31.get_width()
            Credits32 = VersionFont.render(" COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVICE, AND AT ANY POINT NO CONNECTION TO A", aa, AccentCol)
            Credits32Width = Credits32.get_width()
            Credits33 = VersionFont.render(" NETWORK IS REQUIRED. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you.", aa, AccentCol)
            Credits33Width = Credits33.get_width()
            Credits34 = VersionFont.render("Thank You!", aa, FontCol)
            Credits34Width = Credits34.get_width()
            Credits34Height = Credits34.get_height()

            realWidth, realHeight = pygame.display.get_window_size()
            VisualYdisplacement = realHeight
            IntroYDisplacement = (realHeight-TitleHeight)/2
            timer = 5
            tempFPS = FPS
            FullscreenX, FullscreenY = pyautogui.size()

            EndClock = 0
            while True:
                realWidth, realHeight = pygame.display.get_window_size()

                if realWidth < 1280:
                    Display = pygame.display.set_mode((1280, realHeight), RESIZABLE)
                if realHeight < 720:
                    Display = pygame.display.set_mode((realWidth, 720), RESIZABLE)

                yScaleFact = realHeight/720
                xScaleFact = realWidth/1280

                eFPS = clock.get_fps()
                aFPS += eFPS 
                Mx, My = pygame.mouse.get_pos() 
                run += 1
                iteration += 1
                if pygame.display.get_active() == False:
                    tempFPS = 15
                else:
                    tempFPS = FPS

                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                        if sound == True:
                            PlayClickSound(soundVOL)
                        return Fullscreen
                    elif event.type == pygame.KEYDOWN: 
                        if event.key == pygame.K_SPACE and devmode < 10: 
                            devmode += 1 
                        if event.key == pygame.K_q:
                            DataWindow = tk.Tk()
                            DataWindow.title("Player Information") 
                            DataWindow.configure(width = 500, height = 300) 
                            DataWindow.configure(bg="lightblue") 
                            VersionData = f"Pycraft: v{version}" 
                            CoordinatesData = f"Coordinates: x: {Mx} y: {My} z: 0.0 Facing: 0.0, 0.0, 0.0" 
                            FPSData = f"FPS: Actual: {eFPS} Max: {FPS}" 
                            VersionData = tk.Label(DataWindow, text=VersionData) 
                            CoordinatesData = tk.Label(DataWindow, text=CoordinatesData) 
                            FPSData = tk.Label(DataWindow, text=FPSData) 
                            VersionData.grid(row = 0, column = 0, columnspan = 2) 
                            CoordinatesData.grid(row = 1, column = 0, columnspan = 2)
                            FPSData.grid(row = 2, column = 0, columnspan = 2)
                            DataWindow.mainloop() 
                            DataWindow.quit()
                        if event.key == pygame.K_F11:
                            keydown = True
                            if keydown == True:
                                if Fullscreen == True:
                                    Fullscreen = False
                                    pygame.display.quit()
                                    pygame.init()
                                    Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                                    keydown = False
                                elif Fullscreen == False:
                                    Fullscreen = True
                                    Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF)
                                    keydown = False
                        if event.key == pygame.K_x: 
                            devmode = 1 
                            pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log")
                if devmode >= 5 and devmode <= 9: 
                    pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log | you are: {10-devmode} steps away from being a developer") 
                elif devmode == 10: 
                    pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log | Developer mode | V: 0, 0, 0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())}") 
                else:
                    pygame.display.set_caption(f"Pycraft: v{version}: Credits and Change-Log") 
                Display.fill(BackgroundCol)
                Display.blit(Credits1, ((realWidth-Credits1Width)/2, 0+VisualYdisplacement))
                Display.blit(Credits2, ((realWidth-Credits2Width)/2, 115+VisualYdisplacement))
                Display.blit(Credits3, ((realWidth-Credits3Width)/2, (115*2)+VisualYdisplacement))
                Display.blit(Credits4, ((realWidth-Credits4Width)/2, (115*3)+VisualYdisplacement))
                Display.blit(Credits5, ((realWidth-Credits5Width)/2, (115*3)+20+VisualYdisplacement))
                Display.blit(Credits6, ((realWidth-Credits6Width)/2, (115*3)+40+VisualYdisplacement))
                Display.blit(Credits7, ((realWidth-Credits7Width)/2, (115*3)+60+VisualYdisplacement))
                Display.blit(Credits8, ((realWidth-Credits8Width)/2, 540+VisualYdisplacement))
                Display.blit(Credits9, ((realWidth-Credits9Width)/2, 540+20+VisualYdisplacement))
                Display.blit(Credits10, ((realWidth-Credits10Width)/2, 540+40+VisualYdisplacement))
                Display.blit(Credits11, ((realWidth-Credits11Width)/2, 540+60+VisualYdisplacement))
                Display.blit(Credits12, ((realWidth-Credits12Width)/2, 540+80+VisualYdisplacement))
                Display.blit(Credits13, ((realWidth-Credits13Width)/2, 540+100+VisualYdisplacement))
                Display.blit(Credits14, ((realWidth-Credits14Width)/2, 540+120+VisualYdisplacement))
                Display.blit(Credits15, ((realWidth-Credits15Width)/2, 540+140+VisualYdisplacement))
                Display.blit(Credits16, ((realWidth-Credits16Width)/2, 540+160+VisualYdisplacement))
                Display.blit(Credits17, ((realWidth-Credits17Width)/2, 540+180+VisualYdisplacement))
                Display.blit(Credits18, ((realWidth-Credits18Width)/2, 540+200+VisualYdisplacement))
                Display.blit(Credits19, ((realWidth-Credits19Width)/2, 540+220+VisualYdisplacement))
                Display.blit(Credits20, ((realWidth-Credits20Width)/2, 540+240+VisualYdisplacement))
                Display.blit(Credits21, ((realWidth-Credits21Width)/2, 540+260+VisualYdisplacement))
                Display.blit(Credits22, ((realWidth-Credits22Width)/2, 915+VisualYdisplacement))
                Display.blit(Credits23, ((realWidth-Credits23Width)/2, 935+VisualYdisplacement))
                Display.blit(Credits24, ((realWidth-Credits24Width)/2, 1050+VisualYdisplacement))
                Display.blit(Credits25, ((realWidth-Credits25Width)/2, 1165+VisualYdisplacement))
                Display.blit(Credits26, ((realWidth-Credits26Width)/2, 1167+15+VisualYdisplacement))
                Display.blit(Credits27, ((realWidth-Credits27Width)/2, 1167+30+VisualYdisplacement))
                Display.blit(Credits28, ((realWidth-Credits28Width)/2, 1167+45+VisualYdisplacement))
                Display.blit(Credits29, ((realWidth-Credits29Width)/2, 1167+60+VisualYdisplacement))
                Display.blit(Credits30, ((realWidth-Credits30Width)/2, 1167+75+VisualYdisplacement))
                Display.blit(Credits31, ((realWidth-Credits31Width)/2, 1167+90+VisualYdisplacement))
                Display.blit(Credits32, ((realWidth-Credits32Width)/2, 1167+105+VisualYdisplacement))
                Display.blit(Credits33, ((realWidth-Credits33Width)/2, 1167+120+VisualYdisplacement))

                if timer >= 1:
                    Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))
                    timer -= 1/(aFPS/iteration)
                    VisualYdisplacement = realHeight
                else:
                    if IntroYDisplacement <= 0:
                        cover_Rect = pygame.Rect(0, 0, 1280, 90)
                        pygame.draw.rect(Display, (BackgroundCol), cover_Rect)
                        Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))
                        Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50))
                        if int(1402+VisualYdisplacement) <= int(realHeight/2):
                            Display.blit(Credits34, ((realWidth-Credits34Width)/2, (realHeight-Credits34Height)/2))
                            VisualYdisplacement -= 60/(aFPS/iteration)
                            if EndClock >= 5:
                                Home_Screen(Display, themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, musicVOL, camera_x, camera_y, camera_z, size, theme, lastRun, startUP, Fullscreen, SavedWidth, SavedHeight)
                            else:
                                EndClock += 1/(aFPS/iteration)
                        else:
                            Display.blit(Credits34, ((realWidth-Credits34Width)/2, 1402+VisualYdisplacement))
                            VisualYdisplacement -= 60/(aFPS/iteration)
                    else:
                        cover_Rect = pygame.Rect(0, 0, 1280, 90)
                        pygame.draw.rect(Display, (BackgroundCol), cover_Rect)
                        Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))
                        Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50+IntroYDisplacement))
                        IntroYDisplacement -= 90/(aFPS/iteration)
                        VisualYdisplacement = realHeight

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
                if devmode == 10: 
                    dev_Rect = pygame.Rect(1000, 0, 200, 200)
                    pygame.draw.rect(Display, (80, 80, 80), dev_Rect)
                    if run >= 10:
                        pygame.draw.lines(Display, (0, 255, 0), False, (data2))
                        pygame.draw.lines(Display, (255, 0, 0), False, (data1))
                        pygame.draw.lines(Display, (0, 0, 255), False, (data3))
                        pygame.draw.lines(Display, (255, 0, 255), False, (data4))
                        pygame.draw.line(Display, (255, 255, 255), (((run/5)+1000), 20), (((run/5)+1000), 200))
                    runFont = DataFont.render(f"{psutil.virtual_memory().percent} | {str(psutil.cpu_percent())} | {str(run)} | {str(rerun)} | {str(round(eFPS, 2))}", False, (255, 255, 255)) 
                    Display.blit(runFont, (1000, 0)) 
                pygame.display.flip() 
                clock.tick(tempFPS) 


        def CreateRose(FontCol, BackgroundCol, ShapeCol, Display, xScaleFact, yScaleFact):
            defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] 
            pygame.draw.polygon(Display, ShapeCol, defLargeOctagon, width=2)
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 

            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 

            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 

            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 

            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
            pygame.draw.line(Display, ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 

            pygame.draw.line(Display, ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)
            pygame.draw.line(Display, ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)

            pygame.draw.line(Display, ShapeCol, (575*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)


        def LoadQuickText():
            LoadingTextFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            LoadingText = ["Use W,A,S,D to move", "Use W to move forward", "Use S to move backward", "Use A to move left", "Use D to move right", "Access your inventory with E", "Access your map with R", "Use SPACE to jump", "Did you know there is a light mode?", "Did you know there is a dark mode?", "Check us out on GitHub", "Use ESC to remove camera movement", "Hold W to sprint", "Did you know you can change the sound volume in settings?", "Did you know you can change the music volume in settings?", "Did you know you can use L to lock the camera"]
            locat = random.randint(0, (len(LoadingText)-1))
            text = LoadingText[locat]
            return text


        def GenerateLoadDisplay(Display, LoadingFont, text, MessageText, BackgroundCol, ShapeCol, FontCol, aa, LoadingPercent, eventHandle, AccentCol, MainTitleFont, SecondaryFont, LoadingTextFont, line):
            Display.fill(BackgroundCol)

            realWidth, realHeight = pygame.display.get_window_size()
            yScaleFact = realHeight/720
            xScaleFact = realWidth/1280

            PycraftTitle = MainTitleFont.render("Pycraft", aa, FontCol)
            TitleWidth = PycraftTitle.get_width()
            Display.blit(PycraftTitle, ((realWidth-TitleWidth)/2, 0))

            LoadingTitle = SecondaryFont.render("Loading", aa, FontCol)
            Display.blit(LoadingTitle, (((realWidth-TitleWidth)/2)+55, 50))

            line.append((LoadingPercent, realHeight-100))
            pygame.draw.lines(Display, (ShapeCol), aa, [(100, realHeight-100), (realWidth-100, realHeight-100)], 3)
            pygame.draw.lines(Display, (AccentCol), aa, line)

            DisplayMessage = LoadingFont.render(MessageText, aa, FontCol)
            DisplayMessageWidth = DisplayMessage.get_width()
            Display.blit(DisplayMessage, ((realWidth-DisplayMessageWidth)/2, realHeight-120))

            TextFontRendered = LoadingTextFont.render(f"{text}", aa, FontCol)
            TextFontRenderedWidth = TextFontRendered.get_width()
            Display.blit(TextFontRendered, ((realWidth-TextFontRenderedWidth)/2, realHeight-100))

            pygame.display.flip()

            if eventHandle == True:
                pygame.event.get()


        def Home_Screen(Display, themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, musicVOL, camera_x, camera_y, camera_z, size, theme, lastRun, startUP, Fullscreen, SavedWidth, SavedHeight): 
            print(Fullscreen)
            try:
                FullscreenX, FullscreenY = pyautogui.size()
                if Fullscreen == False:
                    #Fullscreen = True
                    pygame.display.quit()
                    pygame.init()
                    Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                    keydown = False
                elif Fullscreen == True:
                    #Fullscreen = False
                    pygame.display.quit()
                    pygame.init()
                    Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF)
                    keydown = False
            except Exception as error:
                SavedWidth = 1280
                SavedHeight = 720
                pygame.display.quit()
                pygame.init()
                Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                keydown = False

            base_folder = os.path.dirname(__file__)

            if startUP == True:
                startUP = True
            elif startUP == False:
                startUP = Start(Display, FontCol, BackgroundCol, ShapeCol, startUP)
            else:
                startUP = Start(Display, FontCol, BackgroundCol, ShapeCol, startUP)

            Display.fill(BackgroundCol)
            pygame.display.flip()
            if devmode == 10 or devmode-10 == 0: 
                pygame.display.set_caption(f"Pycraft: v{version}: Home Screen | Developer Mode | V: 0, 0, 0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}") 
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Home Screen") 
            icon = pygame.image.load(os.path.join(base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
            pygame.display.set_icon(icon)
            Selector = pygame.image.load(os.path.join(base_folder, (f"Resources\\General_Resources\\selectorICON{theme}.jpg"))).convert()
            SelectorWidth = Selector.get_width()
            hover1 = False 
            hover2 = False 
            hover3 = False 
            hover4 = False 
            hover5 = False
            hover6 = False
            mousebuttondown = False 
            current_time = datetime.datetime.now()
            currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"
            
            MainTitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 60) 
            PycraftTitle = MainTitleFont.render("Pycraft", aa, FontCol)
            TitleWidth = PycraftTitle.get_width()
            realWidth, realHeight = pygame.display.get_window_size()
            Display.blit(PycraftTitle, ((realWidth-TitleWidth)/2, 0))
            pygame.display.update()

            SideFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 24) 
            VersionFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15) 
            ButtonFont1 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
            ButtonFont2 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
            ButtonFont3 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
            ButtonFont4 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
            ButtonFont5 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30)
            ButtonFont6 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30)
            DataFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15) 
            LoadingTextFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            SecondaryFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
            LoadingFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            data1 = [] 
            data2 = [] 
            data3 = [] 
            data4 = [] 
            run = 0
            rerun = 0 
            iteration = 1
            aFPS = FPS
            counter = 0
            oldTHEME = theme
            RErun = True
            tempFPS = FPS
            Fullscreen = False
            BackgroundLoadingMusicThread = False
            pygame.mixer.quit()
            pygame.mixer.init()
            while True:
                if pygame.mixer.Channel(3).get_busy() == 1:
                    pygame.mixer.Channel(3).stop()
                if str(Display) == "<Surface(Dead Display)>":
                    try:
                        FullscreenX, FullscreenY = pyautogui.size()
                        if Fullscreen == False:
                            #Fullscreen = True
                            pygame.display.quit()
                            pygame.init()
                            Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                            keydown = False
                        elif Fullscreen == True:
                            #Fullscreen = False
                            pygame.display.quit()
                            pygame.init()
                            Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF)
                            keydown = False
                    except Exception as error:
                        SavedWidth = 1280
                        SavedHeight = 720
                        pygame.display.quit()
                        pygame.init()
                        Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                        keydown = False

                realWidth, realHeight = pygame.display.get_window_size()
                if not (realWidth == FullscreenX and realHeight == FullscreenY):
                    SavedWidth, SavedHeight = pygame.display.get_window_size()

                if SavedWidth == FullscreenX:
                    SavedWidth = 1280
                if SavedHeight == FullscreenY:
                    SavedHeight = 720

                if realWidth < 1280:
                    Display = pygame.display.set_mode((1280, realHeight), RESIZABLE)
                if realHeight < 720:
                    Display = pygame.display.set_mode((realWidth, 720), RESIZABLE)

                yScaleFact = realHeight/720
                xScaleFact = realWidth/1280
                if not oldTHEME == theme:
                    Selector = pygame.image.load(os.path.join(base_folder, (f"Resources\\General_Resources\\selectorICON{theme}.jpg"))).convert()
                    SelectorWidth = Selector.get_width()
                    oldTHEME = theme
                if pygame.display.get_active() == True:
                    pygame.mixer.init()
                    tempFPS = FPS
                    if pygame.mixer.get_busy() == 0 and BackgroundLoadingMusicThread == False:
                        if music == True:
                            PlayInvSound(musicVOL)
                else:
                    BackgroundLoadingMusicThread = False
                    pygame.mixer.quit()
                    tempFPS = 15
                    
                counter += 1
                Display.fill(BackgroundCol)
                eFPS = clock.get_fps()
                aFPS += eFPS 
                iteration += 1
                Mx, My = pygame.mouse.get_pos() 
                run += 1 
                PycraftTitle = MainTitleFont.render("Pycraft", aa, FontCol)
                TitleWidth = PycraftTitle.get_width()

                Name = SideFont.render("By Tom Jebbo", aa, FontCol)
                NameHeight = Name.get_height()

                Version = VersionFont.render(f"Version: {version}", aa, FontCol) 
                VersionWidth = Version.get_width()
                VersionHeight = Version.get_height()

                Play = ButtonFont1.render("Play", aa, FontCol)
                PlayWidth = Play.get_width()

                SettingsText = ButtonFont2.render("Settings", aa, FontCol)
                SettingsWidth = SettingsText.get_width()

                Character_CustomisationsText = ButtonFont3.render("Character Customisations", aa, FontCol)
                CharCustWidth = Character_CustomisationsText.get_width()

                AchievementsText = ButtonFont4.render("Achievements", aa, FontCol)
                AchievementsWidth = AchievementsText.get_width()

                Credits_and_Change_Log_Text = ButtonFont5.render("Credits", aa, FontCol)
                CreditsWidth = Credits_and_Change_Log_Text.get_width()

                BenchmarkText = ButtonFont6.render("Benchmark", aa, FontCol)
                BenchmarkWidth = BenchmarkText.get_width()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        try:
                            with open(os.path.join(base_folder, ("Data_Files\\SaveGameConfig.txt")), mode ="w") as SaveGameConfig:
                                SaveGameConfigDict = {"theme":theme, "FPS":FPS, "eFPS":eFPS, "aFPS":(aFPS/counter), "FOV":FOV, "cameraANGspeed":cameraANGspeed, "aa":aa, "RenderFOG":RenderFOG, "FanSky":FanSky, "FanPart":FanPart, "sound":sound, "soundVOL":soundVOL, "music":music, "musicVOL":musicVOL, "X":camera_x, "Y":camera_y, "Z":camera_z, "lastRun":currentDate, 'startup': startUP, 'crash': False, 'DisplayWidth':SavedWidth, 'DisplayHeight':SavedHeight, 'WindowStatus':Fullscreen}
                                SaveGameConfig.write("save = "+str(SaveGameConfigDict))
                        except Exception as error:
                            errorIMG = pygame.image.load(os.path.join(base_folder, ("Resources\\General_Resources\\Saving_ERROR.jpg"))).convert()
                            Display.blit(errorIMG, (0, -5))
                            pygame.display.update()
                            pygame.time.wait(1000)
                        pygame.quit()
                        sys.exit("Thanks for playing")
                        quit()
                    if event.type == pygame.KEYDOWN: 
                        if event.key == pygame.K_SPACE and devmode < 10: 
                            devmode += 1 
                        if event.key == pygame.K_q:
                            DataWindow = tk.Tk()
                            DataWindow.title("Player Information") 
                            DataWindow.configure(width = 500, height = 300) 
                            DataWindow.configure(bg="lightblue") 
                            VersionData = f"Pycraft: v{version}" 
                            CoordinatesData = f"Coordinates: x: {Mx} y: {My} z: 0.0 Facing: 0.0, 0.0, 0.0" 
                            FPSData = f"FPS: Actual: {eFPS} Max: {FPS}" 
                            VersionData = tk.Label(DataWindow, text=VersionData) 
                            CoordinatesData = tk.Label(DataWindow, text=CoordinatesData) 
                            FPSData = tk.Label(DataWindow, text=FPSData) 
                            VersionData.grid(row = 0, column = 0, columnspan = 2) 
                            CoordinatesData.grid(row = 1, column = 0, columnspan = 2)
                            FPSData.grid(row = 2, column = 0, columnspan = 2)
                            DataWindow.mainloop() 
                            DataWindow.quit()
                        if event.key == pygame.K_F11:
                            keydown = True
                            if keydown == True:
                                if Fullscreen == True:
                                    Fullscreen = False
                                    pygame.display.quit()
                                    pygame.init()
                                    Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                                    keydown = False
                                elif Fullscreen == False:
                                    Fullscreen = True
                                    SavedWidth, SavedHeight = pygame.display.get_window_size()
                                    Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF)
                                    keydown = False
                        if event.key == pygame.K_x: 
                            devmode = 1 
                            pygame.display.set_caption(f"Pycraft: v{version}: Home") 
                    if event.type == pygame.MOUSEBUTTONDOWN: 
                        mousebuttondown = True 
                    if event.type == pygame.MOUSEBUTTONUP: 
                        mousebuttondown = False
                if devmode >= 5 and devmode <= 9: 
                    pygame.display.set_caption(f"Pycraft: v{version}: Home Screen | you are: {10-devmode} steps away from being a developer") 
                elif devmode == 10: 
                    pygame.display.set_caption(f"Pycraft: v{version}: Home Screen | Developer mode | V: 0, 0, 0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}") 
                else:
                    pygame.display.set_caption(f"Pycraft: v{version}: Home Screen") 
                
                ButtonFont1.set_underline(hover1) 
                ButtonFont2.set_underline(hover2) 
                ButtonFont3.set_underline(hover3)
                ButtonFont4.set_underline(hover4)
                ButtonFont5.set_underline(hover5)
                ButtonFont6.set_underline(hover6)
                
                if My >= 202*yScaleFact and My <= 247*yScaleFact and Mx >= (realWidth-(PlayWidth+SelectorWidth))-2:
                    hover1 = True
                    if mousebuttondown == True:
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False

                        Display.fill(BackgroundCol)

                        pygame.mixer.Channel(2).fadeout(2000)

                        PycraftTitle = MainTitleFont.render("Pycraft", aa, FontCol)
                        TitleWidth = PycraftTitle.get_width()
                        Display.blit(PycraftTitle, ((realWidth-TitleWidth)/2, 0))

                        LoadingTitle = SecondaryFont.render("Loading", aa, FontCol)
                        Display.blit(LoadingTitle, (((realWidth-TitleWidth)/2)+55, 50))

                        pygame.draw.lines(Display, (ShapeCol), aa, [(100, realHeight-100), (realWidth-100, realHeight-100)], 3)

                        DisplayMessage = LoadingFont.render("Initiating...", aa, FontCol)
                        DisplayMessageWidth = DisplayMessage.get_width()
                        Display.blit(DisplayMessage, ((realWidth-DisplayMessageWidth)/2, realHeight-120))

                        TextFontRendered = LoadingTextFont.render(f"Loading...", aa, FontCol)
                        TextFontRenderedWidth = TextFontRendered.get_width()
                        Display.blit(TextFontRendered, ((realWidth-TextFontRenderedWidth)/2, realHeight-100))

                        pygame.display.flip()

                        if devmode == 10 or devmode-10 == 0:
                            pygame.display.set_caption(f"Pycraft: v{version}: Playing | Developer mode | V: 0, 0, 0 | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
                        else:
                            pygame.display.set_caption(f"Pycraft: v{version}: Playing")
                        Load3D = True
                        Map = 0
                        min_v = 0
                        max_v = 0
                        Map_box = 0
                        Map_size = 0
                        Map_scale = 0
                        Map_trans = 0
                        max_Map_size = 0
                        map_vertices = 0
                        text = LoadQuickText()
                        TextFontRendered = LoadingTextFont.render(f"{text}", aa, FontCol)
                        Display.blit(TextFontRendered, (600, 160))
                        Fullscreen = main(FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, Display, G3Dscale, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D, map_vertices, realWidth, realHeight, Fullscreen, SavedWidth, SavedHeight, AccentCol) 
                        if sound == True:
                            PlayClickSound(soundVOL)
                        continue
                else:
                    hover1 = False
                
                if My >= 252*yScaleFact and My <= 297*yScaleFact and Mx >= (realWidth-(SettingsWidth+SelectorWidth))-2: 
                    hover2 = True
                    if mousebuttondown == True:
                        Display.fill(BackgroundCol)
                        pygame.display.flip()
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                        themeArray, FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, FanSky, FanPart, sound, soundVOL, music, musicVOL, theme, Fullscreen = settings(Display, themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, FanSky, FanPart, sound, soundVOL, music, musicVOL, theme, Fullscreen, SavedWidth, SavedHeight)
                else:
                    hover2 = False

                if My >= 302*yScaleFact and My <= 347*yScaleFact and Mx >= (realWidth-(CharCustWidth+SelectorWidth)-2):
                    hover3 = True
                    if mousebuttondown == True:
                        Display.fill(BackgroundCol)
                        pygame.display.flip()
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                        Fullscreen = Character_Customiser(Display, FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, aa, FPS, theme, AccentCol, startUP, Fullscreen, SavedWidth, SavedHeight)
                else:
                    hover3 = False

                if My >= 402*yScaleFact and My <= 447*yScaleFact and Mx >= (realWidth-(AchievementsWidth+SelectorWidth)-2):
                    hover4 = True
                    if mousebuttondown == True:
                        Display.fill(BackgroundCol)
                        pygame.display.flip()
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                        Fullscreen = Achievements(Display, FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, aa, FPS, theme, AccentCol, Fullscreen, SavedWidth, SavedHeight)
                else:
                    hover4 = False

                if My >= 352*yScaleFact and My <= 397*yScaleFact and Mx >= (realWidth-(CreditsWidth+SelectorWidth)-2):
                    hover5 = True
                    if mousebuttondown == True:
                        Display.fill(BackgroundCol)
                        pygame.display.flip()
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                        Fullscreen = Credits(Display, FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, aa, FPS, theme, AccentCol, Fullscreen, SavedWidth, SavedHeight)
                else:
                    hover5 = False

                if My >= 452*yScaleFact and My <= 497*yScaleFact and Mx >= (realWidth-(BenchmarkWidth+SelectorWidth)-2):
                    hover6 = True
                    if mousebuttondown == True:
                        Display.fill(BackgroundCol)
                        pygame.display.flip()
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                        Fullscreen = Benchmark(Display, FontCol, BackgroundCol, ShapeCol, numOFerrors, devmode, aa, FPS, theme, AccentCol, Fullscreen, SavedWidth, SavedHeight)
                else:
                    hover6 = False

                Display.fill(BackgroundCol)

                Display.blit(PycraftTitle, ((realWidth-TitleWidth)/2, 0))
                Display.blit(Name, (0, (realHeight-NameHeight)))

                Display.blit(Version, ((realWidth-VersionWidth)-2, (realHeight-VersionHeight)))

                Display.blit(Play, ((realWidth-PlayWidth)-2, 200*yScaleFact))

                Display.blit(SettingsText, ((realWidth-SettingsWidth)-2, 250*yScaleFact))

                Display.blit(Character_CustomisationsText, ((realWidth-CharCustWidth)-2, 300*yScaleFact))

                Display.blit(Credits_and_Change_Log_Text, ((realWidth-CreditsWidth)-2, 350*yScaleFact))

                Display.blit(AchievementsText, ((realWidth-AchievementsWidth)-2, 400*yScaleFact))

                Display.blit(BenchmarkText, ((realWidth-BenchmarkWidth)-2, 450*yScaleFact))

                if hover1 == True:
                    Display.blit(Selector, (realWidth-(PlayWidth+SelectorWidth)-2, 200*yScaleFact))
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif hover2 == True:
                    Display.blit(Selector, (realWidth-(SettingsWidth+SelectorWidth)-2, 250*yScaleFact))
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif hover3 == True:
                    Display.blit(Selector, (realWidth-(CharCustWidth+SelectorWidth)-2, 300*yScaleFact))
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif hover5 == True:
                    Display.blit(Selector, (realWidth-(CreditsWidth+SelectorWidth)-2, 350*yScaleFact))
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif hover4 == True:
                    Display.blit(Selector, (realWidth-(AchievementsWidth+SelectorWidth)-2, 400*yScaleFact))
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif hover6 == True:
                    Display.blit(Selector, (realWidth-(BenchmarkWidth+SelectorWidth)-2, 450*yScaleFact))
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    
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
                        with open(os.path.join(base_folder, ("Data_Files\\errorREPORT.txt")), "w") as errorFILE:
                            errorFILE.write(str(error)+"\n")
                else:
                    data1.append([((run/5)+1000), ((450-(eFPS/4))-250)])
                    data2.append([((run/5)+1000), ((450-((psutil.cpu_percent())))-250)])
                    data3.append([((run/5)+1000), ((200-psutil.virtual_memory().percent))+25])
                    data4.append([((run/5)+1000), ((450-((aFPS/iteration))/4)-250)])
                if devmode == 10: 
                    dev_Rect = pygame.Rect(1000, 0, 200, 200)
                    pygame.draw.rect(Display, (80, 80, 80), dev_Rect)
                    if run >= 10:
                        pygame.draw.lines(Display, (0, 255, 0), False, (data2))
                        pygame.draw.lines(Display, (255, 0, 0), False, (data1))
                        pygame.draw.lines(Display, (0, 0, 255), False, (data3))
                        pygame.draw.lines(Display, (255, 0, 255), False, (data4))
                        pygame.draw.line(Display, (255, 255, 255), (((run/5)+1000), 20), (((run/5)+1000), 200))
                    runFont = DataFont.render(f"{psutil.virtual_memory().percent} | {str(psutil.cpu_percent())} | {str(run)} | {str(rerun)} | {str(round(eFPS, 2))}", False, (255, 255, 255)) 
                    Display.blit(runFont, (1000, 0)) 
                CreateRose(FontCol, BackgroundCol, ShapeCol, Display, xScaleFact, yScaleFact)
                pygame.display.flip()
                clock.tick(tempFPS)


        def LoadMapTexture(aa):
            base_folder = os.path.dirname(__file__)
            if aa == True:
                file = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\Map\\GrassTexture.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512, 512), Image.ANTIALIAS) 
                texture = file.tobytes() 
            if aa == False:
                file = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\Map\\GrassTexture.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512, 512))
                texture = file.tobytes() 
            glGenTextures(7, texture) 
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, 7) 
            glPixelStorei(GL_UNPACK_ALIGNMENT, 1) 
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT) 
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT) 
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_R, GL_MIRRORED_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) 
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            color = [0.0, 1.0, 0.0]
            glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, color)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture) 
            glGenerateMipmap(GL_TEXTURE_2D)


        def LoadSkyBox(aa):
            base_folder = os.path.dirname(__file__)
            if aa == True:
                im1 = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512, 512), Image.ANTIALIAS) 
                texture1 = im1.tobytes() 
                im2 = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg"))).rotate(180).resize((512, 512)) 
                texture2 = im2.tobytes() 
                im3 = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512, 512), Image.ANTIALIAS)
                texture3 = im3.tobytes()
                im4 = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512, 512), Image.ANTIALIAS)
                texture5 = im4.tobytes() 
                im5 = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg"))).rotate(180).resize((512, 512), Image.ANTIALIAS)
                texture4 = im5.tobytes() 
                im6 = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg"))).resize((512, 512), Image.ANTIALIAS)
                texture6 = im6.tobytes() 
            if aa == False:
                im1 = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512, 512)) 
                texture1 = im1.tobytes() 
                im2 = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg"))).rotate(180).resize((512, 512)) 
                texture2 = im2.tobytes() 
                im3 = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512, 512))
                texture3 = im3.tobytes()
                im4 = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg"))).rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512, 512))
                texture5 = im4.tobytes() 
                im5 = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg"))).rotate(180).resize((512, 512))
                texture4 = im5.tobytes() 
                im6 = Image.open(os.path.join(base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg"))).resize((512, 512))
                texture6 = im6.tobytes() 
            
            glGenTextures(1) 
            glBindTexture(GL_TEXTURE_2D, 1) 
            glPixelStorei(GL_UNPACK_ALIGNMENT, 1) 
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP) 
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP) 
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) 
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture1) 
            
            glGenTextures(2)
            glBindTexture(GL_TEXTURE_2D, 2)
            glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture2)
            
            glGenTextures(3)
            glBindTexture(GL_TEXTURE_2D, 3)
            glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture3)
            
            glGenTextures(4)
            glBindTexture(GL_TEXTURE_2D, 4)
            glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture4)
            
            glGenTextures(5)
            glBindTexture(GL_TEXTURE_2D, 5)
            glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 512, 512, 0, GL_RGB, GL_UNSIGNED_BYTE, texture5)
            
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
            glEnable(GL_TEXTURE_2D)
            glColor3f(1, 1, 1) 
            
            glBindTexture(GL_TEXTURE_2D, 1) 
            glBegin(GL_QUADS) 
            glTexCoord2f(0, 0) 
            glVertex3f(-10.0, -10.0-50000, -10.0) 
            glTexCoord2f(1, 0) 
            glVertex3f(10.0, -10.0-50000, -10.0)
            glTexCoord2f(1, 1)
            glVertex3f(10.0, 10.0-50000, -10.0)
            glTexCoord2f(0, 1)
            glVertex3f(-10.0, 10.0-50000, -10.0)
            glEnd() 

            glBindTexture(GL_TEXTURE_2D, 0) 
            
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


        def Inventory(FontCol, BackgroundCol, ShapeCol, aa, version, FPS, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D, map_vertices, realWidth, realHeight, Fullscreen, SavedWidth, SavedHeight):
            FullscreenX, FullscreenY = pyautogui.size()
            base_folder = os.path.dirname(__file__)
            if Fullscreen == False:
                pygame.display.quit()
                pygame.init()
                Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE|SRCALPHA)
                keydown = False
            elif Fullscreen == True:
                pygame.display.quit()
                pygame.init()
                Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF|SRCALPHA)
                keydown = False

            Display.fill(BackgroundCol)
            pygame.display.update()

            MainInventoryFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 60) 
            PycraftTitle = MainInventoryFont.render("Pycraft", aa, FontCol)
            TitleWidth = PycraftTitle.get_width()

            icon = pygame.image.load(os.path.join(base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
            AlphaSurface = pygame.Surface((realWidth, realHeight), HWSURFACE|SRCALPHA)
            pygame.display.set_icon(icon)
            AlphaSurface.set_alpha(204) 
            AlphaSurface.fill(BackgroundCol)

            Selector = pygame.image.load(os.path.join(base_folder, (f"Resources\\General_Resources\\selectorICON{theme}.jpg"))).convert()
            SelectorWidth = Selector.get_width()

            hover1 = False 
            hover2 = False 
            hover3 = False 
            hover4 = False 
            hover5 = False 
            hover6 = False 
            hover7 = False
            hover8 = False
            mousebuttondown = False

            ButtonFont1 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
            WeaponsText = ButtonFont1.render("Weapons", aa, FontCol)
            WeaponsTextWidth = WeaponsText.get_width()
            WeaponsTextHeight = WeaponsText.get_height()

            ButtonFont2 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
            RangedWeaponsText = ButtonFont2.render("Ranged Weapons", aa, FontCol)
            RangedWeaponsTextWidth = RangedWeaponsText.get_width()
            RangedWeaponsTextHeight= RangedWeaponsText.get_height()

            ButtonFont3 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
            ShieldsText = ButtonFont3.render("Shields", aa, FontCol)
            ShieldsTextWidth = ShieldsText.get_width()
            ShieldsTextHeight = ShieldsText.get_height()

            ButtonFont4 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
            ArmourText = ButtonFont4.render("Armour", aa, FontCol)
            ArmourTextWidth = ArmourText.get_width()
            ArmourTextHeight = ArmourText.get_height()

            ButtonFont5 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
            FoodText = ButtonFont5.render("Food", aa, FontCol)
            FoodTextWidth = FoodText.get_width()
            FoodTextHeight = FoodText.get_height()

            ButtonFont6 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
            ItemsText = ButtonFont6.render("Items", aa, FontCol)
            ItemsTextWidth = ItemsText.get_width()
            ItemsTextHeight = ItemsText.get_height()

            ButtonFont7 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
            SpecialItemsText = ButtonFont7.render("Special Items", aa, FontCol)
            SpecialItemsTextWidth = SpecialItemsText.get_width()
            SpecialItemsTextHeight = SpecialItemsText.get_height()

            ButtonFont8 = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
            OptionsText = ButtonFont7.render("Options", aa, FontCol)
            OptionsTextWidth = OptionsText.get_width()
            OptionsTextHeight = OptionsText.get_height()

            pygame.display.set_caption(f"Pycraft: v{version}: Playing | Inventory")
            storage = Map
            FullscreenX, FullscreenY = pyautogui.size()

            while True:
                realWidth, realHeight = pygame.display.get_window_size()

                if realWidth < 1280:
                    Display = pygame.display.set_mode((1280, realHeight), RESIZABLE)
                if realHeight < 720:
                    Display = pygame.display.set_mode((realWidth, 720), RESIZABLE)

                yScaleFact = realHeight/720
                xScaleFact = realWidth/1280

                Mx, My = pygame.mouse.get_pos() 
                Display.fill(BackgroundCol)

                if aa == True:
                    pilImage = Image.open(os.path.join(base_folder, ("Resources\\General_Resources\\PauseIMG.png"))).resize((realWidth, realHeight), Image.ANTIALIAS)
                else:
                    pilImage = Image.open(os.path.join(base_folder, ("Resources\\General_Resources\\PauseIMG.png"))).resize((realWidth, realHeight))
                
                PauseImg = pilImageToSurface(pilImage)
                Display.blit(PauseImg, (0, 0))
                Display.blit(AlphaSurface, (0, 0))

                Display.blit(PycraftTitle, ((realWidth-TitleWidth)/2, 0))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (event.type == pygame.KEYDOWN and event.key == pygame.K_e):
                        Load3D = False
                        if sound == True:
                            PlayClickSound(soundVOL)
                        return Fullscreen
                    if event.type == pygame.VIDEORESIZE:
                        realWidth, realHeight = pygame.display.get_window_size()
                        AlphaSurface = pygame.Surface((realWidth, realHeight), HWSURFACE|SRCALPHA)
                        AlphaSurface.set_alpha(204)
                        AlphaSurface.fill(BackgroundCol)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mousebuttondown = True 
                    if event.type == pygame.MOUSEBUTTONUP:
                        mousebuttondown = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F11:
                            keydown = True
                            if keydown == True:
                                if Fullscreen == True:
                                    Fullscreen = False
                                    pygame.display.quit()
                                    pygame.init()
                                    Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                                    AlphaSurface = pygame.Surface((realWidth, realHeight), HWSURFACE|SRCALPHA)
                                    AlphaSurface.set_alpha(204) 
                                    AlphaSurface.fill(BackgroundCol) 
                                    keydown = False
                                elif Fullscreen == False:
                                    Fullscreen = True
                                    Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF)
                                    AlphaSurface = pygame.Surface((FullscreenX, FullscreenY), HWSURFACE|SRCALPHA|FULLSCREEN|HWSURFACE|DOUBLEBUF) 
                                    AlphaSurface.set_alpha(204) 
                                    AlphaSurface.fill(BackgroundCol) 
                                    keydown = False
                
                if My >= 202*yScaleFact and My <= 247*yScaleFact and Mx >= 1155:
                    hover1 = True
                    if mousebuttondown == True:
                        Display.fill(BackgroundCol)
                        pygame.display.flip() 
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                else: 
                    hover1 = False 

                if My >= 252*yScaleFact and My <= 297*yScaleFact and Mx >= 1105: 
                    hover2 = True
                    if mousebuttondown == True:
                        Display.fill(BackgroundCol)
                        pygame.display.flip()
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                else:
                    hover2 = False

                if My >= 302*yScaleFact and My <= 347*yScaleFact and Mx >= 865:
                    hover3 = True
                    if mousebuttondown == True:
                        Display.fill(BackgroundCol)
                        pygame.display.flip()
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                else:
                    hover3 = False

                if My >= 402*yScaleFact and My <= 447*yScaleFact and Mx >= 1035:
                    hover4 = True
                    if mousebuttondown == True:
                        Display.fill(BackgroundCol)
                        pygame.display.flip()
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                else:
                    hover4 = False

                if My >= 352*yScaleFact and My <= 397*yScaleFact and Mx >= 880:
                    hover5 = True
                    if mousebuttondown == True:
                        Display.fill(BackgroundCol)
                        pygame.display.flip()
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                else:
                    hover5 = False

                if My >= 502*yScaleFact and My <= 547*yScaleFact and Mx >= 1095:
                    hover6 = True
                    if mousebuttondown == True:
                        Display.fill(BackgroundCol)
                        pygame.display.flip()
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                else:
                    hover6 = False

                if My >= 452*yScaleFact and My <= 497*yScaleFact and Mx >= 1095:
                    hover7 = True
                    if mousebuttondown == True:
                        Display.fill(BackgroundCol)
                        pygame.display.flip()
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                else:
                    hover7 = False

                if My >= 552*yScaleFact and My <= 597*yScaleFact and Mx >= 1095:
                    hover8 = True
                    if mousebuttondown == True:
                        Display.fill(BackgroundCol)
                        pygame.display.flip()
                        if sound == True:
                            PlayClickSound(soundVOL)
                        mousebuttondown = False
                else:
                    hover8 = False
                
                ButtonFont1.set_underline(hover1) 
                ButtonFont2.set_underline(hover2) 
                ButtonFont3.set_underline(hover3)
                ButtonFont4.set_underline(hover4)
                ButtonFont5.set_underline(hover5)
                ButtonFont6.set_underline(hover6)
                ButtonFont7.set_underline(hover7)
                ButtonFont8.set_underline(hover8)
                AlphaSurface.fill(BackgroundCol) 
                    
                Display.blit(WeaponsText, ((realWidth-WeaponsTextWidth)-2, 200*yScaleFact)) # ???

                if hover1 == True: 
                    AlphaSurface.blit(Selector, (realWidth-(WeaponsTextWidth+SelectorWidth)-2, 200*yScaleFact))
                    
                Display.blit(RangedWeaponsText, ((realWidth-RangedWeaponsTextWidth)-2, 250*yScaleFact))
                if hover2 == True: 
                    AlphaSurface.blit(Selector, (realWidth-(RangedWeaponsTextWidth+SelectorWidth)-2, 250*yScaleFact))
                    
                Display.blit(ShieldsText, ((realWidth-ShieldsTextWidth)-2, 300*yScaleFact))
                if hover3 == True: 
                    AlphaSurface.blit(Selector, (realWidth-(ShieldsTextWidth+SelectorWidth)-2, 300*yScaleFact))
                    
                Display.blit(ArmourText, ((realWidth-ArmourTextWidth)-2, 350*yScaleFact))
                if hover4 == True: 
                    AlphaSurface.blit(Selector, (realWidth-(FoodTextWidth+SelectorWidth)-2, 400*yScaleFact))
                    
                Display.blit(FoodText, ((realWidth-FoodTextWidth)-2, 400*yScaleFact))
                if hover5 == True: 
                    AlphaSurface.blit(Selector, (realWidth-(ArmourTextWidth+SelectorWidth)-2, 350*yScaleFact))
                    
                Display.blit(ItemsText, ((realWidth-ItemsTextWidth)-2, 450*yScaleFact))
                if hover6 == True: 
                    AlphaSurface.blit(Selector, (realWidth-(SpecialItemsTextWidth+SelectorWidth)-2, 500*yScaleFact))
                    
                Display.blit(SpecialItemsText, ((realWidth-SpecialItemsTextWidth)-2, 500*yScaleFact))
                if hover7 == True: 
                    AlphaSurface.blit(Selector, (realWidth-(ItemsTextWidth+SelectorWidth)-2, 450*yScaleFact))

                Display.blit(OptionsText, ((realWidth-OptionsTextWidth)-2, 550*yScaleFact))
                if hover8 == True:
                    AlphaSurface.blit(Selector, (realWidth-(OptionsTextWidth+SelectorWidth)-2, 550*yScaleFact))

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


        def MapGUI(FontCol, BackgroundCol, ShapeCol, aa, version, FPS, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D, map_vertices, realWidth, realHeight, Fullscreen, SavedWidth, SavedHeight):
            FullscreenX, FullscreenY = pyautogui.size()
            base_folder = os.path.dirname(__file__)
            if Fullscreen == False:
                pygame.display.quit()
                pygame.init()
                Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                keydown = False
            elif Fullscreen == True:
                realWidth, realHeight = pygame.display.get_window_size()
                Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF)
                keydown = False
            Display.fill(BackgroundCol)
            pygame.display.update()
            icon = pygame.image.load(os.path.join(base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
            pygame.display.set_icon(icon)
            MapPIL = Image.open(os.path.join(base_folder, ("Resources\\Map_Resources\\Full_Map.png")))
            Map0 = pygame.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)
            MapIcon = pygame.image.load(os.path.join(base_folder, ("Resources\\Map_Resources\\Marker.jpg"))).convert()
            zoom = 0
            pygame.display.set_caption(f"Pycraft: v{version}: Playing | Map")
            MouseUnlock = True
            X,Y = 0, 0
            key = ""
            FullscreenX, FullscreenY = pyautogui.size()
            while True:
                realWidth, realHeight = pygame.display.get_window_size()
                
                if realWidth < 1280:
                    Display = pygame.display.set_mode((1280, realHeight), RESIZABLE)
                if realHeight < 720:
                    Display = pygame.display.set_mode((realWidth, 720), RESIZABLE)
                
                Display.fill(BackgroundCol)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                        Load3D = False
                        if sound == True:
                            PlayClickSound(soundVOL)
                        return Fullscreen
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
                        if event.key == pygame.K_F11:
                            keydown = True
                            if keydown == True:
                                if Fullscreen == True:
                                    Fullscreen = False
                                    pygame.display.quit()
                                    pygame.init()
                                    Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                                    keydown = False
                                elif Fullscreen == False:
                                    Fullscreen = True
                                    realWidth, realHeight = pygame.display.get_window_size()
                                    Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF)
                                    keydown = False
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
                    MapPIL = Image.open(os.path.join(base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((realWidth, realHeight), Image.ANTIALIAS)
                    Map0 = pygame.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)
                    Display.blit(Map0, (0, 0))
                    Display.blit(MapIcon, GetMapPos(camera_x, camera_z))
                    x, y = 0, 0
                elif zoom == 1:
                    MapPIL = Image.open(os.path.join(base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((int(realWidth*1.75), int(realHeight*1.75)), Image.ANTIALIAS) 
                    Map0 = pygame.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)
                    Display.blit(Map0, (X,Y))
                    Display.blit(MapIcon, GetMapPos(camera_x, camera_z))
                elif zoom == 2:
                    MapPIL = Image.open(os.path.join(base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((int(realWidth*2), int(realHeight*2)), Image.ANTIALIAS) 
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


        def LoadingMapGraphics(vertex, Map_box, counterFORvertex):
            counterFORvertex += 1
            min_v = [min(Map_box[0][i], vertex[i]) for i in range(3)]
            max_v = [max(Map_box[1][i], vertex[i]) for i in range(3)]
            Map_box = (min_v, max_v)
            return min_v, max_v, Map_box, counterFORvertex


        def main(FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, Display, G3Dscale, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D, map_vertices, realWidth, realHeight, Fullscreen, SavedWidth, SavedHeight, AccentCol):
            if Fullscreen == False:
                pygame.display.quit()
                pygame.init()
                Display = pygame.display.set_mode((SavedWidth, SavedHeight), RESIZABLE)
                keydown = False
            elif Fullscreen == True:
                realWidth, realHeight = pygame.display.get_window_size()
                Display = pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF)
                keydown = False
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT)
            base_folder = os.path.dirname(__file__)
            realWidth, realHeight = pygame.display.get_window_size()
            LineScaleFact = realWidth/1280
            LoadingPercent = 0
            line = []
            LoadingPercent += 100+((75/7)*LineScaleFact)        
            MainTitleFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 60)
            SecondaryFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
            LoadingTextFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            LoadingFont = pygame.font.Font(os.path.join(base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
            line.append((LoadingPercent, realHeight-100))
            LoadingPercent += 100+((75/7)*LineScaleFact)
            aFPS = 0
            iteration = 1
            text = LoadQuickText()
            line.append((LoadingPercent, realHeight-100))
            pygame.draw.lines(Display, (30, 30, 30), aa, [(95, 620), (1200, 620)], 3) # FatPyiso
            pygame.draw.lines(Display, (153, 153, 153), aa, line)
            Init = LoadingFont.render("Initiating", aa, FontCol)
            TextFontRendered = LoadingTextFont.render(f"{text}", aa, FontCol)
            Display.blit(TextFontRendered, (600, 160))
            Display.blit(Init, (100, 640))
            pygame.display.flip()
            Jump = False
            JumpID = 0 
            CubeNum = 10 
            FOV = 70 
            MouseUnlock = False 
            max_distance = 0 
            z = 0 
            run = 0 
            y = -10 
            z = 1 
            x = 0 
            cube_dict = {}
            repeater = True
            camera_x = 0
            camera_y = 0
            camera_z = 0

            LoadingPercent += 100+((75/7)*LineScaleFact)
            GenerateLoadDisplay(Display, LoadingFont, text, "Loading", BackgroundCol, ShapeCol, FontCol, aa, LoadingPercent, True, AccentCol, MainTitleFont, SecondaryFont, LoadingTextFont, line)

            if devmode == 10 or devmode-10 == 0:
                pygame.display.set_caption(f"Pycraft: v{version}: Playing | Developer mode | V: 0, 0, 0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Playing")
            MouseUnlock = True
            Sun_pos_x, Sun_pos_y, Sun_pos_z = 0, 10, -20
            LoadingPercent += 100+((75/7)*LineScaleFact)
            GenerateLoadDisplay(Display, LoadingFont, text, "Loaded Image Resources", BackgroundCol, ShapeCol, FontCol, aa, LoadingPercent, True, AccentCol, MainTitleFont, SecondaryFont, LoadingTextFont, line)

            counter = 0
            rotationvectX, rotationvectY = 0, 0

            LoadingPercent += 100+((75/7)*LineScaleFact)
            GenerateLoadDisplay(Display, LoadingFont, text, "Beginning Resource Loading | 0% complete", BackgroundCol, ShapeCol, FontCol, aa, LoadingPercent, True, AccentCol, MainTitleFont, SecondaryFont, LoadingTextFont, line)
            if Load3D == True:
                percent = 0
                Map = pywavefront.Wavefront(os.path.join(base_folder, ("Resources\\G3_Resources\\Map\\map.obj")), create_materials=True, collect_faces=True) 
                MapVerts = numpy.array(Map.vertices)
                Map_box = (MapVerts[0], MapVerts[0])
                counterFORvertex = 0
                for vertex in MapVerts:
                    counterFORvertex += 1
                    min_v, max_v, Map_box, counterFORvertex = LoadingMapGraphics(vertex, Map_box, counterFORvertex)
                    
                    LoadingPercentForEfficiency = (100/13224)*counterFORvertex
                    if int(LoadingPercentForEfficiency) == percent:
                        if percent <= 100:
                            percent += 1

                        LoadingPercent += 2.6448*LineScaleFact
                        COMPLETIONpercent = (100/13224)*counterFORvertex
                        GenerateLoadDisplay(Display, LoadingFont, text, f"Started Resource Loading | Map: {int(COMPLETIONpercent)}% complete", BackgroundCol, ShapeCol, FontCol, aa, LoadingPercent, False, AccentCol, MainTitleFont, SecondaryFont, LoadingTextFont, line)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                                return Fullscreen
                        clock.tick(FPS)
                '''glGenBuffers(0, 1)
                glBindBuffer(GL_ARRAY_BUFFER, 0)
                glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW)'''
                Map_size = [Map_box[1][i]-Map_box[0][i] for i in range(3)]
                max_Map_size = max(Map_size)
                Map_size = G3Dscale 
                Map_scale = [Map_size/max_Map_size for i in range(3)]
                Map_trans = [-(Map_box[1][i]+Map_box[0][i])/2 for i in range(3)]

                map_vertices = []
                for mesh in Map.mesh_list: 
                    for face in mesh.faces: 
                        for vertex_i in face: 
                            Data = Map.vertices[vertex_i]
                            for k in range(len(Data)):
                                map_vertices.append(Data[k])
            GenerateLoadDisplay(Display, LoadingFont, text, "Resource Loading | Loaded Map", BackgroundCol, ShapeCol, FontCol, aa, LoadingPercent, True, AccentCol, MainTitleFont, SecondaryFont, LoadingTextFont, line)
            if devmode == 10 or devmode-10 == 0:
                pygame.display.set_caption(f"Pycraft: v{version}: Playing | Developer mode | V: 0, 0, 0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Playing")

            LoadingPercent += 100+((75/7)*LineScaleFact)
            GenerateLoadDisplay(Display, LoadingFont, text, "Resource Loading | Loaded Map", BackgroundCol, ShapeCol, FontCol, aa, LoadingPercent, True, AccentCol, MainTitleFont, SecondaryFont, LoadingTextFont, line)
            
            run = 0
            pygame.event.get()
            pygame.mouse.set_pos(640, 360)
            Total_move_x, Total_move_y, Total_move_z = 0, 0, 0
            if devmode == 10 or devmode-10 == 0:
                pygame.display.set_caption(f"Pycraft: v{version}: Playing | Developer mode | V: 0, 0, 0 | FPS: {int(clock.get_fps())} aFPS: {int(clock.get_fps())} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | Theme: {theme}")
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Playing")
            WKeyPressed, AKeyPressed, SKeyPressed, DKeyPressed = False, False, False, False
            stop = False
            stop1 = False
            counterForWeather = 2
            weather = random.randint(0, 2)

            LoadingPercent = (realWidth-100)*LineScaleFact
            GenerateLoadDisplay(Display, LoadingFont, text, "Finished Resource Loading; Rendering", BackgroundCol, ShapeCol, FontCol, aa, LoadingPercent, True, AccentCol, MainTitleFont, SecondaryFont, LoadingTextFont, line)

            if Fullscreen == False:
                pygame.display.quit()
                pygame.init()
                pygame.display.set_mode((realWidth, realHeight), DOUBLEBUF|OPENGL)
                display = (realWidth, realHeight)
                keydown = False
            elif Fullscreen == True:
                FullscreenX, FullscreenY = pyautogui.size()
                pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF|OPENGL)
                display = (FullscreenX,FullscreenY)
                keydown = False

            LoadSkyBox(aa)
            LoadMapTexture(aa)
            
            gluPerspective(FOV, (display[0]/display[1]), 1, (rendis*100000))
            firstRUN = 0
            pygame.mouse.set_pos(640, 360)

            prev_camera_x = camera_x
            prev_camera_y = camera_y
            prev_camera_z = camera_z

            prev_collisions = 0

            collisions = [False, 0]

            WkeydownTimer = 0
            AkeydownTimer = 0
            SkeydownTimer = 0
            DkeydownTimer = 0

            glShadeModel(GL_SMOOTH)
            glMatrixMode(GL_MODELVIEW)
            if aa == True:
                glEnable(GL_MULTISAMPLE)
            elif aa == False:
                glDisable(GL_MULTISAMPLE)
            glEnable(GL_FRAMEBUFFER_SRGB)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
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
                realWidth, realHeight = pygame.display.get_window_size()
                if realWidth < 1280:
                    Display = pygame.display.set_mode((1280, realHeight), RESIZABLE)
                if realHeight < 720:
                    Display = pygame.display.set_mode((realWidth, 720), RESIZABLE)
                
                if pygame.mixer.get_busy() == False:
                    PlayAmbientSound(musicVOL)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return Fullscreen
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            AKeyPressed = True
                        if event.key == pygame.K_d:
                            DKeyPressed = True
                        if event.key == pygame.K_e:
                            if Fullscreen == False:
                                myScreenshot = pyautogui.screenshot(region=((0, 0, realWidth, realHeight)))
                                myScreenshot.save(os.path.join(base_folder, ("Resources\\General_Resources\\PauseIMG.png")))
                            else:
                                hwnd = pygame.display.get_wm_info()["window"]

                                prototype = WINFUNCTYPE(BOOL, HWND, POINTER(RECT))
                                paramflags = (1, "hwnd"), (2, "lprect")

                                GetWindowRect = prototype(("GetWindowRect", windll.user32), paramflags)

                                rect = GetWindowRect(hwnd)
                                myScreenshot = pyautogui.screenshot(region=((rect.left+8, rect.top+31, realWidth, realHeight)))
                                myScreenshot.save(os.path.join(base_folder, ("Resources\\General_Resources\\PauseIMG.png")))
                            Fullscreen = Inventory(FontCol, BackgroundCol, ShapeCol, aa, version, FPS, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D, map_vertices, realWidth, realHeight, Fullscreen, SavedWidth, SavedHeight)
                            Load3D = False
                            main(FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, Display, G3Dscale, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D, map_vertices, realWidth, realHeight, Fullscreen, SavedWidth, SavedHeight, AccentCol)
                        if event.key == pygame.K_F11:
                            keydown = True
                            if keydown == True:
                                if Fullscreen == True:
                                    Fullscreen = False
                                    pygame.display.quit()
                                    pygame.init()
                                    pygame.display.set_mode((SavedWidth, SavedHeight), DOUBLEBUF|OPENGL)
                                    display = (realWidth, realHeight)
                                    keydown = False
                                elif Fullscreen == False:
                                    Fullscreen = True
                                    realWidth, realHeight = pygame.display.get_window_size()
                                    FullscreenX, FullscreenY = pyautogui.size()
                                    pygame.display.quit()
                                    pygame.init()
                                    pygame.display.set_mode((FullscreenX, FullscreenY), FULLSCREEN|HWSURFACE|DOUBLEBUF|OPENGL)
                                    display = (FullscreenX,FullscreenY)
                                    keydown = False
                            gluPerspective(FOV, (display[0]/display[1]), 1, (rendis*100000))
                            glShadeModel(GL_SMOOTH)
                            glMatrixMode(GL_MODELVIEW)
                            if aa == True:
                                glEnable(GL_MULTISAMPLE)
                            elif aa == False:
                                glDisable(GL_MULTISAMPLE)
                            glEnable(GL_FRAMEBUFFER_SRGB)
                        if event.key == pygame.K_r:
                            Fullscreen = MapGUI(FontCol, BackgroundCol, ShapeCol, aa, version, FPS, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D, map_vertices, realWidth, realHeight, Fullscreen, SavedWidth, SavedHeight)
                            Load3D = False
                            main(FontCol, BackgroundCol, ShapeCol, rendis, FPS, FOV, cameraANGspeed, devmode, aa, RenderFOG, Display, G3Dscale, Map, Map_box, min_v, max_v, Map_scale, Map_trans, Map_size, max_Map_size, Load3D, map_vertices, realWidth, realHeight, Fullscreen, SavedWidth, SavedHeight, AccentCol)
                        if event.key == pygame.K_w:
                            WKeyPressed = True
                        if event.key == pygame.K_s:
                            SKeyPressed = True
                        if event.key == pygame.K_SPACE and Jump == False: 
                            Jump = True
                        if event.key == pygame.K_l:
                            if MouseUnlock == True:
                                MouseUnlock = False
                            elif MouseUnlock == False:
                                MouseUnlock = True
                        if event.key == pygame.K_q:
                            DataWindow = tk.Tk()
                            DataWindow.title("Player Information")
                            DataWindow.configure(width = 500, height = 300)
                            DataWindow.configure(bg="lightblue")
                            
                            versionData = f"Pycraft: v{version}: Playing"
                            versionData, CoordinatesData, FPSData, RendisData, FOVData = f"Pycraft: v{version}", f"Coordinates: x: {round(camera_x, 3)} y: {round(camera_y, 3)} z: {round(camera_z, 3)}", f"FPS: {eFPS}", f"Render distance: {rendis}", f"FOV: {FOV}"
                            
                            versionData, CoordinatesData, FPSData, RendisData, FOVData = tk.Label(DataWindow, text = versionData), tk.Label(DataWindow, text = CoordinatesData), tk.Label(DataWindow, text = FPSData), tk.Label(DataWindow, text = RendisData), tk.Label(DataWindow, text = FOVData)
                            
                            versionData.grid(row = 0, column = 0, columnspan = 2)
                            CoordinatesData.grid(row = 1, column = 0, columnspan = 2)
                            FPSData.grid(row = 2, column = 0, columnspan = 2)
                            RendisData.grid(row = 3, column = 0, columnspan = 2)
                            FOVData.grid(row = 4, column = 0, columnspan = 2)
                            DataWindow.mainloop()
                            DataWindow.quit()
                            pygame.mouse.set_pos(600, 360)
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w:
                            WKeyPressed = False
                        if event.key == pygame.K_a:
                            AKeyPressed = False
                        if event.key == pygame.K_s:
                            SKeyPressed = False
                        if event.key == pygame.K_d:
                            DKeyPressed = False
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 4:
                            glTranslatef(0, 0, 1)
                        if event.button == 5:
                            glTranslatef(0, 0, -1)

                if WKeyPressed == True:
                    WkeydownTimer += 1
                    if stop == False:
                        time = eFPS*3
                        stop = True
                    if time >= 0:
                        Total_move_z += 35
                        if WkeydownTimer/(aFPS/iteration) >= ((random.randint(75, 100))/100):
                            if sound == True:
                                PlayFootstepsSound(soundVOL)
                            WkeydownTimer = 0
                    elif time <= 0:
                        if WkeydownTimer/(aFPS/iteration) >= ((random.randint(40, 50))/100):
                            if sound == True:
                                PlayFootstepsSound(soundVOL)
                            WkeydownTimer = 0
                        Total_move_z += 100

                    time -= 1
                else:
                    stop = False
                    WkeydownTimer = 0

                if AKeyPressed == True:
                    Total_move_x += -35 
                    AkeydownTimer += 1

                    if AkeydownTimer/(aFPS/iteration) >= ((random.randint(75, 100))/100):
                        if sound == True:
                            PlayFootstepsSound(soundVOL)
                        AkeydownTimer = 0
                else:
                    AkeydownTimer = 0

                if SKeyPressed == True:
                    Total_move_z += -35 
                    SkeydownTimer += 1

                    if SkeydownTimer/(aFPS/iteration) >= ((random.randint(75, 100))/100):
                        if sound == True:
                            PlayFootstepsSound(soundVOL)
                        SkeydownTimer = 0
                else:
                    SkeydownTimer = 0

                if DKeyPressed == True:
                    Total_move_x += 35 
                    DkeydownTimer += 1

                    if DkeydownTimer/(aFPS/iteration) >= ((random.randint(75, 100))/100):
                        if sound == True:
                            PlayFootstepsSound(soundVOL)
                        DkeydownTimer = 0
                else:
                    DkeydownTimer = 0

                
                if Jump == True:
                    JumpID += 1
                    if JumpID <= 20:
                        JumpID += 1
                        Total_move_y -= 100
                    if JumpID >= 21:
                        JumpID += 1
                        Total_move_y += 100
                    if JumpID >= 40:
                        if sound == True:
                            PlayFootstepsSound(soundVOL)
                        Jump = False
                        JumpID = 0

                if MouseUnlock == True:
                    if mX >= 680:
                        glRotatef(cameraANGspeed, 0, 1, 0) 
                        rotationvectX += 0.5
                        
                    if mX <= 600:
                        glRotatef(-cameraANGspeed, 0, 1, 0) 
                        rotationvectX += -0.5

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
                    pygame.display.set_caption(f"Pycraft: v{version}: Playing | Developer mode | V: {Total_move_x, Total_move_y, Total_move_z} C: {round(camera_x, 3)}, {round(camera_y, 3)}, {round(camera_z, 3)} (c: {collisions[0]} t: {collisions[1]}) | FPS: {int(eFPS)} aFPS: {int((aFPS/iteration))} | MemUsE: {psutil.virtual_memory().percent} | CPUUsE: {str(psutil.cpu_percent())} | weather: {weather} changeIN: {round(counterForWeather/FPS)}/300 | Theme: {theme}")
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
                    glTranslatef(0, 50000, 0)
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
                CHandle.MapModel(Map, Map_scale, Map_trans, map_vertices)
                if stop1 == False:
                    counterForWeather = 1
                    stop1 = True
                counterForWeather = counterForWeather + random.randint(0, 10)
                if counterForWeather/FPS >= 300:
                    weather = random.randint(0, 2)
                    stop1 = False
                if RenderFOG == True and weather == 2: 
                    glEnable(GL_FOG)
                    glFogfv(GL_FOG_COLOR, (239, 243, 245, 1)) 
                    glFogi(GL_FOG_MODE, GL_LINEAR)
                    glFogf(GL_FOG_START, 160) 
                    glFogf(GL_FOG_END, 3000) 
                    glFogf(GL_FOG_DENSITY, 0) 
                elif RenderFOG == True and weather == 1: 
                    glEnable(GL_FOG)
                    glFogfv(GL_FOG_COLOR, (115, 145, 165, 1)) 
                    glFogi(GL_FOG_MODE, GL_LINEAR)
                    glFogf(GL_FOG_START, 160) 
                    glFogf(GL_FOG_END, 9000) 
                    glFogf(GL_FOG_DENSITY, 0) 
                elif RenderFOG == True and weather == 0: 
                    glEnable(GL_FOG)
                    glFogfv(GL_FOG_COLOR, (177, 194, 205, 1)) 
                    glFogi(GL_FOG_MODE, GL_LINEAR)
                    glFogf(GL_FOG_START, 160) 
                    glFogf(GL_FOG_END, 30000) 
                    glFogf(GL_FOG_DENSITY, 0) 
                elif RenderFOG == False:
                    glDisable(GL_FOG)
                glEnable(GL_LIGHTING)
                glEnable(GL_LIGHT0)
                glLightfv(GL_LIGHT0,GL_POSITION, (Sun_pos_x, Sun_pos_y, Sun_pos_z))
                glLightfv(GL_LIGHT0,GL_AMBIENT, (1, 0, 1, 1))
                glLightfv(GL_LIGHT0,GL_DIFFUSE, (1, 0, 1, 1))
                glLightfv(GL_LIGHT0,GL_SPECULAR, (1, 0, 1, 1))
                glEnable(GL_COLOR_MATERIAL)
                glColorMaterial(GL_FRONT_AND_BACK,GL_AMBIENT_AND_DIFFUSE)
                glMaterial(GL_FRONT_AND_BACK,GL_SPECULAR, (0, 1, 0, 1))
                glMaterial(GL_FRONT_AND_BACK,GL_EMISSION, (0, 1, 0, 1))

                glTranslatef(Total_move_x, Total_move_y, Total_move_z)
                PlayerModel_pos_x, PlayerModel_pos_y, PlayerModel_pos_z = -Total_move_x, -Total_move_y, -Total_move_z
                Total_move_x, Total_move_y, Total_move_z = 0, 0, 0

                pygame.display.flip()
                clock.tick(FPS)


        themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, musicVOL, camera_x, camera_y, camera_z, size, theme, lastRun, startUP = Home_Screen(Display, themeArray, FontCol, BackgroundCol, ShapeCol, AccentCol, numOFerrors, devmode, rendis, FPS, FOV, cameraANGspeed, aa, RenderFOG, G3Dscale, FanSky, FanPart, sound, soundVOL, music, musicVOL, camera_x, camera_y, camera_z, size, theme, lastRun, startUP, Fullscreen, SavedWidth, SavedHeight)
    except Exception as error:
        try:
            import os, traceback
            base_folder = os.path.dirname(__file__)
            error = ''.join(traceback.format_exception(None, error, error.__traceback__))
            with open(os.path.join(base_folder, ("Data_Files\\errorREPORT.txt")), "w") as errorFILE:
                errorFILE.write(str(error)+"\n")

            try:
                with open(os.path.join(base_folder, ("Data_Files\\SaveGameConfig.txt")), mode ="w") as SaveGameConfig:
                    current_time = datetime.datetime.now()
                    currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"
                    SaveGameConfigDict = {"theme":theme, "FPS":FPS, "eFPS":60, "aFPS":60, "FOV":FOV, "cameraANGspeed":cameraANGspeed, "aa":aa, "RenderFOG":RenderFOG, "FanSky":FanSky, "FanPart":FanPart, "sound":sound, "soundVOL":soundVOL, "music":music, "musicVOL":musicVOL, "X":camera_x, "Y":camera_y, "Z":camera_z, "lastRun":currentDate, 'startup': startUP, 'crash': False, 'DisplayWidth':SavedWidth, 'DisplayHeight':SavedHeight, 'WindowStatus':True}
                    SaveGameConfig.write("save = "+str(save))
            except Exception as FailedToRepairFile:
                import os, traceback
                base_folder = os.path.dirname(__file__)
                error = ''.join(traceback.format_exception(None, error, error.__traceback__))
                with open(os.path.join(base_folder, ("Data_Files\\errorREPORT.txt")), "w") as errorFILE:
                    errorFILE.write(str(f"An error occured whilst trying to save progress on game crash: {FailedToRepairFile}")+"\n")
        except Exception as FatalError:
            try:
                from tkinter import *
                from tkinter import messagebox
                pygame.quit()
                root = Tk()
                root.withdraw()
                messagebox.showerror("Pycraft encountered a problem", f"Your game has errored out, we have since tried to save and repair your progress and data and restart the program, unfortunately this has failed unavoidably. THIS COULD RENDER THE GAME UNPLAYABLE, for help please contact the developer @ thomasjebbo@gmail.com, we apologise greatly for any inconvenience this has caused. A second GUI may appear giving a more graphical message about what went wrong however these crashes can be so bad this may not occur.")
                quit()
            except:
                print("Fatal Error Occured")
else:
    from tkinter import *
    from tkinter import messagebox
    try:
        pygame.quit()
    except:
        donothing = 0
    finally:
        root = Tk()
        root.withdraw()
        messagebox.showwarning("Run error", "Please run this file through PycraftRunUtil, not youself")
        quit()