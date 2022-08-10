if __name__ != "__main__":
    print("Started <Pycraft_Achievements>")

    class GenerateAchievements:
        def __init__(self):
            pass

        def Achievements(self):
            try:
                self.mod_caption_utils__.GenerateCaptions.GetNormalCaption(
                    self,
                    "Achievements")

                if self.platform == "Linux":
                    Infotitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 35)

                    DataFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 15)
                else:
                    Infotitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 35)

                    DataFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 15)

                title_font = self.title_font.render(
                    "Pycraft",
                    self.aa,
                    self.font_color)

                TitleWidth = title_font.get_width()

                AchievementsFont = Infotitle_font.render(
                    "Achievements",
                    self.aa,
                    self.secondary_font_color)

                while True:
                    StartTime = self.mod_time__.perf_counter()

                    displayEvents = self.mod_display_utils__.displayFunctionality.core_display_functions(
                        self)

                    self.mod_caption_utils__.GenerateCaptions.GetNormalCaption(
                        self,
                        "Achievements")

                    self.display.fill(self.background_color)

                    cover_Rect = self.mod_pygame__.Rect(
                        0,
                        0,
                        1280,
                        90)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.background_color,
                        cover_Rect)

                    self.display.blit(
                        title_font,
                        ((self.real_window_width-TitleWidth)/2, 0))

                    self.display.blit(
                        AchievementsFont,
                        (((self.real_window_width-TitleWidth)/2)+55, 50))

                    self.mod_drawing_utils__.GenerateGraph.create_devmode_graph(
                        self,
                        DataFont)

                    if self.go_to is None:
                        self.mod_display_utils__.displayAnimations.FadeIn(self)
                    else:
                        self.mod_display_utils__.displayAnimations.FadeOut(self)

                    if not self.startup_animation and (self.go_to is not None):
                        return None

                    self.mod_pygame__.display.flip()
                    self.clock.tick(
                        self.mod_display_utils__.displayUtils.GetPlayStatus(self))

                    if self.error_message is not None:
                        self.error_message = "".join(
                            ("Achievements > GenerateAchievements > Achievements: ",
                             str(self.error_message)))

                        return

                    self.run_timer += self.mod_time__.perf_counter()-StartTime
            except Exception as Message:
                self.error_message = (
                    f"Achievements > GenerateAchievements > Achievements: {str(Message)}")

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
