if __name__ != "__main__":
    print("Started <Pycraft_IntegratedInstaller>")

    class IntegInstaller:
        def __init__(self):
            pass

        def CheckVersions(self):
            try:
                if (self.mod_urllib_request_ is not None and
                        self.connection_permission and
                        self.connection_status):

                    List = self.mod_subprocess__.check_output(
                        [self.mod_sys__.executable,
                         "-m",
                         "pip",
                         "list",
                         "--outdated"],
                        False)

                    for i in range(len(List)):
                        if List[i:i+14] == b"Python-Pycraft":
                            self.outdated = True
                            self.total_number_of_updates = 1

                    self.get_outdated = [True, False]
            except Exception as Message:
                self.error_message = "".join(("IntegratedInstaller > IntegInstaller ",
                                             f"> CheckVersions: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)


    class CheckConnection:
        def __init__(self):
            pass

        def test(self):
            try:
                self.mod_urllib_request_.urlopen(
                    "https://www.google.com",
                    timeout=1)

                return True
            except:
                return False

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
