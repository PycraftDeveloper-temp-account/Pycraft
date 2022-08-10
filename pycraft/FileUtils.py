if __name__ != "__main__":
    print("Started <Pycraft_FileUtils>")

    class FixInstaller:
        def __init__(self):
            pass

        def Setinstall_location(self):
            try:
                Repair = {"PATH":self.base_folder}

                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//installer_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            Repair,
                            openFile)

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\installer_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            Repair,
                            openFile)

            except Exception as Message:
                self.error_message = "".join(("FileUtils > FixInstaller ",
                                             f"> Setinstall_location: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

        def Getinstall_location(self):
            try:
                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//installer_config.json")), "r") as openFile:

                        StoredData = self.mod_json__.load(openFile)

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\installer_config.json")), "r") as openFile:

                        StoredData = self.mod_json__.load(openFile)

                self.install_location = StoredData["PATH"]
            except Exception as Message:
                print("Message:", Message)
                self.install_location = None

    class LoadSaveFiles:
        def __init__(self):
            pass

        def ReadMainSave(self):
            if self.platform == "Linux":
                with open(
                    self.mod_OS__.path.join(
                        self.base_folder,
                        ("data files//pycraft_config.json")), "r") as openFile:

                    save = self.mod_json__.load(openFile)

            else:
                with open(
                    self.mod_OS__.path.join(
                        self.base_folder,
                        ("data files\\pycraft_config.json")), "r") as openFile:

                    save = self.mod_json__.load(openFile)

            self.theme = save["theme"]
            self.run_full_startup = save["startup"]
            self.crash = save["crash"]
            self.fullscreen = save["WindowStatus"]
            self.recommended_FPS = save["AdaptiveFPS"]
            self.devmode = save["devmode"]
            self.settings_preference = save["profile"]
            self.FPS = save["FPS"]

            self.aFPS = save["aFPS"]
            self.iteration = save["iteration"]

            if self.aFPS == float("inf"):
                self.aFPS = 1
                self.iteration = 1

            self.FOV = save["FOV"]
            self.camera_angle_speed = save["camera_angle_speed"]
            self.render_fog = save["render_fog"]
            self.aa = save["aa"]
            self.x = save["X"]
            self.y = save["Y"]
            self.z = save["Z"]
            self.fancy_graphics = save["fancy_graphics"]
            self.fancy_particles = save["fancy_particles"]
            self.sound = save["sound"]
            self.sound_volume = save["sound_volume"]
            self.music = save["music"]
            self.music_volume = save["music_volume"]
            self.last_run = save["last_run"]
            self.saved_window_width = save["displayWidth"]
            self.saved_window_height = save["displayHeight"]
            self.connection_permission = save["connection_permission"]
            self.total_vertices = save["total_vertices"]
            self.updated = save["updated"]
            self.resource_check_time = save["resource_load_time"]
            self.load_time = save["load_time"]
            if self.total_vertices == 0:
                self.total_vertices = 1
            self.show_message = save["show_message"]
            self.show_lightning = save["show_lightning"]

        def RepairLostSave(self):
            try:
                SavedData = {"total_vertices": 0,
                             "theme": False,
                             "profile": "Medium",
                             "devmode": 0,
                             "AdaptiveFPS": 60,
                             "FPS": 60,
                             "aFPS": 60,
                             "iteration": 1,
                             "FOV": 75,
                             "camera_angle_speed": 3,
                             "aa": True,
                             "render_fog": True,
                             "fancy_graphics": True,
                             "fancy_particles": True,
                             "sound": True,
                             "sound_volume": 75,
                             "music": True,
                             "music_volume": 50,
                             "X": 0,
                             "Y": 0,
                             "Z": 0,
                             "last_run": "29/09/2021",
                             "startup": True,
                             "crash": False,
                             "displayWidth":1280,
                             "displayHeight":720,
                             "WindowStatus":True,
                             "connection_permission": None,
                             "updated": True,
                             "load_time": [0, 1],
                             "resource_load_time": [0, 0],
                             "show_message": False,
                             "show_lightning": False}

                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//pycraft_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            SavedData,
                            openFile)

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\pycraft_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            SavedData,
                            openFile)

            except Exception as Message:
                self.error_message = "FileUtils > LoadSaveFiles > RepairLostSave: "+str(Message)
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

        def SaveTOconfigFILE(self):
            try:
                current_time = self.mod_datetime__.datetime.now()
                current_date = f"{current_time.day}/{current_time.month}/{current_time.year}"

                if self.updated:
                    self.updated = False

                SavedData = {"total_vertices": self.total_vertices,
                                "theme": self.theme,
                                "profile": self.settings_preference,
                                "devmode": self.devmode,
                                "AdaptiveFPS": self.recommended_FPS,
                                "FPS": self.FPS,
                                "aFPS": self.aFPS,
                                "iteration": self.iteration,
                                "FOV": self.FOV,
                                "camera_angle_speed": self.camera_angle_speed,
                                "aa": self.aa,
                                "render_fog": self.render_fog,
                                "fancy_graphics": self.fancy_graphics,
                                "fancy_particles": self.fancy_particles,
                                "sound": self.sound,
                                "sound_volume": self.sound_volume,
                                "music": self.music,
                                "music_volume": self.music_volume,
                                 "X": self.x,
                                 "Y": self.y,
                                 "Z": self.z,
                                "last_run": current_date,
                                "startup": self.run_full_startup,
                                "crash": False,
                                "displayWidth": self.saved_window_width,
                                "displayHeight": self.saved_window_height,
                                "WindowStatus": self.fullscreen,
                                "connection_permission": self.connection_permission,
                                "updated": self.updated,
                                "load_time": self.load_time,
                                "resource_load_time": [self.resource_check_time[0],
                                                    self.resource_check_time[1]],
                                "show_message": self.show_message,
                                "show_lightning": self.show_lightning}

                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//pycraft_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            SavedData,
                            openFile)

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\pycraft_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            SavedData,
                            openFile)
            except Exception as Message:
                self.error_message = "FileUtils > LoadSaveFiles > SaveTOpycraft_configFILE: "+str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

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
