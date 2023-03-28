if __name__ != "__main__":
    try:
        import os
        import pathlib
        import platform
        from tkinter import ttk
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
            
    class Registry:
        directory = os.path.dirname(__file__)
        pycraft_directory = str(directory).split("\\")
        directory = ""

        for folder in range(len(pycraft_directory)-1):
            directory += f"{pycraft_directory[folder]}\\"

        base_folder = pathlib.Path(__file__).parent.parent.parent
        platform = platform.system()
        
        del directory
        del pycraft_directory
        
        banner_path = base_folder / "resources" / "installer resources" / "Banner.png"
        choice = "Latest"
        install_custom_version = False
        installer_config_path = base_folder / "data files" / "installer_config.json"
        installer_config_path.parent.mkdir(exist_ok=True, parents=True)
        installer_text = None
        installer_text_path = base_folder / "data files" / "installer text.json"
        pycraft_install_path = None
        root = None
        
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
