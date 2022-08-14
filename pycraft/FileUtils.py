from ast import keyword


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

                self.mod_error_utils__.generate_error_screen.error_screen(self)

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

            error_array = []
            for key in self.save_keys:
                try:
                    setattr(self, key, save[key])
                except Exception as message_for_array:
                    setattr(self, key, self.save_keys[key])
                    error_array.append(str(message_for_array))
                    

            if len(error_array) > 0:
                Message = ""

                for error in error_array:
                    Message += error+"\n"
                    
                error_message = "".join(("FileUtils > LoadSaveFiles ",
                                              "> ReadMainSave: ",
                                              "Your some of your saved file ",
                                              "was missing, we have attempted ",
                                              "to recover missing data."))

                error_message_detailed = "".join(("FileUtils > LoadSaveFiles ",
                                                       "> ReamMainSave: ",
                                                       "Your some of your saved file ",
                                                       "was missing, we have attempted ",
                                                       "to recover missing data.\n",
                                                       "The following entries were ",
                                                       "missing and have been ",
                                                       f"reset:\n{Message}"))

                if self.devmode == 10:
                    print(error_message_detailed)
                    self.mod_tkinter_messagebox_.showerror("Some saved data was missing",
                                                           error_message_detailed)
                else:
                    print(error_message)
                    self.mod_tkinter_messagebox_.showerror("Some saved data was missing",
                                                           error_message)

            if self.aFPS == float("inf"):
                self.aFPS = 1
                self.iteration = 1

        def RepairLostSave(self):
            try:
                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//pycraft_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            self.save_keys,
                            openFile,
                            indent=1)

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\pycraft_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            self.save_keys,
                            openFile,
                            indent=1)

            except Exception as Message:
                self.error_message = "FileUtils > LoadSaveFiles > RepairLostSave: "+str(Message)
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def SaveTOconfigFILE(self):
            try:
                current_time = self.mod_datetime__.datetime.now()
                current_date = f"{current_time.day}/{current_time.month}/{current_time.year}"

                if self.updated:
                    self.updated = False

                SavedData = {"theme": self.theme,
                                "settings_preference": self.settings_preference,
                                "devmode": self.devmode,
                                "AdaptiveFPS": self.recommended_FPS,
                                "FPS": self.FPS,
                                "aFPS": round(self.aFPS, 3),
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
                                "x": round(self.x, 4),
                                "y": round(self.y, 4),
                                "z": round(self.z, 4),
                                "last_run": current_date,
                                "run_full_startup": self.run_full_startup,
                                "crash": False,
                                "saved_window_width": self.saved_window_width,
                                "saved_window_height": self.saved_window_height,
                                "fullscreen": self.fullscreen,
                                "connection_permission": self.connection_permission,
                                "updated": self.updated,
                                "load_time": [
                                    round(self.load_time[0], 3),
                                    round(self.load_time[1], 3)],
                                
                                "show_message": self.show_message,
                                "show_lightning": self.show_lightning}

                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//pycraft_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            SavedData,
                            openFile,
                            indent=1)

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\pycraft_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            SavedData,
                            openFile,
                            indent=1)
            except Exception as Message:
                self.error_message = "FileUtils > LoadSaveFiles > SaveTOpycraft_configFILE: "+str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

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
