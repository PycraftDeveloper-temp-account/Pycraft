if __name__ == "__main__":
    try:
        import __init__
    except ModuleNotFoundError as Message:
        import sys
        from tkinter import messagebox
        error_message = f"{Message} in main"
        messagebox.showerror(
            "Startup Error",
            error_message)
        sys.exit()
    else:
        __init__.start()