if __name__ != "__main__":
    try:
        import threading
        import time
        import sys
        import subprocess
        import json
        
        import pygame
        
        from registry_utils import Registry
        
        import text_utils
        import theme_utils
        import input_utility
        import toggle_utils
        import slider_utils
        import remapping_utils
        import custom_theme_utils
        import button_utils
        import directory_utils
        import dropdown_utils
        import settings_utils
        import file_utils
        import tkinter_utils
        import pycraft_startup_utils
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in settings_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
        
    class settings_variables:
        button_offset = 0

        current_menu = "General"
        hover_menu = None

        settings_config_path = Registry.base_folder / "data files" / "settings_config.json"

        initial_theme = Registry.theme

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
        enabled = True

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
        
        with open(settings_config_path,
                    "r") as openFile:

                settings_structure = json.load(openFile)
        
    class command_events(Registry):
        def restart_function(self):
            restart_path = Registry.base_folder / "main.py"
            
            subprocess.call(
                [sys.executable,
                    restart_path] + sys.argv[1:])
            
        def controls(self):
            if settings_variables.scan_directory:
                settings_variables.scan_directory = False
                file_utils.scan_folder.search_files()

            if Registry.clear_languages_cache:
                Registry.clear_languages_cache = False
                
                if settings_variables.clear_languages:
                    Registry.translated_text = {}
                    Registry.translation_cache.write_cache()

                    settings_variables.clear_languages = False
                    settings_variables.scan_directory = True

            if Registry.clear_cache:
                Registry.clear_cache = False
                
                if settings_variables.files_to_remove:
                    file_utils.delete_files.clear_temporary_files()

                    settings_variables.files_to_remove = False
                    settings_variables.scan_directory = True

            if Registry.scan_pycraft:
                Registry.scan_pycraft = False

                pycraft_startup_utils.startup_test.pycraft_resource_test(
                    True)

                settings_variables.scanned_files = True

            if Registry.reset_pycraft:
                Registry.reset_pycraft = False

                theme = Registry.theme
                for key in Registry.save_keys:
                    setattr(Registry, key, Registry.save_keys[key])

                Registry.theme = theme

                if Registry.connection_permission is None:
                    permission_message = "Can we have your permission to check the internet for updates to Pycraft?"
                    Registry.connection_permission = tkinter_utils.tkinter_info.get_permissions(
                        permission_message)

                if Registry.remove_file_permission is None:
                    permission_message = "Can we have your permission to send files from the Pycraft directory to the recycle bin?"
                    Registry.remove_file_permission = tkinter_utils.tkinter_info.get_permissions(
                        permission_message)
                    
                if Registry.show_strobe_effects is None:
                    Registry.show_strobe_effects = messagebox.askquestion(
                        "Check Permission",
                        "".join(("Strobe effects and bright flashes of light can ",
                                    "cause discomfort, (for example lightning), you can choose here ",
                                    "whether to enable or disable those ",
                                    "strobe effects in Pycraft.\n",
                                    "Click 'yes' to allow for strobe effects, or 'no' ",
                                    "to turn them off. You can always adjust this in ",
                                    "Pycraft's settings, under 'Storage and permissions'.")))

                    if Registry.show_strobe_effects == "yes":
                        Registry.show_strobe_effects = True

                    else:
                        Registry.show_strobe_effects = False
                
            if Registry.exit_mode == "restart":
                if Registry.save_on_exit:
                    file_utils.pycraft_config_utils.save_pycraft_config()
                    
                threading.Thread(
                    target=self.restart_function).start()

                pygame.quit()
                while True:
                    time.sleep(30)

            if Registry.exit_mode == "exit":
                if Registry.save_on_exit:
                    file_utils.pycraft_config_utils.save_pycraft_config()
                    
                pygame.quit()
                sys.exit()
        
    class widget_drawer(Registry):
        def draw_elements(
                self,
                item,
                text_height,
                mouse_over,
                display_events,
                saved_y_position,
                entry,
                argument_variable):
            
            if list(item[2].keys())[0] == "remap_function":
                remap_pos = (settings_variables.general_y_position + text_height + 10) - settings_variables.scroll
                options = Registry.input_configuration[Registry.selected_input_reconfig]
                
                (keybind_height,
                    mouse_over,
                    settings_variables.hovering,
                    settings_variables.maximum_remap_width,
                    settings_variables.disable_events) = remapping_utils.draw_setting_elements.draw_remap_function(
                    remap_pos,
                    options,
                    settings_variables.hovering,
                    mouse_over,
                    Registry.small_content_font,
                    Registry.small_content_backup_font,
                    settings_variables.maximum_remap_width,
                    display_events,
                    settings_variables.scrollbar_needed)

                settings_variables.general_y_position += keybind_height

            elif list(item[2].keys())[0] == "directory_structure":
                button_pos = (settings_variables.general_y_position + text_height + 10) - settings_variables.scroll

                (graph_height,
                    settings_variables.hovering,
                    mouse_over,
                    settings_variables.hover_id) = directory_utils.draw_setting_elements.draw_directory_structure(
                    button_pos,
                    Registry.small_content_font,
                    Registry.small_content_backup_font,
                    settings_variables.hovering,
                    mouse_over,
                    settings_variables.hover_id,
                    settings_variables.hovering_over_key,
                    settings_variables.scrollbar_needed)

                settings_variables.general_y_position += graph_height

            else:
                name = str(item[entry])
                if name == "use_mouse_input":
                    value = not Registry.__dict__[argument_variable]

                else:
                    value = Registry.__dict__[argument_variable]
                
                if list(item[2].keys())[0] == "button":
                    button_pos = (settings_variables.general_y_position + text_height + 10) - settings_variables.scroll
                    button_text_array = item[2]["button"]
                    
                    button = button_utils.draw_setting_elements()
                    (button_height,
                        settings_variables.hovering,
                        mouse_over) = button.draw_buttons(
                        button_pos,
                        button_text_array,
                        Registry.small_content_font,
                        Registry.small_content_backup_font,
                        value,
                        argument_variable,
                        settings_variables.hovering,
                        mouse_over,
                        settings_variables.files_to_remove,
                        settings_variables.clear_languages,
                        settings_variables.scanned_files,
                        settings_variables.scrollbar_needed)
                    
                    settings_variables.general_y_position += button_height

                if Registry.theme == "custom" and item[3] == "theme":
                    if Registry.custom_theme is None:
                        theme_utils.determine_theme_colors.get_colors()

                        Registry.custom_theme = {
                            "font_color": Registry.font_color,
                            "background_color": Registry.background_color,
                            "shape_color": Registry.shape_color,
                            "accent_color": Registry.accent_color,
                            "secondary_font_color": Registry.secondary_font_color}

                    button_pos = (settings_variables.general_y_position + text_height - 5) - settings_variables.scroll
                        
                    (button_height,
                        settings_variables.hovering,
                        mouse_over,
                        settings_variables.custom_theme_choice) = custom_theme_utils.draw_setting_elements.draw_custom_theme_options(
                        button_pos,
                        Registry.small_content_font,
                        Registry.small_content_backup_font,
                        settings_variables.hovering,
                        mouse_over,
                        settings_variables.scrollbar_needed,
                        settings_variables.custom_theme_choice,
                        display_events)

                    for i in range(len(list(Registry.custom_theme))):
                        argument = str(Registry.custom_theme[list(Registry.custom_theme)[i]])
                        input_result = input_utility.identify_patterns.identify_rgb(argument)
                        if input_result is False:
                            input_result = input_utility.identify_patterns.identify_hex(argument[1:-1])
                            if input_result is False:
                                input_result = input_utility.identify_patterns.identify_text(argument, Registry.color_presets)
                                if not input_result is False:
                                    setattr(Registry, list(Registry.custom_theme)[i], input_result)
                            else:
                                setattr(Registry, list(Registry.custom_theme)[i], input_result)
                        else:
                            setattr(Registry, list(Registry.custom_theme)[i], input_result)

                    settings_variables.general_y_position += button_height

                if list(item[2].keys())[0] == "dropdown":
                    button_pos = (settings_variables.general_y_position + text_height + 10) - settings_variables.scroll
                    if item[2]["dropdown"] == "<translate_languages_list>":
                        content = Registry.language_list
                    elif item[2]["dropdown"] == "<rendering_resolutions>":
                        content = Registry.resolutions_list
                    else:
                        content = None

                    argument_variable = item[3]
                        
                    (dropdown_height,
                        settings_variables.hovering,
                        mouse_over,
                        settings_variables.dropdown_hovering,
                        settings_variables.dropdown_scroll) = dropdown_utils.draw_setting_elements.draw_dropdown( # slow
                        settings_variables.dropdown_scroll,
                        button_pos,
                        Registry.small_content_font,
                        Registry.small_content_backup_font,
                        argument_variable,
                        settings_variables.hovering,
                        settings_variables.dropdown_hovering,
                        mouse_over,
                        settings_variables.scrollbar_needed,
                        content,
                        settings_variables.enabled)

                    settings_variables.general_y_position += dropdown_height

                if list(item[2].keys())[0] == "multi-button":
                    button_pos = (settings_variables.general_y_position + text_height + 10) - settings_variables.scroll
                    button_text_array = item[2]["multi-button"]

                    button = button_utils.draw_setting_elements()
                    (button_height,
                        settings_variables.hovering,
                        mouse_over) = button.draw_multi_buttons(
                        button_pos,
                        button_text_array,
                        Registry.small_content_font,
                        Registry.small_content_backup_font,
                        argument_variable,
                        settings_variables.hovering,
                        mouse_over,
                        settings_variables.scrollbar_needed)

                    settings_variables.general_y_position += button_height

                if list(item[2].keys())[0] == "slider":
                    slider_pos = (settings_variables.general_y_position + text_height + 10) - settings_variables.scroll
                    slider_array = item[2]["slider"]
                    minimum = slider_array[0]
                    maximum = slider_array[1]
                    
                    (slider_height,
                        settings_variables.hovering,
                        mouse_over) = slider_utils.draw_setting_elements.draw_slider(
                        slider_pos,
                        minimum,
                        maximum,
                        value,
                        argument_variable,
                        settings_variables.hovering,
                        mouse_over,
                        settings_variables.scrollbar_needed)
                    
                    settings_variables.general_y_position += slider_height

                if list(item[2].keys())[0] == "toggle":
                    toggle_pos = (settings_variables.general_y_position + text_height + 10) - settings_variables.scroll
                    slider_array = item[2]["toggle"]
                    value_0 = slider_array[0]
                    value_1 = slider_array[1]
                    
                    (toggle_height,
                        settings_variables.hovering,
                        mouse_over) = toggle_utils.draw_setting_elements.draw_toggle(
                        toggle_pos,
                        value_0,
                        value_1,
                        value,
                        argument_variable,
                        settings_variables.hovering,
                        mouse_over,
                        settings_variables.scrollbar_needed,
                        settings_variables.enabled)
                    
                    settings_variables.general_y_position += toggle_height

            if mouse_over:                                    
                settings_utils.draw_setting_elements.create_information_message(
                    Registry.small_content_font,
                    Registry.small_content_backup_font,
                    item[1],
                    saved_y_position)
                
            settings_variables.general_y_position += text_height
            return mouse_over
        
    class configure_setting_elements(Registry):
        def set_text_color(
                self,
                item,
                data):
            
            for entry in range(3, len(item)):
                if str(item[entry]) != "directory_structure":
                    if str(item[entry]) == "average_fps":
                        data.append(int(Registry.average_fps))

                    elif str(item[entry]) == "keybinds":
                        pass
                    
                    else:
                        if str(item[entry]) == "use_mouse_input":
                            argument = not Registry.__dict__[item[entry]]
                        else:
                            argument = Registry.__dict__[item[entry]]
                        data.append(argument)
                            
                        if "float" in str(type(argument)):
                            data.append(int(argument))

                        if item[3] == "dont_use_set_resolution":
                            inverted_value = argument
                            data.append(not inverted_value)
                            
                        if argument is True:
                            data.append("Enabled")
                            
                        if argument is False:
                            data.append("Disabled")
                                    
            text_to_render = str(item[0]).format(*data)
            if (item[3] == "music_volume" and
                    Registry.music is False):
                
                font_color = Registry.shape_color
                
            elif (item[3] == "sound_volume" and
                    Registry.sound is False):
                
                font_color = Registry.shape_color

            elif (item[3] == "fps" and
                    Registry.vsync):

                font_color = Registry.shape_color

            elif (item[3] == "aa_quality" and
                    Registry.aa is False):

                font_color = Registry.shape_color

            elif (item[3] == "clear_cache" and
                    settings_variables.files_to_remove is False):

                font_color = Registry.shape_color
                text_to_render = str(item[0]) + ": Done."

            elif (item[3] == "clear_languages_cache" and
                    settings_variables.clear_languages is False):

                font_color = Registry.shape_color
                text_to_render = str(item[0]) + ": Done."

            elif (item[3] == "scan_pycraft" and
                    settings_variables.scanned_files is True):

                font_color = Registry.shape_color
                text_to_render = str(item[0]) + ": Done, no errors were found."

            elif (item[3] == "use_mouse_input" and
                    not Registry.joystick_connected):

                font_color = Registry.shape_color
                text_to_render = str(item[0]).format(*data)
                settings_variables.enabled = False
                
            else:
                settings_variables.enabled = True
                font_color = Registry.font_color
                if item[3] == "language":
                    language = data[0]
                    data = Registry.language_list[language].capitalize()
                    text_to_render = str(item[0]).format(data)
                    
                else:
                    if (item[3] == "resolution" and
                            Registry.dont_use_set_resolution is False):
                
                        font_color = Registry.shape_color
                        settings_variables.enabled = False
                
                    text_to_render = str(item[0]).format(*data)
                    
            return font_color, text_to_render, entry
                    
    class draw_setting_elements(Registry):
        def create_information_message(
                font,
                backup_font,
                text,
                saved_y_position):
            
            position = ((Registry.real_window_width/2) + 40,
                        (saved_y_position + 10) - settings_variables.info_offset)
            
            width = Registry.real_window_width - (settings_variables.max_x + 43)

            info_text_height = text_utils.text_wrap.blit_text(
                    text,
                    position,
                    font,
                    backup_font,
                    width)

            rect = pygame.Rect(
                position[0] - 10,
                position[1] - 10,
                (width - position[0]) + 20,
                info_text_height + 20)

            pygame.draw.rect(
                Registry.display,
                Registry.font_color,
                rect,
                width=1,
                border_radius=10)

            max_y_value = position[1] + info_text_height + settings_variables.info_offset + 20
            if max_y_value > Registry.real_window_height:
                settings_variables.info_offset = (max_y_value - Registry.real_window_height) + 10

            else:
                settings_variables.info_offset = 0

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
