if __name__ != "__main__":
    try:
        import json
        import traceback
        from tkinter import messagebox

        from registry_utils import Registry
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
                "Startup Error",
                str(Message))
            sys.exit()

        except Exception as Message:
            print(Message)
            sys.exit()
            
    class fix_installer(Registry):
        def set_install_location():
            repair = {"PATH": str(Registry.base_folder)}

            installer_config_path = Registry.base_folder / "data files" / "installer_config.json"

            with open(
                    installer_config_path,
                    "w") as file:

                json.dump(
                    repair,
                    file)

        def get_install_location():
            installer_config_path = Registry.base_folder / "data files" / "installer_config.json"
            with open(
                    installer_config_path,
                    "r") as file:

                data = json.load(file)

            return data["PATH"]

    class pycraft_config_utils(Registry):
        def read_main_save():
            pycraft_config_path = Registry.base_folder / "data files" / "pycraft_config.json"

            with open(
                    pycraft_config_path,
                    "r") as file:

                save = json.load(file)

            error_array = []
            for key in Registry.save_keys:
                try:
                    setattr(Registry, key, save[key])
                    
                except KeyError as message_for_array:
                    setattr(Registry, key, Registry.save_keys[key])
                    error_array.append(str(message_for_array))
                    

            if len(error_array) > 0:
                Message = ""

                for error in error_array:
                    Message += error+"\n"
                    
                error_message = "".join(("FileUtils > pycraft_config_utils ",
                                            "> read_main_save: ",
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

                if Registry.detailed_error_messages:
                    logging_utils.create_log_message.update_log_warning(
                        error_message_detailed)
                    
                    messagebox.showerror(
                        "Some saved data was missing",
                        error_message_detailed)
                    
                else:
                    logging_utils.create_log_message.update_log_warning(
                        error_message)
                    
                    messagebox.showerror(
                        "Some saved data was missing",
                        error_message)

            if Registry.average_fps == float("inf"):
                logging_utils.create_log_message.update_log_warning(
                    "Reset average_fps from infinity")

                Registry.average_fps = 1
                Registry.iteration = 1

        def repair_lost_save():
            pycraft_config_path = Registry.base_folder / "data files" / "pycraft_config.json"
            
            with open(
                    pycraft_config_path,
                    "w") as file:

                json.dump(
                    Registry.save_keys,
                    file,
                    indent=1)

        def save_pycraft_config():
            try:
                if Registry.updated:
                    Registry.updated = False

                SavedData = {
                    "theme": Registry.theme,
                    "settings_preset": Registry.settings_preset,
                    "adaptive_fps": Registry.adaptive_fps,
                    "fps": Registry.fps,
                    "average_fps": round(Registry.average_fps, 3),
                    "iteration": Registry.iteration,
                    "FOV": Registry.FOV,
                    "camera_angle_speed": Registry.camera_angle_speed,
                    "aa": Registry.aa,
                    "render_fog": Registry.render_fog,
                    "fancy_graphics": Registry.fancy_graphics,
                    "fancy_particles": Registry.fancy_particles,
                    "sound": Registry.sound,
                    "sound_volume": Registry.sound_volume,
                    "music": Registry.music,
                    "music_volume": Registry.music_volume,
                    "x": round(Registry.x, 4),
                    "y": round(Registry.y, 4),
                    "z": round(Registry.z, 4),
                    "last_run": Registry.current_date,
                    "run_full_startup": Registry.run_full_startup,
                    "crash": False,
                    "saved_window_width": Registry.saved_window_width,
                    "saved_window_height": Registry.saved_window_height,
                    "fullscreen": Registry.fullscreen,
                    "connection_permission": Registry.connection_permission,
                    "updated": Registry.updated,
                    "load_time": [
                        round(Registry.load_time[0], 3),
                        round(Registry.load_time[1], 3)],
                    
                    "show_message": Registry.show_message,
                    "show_strobe_effects": Registry.show_strobe_effects,
                    "extended_developer_options": Registry.extended_developer_options,
                    "draw_devmode_graph": Registry.draw_devmode_graph,
                    "detailed_error_messages": Registry.detailed_error_messages,
                    "logging_dictionary": Registry.logging_dictionary,
                    "save_on_exit": Registry.save_on_exit,
                    "resolution_preset": Registry.resolution_preset,
                    "vsync": Registry.vsync,
                    "aa_quality": Registry.aa_quality,
                    "detailed_captions": Registry.detailed_captions,
                    "output_log": Registry.output_log,
                    "increased_speed": Registry.increased_speed,
                    "skip_time": Registry.skip_time,
                    "remove_file_permission": Registry.remove_file_permission,
                    "input_configuration": Registry.input_configuration,
                    "resolution": Registry.resolution,
                    "dont_use_set_resolution": Registry.dont_use_set_resolution,
                    "seasonal_events": Registry.seasonal_events,
                    "compile_math": Registry.compile_math,
                    "custom_theme": Registry.custom_theme,
                    "language": Registry.language,
                    "use_transparency_effects": Registry.use_transparency_effects,
                    "auto_save_frequency": Registry.auto_save_frequency,
                    "mono_audio": Registry.mono_audio,
                    "audio_quality": Registry.audio_quality,
                    # temp
                    "position": [0, 0, 0],
                    "rotation": [0, 0],
                    "game_time": 0,
                    "weather": "sunny",
                    "day": 1
                }

                pycraft_config_path = Registry.base_folder / "data files" / "pycraft_config.json"

                with open(
                        pycraft_config_path,
                        "w") as file:

                    json.dump(
                        SavedData,
                        file,
                        indent=1)
                        
            except Exception as Message:
                error_message = "FileUtils > pycraft_config_utils > SaveTOpycraft_configFILE: "+str(Message)

                error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                error_utils.generate_error_screen.error_screen(
                    error_message,
                    error_message_detailed)

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
