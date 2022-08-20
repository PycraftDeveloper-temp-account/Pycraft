if __name__ != "__main__":
    print("Started <Pycraft_Base>")

    import moderngl_window as mglw

    class BenchmarkWindow(mglw.WindowConfig):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.camera = self.shared_data.mod_ModernGL_window_keyboard_camera(
                self.wnd.keys,
                aspect_ratio=self.wnd.aspect_ratio)

            self.camera_enabled = True

        def key_event(self, key, action, modifiers):
            try:
                keys = self.wnd.keys


                if action == keys.ACTION_PRESS:
                    self.wnd.close()
                    self.wnd.destroy()
            except Exception as Message:
                try:
                    self.wnd.close()
                    self.shared_data.error_message = "".join(("GLWindowUtils > BenchmarkWindow ",
                                                            f"> key_event: {str(Message)}"))

                    self.shared_data.error_message_detailed = "".join(
                        self.shared_data.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.shared_data.mod_error_utils__.generate_error_screen.error_screen(
                        self.shared_data)
                except Exception as Message:
                    self.shared_data.error_message = "".join(("GLWindowUtils > BenchmarkWindow ",
                                                            f"> key_event: {str(Message)}"))

                    self.shared_data.error_message_detailed = "".join(
                        self.shared_data.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.shared_data.mod_error_utils__.generate_error_screen.error_screen(
                        self.shared_data)

        def close(self):
            try:
                self.shared_data.command = "Undefined"
                self.iteration = 7500
            except Exception as Message:
                self.shared_data.error_message = "GLWindowUtils > BenchmarkWindow > close: " + \
                    str(Message)

                self.shared_data.error_message_detailed = "".join(
                    self.shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.shared_data.mod_error_utils__.generate_error_screen.error_screen(
                    self.shared_data)

    class CameraWindow(mglw.WindowConfig):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.camera = self.shared_data.mod_ModernGL_window_keyboard_camera(
                self.wnd.keys,
                aspect_ratio=self.wnd.aspect_ratio)

            self.camera_enabled = True

        def key_event(self, key, action, modifiers):
            try:
                keys = self.wnd.keys

                if self.camera_enabled:
                    CurrentRunTime = self.shared_data.mod_time__.perf_counter()

                    if key == keys.D:
                        if action == keys.ACTION_PRESS:
                            self.camera.key_input(
                                keys.D,
                                keys.ACTION_PRESS,
                                modifiers)

                            self.Dkeydowntimer_start = CurrentRunTime
                            self.Dkeydown = True

                        elif action == keys.ACTION_RELEASE:
                            self.camera.key_input(
                                keys.D,
                                keys.ACTION_RELEASE,
                                modifiers)

                            self.Dkeydown = False

                    if key == keys.A:
                        if action == keys.ACTION_PRESS:
                            self.camera.key_input(
                                keys.A,
                                keys.ACTION_PRESS,
                                modifiers)

                            self.Akeydowntimer_start = CurrentRunTime
                            self.Akeydown = True

                        elif action == keys.ACTION_RELEASE:
                            self.camera.key_input(
                                keys.A,
                                keys.ACTION_RELEASE,
                                modifiers)

                            self.Akeydown = False

                    if key == keys.W:
                        if action == keys.ACTION_PRESS:
                            self.camera.key_input(
                                keys.W,
                                keys.ACTION_PRESS,
                                modifiers)

                            self.RunForwardtimer = True
                            self.Wkeydown = True

                            self.RunForwardtimer_start = CurrentRunTime
                            self.RunForwardtimer_start_sound = CurrentRunTime

                        elif action == keys.ACTION_RELEASE:
                            self.camera.key_input(
                                keys.W,
                                keys.ACTION_RELEASE,
                                modifiers)

                            self.RunForwardtimer = False
                            self.Wkeydown = False

                    if key == keys.S:
                        if action == keys.ACTION_PRESS:
                            self.camera.key_input(
                                keys.S,
                                keys.ACTION_PRESS,
                                modifiers)

                            self.Skeydown = True
                            self.Skeydowntimer_start = CurrentRunTime

                        elif action == keys.ACTION_RELEASE:
                            self.camera.key_input(
                                keys.S,
                                keys.ACTION_RELEASE,
                                modifiers)

                            self.Skeydown = False

                if action == keys.ACTION_PRESS:
                    if key == keys.L:
                        self.camera_enabled = not self.camera_enabled
                        self.wnd.mouse_exclusivity = self.camera_enabled
                        self.wnd.cursor = not self.camera_enabled

                    elif key == keys.SPACE and self.Jump is False:
                        self.space_key_pressed = True

                    elif key == keys.K and self.shared_data.devmode == 10:
                        self.time += 30
                        self.GameTime += 30
                        self.WeatherTime += 30

                    elif key == keys.I and self.shared_data.devmode == 10:
                        self.IKeyPressed = True

                    elif key == keys.Q and self.shared_data.devmode == 10:
                        self.shared_data.mod_tkinter_utils__.TkinterInfo.CreateTkinterWindow(
                            self.shared_data)

                    elif key == keys.E:
                        self.Inventory = True

                    elif key == keys.R:
                        self.Map = True

                elif action == keys.ACTION_RELEASE:
                    self.IKeyPressed = False
                    self.space_key_pressed = False
            except Exception as Message:
                try:
                    self.wnd.close()
                    self.shared_data.error_message = "".join(("GLWindowUtils > CameraWindow ",
                                                            f"> key_event: {str(Message)}"))

                    self.shared_data.error_message_detailed = "".join(
                        self.shared_data.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.shared_data.mod_error_utils__.generate_error_screen.error_screen(
                        self.shared_data)
                except Exception as Message:
                    self.shared_data.error_message = "".join(("GLWindowUtils > CameraWindow ",
                                                            f"> key_event: {str(Message)}"))

                    self.shared_data.error_message_detailed = "".join(
                        self.shared_data.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.shared_data.mod_error_utils__.generate_error_screen.error_screen(
                        self.shared_data)


        def mouse_position_event(self, x: int, y: int, dx, dy):
            try:
                if self.camera_enabled:
                    self.camera.rot_state(
                        -dx,
                        -dy)
            except Exception as Message:
                self.shared_data.error_message = "".join(("GLWindowUtils > CameraWindow > ",
                                                        f"mouse_position_event: {str(Message)}"))

                self.shared_data.error_message_detailed = "".join(
                    self.shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.shared_data.mod_error_utils__.generate_error_screen.error_screen(self.shared_data)

        def mouse_scroll_event(self, x_offset: float, y_offset: float):
            self.time += y_offset*2
            self.GameTime += y_offset*2
            #if self.weather != "rain.heavy.thundery":
            self.WeatherTime += y_offset*2
            #if self.weather == "rain.heavy.thundery":
            #self.Thundertimer += y_offset*2

        def resize(self, width: int, height: int):
            try:
                self.shared_data.fullscreen = not self.wnd.fullscreen
                self.shared_data.real_window_width, self.shared_data.real_window_height = self.window_size
                self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)
            except Exception as Message:
                self.shared_data.error_message = "".join(("GLWindowUtils > CameraWindow > ",
                                                        f"resize: {str(Message)}"))

                self.shared_data.error_message_detailed = "".join(
                    self.shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.shared_data.mod_error_utils__.generate_error_screen.error_screen(self.shared_data)

        def close(self):
            try:
                self.shared_data.command = "Undefined"
                self.Running = False
            except Exception as Message:
                self.shared_data.error_message = "GLWindowUtils > CameraWindow > close: "+str(Message)

                self.shared_data.error_message_detailed = "".join(
                    self.shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.shared_data.mod_error_utils__.generate_error_screen.error_screen(self.shared_data)

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
