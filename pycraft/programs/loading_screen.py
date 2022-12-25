if __name__ != "__main__":
    try:
        import sys
        import os
        import traceback
        import time
        
        import pygame
        import pyautogui

        import display_utils
        import caption_utils
        import error_utils
        import file_utils
        import text_utils
        import drawing_utils
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
            
    class generate_load_screen:
        """
        This class is in charge of setting up, managing, loading and running the
        loading GUI. This GUI gets loaded as a separate process at the start
        of the game engine and runs whilst the game engine loads to indicate that
        Pycraft hasn't crashed and how far through loading the game engine we are.
        This is run in parallel (process).
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        
        def __init__(
                self,
                dictionary):
            """
            This class is in charge of turning the dictionary the user enters as
            a parameter (that contains all the data required to properly display
            the loading screen GUI) into a 'generate_load_screen' object in a similar
            style to the 'pycraft_main' program. This also initializes the
            load screen's required modules.
            
            - Args:
                - self (dict): This is used by Pycraft as a way of storing it's current
                    configuration and behaviour and is required by most GUIs. Its use should be
                    reduced where possible for readability reasons.
                - dictionary (dict): This parameter holds all the data that is stored 
                    as 'self' in the game engine. This includes the configuration and
                    user defined settings. Note that the input to this variable must
                    be sorted first to remove any modules or module specific objects.
                    For example a (Pygame Surface) type object as that will cause errors
                    when creating the new process.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            for key in dictionary:
                setattr(self, key, dictionary[key])

            pygame.init()

        def load(
                dictionary,
                start_loading,
                additional_data):
            """
            This subroutine is in charge of loading and running the
            loading GUI. This GUI gets loaded as a separate process at the start
            of the game engine and runs whilst the game engine loads to indicate that
            Pycraft hasn't crashed and how far through loading the game engine we are.
            This is run in parallel (process).
            
            - Args:
                - dictionary (dict): This parameter holds all the data that is stored 
                    as 'self' in the game engine. This includes the configuration and
                    user defined settings. Note that the input to this variable must
                    be sorted first to remove any modules or module specific objects.
                    For example a (Pygame Surface) type object as that will cause errors
                    when creating the new process.
                - start_loading (Multiprocessing Event object): This parameter is an
                    event object used to tell the load screen when the game engine starts
                    to load. When this event is not set the load screen will wait to be
                    called again.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            self = generate_load_screen(dictionary)
            try:
                self.input_key = file_utils.pycraft_config_utils.read_input_key(
                    self.platform,
                    self.base_folder)
                
                if self.platform == "Linux":
                    self.title_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 60)

                    self.title_backup_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//NotoSans-Regular.ttf")), 60)

                    self.subtitle_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 35)

                    self.subtitle_backup_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//NotoSans-Regular.ttf")), 35)

                    self.small_content_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                    self.small_content_backup_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//NotoSans-Regular.ttf")), 15)

                    self.window_icon = pygame.image.load(
                        os.path.join(
                            self.base_folder,
                            ("resources//general resources//Icon.png")))

                else:
                    self.title_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 60)

                    self.title_backup_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\NotoSans-Regular.ttf")), 60)

                    self.subtitle_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 35)

                    self.subtitle_backup_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\NotoSans-Regular.ttf")), 35)

                    self.small_content_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                    self.small_content_backup_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\NotoSans-Regular.ttf")), 15)
                    
                    self.window_icon = pygame.image.load(
                        os.path.join(
                            self.base_folder,
                            ("resources\\general resources\\Icon.png")))

                self.clock = pygame.time.Clock()

                self.fullscreen_x, self.fullscreen_y = pyautogui.size()

                self.mouse_x = self.real_window_width/2
                self.mouse_y = self.real_window_height/2

                average_load_time = self.load_time[0]/self.load_time[1]

                while True:
                    start_loading.wait()

                    pygame.display.init()
                    self.data_average_fps = []
                    self.data_CPU_usage = []
                    self.data_current_fps = []
                    self.data_memory_usage = []

                    self.timer = 0

                    self.data_average_fps_Max = 1
                    self.data_CPU_usage_Max = 1
                    self.data_current_fps_Max = 1
                    self.data_memory_usage_Max = 1

                    fullscreen_x = pyautogui.size()[0]
                    fullscreen_y = pyautogui.size()[1]

                    (self.display,
                        self.saved_window_width,
                        self.saved_window_height) = display_utils.display_utils.set_display(
                            self.fullscreen,
                            self.vsync,
                            self.saved_window_width,
                            self.saved_window_height,
                            self.window_icon,
                            self.logging_dictionary,
                            self.output_log,
                            self.platform,
                            self.base_folder,
                            fullscreen_x,
                            fullscreen_y)

                    loading_progress = 0

                    splash_text = text_utils.GenerateText.LoadQuickText(self)

                    start_load_timer = time.perf_counter()

                    while True:
                        current_load_time = time.perf_counter()-start_load_timer
                        if additional_data.poll():
                            loading_progress = additional_data.recv()["loading_progress"]
                        
                        if loading_progress <= 10:
                            text = "Initializing"
                        elif loading_progress <= 20:
                            text = "Creating display"
                        elif loading_progress <= 30:
                            text = "Creating celestial entities"
                        elif loading_progress <= 40:
                            text = "Loading in-game objects: Map"
                        elif loading_progress <= 50:
                            text = "Loading in-game textures: Skysphere"
                        elif loading_progress <= 60:
                            text = "Loading in-game programmes"
                        elif loading_progress <= 70:
                            text = "Applying programme configurations"
                        elif loading_progress <= 80:
                            text = "Loading in-game textures: Grass"
                        else:
                            text = "Making final touches"

                        try:
                            modifier = current_load_time/average_load_time
                        except Exception as message:
                            warning_message = str(message)
                            logging_utils.create_log_message.update_log_warning(
                                self.logging_dictionary,
                                warning_message,
                                self.output_log,
                                self.platform,
                                self.base_folder)
                            
                            modifier = 1

                        percent_complete = modifier*100
                        if percent_complete > 100:
                            percent_complete = 100
                            
                        loading_bar = 100+(modifier*(self.real_window_width-200))

                        if loading_bar > self.real_window_width-100:
                            loading_bar = self.real_window_width-100
                        
                        caption_utils.generate_captions.get_normal_caption(
                            "Loading",
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

                        self.display.fill(self.background_color)

                        (self.translated_text,
                            returned_text) = text_utils.text_formatter.format_text(
                            "Pycraft",
                            self.language,
                            self.display,
                            ("center", "top"),
                            self.font_color,
                            self.aa,
                            False,
                            False,
                            False,
                            self.title_font,
                            self.title_backup_font,
                            self.translated_text,
                            self.logging_dictionary,
                            self.output_log,
                            self.platform,
                            self.base_folder,
                            self.connection_permission)

                        title_width = returned_text.get_width()

                        (self.translated_text,
                            loading_text) = text_utils.text_formatter.format_text(
                            "Loading",
                            self.language,
                            self.display,
                            (((self.real_window_width-title_width)/2)+55, 50),
                            self.secondary_font_color,
                            self.aa,
                            False,
                            False,
                            False,
                            self.subtitle_font,
                            self.subtitle_backup_font,
                            self.translated_text,
                            self.logging_dictionary,
                            self.output_log,
                            self.platform,
                            self.base_folder,
                            self.connection_permission)

                        graphics_size = ((self.real_window_height-120)-(loading_text.get_height()+50))-100
                        
                        drawing_utils.draw_rose.create_rose(
                            False,
                            self.shape_color,
                            (self.real_window_width-graphics_size)/2,
                            (self.real_window_height-graphics_size)/2,
                            graphics_size,
                            graphics_size,
                            self.display)

                        (self.translated_text,
                            _) = text_utils.text_formatter.format_text(
                            text,
                            self.language,
                            self.display,
                            ("center", self.real_window_height-100),
                            self.secondary_font_color,
                            self.aa,
                            False,
                            False,
                            False,
                            self.small_content_font,
                            self.small_content_backup_font,
                            self.translated_text,
                            self.logging_dictionary,
                            self.output_log,
                            self.platform,
                            self.base_folder,
                            self.connection_permission)

                        (self.translated_text,
                            _) = text_utils.text_formatter.format_text(
                            splash_text,
                            self.language,
                            self.display,
                            ("center", self.real_window_height-120),
                            self.secondary_font_color,
                            self.aa,
                            False,
                            False,
                            False,
                            self.small_content_font,
                            self.small_content_backup_font,
                            self.translated_text,
                            self.logging_dictionary,
                            self.output_log,
                            self.platform,
                            self.base_folder,
                            self.connection_permission)

                        (self.translated_text,
                            _) = text_utils.text_formatter.format_text(
                            f"{str(int(percent_complete))}% complete",
                            self.language,
                            self.display,
                            ("center", self.real_window_height-80),
                            self.secondary_font_color,
                            self.aa,
                            False,
                            False,
                            False,
                            self.small_content_font,
                            self.small_content_backup_font,
                            self.translated_text,
                            self.logging_dictionary,
                            self.output_log,
                            self.platform,
                            self.base_folder,
                            self.connection_permission)

                        pygame.draw.line(
                            self.display,
                            self.shape_color,
                            (100, self.real_window_height-100),
                            (100+(self.real_window_width-200), self.real_window_height-100),
                            width=round(self.y_scale_factor))
                        
                        pygame.draw.line(
                            self.display,
                            self.accent_color,
                            (100, self.real_window_height-100),
                            (loading_bar, self.real_window_height-100),
                            width=round(self.y_scale_factor))

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
                                checkEvents=False)

                        if self.joystick_exit:
                            break

                        for event in pygame.event.get():
                            if (event.type == pygame.QUIT or
                                    (event.type == pygame.KEYDOWN and
                                        event.key == pygame.K_ESCAPE) or
                                    (event.type == pygame.KEYDOWN and
                                        event.key == pygame.K_e)):
                                
                                start_loading.clear()
                                pygame.display.quit()

                            if start_loading.is_set():
                                if event.type == pygame.WINDOWFOCUSLOST:
                                    self.window_in_focus = False
                                elif event.type == pygame.WINDOWFOCUSGAINED:
                                    self.window_in_focus = True

                                if event.type == pygame.WINDOWSIZECHANGED:
                                    self.real_window_width = pygame.display.get_window_size()[0]
                                    self.real_window_height = pygame.display.get_window_size()[1]

                        if not start_loading.is_set():
                            break
                        
                        pygame.display.flip()
                        
                        (tempfps,
                            self.project_sleeping) = display_utils.display_utils.get_play_status(
                                self.platform,
                                self.vsync,
                                self.vsync_fps,
                                self.fps,
                                self.project_sleeping,
                                self.command,
                                self.music,
                                self.fps_overclock,
                                self.base_folder,
                                self.music_volume)
                            
                        self.clock.tick(tempfps)

                    pygame.display.quit()
            except Exception as Message:
                error_message = "loading_screen > generate_load_screen > load: "+str(Message)

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
