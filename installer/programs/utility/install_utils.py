if __name__ != "__main__":
    try:
        import tkinter
        from tkinter import filedialog
        import tkinter.ttk as tkinter_ttk

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
        
else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
