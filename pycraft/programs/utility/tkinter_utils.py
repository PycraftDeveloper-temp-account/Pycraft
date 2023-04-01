if __name__ != "__main__":
    try:
        import os
        import tkinter
        from tkinter import messagebox
        import pathlib
        import threading

        from registry_utils import Registry
        
        import image_utils
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in tkinter_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class splash_screen(Registry):
        def center(win):
            win.update_idletasks()
            width = win.winfo_width()
            frm_width = win.winfo_rootx() - win.winfo_x()
            win_width = width + 2 * frm_width
            height = win.winfo_height()
            titlebar_height = win.winfo_rooty() - win.winfo_y()
            win_height = height + titlebar_height + frm_width
            x = win.winfo_screenwidth() // 2 - win_width // 2
            y = win.winfo_screenheight() // 2 - win_height // 2
            win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
            win.deiconify()
            
        def check_if_necessary(root, stop_splash_screen):
            if not stop_splash_screen.is_set():
                quit()
            else:
                root.after(int((1/15)*1000), lambda: splash_screen.check_if_necessary(root, stop_splash_screen))
        
        def create_splash(stop_splash_screen):
            if stop_splash_screen.is_set():
                directory = os.path.dirname(__file__)
                pycraft_directory = str(directory).split("\\")
                directory = ""

                for folder in range(len(pycraft_directory)-1):
                    directory += f"{pycraft_directory[folder]}\\"

                base_folder = pathlib.Path(directory).parent
                
                root = tkinter.Tk()
                
                root.withdraw()
                
                root.title("Loading Pycraft")
                
                root.geometry("485x193")
                            
                root.resizable(
                    False,
                    False)
                
                colour_key = "#%02x%02x%02x" % (255,
                                                0,
                                                255)
                
                root.attributes("-transparentcolor", colour_key)
                
                banner_path = base_folder / "resources" / "general resources" / "pycraft_logo_smaller_colorkey.png"

                image_utils.tkinter_installer.open_img(
                    root, 
                    banner_path,
                    offset_x=-2,
                    offset_y=-2)

                #Make the window borderless
                root.overrideredirect(True)
                
                splash_screen.center(root)
                
                root.after(int((1/15)*1000), lambda: splash_screen.check_if_necessary(root, stop_splash_screen))

                root.mainloop()
    
    class tkinter_info(Registry):
        def get_permissions(permission_message):
            root = tkinter.Tk()
            root.withdraw()

            answer = messagebox.askquestion(
                "Check Permission",
                permission_message)
            
            return answer == "yes"
            
        def update_content():
            VariableInformation = ""
            for key in Registry.__dict__:
                VariableInformation += f"{key} = {str(Registry.__dict__[key])}\n"
            
            return VariableInformation
        
        def refresh_window(DataWindow, text):
            VariableInformation = tkinter_info.update_content()
            
            text["state"] = tkinter.NORMAL
            text.replace("1.0", tkinter.END, VariableInformation)
            text["state"] = tkinter.DISABLED

            text.place(
                x=0,
                y=0,
                relwidth=1,
                relheight=1)
            
            DataWindow.after(1000, lambda: tkinter_info.refresh_window(DataWindow, text))
            
        def tkinter_window():
            DataWindow = tkinter.Tk()
            DataWindow.title("Registry Information")
            DataWindow.configure(width=500, height=300)
            DataWindow.configure(bg="darkgrey")
            
            text = tkinter.Text(
                DataWindow,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT)
            
            text["bg"] = "#%02x%02x%02x" % (Registry.background_color[0],
                                                Registry.background_color[1],
                                                Registry.background_color[2])

            text["fg"] = "#%02x%02x%02x" % (Registry.font_color[0],
                                                Registry.font_color[1],
                                                Registry.font_color[2])
            
            VariableInformation = tkinter_info.update_content()

            VariableInformation = sorted(VariableInformation)
            
            for i in range(len(VariableInformation)):
                text.insert(tkinter.INSERT, VariableInformation[i])
            
            tkinter_info.refresh_window(DataWindow, text)
            
            DataWindow.after(1000, lambda: tkinter_info.refresh_window(DataWindow, text))

            DataWindow.mainloop()
            DataWindow.quit()
            
        def create_tkinter_window():
            threading.Thread(target=tkinter_info.tkinter_window).start()
                
    class tkinter_installer(Registry):
        def __init__():
            pass

        def create_display(root, platform, base_folder):
            try:
                geometry = root.winfo_geometry().split("+")
                Xpos = geometry[1]
                Ypos = geometry[2]
                root.destroy()
                
            except:
                Xpos, Ypos = 0, 0

            root = tkinter.Tk()
            #root = tkinter.Toplevel()

            root.title("Pycraft Setup Wizard")

            root.resizable(
                False,
                False)

            root.configure(bg="white")
            root.geometry(f"850x537+{int(Xpos)}+{int(Ypos)}")

            banner_path = base_folder / "resources" / "installer resource" / "Banner.png"

            render, load = image_utils.tkinter_installer.open_img(
                root, 
                banner_path)
            
            return root

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
