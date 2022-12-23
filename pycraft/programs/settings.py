if __name__ != "__main__":
    try:
        import subprocess
        import sys
        import os
        import time
        import threading
        import json
        from tkinter import messagebox
        import traceback
        
        import pygame

        import pycraft_startup_utils
        import caption_utils
        import display_utils
        import file_utils
        import error_utils
        import sound_utils
        import tkinter_utils
        import drawing_utils
        import settings_utils
        import text_utils
        import translation_utils
        import theme_utils
        import input_utility
        import toggle_utils
        import slider_utils
        import remapping_utils
        import custom_theme_utils
        import button_utils
        import directory_utils
        import dropdown_utils
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
            sys.exit()
            
    class generate_settings:
        """
        This class is in charge of loading the structure for the settings menu, 
        and rendering the settings menu properly.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        
        def __init__(self):
            pass

        def restart_function(
                platform,
                base_folder):
            """
            This subroutine adds restarting functionality into Pycraft. To do this we
            run a command in a separate process 'python main.py' which launches a
            separate instance of Pycraft before we then close the current instance.
            
            - Args:
                - platform (str): This string tells the subroutine which operating
                    system we are using. This is needed for OS specific operations.
                - base_folder (str): This string is a file path to the resources
                    for Pycraft on your device.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            if platform == "Linux":
                subprocess.call(
                    [sys.executable,
                        (str(base_folder) + "main.py")] + sys.argv[1:])
                
            else:
                subprocess.call(
                    [sys.executable,
                    (str(base_folder) + "main.py")] + sys.argv[1:])

        def settings_gui(
                self):
            """
            This subroutine is in charge of rendering the settings menu and applying
            all changes to their corresponding variables throughout Pycraft.
            
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
                    "Settings",
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

                button_offset = 0

                current_menu = "General"
                hover_menu = None

                self.mouse_x = self.real_window_width/2
                self.mouse_y = self.real_window_height/2

                if self.platform == "Linux":
                    with open(
                        os.path.join(
                            self.base_folder,
                            ("data files//settings_config.json")), "r") as openFile:

                        settings_structure = json.load(openFile)

                    selector = pygame.image.load(
                        os.path.join(
                            self.base_folder,
                            (f"resources//general resources//selectorICON{self.theme}.png")))
                    selector.convert()

                else:
                    with open(
                        os.path.join(
                            self.base_folder,
                            ("data files\\settings_config.json")), "r") as openFile:

                        settings_structure = json.load(openFile)

                    selector = pygame.image.load(
                        os.path.join(
                            self.base_folder,
                            (f"resources\\general resources\\selectorICON{self.theme}.png")))
                    selector.convert()

                selector_width = selector.get_width()

                initial_theme = self.theme

                hovering = False
                dropdown_hovering = False
                max_x = 0
                info_offset = 0
                hover_id = None
                files_to_remove = True
                clear_languages = True
                scanned_files = False
                hovering_over_key = False
                scan_directory = False
                maximum_remap_width = 0
                disable_events = False

                scrollbar_needed = False
                general_y_position = 0
                scroll = 0
                dropdown_scroll = 0
                scroll_enabled = True
                
                button_width = 0
                button_height = 0
                title_width = 0

                underline_button = False

                custom_theme_choice = None
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

                    (display_events,
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
                            return_events=True,
                            disable_events=disable_events)

                    for event in display_events:
                        if event.type == pygame.MOUSEWHEEL and dropdown_hovering:
                            if self.use_mouse_input:
                                pygame.mouse.set_cursor(
                                    pygame.SYSTEM_CURSOR_SIZENS)
                                
                                if str(event.y)[0] == "-":
                                    dropdown_scroll -= 1

                                else:
                                    dropdown_scroll += 1

                        else:           
                            if event.type == pygame.MOUSEWHEEL and scrollbar_needed:
                                if self.use_mouse_input:
                                    pygame.mouse.set_cursor(
                                        pygame.SYSTEM_CURSOR_SIZENS)

                                    
                                    if str(event.y)[0] == "-":
                                        if scroll > 0:
                                            scroll -= 5

                                    else:
                                        if scroll_enabled:
                                            scroll += 5

                    caption_utils.generate_captions.get_normal_caption(
                        "Settings",
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
                        returned_text) = text_utils.text_formatter.format_text(
                        "Settings",
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

                    if initial_theme != self.theme:
                        initial_theme = self.theme
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
                            returned_text) = text_utils.text_formatter.format_text(
                            "Settings",
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
                
                        if self.platform == "Linux":
                            selector = pygame.image.load(
                                os.path.join(
                                    self.base_folder,
                                    (f"resources//general resources//selectorICON{self.theme}.png")))
                            selector.convert()

                        else:
                            selector = pygame.image.load(
                                os.path.join(
                                    self.base_folder,
                                    (f"resources\\general resources\\selectorICON{self.theme}.png")))
                            selector.convert()

                        selector_width = selector.get_width()

                    button_y_position = 0
                    button_id = 0
                            
                    for key in settings_structure:
                        
                        if (key == "Developer options" and
                                self.extended_developer_options is False):
                            
                            font_color = self.shape_color
                            underline_button = False
                            
                        else:
                            if key == hover_menu:
                                underline_button = True

                            
                            font_color = self.font_color

                        if button_width > max_x:
                            max_x = button_width
                        
                        button_height += 50 - button_height

                        button_blit_y = (button_y_position * self.y_scale_factor) + button_offset

                        (self.translated_text,
                            returned_text) = text_utils.text_formatter.format_text(
                            key,
                            self.language,
                            self.display,
                            ("right", button_blit_y),
                            font_color,
                            self.aa,
                            underline_button,
                            False,
                            False,
                            self.option_font,
                            self.option_backup_font,
                            self.translated_text,
                            self.logging_dictionary,
                            self.output_log,
                            self.platform,
                            self.base_folder,
                            self.connection_permission)

                        underline_button = False

                        button_width = returned_text.get_width()
                        button_height = returned_text.get_height()

                        button_blit_x = (self.real_window_width-button_width)-2
                        
                        if key == hover_menu:
                            if not (key == "Developer options" and
                                    self.extended_developer_options is False):
                        
                                self.display.blit(
                                    selector,
                                    (self.real_window_width-(button_width+selector_width)-2,
                                        button_blit_y))

                        if ((self.mouse_x > button_blit_x and
                                    self.mouse_x < self.real_window_width and
                                    self.mouse_y > button_blit_y and
                                    self.mouse_y < button_blit_y + button_height) and
                                not (key == "Developer options" and 
                                        self.extended_developer_options is False)):
                            
                            hover_menu = key
                            hovering = True

                            if (self.mouse_button_down and
                                    current_menu != key):
                                
                                current_menu = key
                                scrollbar_needed = False
                                scroll = 0
                                self.mouse_button_down = False
                                
                                if current_menu == "Storage and permissions":
                                    scan_directory = True
                                
                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)
                                    
                        else:
                            if hover_menu == key:
                                hover_menu = None

                        button_y_position += button_height

                        sub_menu = settings_structure[current_menu]

                        general_y_position = 100

                        if scan_directory:
                            scan_directory = False
                            (self.file_structure,
                                self.folder_size) = file_utils.scan_folder.search_files(
                                    self.base_folder,
                                    self.logging_dictionary,
                                    self.output_log,
                                    self.platform,
                                    self.base_folder,
                                    self.file_structure,
                                    self.files_to_trash)

                        if self.clear_languages_cache:
                            self.clear_languages_cache = False
                            
                            if clear_languages:
                                self.translated_text = {}
                                translation_utils.translation_caching.write_cache(
                                    self.platform,
                                    self.base_folder,
                                    self.translated_text)

                                clear_languages = False
                                scan_directory = True

                        if self.clear_cache:
                            self.clear_cache = False
                            
                            if files_to_remove:
                                file_utils.delete_files.clear_temporary_files(
                                    self.platform,
                                    self.base_folder,
                                    self.files_to_trash,
                                    self.logging_dictionary,
                                    self.output_log)

                                files_to_remove = False
                                scan_directory = True

                        if self.scan_pycraft:
                            self.scan_pycraft = False

                            pycraft_startup_utils.startup_test.pycraft_resource_test(
                                self,
                                True)

                            scanned_files = True

                        if self.reset_pycraft:
                            self.reset_pycraft = False

                            theme = self.theme
                            for key in self.save_keys:
                                setattr(self, key, self.save_keys[key])

                            self.theme = theme

                            if self.connection_permission is None:
                                permission_message = "Can we have your permission to check the internet for updates to Pycraft?"
                                self.connection_permission = tkinter_utils.tkinter_info.get_permissions(
                                    permission_message)

                            if self.remove_file_permission is None:
                                permission_message = "Can we have your permission to send files from the Pycraft directory to the recycle bin?"
                                self.remove_file_permission = tkinter_utils.tkinter_info.get_permissions(
                                    permission_message)

                            if self.show_strobe_effects is None:
                                self.show_strobe_effects = messagebox.askquestion(
                                    "Check Permission",
                                    "".join(("Strobe effects and bright flashes of light can ",
                                                "cause discomfort, (for example lightning), you can choose here ",
                                                "whether to enable or disable those ",
                                                "strobe effects in Pycraft.\n",
                                                "Click 'yes' to allow for strobe effects, or 'no' ",
                                                "to turn them off. You can always adjust this in ",
                                                "Pycraft's settings, under 'Storage and permissions'.")))

                                if self.show_strobe_effects == "yes":
                                    self.show_strobe_effects = True

                                else:
                                    self.show_strobe_effects = False
                            
                        if self.exit_mode == "restart":
                            if self.save_on_exit:
                                file_utils.pycraft_config_utils.save_pycraft_config(
                                self)
                                
                            threading.Thread(
                                target=generate_settings.restart_function,
                                args=(self.platform, self.base_folder,)).start()

                            pygame.quit()
                            while True:
                                time.sleep(30)

                        if self.exit_mode == "exit":
                            if self.save_on_exit:
                                file_utils.pycraft_config_utils.save_pycraft_config(
                                self)
                                
                            pygame.quit()
                            sys.exit()

                        if sub_menu[0] is not None:
                            for item in range(len(sub_menu)):
                                data = []
                                mouse_over = False

                                if scrollbar_needed:
                                    scroll_x_offset = 9

                                else:
                                    scroll_x_offset = 0
                                    
                                for entry in range(3, len(sub_menu[item])):
                                    if str(sub_menu[item][entry]) != "directory_structure":
                                        if str(sub_menu[item][entry]) == "average_fps":
                                            argument = int(self.average_fps/self.iteration)

                                        elif str(sub_menu[item][entry]) == "keybinds":
                                            pass
                                        
                                        else:
                                            if str(sub_menu[item][entry]) == "use_mouse_input":
                                                argument = not self.__dict__[sub_menu[item][entry]]
                                            else:
                                                argument = self.__dict__[sub_menu[item][entry]]
                                                
                                            if "float" in str(type(argument)):
                                                argument = int(argument)

                                            if sub_menu[item][3] == "dont_use_set_resolution":
                                                inverted_value = argument
                                                argument = not inverted_value
                                                
                                            if argument is True:
                                                argument = "Enabled"
                                                
                                            if argument is False:
                                                argument = "Disabled"
                                        
                                    data.append(argument)

                                if (sub_menu[item][3] == "music_volume" and
                                        self.music is False):
                                    
                                    font_color = self.shape_color
                                    
                                elif (sub_menu[item][3] == "sound_volume" and
                                        self.sound is False):
                                    
                                    font_color = self.shape_color

                                elif (sub_menu[item][3] == "fps" and
                                        self.vsync):

                                    font_color = self.shape_color

                                elif (sub_menu[item][3] == "aa_quality" and
                                        self.aa is False):

                                    font_color = self.shape_color

                                elif (sub_menu[item][3] == "clear_cache" and
                                        files_to_remove is False):

                                    font_color = self.shape_color
                                    text_to_render = str(sub_menu[item][0]) + ": Done."

                                elif (sub_menu[item][3] == "clear_languages_cache" and
                                        clear_languages is False):

                                    font_color = self.shape_color
                                    text_to_render = str(sub_menu[item][0]) + ": Done."

                                elif (sub_menu[item][3] == "scan_pycraft" and
                                        scanned_files is True):

                                    font_color = self.shape_color
                                    text_to_render = str(sub_menu[item][0]) + ": Done, no errors were found."

                                elif (sub_menu[item][3] == "use_mouse_input" and
                                        not self.joystick_connected):

                                    font_color = self.shape_color
                                    text_to_render = str(sub_menu[item][0]).format(*data)
                                    enabled = False
                                    
                                else:
                                    enabled = True
                                    font_color = self.font_color
                                    if sub_menu[item][3] == "language":
                                        language = data[0]
                                        data = self.language_list[language].capitalize()
                                        text_to_render = str(sub_menu[item][0]).format(data)
                                        
                                    else:
                                        if (sub_menu[item][3] == "resolution" and
                                                self.dont_use_set_resolution is False):
                                    
                                            font_color = self.shape_color
                                            enabled = False
                                    
                                        text_to_render = str(sub_menu[item][0]).format(*data)

                                (self.translated_text,
                                    returned_text) = text_utils.text_formatter.format_text(
                                    text_to_render,
                                    self.language,
                                    self.display,
                                    (scroll_x_offset, general_y_position - scroll),
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
                                    self.connection_permission)

                                text_height = returned_text.get_height()
                                            
                                argument_variable = sub_menu[item][3]
                                saved_y_position = general_y_position

                                if list(sub_menu[item][2].keys())[0] == "remap_function":
                                    remap_pos = (general_y_position + text_height + 10) - scroll
                                    options = self.input_configuration[self.selected_input_reconfig]
                                    
                                    (keybind_height,
                                        mouse_over,
                                        hover_id,
                                        maximum_remap_width,
                                        disable_events,
                                        self.translated_text) = remapping_utils.draw_setting_elements.draw_remap_function(
                                        self,
                                        remap_pos,
                                        options,
                                        hovering,
                                        mouse_over,
                                        self.small_content_font,
                                        self.small_content_backup_font,
                                        maximum_remap_width,
                                        display_events,
                                        scrollbar_needed,
                                        self.aa,
                                        self.font_color,
                                        self.display,
                                        self.mouse_x,
                                        self.mouse_y,
                                        self.input_key,
                                        self.accent_color,
                                        self.shape_color,
                                        self.logging_dictionary,
                                        self.output_log,
                                        self.platform,
                                        self.base_folder,
                                        self.selected_input_reconfig,
                                        self.language,
                                        self.translated_text,
                                        self.connection_permission)

                                    general_y_position += keybind_height

                                elif list(sub_menu[item][2].keys())[0] == "directory_structure":
                                    button_pos = (general_y_position + text_height + 10) - scroll

                                    (graph_height,
                                        hovering,
                                        mouse_over,
                                        hover_id,
                                        self.translated_text) = directory_utils.draw_setting_elements.draw_directory_structure(
                                        self,
                                        button_pos,
                                        self.small_content_font,
                                        self.small_content_backup_font,
                                        hovering,
                                        mouse_over,
                                        hover_id,
                                        hovering_over_key,
                                        scrollbar_needed,
                                        self.aa,
                                        self.font_color,
                                        self.display,
                                        self.mouse_x,
                                        self.mouse_y,
                                        self.shape_color,
                                        self.real_window_width,
                                        self.file_structure,
                                        self.folder_size,
                                        self.background_color,
                                        self.language,
                                        self.logging_dictionary,
                                        self.output_log,
                                        self.platform,
                                        self.base_folder,
                                        self.translated_text,
                                        self.connection_permission)

                                    general_y_position += graph_height

                                else:
                                    name = str(sub_menu[item][entry])
                                    if name == "use_mouse_input":
                                        value = not self.__dict__[argument_variable]

                                    else:
                                        value = self.__dict__[argument_variable]
                                    
                                    if list(sub_menu[item][2].keys())[0] == "button":
                                        button_pos = (general_y_position + text_height + 10) - scroll
                                        button_text_array = sub_menu[item][2]["button"]
                                        
                                        (button_height,
                                            hovering,
                                            mouse_over,
                                            self.fps,
                                            self.aa,
                                            self.render_fog,
                                            self.fancy_graphics,
                                            self.fancy_particles,
                                            self.average_fps,
                                            self.iteration,
                                            self.themeArray,
                                            self.font_color,
                                            self.background_color,
                                            self.shape_color,
                                            self.accent_color,
                                            self.secondary_font_color,
                                            self.translated_text) = button_utils.draw_setting_elements.draw_buttons(
                                            self,
                                            button_pos,
                                            button_text_array,
                                            self.small_content_font,
                                            self.small_content_backup_font,
                                            value,
                                            argument_variable,
                                            hovering,
                                            mouse_over,
                                            files_to_remove,
                                            clear_languages,
                                            scanned_files,
                                            scrollbar_needed,
                                            self.aa,
                                            self.font_color,
                                            self.display,
                                            self.mouse_x,
                                            self.mouse_y,
                                            self.sound,
                                            self.accent_color,
                                            self.shape_color,
                                            self.platform,
                                            self.base_folder,
                                            self.remove_file_permission,
                                            self.settings_preset,
                                            self.fps,
                                            self.render_fog,
                                            self.fancy_graphics,
                                            self.fancy_particles,
                                            self.average_fps,
                                            self.iteration,
                                            self.use_mouse_input,
                                            self.sound_volume,
                                            self.themeArray,
                                            self.background_color,
                                            self.secondary_font_color,
                                            self.language,
                                            self.logging_dictionary,
                                            self.output_log,
                                            self.translated_text,
                                            self.connection_permission)
                                        
                                        general_y_position += button_height

                                    if self.theme == "custom" and sub_menu[item][3] == "theme":
                                        if self.custom_theme is None:
                                            (_,
                                                font_color,
                                                background_color,
                                                shape_color,
                                                accent_color,
                                                secondary_font_color) = theme_utils.determine_theme_colours.get_colors(
                                                    self,
                                                    self.theme,
                                                    self.custom_theme,
                                                    self.colour_presets)

                                            self.custom_theme = {
                                                "font_color": font_color,
                                                "background_color": background_color,
                                                "shape_color": shape_color,
                                                "accent_color": accent_color,
                                                "secondary_font_color": secondary_font_color}

                                        button_pos = (general_y_position + text_height - 5) - scroll
                                            
                                        (button_height,
                                            hovering,
                                            mouse_over,
                                            self.translated_text,
                                            custom_theme_choice,
                                            self.custom_theme) = custom_theme_utils.draw_setting_elements.draw_custom_theme_options(
                                            self,
                                            button_pos,
                                            self.small_content_font,
                                            self.small_content_backup_font,
                                            hovering,
                                            mouse_over,
                                            scrollbar_needed,
                                            self.aa,
                                            self.font_color,
                                            self.display,
                                            self.mouse_x,
                                            self.mouse_y,
                                            self.sound,
                                            self.accent_color,
                                            self.shape_color,
                                            self.platform,
                                            self.base_folder,
                                            self.use_mouse_input,
                                            self.sound_volume,
                                            self.background_color,
                                            self.secondary_font_color,
                                            self.language,
                                            self.logging_dictionary,
                                            self.output_log,
                                            self.translated_text,
                                            self.connection_permission,
                                            custom_theme_choice,
                                            self.custom_theme,
                                            display_events)

                                        for i in range(len(list(self.custom_theme))):
                                            argument = str(self.custom_theme[list(self.custom_theme)[i]])
                                            input_result = input_utility.identify_patterns.identify_rgb(argument)
                                            if input_result is False:
                                                input_result = input_utility.identify_patterns.identify_hex(argument[1:-1])
                                                if input_result is False:
                                                    input_result = input_utility.identify_patterns.identify_text(argument, self.colour_presets)
                                                    if not input_result is False:
                                                        self.__dict__[list(self.custom_theme)[i]] = input_result
                                                else:
                                                    self.__dict__[list(self.custom_theme)[i]] = input_result
                                            else:
                                                self.__dict__[list(self.custom_theme)[i]] = input_result

                                        general_y_position += button_height

                                    if list(sub_menu[item][2].keys())[0] == "dropdown":
                                        button_pos = (general_y_position + text_height + 10) - scroll
                                        if sub_menu[item][2]["dropdown"] == "<translate_languages_list>":
                                            content = self.language_list
                                        elif sub_menu[item][2]["dropdown"] == "<rendering_resolutions>":
                                            content = self.resolutions_list
                                        else:
                                            content = None

                                        argument_variable = sub_menu[item][3]
                                            
                                        (dropdown_height,
                                            hovering,
                                            mouse_over,
                                            dropdown_hovering,
                                            dropdown_scroll,
                                            mouse_over,
                                            self.translated_text,
                                            self.mouse_button_down) = dropdown_utils.draw_setting_elements.draw_dropdown(
                                            self,
                                            dropdown_scroll,
                                            button_pos,
                                            self.small_content_font,
                                            self.small_content_backup_font,
                                            argument_variable,
                                            hovering,
                                            dropdown_hovering,
                                            mouse_over,
                                            scrollbar_needed,
                                            self.aa,
                                            font_color,
                                            self.display,
                                            self.mouse_x,
                                            self.mouse_y,
                                            self.accent_color,
                                            self.shape_color,
                                            self.platform,
                                            self.base_folder,
                                            self.use_mouse_input,
                                            self.sound,
                                            self.sound_volume,
                                            self.mouse_button_down,
                                            content,
                                            self.real_window_width,
                                            enabled,
                                            self.translated_text,
                                            self.language,
                                            self.logging_dictionary,
                                            self.output_log,
                                            self.connection_permission)

                                        general_y_position += dropdown_height

                                    if list(sub_menu[item][2].keys())[0] == "multi-button":
                                        button_pos = (general_y_position + text_height + 10) - scroll
                                        button_text_array = sub_menu[item][2]["multi-button"]

                                        (button_height,
                                            hovering,
                                            mouse_over,
                                            self.fps,
                                            self.aa,
                                            self.render_fog,
                                            self.fancy_graphics,
                                            self.fancy_particles,
                                            self.average_fps,
                                            self.iteration,
                                            self.themeArray,
                                            self.font_color,
                                            self.background_color,
                                            self.shape_color,
                                            self.accent_color,
                                            self.secondary_font_color,
                                            self.theme,
                                            self.mouse_button_down,
                                            self.translated_text) = button_utils.draw_setting_elements.draw_multi_buttons(
                                            self,
                                            button_pos,
                                            button_text_array,
                                            self.small_content_font,
                                            self.small_content_backup_font,
                                            argument_variable,
                                            hovering,
                                            mouse_over,
                                            scrollbar_needed,
                                            self.aa,
                                            self.font_color,
                                            self.display,
                                            self.mouse_x,
                                            self.mouse_y,
                                            self.accent_color,
                                            self.shape_color,
                                            self.platform,
                                            self.base_folder,
                                            self.use_mouse_input,
                                            self.sound,
                                            self.theme, 
                                            self.sound_volume,
                                            self.settings_preset,
                                            self.themeArray,
                                            self.background_color,
                                            self.secondary_font_color,
                                            self.fps,
                                            self.render_fog,
                                            self.fancy_graphics,
                                            self.fancy_particles,
                                            self.average_fps,
                                            self.iteration,
                                            self.mouse_button_down,
                                            self.language,
                                            self.logging_dictionary,
                                            self.output_log,
                                            self.translated_text,
                                            self.connection_permission)

                                        general_y_position += button_height

                                    if list(sub_menu[item][2].keys())[0] == "slider":
                                        slider_pos = (general_y_position + text_height + 10) - scroll
                                        slider_array = sub_menu[item][2]["slider"]
                                        minimum = slider_array[0]
                                        maximum = slider_array[1]
                                        
                                        (slider_height,
                                            hovering,
                                            mouse_over) = slider_utils.draw_setting_elements.draw_slider(
                                            self,
                                            slider_pos,
                                            minimum,
                                            maximum,
                                            value,
                                            argument_variable,
                                            hovering,
                                            mouse_over,
                                            scrollbar_needed,
                                            self.font_color,
                                            self.display,
                                            self.mouse_x,
                                            self.mouse_y,
                                            self.accent_color,
                                            self.shape_color,
                                            self.music,
                                            self.sound,
                                            self.real_window_width,
                                            self.vsync,
                                            self.background_color)
                                        
                                        general_y_position += slider_height

                                    if list(sub_menu[item][2].keys())[0] == "toggle":
                                        toggle_pos = (general_y_position + text_height + 10) - scroll
                                        slider_array = sub_menu[item][2]["toggle"]
                                        value_0 = slider_array[0]
                                        value_1 = slider_array[1]
                                        
                                        (toggle_height,
                                            hovering,
                                            mouse_over) = toggle_utils.draw_setting_elements.draw_toggle(
                                            self,
                                            toggle_pos,
                                            value_0,
                                            value_1,
                                            value,
                                            argument_variable,
                                            hovering,
                                            mouse_over,
                                            scrollbar_needed,
                                            enabled,
                                            self.font_color,
                                            self.display,
                                            self.mouse_x,
                                            self.mouse_y,
                                            self.accent_color,
                                            self.shape_color,
                                            self.background_color,
                                            self.music,
                                            self.use_mouse_input,
                                            self.sound,
                                            self.platform,
                                            self.base_folder,
                                            self.sound_volume)
                                        
                                        general_y_position += toggle_height

                                if mouse_over:                                    
                                    (info_offset,
                                        self.translated_text) = settings_utils.draw_setting_elements.create_information_message(
                                        self,
                                        self.small_content_font,
                                        self.small_content_backup_font,
                                        sub_menu[item][1],
                                        saved_y_position,
                                        max_x,
                                        info_offset,
                                        self.aa,
                                        self.font_color,
                                        self.display,
                                        self.real_window_width,
                                        self.real_window_height,
                                        self.language,
                                        self.translated_text,
                                        self.logging_dictionary,
                                        self.output_log,
                                        self.platform,
                                        self.base_folder,
                                        self.connection_permission)
                                    
                                general_y_position += text_height

                            if (general_y_position - scroll) + 10 > self.real_window_height:
                                scroll_enabled = True

                            else:
                                scroll_enabled = False

                            if general_y_position > self.real_window_height:
                                scrollbar_needed = True
                                
                                rect = pygame.Rect(
                                    2,
                                    scroll + 2,
                                    3,
                                    self.real_window_height - (general_y_position % self.real_window_height) - 18)

                                pygame.draw.rect(
                                    self.display,
                                    self.shape_color,
                                    rect,
                                    border_radius=2)

                            else:
                                scrollbar_needed = False
                                scroll = 0

                        button_id += 1
                        
                    button_y_position *= self.y_scale_factor

                    button_offset = (self.real_window_height - button_y_position) / 2

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

                    if not self.startup_animation and (self.go_to is not None):
                        return None

                    if hovering:
                        hovering = False
                        pygame.mouse.set_cursor(
                                pygame.cursors.Cursor(
                                    pygame.SYSTEM_CURSOR_HAND))
                    else:
                        pygame.mouse.set_cursor(
                            pygame.cursors.Cursor(
                                pygame.SYSTEM_CURSOR_ARROW))

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
                error_message = (
                    f"settings > generate_settings > settings: {str(Message)}")

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
