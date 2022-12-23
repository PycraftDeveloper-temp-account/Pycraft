if __name__ != "__main__":
    try:
        import os
        import json
        import traceback
        from tkinter import messagebox
        import datetime
        
        import send2trash

        import logging_utils
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
            
    class delete_files:
        def __init__(self):
            pass

        def clear_temporary_files(
                platform,
                base_folder,
                files_to_trash,
                logging_dictionary,
                output_log):
            
            for i in range(len(files_to_trash)):
                try:
                    send2trash.send2trash(
                        os.path.join(
                            base_folder,
                            files_to_trash[i]))
                    
                except Exception as Message:
                    log_message = "".join(("FileUtils > delete_files > ",
                                        "clear_temporary_files: Unable ",
                                        "to remove file as it likely ",
                                        "doesn't exist. More details:\n",
                                        f"{str(Message)}"))

                    logging_utils.create_log_message.update_log_warning(
                        logging_dictionary,
                        log_message,
                        output_log,
                        platform,
                        base_folder)

                else:
                    logging_utils.create_log_message.update_log_information(
                        logging_dictionary,
                        f"Cleared: {os.path.join(base_folder, files_to_trash[i])} \nwhich is considered a temporary file",
                        output_log,
                        platform,
                        base_folder)
                
    class scan_folder:
        def __init__(self):
            pass

        def search_files(
                directory,
                logging_dictionary,
                output_log,
                platform,
                base_folder,
                file_structure,
                files_to_trash):
            
            logging_utils.create_log_message.update_log_information(
                logging_dictionary,
                f"Scanning {directory}",
                output_log,
                platform,
                base_folder)

            for key in file_structure:
                file_structure[key]["size"] = 0

            folder_size = 0
            trash_files_array = []
            for i in range(len(files_to_trash)):
                trash_files_array.append(os.path.join(
                    base_folder, files_to_trash[i]))
                
            files_array = []
            for dirpath, _, files in os.walk(directory):
                for name in files:
                    file_path = os.path.join(dirpath, name)
                    files_array.append(file_path)
                    folder_size += os.path.getsize(file_path)

            for i in range(len(files_array)):
                trash = False
                for j in range(len(trash_files_array)):
                    if files_array[i] == trash_files_array[j]:
                        trash = True
                        file_structure["Temporary"]["size"] += os.path.getsize(
                            files_array[i])

                if trash is False:
                    if (".ogg" in files_array[i] or
                            ".wav" in files_array[i] or
                            ".mp3" in files_array[i]):
                        
                        file_structure["Audio"]["size"] += os.path.getsize(
                            files_array[i])

                    elif ".ttf" in files_array[i]:
                        file_structure["Fonts"]["size"] += os.path.getsize(
                            files_array[i])

                    elif (".txt" in files_array[i] or
                            ".json" in files_array[i] or
                            ".md" in files_array[i]):
                        
                        file_structure["Data files"]["size"] += os.path.getsize(
                            files_array[i])

                    elif (".py" in files_array[i] or
                            ".glsl" in files_array[i]):
                        
                        file_structure["Source code"]["size"] += os.path.getsize(
                            files_array[i])

                    elif (".obj" in files_array[i] or
                            ".mtl" in files_array[i]):
                        
                        file_structure["3D objects"]["size"] += os.path.getsize(
                            files_array[i])

                    elif (".png" in files_array[i] or
                            ".jpg" in files_array[i] or
                            ".ico" in files_array[i] or
                            ".gif" in files_array[i]):
                        
                        file_structure["Images"]["size"] += os.path.getsize(
                            files_array[i])

                    else:
                        logging_utils.create_log_message.update_log_information(
                            logging_dictionary,
                            f"Not currently categorised: {files_array[i]}",
                            output_log,
                            platform,
                            base_folder)

                        file_structure["Misc"]["size"] += os.path.getsize(
                            files_array[i])

            return file_structure, folder_size
                        
    class FixInstaller:
        def __init__(self):
            pass

        def Setinstall_location(platform, base_folder):
            Repair = {"PATH": base_folder}

            if platform == "Linux":
                with open(
                    os.path.join(
                        base_folder,
                        ("data files//installer_config.json")), "w") as openFile:

                    json.dump(
                        Repair,
                        openFile)

            else:
                with open(
                    os.path.join(
                        base_folder,
                        ("data files\\installer_config.json")), "w") as openFile:

                    json.dump(
                        Repair,
                        openFile)

        def Getinstall_location(platform, base_folder):
            if platform == "Linux":
                with open(
                    os.path.join(
                        base_folder,
                        ("data files//installer_config.json")), "r") as openFile:

                    StoredData = json.load(openFile)

            else:
                with open(
                    os.path.join(
                        base_folder,
                        ("data files\\installer_config.json")), "r") as openFile:

                    StoredData = json.load(openFile)

            return StoredData["PATH"]

    class pycraft_config_utils:
        def __init__(self):
            pass

        def read_input_key(platform, base_folder):
            if platform == "Linux":
                with open(
                    os.path.join(
                        base_folder,
                        ("data files//input_key.json")), "r") as openFile:

                    input_key = json.load(openFile)

            else:
                with open(
                    os.path.join(
                        base_folder,
                        ("data files\\input_key.json")), "r") as openFile:

                    input_key = json.load(openFile)

            return input_key

        def ReadMainSave(self):
            if self.platform == "Linux":
                with open(
                    os.path.join(
                        self.base_folder,
                        ("data files//pycraft_config.json")), "r") as openFile:

                    save = json.load(openFile)

            else:
                with open(
                    os.path.join(
                        self.base_folder,
                        ("data files\\pycraft_config.json")), "r") as openFile:

                    save = json.load(openFile)

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
                    
                error_message = "".join(("FileUtils > pycraft_config_utils ",
                                            "> ReadMainSave: ",
                                            "Your some of your saved file ",
                                            "was missing, we have attempted ",
                                            "to recover missing data."))

                error_message_detailed = "".join(("FileUtils > pycraft_config_utils ",
                                                    "> ReamMainSave: ",
                                                    "Your some of your saved file ",
                                                    "was missing, we have attempted ",
                                                    "to recover missing data.\n",
                                                    "The following entries were ",
                                                    "missing and have been ",
                                                    f"reset:\n{Message}"))

                if self.detailed_error_messages:
                    logging_utils.create_log_message.update_log_warning(
                        self.logging_dictionary,
                        error_message_detailed,
                        self.output_log,
                        self.platform,
                        self.base_folder)
                    
                    messagebox.showerror(
                        "Some saved data was missing",
                        error_message_detailed)
                    
                else:
                    logging_utils.create_log_message.update_log_warning(
                        self.logging_dictionary,
                        error_message,
                        self.output_log,
                        self.platform,
                        self.base_folder)
                    
                    messagebox.showerror(
                        "Some saved data was missing",
                        error_message)

            if self.average_fps == float("inf"):
                logging_utils.create_log_message.update_log_warning(
                    self.logging_dictionary,
                    "Reset average_fps from infinity",
                    self.output_log,
                    self.platform,
                    self.base_folder)

                self.average_fps = 1
                self.iteration = 1

        def RepairLostSave(self):
            if self.platform == "Linux":
                with open(
                    os.path.join(
                        self.base_folder,
                        ("data files//pycraft_config.json")), "w") as openFile:

                    json.dump(
                        self.save_keys,
                        openFile,
                        indent=1)

            else:
                with open(
                    os.path.join(
                        self.base_folder,
                        ("data files\\pycraft_config.json")), "w") as openFile:

                    json.dump(
                        self.save_keys,
                        openFile,
                        indent=1)

        def save_pycraft_config(self):
            try:
                current_time = datetime.datetime.now()
                current_date = f"{current_time.day}/{current_time.month}/{current_time.year}"

                if self.updated:
                    self.updated = False

                SavedData = {
                    "theme": self.theme,
                    "settings_preset": self.settings_preset,
                    "adaptive_fps": self.adaptive_fps,
                    "fps": self.fps,
                    "average_fps": round(self.average_fps, 3),
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
                    "show_strobe_effects": self.show_strobe_effects,
                    "extended_developer_options": self.extended_developer_options,
                    "draw_devmode_graph": self.draw_devmode_graph,
                    "detailed_error_messages": self.detailed_error_messages,
                    "logging_dictionary": self.logging_dictionary,
                    "save_on_exit": self.save_on_exit,
                    "resolution_preset": self.resolution_preset,
                    "vsync": self.vsync,
                    "aa_quality": self.aa_quality,
                    "detailed_captions": self.detailed_captions,
                    "output_log": self.output_log,
                    "increased_speed": self.increased_speed,
                    "skip_time": self.skip_time,
                    "remove_file_permission": self.remove_file_permission,
                    "input_configuration": self.input_configuration,
                    "resolution": self.resolution,
                    "dont_use_set_resolution": self.dont_use_set_resolution,
                    "seasonal_events": self.seasonal_events,
                    "compile_math": self.compile_math,
                    "custom_theme": self.custom_theme
                }

                if self.platform == "Linux":
                    with open(
                        os.path.join(
                            self.base_folder,
                            ("data files//pycraft_config.json")), "w") as openFile:

                        json.dump(
                            SavedData,
                            openFile,
                            indent=1)

                else:
                    with open(
                        os.path.join(
                            self.base_folder,
                            ("data files\\pycraft_config.json")), "w") as openFile:

                        json.dump(
                            SavedData,
                            openFile,
                            indent=1)
                        
            except Exception as Message:
                error_message = "FileUtils > pycraft_config_utils > SaveTOpycraft_configFILE: "+str(Message)

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
