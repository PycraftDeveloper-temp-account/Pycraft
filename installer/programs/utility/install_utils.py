if __name__ != "__main__":
    try:
        import os
        import platform
        import tkinter
        from tkinter import filedialog
        import tkinter.ttk as tkinter_ttk
        
        if platform.system() == "Windows":
            from win32com.shell import shell, shellcon
            import win32com.client

        from registry_utils import Registry
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in installer_main"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
        
    class install_data:
        var1 = None
        Dir = Registry.base_folder
        CurrentLocat = None
        
    class install_screen_one(Registry):
        def button_check():
                data = install_data.var1.get()
                if data is None or data == 0:
                    continueButton = tkinter_ttk.Button(
                        Registry.root,
                        text="Continue")

                    continueButton.place(x=760, y=500)
                    continueButton["state"] = tkinter.DISABLED

                else:
                    from install import begin_install
                    continueButton = tkinter_ttk.Button(
                        Registry.root,
                        text="Continue",
                        command=lambda: begin_install.install_screen_two())

                    continueButton.place(x=760, y=500)
                    continueButton["state"] = tkinter.NORMAL
                    Registry.root.update_idletasks()
                    
    class install_screen_two(Registry):
        def get_dir():
            install_data.Dir = filedialog.askdirectory()
            if len(install_data.Dir) >= 80:
                Dir2 = install_data.Dir[:80]+"..."
            else:
                Dir2 = install_data.Dir

            install_data.CurrentLocat.destroy()
            install_data.CurrentLocat = tkinter.Label(
                Registry.root,
                text=("  "+Dir2+"  "),
                background="white",
                relief=tkinter.RIDGE)

            install_data.CurrentLocat.place(x=313, y=152.5)

            Registry.root.update_idletasks()
            
    class install_screen_three(Registry):
        def render_progress_bar(i):
            CompletionProgressbar = tkinter_ttk.Progressbar(
                Registry.root,
                orient=tkinter.HORIZONTAL,
                length=100,
                mode="indeterminate")

            CompletionProgressbar.place(x=200, y=500)

            CompletionProgressbar["value"] += i
            Registry.root.update()
            
    class install_screen_four(Registry):
        def desktop_is_checked():
            global CreateDSKShortcut
            CreateDSKShortcut = CS.get()

        def start_is_checked():
            global CreateSTRTShortcut
            CreateSTRTShortcut = CSS.get()

        def toggle_release_notes():
            global ReleaseNotes
            ReleaseNotes = RelNot.get()

        def on_exit():
            try:
                if CreateDSKShortcut:
                    if Registry.platform == "Windows":
                        desktop = os.path.join(
                            os.path.join(
                                os.environ["USERPROFILE"]),
                            "Desktop")

                        shell = client.Dispatch(
                            "WScript.Shell")

                        shortcut = shell.CreateShortCut(
                            os.path.join(
                                desktop,
                                'Pycraft.lnk'))

                        FolderDirectory = "/pycraft/resources/folder resources/FolderIcon.ico"
                        shortcut.Targetpath = install_data.Dir+"/Pycraft/main.py"
                        shortcut.IconLocation = install_data.Dir+FolderDirectory
                        shortcut.save()

                if CreateSTRTShortcut:
                    if Registry.platform == "Windows":
                        try:
                            start = shell.SHGetSpecialFolderPath(
                                0,
                                shellcon.CSIDL_COMMON_STARTMENU)

                            shell = client.Dispatch(
                                "WScript.Shell")

                            shortcut = shell.CreateShortCut(
                                os.path.join(
                                    start,
                                    "Programs\\Pycraft.lnk"))

                            FolderDirectory = "/pycraft/resources/folder resources/FolderIcon.ico"

                            shortcut.Targetpath = install_data.Dir+"/pycraft/main.py"
                            shortcut.IconLocation = install_data.Dir+FolderDirectory
                            shortcut.save()

                        except Exception as Message:
                            print(Message)
                            messagebox.showwarning(
                                "Permission Denied",
                                Registry.installer_text["install"][6].format(Registry.choice))

                if ReleaseNotes:
                    import webbrowser
                    webbrowser.open(
                        "https://github.com/PycraftDeveloper/Pycraft")

            except Exception as Message:
                messagebox.showerror(
                    "An error occurred",
                    Registry.installer_text["install"][7].format(Message))

            quit()
        
else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
