if __name__ != "__main__":
    try:
        import os
        import tkinter
        from tkinter import messagebox
        import tkinter.ttk as tkinter_ttk
        import threading
        import json
        import sys

        import install

        import tkinter_utils
        import installer_utils
        import text_utils
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
            
    class BeginUninstall:
        def __init__(self):
            pass

        def UninstallScreen_0(self, root, PycPath, ChooseBETA, Choice):
            root = tkinter_utils.tkinter_installer.create_display(
                root,
                self.platform,
                self.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Modify Your install - Uninstall",
                background='white',
                font=(None, 20)).place(x=200, y=35)

            text = tkinter.Text(
                root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            UninstallerInstructions = "".join(("You have arrived at Pycraft's uninstall ",
                                               "utility, here you can remove Pycraft from ",
                                               "your system and/or remove the project's ",
                                               "additional files, these will be sent to ",
                                               "your recycle bin so you have the option to ",
                                               "change your mind.\n\nIf you want to feel ",
                                               "free to feedback any bugs, ideas or ",
                                               "suggestions to the developers who's contact ",
                                               "you can find here: ",
                                               "https://github.com/PycraftDeveloper/Pycraft"))

            text.insert(tkinter.INSERT, UninstallerInstructions)
            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)

            def GetConformation():
                global UpdateUtility
                UpdateUtility = False
                if messagebox.askokcancel(
                    "Are you sure with your decision",
                    "".join(("Please now take the time to make sure you have ",
                             "chosen correctly as some options will clear all ",
                             "settings and progress made! \n\nPress OK to ",
                             "continue the uninstall process"))):

                    ans = messagebox.askquestion(
                        "Permissions manager",
                        "Can we have permission to remove and change some files on your PC?")

                    while ans == "no":
                        ans2 = messagebox.askquestion(
                            "Caution",
                            "".join(("We did not receive permission to remove and modify ",
                                     "files on this PC, as a result we cannot uninstall ",
                                     "Pycraft, would you like to amend this decision (yes) ",
                                     "or close the installer (no)?")))

                        if ans2 == "no":
                            quit()
                        else:
                            ans = messagebox.askquestion(
                                "Permissions manager",
                                "Can we have permission to remove and change files on your PC?")

                    if Uninstall_Option.get() == 1:
                        BeginUninstall.Remove_But_Keep_Save(
                            self,
                            root,
                            PycPath,
                            ChooseBETA,
                            Choice)

                    elif Uninstall_Option.get() == 2:
                        BeginUninstall.Remove_But_Leave(
                            self,
                            root,
                            PycPath,
                            ChooseBETA,
                            Choice)

                    else:
                        BeginUninstall.Remove_All(
                            self,
                            root,
                            PycPath,
                            ChooseBETA,
                            Choice)

            tkinter_ttk.Button(
                root,
                text='home',
                command=lambda: installer_utils.core_installer_functionality.home(
                    self,
                    root,
                    PycPath,
                    ChooseBETA, Choice)).place(x=680, y=500)

            tkinter_ttk.Button(
                root,
                text='Continue',
                command=GetConformation).place(x=760, y=500)

            Uninstall_Option = tkinter.IntVar()

            tkinter_ttk.Radiobutton(
                root,
                text="Remove Pycraft and additional files but keep save data",
                variable=Uninstall_Option,
                value=1).place(x=200, y=200)

            tkinter_ttk.Radiobutton(
                root,
                text="Remove Pycraft but leave additional files",
                variable=Uninstall_Option,
                value=2).place(x=200, y=225)

            tkinter_ttk.Radiobutton(
                root,
                text="Remove everything",
                variable=Uninstall_Option,
                value=3).place(x=200, y=250)

            Uninstall_Option.set(1)

            root.mainloop()


        def Remove_All(self, root, PycPath, ChooseBETA, Choice):
            root = tkinter_utils.tkinter_installer.create_display(root, self.platform, self.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Uninstalling Pycraft and all additional files",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            OUTPUTtext = "Querying versions"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            import pycraft_main
            version = pycraft_main.QueryVersion()
            OUTPUTtext += f"\nPreparing to remove {version} and additional files"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            FileArray = installer_utils.file_manipulation.search_files(
                self,
                PycPath)

            import site
            if self.platform == "Linux":
                AdditionalFileArray = installer_utils.file_manipulation.search_files(
                    self,
                    (site.getuserbase()+"//Python310//site-packages"))

            else:
                AdditionalFileArray = installer_utils.file_manipulation.search_files(
                    self,
                    (site.getuserbase()+"\\Python310\\site-packages"))

            FileArray = FileArray+AdditionalFileArray
            OUTPUTtext += f"\nIdentified {len(FileArray)} files to remove"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            threading.Thread(
                target=installer_utils.file_manipulation.remove_files,
                args=(self,
                        FileArray,)).start()

            OUTPUTtext += f"\nRemoving {version}"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            i = 0
            def Render_Progressbar(i):
                CompletionProgressbar = tkinter_ttk.Progressbar(
                    root,
                    orient=tkinter.HORIZONTAL,
                    length=100,
                    mode='indeterminate')

                CompletionProgressbar.place(x=200, y=500)
                CompletionProgressbar['value'] += i
                root.update()

            while "remove_files" in threading.enumerate():
                i += 1
                root.after(
                    50,
                    Render_Progressbar(i))

            OUTPUTtext += f"\nSuccessfully removed {version} and additional files"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            OUTPUTtext += "\nCleaning Up"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            try:
                os.rmdir(PycPath)
                
            except:
                pass

            OUTPUTtext += "\nDone"
            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            BeginUninstall.Finish_Uninstall(
                self,
                root)


        def Remove_But_Keep_Save(self, root, PycPath, ChooseBETA, Choice):
            root = tkinter_utils.tkinter_installer.create_display(
                root,
                self.platform,
                self.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Uninstalling Pycraft and all additional files but keeping save data",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            OUTPUTtext = "Querying versions"
            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            import pycraft_main
            version = pycraft_main.QueryVersion()
            OUTPUTtext += f"\nPreparing to remove {version} and additional files"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            FileArray = installer_utils.file_manipulation.search_files(
                self,
                PycPath)

            import site
            if self.platform == "Linux":
                AdditionalFileArray = installer_utils.file_manipulation.search_files(
                    self,
                    (site.getuserbase()+"//Python310//site-packages"))
            
            else:
                AdditionalFileArray = installer_utils.file_manipulation.search_files(
                    self,
                    (site.getuserbase()+"\\Python310\\site-packages"))

            FileArray = FileArray+AdditionalFileArray
            OUTPUTtext += f"\nIdentified {len(FileArray)} files to remove"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            threading.Thread(
                target=installer_utils.file_manipulation.remove_files,
                args=(self,
                        FileArray,)).start()

            OUTPUTtext += f"\nRemoving {version}"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            i = 0
            def Render_Progressbar(i):
                CompletionProgressbar = tkinter_ttk.Progressbar(
                    root,
                    orient=tkinter.HORIZONTAL,
                    length=100,
                    mode='indeterminate')

                CompletionProgressbar.place(x=200, y=500)
                CompletionProgressbar['value'] += i
                root.update()

            while "remove_files" in threading.enumerate():
                i += 1
                root.after(
                    50,
                    Render_Progressbar(i))

            OUTPUTtext += f"\nSuccessfully removed {version} and additional files"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            OUTPUTtext += "\nCleaning Up"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            OUTPUTtext += "\nDone"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            try:
                global UpdateUtility
                if not UpdateUtility:
                    BeginUninstall.Finish_Uninstall(
                        self,
                        root)

            except:
                if self.platform == "Linux":
                    with open(
                        os.path.join(
                            self.base_folder,
                            ("data files//installer_config.json")), 'r') as openFile:

                        SavedData = json.load(openFile)

                else:
                    with open(
                        os.path.join(
                            self.base_folder,
                            ("data files\\installer_config.json")), 'r') as openFile:

                        SavedData = json.load(openFile)
                    
                Dir = SavedData["PATH"]

                install.Begininstall.installScreen_2(
                    self,
                    root,
                    Choice,
                    Dir)


        def Remove_But_Leave(self, root, PycPath, ChooseBETA, Choice):
            root = tkinter_utils.tkinter_installer.create_display(
                root,
                self.platform,
                self.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Uninstalling Pycraft but keeping additional files",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            OUTPUTtext = "Querying versions"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            import pycraft_main
            version = pycraft_main.QueryVersion()
            OUTPUTtext += f"\nPreparing to remove {version}"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            FileArray = installer_utils.file_manipulation.search_files(
                self,
                PycPath)

            OUTPUTtext += f"\nIdentified {len(FileArray)} files to remove"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            threading.Thread(
                target=installer_utils.file_manipulation.remove_files,
                args=(self,
                        FileArray,)).start()

            OUTPUTtext += f"\nRemoving {version}"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            i = 0
            def Render_Progressbar(i):
                CompletionProgressbar = tkinter_ttk.Progressbar(
                    root,
                    orient=tkinter.HORIZONTAL,
                    length=100,
                    mode='indeterminate')

                CompletionProgressbar.place(x=200, y=500)
                CompletionProgressbar['value'] += i
                root.update()

            while "remove_files" in threading.enumerate():
                i += 1
                root.after(
                    50,
                    Render_Progressbar(i))

            OUTPUTtext += f"\nSuccessfully removed {version}"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            OUTPUTtext += "\nCleaning Up"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            try:
                os.rmdir(PycPath)
                
            except:
                pass

            OUTPUTtext += "\nDone"

            text_utils.installerText.CreateText(
                root,
                OUTPUTtext)

            BeginUninstall.Finish_Uninstall(
                self,
                root)


        def Finish_Uninstall(self, root):
            root = tkinter_utils.tkinter_installer.create_display(
                root,
                self.platform,
                self.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Successfully uninstalled Pycraft",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            EnterText = "".join(("Pycraft has been removed from your computer, ",
                                 "you can re-install the project at any time ",
                                 "from GitHub, SourceForge or PyPi. If you ",
                                 "have experienced any bugs or have any ",
                                 "suggestions then feel free to share them ",
                                 "on the project page!"))

            text = tkinter.Text(
                root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                EnterText)

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=40)

            tkinter_ttk.Button(
                root,
                text='Quit',
                command=sys.exit).place(x=760, y=500)

            root.mainloop()

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
