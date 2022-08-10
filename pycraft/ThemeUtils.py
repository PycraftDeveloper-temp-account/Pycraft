if __name__ != "__main__":
    print("Started <Pycraft_ThemeUtils>")

    class DetermineThemeColours:
        def __init__(self):
            pass

        def GetColours(self):
            try:
                self.themeArray = [
                    [(255, 255, 255),
                        [30, 30, 30],
                        (80, 80, 80),
                        (237, 125, 49),
                        (255, 255, 255)],

                    [(0, 0, 0),
                        [255, 255, 255],
                        (80, 80, 80),
                        (237, 125, 49),
                        (100, 100, 100)]]

                if self.theme == "dark":
                    self.font_color = self.themeArray[0][0]
                    self.background_color = self.themeArray[0][1]
                    self.shape_color = self.themeArray[0][2]
                    self.accent_color = self.themeArray[0][3]
                    self.secondary_font_color = self.themeArray[0][4]

                elif self.theme == "light":
                    self.font_color = self.themeArray[1][0]
                    self.background_color = self.themeArray[1][1]
                    self.shape_color = self.themeArray[1][2]
                    self.accent_color = self.themeArray[1][3]
                    self.secondary_font_color = self.themeArray[1][4]
            except Exception as Message:
                self.error_message = "ThemeUtils > DetermineThemeColours > GetColours: "+str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)


        def GetThemeGUI(self):
            try:
                Title = self.title_font.render(
                    "Pycraft",
                    True,
                    self.font_color)
                TitleWidth = Title.get_width()

                if self.platform == "Linux":
                    MiddleFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    SideFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 20)

                else:
                    MiddleFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    SideFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 20)

                mouse_button_down = False

                Name = SideFont.render(
                    "By Tom Jebbo",
                    self.aa,
                    self.font_color)
                NameHeight = Name.get_height()

                Version = SideFont.render(
                    f"Version: {self.version}",
                    self.aa,
                    self.font_color)
                VersionWidth = Version.get_width()
                VersionHeight = Version.get_height()

                DarkModeFont = MiddleFont.render(
                    "Dark",
                    True,
                    self.font_color)
                DarkModeFont_Width = DarkModeFont.get_width()
                DarkModeFont_Height = DarkModeFont.get_height()

                LightModeFont = MiddleFont.render(
                    "Light",
                    True,
                    self.font_color)
                LightModeFont_Width = LightModeFont.get_width()
                LightModeFont_Height = LightModeFont.get_height()

                mouse_x = self.real_window_width/2
                mouse_y = self.real_window_height/2

                while True:
                    if self.use_mouse_input is False:
                        mouse_x, mouse_y = mouse_x+self.joystick_mouse[0], mouse_y+self.joystick_mouse[1]
                        self.mod_pygame__.mouse.set_pos(
                            mouse_x,
                            mouse_y)

                    else:
                        self.joystick_confirm = False

                    if self.use_mouse_input:
                        mouse_x, mouse_y = self.mod_pygame__.mouse.get_pos()

                    self.mod_caption_utils__.GenerateCaptions.GetNormalCaption(
                        self,
                        "Theme Selector")

                    self.real_window_width = self.mod_pygame__.display.get_window_size()[0]
                    self.real_window_height = self.mod_pygame__.display.get_window_size()[1]

                    LightRect = self.mod_pygame__.Rect(
                        0,
                        100,
                        self.real_window_width/2,
                        self.real_window_height-200)

                    DarkRect = self.mod_pygame__.Rect(
                        self.real_window_width/2,
                        100,
                        self.real_window_width/2,
                        self.real_window_height-200)

                    self.display.fill(self.background_color)

                    Name = SideFont.render(
                        "By Tom Jebbo",
                        self.aa,
                        self.font_color)
                    NameHeight = Name.get_height()

                    Version = SideFont.render(
                        f"Version: {self.version}",
                        self.aa,
                        self.font_color)
                    VersionWidth = Version.get_width()
                    VersionHeight = Version.get_height()

                    Title = self.title_font.render(
                        "Pycraft",
                        True,
                        self.font_color)
                    TitleWidth = Title.get_width()

                    self.display.blit(
                        Title,
                        ((self.real_window_width-TitleWidth)/2, 0))

                    self.display.blit(
                        Name,
                        (0, (self.real_window_height-NameHeight)))

                    self.display.blit(
                        Version,
                        ((self.real_window_width-VersionWidth)-2,
                            (self.real_window_height-VersionHeight)))

                    self.theme = "light"
                    self.mod_theme_utils__.DetermineThemeColours.GetColours(self)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.background_color,
                        LightRect)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        LightRect,
                        3)

                    LightModeFont = MiddleFont.render(
                        "Light",
                        True,
                        self.font_color)
                    LightModeFont_Width = LightModeFont.get_width()
                    LightModeFont_Height = LightModeFont.get_height()

                    self.display.blit(
                        LightModeFont,
                        (((self.real_window_width/2)-LightModeFont_Width)/2,
                            (self.real_window_height-LightModeFont_Height)/2))

                    self.theme = "dark"
                    self.mod_theme_utils__.DetermineThemeColours.GetColours(self)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.background_color,
                        DarkRect)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        DarkRect,
                        3)

                    DarkModeFont = MiddleFont.render(
                        "Dark",
                        True,
                        self.font_color)
                    DarkModeFont_Width = DarkModeFont.get_width()
                    DarkModeFont_Height = DarkModeFont.get_height()

                    self.display.blit(
                        DarkModeFont,
                        (((self.real_window_width+(self.real_window_width/2))-DarkModeFont_Width)/2,
                            (self.real_window_height-DarkModeFont_Height)/2))

                    if mouse_y >= 100 and mouse_y <= self.real_window_height-100:
                        if mouse_x <= self.real_window_width/2:
                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.accent_color,
                                LightRect,
                                1)

                            self.theme = "light"

                            if mouse_button_down:
                                if self.sound:
                                    self.mod_sound_utils__.PlaySound.PlayClickSound(self)
                                break

                        elif mouse_x >= self.real_window_width/2:
                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.accent_color,
                                DarkRect,
                                1)

                            self.theme = "dark"
                            if mouse_button_down:
                                if self.sound:
                                    self.mod_sound_utils__.PlaySound.PlayClickSound(self)
                                break

                        self.mod_theme_utils__.DetermineThemeColours.GetColours(self)

                    Choice = SideFont.render(
                        "".join((f"You have selected the {self.theme} ",
                                 "theme, you can change this later in settings")),

                        self.aa,
                        self.font_color)
                    ChoiceWidth = Choice.get_width()

                    self.display.blit(
                        Choice,
                        ((self.real_window_width-ChoiceWidth)/2,
                            (self.real_window_height-NameHeight)))

                    for event in self.mod_pygame__.event.get():
                        if event.type == self.mod_pygame__.QUIT:
                            self.stop_thread_event.set()

                            self.thread_start_long_thread.join()
                            self.thread_adaptive_mode.join()
                            self.thread_start_long_thread.join()

                            self.mod_pygame__.quit()
                            self.mod_sys__.exit()

                        if event.type == self.mod_pygame__.MOUSEBUTTONDOWN:
                            mouse_button_down = True

                        if event.type == self.mod_pygame__.MOUSEBUTTONUP:
                            mouse_button_down = False

                    self.mod_pygame__.display.update()
                    self.clock.tick(self.FPS)
            except Exception as Message:
                self.error_message = "".join(("ThemeUtils > DetermineThemeColours ",
                                             f"> GetThemeGUI: {str(Message)}"))

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
