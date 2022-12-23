if __name__ != "__main__":
    try:
        import os
        import time
        import traceback

        import pygame
        
        import caption_utils
        import display_utils
        import drawing_utils
        import error_utils
        import text_utils
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
            
    class generate_character_designer:
        """
        This class is in charge of rendering the character customiser GUI, currently
        this is just a black window as we need to get the game engine right and work on
        a character model, in later versions the character will hopefully be rendered in
        3D and the result (as well as any changes), should be able to be viewed live.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        
        def __init__(self):
            pass

        def character_designer_gui(self):
            """
            This subroutine does the bulk of the rendering for the character customiser GUI, currently
            this is just a black window as we need to get the game engine right and work on
            a character model, in later versions the character will hopefully be rendered in
            3D and the result (as well as any changes), should be able to be viewed live.
            
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
                caption_utils.generate_captions.get_normal_caption(
                    "Character Designer",
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

                title_width = 0

                while True:
                    start_time = time.perf_counter()

                    if not (self.error_message is None or self.error_message_detailed is None):
                        error_utils.generate_error_screen.error_screen(
                            self.logging_dictionary,
                            self.output_log,
                            self.detailed_error_messages,
                            self.error_message,
                            self.error_message_detailed,
                            self.platform,
                            self.base_folder)

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
                            self.error_message_detailed)

                    caption_utils.generate_captions.get_normal_caption(
                        "Character Designer",
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

                    self.display.fill(self.background_color)

                    cover_Rect = pygame.Rect(
                        0,
                        0,
                        1280,
                        90)

                    pygame.draw.rect(
                        self.display,
                        self.background_color,
                        cover_Rect)

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
                        _) = text_utils.text_formatter.format_text(
                        "Character Designer",
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

                    (self.data_average_fps,
                        self.data_CPU_usage,
                        self.data_current_fps,
                        self.data_memory_usage,
                        self.timer,
                        self.data_average_fps_Max,
                        self.data_CPU_usage_Max,
                        self.data_current_fps_Max,
                        self.data_memory_usage_Max,
                        self.current_memory_usage) = drawing_utils.generate_graph.create_devmode_graph(
                        self.small_content_font,
                        self.draw_devmode_graph,
                        self.real_window_width,
                        self.data_average_fps,
                        self.data_CPU_usage,
                        self.data_current_fps,
                        self.data_memory_usage,
                        self.timer,
                        self.data_average_fps_Max,
                        self.data_CPU_usage_Max,
                        self.data_current_fps_Max,
                        self.data_memory_usage_Max,
                        self.display,
                        self.shape_color,
                        self.average_fps,
                        self.iteration,
                        self.current_fps,
                        self.fps_overclock,
                        self.aa,
                        self.fps,
                        self.current_memory_usage)

                    if self.go_to is None:
                        self.startup_animation = display_utils.display_animations.fade_in(
                            self.startup_animation,
                            self.real_window_width,
                            self.real_window_height,
                            self.run_timer,
                            self.background_color,
                            self.display)
                            
                    else:
                        self.startup_animation = display_utils.display_animations.fade_out(
                            self.startup_animation,
                            self.real_window_width,
                            self.real_window_height,
                            self.run_timer,
                            self.background_color,
                            self.display,
                            self.go_to)

                    if self.startup_animation is False and (self.go_to is not None):
                        return None

                    target_fps, self.project_sleeping = display_utils.display_utils.get_play_status(
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

                    pygame.display.flip()
                    self.clock.tick(target_fps)

                    self.run_timer += time.perf_counter()-start_time
                    
            except Exception as Message:
                error_message = "".join(("character_designer > ",
                                             "generate_character_designer > ",
                                             f"character_designer: {str(Message)}"))

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
