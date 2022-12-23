if __name__ != "__main__":
    try:
        import os
        import random
            
        import pygame
    except Exception as Message:
        try:
            import sys
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(
                "Startup Fail",
                str(Message))
            sys.exit()

        except Exception as Message:
            print(Message)
            sys.exit()
            
    class play_sound:
        def __init__(self):
            pass

        def play_inventory_sound(platform, base_folder, music_volume):
            if platform == "Linux":
                pygame.mixer.music.load(
                    os.path.join(
                        base_folder,
                        ("resources//general resources//inventoryGeneral.ogg")))

            else:
                pygame.mixer.music.load(
                    os.path.join(
                        base_folder,
                        ("resources\\general resources\\inventoryGeneral.ogg")))

            pygame.mixer.music.set_volume(music_volume/100)
            pygame.mixer.music.play(loops=-1)

        def play_click_sound(platform, base_folder, sound_volume):
            channel0 = pygame.mixer.Channel(0)
            if platform == "Linux":
                clickMUSIC = pygame.mixer.Sound(
                    os.path.join(
                        base_folder,
                        ("resources//general resources//Click.ogg")))

            else:
                clickMUSIC = pygame.mixer.Sound(
                    os.path.join(
                        base_folder,
                        ("resources\\general resources\\Click.ogg")))

            channel0.set_volume(sound_volume/100)
            channel0.play(clickMUSIC)
            pygame.time.wait(40)
                
        def play_footsteps_sound(self):
            channel1 = pygame.mixer.Channel(1)
            RandomNum = random.randint(0, 5)

            if self.platform == "Linux":
                Footsteps = pygame.mixer.Sound(
                    os.path.join(
                        self.base_folder,
                        (f"resources//game engine resources//GameSounds//footstep//footsteps{RandomNum}.wav")))

            else:
                Footsteps = pygame.mixer.Sound(
                    os.path.join(
                        self.base_folder,
                        (f"resources\\game engine resources\\GameSounds\\footstep\\footsteps{RandomNum}.wav")))

            channel1.set_volume(self.sound_volume/100)
            channel1.play(Footsteps)

        def play_ambient_sound(self):
            channel2 = pygame.mixer.Channel(2)
            if self.platform == "Linux":
                LoadAmb = pygame.mixer.Sound(
                    os.path.join(
                        self.base_folder,
                        ("resources//game engine resources//GameSounds//FieldAmb.ogg")))

            else:
                LoadAmb = pygame.mixer.Sound(
                    os.path.join(
                        self.base_folder,
                        ("resources\\game engine resources\\GameSounds\\FieldAmb.ogg")))

            channel2.set_volume(self.sound_volume/100)
            channel2.play(LoadAmb)

        def play_thunder_sound(self):
            channel3 = pygame.mixer.Channel(3)
            RandomNum = random.randint(0, 10)

            if self.platform == "Linux":
                Thunder = pygame.mixer.Sound(
                    os.path.join(
                        self.base_folder,
                        (f"resources//game engine resources//GameSounds//thunder//thunder{RandomNum}.ogg")))

            else:
                Thunder = pygame.mixer.Sound(
                    os.path.join(
                        self.base_folder,
                        (f"resources\\game engine resources\\GameSounds\\thunder\\thunder{RandomNum}.ogg")))

            channel3.set_volume(self.sound_volume/100)
            channel3.play(Thunder)

        def play_rain_sound(self):
            channel4 = pygame.mixer.Channel(4)

            if self.platform == "Linux":
                Rain = pygame.mixer.Sound(
                    os.path.join(
                        self.base_folder,
                        ("resources//game engine resources//GameSounds//rain.ogg")))

            else:
                Rain = pygame.mixer.Sound(
                    os.path.join(
                        self.base_folder,
                        ("resources\\game engine resources\\GameSounds\\rain.ogg")))

            channel4.set_volume(self.sound_volume/100)
            channel4.play(Rain)

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Fail",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
