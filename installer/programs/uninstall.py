if __name__ != "__main__":
    try:
        import os
        import tkinter
        from tkinter import messagebox
        import tkinter.ttk as tkinter_ttk
        import threading
        import json
        import site
        import time
        
        from registry_utils import Registry

        import install

        import tkinter_utils
        import installer_utils
        import text_utils
        import uninstall_utils
        import file_utils
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in uninstall"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class Uninstall(Registry):
        def uninstall_screen_one():
            tkinter_utils.tkinter_installer.create_display()

            tkinter.Label(
                Registry.root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                Registry.root,
                text="Modify Your install - Uninstall",
                background='white',
                font=(None, 20)).place(x=200, y=35)

            text = tkinter.Text(
                Registry.root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            UninstallerInstructions = Registry.installer_text["uninstall"][0]

            text.insert(tkinter.INSERT, UninstallerInstructions)
            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)

            tkinter_ttk.Button(
                Registry.root,
                text='Home',
                command=installer_utils.core_installer_functionality.home).place(x=680, y=500)

            tkinter_ttk.Button(
                Registry.root,
                text='Continue',
                command=uninstall_utils.uninstall_screen_one.get_confirmation).place(x=760, y=500)

            uninstall_utils.uninstaller_data.uninstall_option = tkinter.IntVar()

            tkinter_utils.tkinter_installer.style("TRadiobutton")
            tkinter_ttk.Radiobutton(
                Registry.root,
                text="Remove Pycraft and additional files but keep save data",
                variable=uninstall_utils.uninstaller_data.uninstall_option,
                value=1).place(x=200, y=200)

            tkinter_utils.tkinter_installer.style("TRadiobutton")
            tkinter_ttk.Radiobutton(
                Registry.root,
                text="Remove Pycraft but leave additional files",
                variable=uninstall_utils.uninstaller_data.uninstall_option,
                value=2).place(x=200, y=225)

            tkinter_utils.tkinter_installer.style("TRadiobutton")
            tkinter_ttk.Radiobutton(
                Registry.root,
                text="Remove everything",
                variable=uninstall_utils.uninstaller_data.uninstall_option,
                value=3).place(x=200, y=250)

            uninstall_utils.uninstaller_data.uninstall_option.set(1)

            Registry.root.mainloop()
            
        def uninstall_screen_two():
            tkinter_utils.tkinter_installer.create_display()

            tkinter.Label(
                Registry.root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                Registry.root,
                text="Uninstalling Pycraft",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            text_utils.installer_text.create_text(
                uninstall_utils.uninstaller_data.output_text)
            
            uninstall_utils.uninstaller_data.version = installer_utils.core_installer_functionality.get_installed_pycraft_version()

            uninstall_utils.uninstaller_data.output_text += f"\nPreparing to remove {uninstall_utils.uninstaller_data.version}"

            text_utils.installer_text.create_text(
                uninstall_utils.uninstaller_data.output_text)
            
            if uninstall_utils.uninstaller_data.uninstall_option.get() == 1:
                Uninstall.remove_but_keep_save()

            elif uninstall_utils.uninstaller_data.uninstall_option.get() == 2:
                Uninstall.remove_but_leave()

            else:
                Uninstall.remove_all()
                
            uninstall_utils.uninstaller_data.output_text += "\nDone"
            text_utils.installer_text.create_text(
                uninstall_utils.uninstaller_data.output_text)
                
            Uninstall.finish_uninstall()

        def remove_all():
            # Removes Pycraft - Yes
            # Removes Pycraft's saves - Yes
            # Removes dependencies - Yes
            uninstall_utils.uninstaller_data.output_text += f"\nRemoving {uninstall_utils.uninstaller_data.version}'s dependencies"

            text_utils.installer_text.create_text(
                uninstall_utils.uninstaller_data.output_text)

            uninstall_thread = threading.Thread(
                target=installer_utils.file_manipulation.uninstall_dependencies)
            uninstall_thread.name = "[thread]: Uninstalling Pycraft's dependencies"
            uninstall_thread.start()

            start = time.perf_counter()
            i = 0
            while threading.active_count() == 2:
                i += 1
                Registry.root.after(
                    50,
                    installer_utils.core_installer_functionality.render_progress_bar(i))
                
            uninstall_time = time.perf_counter()-start
                
            uninstall_utils.uninstaller_data.output_text += f" - done in {round(uninstall_time, 2)} seconds"

            text_utils.installer_text.create_text(
                uninstall_utils.uninstaller_data.output_text)
            
            uninstall_utils.uninstaller_data.output_text += f"\nRemoving {uninstall_utils.uninstaller_data.version}"

            text_utils.installer_text.create_text(
                uninstall_utils.uninstaller_data.output_text)
            
            os.rmdir(Registry.pycraft_install_path)

            uninstall_utils.uninstaller_data.output_text += f"\nSuccessfully removed {uninstall_utils.uninstaller_data.version} and additional files"

            text_utils.installer_text.create_text(
                uninstall_utils.uninstaller_data.output_text)

        def remove_but_keep_save():
            # Removes Pycraft - Yes
            # Removes Pycraft's saves - No
            # Removes dependencies - Yes
            FileArray = installer_utils.file_manipulation.search_files(Registry.pycraft_install_path)

            uninstall_utils.uninstaller_data.output_text += f"\nRemoving {uninstall_utils.uninstaller_data.version}"

            text_utils.installer_text.create_text(
                uninstall_utils.uninstaller_data.output_text)
            
            uninstall_thread = threading.Thread(
                target=installer_utils.file_manipulation.remove_files,
                args=(FileArray,))
            uninstall_thread.name = "[thread]: Uninstalling Pycraft"
            uninstall_thread.start()
            
            i = 0
            while threading.active_count() == 2:
                i += 1
                Registry.root.after(
                    50,
                    installer_utils.core_installer_functionality.render_progress_bar(i))

            uninstall_utils.uninstaller_data.output_text += f"\nSuccessfully removed {uninstall_utils.uninstaller_data.version}"

            text_utils.installer_text.create_text(
                uninstall_utils.uninstaller_data.output_text)

            uninstall_thread = threading.Thread(
                target=installer_utils.file_manipulation.uninstall_dependencies)
            uninstall_thread.name = "[thread]: Uninstalling Pycraft's dependencies"
            uninstall_thread.start()

            uninstall_utils.uninstaller_data.output_text += f"\nRemoving {uninstall_utils.uninstaller_data.version}'s dependencies"

            text_utils.installer_text.create_text(
                uninstall_utils.uninstaller_data.output_text)

            i = 0
            while threading.active_count() == 2:
                i += 1
                Registry.root.after(
                    50,
                    installer_utils.core_installer_functionality.render_progress_bar(i))

            uninstall_utils.uninstaller_data.output_text += f"\nSuccessfully removed {uninstall_utils.uninstaller_data.version} and additional files"

            text_utils.installer_text.create_text(
                uninstall_utils.uninstaller_data.output_text)

        def remove_but_leave():
            # Removes Pycraft - Yes
            # Removes Pycraft's saves - No
            # Removes dependencies - No
            uninstall_utils.uninstaller_data.output_text += f"\nRemoving {uninstall_utils.uninstaller_data.version}"

            text_utils.installer_text.create_text(
                uninstall_utils.uninstaller_data.output_text)

            os.rmdir(Registry.pycraft_install_path)

            uninstall_utils.uninstaller_data.output_text += f"\nSuccessfully removed {uninstall_utils.uninstaller_data.version}"

            text_utils.installer_text.create_text(
                uninstall_utils.uninstaller_data.output_text)

        def finish_uninstall():
            Registry.pycraft_install_path = None
            file_utils.fix_installer.set_installer_config()
            
            tkinter_utils.tkinter_installer.create_display()

            tkinter.Label(
                Registry.root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                Registry.root,
                text="Successfully uninstalled Pycraft",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            EnterText = Registry.installer_text["uninstall"][3]

            text = tkinter.Text(
                Registry.root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                EnterText)

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=40)

            tkinter_ttk.Button(
                Registry.root,
                text='Quit',
                command=quit).place(x=760, y=500)

            Registry.root.mainloop()

else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
