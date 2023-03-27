if __name__ != "__main__":
    try:
        import tkinter
        from tkinter import messagebox

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
        def create_display():
            try:
                geometry = Registry.root.winfo_geometry().split("+")
                Xpos = geometry[1]
                Ypos = geometry[2]
                Registry.root.destroy()
                
            except:
                Xpos, Ypos = 0, 0

            Registry.root = tkinter.Tk()
            #root = tkinter.Toplevel()

            Registry.root.title("Pycraft Setup Wizard")

            Registry.root.resizable(
                False,
                False)

            Registry.root.configure(bg="white")
            Registry.root.geometry(f"850x537+{int(Xpos)}+{int(Ypos)}")

            #render, load = image_utils.tkinter_installer.open_img()

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
