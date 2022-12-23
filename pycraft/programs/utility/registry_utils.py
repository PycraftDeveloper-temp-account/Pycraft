if __name__ != "__main__":
    try:
        import datetime
        import random
        import os
        
        import pygame
        import pyautogui
        import googletrans

        import seasonal_events_utils
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
            
    class generate_registry:
        """
        This class is in charge of setting all the default values, and making sure every
        variable defined in 'self' exists, reducing the risk of errors because variables
        are not defined. This is sorted alphabetically.
        
        - Args:
            - None
                
        - Keyword Args:
            - None

        - Output:
            - None
        """
        def __init__(self):
            pass

        def registry(
                self):
            """
            This subroutine is in charge of setting all the default values, and making sure every
            variable defined in 'self' exists, reducing the risk of errors because variables
            are not defined. This is sorted alphabetically. This must always be called at startup
            (in 'pycraft_main').
            
            - Args:
                - self (dict): This is used by Pycraft as a way of storing it's current
                    configuration and behaviour and is required by most GUIs. Its use should be
                    reduced where possible for readability reasons.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
        
            CurrentTime = datetime.datetime.now()
            
            self.FOV = 70
            self.fps = 60
            self.fps_overclock = False
            self.average_fps = 0
            self.aa = True
            self.aa_quality = "2x"
            self.accent_color = (237, 125, 49)
            self.background_color = [30, 30, 30]
            self.camera = None
            self.camera_angle_speed = 3.5
            self.camera_enabled = True
            self.clear_cache = False
            self.clear_languages_cache = False
            self.clock = pygame.time.Clock()
            self.colour_presets = {
                "red": (255, 0, 0),
                "dark red": (128, 0, 0),
                "green": (0, 255, 0),
                "dark green": (0, 128, 0),
                "blue": (0, 0, 255),
                "dark blue": (0, 0, 128),
                "yellow": (255, 255, 0),
                "dark yellow": (128, 128, 0),
                "turquoise": (0, 255, 255),
                "dark turquoise": (0, 128, 128),
                "purple": (255, 0, 255),
                "dark purple": (128, 0, 128),
                "light grey": (80, 80, 80),
                "dark grey": (30, 30, 30),
                "black": (0, 0, 0),
                "white": (255, 255, 255),
                "orange": (237, 125, 49)
            }

            self.command = None
            self.compile_math = True
            self.connection_permission = None
            self.connection_status = False
            self.crash = False
            self.ctx = 0
            self.current_date = "".join((f"{CurrentTime.day}/",
                                        f"{CurrentTime.month}/",
                                        f"{CurrentTime.year}"))
            
            self.current_memory_usage = 0
            self.current_time = CurrentTime
            self.currently_displaying_message = False
            self.custom_theme = None
            self.data_CPU_usage = []
            self.data_CPU_usage_Max = 1
            self.data_average_fps = []
            self.data_average_fps_Max = 1
            self.data_current_fps = []
            self.data_current_fps_Max = 1
            self.data_memory_usage = []
            self.data_memory_usage_Max = 1
            self.date = str(datetime.date.today())
            self.detailed_captions = False
            self.detailed_error_messages = False
            self.device_connected = False
            self.device_connected_update = False
            self.display = 0
            self.draw_devmode_graph = False
            self.current_fps = 60
            self.error_message = None
            self.error_message_detailed = None
            self.event = seasonal_events_utils.configure_seasonal_event.is_seasonal_event(
                self.date)

            self.exit_mode = None
            self.extended_developer_options = False
            self.fancy_graphics = True
            self.fancy_particles = True

            self.folder_size = 0

            self.colors = [(224, 175, 160),
                                (181, 68, 110),
                                (144, 227, 154),
                                (125, 131, 255),
                                (43, 65, 98),
                                (175, 66, 174),
                                (77, 157, 224),
                                (0, 212, 140),
                                (6, 141, 157),
                                (109, 157, 197),
                                (232, 141, 103),
                                (97, 61, 193),
                                (155, 197, 61)]
                
            self.chosen_colors = []

            temporary_colors = self.colors
            for _ in range(9):
                index = random.randint(0, len(temporary_colors)-1)
                self.chosen_colors.append(temporary_colors[index])
                del temporary_colors[index]
                
            self.file_structure = {"Source code": {"size": 0, "color": self.chosen_colors[0]},
                                        "Data files": {"size": 0, "color": self.chosen_colors[1]},
                                        "Audio": {"size": 0, "color": self.chosen_colors[2]},
                                        "Video": {"size": 0, "color": self.chosen_colors[3]},
                                        "Images": {"size": 0, "color": self.chosen_colors[4]},
                                        "3D objects": {"size": 0, "color": self.chosen_colors[5]},
                                        "Temporary": {"size": 0, "color": self.chosen_colors[6]},
                                        "Fonts": {"size": 0, "color": self.chosen_colors[7]},
                                        "Misc": {"size": 0, "color": self.chosen_colors[8]}}

            if self.platform == "Linux":
                self.files_to_trash = ["resources//benchmark resources//Crate.obj.bin",
                                "resources//game engine resources//map//map.obj.bin",
                                "resources//game engine resources//map//map.obj.json",
                                "resources//game engine resources//map//map2.obj.bin",
                                "resources//game engine resources//map//map2.obj.json",
                                "resources//game engine resources//clouds//Rnd_noise.png",
                                "resources//general resources//PauseIMG.png"]

            else:
                self.files_to_trash = ["resources\\benchmark resources\\Crate.obj.bin",
                                "resources\\game engine resources\\map\\map.obj.bin",
                                "resources\\game engine resources\\map\\map.obj.json",
                                "resources\\game engine resources\\map\\map2.obj.bin",
                                "resources\\game engine resources\\map\\map2.obj.json",
                                "resources\\game engine resources\\clouds\\Rnd_noise.png",
                                "resources\\general resources\\PauseIMG.png"]

            for dirpath, _, files in os.walk(self.base_folder):
                for name in files:
                    if "__pycache__" in str(dirpath):
                        if ".pyc" in str(name) or ".nbc" in str(name) or ".nbi" in str(name):
                            file_path = os.path.join(dirpath, name)
                            self.files_to_trash.append(file_path)
            
            self.font_color = (255, 255, 255)
            self.FOV = 90
            self.format_text_chars = {
                "$r": (255, 0, 0), # red
                "$g": (0, 255, 0), # green
                "$b": (0, 0, 255), # blue
                "$y": (255, 255, 0), # yellow
                "$t": (0, 255, 255), # turquoise
                "$p": (255, 0, 255), # purple
                "$u": "<underline>", # underlines font
                "$c": "<bold>", # makes the font bold
                "$i": "<italics>", # makes the font to italics
                "$s": "<shape_color>", # sets the color to the (themed) shape color
                "$a": "<accent_color>", # sets the color to the (themed) accent color
                "$v": "<secondary_font_color>", # sets the color to the (themed) secondary font color
                "$/": "<fake_space>" # acts like the space character, but isn't displayed
            }

            self.fps = 60
            self.from_game_GUI = False
            self.from_play = False
            self.fullscreen = False
            self.fullscreen_x = pyautogui.size()[0]
            self.fullscreen_y = pyautogui.size()[1]
            
            self.game_engine_control = [[False, False],
                                        [False, False],
                                        [False, False],
                                        [False, False]]
            
            self.get_outdated = [False, False]
            self.go_to = None
            self.increased_speed = False
            self.input_configuration = None
            self.install_location = None
            self.iteration = 1
            self.joystick_connected = False
            self.joystick_exit = False
            self.joystick_hat_pressed = False
            self.joystick_zoom = None
            self.language = "en"
            self.language_list = googletrans.LANGUAGES
            self.last_run = "29/09/2021"
            self.load_3D = True
            self.load_music = True
            self.load_time = [0, 1]
            self.logging_dictionary = {
                "information": False,
                "warnings": False,
                "errors": False}
            
            self.mouse_button_down = False
            self.mouse_x = 0
            self.mouse_y = 0
            self.music = True
            self.music_volume = 5
            self.outdated = False
            self.output_log = False
            self.play_time = 0
            self.progress_line = []
            self.progress_message_text = "Initiating"
            self.project_sleeping = False
            self.pygame_device_added_update = False
            self.pygame_device_removed_update = False
            self.real_window_height = 720
            self.real_window_width = 1280
            self.adaptive_fps = 60
            self.remove_file_permission = None
            self.render_fog = True
            self.reset_pycraft = False
            self.resolution = "(1280, 720)"
            self.dont_use_set_resolution = False
            self.resolutions_list = {
                "(1024, 576)": "(16:9) 1024 x 576",
                "(1152, 648)": "(16:9) 1152 x 648",
                "(1280, 720)": "(16:9) 1280 x 720 (HD)",
                "(1366, 768)": "(16:9) 1366 x 768",
                "(1600, 900)": "(16:9) 1600 x 900",
                "(1920, 1080)": "(16:9) 1920 x 1080 (Full HD)",
                "(2560, 1440)": "(16:9) 2560 x 1440",
                "(3840, 2160)": "(16:9) 3840 x 2160 (4K UHD)",
                "(7680, 4320)": "(16:9) 7680 x 4320 (8K UHD)"
            }
            
            self.resolution_preset = "default"
            self.run_full_startup = False
            self.run_timer = 0
            self.save_keys = {
                "theme": False,
                "settings_preset": "high",
                "adaptive_fps": 60,
                "fps": 60,
                "average_fps": 60,
                "iteration": 1,
                "FOV": 75,
                "camera_angle_speed": 3,
                "aa": True,
                "render_fog": True,
                "fancy_graphics": True,
                "fancy_particles": True,
                "sound": True,
                "sound_volume": 75,
                "music": False,
                "music_volume": 50,
                "x": 0,
                "y": 0,
                "z": 0,
                "last_run": "29/09/2021",
                "run_full_startup": True,
                "crash": False,
                "saved_window_width": 1280,
                "saved_window_height": 720,
                "fullscreen": True,
                "connection_permission": None,
                "updated": True,
                "load_time": [0, 1],
                "show_message": False,
                "show_strobe_effects": None,
                "extended_developer_options": False,
                "draw_devmode_graph": False,
                "detailed_error_messages": False,
                "logging_dictionary": {"information": False,
                                            "warnings": False,
                                            "errors": False},
                "save_on_exit": True,
                "resolution_preset": "default",
                "vsync": True,
                "aa_quality": "2x",
                "detailed_captions": False,
                "output_log": False,
                "increased_speed": False,
                "skip_time": False,
                "remove_file_permission": None,
                "input_configuration": {
                    "keyboard": {
                        "Jump": "Space",
                        "Back": "Esc",
                        "Toggle full-screen": "F11",
                        "List variables": "Q",
                        "Walk forwards": "W",
                        "Walk backwards": "S", 
                        "Walk left": "A", 
                        "Walk right": "D",
                        "Open inventory": "E",
                        "Open map": "R",
                        "Unlock mouse": "L",
                        "Skip time": "K",
                        "Confirm": "Enter",
                        "Increase speed": "I"},

                    "controller": {
                        "Confirm": 1,
                        "Back": 3,
                        "Open inventory": 7,
                        "Open map": 6,
                        "Jump": 3
                    }
                },
                "resolution": "(1280, 720)",
                "dont_use_set_resolution": False,
                "seasonal_events": False,
                "compile_math": True,
                "custom_theme": None
            }
            
            self.save_on_exit = True
            self.saved_window_height = 720
            self.saved_window_width = 1280
            self.scan_pycraft = False
            self.seasonal_events = False
            self.secondary_font_color = (100, 100, 100)
            self.selected_input_reconfig = "keyboard"
            self.settings_preset = "Medium"
            self.shape_color = (80, 80, 80)
            self.show_strobe_effects = None
            self.show_message = True
            self.skip_time = False
            self.sound = True
            self.sound_volume = 75
            self.startup_animation = True
            self.theme = False
            self.timer = 0
            self.total_move_x = 0
            self.total_move_y = 0
            self.total_move_z = 0
            self.total_number_of_updates = 0
            self.translated_text = {}
            self.updated = False
            self.use_mouse_input = True
            self.version = "9.5.5"
            self.vsync = True
            self.vsync_fps = 60
            self.window_in_focus = True
            self.wnd = None
            self.x = 0
            self.x_scale_factor = 0
            self.y = 0
            self.y_scale_factor = 0
            self.z = 0
                
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
