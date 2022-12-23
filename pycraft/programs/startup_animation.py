if __name__ != "_main_":
    try:
        import traceback
        import os
        import threading
        import time
        
        import pygame
        
        import theme_utils
        import display_utils
        import error_utils
        import pycraft_startup_utils
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
            
    class generate_startup_gui:
        """
        This class is in charge of running the startup menu and also creating a thread that
        checks Pycraft's directory for required resources.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        
        def _init_(self):
            pass

        def startup_gui(self):
            """
            This subroutine is in charge of running the startup menu and also creating a thread that
            checks Pycraft's directory for required resources. This GUI runs before the theme decision
            menu, so if the user hasn't already set a theme then the startup animation will default
            to default. (The default theme for Pycraft is 'dark').
            
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
                if self.theme is False:
                    self.theme = "dark"
                    update_theme_later = True
                    
                else:
                    update_theme_later = False

                (self.themeArray,
                    self.font_color,
                    self.background_color,
                    self.shape_color,
                    self.accent_color,
                    self.secondary_font_color) = theme_utils.determine_theme_colours.get_colors(
                        self,
                        self.theme,
                        self.custom_theme,
                        self.colour_presets)

                if update_theme_later:
                    self.theme = False
                
                if self.platform == "Linux":
                    PresentsFont = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 35)

                    PycraftFont = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 60)

                    NameFont = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 45)

                else:
                    PresentsFont = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 35)

                    PycraftFont = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 60)

                    NameFont = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 45)

                NameText = NameFont.render(
                    "PycraftDev",
                    True,
                    self.font_color)
                NameTextWidth = NameText.get_width()
                NameTextHeight = NameText.get_height()

                self.real_window_width = pygame.display.get_window_size()[0]
                self.real_window_height = pygame.display.get_window_size()[1]

                self.display.fill(self.background_color)
                
                pygame.display.flip()
                pygame.display.set_caption(f"Pycraft: v{self.version}: Welcome")

                PresentsText = PresentsFont.render(
                    "presents",
                    True,
                    self.font_color)

                presentOffSet = 39

                PycraftText = PycraftFont.render(
                    "Pycraft",
                    True,
                    self.font_color)
                TitleTextWidth = PycraftText.get_width()

                PycraftStartPos = pygame.Vector2(
                    ((self.real_window_width-TitleTextWidth)/2,
                        self.real_window_height/2 - NameTextHeight))

                PycraftEndPos = pygame.Vector2(
                    PycraftStartPos.x,
                    0)

                self.clock = pygame.time.Clock()

                InterpolateSpeed = 0.02

                timer = 2

                while timer > 0 and self.run_full_startup:
                    (_,
                        self.display,
                        self.mouse_button_down,
                        self.go_to,
                        self.startup_animation,
                        self.run_timer,
                        self.current_fps,
                        self.average_fps,
                        self.iteration,
                        self.saved_window_width,
                        self.saved_window_height,
                        self.window_in_focus,
                        self.joystick_exit,
                        self.x_scale_factor,
                        self.y_scale_factor,
                        self.real_window_width,
                        self.real_window_height,
                        self.mouse_x,
                        self.mouse_y,
                        self.data_average_fps,
                        self.data_CPU_usage,
                        self.data_current_fps,
                        self.data_memory_usage,
                        self.timer,
                        self.data_average_fps_Max,
                        self.data_CPU_usage_Max,
                        self.data_current_fps_Max,
                        self.data_memory_usage_Max,
                        self.joystick_zoom,
                        self.clock,
                        self.joystick_hat_pressed,
                        self.fullscreen,
                        self.joystick_connected) = display_utils.display_functionality.core_display_functions(
                            self.platform,
                            self.base_folder,
                            self.display,
                            self.use_mouse_input,
                            self.average_fps,
                            self.iteration,
                            self.mouse_x,
                            self.mouse_y,
                            self.x_scale_factor,
                            self.y_scale_factor,
                            self.go_to,
                            self.joystick_exit,
                            self.joystick_hat_pressed,
                            self.window_in_focus,
                            self.saved_window_width,
                            self.saved_window_height,
                            self.clock,
                            self.sound,
                            self.input_key,
                            self.input_configuration,
                            self.extended_developer_options,
                            self.logging_dictionary,
                            self.output_log,
                            self.vsync,
                            self.window_icon,
                            self.sound_volume,
                            self,
                            self.version,
                            self.background_color,
                            self.font_color,
                            self.fullscreen,
                            self.startup_animation,
                            self.run_timer,
                            self.data_average_fps,
                            self.data_CPU_usage,
                            self.data_current_fps,
                            self.data_memory_usage,
                            self.timer,
                            self.data_average_fps_Max,
                            self.data_CPU_usage_Max,
                            self.data_current_fps_Max,
                            self.data_memory_usage_Max,
                            self.joystick_zoom,
                            self.mouse_button_down,
                            self.error_message,
                            self.error_message_detailed,
                            location="exit",
                            resize=False)

                    self.display.fill(self.background_color)
                    
                    timer -= 0.01

                    self.display.blit(
                        NameText,
                        ((self.real_window_width-NameTextWidth)/2,
                            self.real_window_height/2 - NameTextHeight))

                    if timer <= 1:
                        self.display.blit(
                            PresentsText,
                            ((self.real_window_width-NameTextWidth)/2 + presentOffSet,
                                self.real_window_height/2 + NameTextHeight - 77))

                    pygame.display.flip()
                    self.clock.tick(60)

                Thread_ResourceCheck = threading.Thread(
                    target=pycraft_startup_utils.startup_test.pycraft_resource_test,
                    args=(self, False,))
                Thread_ResourceCheck.name = "Thread_ResourceCheck"
                Thread_ResourceCheck.start()

                runtimer = 0

                while True:
                    (_,
                        self.display,
                        self.mouse_button_down,
                        self.go_to,
                        self.startup_animation,
                        self.run_timer,
                        self.current_fps,
                        self.average_fps,
                        self.iteration,
                        self.saved_window_width,
                        self.saved_window_height,
                        self.window_in_focus,
                        self.joystick_exit,
                        self.x_scale_factor,
                        self.y_scale_factor,
                        self.real_window_width,
                        self.real_window_height,
                        self.mouse_x,
                        self.mouse_y,
                        self.data_average_fps,
                        self.data_CPU_usage,
                        self.data_current_fps,
                        self.data_memory_usage,
                        self.timer,
                        self.data_average_fps_Max,
                        self.data_CPU_usage_Max,
                        self.data_current_fps_Max,
                        self.data_memory_usage_Max,
                        self.joystick_zoom,
                        self.clock,
                        self.joystick_hat_pressed,
                        self.fullscreen,
                        self.joystick_connected) = display_utils.display_functionality.core_display_functions(
                            self.platform,
                            self.base_folder,
                            self.display,
                            self.use_mouse_input,
                            self.average_fps,
                            self.iteration,
                            self.mouse_x,
                            self.mouse_y,
                            self.x_scale_factor,
                            self.y_scale_factor,
                            self.go_to,
                            self.joystick_exit,
                            self.joystick_hat_pressed,
                            self.window_in_focus,
                            self.saved_window_width,
                            self.saved_window_height,
                            self.clock,
                            self.sound,
                            self.input_key,
                            self.input_configuration,
                            self.extended_developer_options,
                            self.logging_dictionary,
                            self.output_log,
                            self.vsync,
                            self.window_icon,
                            self.sound_volume,
                            self,
                            self.version,
                            self.background_color,
                            self.font_color,
                            self.fullscreen,
                            self.startup_animation,
                            self.run_timer,
                            self.data_average_fps,
                            self.data_CPU_usage,
                            self.data_current_fps,
                            self.data_memory_usage,
                            self.timer,
                            self.data_average_fps_Max,
                            self.data_CPU_usage_Max,
                            self.data_current_fps_Max,
                            self.data_memory_usage_Max,
                            self.joystick_zoom,
                            self.mouse_button_down,
                            self.error_message,
                            self.error_message_detailed,
                            location="exit",
                            resize=False)

                    RefreshTime = time.perf_counter()

                    self.display.fill(self.background_color)

                    if "Thread_ResourceCheck" not in str(threading.enumerate()):
                        if not (self.error_message is None or
                                    self.error_message_detailed is None):
                            
                            error_utils.generate_error_screen.error_screen(
                                self.logging_dictionary,
                                self.output_log,
                                self.detailed_error_messages,
                                self.error_message,
                                self.error_message_detailed,
                                self.platform,
                                self.base_folder)
                            
                        PycraftStartPos = pygame.math.Vector2.lerp(
                            PycraftStartPos,
                            PycraftEndPos,
                            InterpolateSpeed)

                    self.display.blit(
                        PycraftText,
                        (PycraftStartPos.x, PycraftStartPos.y))

                    pygame.display.flip()
                    self.clock.tick(60)

                    if PycraftStartPos.y <= 1:
                        PycraftStartPos = PycraftEndPos
                        self.run_full_startup = False
                        break

                    runtimer += time.perf_counter()-RefreshTime

            except Exception as Message:
                error_message = "".join(("StartupAnimation > generate_startup_gui ",
                                             f"> Start: {str(Message)}"))

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
