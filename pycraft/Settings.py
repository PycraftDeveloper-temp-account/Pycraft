if __name__ != "__main__":
    print("Started <Pycraft_Settings>")

    class GenerateSettings:
        def __init__(self):
            pass

        def settings(self):
            try:
                self.mod_caption_utils__.GenerateCaptions.GetNormalCaption(
                    self,
                    "Settings")

                if self.platform == "Linux":
                    VersionFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                    Infotitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 35)

                    LOWFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                    MEDIUMFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                    HIGHFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                    ADAPTIVEFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                    LightThemeFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                    DarkThemeFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                    DataFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                    SettingsInformationFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                else:
                    VersionFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                    Infotitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 35)

                    LOWFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                    MEDIUMFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                    HIGHFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                    ADAPTIVEFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                    LightThemeFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                    DarkThemeFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                    DataFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                    SettingsInformationFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                Tempmouse_x = 0

                scroll = 50

                FocusedOn = [False, None]
                MoveToPosition = [False,
                                  False,
                                  False,
                                  False,
                                  False]

                ChangeLine = []

                MenuSelector = 13
                LeftAndRight = 0

                while True:
                    StartTime = self.mod_time__.perf_counter()
                    Tempmouse_x = self.mouse_x

                    if self.use_mouse_input is False:
                        if (MenuSelector not in range(0, 2) or LeftAndRight == 0):
                            LeftAndRight = 0

                    if self.joystick_hat_pressed:
                        self.joystick_hat_pressed = False
                        if self.joystick_mouse[1] == "Down" and MenuSelector <= 13:
                            MenuSelector += 1
                            if MenuSelector == 14:
                                MenuSelector = 0
                                
                        if self.joystick_mouse[1] == "Up" and MenuSelector >= 0:
                            MenuSelector -= 1
                            if MenuSelector == -1:
                                MenuSelector = 13
                                
                        if self.joystick_mouse[0] == "Right":
                            LeftAndRight += 1
                            
                        if self.joystick_mouse[0] == "Left":
                            LeftAndRight -= 1

                    xScaleFact = self.real_window_width/1280

                    displayEvents = self.mod_display_utils__.display_functionality.core_display_functions(
                        self)

                    for event in displayEvents:
                        if event.type == self.mod_pygame__.MOUSEWHEEL and self.real_window_height <= 760:
                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_SIZENS)
                                if str(event.y)[0] == "-":
                                    scroll -= 5

                                else:
                                    scroll += 5

                        else:
                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_ARROW)

                    self.mod_caption_utils__.GenerateCaptions.GetNormalCaption(
                        self,
                        "Settings")

                    if scroll > 35:
                        scroll = 35
                    elif scroll < -40:
                        scroll = -40

                        if self.joystick_hat_pressed:
                            self.joystick_hat_pressed = False
                            if self.joystick_mouse[1] == "Down" and MenuSelector <= 13:
                                MenuSelector += 1
                                if MenuSelector == 14:
                                    MenuSelector = 0

                            if self.joystick_mouse[1] == "Up" and MenuSelector >= 0:
                                MenuSelector -= 1
                                if MenuSelector == -1:
                                    MenuSelector = 13

                            if self.joystick_mouse[0] == "Right":
                                LeftAndRight += 1

                            if self.joystick_mouse[0] == "Left":
                                LeftAndRight -= 1

                        if self.joystick_confirm:
                            self.mouse_button_down = True
                            self.joystick_confirm = False

                        else:
                            if self.joystick_confirm_toggle is False:
                                self.mouse_button_down = False

                    title_font = self.title_font.render(
                        "Pycraft",
                        self.aa,
                        self.font_color)
                    TitleWidth = title_font.get_width()

                    InfoFont = Infotitle_font.render(
                        "Settings",
                        self.aa,
                        self.secondary_font_color)

                    FPSFont = VersionFont.render(
                        "".join((f"FPS: Actual: {int(self.eFPS)} ",
                                 f"Max: {int(self.FPS)} ",
                                 f"Average: {int((self.aFPS/self.iteration))}")),
                        self.aa,
                        self.font_color)

                    FOVFont = VersionFont.render(
                        f"FOV: {self.FOV}",
                        self.aa,
                        self.font_color)

                    CamRotFont = VersionFont.render(
                        f"Camera Rotation Speed: {round(self.camera_angle_speed, 1)}",
                        self.aa,
                        self.font_color)

                    ModeFont = VersionFont.render(
                        "Mode;         ,                 ,            ,          .",
                        self.aa,
                        self.font_color)

                    AAFont = VersionFont.render(
                        f"Anti-Aliasing: {self.aa}",
                        self.aa,
                        self.font_color)

                    RenderFogFont = VersionFont.render(
                        f"Render Fog: {self.render_fog}",
                        self.aa,
                        self.font_color)

                    FancySkyFont = VersionFont.render(
                        f"Fancy Graphics: {self.fancy_graphics}",
                        self.aa,
                        self.font_color)

                    FancyParticleFont = VersionFont.render(
                        f"Fancy Particles: {self.fancy_particles}",
                        self.aa,
                        self.font_color)

                    SoundFont = VersionFont.render(
                        f"Sound: {self.sound}",
                        self.aa,
                        self.font_color)

                    if self.sound:
                        SoundVoltFont = VersionFont.render(
                            f"Sound Volume: {self.sound_volume}%",
                            self.aa,
                            self.font_color)

                    else:
                        SoundVoltFont = VersionFont.render(
                            f"Sound Volume: {self.sound_volume}%",
                            self.aa,
                            self.shape_color)

                    MusicFont = VersionFont.render(
                        f"Music: {self.music}",
                        self.aa,
                        self.font_color)

                    if self.music:
                        MusicVoltFont = VersionFont.render(
                            f"Music Volume: {self.music_volume}%",
                            self.aa,
                            self.font_color)

                    else:
                        MusicVoltFont = VersionFont.render(
                            f"Music Volume: {self.music_volume}%",
                            self.aa,
                            self.shape_color)

                    ThemeFont = VersionFont.render(
                        f"Theme:          ,          | Current Theme: {self.theme}",
                        self.aa,
                        self.font_color)

                    ToggleControllerSupportFont = VersionFont.render(
                        f"Enable controller support: {not self.use_mouse_input}",
                        self.aa,
                        self.font_color)

                    ThemeInformationFont = SettingsInformationFont.render(
                        "Gives you control over which theme you can use",
                        self.aa,
                        self.accent_color)

                    ModeInformationFont = SettingsInformationFont.render(
                        "".join(("Gives you 4 separate pre-sets for settings, ",
                                 "Adaptive mode will automatically adjust your settings")),
                        self.aa,
                        self.accent_color)

                    FPSInformationFont = SettingsInformationFont.render(
                        "".join(("Controls the maximum frame rate the game ",
                                 "will limit to, does not guarantee that FPS unfortunately")),
                        self.aa,
                        self.accent_color)

                    FOVInformationFont = SettingsInformationFont.render(
                        "Controls the FOV of the camera in-game",
                        self.aa,
                        self.accent_color)

                    CameraRotationSpeedInformationFont = SettingsInformationFont.render(
                        "Controls the rotation speed of the camera in-game (1 is low, 5 is high)",
                        self.aa,
                        self.accent_color)

                    AAInformationFont = SettingsInformationFont.render(
                        "".join(("Enables/Disables anti-aliasing in game and in ",
                                 "the GUI, will give you a minor performance ",
                                 "improvement, mainly for low powered devices")),
                        self.aa,
                        self.accent_color)

                    RenderFogInformationFont = SettingsInformationFont.render(
                        "".join(("Enables/Disables fog effects in game, for ",
                                 "a small performance benefit")),
                        self.aa,
                        self.accent_color)

                    fancy_graphicsInformationFont = SettingsInformationFont.render(
                        "".join(("Enables/Disables some graphical features, this ",
                                 "can result in better performance when turned off")),
                        self.aa,
                        self.accent_color)

                    FancyParticlesInformationFont = SettingsInformationFont.render(
                        "".join(("Enables/Disables particles in game as particles ",
                                 "can have a significant performance decrease")),
                        self.aa,
                        self.accent_color)

                    SoundInformationFont = SettingsInformationFont.render(
                        "".join(("Enables/Disables sound effects in game, ",
                                 "like for example the click sound and footsteps in game")),
                        self.aa,
                        self.accent_color)

                    SoundVolInformationFont = SettingsInformationFont.render(
                        "".join(("Controls the volume of the sound effects, ",
                                 "where 100% is maximum and 0% is minimum volume")),
                        self.aa,
                        self.accent_color)

                    MusicInformationFont = SettingsInformationFont.render(
                        "Enables/Disables music in game, like for example the GUI music",
                        self.aa,
                        self.accent_color)

                    MusicVolInformationFont = SettingsInformationFont.render(
                        "".join(("Controls the volume of the music, some effects ",
                                 "may not apply until the game reloads")),
                        self.aa,
                        self.accent_color)

                    ToggleControllerSupportInformationFont = SettingsInformationFont.render(
                        "".join(("Toggles the use of either keyboard and mouse or a ",
                                 "controller to control the mouse and interact with the GUI")),
                        self.aa,
                        self.accent_color)

                    self.display.fill(self.background_color)

                    FPS_rect = self.mod_pygame__.Rect(
                        50,
                        180+scroll,
                        450*xScaleFact,
                        10)

                    FOV_rect = self.mod_pygame__.Rect(
                        50,
                        230+scroll,
                        450*xScaleFact,
                        10)

                    CAM_rect = self.mod_pygame__.Rect(
                        50,
                        280+scroll,
                        450*xScaleFact,
                        10)

                    sound_rect = self.mod_pygame__.Rect(
                        50,
                        580+scroll,
                        450*xScaleFact,
                        10)

                    music_rect = self.mod_pygame__.Rect(
                        50,
                        680+scroll,
                        450*xScaleFact,
                        10)

                    aa_rect = self.mod_pygame__.Rect(
                        50,
                        330+scroll,
                        50,
                        10)

                    render_fog_Rect = self.mod_pygame__.Rect(
                        50,
                        380+scroll,
                        50,
                        10)

                    Fansky_Rect = self.mod_pygame__.Rect(
                        50,
                        430+scroll,
                        50,
                        10)

                    fancy_particles_Rect = self.mod_pygame__.Rect(
                        50,
                        480+scroll,
                        50,
                        10)

                    sound_Rect = self.mod_pygame__.Rect(
                        50,
                        530+scroll,
                        50,
                        10)

                    music_Rect = self.mod_pygame__.Rect(
                        50,
                        630+scroll,
                        50,
                        10)

                    Controller_Rect = self.mod_pygame__.Rect(
                        50,
                        730+scroll,
                        50,
                        10)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        FPS_rect,
                        0)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        FOV_rect,
                        0)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        CAM_rect,
                        0)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        sound_rect,
                        0)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        music_rect,
                        0)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        aa_rect,
                        0)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        render_fog_Rect,
                        0)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        Fansky_Rect,
                        0)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        fancy_particles_Rect,
                        0)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        sound_Rect,
                        0)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        music_Rect,
                        0)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        Controller_Rect,
                        0)

                    if self.mouse_button_down:
                        if ((self.mouse_y > 180+scroll and
                                    self.mouse_y < 190+scroll) or
                                (FocusedOn[0] and
                                    FocusedOn[1] == "FPS") or
                                (MenuSelector == 2 and
                                    self.use_mouse_input is False)):

                            FocusedOn = [True, "FPS"]
                            if self.use_mouse_input:
                                self.mouse_y = 185+scroll

                        else:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (int(self.FPS+45)*xScaleFact,
                                    185+scroll),
                                9)

                        if ((self.mouse_y > 230+scroll and
                                    self.mouse_y < 240+scroll) or
                                (FocusedOn[0] and
                                    FocusedOn[1] == "FOV") or
                                (MenuSelector == 3 and
                                    self.use_mouse_input is False)):

                            FocusedOn = [True, "FOV"]
                            if self.use_mouse_input:
                                self.mouse_y = 235+scroll

                        else:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (int(self.FOV*5)*xScaleFact,
                                    235+scroll),
                                9)

                        if ((self.mouse_y > 280+scroll and
                                    self.mouse_y < 290+scroll) or
                                (FocusedOn[0] and
                                    FocusedOn[1] == "CAS") or
                                (MenuSelector == 4 and
                                    self.use_mouse_input is False)):

                            FocusedOn = [True, "CAS"] # CAS = Camera Angle Speed
                            if self.use_mouse_input:
                                self.mouse_y = 285+scroll

                        else:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                ((int(self.camera_angle_speed*89)+45)*xScaleFact,
                                    285+scroll),
                                9)

                        if ((self.mouse_y > 580+scroll and
                                    self.mouse_y < 590+scroll and
                                    self.sound) or
                                (FocusedOn[0] and
                                    FocusedOn[1] == "SVL") or
                                (MenuSelector == 10 and
                                    self.use_mouse_input is False)):

                            FocusedOn = [True, "SVL"]
                            if self.use_mouse_input:
                                self.mouse_y = 585+scroll

                        else:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                ((int(self.sound_volume*4.4)+50)*xScaleFact,
                                    585+scroll),
                                9)

                        if ((self.mouse_y > 680+scroll and
                                    self.mouse_y < 690+scroll and
                                    self.music) or
                                (FocusedOn[0] and
                                    FocusedOn[1] == "MVL") or
                                (MenuSelector == 12 and
                                    self.use_mouse_input is False)):

                            FocusedOn = [True, "MVL"]
                            if self.use_mouse_input:
                                self.mouse_y = 685+scroll

                        else:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                ((int(self.music_volume*4.4)+50)*xScaleFact,
                                    685+scroll),
                                9)

                        if ((self.mouse_y > 330+scroll and
                                    self.mouse_y < 340+scroll) or
                                (MenuSelector == 5 and
                                    self.use_mouse_input is False)):

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            if self.aa:
                                self.aa = False
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                            elif self.aa is False:
                                self.aa = True
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                        if self.aa:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 335+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 335+scroll),
                                6)

                        elif self.aa is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 335+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 335+scroll),
                                6)

                        if ((self.mouse_y > 380+scroll and
                                    self.mouse_y < 390+scroll) or
                                (MenuSelector == 6 and
                                    self.use_mouse_input is False)):

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            if self.render_fog:
                                self.render_fog = False
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                            elif self.render_fog is False:
                                self.render_fog = True
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                        if self.render_fog:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 385+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 385+scroll),
                                6)

                        elif self.render_fog is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 385+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 385+scroll),
                                6)

                        if ((self.mouse_y > 430+scroll and
                                    self.mouse_y < 440+scroll) or
                                (MenuSelector == 7 and
                                    self.use_mouse_input is False)):

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            if self.fancy_graphics:
                                self.fancy_graphics = False
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                            elif self.fancy_graphics is False:
                                self.fancy_graphics = True
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                        if self.fancy_graphics:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 435+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 435+scroll),
                                6)

                        elif self.fancy_graphics is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 435+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 435+scroll),
                                6)

                        if ((self.mouse_y > 480+scroll and
                                    self.mouse_y < 490+scroll) or
                                (MenuSelector == 8 and
                                    self.use_mouse_input is False)):

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            if self.fancy_particles:
                                self.fancy_particles = False
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                            elif self.fancy_particles is False:
                                self.fancy_particles = True
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                        if self.fancy_particles:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 485+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 485+scroll),
                                6)

                        elif self.fancy_particles is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 485+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 485+scroll),
                                6)

                        if ((self.mouse_y > 530+scroll and
                                    self.mouse_y < 540+scroll) or
                                (MenuSelector == 9 and
                                    self.use_mouse_input is False)):

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            if self.sound:
                                self.sound = False
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                            elif self.sound is False:
                                self.sound = True
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                        if self.sound:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 535+scroll), 9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 535+scroll), 6)

                        elif self.sound is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 535+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 535+scroll),
                                6)

                        if ((self.mouse_y > 630+scroll and
                                    self.mouse_y < 640+scroll and
                                    self.use_mouse_input) or
                                (MenuSelector == 11 and
                                    self.use_mouse_input is False)):

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            if self.music:
                                self.music = False
                                self.mod_pygame__.mixer.music.fadeout(500)
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                            elif self.music is False:
                                self.music = True
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                        if self.music:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 635+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 635+scroll),
                                6)

                        elif self.music is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 635+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 635+scroll),
                                6)

                        if ((self.mouse_y > 730+scroll and
                                    self.mouse_y < 740+scroll and
                                    self.use_mouse_input) or
                                (MenuSelector == 13 and
                                    self.use_mouse_input is False)):

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            if self.use_mouse_input:
                                self.use_mouse_input = False
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                            elif self.use_mouse_input is False:
                                self.use_mouse_input = True
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.mouse_button_down = False

                        if not self.use_mouse_input:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 735+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 735+scroll),
                                6)

                        elif not self.use_mouse_input is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 735+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 735+scroll),
                                6)

                    else:
                        FocusedOn = [False, None]
                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_visible(True)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            (255, 255, 255),
                            ((int(self.sound_volume*4.4)+50)*xScaleFact,
                                585+scroll),
                            9)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            (255, 255, 255),
                            ((int(self.FPS+45)*xScaleFact),
                                185+scroll),
                            9)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            (255, 255, 255),
                            ((int(self.camera_angle_speed*89)+45)*xScaleFact,
                                285+scroll),
                            9)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            (255, 255, 255),
                            ((int(self.FOV*5))*xScaleFact,
                                235+scroll),
                            9)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            (255, 255, 255),
                            ((int(self.music_volume*4.4)+50)*xScaleFact,
                                685+scroll),
                            9)

                        if self.aa:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 335+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 335+scroll),
                                6)

                        elif self.aa is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 335+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 335+scroll),
                                6)

                        if self.render_fog:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 385+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 385+scroll),
                                6)

                        elif self.render_fog is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 385+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 385+scroll),
                                6)

                        if self.fancy_graphics:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 435+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 435+scroll),
                                6)

                        elif self.fancy_graphics is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 435+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 435+scroll),
                                6)

                        if self.fancy_particles:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 485+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 485+scroll),
                                6)

                        elif self.fancy_particles is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 485+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 485+scroll),
                                6)

                        if self.sound:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 535+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 535+scroll),
                                6)

                        elif self.sound is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 535+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 535+scroll),
                                6)

                        if self.music:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 635+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 635+scroll),
                                6)

                        elif self.music is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 635+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 635+scroll),
                                6)

                        if not self.use_mouse_input:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (90, 735+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (90, 735+scroll),
                                6)

                        elif not self.use_mouse_input is False:
                            self.mod_pygame__.draw.circle(
                                self.display,
                                (255, 255, 255),
                                (60, 735+scroll),
                                9)

                            self.mod_pygame__.draw.circle(
                                self.display,
                                self.shape_color,
                                (60, 735+scroll),
                                6)

                        if ((self.mouse_y > 330+scroll and
                                    self.mouse_y < 340+scroll and
                                    self.use_mouse_input) or
                                (MenuSelector == 5 and
                                    self.use_mouse_input is False)):

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            self.display.blit(
                                AAInformationFont,
                                (120, 325+scroll))

                            if self.aa:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.accent_color,
                                    (90, 335+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (90, 335+scroll),
                                    6)

                            elif self.aa is False:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.accent_color,
                                    (60, 335+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (60, 335+scroll),
                                    6)

                        if ((self.mouse_y > 380+scroll and
                                    self.mouse_y < 390+scroll and
                                    self.use_mouse_input) or
                                (MenuSelector == 6 and
                                    self.use_mouse_input is False)):

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            self.display.blit(
                                RenderFogInformationFont,
                                (120, 375+scroll))

                            if self.render_fog:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.accent_color,
                                    (90, 385+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (90, 385+scroll),
                                    6)

                            elif self.render_fog is False:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.accent_color,
                                    (60, 385+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (60, 385+scroll),
                                    6)

                        if ((self.mouse_y > 430+scroll and
                                    self.mouse_y < 440+scroll and
                                    self.use_mouse_input) or
                                (MenuSelector == 7 and
                                    self.use_mouse_input is False)):

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            self.display.blit(
                                fancy_graphicsInformationFont,
                                (120, 425+scroll))

                            if self.fancy_graphics:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.accent_color,
                                    (90, 435+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (90, 435+scroll),
                                    6)

                            elif self.fancy_graphics is False:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.accent_color,
                                    (60, 435+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (60, 435+scroll),
                                    6)


                        if ((self.mouse_y > 480+scroll and
                                    self.mouse_y < 490+scroll and
                                    self.use_mouse_input) or
                                (MenuSelector == 8 and
                                    self.use_mouse_input is False)):

                            self.display.blit(
                                FancyParticlesInformationFont,
                                (120, 475+scroll))

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            if self.fancy_particles:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.accent_color,
                                    (90, 485+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (90, 485+scroll),
                                    6)

                            elif self.fancy_particles is False:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.accent_color,
                                    (60, 485+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (60, 485+scroll),
                                    6)

                        if ((self.mouse_y > 530+scroll and
                                    self.mouse_y < 540+scroll and
                                    self.use_mouse_input) or
                                (MenuSelector == 9 and
                                 self.use_mouse_input is False)):

                            self.display.blit(
                                SoundInformationFont,
                                (120, 525+scroll))

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            if self.sound:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.accent_color,
                                    (90, 535+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (90, 535+scroll),
                                    6)

                            elif self.sound is False:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.accent_color,
                                    (60, 535+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (60, 535+scroll),
                                    6)

                        if ((self.mouse_y > 630+scroll and
                                    self.mouse_y < 640+scroll and
                                    self.use_mouse_input) or
                                (MenuSelector == 11 and
                                    self.use_mouse_input is False)):

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            self.display.blit(
                                MusicInformationFont,
                                (120, 625+scroll))

                            if self.music:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.accent_color,
                                    (90, 635+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (90, 635+scroll),
                                    6)

                            elif self.music is False:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.accent_color,
                                    (60, 635+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (60, 635+scroll),
                                    6)

                        if ((self.mouse_y > 730+scroll and
                                    self.mouse_y < 740+scroll and
                                    self.use_mouse_input) or
                                (MenuSelector == 13 and
                                    self.use_mouse_input is False)):

                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND)

                            self.display.blit(
                                ToggleControllerSupportInformationFont,
                                (120, 725+scroll))

                            if not self.use_mouse_input:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    (255, 255, 255),
                                    (90, 735+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (90, 735+scroll),
                                    6)

                            elif not self.use_mouse_input is False:
                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    (255, 255, 255),
                                    (60, 735+scroll),
                                    9)

                                self.mod_pygame__.draw.circle(
                                    self.display,
                                    self.shape_color,
                                    (60, 735+scroll),
                                    6)

                    if ((self.mouse_y >= 65+scroll and
                                self.mouse_y <= 75+scroll) or
                            (MenuSelector == 0 and
                                self.use_mouse_input is False)):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                        self.display.blit(
                            ThemeInformationFont,
                            (300, 67+scroll))

                    if ((self.mouse_y >= 65+scroll and
                                self.mouse_y <= 75+scroll and
                                self.mouse_x >= 55 and
                                self.mouse_x <= 95) or
                            (MenuSelector == 0 and
                                self.use_mouse_input is False and
                                LeftAndRight == 0)):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                        LightTheme = LightThemeFont.render(
                            "Light",
                            self.aa,
                            self.accent_color)
                        LightThemeFont.set_underline(True)

                        if self.mouse_button_down:
                            self.theme = "light"
                            self.mod_theme_utils__.determine_theme_colours.get_colors(self)
                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)

                            self.mouse_button_down = False

                    else:
                        if (self.use_mouse_input is False and
                                LeftAndRight < 0 and
                                MenuSelector == 0):

                            LeftAndRight = 1

                        LightTheme = LightThemeFont.render(
                            "Light",
                            self.aa,
                            self.font_color)
                        LightThemeFont.set_underline(False)

                    if ((self.mouse_y >= 65+scroll and
                                self.mouse_y <= 75+scroll and
                                self.mouse_x >= 95 and
                                self.mouse_x <= 135) or
                            (MenuSelector == 0 and
                                self.use_mouse_input is False and
                                LeftAndRight == 1)):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                        DarkTheme = DarkThemeFont.render(
                            "Dark",
                            self.aa,
                            self.accent_color)
                        DarkThemeFont.set_underline(True)

                        if self.mouse_button_down:
                            self.theme = "dark"
                            self.mod_theme_utils__.determine_theme_colours.get_colors(self)
                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)

                            self.mouse_button_down = False

                    else:
                        if (self.use_mouse_input is False and
                                LeftAndRight > 1 and
                                MenuSelector == 0):

                            LeftAndRight = 0

                        DarkTheme = DarkThemeFont.render(
                            "Dark",
                            self.aa,
                            self.font_color)
                        DarkThemeFont.set_underline(False)

                    if ((self.mouse_y >= 85+scroll and
                                self.mouse_y <= 95+scroll) or
                            (MenuSelector == 1 and
                                self.use_mouse_input is False)):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                        self.display.blit(
                            ModeInformationFont,
                            (300, 85+scroll))

                    if ((self.mouse_y > 680+scroll and
                                self.mouse_y < 690+scroll and
                                self.use_mouse_input) or
                            (MenuSelector == 12 and
                                self.use_mouse_input is False)):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                        self.display.blit(
                            MusicVolInformationFont,
                            (520*xScaleFact, 675+scroll))

                    if ((self.mouse_y > 580+scroll and
                                self.mouse_y < 590+scroll and
                                self.use_mouse_input) or
                            (MenuSelector == 10 and
                                self.use_mouse_input is False)):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                        self.display.blit(
                            SoundVolInformationFont,
                            (520*xScaleFact, 575+scroll))

                    if ((self.mouse_y > 280+scroll and
                                self.mouse_y < 290+scroll and
                                self.use_mouse_input) or
                            (MenuSelector == 4 and
                                self.use_mouse_input is False)):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                        self.display.blit(
                            CameraRotationSpeedInformationFont,
                            (520*xScaleFact, 275+scroll))

                    if ((self.mouse_y > 230+scroll and
                                self.mouse_y < 240+scroll and
                                self.use_mouse_input) or
                            (MenuSelector == 3 and
                                self.use_mouse_input is False)):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                        self.display.blit(
                            FOVInformationFont,
                            (520*xScaleFact, 225+scroll))

                    if ((self.mouse_y > 180+scroll and
                                self.mouse_y < 190+scroll and
                                self.use_mouse_input) or
                            (MenuSelector == 2 and
                                self.use_mouse_input is False)):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                        self.display.blit(
                            FPSInformationFont,
                            (520*xScaleFact, 175+scroll))

                    if ((self.mouse_y >= 85+scroll and
                                self.mouse_y <= 95+scroll and
                                self.mouse_x >= 40 and
                                self.mouse_x <= 80) or
                            (MenuSelector == 1 and
                                self.use_mouse_input is False and
                                LeftAndRight == 0)):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                        LOWtFont = LOWFont.render(
                            "Low",
                            self.aa,
                            self.accent_color)
                        LOWFont.set_underline(True)

                        if self.mouse_button_down:
                            self.settings_preference = "Low"
                            self.FPS = 15
                            self.aa = False
                            self.render_fog = False
                            self.fancy_graphics = False
                            self.fancy_particles = False
                            self.mouse_button_down = False

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)

                            self.aFPS = (self.aFPS/self.iteration)
                            self.iteration = 1

                    else:
                        if (self.use_mouse_input is False and
                                LeftAndRight < 0 and
                                MenuSelector == 1):

                            LeftAndRight = 1

                        LOWtFont = LOWFont.render(
                            "Low",
                            self.aa,
                            self.font_color)
                        LOWFont.set_underline(False)

                    if ((self.mouse_y >= 85+scroll and
                                self.mouse_y <= 95+scroll and
                                self.mouse_x >= 90 and
                                self.mouse_x <= 155) or
                            (MenuSelector == 1 and
                                self.use_mouse_input is False and
                                LeftAndRight == 1)):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                        MEDIUMtFont = MEDIUMFont.render(
                            "Medium",
                            self.aa,
                            self.accent_color)
                        MEDIUMFont.set_underline(True)

                        if self.mouse_button_down:
                            self.settings_preference = "Medium"
                            self.FPS = 30
                            self.aa = True
                            self.render_fog = False
                            self.fancy_graphics = True
                            self.fancy_particles = False

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)

                            self.mouse_button_down = False
                            self.aFPS = (self.aFPS/self.iteration)
                            self.iteration = 1

                    else:
                        MEDIUMtFont = MEDIUMFont.render(
                            "Medium",
                            self.aa,
                            self.font_color)
                        MEDIUMFont.set_underline(False)

                    if ((self.mouse_y >= 85+scroll and
                                self.mouse_y <= 95+scroll and
                                self.mouse_x >= 165 and
                                self.mouse_x <= 205) or
                            (MenuSelector == 1 and
                                self.use_mouse_input is False and LeftAndRight == 2)):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                        HIGHFontText = HIGHFont.render(
                            "High",
                            self.aa,
                            self.accent_color)

                        HIGHFont.set_underline(True)

                        if self.mouse_button_down:
                            self.settings_preference = "High"
                            self.FPS = 60
                            self.aa = True
                            self.render_fog = True
                            self.fancy_graphics = True
                            self.fancy_particles = True

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)

                            self.mouse_button_down = False
                            self.aFPS = (self.aFPS/self.iteration)
                            self.iteration = 1

                    else:
                        HIGHFontText = HIGHFont.render(
                            "High",
                            self.aa,
                            self.font_color)

                        HIGHFont.set_underline(False)

                    if ((self.mouse_y >= 85+scroll and
                                self.mouse_y <= 95+scroll and
                                self.mouse_x >= 215 and
                                self.mouse_x <= 300) or
                            (MenuSelector == 1 and
                                self.use_mouse_input is False and
                                LeftAndRight == 3)):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                        ADAPTIVEtFont = ADAPTIVEFont.render(
                            "Adaptive",
                            self.aa,
                            self.accent_color)
                        ADAPTIVEFont.set_underline(True)

                        if self.mouse_button_down:
                            self.settings_preference = "Adaptive"
                            self.FPS = (self.mod_psutil__.cpu_freq(percpu=True)[0][2])/35

                            CPU_Freq = (self.mod_psutil__.cpu_freq(percpu=True)[0][2])/10
                            MEM_Total = self.mod_psutil__.virtual_memory().total

                            if (CPU_Freq > 300 and
                                    MEM_Total > 8589934592):

                                self.aa = True
                                self.RenderFog = True
                                self.fancy_graphics = True
                                self.fancy_particles = True

                            elif (CPU_Freq > 200 and
                                    MEM_Total > 4294967296):

                                self.aa = True
                                self.RenderFog = True
                                self.fancy_graphics = True
                                self.fancy_particles = False

                            elif (CPU_Freq > 100 and
                                    MEM_Total > 2147483648):

                                self.aa = False
                                self.RenderFog = False
                                self.fancy_graphics = True
                                self.fancy_particles = False

                            elif (CPU_Freq < 100 and
                                    CPU_Freq > 75 and
                                    MEM_Total > 1073741824):

                                self.aa = False
                                self.RenderFog = False
                                self.fancy_graphics = False
                                self.fancy_particles = False

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)

                            self.mouse_button_down = False

                    else:
                        if (self.use_mouse_input is False and
                                LeftAndRight > 3 and
                                MenuSelector == 1):

                            LeftAndRight = 0

                        ADAPTIVEtFont = ADAPTIVEFont.render(
                            "Adaptive",
                            self.aa,
                            self.font_color)
                        ADAPTIVEFont.set_underline(False)


                    if (FocusedOn[0] and
                            FocusedOn[1] == "FPS"):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_visible(False)

                        if self.mouse_x > Tempmouse_x and self.FPS < 445:
                            self.FPS += 1

                        elif self.mouse_x < Tempmouse_x and self.FPS > 15:
                            self.FPS -= 1

                        if self.FPS < 15:
                            self.FPS = 16

                        elif self.FPS > 445:
                            self.FPS = 444

                        if self.fancy_graphics:
                            ChangeLine.append(
                                (int(self.FPS+45)*xScaleFact,
                                 185+scroll))

                            if len(ChangeLine) >= 2:
                                self.mod_pygame__.draw.lines(
                                    self.display,
                                    self.accent_color,
                                    False,
                                    ChangeLine)

                        self.aFPS = (self.aFPS/self.iteration)
                        self.iteration = 1

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.accent_color,
                            (int(self.FPS+45)*xScaleFact,
                                185+scroll),
                            9)

                        MoveToPosition[0] = True

                    else:
                        if MoveToPosition[0]:
                            ChangeLine = []
                            self.mod_pygame__.mouse.set_pos(
                                (int(self.FPS+45)*xScaleFact),
                                185+scroll)

                            MoveToPosition[0] = False

                    if (FocusedOn[0] and
                            FocusedOn[1] == "FOV"):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_visible(False)

                        if self.mouse_x > Tempmouse_x and self.FOV < 98:
                            self.FOV += 1

                        elif self.mouse_x < Tempmouse_x and self.FOV > 12:
                            self.FOV -= 1

                        if self.FOV < 12:
                            self.FOV = 13

                        elif self.FOV > 98:
                            self.FOV = 97

                        if self.fancy_graphics:
                            ChangeLine.append(
                                (int(self.FOV*5)*xScaleFact,
                                    235+scroll))

                            if len(ChangeLine) >= 2:
                                self.mod_pygame__.draw.lines(
                                    self.display,
                                    self.accent_color,
                                    False,
                                    ChangeLine)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.accent_color,
                            (int(self.FOV*5)*xScaleFact,
                             235+scroll),
                            9)

                        MoveToPosition[1] = True

                    else:
                        if MoveToPosition[1]:
                            ChangeLine = []

                            self.mod_pygame__.mouse.set_pos(
                                (int(self.FOV*5)*xScaleFact),
                                235+scroll)

                            MoveToPosition[1] = False

                    if (FocusedOn[0] and FocusedOn[1] == "CAS"):
                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_visible(False)

                        if self.mouse_x > Tempmouse_x and self.camera_angle_speed < 5.0:
                            self.camera_angle_speed += 0.1

                        elif self.mouse_x < Tempmouse_x and self.camera_angle_speed > 0.0:
                            self.camera_angle_speed -= 0.1

                        if self.camera_angle_speed > 5.0:
                            self.camera_angle_speed = 4.9

                        elif self.camera_angle_speed <= 0:
                            self.camera_angle_speed = 0.1

                        if self.fancy_graphics:
                            ChangeLine.append(
                                ((int(self.camera_angle_speed*89)+45)*xScaleFact,
                                 285+scroll))

                            if len(ChangeLine) >= 2:
                                self.mod_pygame__.draw.lines(
                                    self.display,
                                    self.accent_color,
                                    False,
                                    ChangeLine)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.accent_color,
                            ((int(self.camera_angle_speed*89)+45)*xScaleFact,
                             285+scroll),
                            9)

                        MoveToPosition[2] = True

                    else:
                        if MoveToPosition[2]:
                            ChangeLine = []
                            self.mod_pygame__.mouse.set_pos(
                                ((int(self.camera_angle_speed*89)+45)*xScaleFact),
                                285+scroll)

                            MoveToPosition[2] = False

                    if (FocusedOn[0] and
                            FocusedOn[1] == "SVL"):

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_visible(False)

                        if self.mouse_x > Tempmouse_x and self.sound_volume < 100:
                            self.sound_volume += 1

                        elif self.mouse_x < Tempmouse_x and self.sound_volume > 0:
                            self.sound_volume -= 1

                        if self.sound_volume > 100:
                            self.sound_volume = 100

                        elif self.sound_volume < 0:
                            self.sound_volume = 0

                        if self.fancy_graphics:
                            ChangeLine.append(
                                ((int(self.sound_volume*4.4)+50)*xScaleFact,
                                 585+scroll))

                            if len(ChangeLine) >= 2:
                                self.mod_pygame__.draw.lines(
                                    self.display,
                                    self.accent_color,
                                    False,
                                    ChangeLine)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.accent_color,
                            ((int(self.sound_volume*4.4)+50)*xScaleFact,
                                585+scroll),
                            9)

                        MoveToPosition[3] = True

                    else:
                        if MoveToPosition[3]:
                            ChangeLine = []
                            self.mod_pygame__.mouse.set_pos(
                                ((int(self.sound_volume*4.4)+50)*xScaleFact),
                                585+scroll)

                            MoveToPosition[3] = False

                    if (FocusedOn[0] and FocusedOn[1] == "MVL"):
                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_visible(False)

                        if self.mouse_x > Tempmouse_x and self.music_volume < 100:
                            self.music_volume += 1

                        elif self.mouse_x < Tempmouse_x and self.music_volume > 0:
                            self.music_volume -= 1

                        if self.music_volume > 100:
                            self.music_volume = 100

                        elif self.music_volume < 0:
                            self.music_volume = 0

                        if self.fancy_graphics:
                            ChangeLine.append(
                                ((int(self.music_volume*4.4)+50)*xScaleFact,
                                 685+scroll))

                            if len(ChangeLine) >= 2:
                                self.mod_pygame__.draw.lines(
                                    self.display,
                                    self.accent_color,
                                    False,
                                    ChangeLine)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.accent_color,
                            ((int(self.music_volume*4.4)+50)*xScaleFact,
                             685+scroll),
                            9)

                        MoveToPosition[4] = True

                    else:
                        if MoveToPosition[4]:
                            ChangeLine = []
                            self.mod_pygame__.mouse.set_pos(
                                ((int(self.music_volume*4.4)+50)*xScaleFact),
                                685+scroll)

                            MoveToPosition[4] = False

                    self.display.blit(
                        FPSFont,
                        (0, 150+scroll))

                    self.display.blit(
                        FOVFont,
                        (0, 200+scroll))

                    self.display.blit(
                        CamRotFont,
                        (0, 250+scroll))

                    self.display.blit(
                        ModeFont,
                        (0, 85+scroll))

                    self.display.blit(
                        LOWtFont,
                        (48, 85+scroll))

                    self.display.blit(
                        MEDIUMtFont,
                        (90, 85+scroll))

                    self.display.blit(
                        HIGHFontText,
                        (165, 85+scroll))

                    self.display.blit(
                        ADAPTIVEtFont,
                        (215, 85+scroll))

                    self.display.blit(
                        AAFont,
                        (0, 300+scroll))

                    self.display.blit(
                        RenderFogFont,
                        (0, 350+scroll))

                    self.display.blit(
                        FancySkyFont,
                        (0, 400+scroll))

                    self.display.blit(
                        FancyParticleFont,
                        (0, 450+scroll))

                    self.display.blit(
                        SoundFont,
                        (0, 500+scroll))

                    self.display.blit(
                        SoundVoltFont,
                        (0, 550+scroll))

                    self.display.blit(
                        MusicFont,
                        (0, 600+scroll))

                    self.display.blit(
                        MusicVoltFont,
                        (0, 650+scroll))

                    self.display.blit(
                        ToggleControllerSupportFont,
                        (0, 700+scroll))

                    self.display.blit(
                        ThemeFont,
                        (0, 65+scroll))

                    self.display.blit(
                        LightTheme,
                        (55, 65+scroll))

                    self.display.blit(
                        DarkTheme,
                        (95, 65+scroll))

                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.shape_color,
                        (int(self.FPS+45)*xScaleFact,
                            185+scroll),
                        6)

                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.shape_color,
                        (int(self.FOV*5)*xScaleFact,
                            235+scroll),
                        6)

                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.shape_color,
                        ((int(self.camera_angle_speed*89)+45)*xScaleFact,
                            285+scroll),
                        6)

                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.shape_color,
                        ((int(self.sound_volume*4.4)+50)*xScaleFact,
                         585+scroll),
                        6)

                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.shape_color,
                        ((int(self.music_volume*4.4)+50)*xScaleFact,
                         685+scroll),
                        6)

                    cover_Rect = self.mod_pygame__.Rect(
                        0,
                        0,
                        1280,
                        100)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        (self.background_color),
                        cover_Rect)

                    self.display.blit(
                        title_font,
                        ((self.real_window_width-TitleWidth)/2, 0))

                    self.display.blit(
                        InfoFont,
                        (((self.real_window_width-TitleWidth)/2)+55, 50))

                    if self.real_window_height <= 760:
                        self.mod_pygame__.draw.line(
                            self.display,
                            self.shape_color,
                            (self.real_window_width-10, scroll+40),
                            (self.real_window_width-10, self.real_window_height+(scroll-40)+5),
                            1)

                        if self.use_mouse_input is False:
                            if MenuSelector >= 11 and scroll > -40:
                                scroll -= 5/(self.FPS/(self.aFPS/self.iteration))

                            if MenuSelector <= 5 and scroll < 50:
                                scroll += 5/(self.FPS/(self.aFPS/self.iteration))

                    else:
                        scroll = 50

                    self.mod_drawing_utils__.generate_graph.create_devmode_graph(
                        self,
                        DataFont)

                    if self.go_to is None:
                        self.mod_display_utils__.display_animations.fade_in(self)

                    else:
                        self.mod_display_utils__.display_animations.fade_out(
                            self)

                    if self.startup_animation is False and (self.go_to is not None):
                        return None

                    self.mod_pygame__.display.flip()
                    self.clock.tick(
                        self.mod_display_utils__.display_utils.get_play_status(self))

                    self.run_timer += self.mod_time__.perf_counter()-StartTime

                    if self.error_message is not None:
                        self.error_message = "".join(("Settings > GenerateSettings ",
                                                     f"> settings: {str(self.error_message)}"))

                        self.error_message_detailed = "".join(
                            self.mod_traceback__.format_exception(
                                None,
                                Message,
                                Message.__traceback__))

                        self.mod_error_utils__.generate_error_screen.error_screen(self)

            except Exception as Message:
                self.error_message = "Settings > GenerateSettings > settings: "+str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

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
