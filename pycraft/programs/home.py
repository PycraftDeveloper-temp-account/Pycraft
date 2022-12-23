if __name__ != "__main__":
    try:
        import os
        import time
        import traceback
        import threading
        import random

        import pygame
        import pyautogui

        import display_utils
        import error_utils
        import caption_utils
        import sound_utils
        import drawing_utils
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
            
    class generate_home:
        """
        This class is in charge of loading the resources used in the main menu
        of Pycraft. (Alternatively also called the 'title screen' or 'home screen')
        This class is also in charge of rendering the main menu.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        
        def __init__(self):
            pass

        def create_banner(self):
            """
            This subroutine is used to render the messages the user may see
            at the bottom of the home screen. This is run in parallel (thread).
            
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
                global show_message, MessageColor

                timer_start = 0
                RenderedText = False

                while self.command == "Undefined":
                    RenderRect = pygame.Rect(
                        0,
                        self.real_window_height-40,
                        self.real_window_width,
                        self.real_window_height)

                    self.display.fill(
                        self.background_color,
                        RenderRect)

                    if (show_message is not None and
                            MessageColor is not None and
                            RenderedText is False):
                        
                        timer_start = time.perf_counter()
                        RenderedText = True

                    if RenderedText:
                        if time.perf_counter()-timer_start < 3:
                            (self.translated_text,
                                _) = text_utils.text_formatter.format_text(
                                show_message,
                                self.language,
                                self.display,
                                ("center", "bottom"),
                                MessageColor,
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
                                self.connection_permission)

                        else:
                            show_message = None
                            MessageColor = None
                            RenderedText = False
                    else:
                        if self.use_mouse_input is False:
                            MessageText = "".join(("On the controller; use the D-pad to navigate the menu, ",
                                         "press 'B' to confirm or press 'Y' to exit"))

                            (self.translated_text,
                                _) = text_utils.text_formatter.format_text(
                                MessageText,
                                self.language,
                                self.display,
                                ("center", "bottom"),
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
                                self.connection_permission)

                    (self.translated_text,
                        _) = text_utils.text_formatter.format_text(
                        "By PycraftDev",
                        self.language,
                        self.display,
                        ("left", "bottom"),
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
                        self.connection_permission)

                    (self.translated_text,
                        _) = text_utils.text_formatter.format_text(
                        f"Version: {self.version}",
                        self.language,
                        self.display,
                        ("right", "bottom"),
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
                        self.connection_permission)

                    pygame.display.update(RenderRect)

                    (target_fps,
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

                    self.clock.tick(target_fps/2)
                    
            except Exception as Message:
                if str(Message) != "display Surface quit":
                    self.error_message = "".join(("homeScreen > generate_home > ",
                                                 f"create_banner (thread): {str(Message)}"))

                    self.error_message_detailed = "".join(
                        traceback.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

        def home_gui(self):
            """
            This subroutine is in charge of loading the resources used in the main menu
            of Pycraft. (Alternatively also called the 'title screen' or 'home screen')
            This subroutine is also in charge of rendering the main menu.
            
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
                global show_message, MessageColor

                show_message = None
                MessageColor = self.font_color

                BannerThread = threading.Thread(
                    target=generate_home.create_banner,
                    args=(self,))
                BannerThread.name = "Thread_BannerThread_HS"
                BannerThread.daemon = True
                BannerThread.start()

                caption_utils.generate_captions.get_normal_caption(
                    "Home",
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
                hover1 = False
                hover2 = False
                hover3 = False
                hover4 = False
                hover5 = False
                hover6 = False
                hover7 = False

                self.real_window_width = pygame.display.get_window_size()[0]
                self.real_window_height = pygame.display.get_window_size()[1]

                pygame.display.flip()

                oldTHEME = self.theme
                coloursARRAY = []

                anim = False

                special = [30,
                           30,
                           30]

                TargetARRAY = []

                ColourDisplacement = 80

                increment = False

                self.currently_displaying_message = False

                outdated = self.outdated

                self.mouse_x = self.real_window_width/2
                self.mouse_y = self.real_window_height/2

                play_width = 0
                settings_width = 0
                char_designer_width = 0
                credits_width = 0
                achievements_width = 0
                benchmark_width = 0
                installer_width = 0

                prev_joystick_connected = False

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

                    RenderRect = pygame.Rect(
                        0,
                        0,
                        self.real_window_width,
                        self.real_window_height-40)

                    if self.get_outdated == [True, False]:
                        self.get_outdated = [
                            True,
                            True]

                        outdated = self.outdated

                    if self.fancy_graphics:
                        coloursARRAY = []
                        if anim:
                            anim = False
                            TargetARRAY = []
                            for a in range(random.randint(0, 32)):
                                TargetARRAY.append(a)

                        if len(TargetARRAY) == 0:
                            TargetARRAY = [33]

                        for i in range(32):
                            for j in range(len(TargetARRAY)):
                                if i == TargetARRAY[j]:
                                    coloursARRAY.append(special)

                                else:
                                    coloursARRAY.append(self.shape_color)

                        if increment is False:
                            RandomInt = random.randint(0, 10)
                            if self.average_fps == 0 or self.iteration == 0:
                                ColourDisplacement -= RandomInt/(self.fps/4)

                            else:
                                ColourDisplacement -= RandomInt/((self.average_fps/self.iteration)/4)

                            special[0] = ColourDisplacement
                            special[1] = ColourDisplacement
                            special[2] = ColourDisplacement

                        if increment:
                            RandomInt = random.randint(0, 10)
                            if self.average_fps == 0 or self.iteration == 0:
                                ColourDisplacement += RandomInt/(self.fps/4)

                            else:
                                ColourDisplacement += RandomInt/((self.average_fps/self.iteration)/4)

                            special[0] = ColourDisplacement
                            special[1] = ColourDisplacement
                            special[2] = ColourDisplacement

                        if special[0] <= 30:
                            increment = True
                            special[0] = 30
                            special[1] = 30
                            special[2] = 30

                        if special[0] >= 80:
                            increment = False
                            anim = True
                            special[0] = 80
                            special[1] = 80
                            special[2] = 80
                    else:
                        coloursARRAY = self.fancy_graphics

                    if str(self.display) == "<Surface(Dead display)>":
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

                    if not oldTHEME == self.theme:
                        if self.platform == "Linux":
                            selector = pygame.image.load(
                                os.path.join(
                                    self.base_folder,
                                    ("".join(("resources//general resources",
                                              f"//selectorICON{self.theme}.png")))))
                            selector.convert()

                        else:
                            selector = pygame.image.load(
                                os.path.join(
                                    self.base_folder,
                                    ("".join(("resources\\general resources",
                                              f"\\selectorICON{self.theme}.png")))))
                            selector.convert()

                        selector_width = selector.get_width()
                        oldTHEME = self.theme

                    self.display.fill(self.background_color, RenderRect)

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
                            location="saveANDexit")

                    caption_utils.generate_captions.get_normal_caption(
                        "Home",
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

                    if self.go_to is None:
                        if (self.mouse_y >= 202*self.y_scale_factor and
                                self.mouse_y <= 247*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(play_width+selector_width))-2):

                            hover1 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)

                                if self.show_strobe_effects is None:
                                    self.show_strobe_effects = messagebox.askquestion(
                                        "Check Permission",
                                        "".join(("Strobe effects and bright flashes of light can ",
                                                 "cause discomfort, (for example lightning), you can choose here ",
                                                 "whether to enable or disable those ",
                                                 "strobe effects in Pycraft.\n\n",
                                                 "Click 'yes' to allow for strobe effects, or 'no' ",
                                                 "to turn them off. You can always adjust this in ",
                                                 "Pycraft's settings, under 'Storage and permissions'.")))

                                    if self.show_strobe_effects == "yes":
                                        self.show_strobe_effects = True

                                    else:
                                        self.show_strobe_effects = False
                                        
                                self.go_to = "Play"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover1 = False

                        if (self.mouse_y >= 252*self.y_scale_factor and
                                self.mouse_y <= 297*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(settings_width+selector_width))-2):

                            hover2 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)

                                self.go_to = "settings"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover2 = False

                        if (self.mouse_y >= 302*self.y_scale_factor and
                                self.mouse_y <= 347*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(char_designer_width+selector_width)-2)):

                            hover3 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)

                                self.go_to = "character_designer"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover3 = False

                        if (self.mouse_y >= 402*self.y_scale_factor and
                                self.mouse_y <= 447*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(achievements_width+selector_width)-2)):

                            hover4 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)

                                self.go_to = "achievements"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover4 = False

                        if (self.mouse_y >= 352*self.y_scale_factor and
                                self.mouse_y <= 397*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(credits_width+selector_width)-2)):

                            hover5 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)

                                self.go_to = "credits"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover5 = False

                        if (self.mouse_y >= 452*self.y_scale_factor and
                                self.mouse_y <= 497*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(benchmark_width+selector_width)-2)):

                            hover6 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)

                                self.go_to = "benchmark"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover6 = False

                        if (self.mouse_y >= 502*self.y_scale_factor and
                                self.mouse_y <= 547*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(installer_width+selector_width)-2)):

                            hover7 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)

                                self.go_to = "Installer"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover7 = False

                    if show_message is None:
                        if self.updated:
                            self.updated = False
                            show_message = f"Successfully updated Pycraft to v{self.version}"
                            MessageColor = (0, 255, 0)

                        elif outdated and self.total_number_of_updates == 1:
                            outdated = False
                            show_message = f"There are {self.total_number_of_updates} updates available!"
                            MessageColor = (0, 255, 0)

                        elif outdated and self.total_number_of_updates == 1:
                            outdated = False
                            show_message = "There is an update available!"
                            MessageColor = (0, 255, 0)

                        elif not prev_joystick_connected == self.joystick_connected:
                            prev_joystick_connected = self.joystick_connected
                            if self.joystick_connected:
                                show_message = "".join(("There is a new input device available! ",
                                                   "You can change input modes in settings"))

                                MessageColor = (0, 255, 0)

                            else:
                                if self.use_mouse_input:
                                    show_message = "Terminated connection to an input device"
                                    MessageColor = (255, 0, 0)

                                else:
                                    show_message = "".join(("Terminated connection to current ",
                                                       "input device, returning to ",
                                                       "default setting"))

                                    MessageColor = (255, 0, 0)
                                    self.use_mouse_input = True

                            self.device_connected_update = False

                    (self.translated_text,
                        _) = text_utils.text_formatter.format_text(
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

                    (self.translated_text,
                        returned_text) = text_utils.text_formatter.format_text(
                        "Play",
                        self.language,
                        self.display,
                        ("right", 200*self.y_scale_factor),
                        self.font_color,
                        self.aa,
                        hover1,
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

                    play_width = returned_text.get_width()

                    (self.translated_text,
                        returned_text) = text_utils.text_formatter.format_text(
                        "Settings",
                        self.language,
                        self.display,
                        ("right", 250*self.y_scale_factor),
                        self.font_color,
                        self.aa,
                        hover2,
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

                    settings_width = returned_text.get_width()

                    (self.translated_text,
                        returned_text) = text_utils.text_formatter.format_text(
                        "Character Designer",
                        self.language,
                        self.display,
                        ("right", 300*self.y_scale_factor),
                        self.font_color,
                        self.aa,
                        hover3,
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

                    char_designer_width = returned_text.get_width()

                    (self.translated_text,
                        returned_text) = text_utils.text_formatter.format_text(
                        "Credits",
                        self.language,
                        self.display,
                        ("right", 350*self.y_scale_factor),
                        self.font_color,
                        self.aa,
                        hover5,
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

                    credits_width = returned_text.get_width()

                    (self.translated_text,
                        returned_text) = text_utils.text_formatter.format_text(
                        "Achievements",
                        self.language,
                        self.display,
                        ("right", 400*self.y_scale_factor),
                        self.font_color,
                        self.aa,
                        hover4,
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

                    achievements_width = returned_text.get_width()

                    (self.translated_text,
                        returned_text) = text_utils.text_formatter.format_text(
                        "Benchmark",
                        self.language,
                        self.display,
                        ("right", 450*self.y_scale_factor),
                        self.font_color,
                        self.aa,
                        hover6,
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

                    benchmark_width = returned_text.get_width()

                    (self.translated_text,
                        returned_text) = text_utils.text_formatter.format_text(
                        "Installer",
                        self.language,
                        self.display,
                        ("right", 500*self.y_scale_factor),
                        self.font_color,
                        self.aa,
                        hover7,
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

                    installer_width = returned_text.get_width()

                    if hover1:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(play_width+selector_width)-2,
                                200*self.y_scale_factor))

                        if self.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif hover2:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(settings_width+selector_width)-2,
                                250*self.y_scale_factor))
                        
                        if self.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif hover3:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(char_designer_width+selector_width)-2,
                                300*self.y_scale_factor))

                        if self.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif hover5:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(credits_width+selector_width)-2,
                                350*self.y_scale_factor))

                        if self.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif hover4:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(achievements_width+selector_width)-2,
                                400*self.y_scale_factor))

                        if self.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif hover6:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(benchmark_width+selector_width)-2,
                                450*self.y_scale_factor))

                        if self.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif hover7:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(installer_width+selector_width)-2,
                                500*self.y_scale_factor))

                        if self.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    else:
                        if self.use_mouse_input:
                            pygame.mouse.set_cursor(
                                pygame.SYSTEM_CURSOR_ARROW)

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

                    drawing_utils.draw_rose.create_rose(
                        coloursARRAY,
                        self.shape_color,
                        51,
                        142,
                        524*self.x_scale_factor,
                        524*self.y_scale_factor,
                        self.display)
                        
                    if (self.startup_animation is False and
                            (self.go_to is not None)):
                        
                        return self.go_to

                    if self.go_to is None:
                        self.startup_animation = display_utils.display_animations.fade_in(
                            self.startup_animation,
                            self.real_window_width,
                            self.real_window_height,
                            self.run_timer,
                            self.background_color,
                            self.display,
                            size="limited")
                            
                    else:
                        self.startup_animation = display_utils.display_animations.fade_out(
                            self.startup_animation,
                            self.real_window_width,
                            self.real_window_height,
                            self.run_timer,
                            self.background_color,
                            self.display,
                            self.go_to, 
                            size="limited")

                    pygame.display.update(RenderRect)

                    (target_fps,
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

                    self.clock.tick(target_fps/2)
                    self.run_timer += time.perf_counter()-start_time

                    if self.error_message is not None:
                        self.error_message = "homeScreen: "+str(self.error_message)
                        return

            except Exception as Message:
                error_message = "homeScreen > generate_home > home_gui: "+ str(Message)
                
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
