if __name__ != "__main__":
    try:
        import traceback
        import os

        import pygame
        
        import caption_utils
        import display_utils
        import error_utils
        import sound_utils
        import theme_utils
        import input_utility
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
            
    class determine_theme_colours:
        def __init__(self):
            pass

        def get_colors(self, theme, custom_theme, colour_presets):
            themeArray = [
                [(255, 255, 255),
                    [30, 30, 30],
                    (80, 80, 80),
                    (237, 125, 49),
                    (255, 255, 255)],

                [(0, 0, 0),
                    [255, 255, 255],
                    (80, 80, 80),
                    (237, 125, 49),
                    (100, 100, 100)]]

            if theme == "dark":
                font_color = themeArray[0][0]
                background_color = themeArray[0][1]
                shape_color = themeArray[0][2]
                accent_color = themeArray[0][3]
                secondary_font_color = themeArray[0][4]

            elif theme == "light":
                font_color = themeArray[1][0]
                background_color = themeArray[1][1]
                shape_color = themeArray[1][2]
                accent_color = themeArray[1][3]
                secondary_font_color = themeArray[1][4]

            elif theme == "custom" and not custom_theme is None:
                for i in range(len(list(custom_theme))):
                    argument = str(custom_theme[list(custom_theme)[i]])
                    input_result = input_utility.identify_patterns.identify_rgb(argument)
                    if input_result is False:
                        input_result = input_utility.identify_patterns.identify_hex(argument[1:-1])
                        if input_result is False:
                            input_result = input_utility.identify_patterns.identify_text(argument, colour_presets)
                            if not input_result is False:
                                self.__dict__[list(custom_theme)[i]] = input_result
                        else:
                            self.__dict__[list(custom_theme)[i]] = input_result
                    else:
                        self.__dict__[list(custom_theme)[i]] = input_result

                
                return (themeArray,
                    self.font_color,
                    self.background_color,
                    self.shape_color,
                    self.accent_color,
                    self.secondary_font_color)
                
            else:
                font_color = themeArray[0][0]
                background_color = themeArray[0][1]
                shape_color = themeArray[0][2]
                accent_color = themeArray[0][3]
                secondary_font_color = themeArray[0][4]
                
            return (themeArray,
                        font_color,
                        background_color,
                        shape_color,
                        accent_color,
                        secondary_font_color)
                
        def get_theme_gui(self):
            try:
                Title = self.title_font.render(
                    "Pycraft",
                    True,
                    self.font_color)
                title_width = Title.get_width()

                if self.platform == "Linux":
                    MiddleFont = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    SideFont = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 20)

                else:
                    MiddleFont = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    SideFont = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 20)

                self.mouse_button_down = False

                DarkModeFont = MiddleFont.render(
                    "Dark",
                    True,
                    self.font_color)
                DarkModeFont_Width = DarkModeFont.get_width()
                DarkModeFont_Height = DarkModeFont.get_height()

                LightModeFont = MiddleFont.render(
                    "Light",
                    True,
                    self.font_color)
                LightModeFont_Width = LightModeFont.get_width()
                LightModeFont_Height = LightModeFont.get_height()

                self.mouse_x = self.real_window_width/2
                self.mouse_y = self.real_window_height/2

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
                        self.fullscreen) = display_utils.display_functionality.core_display_functions(
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
                            location="saveANDexit")

                    caption_utils.generate_captions.get_normal_caption(
                        "Theme selector",
                        self.detailed_captions,
                        self.play_time,
                        self.x,
                        self.y,
                        self.z,
                        self.total_move_x,
                        self.total_move_y,
                        self.total_move_z,
                        self.fps_overclock,
                        self.current_fps,
                        self.iteration,
                        self.version,
                        self.current_memory_usage,
                        self.theme,
                        self.fps,
                        self.average_fps)

                    LightRect = pygame.Rect(
                        0,
                        100,
                        self.real_window_width/2,
                        self.real_window_height-200)

                    DarkRect = pygame.Rect(
                        self.real_window_width/2,
                        100,
                        self.real_window_width/2,
                        self.real_window_height-200)

                    self.display.fill(self.background_color)

                    Title = self.title_font.render(
                        "Pycraft",
                        True,
                        self.font_color)
                    title_width = Title.get_width()

                    self.display.blit(
                        Title,
                        ((self.real_window_width-title_width)/2, 0))

                    self.theme = "light"
                    
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

                    pygame.draw.rect(
                        self.display,
                        self.background_color,
                        LightRect)

                    pygame.draw.rect(
                        self.display,
                        self.shape_color,
                        LightRect,
                        3)

                    LightModeFont = MiddleFont.render(
                        "Light",
                        True,
                        self.font_color)
                    LightModeFont_Width = LightModeFont.get_width()
                    LightModeFont_Height = LightModeFont.get_height()

                    self.display.blit(
                        LightModeFont,
                        (((self.real_window_width/2)-LightModeFont_Width)/2,
                            (self.real_window_height-LightModeFont_Height)/2))

                    self.theme = "dark"
                    
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

                    pygame.draw.rect(
                        self.display,
                        self.background_color,
                        DarkRect)

                    pygame.draw.rect(
                        self.display,
                        self.shape_color,
                        DarkRect,
                        3)

                    DarkModeFont = MiddleFont.render(
                        "Dark",
                        True,
                        self.font_color)
                    DarkModeFont_Width = DarkModeFont.get_width()
                    DarkModeFont_Height = DarkModeFont.get_height()

                    self.display.blit(
                        DarkModeFont,
                        (((self.real_window_width+(self.real_window_width/2))-DarkModeFont_Width)/2,
                            (self.real_window_height-DarkModeFont_Height)/2))

                    if self.mouse_y >= 100 and self.mouse_y <= self.real_window_height-100:
                        if self.mouse_x <= self.real_window_width/2:
                            pygame.draw.rect(
                                self.display,
                                self.accent_color,
                                LightRect,
                                1)

                            self.theme = "light"

                            if self.mouse_button_down:
                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)

                                break

                        elif self.mouse_x >= self.real_window_width/2:
                            pygame.draw.rect(
                                self.display,
                                self.accent_color,
                                DarkRect,
                                1)

                            self.theme = "dark"
                            if self.mouse_button_down:
                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)
                                        
                                break

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

                    Choice = SideFont.render(
                        "".join((f"You have selected the {self.theme} ",
                                 "theme, you can change this later in settings")),

                        self.aa,
                        self.font_color)
                    ChoiceWidth = Choice.get_width()
                    choice_height = Choice.get_height()

                    self.display.blit(
                        Choice,
                        ((self.real_window_width-ChoiceWidth)/2,
                            (self.real_window_height-choice_height)))

                    pygame.display.update()
                    self.clock.tick(self.fps)
                    
            except Exception as Message:
                error_message = "".join(("theme_utils > determine_theme_colours ",
                                             f"> get_theme_gui: {str(Message)}"))

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
