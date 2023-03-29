if __name__ != "__main__":
    try:
        import tkinter

        from registry_utils import Registry
    except ModuleNotFoundError as Message:
        import sys
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        error_message = f"{Message} in text_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        sys.exit()
            
    class installer_text(Registry):
        def __init__(self):
            pass

        def create_text(root, OUTPUTtext):
            text = tkinter.Text(
                root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                OUTPUTtext)

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)
            root.update_idletasks()
            
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
