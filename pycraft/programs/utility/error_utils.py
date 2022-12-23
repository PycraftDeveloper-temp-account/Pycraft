if __name__ != "__main__":
    try:
        import logging_utils
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
            
    class generate_error_screen:
        def __init__(self):
            pass

        def error_screen(
                logging_dictionary,
                output_log,
                detailed_error_messages,
                error_message,
                error_message_detailed,
                platform,
                base_folder,
                close_pygame_window=True):
            
            import tkinter as TKINTER
            import sys
            from tkinter import messagebox as msgbox

            if close_pygame_window:
                try:
                    import pygame
                    pygame.init()
                    pygame.display.quit()
                    
                except Exception as Message:
                    log_message = "ErrorUtils > generate_error_screen > error_screen" + str(Message)

                    logging_utils.create_log_message.update_log_warning(
                        logging_dictionary,
                        log_message,
                        output_log,
                        platform,
                        base_folder)

            try:
                BaseWindow = TKINTER.Tk()
                BaseWindow.withdraw()
                if detailed_error_messages:
                    message = "".join(("Pycraft closed because an error occurred\n\n",
                                            f"More Details:\n{error_message_detailed}"))
                    
                    logging_utils.create_log_message.update_log_error(
                        logging_dictionary,
                        message,
                        output_log,
                        platform,
                        base_folder)

                    msgbox.showerror(
                        "Pycraft closed because an error occurred",
                        message)

                else:
                    message = "".join(("Pycraft closed because an error occurred\n\n",
                                       f"More Details:\n{error_message}"))

                    logging_utils.create_log_message.update_log_error(
                        logging_dictionary,
                        message,
                        output_log,
                        platform,
                        base_folder)
                    
                    msgbox.showerror(
                        "Pycraft closed because an error occurred",
                        message)

                sys.exit()
                
            except Exception as Message:
                try:
                    log_message = "ErrorUtils > generate_error_screen > error_screen: " + str(Message)
                    
                    logging_utils.create_log_message.update_log_warning(
                        logging_dictionary,
                        log_message,
                        output_log,
                        platform,
                        base_folder)
                    
                except Exception as Message:
                    print(Message)
                
                try:
                    BaseWindow = TKINTER.Tk()
                    BaseWindow.withdraw()
                    msgbox.showerror("Pycraft closed because an error occurred",
                                     "".join(("Pycraft closed because an error occurred\n\n",
                                              f"More Details:\n{error_message}")))

                    sys.exit()
                    
                except Exception as Message:
                    print(Message)

                quit()

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
