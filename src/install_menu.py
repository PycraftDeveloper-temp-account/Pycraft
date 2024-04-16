if __name__ != "__main__":
    try:
        import pathlib
        import os
        import sys
        import tkinter as tk
        import tkinter.font as font
        import tkinter.filedialog as filedialog
        from tkinter import ttk
        import shutil
        from tkinter import messagebox

        from registry_utils import Registry

        import path_utils
        import install_coordinator_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft Installer",
            f"A problem occurred whilst trying to start Pycraft Installer.\nMore Details: {error}")

    class InstallMenu:
        def __init__(self):
            title_font = font.Font(Registry.root, size=Registry.default_font_size+7)
            content_font = font.Font(Registry.root, size=Registry.default_font_size)

            self.title_label = ttk.Label(Registry.root, text="Pycraft's Installation Assistant", font=title_font)

            Registry.progressbar = ttk.Progressbar()

            self.coordinator = install_coordinator_utils.InstallCoordinator()

        def main(self):
            self.coordinator.start()

            self.title_label.pack()

            Registry.progressbar.pack(fill=tk.X)

            Registry.root.mainloop()

else:
    MESSAGE = "You need to run this as part of Pycraft's Installer. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
