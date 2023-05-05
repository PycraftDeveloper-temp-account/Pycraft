if __name__ != "__main__":
    try:
        from urllib import request
        import traceback
        import pathlib
        import requests
        from requests.adapters import TimeoutSauce
        import re
        import importlib.util as importlib_util
        
        from registry_utils import Registry

        import error_utils
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in integrated_installer_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
        
    class MyTimeout(TimeoutSauce):
        def __init__(self, *args, **kwargs):
            if kwargs['connect'] is None:
                kwargs['connect'] = 5
            if kwargs['read'] is None:
                kwargs['read'] = 5
            super(MyTimeout, self).__init__(*args, **kwargs)

    requests.adapters.TimeoutSauce = MyTimeout
    
    class integrated_installer(Registry):
        def text_version_to_int(name):
            version_code = ""
            broken_down = re.split("[.dev]", name[1])
            if broken_down[1] != "0":
                for element in broken_down:
                    if len(element) > 0:
                        version_code += ("0"*(3-len(element))+element)
            
            try:
                return int(version_code)
            except:
                return 0
            
        def get_versions():
            version_IDs = {}
            r = requests.get(
                'https://api.github.com/repos/PycraftDeveloper/Pycraft/tags',
                timeout=30)
            raw = r.text
            array = raw.split("},{")
            for element in array:
                name = re.sub('["\[\]{}]', "", element[1:-1]).split(",")
                name = name[0].split(":")
                version_code = integrated_installer.text_version_to_int(name)
                if version_code > 9005000007:
                    version_IDs[name[1]] = version_code

            Registry.pycraft_versions = version_IDs
            
        def check_versions():
            try:
                if Registry.pycraft_install_path is not None:
                    pycraft_main_install_path = pathlib.Path(Registry.pycraft_install_path) / "pycraft" / "main.py"
                    pycraft_main_spec = importlib_util.spec_from_file_location(
                        "main", 
                        pycraft_main_install_path)
                    pycraft_main = importlib_util.module_from_spec(pycraft_main_spec)
                    pycraft_main_spec.loader.exec_module(pycraft_main)
                    version_name = pycraft_main.QueryVersion()

                    version_code = integrated_installer.text_version_to_int(version_name.split(" "))
                    for key in Registry.pycraft_versions:
                        if version_code < Registry.pycraft_versions[key]:
                            Registry.outdated = True
                            break
            except Exception as message:
                error_message = "".join(("IntegratedInstaller > integrated_installer ",
                                             f"> check_versions: {str(message)}"))

                error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        message,
                        message.__traceback__))

                error_utils.generate_error_screen.error_screen(
                    error_message,
                    error_message_detailed)


    class check_connection(Registry):
        def test():
            try:
                request.urlopen(
                    "https://www.google.com",
                    timeout=1)

                return True
            
            except:
                return False

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
