if __name__ != "__main__":
    class establish_joystick_removed:
        def __init__(self):
            pass

        def JoystickRemoved(self):
            while True:
                try:
                    if self.mod_pygame__.init():
                        if (self.mod_pygame__.joystick.get_count() == 0 and
                                self.pygame_device_removed_update is False and
                                self.joystick_connected):

                            self.pygame_device_removed_update = True
                            self.device_connected = False
                            self.device_connected_update = True
                            self.pygame_device_added_update = False

                        elif (self.mod_pygame__.joystick.get_count() >= 1 and
                                self.pygame_device_added_update is False):

                            self.device_connected = True
                            self.device_connected_update = True
                            self.DeviceRemoved_Update = True
                            self.pygame_device_added_update = True
                            self.pygame_device_removed_update = False
                            self.joystick_connected = True
                            
                except Exception as Message:
                    log_message = "JoystickUtils > establish_joystick_connection > JoystickRemoved: " + \
                        str(Message)

                    self.mod_logging_utils__.create_log_message.update_log_warning(
                        self,
                        log_message)

                finally:
                    self.mod_time__.sleep(1)

            self.mod_logging_utils__.create_log_message.update_log_information(
                self,
                "'thread_joystick_removed' has stopped")

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
