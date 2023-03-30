print("Thank you for using Pycraft!\nPlease wait, we are getting it ready for you now.")

try:
    import sys
    import pathlib
    import platform
    import os
    import ctypes
except ModuleNotFoundError as Message:
    import sys
    import tkinter as tk
    from tkinter import messagebox
    error_message = f"{Message} in __init__"
    messagebox.showerror(
        "Startup Error",
        error_message)
    sys.exit()

# caution: path[0] is reserved for script path (or '' in REPL)
base_folder = pathlib.Path(os.path.dirname(__file__))
sys.pycache_prefix = base_folder / "temporary"

programs_base_folder = base_folder / "programs"
utility_base_folder = base_folder / "programs" / "utility"

sys.path.append(str(programs_base_folder))
sys.path.append(str(utility_base_folder))

try:
    from pycraft_main import QueryVersion
    from pycraft_main import start
except ModuleNotFoundError as Message:
    import sys
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    error_message = f"{Message} in __init__"
    messagebox.showerror(
        "Startup Error",
        error_message)
    sys.exit()

if platform.system() == "Windows":
    myappid = f'PycraftDev.Pycraft._.{QueryVersion()}' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    del myappid

del sys
del os
del pathlib
del platform
del ctypes
del base_folder
del utility_base_folder
del programs_base_folder