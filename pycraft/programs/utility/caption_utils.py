if __name__ != "__main__":
    try:
        import threading
        
        import pygame
        import psutil
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
            
    class generate_captions:
        """
            NYI
            
            - Args:
                - None
    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            
        def __init__(self):
            pass

        def GetLoadingCaption(
                version,
                num):
            """
            NYI
            
            - Args:
                - version ():
                - num ():
    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            if num == 0:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading (-)")
            elif num == 1:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading (\)")
            elif num == 2:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading (|)")
            elif num == 3:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading (/)")
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading")

        def get_normal_caption(
                location,
                detailed_captions,
                play_time,
                x,
                y,
                z,
                total_move_x,
                total_move_y,
                total_move_z,
                fps_overclock,
                current_fps,
                iteration,
                version,
                current_memory_usage,
                theme,
                fps,
                average_fps):
            """
            NYI
            
            - Args:
                - location ():
                - detailed_captions ():
                - play_time ():
                - x ():
                - y ():
                - z ():
                - total_move_x ():
                - total_move_y ():
                - total_move_z ():
                - fps_overclock ():
                - current_fps ():
                - iteration ():
                - version ():
                - current_memory_usage ():
                - theme ():
                - fps ():
                - average_fp ():
    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            if detailed_captions:
                hours = int((play_time/60)/60)
                minutes = int(play_time/60)
                seconds = int(play_time)

                Position = f"{round(x, 2)}, {round(y, 2)}, {round(z, 2)}"
                Velocity = f"{total_move_x}, {total_move_y}, {total_move_z}"

                time = f"{hours} : {minutes} : {seconds}"

                if fps_overclock:
                    try:
                        fps_text = "".join((f"fps: 2000 current_fps: {int(current_fps)} ",
                                        f"average_fps: N/A iteration: {iteration} | "))

                        pygame.display.set_caption(
                            "".join((f"Pycraft: v{version}: {location} | ",
                                        f"Play Time: {time} | ",
                                        f"Pos: {Position} | ",
                                        f"V: {Velocity} | ",
                                        fps_text,
                                        f"MemUsE: {int(current_memory_usage)}% | ",
                                        f"CPUUsE: {psutil.cpu_percent()}% | ",
                                        f"Theme: {theme} | ",
                                        f"Thread Count: {threading.active_count()}")))

                    except:
                        fps_text = f"fps: 2000 current_fps: NaN* average_fps: N/A iteration: {iteration} | "

                        pygame.display.set_caption(
                            "".join((f"Pycraft: v{version}: {location} | ",
                                        f"Play Time: {time} | ",
                                        f"Pos: {Position} | ",
                                        f"V: {Velocity} | ",
                                        fps_text,
                                        f"MemUsE: {int(current_memory_usage)}% | ",
                                        f"CPUUsE: {psutil.cpu_percent()}% | ",
                                        f"Theme: {theme} | ",
                                        f"Thread Count: {threading.active_count()}")))

                else:
                    fps_text = "".join((f"fps: {fps} current_fps: {int(current_fps)} ",
                                    f"average_fps: {int(average_fps/iteration)} ",
                                    f"iteration: {iteration} | "))

                    pygame.display.set_caption(
                        "".join((f"Pycraft: v{version}: {location} | ",
                                    f"Play Time: {time} | ",
                                    f"Pos: {Position} | ",
                                    f"V: {Velocity} | ",
                                    fps_text,
                                    f"MemUsE: {int(current_memory_usage)}% | ",
                                    f"CPUUsE: {psutil.cpu_percent()}% | ",
                                    f"Theme: {theme} | ",
                                    f"Thread Count: {threading.active_count()}")))

            else:
                pygame.display.set_caption(f"Pycraft: v{version}: {location}")

        def setOpenGLCaption(
                self,
                play_time,
                Time_Percent,
                day,
                total_move_x,
                total_move_y,
                total_move_z,
                weather):
            """
            NYI
            
            - Args:
                - self ():
                - play_time ():
                - Time_Percent ():
                - day ():
                - total_move_x ():
                - total_move_y ():
                - total_move_z ():
                - weather ():
    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            if self.detailed_captions:
                time_seconds = int(play_time)
                time_minutes = int(play_time/60)
                time_hours = int((play_time/60)/60)

                minutes = time_minutes-(60*time_hours)
                seconds = time_seconds-(60*time_minutes)

                time = f"{time_hours} : {minutes} : {seconds}"

                play_time = "".join((f"Play Time: {time} Game Time: ",
                                    f"{round(Time_Percent, 1)} ",
                                    f": {day-1} | "))

                Position = "".join((f"Pos: {round(self.x, 2)}, ",
                                    f"{round(self.y, 2)}, ",
                                    f"{round(self.z, 2)} | "))

                Velocity = "".join((f"V: {total_move_x}, ",
                                    f"{total_move_y}, ",
                                    f"{total_move_z} | "))

                MemUse = f"MemUsE: {int(self.current_memory_usage)}% | "

                CPUUsE = f"CPUUsE: {psutil.cpu_percent()}% | "

                ThreadCount = f"Thread Count: {threading.active_count()}"

                if self.fps_overclock:
                    try:
                        fps = "".join((f"fps: 2000 current_fps: {int(self.current_fps)} ",
                                        f"average_fps: N/A iteration: {self.iteration} | "))

                        pygame.display.set_caption("".join((f"Pycraft: v{self.version}: Playing ",
                                                        play_time,
                                                        f"Weather: {weather} | ",
                                                        Position,
                                                        Velocity,
                                                        fps,
                                                        MemUse,
                                                        CPUUsE,
                                                        ThreadCount)))
                        
                    except:
                        fps = f"fps: 2000 current_fps: NaN* average_fps: N/A iteration: {self.iteration} | "

                        pygame.display.set_caption("".join((f"Pycraft: v{self.version}: Playing ",
                                                        play_time,
                                                        f"Weather: {weather} | ",
                                                        Position,
                                                        Velocity,
                                                        fps,
                                                        MemUse,
                                                        CPUUsE,
                                                        ThreadCount)))
                else:
                    try:
                        fps = "".join((f"fps: {self.fps} current_fps: ",
                                f"{int(self.current_fps)} average_fps: ",
                                f"{int(self.average_fps/self.iteration)} ",
                                f"iteration: {self.iteration} | "))

                        pygame.display.set_caption("".join((f"Pycraft: v{self.version}: Playing ",
                                                        play_time,
                                                        f"Weather: {weather} | ",
                                                        Position,
                                                        Velocity,
                                                        fps,
                                                        MemUse,
                                                        CPUUsE,
                                                        ThreadCount)))

                    except:
                        fps = "".join((f"fps: {self.fps} current_fps: ",
                                f"{int(self.current_fps)} average_fps: ",
                                f"{int(self.average_fps/self.iteration)} ",
                                f"iteration: {self.iteration} | "))

                        pygame.display.set_caption("".join((f"Pycraft: v{self.version}: Playing ",
                                                        play_time,
                                                        f"Weather: {weather} | ",
                                                        Position,
                                                        Velocity,
                                                        fps,
                                                        MemUse,
                                                        CPUUsE,
                                                        ThreadCount)))
            else:
                pygame.display.set_caption(f"Pycraft: v{self.version}: Playing")

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
