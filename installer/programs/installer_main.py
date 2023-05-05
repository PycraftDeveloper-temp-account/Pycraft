try:
    from tkinter import messagebox

    from registry_utils import Registry

    import tkinter_utils
    import installer_utils
    import installer_home
    import file_utils
except ModuleNotFoundError as message:
    from tkinter import messagebox
    error_message = f"{message} in installer_main"
    messagebox.showerror(
        "Startup Error",
        error_message)
    quit()

class Run(Registry):
    def init():
        tkinter_utils.tkinter_installer.create_display()

        file_utils.fix_installer.get_installer_config()

        file_utils.InstallerText.get_installer_text()
        
        installer_utils.file_manipulation.get_versions()
        
        if (len(Registry.pycraft_versions) == 0 and
                Registry.pycraft_install_path is None and
                Registry.developer_version is False):
            
            messagebox.showinfo(
                "Incompatibility Error",
                "We where unable to find any versions of Pycraft supported by this installer.")
            quit()
        
        Registry.initialized = True
        
    def start(developer_version=False):
        Registry.developer_version = developer_version
        if not Registry.initialized:
            Run.init()
            
        installer_home.installer_home.start()

        Registry.root.mainloop()

def get_installer_version():
    return "3.2.0"
