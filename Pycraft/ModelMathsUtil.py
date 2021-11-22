if not __name__ == "__main__":
    print("Started <Pycraft_ModelMathsUtil>")
    class ComputeOBJPoints:
        def __init__(self):
            pass

        def LoadingMapData(self):
            self.Map_min_v = [min(self.Map_box[0][i], self.vertex[i]) for i in range(3)]
            self.Map_max_v = [max(self.Map_box[1][i], self.vertex[i]) for i in range(3)]
            self.Map_box = (self.Map_min_v, self.Map_max_v)
            
        def LoadingHUDData(self):
            self.HUD_min_v = [min(self.HUD_box[0][i], self.vertex[i]) for i in range(3)]
            self.HUD_max_v = [max(self.HUD_box[1][i], self.vertex[i]) for i in range(3)]
            self.HUD_box = (self.HUD_min_v, self.HUD_max_v)
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()