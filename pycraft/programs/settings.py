if __name__ != "__main__":
    try:
        import subprocess
        import sys
        import time
        import json
        from tkinter import messagebox
        import traceback
        
        import pygame

        from registry_utils import Registry
        
        import caption_utils
        import display_utils
        import error_utils
        import sound_utils
        import drawing_utils
        import settings_utils
        import text_utils
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in settings"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class generate_settings(Registry): 
        def settings_gui(self):
            try:
                selector_path = Registry.base_folder / "resources" / "general resources" / f"selectorICON{Registry.theme}.png"
                settings_utils.settings_variables.selector = pygame.image.load(selector_path)
                settings_utils.settings_variables.selector.convert()
        
                caption_utils.generate_captions.set_caption(
                    "Settings")

                while True:
                    start_time = time.perf_counter()

                    if not (Registry.error_message is None or
                                Registry.error_message_detailed is None):
                        
                        error_utils.generate_error_screen.error_screen(
                            Registry.error_message,
                            Registry.error_message_detailed)

                    display_events = display_utils.display_functionality.core_display_functions(
                        return_events=True,
                        disable_events=settings_utils.settings_variables.disable_events)

                    for event in display_events:
                        if event.type == pygame.MOUSEWHEEL and settings_utils.settings_variables.dropdown_hovering:
                            if Registry.use_mouse_input:
                                pygame.mouse.set_cursor(
                                    pygame.SYSTEM_CURSOR_SIZENS)
                                
                        else:           
                            if event.type == pygame.MOUSEWHEEL and settings_utils.settings_variables.scrollbar_needed:
                                if Registry.use_mouse_input:
                                    pygame.mouse.set_cursor(
                                        pygame.SYSTEM_CURSOR_SIZENS)

                                    
                                    if str(event.y)[0] == "-":
                                        if settings_utils.settings_variables.scroll > 0:
                                            settings_utils.settings_variables.scroll -= 5

                                    else:
                                        if settings_utils.settings_variables.scroll_enabled:
                                            settings_utils.settings_variables.scroll += 5

                    caption_utils.generate_captions.set_caption(
                        "Settings")

                    Registry.display.fill(Registry.background_color)

                    cover_Rect = pygame.Rect(
                        0,
                        0,
                        Registry.real_window_width,
                        90)

                    pygame.draw.rect(
                        Registry.display,
                        Registry.background_color,
                        cover_Rect)
                    
                    returned_text = text_utils.text_formatter.format_text(
                        "Pycraft",
                        ("center", "top"),
                        Registry.title_font,
                        Registry.title_backup_font)

                    settings_utils.settings_variables.title_width = returned_text.get_width()

                    returned_text = text_utils.text_formatter.format_text(
                        "Settings",
                        (((Registry.real_window_width-settings_utils.settings_variables.title_width)/2)+55, 50),
                        Registry.subtitle_font,
                        Registry.subtitle_backup_font,
                        font_color=Registry.secondary_font_color)

                    if settings_utils.settings_variables.initial_theme != Registry.theme:
                        settings_utils.settings_variables.initial_theme = Registry.theme
                        returned_text = text_utils.text_formatter.format_text(
                            "Pycraft",
                            ("center", "top"),
                            Registry.title_font,
                            Registry.title_backup_font)

                        settings_utils.settings_variables.title_width = returned_text.get_width()

                        returned_text = text_utils.text_formatter.format_text(
                            "Settings",
                            (((Registry.real_window_width-settings_utils.settings_variables.title_width)/2)+55, 50),
                            Registry.subtitle_font,
                            Registry.subtitle_backup_font,
                            font_color=Registry.secondary_font_color)

                        selector_path = Registry.base_folder / "resources" / "general resources" / f"selectorICON{Registry.theme}.png"
                
                        settings_utils.settings_variables.selector = pygame.image.load(selector_path)
                        settings_utils.settings_variables.selector.convert()

                        settings_utils.settings_variables.selector_width = settings_utils.settings_variables.selector.get_width()

                    button_y_position = 0
                    button_id = 0
                            
                    for key in settings_utils.settings_variables.settings_structure:
                        
                        if (key == "Developer options" and
                                Registry.extended_developer_options is False):
                            
                            font_color = Registry.shape_color
                            settings_utils.settings_variables.underline_button = False
                            
                        else:
                            if key == settings_utils.settings_variables.hover_menu:
                                settings_utils.settings_variables.underline_button = True

                            
                            font_color = Registry.font_color

                        if settings_utils.settings_variables.button_width > settings_utils.settings_variables.max_x:
                            settings_utils.settings_variables.max_x = settings_utils.settings_variables.button_width
                        
                        settings_utils.settings_variables.button_height += 50 - settings_utils.settings_variables.button_height

                        button_blit_y = (button_y_position * Registry.y_scale_factor) + settings_utils.settings_variables.button_offset

                        returned_text = text_utils.text_formatter.format_text(
                            key,
                            ("right", button_blit_y),
                            Registry.option_font,
                            Registry.option_backup_font,
                            font_color=font_color,
                            underline=settings_utils.settings_variables.underline_button)

                        settings_utils.settings_variables.underline_button = False

                        settings_utils.settings_variables.button_width = returned_text.get_width()
                        settings_utils.settings_variables.button_height = returned_text.get_height()

                        button_blit_x = (Registry.real_window_width-settings_utils.settings_variables.button_width)-2
                        
                        if key == settings_utils.settings_variables.hover_menu:
                            if not (key == "Developer options" and
                                    Registry.extended_developer_options is False):
                        
                                Registry.display.blit(
                                    settings_utils.settings_variables.selector,
                                    (Registry.real_window_width-(settings_utils.settings_variables.button_width+settings_utils.settings_variables.selector_width)-2,
                                        button_blit_y))

                        if ((Registry.mouse_x > button_blit_x and
                                    Registry.mouse_x < Registry.real_window_width and
                                    Registry.mouse_y > button_blit_y and
                                    Registry.mouse_y < button_blit_y + settings_utils.settings_variables.button_height) and
                                not (key == "Developer options" and 
                                        Registry.extended_developer_options is False)):
                            
                            settings_utils.settings_variables.hover_menu = key
                            settings_utils.settings_variables.hovering = True

                            if (Registry.primary_mouse_button_down and
                                    settings_utils.settings_variables.current_menu != key):
                                
                                settings_utils.settings_variables.current_menu = key
                                settings_utils.settings_variables.scrollbar_needed = False
                                settings_utils.settings_variables.scroll = 0
                                Registry.primary_mouse_button_down = False
                                
                                if settings_utils.settings_variables.current_menu == "Storage and permissions":
                                    settings_utils.settings_variables.scan_directory = True
                                
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()
                                    
                        else:
                            if settings_utils.settings_variables.hover_menu == key:
                                settings_utils.settings_variables.hover_menu = None

                        button_y_position += settings_utils.settings_variables.button_height

                        sub_menu = settings_utils.settings_variables.settings_structure[settings_utils.settings_variables.current_menu]

                        settings_utils.settings_variables.general_y_position = 100

                        settings_utils.command_events().controls()

                        if sub_menu[0] is not None:
                            for item in sub_menu:
                                data = []
                                mouse_over = False

                                if settings_utils.settings_variables.scrollbar_needed:
                                    scroll_x_offset = 9

                                else:
                                    scroll_x_offset = 0

                                (font_color,
                                    text_to_render,
                                    entry) = settings_utils.configure_setting_elements().set_text_color(
                                    item,
                                    data)

                                returned_text = text_utils.text_formatter.format_text(
                                    text_to_render,
                                    (scroll_x_offset, settings_utils.settings_variables.general_y_position - settings_utils.settings_variables.scroll),
                                    Registry.small_content_font,
                                    Registry.small_content_backup_font,
                                    font_color=font_color)

                                text_height = returned_text.get_height()
                                            
                                argument_variable = item[3]
                                saved_y_position = settings_utils.settings_variables.general_y_position

                                mouse_over = settings_utils.widget_drawer().draw_elements(
                                    item,
                                    text_height,
                                    mouse_over,
                                    display_events,
                                    saved_y_position,
                                    entry,
                                    argument_variable)

                            if (settings_utils.settings_variables.general_y_position - settings_utils.settings_variables.scroll) + 10 > Registry.real_window_height:
                                settings_utils.settings_variables.scroll_enabled = True

                            else:
                                settings_utils.settings_variables.scroll_enabled = False

                            if settings_utils.settings_variables.general_y_position > Registry.real_window_height:
                                settings_utils.settings_variables.scrollbar_needed = True
                                
                                rect = pygame.Rect(
                                    2,
                                    settings_utils.settings_variables.scroll + 2,
                                    3,
                                    Registry.real_window_height - (settings_utils.settings_variables.general_y_position % Registry.real_window_height) - 18)

                                pygame.draw.rect(
                                    Registry.display,
                                    Registry.shape_color,
                                    rect,
                                    border_radius=2)

                            else:
                                settings_utils.settings_variables.scrollbar_needed = False
                                settings_utils.settings_variables.scroll = 0

                        button_id += 1
                        
                    button_y_position *= Registry.y_scale_factor

                    settings_utils.settings_variables.button_offset = (Registry.real_window_height - button_y_position) / 2

                    drawing_utils.generate_graph().draw_developer_graph()

                    if Registry.go_to is None:
                        display_utils.display_animations.fade_in()
                            
                    else:
                        display_utils.display_animations.fade_out()

                    if not Registry.startup_animation and (Registry.go_to is not None):
                        return

                    if settings_utils.settings_variables.hovering:
                        settings_utils.settings_variables.hovering = False
                        pygame.mouse.set_cursor(
                                pygame.cursors.Cursor(
                                    pygame.SYSTEM_CURSOR_HAND))
                    else:
                        pygame.mouse.set_cursor(
                            pygame.cursors.Cursor(
                                pygame.SYSTEM_CURSOR_ARROW))

                    target_fps = display_utils.display_utils.get_play_status()
                        
                    pygame.display.flip()
                    Registry.clock.tick(target_fps)

                    Registry.run_timer += time.perf_counter()-start_time
                    
            except Exception as message:
                error_message = (
                    f"settings > settings_utils.settings_variables > settings: {str(message)}")

                error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        message,
                        message.__traceback__))

                error_utils.generate_error_screen.error_screen(
                    error_message,
                    error_message_detailed)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
    