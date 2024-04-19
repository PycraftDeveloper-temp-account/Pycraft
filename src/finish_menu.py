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
        import time
        import threading

        from registry_utils import Registry

        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft Installer",
            f"A problem occurred whilst trying to start Pycraft Installer.\nMore Details: {error}")

    class FinishMenu:
        def __init__(self):
            self.finish_menu_frame = ttk.Frame(Registry.root)

            title_font = font.Font(self.finish_menu_frame, size=Registry.default_font_size+7)
            content_font = font.Font(self.finish_menu_frame, size=Registry.default_font_size)

            self.title_label = ttk.Label(self.finish_menu_frame, text="Pycraft's Installation Assistant", font=title_font)

            self.title_label.pack()

        def main(self):
            self.finish_menu_frame.pack(fill=tk.BOTH, expand=True)

else:
    MESSAGE = "You need to run this as part of Pycraft's Installer. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
