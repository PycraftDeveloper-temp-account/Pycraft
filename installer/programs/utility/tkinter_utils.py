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
                "startup Fail",
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
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "startup Fail",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
