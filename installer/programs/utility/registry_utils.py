if __name__ != "__main__":
    try:
        import os
        import pathlib
        import platform
    except ModuleNotFoundError as Message:
        import sys
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        error_message = f"{Message} in registry_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
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
        icon_path = base_folder / "resources" / "general resources" / "Icon.ico"
        initialized = False
        install_custom_version = False
        installer_config_path = base_folder / "data files" / "installer_config.json"
        installer_config_path.parent.mkdir(exist_ok=True, parents=True)
        installer_text = None
        installer_text_path = base_folder / "data files" / "installer text.json"
        pycraft_install_path = None
        root = None
        
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
