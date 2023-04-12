if __name__ != "__main__":
    try:
        import psutil
        
        from registry_utils import Registry
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in setting_preset_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class presets(Registry):
        def update_profile():
            
            if Registry.settings_preset == "low":
                Registry.fps = 15
                Registry.aa = False
                Registry.render_fog = False
                Registry.fancy_graphics = False
                Registry.fancy_particles = False
                Registry.average_fps = (Registry.average_fps/Registry.iteration)
                Registry.iteration = 1

            elif Registry.settings_preset == "medium":
                Registry.fps = 30
                Registry.aa = True
                Registry.render_fog = False
                Registry.fancy_graphics = True
                Registry.fancy_particles = False
                Registry.average_fps = (Registry.average_fps/Registry.iteration)
                Registry.iteration = 1
                
            elif Registry.settings_preset == "high":
                Registry.fps = 60
                Registry.aa = True
                Registry.render_fog = True
                Registry.fancy_graphics = True
                Registry.fancy_particles = True
                Registry.average_fps = (Registry.average_fps/Registry.iteration)
                Registry.iteration = 1
                
            elif Registry.settings_preset == "adaptive":
                CPU_Freq = (psutil.cpu_freq(percpu=True)[0][2])/10
                MEM_Total = psutil.virtual_memory().total

                if (CPU_Freq > 300 and
                        MEM_Total > 8589934592):

                    Registry.aa = True
                    Registry.render_fog = True
                    Registry.fancy_graphics = True
                    Registry.fancy_particles = True

                elif (CPU_Freq > 200 and
                        MEM_Total > 4294967296):

                    Registry.aa = True
                    Registry.render_fog = True
                    Registry.fancy_graphics = True
                    Registry.fancy_particles = False

                elif (CPU_Freq > 100 and
                        MEM_Total > 2147483648):

                    Registry.aa = False
                    Registry.render_fog = False
                    Registry.fancy_graphics = True
                    Registry.fancy_particles = False

                elif (CPU_Freq < 100 and
                        CPU_Freq > 75 and
                        MEM_Total > 1073741824):

                    Registry.aa = False
                    Registry.render_fog = False
                    Registry.fancy_graphics = False
                    Registry.fancy_particles = False

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()