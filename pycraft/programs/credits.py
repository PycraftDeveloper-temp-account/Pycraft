if __name__ != "__main__":
    try:
        import os
        import time
        import traceback
        import json

        import pygame
        
        import caption_utils
        import display_utils
        import drawing_utils
        import text_utils
        import error_utils
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
            
    class generate_credits:
        """
        This class is in charge of creating the credits menu from a file called
        'credits_config.json' in the 'data files' folder.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        
        def __init__(self):
            pass

        def credits_gui(self):
            """
            This subroutine is in charge of creating the credits menu from a file called
            'credits_config.json' in the 'data files' folder. Every key has a purpose, with
            the '<spacerN>' syntax being used to specify any spaces or breaks to make the
            credits menu easier to read. (The 'N' being used to count the number of spaces as
            without this the spacer gets ignored.)
            
            - Args:
                - None
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            try:
                caption_utils.generate_captions.get_normal_caption(
                    "Credits",
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

                if self.platform == "Linux":
                    with open(
                        os.path.join(
                            self.base_folder,
                            ("data files//credits_config.json")), "r") as file:

                        credits_data = json.load(file)

                else:
                    with open(
                        os.path.join(
                            self.base_folder,
                            ("data files\\credits_config.json")), "r") as file:

                        credits_data = json.load(file)

                structure = []
                for key in credits_data:
                    if "<spacer" in key:
                        structure.append(" ")
                    else:
                        title = key
                        if "{self.version}" in title:
                            title = title.replace("{self.version}", f"{self.version}")
                        structure.append(title)
                        if str(type(credits_data[key])) == "<class 'list'>":
                            for item in credits_data[key]:
                                structure.append(item)
                        elif str(type(credits_data[key])) == "<class 'str'>":
                            structure.append(credits_data[key])


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
                title_height = returned_text.get_height()

                credits_structure = structure

                VisualYdisplacement = self.real_window_height
                IntroYDisplacement = (self.real_window_height-title_height)/2
                timer = 5

                HoldOnExit = False
                Holdtimer = 0

                LoadText = False
                while True:
                    start_time = time.perf_counter()

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

                    caption_utils.generate_captions.get_normal_caption(
                        "Credits",
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

                    self.display.fill(self.background_color)

                    Ypos = 0
                    for i in range(len(credits_structure)):
                        if LoadText:
                            if i > 0:
                                if credits_structure[i-1] == " ":
                                    (self.translated_text,
                                        returned_text) = text_utils.text_formatter.format_text(
                                        credits_structure[i],
                                        self.language,
                                        self.display,
                                        ("left", "top"),
                                        self.font_color,
                                        self.aa,
                                        False,
                                        False,
                                        False,
                                        self.large_content_font,
                                        self.large_content_backup_font,
                                        self.translated_text,
                                        self.logging_dictionary,
                                        self.output_log,
                                        self.platform,
                                        self.base_folder,
                                        self.connection_permission,
                                        blit=False)
                                        
                                else:
                                    (self.translated_text,
                                        returned_text) = text_utils.text_formatter.format_text(
                                        credits_structure[i],
                                        self.language,
                                        self.display,
                                        ("left", "top"),
                                        self.font_color,
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
                                        self.connection_permission,
                                        blit=False)
                                        
                            else:
                                (self.translated_text,
                                    returned_text) = text_utils.text_formatter.format_text(
                                    credits_structure[i],
                                    self.language,
                                    self.display,
                                    ("left", "top"),
                                    self.font_color,
                                    self.aa,
                                    False,
                                    False,
                                    False,
                                    self.large_content_font,
                                    self.large_content_backup_font,
                                    self.translated_text,
                                    self.logging_dictionary,
                                    self.output_log,
                                    self.platform,
                                    self.base_folder,
                                    self.connection_permission,
                                    blit=False)

                            TextSurfaceHeight = returned_text.get_height()
                            TextSurfaceWidth = returned_text.get_width()

                            if TextSurfaceWidth > self.real_window_width:
                                (displacement,
                                    self.translated_text) = text_utils.TextWrap.blit_text(
                                        credits_structure[i],
                                        (3, Ypos+VisualYdisplacement),
                                        self.small_content_font,
                                        self.small_content_backup_font,
                                        self.font_color,
                                        self.real_window_width,
                                        self.display,
                                        self.aa,
                                        self.language,
                                        self.translated_text,
                                        self.logging_dictionary,
                                        self.output_log,
                                        self.platform,
                                        self.base_folder,
                                        self.connection_permission)
                                    
                                Ypos += displacement
                                
                            else:
                                if i+1 == len(credits_structure) and HoldOnExit:
                                    TextSurface_x_pos = (self.real_window_width-TextSurfaceWidth)/2
                                    TextSurface_y_pos = (self.real_window_height-TextSurfaceHeight)/2

                                    self.display.blit(
                                        returned_text,
                                        (TextSurface_x_pos, TextSurface_y_pos))
                                else:
                                    if (Ypos+VisualYdisplacement >= 0 and
                                        Ypos+VisualYdisplacement <= self.real_window_height):

                                        TextSurface_x_pos = (self.real_window_width-TextSurfaceWidth)/2
                                        TextSurface_y_pos = Ypos+VisualYdisplacement

                                        self.display.blit(
                                            returned_text,
                                            (TextSurface_x_pos, TextSurface_y_pos))

                            Ypos += TextSurfaceHeight

                    if timer >= 1:
                        (self.translated_text,
                            returned_text) = text_utils.text_formatter.format_text(
                            "Pycraft",
                            self.language,
                            self.display,
                            ("center", 0+IntroYDisplacement),
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

                        timer -= 1/(self.average_fps/self.iteration)
                        VisualYdisplacement = self.real_window_height
                    else:
                        if IntroYDisplacement <= 0:
                            cover_Rect = pygame.Rect(
                                0,
                                0,
                                self.real_window_width,
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
                                ("center", 0+IntroYDisplacement),
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
                                "Credits",
                                self.language,
                                self.display,
                                (((self.real_window_width-title_width)/2)+65, 50),
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

                            VisualYdisplacement -= 60/(self.average_fps/self.iteration)
                            LoadText = True
                            if Ypos+VisualYdisplacement <= self.real_window_height/2:
                                HoldOnExit = True
                                Holdtimer += 1/(self.average_fps/self.iteration)
                                if Holdtimer >= 5:
                                    self.go_to = "home"
                        else:
                            cover_Rect = pygame.Rect(
                                0,
                                0,
                                self.real_window_width,
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
                                ("center", 0+IntroYDisplacement),
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
                                "Credits",
                                self.language,
                                self.display,
                                (((self.real_window_width-title_width)/2)+65, 50+IntroYDisplacement),
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

                            IntroYDisplacement -= 90/(self.average_fps/self.iteration)
                            VisualYdisplacement = self.real_window_height

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
                error_message = "credits > generate_credits > credits: "+str(Message)
                
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
