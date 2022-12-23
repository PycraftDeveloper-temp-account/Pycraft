if __name__ != "__main__":
    try:
        import sys
        import os
        import traceback
        
        import pygame
        import pyautogui
        from PIL import Image, ImageFilter

        import sound_utils
        import display_utils
        import image_utils
        import caption_utils
        import error_utils
        import file_utils
        import tkinter_utils
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
            
    class generate_inventory:
        """
        This class is in charge of setting up, managing, loading and running the
        inventory GUI. This GUI gets loaded as a separate process at the start
        of the game engine and runs only when the game engine sends a command.
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
            the inventory GUI) into a 'generate_inventory' object in a similar
            style to the 'pycraft_main' program. This also initializes the
            inventory's required modules.
            
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

        def inventory_gui(
                dictionary,
                start_inventory):
            """
            This subroutine is in charge of loading and running the inventory GUI. This
            GUI gets loaded as a separate process at the start of the game engine
            and runs only when the game engine sends a command. This is run in
            parallel (process).
            
            - Args:
                - dictionary (dict): This parameter holds all the data that is stored 
                    as 'self' in the game engine. This includes the configuration and
                    user defined settings. Note that the input to this variable must
                    be sorted first to remove any modules or module specific objects.
                    For example a (Pygame Surface) type object as that will cause errors
                    when creating the new process.
                - start_inventory (Multiprocessing Event object): This parameter is an
                    event object used to tell the inventory when the game engine wants
                    to have the inventory displayed. When this event is not set the
                    inventory will wait.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            self = generate_inventory(dictionary)
            try:
                self.input_key = file_utils.pycraft_config_utils.read_input_key(
                    self.platform,
                    self.base_folder)

                self.clock = pygame.time.Clock()

                AlphaSurface = pygame.Surface(
                    (self.real_window_width,
                        self.real_window_height),
                    pygame.HWSURFACE|
                    pygame.SRCALPHA)
                AlphaSurface.set_alpha(204)
                AlphaSurface.fill(self.background_color)

                if self.platform == "Linux":
                    selector = pygame.image.load(
                        os.path.join(
                            self.base_folder,
                            (f"resources//general resources//selectorICON{self.theme}.png")))

                else:
                    selector = pygame.image.load(
                        os.path.join(
                            self.base_folder,
                            (f"resources\\general resources\\selectorICON{self.theme}.png")))

                selector_width = selector.get_width()

                hover1 = False
                hover2 = False
                hover3 = False
                hover4 = False
                hover5 = False
                hover6 = False
                hover7 = False
                hover8 = False

                if self.platform == "Linux":
                    self.title_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 60)

                    self.subtitle_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 35)

                    self.option_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    self.title_backup_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//NotoSans-Regular.ttf")), 60)

                    self.subtitle_backup_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//NotoSans-Regular.ttf")), 35)

                    self.option_backup_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//NotoSans-Regular.ttf")), 30)

                    self.window_icon = pygame.image.load(
                        os.path.join(
                            self.base_folder,
                            ("resources//general resources//Icon.png")))

                else:
                    self.title_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 60)

                    self.subtitle_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 35)

                    self.option_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    self.title_backup_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\NotoSans-Regular.ttf")), 60)

                    self.subtitle_backup_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\NotoSans-Regular.ttf")), 35)

                    self.option_backup_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\NotoSans-Regular.ttf")), 30)
                    
                    self.window_icon = pygame.image.load(
                        os.path.join(
                            self.base_folder,
                            ("resources\\general resources\\Icon.png")))

                self.fullscreen_x, self.fullscreen_y = pyautogui.size()

                self.mouse_x = self.real_window_width/2
                self.mouse_y = self.real_window_height/2

                while True:
                    start_inventory.wait()

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

                    AlphaSurface.convert_alpha()
                    selector.convert()

                    if self.aa:
                        if self.platform == "Linux":
                            pilImage = Image.open(
                                os.path.join(
                                    self.base_folder,
                                    ("resources//general resources//PauseIMG.png"))).resize(
                                        (self.real_window_width,
                                            self.real_window_height),
                                        Image.ANTIALIAS)
                        else:
                            pilImage = Image.open(
                                os.path.join(
                                    self.base_folder,
                                    ("resources\\general resources\\PauseIMG.png"))).resize(
                                        (self.real_window_width,
                                            self.real_window_height),
                                        Image.ANTIALIAS)

                    else:
                        if self.platform == "Linux":
                            pilImage = Image.open(
                                os.path.join(
                                    self.base_folder,
                                    ("resources//general resources//PauseIMG.png"))).resize(
                                        (self.real_window_width,
                                            self.real_window_height))

                        else:
                            pilImage = Image.open(
                                os.path.join(
                                    self.base_folder,
                                    ("resources\\general resources\\PauseIMG.png"))).resize(
                                        (self.real_window_width,
                                            self.real_window_height))

                    BLURRED_pilImage = pilImage.filter(ImageFilter.BoxBlur(5))

                    PauseImg = image_utils.ConvertImage.pilImageToSurface(
                        BLURRED_pilImage).convert()

                    title_width = 0
                    WeaponsTextWidth = 0
                    RangedWeaponsTextWidth = 0
                    ShieldsTextWidth = 0
                    ArmourTextWidth = 0
                    FoodTextWidth = 0
                    ItemsTextWidth = 0
                    SpecialItemsTextWidth = 0
                    OptionsTextWidth = 0

                    while True:
                        caption_utils.generate_captions.get_normal_caption(
                            "Inventory",
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

                        self.display.blit(
                            PauseImg,
                            (0, 0))

                        self.display.blit(
                            AlphaSurface,
                            (0, 0))

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
                            "Inventory",
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
                                
                                start_inventory.clear()

                            if start_inventory.is_set():
                                if event.type == pygame.WINDOWFOCUSLOST:
                                    self.window_in_focus = False
                                elif event.type == pygame.WINDOWFOCUSGAINED:
                                    self.window_in_focus = True

                                if event.type == pygame.WINDOWSIZECHANGED:
                                    self.real_window_width = pygame.display.get_window_size()[0]
                                    self.real_window_height = pygame.display.get_window_size()[1]

                                    AlphaSurface = pygame.Surface(
                                        (self.real_window_width,
                                            self.real_window_height),
                                        pygame.HWSURFACE|
                                        pygame.SRCALPHA).convert_alpha()
                                    AlphaSurface.set_alpha(204)
                                    AlphaSurface.fill(self.background_color)

                                    if self.platform == "Linux":
                                        if self.aa:
                                            pilImage = Image.open(
                                                os.path.join(
                                                    self.base_folder,
                                                    ("resources//general resources//PauseIMG.png"))).resize(
                                                        (self.real_window_width,
                                                            self.real_window_height),
                                                        Image.ANTIALIAS)

                                        else:
                                            pilImage = Image.open(
                                                os.path.join(
                                                    self.base_folder,
                                                    ("resources//general resources//PauseIMG.png"))).resize(
                                                        (self.real_window_width,
                                                            self.real_window_height))

                                    else:
                                        if self.aa:
                                            pilImage = Image.open(
                                                os.path.join(
                                                    self.base_folder,
                                                    ("resources\\general resources\\PauseIMG.png"))).resize(
                                                        (self.real_window_width,
                                                            self.real_window_height),
                                                        Image.ANTIALIAS)

                                        else:
                                            pilImage = Image.open(
                                                os.path.join(
                                                    self.base_folder,
                                                    ("resources\\general resources\\PauseIMG.png"))).resize(
                                                        (self.real_window_width,
                                                            self.real_window_height))

                                    BLURRED_pilImage = pilImage.filter(ImageFilter.BoxBlur(5))

                                    PauseImg = image_utils.ConvertImage.pilImageToSurface(
                                        BLURRED_pilImage).convert()

                                if self.use_mouse_input:
                                    if (((event.type == pygame.MOUSEBUTTONDOWN or
                                            pygame.mouse.get_pressed()[0]) and
                                        (not event.type == pygame.MOUSEMOTION)) and
                                            self.go_to is None):

                                        self.mouse_button_down = True

                                    else:
                                        self.mouse_button_down = False
                                        
                                    if event.type == pygame.KEYDOWN:
                                        if (event.key == self.input_key[
                                                self.input_configuration["keyboard"]["List variables"]][0] and
                                                self.extended_developer_options):

                                            tkinter_utils.tkinter_info.create_tkinter_window(
                                                self,
                                                self.version,
                                                self.background_color,
                                                self.font_color)
                                
                                        if event.key == self.input_key[
                                                self.input_configuration["keyboard"]["Toggle full-screen"]][0]:
                                            
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
                                                self.saved_window_height,
                                                self.fullscreen) = display_utils.display_utils.update_display(
                                                    self.window_icon,
                                                    self.fullscreen,
                                                    self.vsync,
                                                    self.saved_window_width,
                                                    self.saved_window_height,
                                                    self.logging_dictionary,
                                                    self.output_log,
                                                    self.platform,
                                                    self.base_folder,
                                                    fullscreen_x,
                                                    fullscreen_y)

                                            AlphaSurface = pygame.Surface(
                                                (self.fullscreen_x,
                                                    self.fullscreen_y),
                                                pygame.HWSURFACE|
                                                pygame.SRCALPHA).convert_alpha()
                                            AlphaSurface.set_alpha(204)
                                            AlphaSurface.fill(self.background_color)

                                        if event.key == self.input_key[
                                                self.input_configuration["keyboard"]["Confirm"]][0]:
                                            
                                            self.mouse_button_down = True

                        if not start_inventory.is_set():
                            break
                        
                        if (self.mouse_y >= 202*self.y_scale_factor and
                                    self.mouse_y <= 247*self.y_scale_factor and
                                    self.mouse_x >= 1155):

                            hover1 = True
                            if self.mouse_button_down:
                                PauseImg = image_utils.ConvertImage.pilImageToSurface(
                                    BLURRED_pilImage).convert()

                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)

                                self.mouse_button_down = False
                        else:
                            hover1 = False

                        if (self.mouse_y >= 252*self.y_scale_factor and
                                    self.mouse_y <= 297*self.y_scale_factor and
                                    self.mouse_x >= 1105):

                            hover2 = True
                            if self.mouse_button_down:
                                PauseImg = image_utils.ConvertImage.pilImageToSurface(
                                    BLURRED_pilImage).convert()

                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)
                                    
                                self.mouse_button_down = False
                        else:
                            hover2 = False

                        if (self.mouse_y >= 302*self.y_scale_factor and
                                    self.mouse_y <= 347*self.y_scale_factor and
                                    self.mouse_x >= 865):

                            hover3 = True
                            if self.mouse_button_down:
                                PauseImg = image_utils.ConvertImage.pilImageToSurface(
                                    BLURRED_pilImage).convert()

                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)
                                    
                                self.mouse_button_down = False
                        else:
                            hover3 = False

                        if (self.mouse_y >= 402*self.y_scale_factor and
                                    self.mouse_y <= 447*self.y_scale_factor and
                                    self.mouse_x >= 1035):

                            hover4 = True
                            if self.mouse_button_down:
                                PauseImg = image_utils.ConvertImage.pilImageToSurface(
                                    BLURRED_pilImage).convert()

                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)
                                    
                                self.mouse_button_down = False
                        else:
                            hover4 = False

                        if (self.mouse_y >= 352*self.y_scale_factor and
                                    self.mouse_y <= 397*self.y_scale_factor and
                                    self.mouse_x >= 880):

                            hover5 = True
                            if self.mouse_button_down:
                                PauseImg = image_utils.ConvertImage.pilImageToSurface(
                                    BLURRED_pilImage).convert()

                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)
                                    
                                self.mouse_button_down = False
                        else:
                            hover5 = False

                        if (self.mouse_y >= 502*self.y_scale_factor and
                                    self.mouse_y <= 547*self.y_scale_factor and
                                    self.mouse_x >= 1095):

                            hover6 = True
                            if self.mouse_button_down:
                                PauseImg = image_utils.ConvertImage.pilImageToSurface(
                                    BLURRED_pilImage).convert()

                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)
                                    
                                self.mouse_button_down = False
                        else:
                            hover6 = False

                        if (self.mouse_y >= 452*self.y_scale_factor and
                                    self.mouse_y <= 497*self.y_scale_factor and
                                    self.mouse_x >= 1095):

                            hover7 = True
                            if self.mouse_button_down:
                                PauseImg = image_utils.ConvertImage.pilImageToSurface(
                                    BLURRED_pilImage).convert()

                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)
                                    
                                self.mouse_button_down = False
                        else:
                            hover7 = False

                        if (self.mouse_y >= 552*self.y_scale_factor and
                                    self.mouse_y <= 597*self.y_scale_factor and
                                    self.mouse_x >= 1095):

                            hover8 = True
                            if self.mouse_button_down:
                                PauseImg = image_utils.ConvertImage.pilImageToSurface(
                                    BLURRED_pilImage).convert()

                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)
                                    
                                self.mouse_button_down = False
                        else:
                            hover8 = False

                        AlphaSurface.fill(self.background_color)

                        (self.translated_text,
                            returned_text) = text_utils.text_formatter.format_text(
                            "Weapons",
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

                        WeaponsTextWidth = returned_text.get_width()

                        (self.translated_text,
                            returned_text) = text_utils.text_formatter.format_text(
                            "Ranged Weapons",
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

                        RangedWeaponsTextWidth = returned_text.get_width()

                        (self.translated_text,
                            returned_text) = text_utils.text_formatter.format_text(
                            "Shields",
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

                        ShieldsTextWidth = returned_text.get_width()

                        (self.translated_text,
                            returned_text) = text_utils.text_formatter.format_text(
                            "Armour",
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

                        ArmourTextWidth = returned_text.get_width()

                        (self.translated_text,
                            returned_text) = text_utils.text_formatter.format_text(
                            "Food",
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

                        FoodTextWidth = returned_text.get_width()

                        (self.translated_text,
                            returned_text) = text_utils.text_formatter.format_text(
                            "Items",
                            self.language,
                            self.display,
                            ("right", 450*self.y_scale_factor),
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

                        ItemsTextWidth = returned_text.get_width()
                        
                        (self.translated_text,
                            returned_text) = text_utils.text_formatter.format_text(
                            "Special Items",
                            self.language,
                            self.display,
                            ("right", 500*self.y_scale_factor),
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

                        SpecialItemsTextWidth = returned_text.get_width()

                        (self.translated_text,
                            returned_text) = text_utils.text_formatter.format_text(
                            "Options",
                            self.language,
                            self.display,
                            ("right", 550*self.y_scale_factor),
                            self.font_color,
                            self.aa,
                            hover8,
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

                        OptionsTextWidth = returned_text.get_width()
                        
                        if hover1:
                            AlphaSurface.blit(
                                selector,
                                (self.real_window_width-(WeaponsTextWidth+selector_width)-2,
                                    200*self.y_scale_factor))

                        if hover2:
                            AlphaSurface.blit(
                                selector,
                                (self.real_window_width-(RangedWeaponsTextWidth+selector_width)-2,
                                    250*self.y_scale_factor))

                        if hover3:
                            AlphaSurface.blit(
                                selector,
                                (self.real_window_width-(ShieldsTextWidth+selector_width)-2,
                                    300*self.y_scale_factor))

                        if hover4:
                            AlphaSurface.blit(
                                selector,
                                (self.real_window_width-(FoodTextWidth+selector_width)-2,
                                    400*self.y_scale_factor))

                        if hover5:
                            AlphaSurface.blit(
                                selector,
                                (self.real_window_width-(ArmourTextWidth+selector_width)-2,
                                    350*self.y_scale_factor))

                        if hover6:
                            AlphaSurface.blit(
                                selector,
                                (self.real_window_width-(SpecialItemsTextWidth+selector_width)-2,
                                    500*self.y_scale_factor))

                        if hover7:
                            AlphaSurface.blit(
                                selector,
                                (self.real_window_width-(ItemsTextWidth+selector_width)-2,
                                    450*self.y_scale_factor))

                        if hover8:
                            AlphaSurface.blit(
                                selector,
                                (self.real_window_width-(OptionsTextWidth+selector_width)-2,
                                    550*self.y_scale_factor))

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
                error_message = "inventory > generate_inventory > inventory: "+str(Message)

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
