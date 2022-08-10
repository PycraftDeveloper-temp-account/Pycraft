if __name__ != "__main__":
    print("Started <Pycraft_displayUtils>")

    class displayFunctionality:
        def __init__(self):
            pass

        def core_display_functions(self, location="Home", checkEvents=True):
            if self.use_mouse_input is False:
                self.mod_pygame__.mouse.set_visible(False)
                if self.joystick_mouse[0] == "Right":
                    self.mouse_x += 3
                if self.joystick_mouse[0] == "Left":
                    self.mouse_x -= 3
                if self.joystick_mouse[1] == "Up":
                    self.mouse_y += 3
                if self.joystick_mouse[1] == "Down":
                    self.mouse_y -= 3
                self.mod_pygame__.mouse.set_pos(
                    self.mouse_x,
                    self.mouse_y)
            else:
                self.joystick_confirm = False
                self.mouse_x = self.mod_pygame__.mouse.get_pos()[0]
                self.mouse_y = self.mod_pygame__.mouse.get_pos()[1]
                self.mod_pygame__.mouse.set_visible(True)

            self.real_window_width = self.mod_pygame__.display.get_window_size()[0]
            self.real_window_height = self.mod_pygame__.display.get_window_size()[1]

            if self.real_window_width < 1280:
                self.mod_display_utils__.displayUtils.GenerateMindisplay(
                    self,
                    1280,
                    self.saved_window_height)

            if self.real_window_height < 720:
                self.mod_display_utils__.displayUtils.GenerateMindisplay(
                    self,
                    self.saved_window_width,
                    720)

            if self.saved_window_width == self.fullscreen_x:
                self.saved_window_width = 1280

            if self.saved_window_height == self.fullscreen_y:
                self.saved_window_height = 720

            if self.real_window_width != self.fullscreen_x and self.real_window_height != self.fullscreen_y:
                self.saved_window_width = self.mod_pygame__.display.get_window_size()[0]
                self.saved_window_height = self.mod_pygame__.display.get_window_size()[1]

            self.eFPS = self.clock.get_fps()
            self.aFPS += self.eFPS
            self.iteration += 1

            if self.use_mouse_input is False:
                if self.joystick_exit:
                    self.joystick_exit = False
                    if self.sound:
                        self.mod_sound_utils__.PlaySound.PlayClickSound(self)
                    self.startup_animation = True
                    self.run_timer = 0
                    self.go_to = location

            if self.joystick_confirm:
                self.mouse_button_down = True
                self.joystick_confirm = False

            if checkEvents:
                displayEvents = self.mod_pygame__.event.get()
                for event in displayEvents:
                    if (event.type == self.mod_pygame__.QUIT
                            or (event.type == self.mod_pygame__.KEYDOWN
                                and event.key == self.mod_pygame__.K_ESCAPE)):

                        self.joystick_exit = False

                        if self.sound:
                            self.mod_sound_utils__.PlaySound.PlayClickSound(
                                self)

                        self.startup_animation = True
                        self.run_timer = 0
                        self.go_to = location

                    elif event.type == self.mod_pygame__.KEYDOWN:
                        if event.key == self.mod_pygame__.K_SPACE and self.devmode < 10:
                            self.devmode += 1

                        if event.key == self.mod_pygame__.K_q:
                            self.mod_tkinter_utils__.TkinterInfo.CreateTkinterWindow(
                                self)

                        if event.key == self.mod_pygame__.K_F11:
                            self.mod_display_utils__.displayUtils.updatedisplay(self)

                        if event.key == self.mod_pygame__.K_x:
                            self.devmode = 1

                return displayEvents


    class displayUtils:
        def __init__(self):
            pass


        def updatedisplay(self):
            self.data_aFPS = []
            self.data_CPU_usage = []
            self.data_eFPS = []
            self.data_memory_usage = []

            self.timer = 0

            self.data_aFPS_Max = 1
            self.data_CPU_usage_Max = 1
            self.data_eFPS_Max = 1
            self.data_memory_usage_Max = 1

            try:
                try:
                    self.fullscreen_x = self.mod_pyautogui__.size()[0]
                    self.fullscreen_y = self.mod_pyautogui__.size()[1]

                    self.mod_pygame__.display.set_icon(self.window_icon)

                    if self.fullscreen is False:
                        self.fullscreen = True
                        self.display = self.mod_pygame__.display.set_mode(
                            (self.saved_window_width, self.saved_window_height),
                            self.mod_pygame__.RESIZABLE)

                    elif self.fullscreen:
                        self.fullscreen = False
                        self.display = self.mod_pygame__.display.set_mode(
                            (self.fullscreen_x, self.fullscreen_y),
                            self.mod_pygame__.FULLSCREEN|
                            self.mod_pygame__.HWSURFACE|
                            self.mod_pygame__.DOUBLEBUF)

                except Exception as Message:
                    print("displayUtils > displayUtils > updatedisplay: "+ str(Message))
                    self.fullscreen = True
                    self.saved_window_width = 1280
                    self.saved_window_height = 720
                    self.mod_pygame__.display.quit()
                    self.mod_pygame__.init()
                    self.display = self.mod_pygame__.display.set_mode(
                        (self.saved_window_width, self.saved_window_height))

                self.mod_pygame__.display.set_icon(self.window_icon)
            except Exception as Message:
                self.error_message = "displayUtils > displayUtils > updatedisplay: "+str(Message)
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

        def set_display(self):
            self.data_aFPS = []
            self.data_CPU_usage = []
            self.data_eFPS = []
            self.data_memory_usage = []

            self.timer = 0

            self.data_aFPS_Max = 1
            self.data_CPU_usage_Max = 1
            self.data_eFPS_Max = 1
            self.data_memory_usage_Max = 1

            try:
                try:
                    self.fullscreen_x = self.mod_pyautogui__.size()[0]
                    self.fullscreen_y = self.mod_pyautogui__.size()[1]

                    if self.fullscreen:
                        self.display = self.mod_pygame__.display.set_mode(
                            (self.saved_window_width, self.saved_window_height),
                            self.mod_pygame__.RESIZABLE)

                    elif self.fullscreen is False:
                        self.display = self.mod_pygame__.display.set_mode(
                            (self.fullscreen_x, self.fullscreen_y),
                            self.mod_pygame__.FULLSCREEN|
                            self.mod_pygame__.HWSURFACE|
                            self.mod_pygame__.DOUBLEBUF)

                except Exception as Message:
                    print("".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__)))

                    print("displayUtils > displayUtils > set_display:", Message)
                    self.saved_window_width = 1280
                    self.saved_window_height = 720
                    self.mod_pygame__.display.quit()
                    self.mod_pygame__.init()
                    self.display = self.mod_pygame__.display.set_mode(
                        (self.saved_window_width, self.saved_window_height))

                self.mod_pygame__.display.set_icon(self.window_icon)
            except Exception as Message:
                self.error_message = "displayUtils > displayUtils > set_display: "+str(Message)
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)


        def GenerateMindisplay(self, width, height):
            try:
                self.display = self.mod_pygame__.display.set_mode(
                    (width, height),
                    self.mod_pygame__.RESIZABLE)

                self.mod_pygame__.display.set_icon(self.window_icon)
            except Exception as Message:
                self.error_message = "".join(("displayUtils > displayUtils > ",
                                             f"GenerateMindisplay: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)


        def GetdisplayLocation(self):
            try:
                hwnd = self.mod_pygame__.display.get_wm_info()["window"]

                prototype = self.mod_ctypes__.WINFUNCTYPE(
                    self.mod_ctypes__.wintypes.BOOL,
                    self.mod_ctypes__.wintypes.HWND,
                    self.mod_ctypes__.POINTER(
                        self.mod_ctypes__.wintypes.RECT))

                paramflags = (1, "hwnd"), (2, "lprect")

                GetWindowRect = prototype(
                    ("GetWindowRect",self.mod_ctypes__.windll.user32),
                    paramflags)

                rect = GetWindowRect(hwnd)
                return rect.left+8, rect.top+31
            except Exception:
                pass


        def GetPlayStatus(self):
            try:
                if self.mod_pygame__.display.get_active():
                    tempFPS = self.FPS
                    self.project_sleeping = False
                    if not (self.command == "Play" or self.command == "Benchmark"):
                        if self.music:
                            self.mod_pygame__.mixer.music.unpause()
                            if self.mod_pygame__.mixer.music.get_busy() == 0:
                                self.mod_sound_utils__.PlaySound.PlayInvSound(self)
                else:
                    tempFPS = 5
                    self.project_sleeping = True
                    self.mod_pygame__.mixer.music.fadeout(500)

                if self.FPS_overclock:
                    tempFPS = 2000

                return tempFPS
            except Exception as Message:
                self.error_message = "displayUtils > displayUtils > GetPlayStatus: "+str(Message)
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)


    class displayAnimations:
        def __init__(self):
            pass


        def FadeIn(self):
            try:
                if self.startup_animation:
                    HideSurface = self.mod_pygame__.Surface(
                        (self.real_window_width, self.real_window_height))

                    SurfaceAlpha = 255-(self.run_timer*1000)
                    HideSurface.set_alpha(SurfaceAlpha)
                    HideSurface.fill(self.background_color)
                    self.display.blit(
                        HideSurface,
                        (0, 100))

                    if SurfaceAlpha <= 0:
                        self.startup_animation = False
            except Exception as Message:
                self.error_message = "displayUtils > displayAnimations > FadeIn: "+str(Message)
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)



        def FadeOut(self):
            try:
                if self.startup_animation:
                    HideSurface = self.mod_pygame__.Surface(
                        (self.real_window_width, self.real_window_height))

                    SurfaceAlpha = 255-(self.run_timer*1000)
                    HideSurface.set_alpha(255-SurfaceAlpha)
                    HideSurface.fill(self.background_color)

                    if self.go_to == "Credits":
                        self.display.blit(
                            HideSurface,
                            (0, 0))
                    else:
                        self.display.blit(
                            HideSurface,
                            (0, 100))

                    if SurfaceAlpha <= 0:
                        self.startup_animation = False
            except Exception as Message:
                self.error_message = "displayUtils > displayAnimations > FadeOut: "+str(Message)
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
