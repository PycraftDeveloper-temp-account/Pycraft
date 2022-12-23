if __name__ != "__main__":
    try:
        import datetime
        import os
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
        
    class create_log_message:
        """This class adds logging support to Pycraft.
            
        - Args:
            - None
                
        - Keyword Args:
            - None

        - Output:
            - None
        """
        def __init__(self):
            pass

        def update_log_information(
                logging_dictionary,
                text,
                output_log,
                platform,
                base_folder):
            """This subroutine handles the formatting, output and logging of all
            non-critical information. This can be a handy debugging tool.
            
            - Args:
                - logging_dictionary (dict): This dictionary is used to tell this
                    subroutine if information messages are to be logged, this can be
                    adjusted in settings.
                - text (str): This string contains the piece of information to log.
                - output_log (bool): This option tells the subroutine if logged
                    messages should also be outputted to the console.
                - platform (str): This string tells the subroutine which operating
                    system we are using. This is needed for OS specific operations.
                - base_folder (str): This string is a file path to the resources
                    for Pycraft on your device.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            
            if logging_dictionary["information"]:
                text = f"Information: {str(text)}"
                text += f" @ {datetime.datetime.now()}"
                if output_log:
                    print(text)
                    
                log_file.update_log(
                    platform,
                    base_folder,
                    text)

        def update_log_warning(
                logging_dictionary,
                text,
                output_log,
                platform,
                base_folder):
            """This subroutine handles the formatting, output and logging of all non-critical warnings
            that could cause errors if not dealt with during the execution of Pycraft. 
            This can be a handy debugging tool.
            
            - Args:
                - logging_dictionary (dict): This dictionary is used to tell this
                    subroutine if warning messages are to be logged, this can be
                    adjusted in settings.
                - text (str): This string contains the piece of information to log.
                - output_log (bool): This option tells the subroutine if logged
                    messages should also be outputted to the console.
                - platform (str): This string tells the subroutine which operating
                    system we are using. This is needed for OS specific operations.
                - base_folder (str): This string is a file path to the resources
                    for Pycraft on your device.
                
            - Keyword Args:
                - None

            - Output:
                - None
            """
            
            if logging_dictionary["warnings"]:
                text = f"Warning: {str(text)}"
                text += f" @ {datetime.datetime.now()}"
                if output_log:
                    print(text)

                log_file.update_log(
                    platform,
                    base_folder,
                    text)

        def update_log_error(
                logging_dictionary,
                error_text,
                output_log,
                platform,
                base_folder):
            """This subroutine handles the formatting, output and logging of all critical errors in Pycraft.
            These must be dealt with immediately and will stop the execution of Pycraft, or could cause
            some things to not behave as expected.
            
            - Args:
                - logging_dictionary (dict): This dictionary is used to tell this
                    subroutine if error messages are to be logged, this can be
                    adjusted in settings.
                - text (str): This string contains the piece of information to log.
                - output_log (bool): This option tells the subroutine if logged
                    messages should also be outputted to the console.
                - platform (str): This string tells the subroutine which operating
                    system we are using. This is needed for OS specific operations.
                - base_folder (str): This string is a file path to the resources
                    for Pycraft on your device.
                
            - Keyword Args:
                - None

            - Output:
                - None
            """
            
            if logging_dictionary["errors"]:
                text = "### ### ### ###\n\n"
                text += f"Error: {str(error_text)}"
                text += f" @ {datetime.datetime.now()}\n"
                text += "\n### ### ### ###\n"
                if output_log:
                    print(text)

                log_file.update_log(
                    platform,
                    base_folder,
                    text)

    class log_file:
        """This class handles the writing to and formatting of the log file.
            
        - Args:
            - None
                
        - Keyword Args:
            - None

        - Output:
            - None
        """
        def __init__(self):
            pass

        def clear_log(
                platform,
                base_folder):
            """This subroutine clears the log file.
            This is often called at startup to prevent the log file becoming too long.
            
            - Args:
                - platform (str): This string tells the subroutine which operating
                    system we are using. This is needed for OS specific operations.
                - base_folder (str): This string is a file path to the resources
                    for Pycraft on your device.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
        
            if platform == "Linux":
                with open(
                    os.path.join(
                        base_folder,
                        "data files//log.txt"), "w"):

                    pass

            else:
                with open(
                    os.path.join(
                        base_folder,
                        "data files\\log.txt"), "w"):

                    pass

        def update_log(
                platform,
                base_folder,
                text):
            """This subroutine updates the log file by appending new information to the end.
            This is usually called every time a log is made.
            
            - Args:
                - platform (str): This string tells the subroutine which operating
                    system we are using. This is needed for OS specific operations.
                - base_folder (str): This string is a file path to the resources
                    for Pycraft on your device.
                - text (str): This string contains the formatted log which will be
                    added to the log.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            
            size = (os.path.getsize(
                os.path.join(
                    base_folder,
                    "data files//log.txt"))/1000)/1000 #MB

            if size < 1:
                if platform == "Linux":
                    with open(
                        os.path.join(
                            base_folder,
                            "data files//log.txt"), "a") as file:

                        file.write(text)

                else:
                    with open(
                        os.path.join(
                            base_folder,
                            "data files\\log.txt"), "a") as file:

                        file.write(text)

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
