if __name__ != "__main__":
    try:
        import threading

        from registry_utils import Registry
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft Installer",
            f"A problem occurred whilst trying to start Pycraft Installer.\nMore Details: {error}")

    class InstallCoordinator:
        def __init__(self):
            self.main_install_thread = threading.Thread(target=self.main)

        def start(self):
            self.main_install_thread.start()

        def main(self):
            print("begin install")
            #Registry.progressbar['value'] = k

        def setup_directories(self): # 1/8 or 12.5
            pass

        def setup_venv(self):
            import venv
            venv.

        def download_source_code(self):
            pass

        def extract_source_code(self):
            pass

        def download_resources(self):
            pass

        def install_dependencies(self):
            pass

        def extract_resources(self):
            pass

        def clean_up(self):
            pass

else:
    MESSAGE = "You need to run this as part of Pycraft's Installer. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
