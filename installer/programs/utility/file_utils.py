if __name__ != "__main__":
    try:
        import json
        import traceback
        from tkinter import messagebox

        from registry_utils import Registry
        import logging_utils
        import error_utils
    except ModuleNotFoundError as Message:
        import sys
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        error_message = f"{Message} in file_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        sys.exit()
            
    class InstallerText(Registry):
        def get_installer_text():
            with open(
                    Registry.installer_text_path,
                    "r") as file:
                
                Registry.installer_text = json.load(file)
            
    class fix_installer(Registry):
        def set_install_location():
            repair = {"PATH": str(Registry.base_folder)}

            installer_config_path = Registry.base_folder / "data files" / "installer_config.json"

            with open(
                    installer_config_path,
                    "w") as file:

                json.dump(
                    repair,
                    file)

        def get_install_location():
            installer_config_path = Registry.base_folder / "data files" / "installer_config.json"
            with open(
                    installer_config_path,
                    "r") as file:

                data = json.load(file)

            return data["PATH"]

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
