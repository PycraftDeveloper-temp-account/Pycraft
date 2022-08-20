if __name__ != "__main__":
    print("Started <Pycraft_ErrorUtils>")

    class generate_error_screen:
        def __init__(self):
            pass

        def error_screen(self):
            import tkinter as TKINTER
            import sys
            from tkinter import messagebox as msgbox

            try:
                BaseWindow = TKINTER.Tk()
                BaseWindow.withdraw()
                if self.devmode == 10:
                    print(self.error_message_detailed)
                    msgbox.showerror("Pycraft closed because an error occurred",
                                         "".join(("Pycraft closed because an error occurred\n\n",
                                                  f"More Details:\n{self.error_message_detailed}")))

                else:
                    print(self.error_message)
                    msgbox.showerror("Pycraft closed because an error occurred",
                                         "".join(("Pycraft closed because an error occurred\n\n",
                                                  f"More Details:\n{self.error_message}")))

                sys.exit()
            except Exception as Message:
                sys.exit(Message)

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Fail",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
