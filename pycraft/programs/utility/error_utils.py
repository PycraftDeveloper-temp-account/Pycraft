if __name__ != "__main__":
    try:
        from registry_utils import Registry
        
        import logging_utils
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in error_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class generate_error_screen(Registry):
        def error_screen(
                error_message,
                error_message_detailed,
                close_pygame_window=True):
            
            from tkinter import messagebox

            if close_pygame_window:
                try:
                    import pygame
                    pygame.init()
                    pygame.display.quit()
                    
                except Exception as message:
                    log_message = "ErrorUtils > generate_error_screen > error_screen" + str(message)

                    logging_utils.create_log_message.update_log_warning(
                        log_message)

            try:
                if Registry.detailed_error_messages:
                    message = "".join(("Pycraft closed because an error occurred\n\n",
                                            f"More Details:\n{error_message_detailed}"))
                    
                    logging_utils.create_log_message.update_log_error(
                        message)

                    messagebox.showerror(
                        "Pycraft closed because an error occurred",
                        message)

                else:
                    message = "".join(("Pycraft closed because an error occurred\n\n",
                                       f"More Details:\n{error_message}"))

                    logging_utils.create_log_message.update_log_error(
                        message)
                    
                    messagebox.showerror(
                        "Pycraft closed because an error occurred",
                        message)

                quit()
                
            except Exception as message:
                try:
                    log_message = "ErrorUtils > generate_error_screen > error_screen: " + str(message)
                    
                    logging_utils.create_log_message.update_log_warning(
                        log_message)
                    
                except Exception as message:
                    print(message)
                
                try:
                    messagebox.showerror("Pycraft closed because an error occurred",
                                     "".join(("Pycraft closed because an error occurred\n\n",
                                              f"More Details:\n{error_message}")))

                    quit()
                    
                except Exception as message:
                    print(message)

                quit()

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
