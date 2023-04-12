DEVELOPER_BUILD = True

def QueryVersion():
    return "pycraft v9.5.0dev8"

def start():
    try:
        import __init__
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in main"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    try:
        __init__.pycraft_main.Initialize.start()
    except Exception as message:
        try:
            import traceback
            from tkinter import messagebox
            import logging_utils
        except ModuleNotFoundError as message:
            from tkinter import messagebox
            error_message = f"{message} in main"
            messagebox.showerror(
                "Startup Error",
                error_message)
            quit()

        if DEVELOPER_BUILD:
            message = "".join((traceback.format_exception(
                None,
                message,
                message.__traceback__)))
            
        logging_utils.create_log_message.update_log_error(
            message)
            
        messagebox.showerror(
            "Pycraft closed because an error occurred",
            str(message))
        
        quit()
        
if __name__ == "__main__":
    try:
        try:
            import psutil

            import __init__
        except ModuleNotFoundError as message:
            from tkinter import messagebox
            error_message = f"{message} in main"
            messagebox.showerror(
                "Startup Error",
                error_message)
            quit()
        else:
            counter = 0
            for proc in psutil.process_iter(["pid", "name", "username"]):
                if "pycraft.exe" in str(proc.info["name"]).lower():
                    counter += 1

            if counter >= 2:
                quit()

            start()
            
    except Exception as message:
        from tkinter import messagebox
        messagebox.showerror(
            "Startup Error",
            str(message))

        quit()