if __name__ != "__main__":
    try:
        import traceback
        import os
        import time

        import pygame
        from PIL import ImageGrab

        import error_utils
        import display_utils
        import sound_utils
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
            
    class AccessOtherGUIs:
        def __init__(self):
            pass

        def AccessGUI(self, load_inventory, load_map, start_inventory, start_map):
            try:
                if load_inventory:
                    bbox = (
                        *display_utils.display_utils.get_display_location(),
                        *pygame.display.get_window_size())

                    image = ImageGrab.grab(bbox)
                
                    if self.platform == "Linux":
                        image.save(
                            os.path.join(
                                self.base_folder,
                                "resources//general resources//PauseIMG.png"))
                        
                    else:
                        image.save(
                            os.path.join(
                                self.base_folder,
                                "resources\\general resources\\PauseIMG.png"))

                    pygame.event.set_grab(False)
                    pygame.mouse.set_visible(True)

                    start_inventory.set()
                    
                    while start_inventory.is_set():
                        pygame.event.poll()
                        time.sleep(1)

                    if self.sound:
                        sound_utils.play_sound.play_click_sound(
                            self.platform,
                            self.base_folder,
                            self.sound_volume)
                    
                    load_inventory = False

                    pygame.event.set_grab(True)
                    pygame.mouse.set_visible(False)

                elif load_map:
                    pygame.event.set_grab(False)
                    pygame.mouse.set_visible(True)

                    start_map.set()

                    while start_map.is_set():
                        pygame.event.poll()
                        time.sleep(1)

                    if self.sound:
                        sound_utils.play_sound.play_click_sound(
                            self.platform,
                            self.base_folder,
                            self.sound_volume)
                    
                    load_map = False

                    pygame.event.set_grab(True)
                    pygame.mouse.set_visible(False)


                return load_inventory, load_map
                
            except Exception as Message:
                error_message = "".join(("GameEngineUtils > AccessOtherGUIs ",
                                                        f"> AccessGUI: {str(Message)}"))

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