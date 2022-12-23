if __name__ != "__main__":
    try:
        import os
        import json

        import googletrans
        
        import logging_utils
        import integrated_installer_utils
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

    class translation_caching:
        def __init__(self):
            pass

        def write_cache(platform, base_folder, translated_text):
            if platform == "Linux":
                with open(
                    os.path.join(
                        base_folder,
                        ("data files//translated_data.json")), "w") as file:

                    json.dump(
                        translated_text,
                        file,
                        indent=1)

            else:
                with open(
                    os.path.join(
                        base_folder,
                        ("data files\\translated_data.json")), "w") as file:

                    json.dump(
                        translated_text,
                        file,
                        indent=1)

        def read_cache(platform, base_folder):
            if platform == "Linux":
                with open(
                    os.path.join(
                        base_folder,
                        ("data files//translated_data.json")), "r") as file:

                    translated_text = json.load(file)

            else:
                with open(
                    os.path.join(
                        base_folder,
                        ("data files\\translated_data.json")), "r") as file:

                    translated_text = json.load(file)

            return translated_text

    class string_translator:
        def __init__(self):
            pass

        def change_language(language, string, translated_text, logging_dictionary, output_log, platform, base_folder, connection_permission):
            if language != "en" and len(str(string).strip()) > 0:
                found = False
                try:
                    for key in translated_text:
                        if key == string:
                            found = True
                            translate = translated_text[key]
                except Exception as Message:
                    log_message = f"Dictionary of translated phrases is empty. More details: {Message}"
                    logging_utils.create_log_message.update_log_warning(
                        logging_dictionary,
                        log_message,
                        output_log,
                        platform,
                        base_folder)

                if found is False:
                    if connection_permission:
                        try:
                            translator = googletrans.Translator()
                            translate = str(translator.translate(string, dest=language).text)
                        except Exception as message:
                            connection_status = integrated_installer_utils.CheckConnection.test()

                            if connection_status:
                                error_message = "".join(("translation_utils > string_translator > change_language: ",
                                                            "An error occured whilst trying to translate ",
                                                            f"text ('{string}'). More details: {message}"))

                                raise Exception(error_message) from message

                            else:
                                log_message = f"translation_utils > string_translator > change_language: {str(message)}"

                                logging_utils.create_log_message.update_log_warning(
                                    logging_dictionary,
                                    log_message,
                                    output_log,
                                    platform,
                                    base_folder)
                                
                            translate = string

                    else:
                        translate = string
                                
                translated_text[string] = translate

                return translate, translated_text
            
            else:
                return string, translated_text

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
