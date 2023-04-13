if __name__ != "__main__":
    try:
        from tkinter import messagebox

        from registry_utils import Registry
        
        import uninstall
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in installer_main"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
        
    class uninstaller_data:
        uninstall_option = None
        version = None
        output_text = "Querying versions"
    
    class uninstall_screen_one(Registry):
        def get_confirmation():
            Registry.UpdateUtility = False
            if messagebox.askokcancel(
                "Are you sure with your decision",
                Registry.installer_text["uninstall"][1]):

                ans = messagebox.askquestion(
                    "Permissions manager",
                    "Can we have permission to remove and change some files on your PC?")

                while ans == "no":
                    ans2 = messagebox.askquestion(
                        "Caution",
                        Registry.installer_text["uninstall"][2])

                    if ans2 == "no":
                        quit()
                    else:
                        ans = messagebox.askquestion(
                            "Permissions manager",
                            "Can we have permission to remove and change files on your PC?")

                uninstall.Uninstall.uninstall_screen_two()
        
else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
