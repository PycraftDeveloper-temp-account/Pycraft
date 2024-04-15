if __name__ != "__main__":
    try:
        import threading
        import os
        import shutil
        from tkinter import messagebox
        import subprocess
        import sys
        import venv
        import requests
        import json
        import platform

        from registry_utils import Registry

        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft Installer",
            f"A problem occurred whilst trying to start Pycraft Installer.\nMore Details: {error}")

    class InstallCoordinator:
        def __init__(self):
            self.main_install_thread = threading.Thread(target=self.main)
            self.install_directory = Registry.install_directory
            self.temporary_directory = None
            self.src_directory = None
            self.resources_directory = None
            self.component_progress = (1/8)*100

        def start(self):
            self.main_install_thread.start()

        def main(self):
            self.install_directory = path_utils.Path(f"{Registry.install_directory}/Pycraft").path
            self.temporary_directory = path_utils.Path(f"{self.install_directory}/temporary").path
            self.src_directory = path_utils.Path(f"{self.install_directory}/src").path
            self.resources_directory = path_utils.Path(f"{self.install_directory}/resources").path
            self.environment_directory = path_utils.Path(f"{self.install_directory}/venv").path
            self.pycraft_environment_directory = path_utils.Path(f"{self.install_directory}/venv/pycraft").path
            if platform.system() == "Windows":
                self.activate_environment_directory = path_utils.Path(f"{self.install_directory}/venv/pycraft/Scripts/activate.bat").path
            else:
                self.activate_environment_directory = path_utils.Path(f"{self.install_directory}/venv/pycraft/bin/activate").path
            self.setup_directories()

            environment_setup_thread = threading.Thread(target=self.setup_venv)
            environment_setup_thread.start()

            download_source_code_thread = threading.Thread(target=self.download_source_code)
            download_source_code_thread.start()

            environment_setup_thread.join()
            download_source_code_thread.join()

            download_resources_thread = threading.Thread(target=self.download_resources)
            download_resources_thread.start()

            download_resources_thread.join()

        def setup_directories(self): # 1/8 or 12.5
            try:
                os.mkdir(self.install_directory)
            except FileExistsError:
                try:
                    answer = messagebox.askyesno("Pycraft: Installer", "This directory is not empty.\nDo you want to overwrite it?")
                    if answer:
                        shutil.rmtree(self.install_directory)
                        os.mkdir(self.install_directory)
                except:
                    messagebox.showerror("Pycraft: Installer", "Pycraft's installation has failed.\nThis is likely because of a file permission error.")
            except:
                messagebox.showerror("Pycraft: Installer", "Pycraft's installation has failed.\nThis is likely because of a file permission error.")

            Registry.progressbar['value'] += self.component_progress/6
            os.mkdir(self.temporary_directory)
            Registry.progressbar['value'] += self.component_progress/6
            os.mkdir(self.src_directory)
            Registry.progressbar['value'] += self.component_progress/6
            os.mkdir(self.resources_directory)
            Registry.progressbar['value'] += self.component_progress/6
            os.mkdir(self.environment_directory)
            Registry.progressbar['value'] += self.component_progress/6
            os.mkdir(self.pycraft_environment_directory)
            Registry.progressbar['value'] += self.component_progress/6

        def setup_venv(self):
            venv.create(self.pycraft_environment_directory, with_pip=True)
            Registry.progressbar['value'] += self.component_progress

        def download_source_code(self):
            online_version = "0.0.0"
            try:
                try:
                    response = requests.get(
                        "https://api.github.com/repos/PycraftDeveloper/Pycraft/tags")
                    response.raise_for_status()
                except requests.exceptions.ConnectionError:
                    messagebox.showerror("Pycraft: Installer", "Pycraft's installation has failed.\nThis is likely because the installer couldn't access the internet.")

                try:
                    laames_tags = json.loads(response.text)
                    result =  laames_tags[0]["name"]
                except (IndexError, UnboundLocalError):
                    pass

                else:
                    online_version = result
            except Exception:
                messagebox.showerror("Pycraft: Installer", "Pycraft's installation has failed.\nUnable to get latest online version from GitHub")

            base_url = "http://api.github.com/repos/PycraftDeveloper/Pycraft/zipball/"
            online_content_url = f"{base_url}{str(online_version)}"

            request = requests.get(online_content_url)
            download_size = len(request.content)

            progress = self.component_progress/download_size

            source_code_download_file = path_utils.Path(f"{self.temporary_directory}/pycraft_sc.zip").path

            with requests.get(
                online_content_url,
                stream=True) as request:

                request.raise_for_status()
                with open(
                        source_code_download_file,
                        'wb') as file:

                    for chunk in request.iter_content(
                            chunk_size=None):
                        Registry.progressbar['value'] += progress*len(chunk)
                        file.write(chunk)

        def extract_source_code(self):
            pass

        def activate_venv(self, additional_command):
            if platform.system() == "Windows":
                command = ""
            else:
                command = "source"
            command = f"{command} {self.activate_environment_directory} && {additional_command}"

            return subprocess.Popen([*command.split()])

        def download_resources(self):
            self.activate_venv("pip install mediafiregrabber").communicate()

            resource_downloader_file = path_utils.Path(f"{Registry.base_path}/src/utility/resource_downloader.py").path

            downloaded_resources_folder = path_utils.Path(f"{self.temporary_directory}/pycraft_rs").path

            os.mkdir(downloaded_resources_folder)

            resource_downloader_process = subprocess.Popen([sys.executable, resource_downloader_file, downloaded_resources_folder])
            resource_downloader_process.communicate()

        def install_dependencies(self):
            pass

        def extract_resources(self):
            pass

        def clean_up(self):
            pass

else:
    MESSAGE = "You need to run this as part of Pycraft's Installer. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
