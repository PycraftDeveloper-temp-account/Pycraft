if __name__ != "__main__":
    try:
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
            
    class presets:
        def __init__(self):
            pass

        def update_profile(settings_preset,
                fps,
                aa,
                render_fog,
                fancy_graphics,
                fancy_particles,
                average_fps,
                iteration):
            
            if settings_preset == "low":
                fps = 15
                aa = False
                render_fog = False
                fancy_graphics = False
                fancy_particles = False
                average_fps = (average_fps/iteration)
                iteration = 1

            elif settings_preset == "medium":
                fps = 30
                aa = True
                render_fog = False
                fancy_graphics = True
                fancy_particles = False
                average_fps = (average_fps/iteration)
                iteration = 1
                
            elif settings_preset == "high":
                fps = 60
                aa = True
                render_fog = True
                fancy_graphics = True
                fancy_particles = True
                average_fps = (average_fps/iteration)
                iteration = 1
                
            elif settings_preset == "adaptive":
                CPU_Freq = (psutil.cpu_freq(percpu=True)[0][2])/10
                MEM_Total = psutil.virtual_memory().total

                if (CPU_Freq > 300 and
                        MEM_Total > 8589934592):

                    aa = True
                    render_fog = True
                    fancy_graphics = True
                    fancy_particles = True

                elif (CPU_Freq > 200 and
                        MEM_Total > 4294967296):

                    aa = True
                    render_fog = True
                    fancy_graphics = True
                    fancy_particles = False

                elif (CPU_Freq > 100 and
                        MEM_Total > 2147483648):

                    aa = False
                    render_fog = False
                    fancy_graphics = True
                    fancy_particles = False

                elif (CPU_Freq < 100 and
                        CPU_Freq > 75 and
                        MEM_Total > 1073741824):

                    aa = False
                    render_fog = False
                    fancy_graphics = False
                    fancy_particles = False

            return (fps,
                        aa,
                        render_fog,
                        fancy_graphics,
                        fancy_particles,
                        average_fps,
                        iteration)

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