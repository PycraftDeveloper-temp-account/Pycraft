try:
    from registry_utils import Registry
    
    import tkinter_utils
    import installer_utils
    import installer_home
    import file_utils
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
        
class run_installer(Registry):
    def Initialize():
        tkinter_utils.tkinter_installer.create_display()

        installer_utils.get_installer_data.get_data()
        
        file_utils.InstallerText.get_installer_text()

        installer_home.installer_home.start()

        Registry.root.mainloop()
        
def QueryVersion():
    return "3.2.0"