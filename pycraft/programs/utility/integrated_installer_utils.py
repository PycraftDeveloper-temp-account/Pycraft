if __name__ != "__main__":
    try:
        from urllib import request
        import subprocess
        import sys
        import traceback

        import error_utils
    except Exception as Message:
        try:
            import sys
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(
                "Startup Fail",
                str(Message))
            sys.exit()

        except Exception as Message:
            print(Message)
            sys.exit()
            
    class IntegInstaller:
        """
        This class is in charge of connecting the installer and Pycraft together.
        This class is used to check for updates to Pycraft.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        def __init__(self):
            pass

        def CheckVersions(self):
            """
            This subroutine runs the command 'pip list --outdated' in a thread.
            The results of this command are then processed to check of Pycraft is
            outdated. This is run in parallel (thread).
            
            - Args:
                - self (dict): This is used by Pycraft as a way of storing it's current
                    configuration and behaviour and is required by most GUIs. Its use should be
                    reduced where possible for readability reasons.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            
            try:
                if (self.connection_permission and
                        self.connection_status):

                    List = subprocess.check_output(
                        [sys.executable, "-m", "pip", "list", "--outdated"],
                        False)

                    for i in range(len(List)):
                        if List[i:i+14] == b"Python-Pycraft":
                            self.outdated = True
                            self.total_number_of_updates = 1

                    self.get_outdated = [True, False]
                    
            except Exception as Message:
                error_message = "".join(("IntegratedInstaller > IntegInstaller ",
                                             f"> CheckVersions: {str(Message)}"))

                error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                error_utils.generate_error_screen.error_screen(
                    self.logging_dictionary,
                    self.output_log,
                    self.detailed_error_messages,
                    error_message,
                    error_message_detailed,
                    self.platform,
                    self.base_folder)


    class CheckConnection:
        """
        This class is used to check if your PC has a working network
        connection so that updates can be checked for successfully.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        def __init__(self):
            pass

        def test():
            """
            This subroutine attempts to ping google's servers.
            If this is successfully it means there is currently an
            internet connection to your PC. This is not run in a thread,
            so therefore there is a 1 second timeout. This means that if
            there isn't an internet connection available it doesn't slow down
            Pycraft's startup too much.
            
            - Args:
                - None
                    
            - Keyword Args:
                - None

            - Output:
                - (bool): This subroutine will return True if an internet
                    connection can be established. If an internet connection could
                    not be established, nothing is returned.
            """

            try:
                request.urlopen(
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
