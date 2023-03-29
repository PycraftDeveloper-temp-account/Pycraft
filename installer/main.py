if __name__ == "__main__":
    try:
        import __init__
    except ModuleNotFoundError as Message:
        import sys
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        error_message = f"{Message} in main"
        messagebox.showerror(
            "Startup Error",
            error_message)
        sys.exit()
    else:
        __init__.installer_main.Run.start()