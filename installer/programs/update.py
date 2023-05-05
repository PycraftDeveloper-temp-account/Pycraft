if __name__ != "__main__":
    try:
        from tkinter import messagebox

        import uninstall
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in update"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()

    class Update:
        def update_screen_one():
            query = messagebox.askyesno(
                "Are you sure?",
                "Would you like to update to the latest version of Pycraft?")
            
            if query:
                uninstall.Uninstall.remove_but_keep_save(updating=True)

else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
