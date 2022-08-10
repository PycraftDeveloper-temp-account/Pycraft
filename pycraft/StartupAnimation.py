if __name__ != "_main_":
    print("Started <Pycraft_StartupAnimation>")

    class GenerateStartupScreen:
        def _init_(self):
            pass

        def Start(self):
            try:
                if self.platform == "Linux":
                    PresentsFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 35)

                    PycraftFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 60)

                    NameFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 45)

                else:
                    PresentsFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 35)

                    PycraftFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 60)

                    NameFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 45)

                NameText = NameFont.render(
                    "PycraftDev",
                    True,
                    self.font_color)
                NameTextWidth = NameText.get_width()
                NameTextHeight = NameText.get_height()

                self.real_window_width, self.real_window_height = self.mod_pygame__.display.get_window_size()

                self.display.fill(self.background_color)
                self.mod_pygame__.display.flip()
                self.mod_pygame__.display.set_caption(f"Pycraft: v{self.version}: Welcome")

                PresentsText = PresentsFont.render(
                    "presents",
                    True,
                    self.font_color)

                presentOffSet = 39

                PycraftText = PycraftFont.render(
                    "Pycraft",
                    True,
                    self.font_color)
                TitleTextWidth = PycraftText.get_width()

                PycraftStartPos = self.mod_pygame__.Vector2(
                    ((self.real_window_width-TitleTextWidth)/2,
                        self.real_window_height/2 - NameTextHeight))

                PycraftEndPos = self.mod_pygame__.Vector2(
                    PycraftStartPos.x,
                    0)

                self.clock = self.mod_pygame__.time.Clock()

                InterpolateSpeed = 0.02

                timer = 2

                if (self.current_date != self.last_run) or self.crash or self.run_full_startup:
                    self.animate_logo = False

                else:
                    self.animate_logo = True

                while timer > 0 and self.run_full_startup:
                    for event in self.mod_pygame__.event.get():
                        if (event.type == self.mod_pygame__.QUIT or
                                (event.type == self.mod_pygame__.KEYDOWN and
                                    event.key == self.mod_pygame__.K_ESCAPE)):

                            self.joystick_exit = False
                            if self.sound:
                                self.mod_sound_utils__.PlaySound.PlayClickSound(self)

                            self.mod_pygame__.quit()
                            self.mod_sys__.exit()

                    self.display.fill(self.background_color)

                    timer -= 0.01

                    self.display.blit(
                        NameText,
                        ((self.real_window_width-NameTextWidth)/2,
                            self.real_window_height/2 - NameTextHeight))

                    if timer <= 1:
                        self.display.blit(
                            PresentsText,
                            ((self.real_window_width-NameTextWidth)/2 + presentOffSet,
                                self.real_window_height/2 + NameTextHeight - 77))

                    self.clock.tick(60)
                    self.mod_pygame__.display.flip()

                Thread_ResourceCheck = self.mod_threading__.Thread(
                    target=self.mod_pycraft_startup_test__.StartupTest.PycraftResourceTest,
                    args=(self,))
                Thread_ResourceCheck.name = "Thread_ResourceCheck"
                Thread_ResourceCheck.start()

                runtimer = 0

                progress_line = [(100, self.real_window_height-100),
                                 (100, self.real_window_height-100)]

                while True:
                    if not self.resource_check_time[1] == 0:
                        calculation = ((self.real_window_width-200)/self.resource_check_time[1])
                        calculation = (calculation*runtimer)+100

                        if calculation > self.real_window_width-100:
                            calculation = self.real_window_width-100

                        progress_line.append(
                            (calculation,
                             self.real_window_height-100))

                    RefreshTime = self.mod_time__.perf_counter()
                    for event in self.mod_pygame__.event.get():
                        if (event.type == self.mod_pygame__.QUIT or
                                (event.type == self.mod_pygame__.KEYDOWN and
                                    event.key == self.mod_pygame__.K_ESCAPE)):

                            self.joystick_exit = False
                            if self.sound:
                                self.mod_sound_utils__.PlaySound.PlayClickSound(self)

                            self.mod_pygame__.quit()
                            self.mod_sys__.exit()

                    if self.use_mouse_input is False:
                        if self.joystick_exit:
                            self.joystick_exit = False
                            if self.sound:
                                self.mod_sound_utils__.PlaySound.PlayClickSound(self)

                            self.mod_pygame__.quit()
                            self.mod_sys__.exit()

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

                    self.real_window_width = self.mod_pygame__.display.get_window_size()[0]
                    self.real_window_height = self.mod_pygame__.display.get_window_size()[1]

                    self.display.fill(self.background_color)

                    if ((self.animate_logo or
                            self.resource_check_time[0] <= 0) and
                            "Thread_ResourceCheck" not in str(self.mod_threading__.enumerate())):

                        PycraftStartPos = self.mod_pygame__.math.Vector2.lerp(
                            PycraftStartPos,
                            PycraftEndPos,
                            InterpolateSpeed)

                    else:
                        if self.resource_check_time[1] >= 1:
                            self.mod_pygame__.draw.lines(
                                self.display,
                                self.shape_color,
                                self.aa,
                                [(100, self.real_window_height-100),
                                    (self.real_window_width-100,
                                        self.real_window_height-100)],
                                3)

                            self.mod_pygame__.draw.lines(
                                self.display,
                                self.accent_color,
                                self.aa,
                                progress_line)

                    self.display.blit(
                        PycraftText,
                        (PycraftStartPos.x, PycraftStartPos.y))

                    self.mod_pygame__.display.flip()
                    self.clock.tick(60)

                    if PycraftStartPos.y <= 1:
                        PycraftStartPos = PycraftEndPos
                        self.run_full_startup = False
                        break

                    runtimer += self.mod_time__.perf_counter()-RefreshTime

                if self.current_resource_check_time > 0:
                    self.resource_check_time[0] += 1
                    self.resource_check_time[1] += self.current_resource_check_time
                    self.resource_check_time[1] = self.resource_check_time[1]/self.resource_check_time[0]

            except Exception as Message:
                print(Message)
                self.error_message = "".join(("StartupAnimation > GenerateStartupScreen ",
                                             f"> Start: {str(Message)}"))

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
