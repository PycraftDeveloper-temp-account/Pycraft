if __name__ != "__main__":
    print("Started <Pycraft_CaptionUtils>")

    class GenerateCaptions:
        def __init__(self):
            pass

        def GetLoadingCaption(self, num):
            try:
                if num == 0:
                    self.mod_pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (-)")
                elif num == 1:
                    self.mod_pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (\)")
                elif num == 2:
                    self.mod_pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (|)")
                elif num == 3:
                    self.mod_pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (/)")
                else:
                    self.mod_pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading")
                self.mod_pygame__.display.update()
            except Exception as Message:
                self.error_message = "".join(("CaptionUtils > GenerateCaptions ",
                                             f"> GetLoadingCaption: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)


        def GetNormalCaption(self, location):
            try:
                if self.devmode >= 5 and self.devmode <= 9:
                    self.mod_pygame__.display.set_caption(
                        "".join((f"Pycraft: v{self.version}: {location}",
                                 " | ",
                                 f"you are: {10-self.devmode} steps away from being a developer")))

                elif self.devmode == 10:
                    hours = int((self.play_time/60)/60)
                    minutes = int(self.play_time/60)
                    seconds = int(self.play_time)

                    Position = f"{round(self.x, 2)}, {round(self.y, 2)}, {round(self.z, 2)}"
                    Velocity = f"{self.total_move_x}, {self.total_move_y}, {self.total_move_z}"

                    time = f"{hours} : {minutes} : {seconds}"

                    if self.FPS_overclock:
                        try:
                            FPS = "".join((f"FPS: 2000 eFPS: {int(self.eFPS)} ",
                                           f"aFPS: N/A iteration: {self.iteration} | "))

                            self.mod_pygame__.display.set_caption(
                                "".join((f"Pycraft: v{self.version}: {location} | ",
                                         "Dev Mode | ",
                                         f"Play Time: {time} | ",
                                         f"Pos: {Position} | ",
                                         f"V: {Velocity} | ",
                                         FPS,
                                         f"MemUsE: {int(self.current_memory_usage)}% | ",
                                         f"CPUUsE: {self.mod_psutil__.cpu_percent()}% | ",
                                         f"Theme: {self.theme} | ",
                                         f"Thread Count: {self.mod_threading__.active_count()}")))

                        except:
                            FPS = f"FPS: 2000 eFPS: NaN* aFPS: N/A iteration: {self.iteration} | "

                            self.mod_pygame__.display.set_caption(
                                "".join((f"Pycraft: v{self.version}: {location} | ",
                                         "Dev Mode | ",
                                         f"Play Time: {time} | ",
                                         f"Pos: {Position} | ",
                                         f"V: {Velocity} | ",
                                         FPS,
                                         f"MemUsE: {int(self.current_memory_usage)}% | ",
                                         f"CPUUsE: {self.mod_psutil__.cpu_percent()}% | ",
                                         f"Theme: {self.theme} | ",
                                         f"Thread Count: {self.mod_threading__.active_count()}")))

                    else:
                        FPS = "".join((f"FPS: {self.FPS} eFPS: {int(self.eFPS)} ",
                                       f"aFPS: {int(self.aFPS/self.iteration)} ",
                                       f"iteration: {self.iteration} | "))

                        self.mod_pygame__.display.set_caption(
                            "".join((f"Pycraft: v{self.version}: {location} | ",
                                     "Dev Mode | ",
                                     f"Play Time: {time} | ",
                                     f"Pos: {Position} | ",
                                     f"V: {Velocity} | ",
                                     FPS,
                                     f"MemUsE: {int(self.current_memory_usage)}% | ",
                                     f"CPUUsE: {self.mod_psutil__.cpu_percent()}% | ",
                                     f"Theme: {self.theme} | ",
                                     f"Thread Count: {self.mod_threading__.active_count()}")))

                else:
                    self.mod_pygame__.display.set_caption(f"Pycraft: v{self.version}: {location}")
            except Exception as Message:
                self.error_message = "".join(("CaptionUtils > GenerateCaptions ",
                                             f"> GetNormalCaption: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)


        def GetOpenGLCaption(self, GameData):
            try:
                if self.devmode >= 5 and self.devmode <= 9:
                    GameData.wnd.title = "".join((f"Pycraft: v{self.version}: Playing | ",
                                                  f"you are: {10-self.devmode} steps ",
                                                  "away from being a developer"))

                elif self.devmode == 10:
                    time_seconds = int(self.play_time)
                    time_minutes = int(self.play_time/60)
                    time_hours = int((self.play_time/60)/60)

                    minutes = time_minutes-(60*time_hours)
                    seconds = time_seconds-(60*time_minutes)

                    time = f"{time_hours} : {minutes} : {seconds}"

                    play_time = "".join((f"Play Time: {time} Game Time: ",
                                        f"{round(GameData.Time_Percent, 1)} ",
                                        f": {GameData.day-1} | "))

                    Position = "".join((f"Pos: {round(self.x, 2)}, ",
                                        f"{round(self.y, 2)}, ",
                                        f"{round(self.z, 2)} | "))

                    Velocity = "".join((f"V: {self.total_move_x}, ",
                                        f"{self.total_move_y}, ",
                                        f"{self.total_move_z} | "))

                    MemUse = f"MemUsE: {int(self.current_memory_usage)}% | "

                    CPUUsE = f"CPUUsE: {self.mod_psutil__.cpu_percent()}% | "

                    ThreadCount = f"Thread Count: {self.mod_threading__.active_count()}"

                    if self.FPS_overclock:
                        try:
                            FPS = "".join((f"FPS: 2000 eFPS: {int(self.eFPS)} ",
                                           f"aFPS: N/A iteration: {self.iteration} | "))

                            GameData.wnd.title = "".join((f"Pycraft: v{self.version}: Playing ",
                                                          "| Dev Mode | ",
                                                          play_time,
                                                          f"Weather: {GameData.weather} | ",
                                                          Position,
                                                          Velocity,
                                                          FPS,
                                                          MemUse,
                                                          CPUUsE,
                                                          ThreadCount))
                        except:
                            FPS = f"FPS: 2000 eFPS: NaN* aFPS: N/A iteration: {self.iteration} | "

                            GameData.wnd.title = "".join((f"Pycraft: v{self.version}: Playing ",
                                                          "| Dev Mode | ",
                                                          play_time,
                                                          f"Weather: {GameData.weather} | ",
                                                          Position,
                                                          Velocity,
                                                          FPS,
                                                          MemUse,
                                                          CPUUsE,
                                                          ThreadCount))
                    else:
                        try:
                            FPS = "".join((f"FPS: {self.FPS} eFPS: ",
                                    f"{int(self.eFPS)} aFPS: ",
                                    f"{int(self.aFPS/self.iteration)} ",
                                    f"iteration: {self.iteration} | "))

                            GameData.wnd.title = "".join((f"Pycraft: v{self.version}: Playing ",
                                                          "| Dev Mode | ",
                                                          play_time,
                                                          f"Weather: {GameData.weather} | ",
                                                          Position,
                                                          Velocity,
                                                          FPS,
                                                          MemUse,
                                                          CPUUsE,
                                                          ThreadCount))

                        except:
                            FPS = "".join((f"FPS: {self.FPS} eFPS: ",
                                    f"{int(self.eFPS)} aFPS: ",
                                    f"{int(self.aFPS/self.iteration)} ",
                                    f"iteration: {self.iteration} | "))

                            GameData.wnd.title = "".join((f"Pycraft: v{self.version}: Playing ",
                                                          "| Dev Mode | ",
                                                          play_time,
                                                          f"Weather: {GameData.weather} | ",
                                                          Position,
                                                          Velocity,
                                                          FPS,
                                                          MemUse,
                                                          CPUUsE,
                                                          ThreadCount))
                else:
                    GameData.wnd.title = f"Pycraft: v{self.version}: Playing"
            except Exception as Message:
                self.error_message = "".join(("CaptionUtils > GenerateCaptions ",
                                             f"> GetNormalCaption: {str(Message)}"))

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
