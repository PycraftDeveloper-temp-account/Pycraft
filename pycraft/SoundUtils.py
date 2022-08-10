if __name__ != "__main__":
    print("Started <Pycraft_SoundUtils>")

    class PlaySound:
        def __init__(self):
            pass

        def PlayInvSound(self):
            try:
                if self.platform == "Linux":
                    self.mod_pygame__.mixer.music.load(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//general resources//InventoryGeneral.ogg")))

                else:
                    self.mod_pygame__.mixer.music.load(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\general resources\\InventoryGeneral.ogg")))

                self.mod_pygame__.mixer.music.set_volume(self.music_volume/100)
                self.mod_pygame__.mixer.music.play(loops=-1)
            except Exception as Message:
                if not self.stop_thread_event.is_set():
                    self.error_message = "SoundUtils > PlaySound > PlayInvSound: "+str(Message)

                    self.error_message_detailed = "".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

        def PlayClickSound(self):
            try:
                channel0 = self.mod_pygame__.mixer.Channel(0)
                if self.platform == "Linux":
                    clickMUSIC = self.mod_pygame__.mixer.Sound(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//general resources//Click.ogg")))

                else:
                    clickMUSIC = self.mod_pygame__.mixer.Sound(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\general resources\\Click.ogg")))

                channel0.set_volume(self.sound_volume/100)
                channel0.play(clickMUSIC)
                self.mod_pygame__.time.wait(40)
            except Exception as Message:
                if not self.stop_thread_event.is_set():
                    self.error_message = "SoundUtils > PlaySound > PlayClickSound: "+str(Message)

                    self.error_message_detailed = "".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

        def PlayFootstepsSound(self):
            try:
                channel1 = self.mod_pygame__.mixer.Channel(1)
                RandomNum = self.mod_random__.randint(0, 5)

                if self.platform == "Linux":
                    Footsteps = self.mod_pygame__.mixer.Sound(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            (f"resources//game engine resources//GameSounds//footstep//footsteps{RandomNum}.wav")))

                else:
                    Footsteps = self.mod_pygame__.mixer.Sound(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            (f"resources\\game engine resources\\GameSounds\\footstep\\footsteps{RandomNum}.wav")))

                channel1.set_volume(self.sound_volume/100)
                channel1.play(Footsteps)
            except Exception as Message:
                if not self.stop_thread_event.is_set():
                    self.error_message = "SoundUtils > PlaySound > PlayFootstepsSound: "+str(Message)

                    self.error_message_detailed = "".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

        def PlayAmbientSound(self):
            try:
                channel2 = self.mod_pygame__.mixer.Channel(2)
                if self.platform == "Linux":
                    LoadAmb = self.mod_pygame__.mixer.Sound(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//game engine resources//GameSounds//FieldAmb.ogg")))

                else:
                    LoadAmb = self.mod_pygame__.mixer.Sound(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\game engine resources\\GameSounds\\FieldAmb.ogg")))

                channel2.set_volume(self.sound_volume/100)
                channel2.play(LoadAmb)
            except Exception as Message:
                if not self.stop_thread_event.is_set():
                    self.error_message = "SoundUtils > PlaySound > PlayAmbientSound: "+str(Message)

                    self.error_message_detailed = "".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

        def PlayThunderSound(self):
            try:
                channel3 = self.mod_pygame__.mixer.Channel(3)
                RandomNum = self.mod_random__.randint(0, 10)

                if self.platform == "Linux":
                    Thunder = self.mod_pygame__.mixer.Sound(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            (f"resources//game engine resources//GameSounds//thunder//thunder{RandomNum}.ogg")))

                else:
                    Thunder = self.mod_pygame__.mixer.Sound(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            (f"resources\\game engine resources\\GameSounds\\thunder\\thunder{RandomNum}.ogg")))

                channel3.set_volume(self.sound_volume/100)
                channel3.play(Thunder)
            except Exception as Message:
                if not self.stop_thread_event.is_set():
                    self.error_message = "SoundUtils > PlaySound > PlayThunderSound: " + \
                        str(Message)

                    self.error_message_detailed = "".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

        def PlayRainSound(self):
            try:
                channel4 = self.mod_pygame__.mixer.Channel(4)

                if self.platform == "Linux":
                    Rain = self.mod_pygame__.mixer.Sound(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//game engine resources//GameSounds//rain.ogg")))

                else:
                    Rain = self.mod_pygame__.mixer.Sound(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\game engine resources\\GameSounds\\rain.ogg")))

                channel4.set_volume(self.sound_volume/100)
                channel4.play(Rain)
            except Exception as Message:
                if not self.stop_thread_event.is_set():
                    self.error_message = "SoundUtils > PlaySound > PlayRainSound: " + \
                        str(Message)

                    self.error_message_detailed = "".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

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
