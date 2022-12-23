if __name__ != "__main__":
    try:
        import os
        import tkinter
        from tkinter import messagebox

        import image_utils
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
    
    class tkinter_info:
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

        def create_tkinter_window(
                variable_data,
                version, 
                background_color,
                font_color):
            
            DataWindow = tkinter.Tk()
            DataWindow.title("Player Information")
            DataWindow.configure(width=500, height=300)
            DataWindow.configure(bg="darkgrey")

            text = tkinter.Text(
                DataWindow,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT)

            text.insert(
                tkinter.INSERT,
                f"Pycraft: v{version}\n")

            VariableData = vars(variable_data)

            VariableInformation = []
            for key in VariableData:
                VariableInformation.append(f"{key} = {str(VariableData[key])}\n")

            VariableInformation = sorted(VariableInformation, key=len)

            for i in range(len(VariableInformation)):
                text.insert(tkinter.INSERT, VariableInformation[i])

            text["state"] = tkinter.DISABLED

            text["bg"] = "#%02x%02x%02x" % (background_color[0],
                                                background_color[1],
                                                background_color[2])

            text["fg"] = "#%02x%02x%02x" % (font_color[0],
                                                font_color[1],
                                                font_color[2])

            text.place(
                x=0,
                y=0,
                relwidth=1,
                relheight=1)

            DataWindow.mainloop()
            DataWindow.quit()
                
    class tkinter_installer:
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

            if platform == "Linux":
                ImageFileLocation = os.path.join(
                    base_folder,
                    ("resources//installer resources//Banner.png"))

            else:
                ImageFileLocation = os.path.join(
                    base_folder,
                    ("resources\\installer resources\\Banner.png"))

            render, load = image_utils.tkinter_installer.open_img(
                root, 
                ImageFileLocation)
            
            return root

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
