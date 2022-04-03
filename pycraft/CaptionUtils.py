if not __name__ == "__main__":
    print("Started <Pycraft_CaptionUtils>")
    class GenerateCaptions:
        def __init__(self):
            pass

        def GetLoadingCaption(self, num):
            try:
                if num == 0:
                    self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (-)")
                elif num == 1:
                    self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (\)")
                elif num == 2:
                    self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (|)")
                elif num == 3:
                    self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (/)")
                else:
                    self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading")
                self.mod_Pygame__.display.update()
            except Exception as Message:
                self.ErrorMessage = "CaptionUtils > GenerateCaptions > GetLoadingCaption: "+str(Message)
                
                
        def GetNormalCaption(self, location):
            if self.Devmode >= 5 and self.Devmode <= 9:
                self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | you are: {10-self.Devmode} steps away from being a developer") 
            elif self.Devmode == 10: 
                self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | Developer Mode | Pos: {round(self.X, 2)}, {round(self.Y, 2)}, {round(self.Z, 2)} | V: {self.Total_move_x}, {self.Total_move_y}, {self.Total_move_z} FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: {int(self.aFPS/self.Iteration)} Iteration: {self.Iteration} | MemUsE: {int(self.CurrentMemoryUsage)}% | CPUUsE: {self.mod_Psutil__.cpu_percent()}% | Theme: {self.theme} | Thread Count: {self.mod_Threading__.active_count()}") 
            else:
                self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location}")


        def GetOpenGLCaption(self, GameData):
            try:
                if self.Devmode >= 5 and self.Devmode <= 9:
                    GameData.wnd.title = f"Pycraft: v{self.version}: Playing | you are: {10-self.Devmode} steps away from being a developer"
                elif self.Devmode == 10:
                    GameData.wnd.title = f"Pycraft: v{self.version}: Playing | Developer Mode | Pos: {round(self.X, 2)}, {round(self.Y, 2)}, {round(self.Z, 2)} | V: {self.Total_move_x}, {self.Total_move_y}, {self.Total_move_z} | FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: {int(self.aFPS/self.Iteration)} Iteration: {self.Iteration} | MemUsE: {int(self.CurrentMemoryUsage)}% | CPUUsE: {self.mod_Psutil__.cpu_percent()}% | Theme: {self.theme} | Thread Count: {self.mod_Threading__.active_count()}"
                else:
                    GameData.wnd.title = f"Pycraft: v{self.version}: Playing"
            except Exception as Message:
                self.ErrorMessage = "CaptionUtils > GenerateCaptions > GetNormalCaption: "+str(Message)

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()