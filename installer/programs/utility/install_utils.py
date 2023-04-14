if __name__ != "__main__":
    try:
        import os
        import platform
        import tkinter
        from tkinter import filedialog
        from tkinter import messagebox
        import tkinter.ttk as tkinter_ttk
        import webbrowser
        import pathlib
        import shutil
        
        if platform.system() == "Windows":
            from win32com.shell import shell, shellcon
            import win32com.client as win32com_client

        from registry_utils import Registry
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in installer_main"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
        
    class install_data:
        var1 = None
        Dir = Registry.base_folder
        CurrentLocat = None
        create_desktop_shortcut = True
        create_start_menu_shortcut = False
        show_release_notes = True
        
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
            
    class install_screen_four(Registry):
        def desktop_is_checked(choose_create_desktop_shortcut):
            install_data.create_desktop_shortcut = choose_create_desktop_shortcut.get()

        def start_is_checked(choose_create_start_menu_shortcut):
            install_data.create_start_menu_shortcut = choose_create_start_menu_shortcut.get()

        def toggle_release_notes(choose_release_notes):
            install_data.show_release_notes = choose_release_notes.get()
            
        def create_desktop_shortcut_windows():
            desktop = os.path.join(
                os.path.join(
                    os.environ["USERPROFILE"]),
                "Desktop")

            shell_com = win32com_client.Dispatch(
                "WScript.Shell")

            shortcut = shell_com.CreateShortCut(
                os.path.join(
                    desktop,
                    'Pycraft.lnk'))

            shortcut.Targetpath = str(pathlib.Path(install_data.Dir) / "pycraft" / "main.py")
            shortcut.IconLocation = str(Registry.icon_path)
            shortcut.save()
            
        def create_desktop_shortcut_linux():
            linux_desktop = pathlib.Path("/usr/share/applications")
            desktop_file = Registry.base_folder / "resources" / "folder resources" / "pycraft.desktop"
            temporary_desktop_file = Registry.base_folder / "resources" / "folder resources" / "tmp_pycraft.desktop"
            with open(desktop_file, "r") as file:
                file_data = file.readlines()
            
            string = ""
            for line in file_data:
                if "{install_path}" in line:
                    line = line.replace("{install_path}", str(Registry.pycraft_install_path))
                elif "{version}" in line:
                    if " (latest)" in Registry.choice or Registry.choice == "Latest":
                        version = list(Registry.pycraft_versions.keys())[0]
                    else:
                        version = Registry.choice
                    
                    line = line.replace("{version}", version[1:])
                    
                string += line
                
            with open(temporary_desktop_file, "w") as file:
                file.write(string)
            
            shutil.move(temporary_desktop_file, linux_desktop)
            
        def create_start_menu_shortcut_windows():
            start_menu = shell.SHGetSpecialFolderPath(
                0,
                shellcon.CSIDL_PROGRAMS)
            
            shell_com = win32com_client.Dispatch(
                "WScript.Shell")
            
            start_menu_path = pathlib.Path(start_menu)
            shortcut = shell_com.CreateShortCut(
                str(start_menu_path / "Pycraft.lnk"))

            shortcut.Targetpath = str(pathlib.Path(install_data.Dir) / "pycraft" / "main.py")
            shortcut.IconLocation = str(Registry.icon_path)
            shortcut.save()
                
        def show_release_notes():
            webbrowser.open(
                "https://github.com/PycraftDeveloper/Pycraft")
                    
        def on_exit():
            try:
                if install_data.create_desktop_shortcut:
                    if Registry.platform == "Windows":
                        install_screen_four.create_desktop_shortcut_windows()
                    elif Registry.platform == "Linux":
                        install_screen_four.create_desktop_shortcut_linux()

                if install_data.create_start_menu_shortcut:
                    if Registry.platform == "Windows":
                        install_screen_four.create_start_menu_shortcut_windows()
                    elif Registry.platform == "Linux":
                        install_screen_four.create_desktop_shortcut_linux()

                if install_data.show_release_notes:
                    install_screen_four.show_release_notes()

            except PermissionError as message:
                print(message)
                messagebox.showwarning(
                    "Permission Denied",
                    Registry.installer_text["install"][7].format(Registry.choice))
                
            except Exception as message:
                print(message)
                messagebox.showerror(
                    "An error occurred",
                    Registry.installer_text["install"][8].format(message))

            quit()
        
else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
