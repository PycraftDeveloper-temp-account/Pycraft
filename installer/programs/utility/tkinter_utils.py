if __name__ != "__main__":
    try:
        import tkinter
        from tkinter import messagebox
        from tkinter import ttk

        from registry_utils import Registry
        
        import image_utils
    except Exception as Message:
        try:
            import sys
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(
                "Startup Error",
                str(Message))
            sys.exit()

        except Exception as Message:
            print(Message)
            sys.exit()
    
    class tkinter_info(Registry):
        def __init__(self):
            pass

        def get_permissions(permission_message):
            root = tkinter.Tk()
            root.withdraw()

            answer = messagebox.askquestion(
                "Check Permission",
                permission_message)
            
            if answer == "yes":
                return True

            else:
                return False
                
    class tkinter_installer(Registry):
        def style(widget):
            #https://www.pythontutorial.net/tkinter/ttk-style/
            style = ttk.Style()
            style.configure(
                widget,
                background="white",
                foreground="black",
                width=20,
                borderwidth=1,
                focusthickness=3,
                focuscolor="none")
            
            style.map(
                widget,
                background=[
                    ("active", "white")])
                        
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
            
        def create_display():
            try:
                geometry = Registry.root.winfo_geometry().split("+")
                Xpos = geometry[1]
                Ypos = geometry[2]
                Registry.root.destroy()
                old_display = True
            except:
                old_display = False
                Xpos, Ypos = 0, 0

            Registry.root = tkinter.Tk()
            
            Registry.root.iconbitmap(default=Registry.icon_path)

            Registry.root.title("Pycraft Setup Wizard")

            Registry.root.resizable(
                False,
                False)

            Registry.root.configure(bg="white")
            
            if old_display:
                Registry.root.geometry(f"850x537+{int(Xpos)}+{int(Ypos)}")
            else:
                Registry.root.geometry("850x537")
                tkinter_installer.center(Registry.root)
                
            image_utils.tkinter_installer.open_img()

else:
    print("You need to run this as part of Pycraft's Installer")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
