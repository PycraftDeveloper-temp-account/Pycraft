if __name__ != "__main__":
    try:
        import json
        import pathlib

        import googletrans
        import pygame
        
        from registry_utils import Registry
        
        import logging_utils
        import integrated_installer_utils
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in translation_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
        
    class TranslationFileHandling(Registry):
        def __init__(self) -> None:
            file_path = Registry.base_folder / "data files" / "translated_data.json"
            self.translated_cache_path = pathlib.Path(file_path)
            if self.translated_cache_path.exists() is False:
                with open(
                        self.translated_cache_path,
                        "w",
                        encoding="utf-8") as file:

                    json.dump(
                        obj={},
                        fp=file,
                        indent=1)

    class TranslationCaching(Registry):
        def __init__(self) -> None:
            self.translated_cache_path = TranslationFileHandling().translated_cache_path
            
        def write_cache(self) -> None:
            with open(
                    self.translated_cache_path,
                    "w",
                    encoding="utf-8") as file:

                json.dump(
                    obj=Registry.translated_text,
                    fp=file,
                    indent=1)

        def read_cache(self) -> None:
            with open(
                    self.translated_cache_path,
                    "r",
                    encoding="utf-8",) as file:

                Registry.translated_text = json.load(
                    fp=file)

    class TranslateText(Registry):
        def __init__(self):
            pass
        
        def change_language(
                self,
                string: str) -> str:
            
            if Registry.language != "en" and len(str(string).strip()) > 0:
                pygame.event.pump()
                found = False
                try:
                    for key in Registry.translated_text:
                        if key == string:
                            found = True
                            translate = Registry.translated_text[key]
                except Exception as message:
                    log_message = f"Dictionary of translated phrases is empty. More details: {message}"
                    logging_utils.create_log_message.update_log_warning(
                        log_message)

                if found is False:
                    if Registry.connection_permission:
                        try:
                            translator = googletrans.Translator()
                            translate = str(translator.translate(
                                string,
                                dest=Registry.language).text)
                            
                        except Exception as message:
                            connection_status = integrated_installer_utils.check_connection.test()

                            if connection_status:
                                error_message = "".join(("translation_utils > TranslateText > change_language: ",
                                                            "An error occurred whilst trying to translate ",
                                                            f"text ('{string}'). More details: {message}"))

                                raise Exception(error_message) from message

                            else:
                                log_message = f"translation_utils > TranslateText > change_language: {str(message)}"

                                logging_utils.create_log_message.update_log_warning(
                                    log_message)
                                
                            translate = string

                    else:
                        translate = string
                                
                Registry.translated_text[string] = translate

                return translate
            
            else:
                return string

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
