if __name__ != "__main__":
    print("Started <Pycraft_JoystickUtils>")

    class EstablishJoystickRemoved:
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
                except:
                    pass
                finally:
                    self.mod_time__.sleep(1)

            print("'thread_joystick_removed' has stopped")


    class EstablishJoystickConnection:
        def __init__(self):
            pass

        def JoystickEvents(self):
            def print_add(joy):
                pass

            def print_remove(joy):
                pass

            def key_received(key):
                import os
                if ("site-packages" in os.path.dirname(__file__) or
                        "dist-packages" in os.path.dirname(__file__)):
                    try:
                        from pycraft.ShareDataUtils import Game_SharedData
                    except:
                        from ShareDataUtils import Game_SharedData
                else:
                    from ShareDataUtils import Game_SharedData

                try:
                    if self.use_mouse_input is False:
                        if self.command == "Play":
                            if "Button" in str(key) or "Hat" in str(key):
                                self.joystick_confirm_toggle = not self.joystick_confirm_toggle

                                if self.joystick_confirm_toggle:
                                    if "Button 3" in str(key) and Game_SharedData.Jump is False:
                                        Game_SharedData.Jump = True
                                        Game_SharedData.JumpUP = True

                                        Ypos = Game_SharedData.camera.position.y
                                        Game_SharedData.StartYposition = Ypos

                                        eFPS = Game_SharedData.SharedData.eFPS
                                        Game_SharedData.Jump_Start_FPS = eFPS

                                    if "Hat" in str(key):
                                        Game_SharedData.SharedData.mod_base__.CameraWindow.close(
                                            Game_SharedData)

                                    else:
                                        if "Button 7" in str(key):
                                            Game_SharedData.SharedData.mod_base__.CameraWindow.key_event(
                                                Game_SharedData,
                                                Game_SharedData.wnd.keys.E,
                                                Game_SharedData.wnd.keys.ACTION_PRESS,
                                                None)

                                        elif "Button 6" in str(key):
                                            Game_SharedData.SharedData.mod_base__.CameraWindow.key_event(
                                                Game_SharedData,
                                                Game_SharedData.wnd.keys.R,
                                                Game_SharedData.wnd.keys.ACTION_PRESS,
                                                None)

                                        else:
                                            self.joystick_confirm = True
                                else:
                                    self.joystick_confirm = False

                            if "Axis" in str(key):
                                if "Axis 3" in str(key):
                                    Axis3value = self.mod_pyjoystick__.Key.get_value(key)
                                    Game_SharedData.Joystick_Rotation[0] = Axis3value

                                if "Axis 4" in str(key):
                                    Axis4value = self.mod_pyjoystick__.Key.get_value(key)
                                    Game_SharedData.Joystick_Rotation[1] = Axis4value

                                if "Axis 1" in str(key):
                                    try:
                                        if self.mod_pyjoystick__.Key.get_value(key) < -0.25:
                                            Game_SharedData.SharedData.mod_base__.CameraWindow.key_event(
                                                Game_SharedData,
                                                Game_SharedData.wnd.keys.W,
                                                Game_SharedData.wnd.keys.ACTION_PRESS,
                                                None)

                                        else:
                                            Game_SharedData.SharedData.mod_base__.CameraWindow.key_event(
                                                Game_SharedData,
                                                Game_SharedData.wnd.keys.W,
                                                Game_SharedData.wnd.keys.ACTION_RELEASE,
                                                None)

                                        if self.mod_pyjoystick__.Key.get_value(key) > 0.25:
                                            Game_SharedData.SharedData.mod_base__.CameraWindow.key_event(
                                                Game_SharedData,
                                                Game_SharedData.wnd.keys.S,
                                                Game_SharedData.wnd.keys.ACTION_PRESS,
                                                None)

                                        else:
                                            Game_SharedData.SharedData.mod_base__.CameraWindow.key_event(
                                                Game_SharedData,
                                                Game_SharedData.wnd.keys.S,
                                                Game_SharedData.wnd.keys.ACTION_RELEASE,
                                                None)
                                    except Exception as Message:
                                        print(Message)

                                if "Axis 0" in str(key):
                                    try:
                                        if self.mod_pyjoystick__.Key.get_value(key) < -0.25:
                                            Game_SharedData.SharedData.mod_base__.CameraWindow.key_event(
                                                Game_SharedData,
                                                Game_SharedData.wnd.keys.A,
                                                Game_SharedData.wnd.keys.ACTION_PRESS,
                                                None)

                                        else:
                                            Game_SharedData.SharedData.mod_base__.CameraWindow.key_event(
                                                Game_SharedData,
                                                Game_SharedData.wnd.keys.A,
                                                Game_SharedData.wnd.keys.ACTION_RELEASE,
                                                None)

                                        if self.mod_pyjoystick__.Key.get_value(key) > 0.25:
                                            Game_SharedData.SharedData.mod_base__.CameraWindow.key_event(
                                                Game_SharedData,
                                                Game_SharedData.wnd.keys.D,
                                                Game_SharedData.wnd.keys.ACTION_PRESS,
                                                None)

                                        else:
                                            Game_SharedData.SharedData.mod_base__.CameraWindow.key_event(
                                                Game_SharedData,
                                                Game_SharedData.wnd.keys.D,
                                                Game_SharedData.wnd.keys.ACTION_RELEASE,
                                                None)
                                    except Exception as Message:
                                        print(Message)

                        else:
                            self.joystick_mouse = [0, 0]
                            if "Button" in str(key):
                                self.joystick_confirm_toggle = not self.joystick_confirm_toggle

                                if self.joystick_confirm_toggle:
                                    if "Button 3" in str(key):
                                        self.joystick_exit = True

                                    else:
                                        if "Button 2" in str(key):
                                            self.joystick_zoom = "+"

                                        elif "Button 1" in str(key):
                                            self.joystick_zoom = "-"

                                        elif "Button 0" in str(key):
                                            self.joystick_reset = True

                                        self.joystick_exit = False
                                        self.joystick_confirm = True

                                else:
                                    self.joystick_confirm = False

                            if "Hat" in str(key):
                                self.joystick_hat_pressed = True
                                self.joystick_mouse = [0, 0]

                                if "Right" in str(key):
                                    self.joystick_mouse[0] = "Right"

                                if "Left" in str(key):
                                    self.joystick_mouse[0] = "Left"

                                if  "Up" in str(key):
                                    self.joystick_mouse[1] = "Up"

                                if  "Down" in str(key):
                                    self.joystick_mouse[1] = "Down"
                            else:
                                self.joystick_hat_pressed = False

                except Exception as Message:
                    self.error_message = "".join(("JoystickUtils > EstablishJoystickConnection ",
                                                 "> JoystickEvents > ",
                                                 f"key_received: {str(Message)}"))

                    self.error_message_detailed = "".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)
            try:
                while True:
                    self.mod_pyjoystick_run_event_loop_(print_add, print_remove, key_received)
            except Exception as Message:
                self.error_message = "".join(("JoystickUtils > GenerateHomeScreen > ",
                                             f"JoystickEvents: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

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
