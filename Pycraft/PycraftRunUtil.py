if __name__ == "__main__":
    print("--Running PycraftRunUtil")
    try:
        import tkinter as tk
        from tkinter.ttk import *
        from PIL import Image, ImageTk, ImageGrab
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
        import traceback
        import datetime
        import ctypes
    except Exception as IntError:
        print(IntError)
        try:
            import PycraftInstaller
        except:
            crash = True
        else:
            contINT=0
    else:
        contINT=0

        if sys.platform == "win32" or sys.platform == "win64":
            os.environ["SDL_VIDEO_CENTERED"] = "1"

        base_folder = os.path.dirname(__file__)

        def crash(error, base_folder):
            import os, pygame
            pygame.init()
            pygame.mixer.stop()
            print("--Running PycraftRunUtl")
            try:
                pygame.display.quit()
                pygame.init()
                Display = pygame.display.set_mode((1280, 720))
                pygame.display.set_caption(f"Pycraft: An Error Occured")

                with open(os.path.join(base_folder,("Data_Files\\errorREPORT.txt")), "r+") as ErrorDoc:
                    numOFerrors = len(ErrorDoc.readlines())
                    ErrorDoc.write(str(error)+"\n")
                    errorTOTALforRETURNING = str(ErrorDoc.read())+"\n"+str(error)
                with open(os.path.join(base_folder,("Data_Files\\errorREPORT.txt")), "r+") as ErrorDoc:
                    error = ErrorDoc.read()
                    ErrorDoc.seek(0)
                    ErrorArray1 = ErrorDoc.readlines()

                ErrorDocLines = 0

                ErrorArray = []
                for i in range(len(error)):
                    if error[i:i+22] == "<module 'OpenGL.error'":
                        break
                    if error[i:i+len('Thanks for playing')] == "Thanks for playing":
                        quit()
                    if not error[i] == "\n":
                        ErrorArray.append(error[i])
                    else:
                        ErrorDocLines += 1

                TextPERline = {}

                MessageFont = pygame.font.Font(os.path.join(base_folder,("Fonts\\Book Antiqua.ttf")), 15)

                for a in range(len(ErrorArray1)):
                    while str(ErrorArray1[a])[0] == " ":
                        ErrorArray1[a] = ErrorArray1[a][1:]
                    if len(ErrorArray1[a]) == 253:
                        ErrorArray1[a] = "[sub] Home_Screen"
                    if len(ErrorArray1[a]) == 181:
                        ErrorArray1[a] = "[sub] Settings"
                    if len(ErrorArray1[a]) == 90:
                        ErrorArray1[a] = "[sub] Credits"
                    if len(ErrorArray1[a]) == 172:
                        ErrorArray1[a] = "[sub] Inventory"
                    if len(ErrorArray1[a]) == 169:
                        ErrorArray1[a] = "[sub] MapGUI"
                    if len(ErrorArray1[a]) == 100:
                        ErrorArray1[a] = "[sub] Map_Graphics"
                    if len(ErrorArray1[a]) == 229:
                        ErrorArray1[a] = "[sub] Main"

                    if len(ErrorArray1[a]) >= 75:
                        temp = str(ErrorArray1[a])
                        ErrorArray1[a] = ((ErrorArray1[a])[:75])+"..."

                for k in range(ErrorDocLines):
                    TextPERline.update({f"{k}":str(ErrorArray1[k])})

                ErrorMessageText0 = MessageFont.render(TextPERline["0"], True, (255,0,0))
                if ErrorDocLines >= 2:
                    ErrorMessageText1 = MessageFont.render(TextPERline["1"], True, (255,0,0))
                if ErrorDocLines >= 3:
                    ErrorMessageText2 = MessageFont.render(TextPERline["2"], True, (255,0,0))
                if ErrorDocLines >= 4:
                    ErrorMessageText3 = MessageFont.render(TextPERline["3"], True, (255,0,0))
                if ErrorDocLines >= 5:
                    ErrorMessageText4 = MessageFont.render(TextPERline["4"], True, (255,0,0))
                if ErrorDocLines >= 6:
                    ErrorMessageText5 = MessageFont.render(TextPERline["5"], True, (255,0,0))
                if ErrorDocLines >= 7:
                    ErrorMessageText6 = MessageFont.render(TextPERline["6"], True, (255,0,0))
                if ErrorDocLines >= 8:
                    ErrorMessageText7 = MessageFont.render(TextPERline["7"], True, (255,0,0))
                if ErrorDocLines >= 9:
                    ErrorMessageText8 = MessageFont.render(TextPERline["8"], True, (255,0,0))
                if ErrorDocLines >= 10:
                    ErrorMessageText9 = MessageFont.render(TextPERline["9"], True, (255,0,0))
                if ErrorDocLines >= 11:
                    ErrorMessageText10 = MessageFont.render(TextPERline["10"], True, (255,0,0))
                if ErrorDocLines >= 12:
                    ErrorMessageText11 = MessageFont.render(TextPERline["11"], True, (255,0,0))
                if ErrorDocLines >= 13:
                    ErrorMessageText12 = MessageFont.render(TextPERline["12"], True, (255,0,0))

                numOFerrorsText = MessageFont.render(f"This many errors where encountered during the running of the program: {numOFerrors}", True, (255,152,0))
                
                Display = pygame.display.set_mode((1280,720))

                IconImage = pygame.image.load(os.path.join(base_folder,("Resources\\Error_Resources\\Icon.jpg")))
                pygame.display.set_icon(IconImage)
                image = pygame.image.load(os.path.join(base_folder,("Resources\\Error_Resources\\Error_Message.png")))
                Clock = pygame.time.Clock()

                while True:
                    Display.fill((20,20,20))
                    Display.blit(image, (0,0))
                    displacement = 200
                    Display.blit(ErrorMessageText0, (0, 200))
                    if ErrorDocLines >= 2:
                        Display.blit(ErrorMessageText1, (0, 215))
                        displacement += 15
                    if ErrorDocLines >= 3:
                        Display.blit(ErrorMessageText2, (0, 230))
                        displacement += 15
                    if ErrorDocLines >= 4:
                        Display.blit(ErrorMessageText3, (0, 245))
                        displacement += 15
                    if ErrorDocLines >= 5:
                        Display.blit(ErrorMessageText4, (0, 260))
                        displacement += 15
                    if ErrorDocLines >= 6:
                        Display.blit(ErrorMessageText5, (0, 275))
                        displacement += 15
                    if ErrorDocLines >= 7:
                        Display.blit(ErrorMessageText6, (0, 290))
                        displacement += 15
                    if ErrorDocLines >= 8:
                        Display.blit(ErrorMessageText7, (0, 305))
                        displacement += 15
                    if ErrorDocLines >= 9:
                        Display.blit(ErrorMessageText8, (0, 320))
                        displacement += 15
                    if ErrorDocLines >= 10:
                        Display.blit(ErrorMessageText9, (0, 335))
                        displacement += 15
                    if ErrorDocLines >= 11:
                        Display.blit(ErrorMessageText10, (0, 350))
                        displacement += 15
                    if ErrorDocLines >= 12:
                        Display.blit(ErrorMessageText11, (0, 365))
                        displacement += 15
                    if ErrorDocLines >= 13:
                        Display.blit(ErrorMessageText12, (0, 380))
                        displacement += 15
                    if ErrorDocLines >= 14:
                        displacement += 15
                        ErrorMessageText13 = MessageFont.render("...", True, (255,0,0))
                        Display.blit(ErrorMessageText12, (0, 395))

                    Display.blit(numOFerrorsText, (0, displacement+15))

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
        messagebox.showwarning("Run error", "Please run this file yourself, not through another script")
        quit()
