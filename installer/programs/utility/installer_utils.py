if __name__ != "__main__":
    try:
        import os
        import sys
        import subprocess
        from zipfile import ZipFile
        import pathlib
        import requests
        from requests.adapters import TimeoutSauce
        import re
        from tkinter import messagebox
        import importlib.util as importlib_util
        import tkinter.ttk as tkinter_ttk
        import tkinter
        
        from registry_utils import Registry

        import installer_home
        
        import file_utils
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in installer_utils"
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

    class core_installer_functionality(Registry):
        def render_progress_bar(i):
            CompletionProgressbar = tkinter_ttk.Progressbar(
                Registry.root,
                orient=tkinter.HORIZONTAL,
                length=100,
                mode="indeterminate")

            CompletionProgressbar.place(x=200, y=500)

            CompletionProgressbar["value"] += i
            Registry.root.update()
            
        def close():
            if messagebox.askokcancel(
                "Pycraft Setup Wizard",
                "Are you sure you want to quit?"):

                Registry.root.destroy()
                sys.exit()


        def home():
            installer_home.installer_home.start()
            
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
            
        def get_installed_pycraft_version():
            pycraft_main_install_path = pathlib.Path(Registry.pycraft_install_path) / "pycraft" / "main.py"
            pycraft_main_spec = importlib_util.spec_from_file_location(
                "main", 
                pycraft_main_install_path)
            pycraft_main = importlib_util.module_from_spec(pycraft_main_spec)
            pycraft_main_spec.loader.exec_module(pycraft_main)
            return pycraft_main.QueryVersion()
                
        def outdated_detector():
            try:
                version_name = core_installer_functionality.get_installed_pycraft_version()
                version_code = core_installer_functionality.text_version_to_int(version_name.split(" "))
                for key in Registry.pycraft_versions:
                    if version_code < Registry.pycraft_versions[key]:
                        Registry.outdated = True
                        break
                    
            except Exception as message:
                messagebox.showerror(
                    "An error has occurred",
                    "".join(("We were unable to check for updates to Pycraft, ",
                             "the most likely reason for this is a faulty ",
                             "internet connection.\n\nFull Error ",
                             f"message:\n{message}")))

                quit()

    class file_manipulation(Registry):
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
                if "dev" in name[1]:
                    if not Registry.developer_version:
                        continue
                
                version_code = core_installer_functionality.text_version_to_int(name)
                if version_code > 9005000007:
                    version_IDs[name[1]] = version_code

            Registry.pycraft_versions = version_IDs
            
        def install_dependencies():
            requirements_file_path = pathlib.Path(Registry.pycraft_install_path) / "requirements.txt"
            subprocess.check_output(
                f"{sys.executable} -m pip install -r \"{str(requirements_file_path)}\"")

        def download(base_folder, install_path, choice):
            try:
                if " (latest)" in choice or choice == "Latest":
                    version = list(Registry.pycraft_versions.keys())[0]
                    url = f"https://github.com/PycraftDeveloper/Pycraft/archive/refs/tags/{version}.zip"
                else:
                    url = f"https://github.com/PycraftDeveloper/Pycraft/archive/refs/tags/{choice.split(' ')[1]}.zip"
                
                path = install_path / "TEMP.zip"

                session = requests.Session()
                online_download = session.get(url)

                online_download.raise_for_status()
                
                with open(path, "wb") as file:
                    file.write(online_download.content)
                
                with ZipFile(path, "r") as zip_file:
                    file_names = zip_file.namelist()
                    zip_file.extractall(path=path.parent)
                    
                extracted_file_path = path.parent / file_names[0]
                
                new_data = {"pycraft_install_path": str(extracted_file_path)}
                file_utils.fix_installer.update_install_config(new_data)
                
                Registry.pycraft_install_path = extracted_file_path
                
                file_utils.fix_installer.link_pycraft_to_installer()
                
                os.remove(str(path))
            except Exception as message:
                messagebox.showerror(
                    "An error ocurred",
                    "".join(("We were unable to install the additional ",
                             "files Pycraft needs in-order to install.\n\n",
                             f"Full Error message: {message}")))

                quit()

        def search_files(directory):
            arr = []
            print(f"Scanning {directory}")
            for dirpath, dirnames, files in os.walk(directory):
                for name in files:
                    arr.append(f"{dirpath}\{name}")
                    
            return arr
        
        def uninstall_dependencies():
            requirements_file_path = pathlib.Path(Registry.pycraft_install_path) / "requirements.txt"
            subprocess.check_output(
                f"{sys.executable} -m pip uninstall -r \"{str(requirements_file_path)}\"")

        def remove_files(FileArray, keep_save=True):
            try:
                for i in range(len(FileArray)):
                    try:
                        if keep_save:
                            if not (pathlib.Path(FileArray[i]).name == "pycraft_config.json" or
                                    pathlib.Path(FileArray[i]).name == "pycraft config.json"):

                                os.remove(FileArray[i])

                        else:
                            os.remove(FileArray[i])

                    except Exception as message:
                        print(message)
                        
            except Exception as message:
                messagebox.showerror(
                    "An error ocurred",
                    "".join(("We were unable to remove some files for ",
                             f"Pycraft from your PC.\n\nFull Error message: {message}")))

                quit()

else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
