Nomenclature and programming techniques
====================

Pycraft maintains a scheme for naming variables and controlling code structure in Pycraft; this section details all the information you will need for understanding the structure for the program, in addition to the nomenclature (a series of rules that determines how objects should be named). This section will also help you understand the comments and documentation attached below; we strongly recommend you read this before getting started!

Some of these rules are NOT yet integrated into Pycraft, but will be accommodated into versions of Pycraft greater than or equal to v0.9.4 (or v0.9.4-1 pre-release found here: https://github.com/PycraftDeveloper/Pycraft-Insider-Preview).

Variables
++++++++++++++++++++

* All variables should be named in accordance to its function, or based on a description of the data it stores.
* There is no limit to the length of the name of a variable as at current there is no limit on the length of a of code.
* Here are some good examples of variable names. ``StoreRandomNumber`` or ``StoreMapVertexBuffer``

Subroutines
++++++++++++++++++++

* Subroutines can be of any length, as there is no limit to the length of a of code in Pycraft at present.
* Subroutines should avoid using global variables as much as possible, as this makes it easier to trace variables and possible bugs. (The exceptions here being the ``Class_Startup_variables`` and ``self`` variables which are referenced throughout the different modules for Pycraft).
* Subroutines should be named according to their function, and not be dependent on other code in a specific module to work. (For example, making a random number generator that relies on global variables created elsewhere in a module)
* Subroutines should only have parameters if they are used within the subroutine.
* If a function returns a value, then this must be implicitly stated in the documentation here.

Modules
++++++++++++++++++++

* All modules should be preceded by the following code, regardless of function:

.. code-block:: python

    if not __name__ == "__main__":
        print("Started <Pycraft_<name>>")
        class <name>:
            def __init__(self):
                pass
             
* All modules should also be proceeded by the following code, the ‘else’ here is important, this connects to the 'if' statement we created above:

.. code-block:: python

    else:
        print("You need to run this as part of Pycraft")
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
        quit()

* If a module does not directly have its own GUI (for example the Achievements GUI is made by the 'Achievements.py' file), then it should have 'Utils' attached at the end of the name, this specifies that the program contains code that aids the creation of the game. There may already be a suitable 'Utils' file already. (If the subroutine your creating involves the use of Tkinter, even if it is to create a GUI, and is NOT part of the installer, then place that code under the 'Tkinterutils.py' file).

* Modules that are only ever used in a thread, must be placed into the 'ThreadingUtils.py' file.

* Modules can be broken down into as many classes as needed, but all subroutines must be placed in classes where possible to help speed up locating code if something does go wrong.

Error Handling
++++++++++++++++++++

* No error should pass silently; errors should be grouped into two categories; 'fatal' and 'recoverable', errors that are deemed to be 'fatal' must immediately lead to the termination of the currently running program, and a message displayed through the crash GUI if possible. Non-'fatal' errors should be appropriately handled in the relevant module, and if expected to pass silently until a fix is available, then must be logged or printed out to the terminal, so other programmers can fix the error later on to stop it potentially causing problems.

* All errors should be -where possible- stored in the variable ``message``.

Notices
====================
* This documentation will be updated after a release of Pycraft, but only the necessary parts will be changed, if something is out of date or there is a mistake, then please contact Tom at thomasjebbo@gmail.com or post the issue in the issues tab so we are made aware!
* All indentation will be represented by ``¬`` in the by breakdowns.
* From here onwards will be the documentation for every in Pycraft, this will be updated regularly. We begin by introducing an overview of what each module and class and subroutine does, then go into a by-analysis, this will be long and if your looking for something specific then we recommend that you use <control+f> to speed up the process!
* Any other notices will be places here!

Code found in every module
====================
This section goes over the code structures that are used in every module in Pycraft.

At the Start
+++++++++++++++++++
.. code-block:: python

    if not __name__ == "__main__":
        print("Started <Pycraft_<name>>")
        class <name>:
            def __init__(self):
                pass

This code appears at the top of every module in Pycraft (with the exception of ``main.py``) as this prevents the module from running unless called from in Pycraft, this is needed because each of the modules link together from the main module means that objects this module might rely on may be defined in other programs, which can cause errors, this is the start of the if-statement that prevents this.

1. ``if not __name__ == "__main__":`` This checks to see if the place its called from (stored in the variable ``__name__``) is not ``"__main__"``. The string ``"__main__"`` would be the data stored in the variable ``__name__`` if the project was run on its own, which in this case we don't want so we only allow the code inside the if-statement to run if the data in ``__name__`` is not ``"__main__"``.
2. ``¬ print("Started <Pycraft_<name>>")`` Now we output data to the terminal if the program is running, this allows us to know if there are any errors preventing this module from loading, in which case the program would crash before that is outputted to the terminal, making us aware the error is in this module.
3. ``¬ class <name>:`` Now we are defining a class with a suitable name that represents what the subroutines in this class do; this allows us to group up our code to make it easier to edit, organise and debug later on, as well as saving on memory as not every function will need to be loaded at once.
4. ``¬ ¬ def __init__(self):`` Here we make sure the module is initialized correctly we do this because if we tried to call this standalone, and without the code that would stop this, then all references to variables and subroutines outside of this project would be invalid and cause issues. This is also where the variable 'self' is defined for all references in this class. This subroutine is a procedure, so does not return a value.
5. ``¬ ¬ ¬ pass`` Now we only put code in the ``__init__`` procedure in some situations, like for example in ``GameEngine.py`` and ``main.py``, which is where the code that would go in this procedure is called, reducing the number of  the project uses.

At the End
++++++++++++++++++++
.. code-block:: python

    else:
        print("You need to run this as part of Pycraft")
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
        quit()

This code links to the if-statement made above at the start of the program, if the user calls this module on it's own, we can run this code to tell the user.

1. ``else:`` This links to the if-statement above, running the indented code below if the if-statement is false.
2. ``¬ print("You need to run this as part of Pycraft")`` if the user is running the code from PyPi, or as a raw ".py" file then this will be outputted to the terminal, however uses of the compiled ".exe" editions will not see this. This code is also printed first in-case the code below fails.
3. ``¬ import tkinter as tk`` Now we are importing the tkinter module into the project, all code here must be standalone and not rely on code in other modules in the project, this way the project can be taken apart and this should still work. We store he imported module, "Tkinter" with the name ``tk``, this shortens length and all references to "Tkinter" from how on in this indented block will use this name.
4. ``¬ from tkinter import messagebox`` Here we are importing specific sections of "Tkinter", in this case; ``messagebox``, this module allows us to make dialogue boxes that are commonplace in Windows and Apple based devices.
5. ``¬ root = tk.Tk()`` This of code is required to make the dialogue box, which is what we want. This will create a window to the default size "Tkinter" has defined, and initialises the ``messagebox`` module, which we want.
6. ``¬ root.withdraw()`` We use this code to hide the window that appears by using the previous  ``root`` is the internal name for the window, as that is what the window created in the previous was stored in (as a variable).
7. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")`` Here we make our all to the ``messagebox`` module, which has several pre-made dialogue boxes, we are using the ``showerror`` pre-made dialogue box procedure here. We give it the caption of ``"Startup Fail"``, and then elaborate on the issue in the main body of the window, by displaying the text ``"You need to run this as part of Pycraft, please run the 'main.py' file"``.
8. ``¬ quit()`` This is Python's way of closing the project, we normally use ``sys.exit`` for this, which you will see later on, because its  a bit cleaner on some IDLE's and terminals. However to reduce the length of this project, we use the built in function here instead.

Achievements
====================
Overview
++++++++++++++++++++
This module controls the displaying and processing of in-game achievements: This feature will be expanded upon when achievements are added and you can earn them in game.

The ``GenerateAchievements`` class controls the rendering of the achievements GUI this can be accessed from the 'home screen' of Pycraft, currently this class only renders a blank window, which is coloured and has a title [Pycraft] and header [Achievements], but expect an update here when its possible to earn achievements in game!

The ``Achievements(self)`` function, like most subroutines in Pycraft, takes ``self`` to be its only input. It will return only an error, should one arise, which will be stored in the ``messages`` variable. This subroutine is where the bulk of the processing for this class is done, this subroutine is responsible for the Achievements GUI which you can access through Pycraft's home screen.

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_Achievements>")``
   ``¬ class GenerateAchievements:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def Achievements(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol) ``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")``
``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) ``
``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``

``¬ ¬ ¬ ¬ AchievementsFont = InfoTitleFont.render("Achievements", self.aa, self.SecondFontCol)``
``¬ ¬ ¬ ¬ tempFPS = self.FPS``

``¬ ¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS ``
``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``

``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get(): ``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE): ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1 ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1 ``

``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))``

``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
``¬ ¬ ¬ ¬ ¬ if not Message == None:``
``¬ ¬ ¬ ¬ ¬ ¬ return Message``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip() ``
``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_Base>")``

``¬ import moderngl_window as mglw``
``¬ from moderngl_window.scene.camera import KeyboardCamera, OrbitCamera``


``¬ class CameraWindow(mglw.WindowConfig):``
``¬ ¬ """Base class with built in 3D camera support"""``

``¬ ¬ def __init__(self, **kwargs):``
``¬ ¬ ¬ super().__init__(**kwargs)``
``¬ ¬ ¬ self.camera = KeyboardCamera(self.wnd.keys, aspect_ratio=self.wnd.aspect_ratio)``
``¬ ¬ ¬ self.camera_enabled = True``

``¬ ¬ def key_event(self, key, action, modifiers):``
``¬ ¬ ¬ keys = self.wnd.keys``

``¬ ¬ ¬ if self.camera_enabled:``
``¬ ¬ ¬ ¬ self.camera.key_input(key, action, modifiers)``

``¬ ¬ ¬ if action == keys.ACTION_PRESS:``
``¬ ¬ ¬ ¬ if key == keys.C:``
``¬ ¬ ¬ ¬ ¬ self.camera_enabled = not self.camera_enabled``
``¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = self.camera_enabled``
``¬ ¬ ¬ ¬ ¬ self.wnd.cursor = not self.camera_enabled``
``¬ ¬ ¬ ¬ if key == keys.SPACE:``
``¬ ¬ ¬ ¬ ¬ self.timer.toggle_pause()``

``¬ ¬ def mouse_position_event(self, x: int, y: int, dx, dy):``
``¬ ¬ ¬ if self.camera_enabled:``
``¬ ¬ ¬ ¬ self.camera.rot_state(-dx, -dy)``

``¬ ¬ def resize(self, width: int, height: int):``
``¬ ¬ ¬ self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)``


``¬ class OrbitCameraWindow(mglw.WindowConfig):``
``¬ ¬ """Base class with built in 3D orbit camera support"""``

``¬ ¬ def __init__(self, **kwargs):``
``¬ ¬ ¬ super().__init__(**kwargs)``
``¬ ¬ ¬ self.camera = OrbitCamera(aspect_ratio=self.wnd.aspect_ratio)``
``¬ ¬ ¬ self.camera_enabled = True``

``¬ ¬ def key_event(self, key, action, modifiers):``
``¬ ¬ ¬ keys = self.wnd.keys``

``¬ ¬ ¬ if action == keys.ACTION_PRESS:``
``¬ ¬ ¬ ¬ if key == keys.C:``
``¬ ¬ ¬ ¬ ¬ self.camera_enabled = not self.camera_enabled``
``¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = self.camera_enabled``
``¬ ¬ ¬ ¬ ¬ self.wnd.cursor = not self.camera_enabled``
``¬ ¬ ¬ ¬ if key == keys.SPACE:``
``¬ ¬ ¬ ¬ ¬ self.timer.toggle_pause()``

``¬ ¬ def mouse_position_event(self, x: int, y: int, dx, dy):``
``¬ ¬ ¬ if self.camera_enabled:``
``¬ ¬ ¬ ¬ self.camera.rot_state(dx, dy)``

``¬ ¬ def mouse_scroll_event(self, x_offset: float, y_offset: float):``
``¬ ¬ ¬ if self.camera_enabled:``
``¬ ¬ ¬ ¬ self.camera.zoom_state(y_offset)``

``¬ ¬ def resize(self, width: int, height: int):``
``¬ ¬ ¬ self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_Benchmark>")``
   ``¬ class GenerateBenchmarkMenu:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def Benchmark(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).pause()``
``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol) ``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark")``
``¬ ¬ ¬ ¬ self.VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15) ``
``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) ``
``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
``¬ ¬ ¬ ¬ DetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``
``¬ ¬ ¬ ¬ InfoDetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``

``¬ ¬ ¬ ¬ BenchmarkFont = InfoTitleFont.render("Benchmark", self.aa, self.SecondFontCol)``
``¬ ¬ ¬ ¬ FPSinfoTEXT = DetailsFont.render("FPS benchmark results", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ FPSinfoTEXTWidth = FPSinfoTEXT.get_width()``
``¬ ¬ ¬ ¬ FILEinfoTEXT = DetailsFont.render("Read test results", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ FILEinfoTEXTWidth = FILEinfoTEXT.get_width()``
``¬ ¬ ¬ ¬ HARDWAREinfoTEXT = DetailsFont.render("Hardware results", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ HARDWAREinfoTEXTwidth = HARDWAREinfoTEXT.get_width()``

``¬ ¬ ¬ ¬ SixtyFPSData = DataFont.render("60 Hz", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ OneFourFourFPSData = DataFont.render("144 Hz", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ TwoFortyFPSData = DataFont.render("240 Hz", self.aa, self.AccentCol)``

``¬ ¬ ¬ ¬ InfoFont1 = DataFont.render("Welcome to Benchmark mode, press the SPACE bar to continue or press ANY other key to cancel, or press 'X'", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ InfoFont2 = DataFont.render("Benchmark mode is used to make the 'ADAPTIVE' feature in settings function and also to give an indication of the experience you are likely to get on this device", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ InfoFont3 = DataFont.render("Benchmark mode consists of several stages:", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ InfoFont4 = DataFont.render("First it will gather some basic information about your system", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ InfoFont5 = DataFont.render("Then it will test your maximum frame rate on a blank screen, then with a basic animation, and finally in a 3D OpenGL space", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ InfoFont6 = DataFont.render("After its done that the focus moves on to a quick storage test, before finishing", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ InfoFont7 = DataFont.render("Your results will then be displayed on screen with your frame rate scores on a line graph and the rest detailed to the right", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ InfoFont8 = DataFont.render("During the time the benchmark is running the window may appear unresponsive, don't panic this can be expected.", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ InfoFont9 = DataFont.render("In addition to achieve the best scores try to avoid doing anything else on the computer whilst the benchmark runs", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ InfoFont10 = DataFont.render("This benchmark may show some system instability or cause your device to get warm, you use this at your own risk!", self.aa, (255, 0, 0))``

``¬ ¬ ¬ ¬ stage = 0``

``¬ ¬ ¬ ¬ resize = False``

``¬ ¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

``¬ ¬ ¬ ¬ ¬ if stage == 0:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont1, (3, 100))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont2, (3, 130))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont3, (3, 145))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont4, (3, 160))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont5, (3, 175))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont6, (3, 190))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont7, (3, 220))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont8, (3, 235))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont9, (3, 250))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont10, (3, 280))``

``¬ ¬ ¬ ¬ ¬ if stage == 1:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Getting System Information")``
``¬ ¬ ¬ ¬ ¬ ¬ CPUid = f"{self.mod_CPUinfo__.get_cpu_info()['brand_raw']} w/{self.mod_Psutil__.cpu_count(logical=False)} cores @ {self.mod_Psutil__.cpu_freq().max} MHz"``
``¬ ¬ ¬ ¬ ¬ ¬ RAMid = f"{round((((self.mod_Psutil__.virtual_memory().total)/1000)/1000/1000),2)} GB of memory, with {self.mod_Psutil__.virtual_memory().percent}% used"``
``¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFO = DataFont.render(CPUid, self.aa, (255, 255, 255))``
``¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFOwidth = CPUhwINFO.get_width()``

``¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFO = DataFont.render(RAMid, self.aa, (255, 255, 255))``
``¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFOwidth = RAMhwINFO.get_width()``
``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``

``¬ ¬ ¬ ¬ ¬ if stage == 2:``
``¬ ¬ ¬ ¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3 = self.mod_ExBenchmark__.LoadBenchmark.run(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``
``¬ ¬ ¬ ¬ ¬ ¬ except:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Cancelled benchmark")``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Finished self.FPS based benchmarks")``
``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``

``¬ ¬ ¬ ¬ ¬ if stage == 3:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Starting disk read test")``
``¬ ¬ ¬ ¬ ¬ ¬ ReadIteration = 50``
``¬ ¬ ¬ ¬ ¬ ¬ for i in range(ReadIteration):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Benchdata = Bench.read()``

``¬ ¬ ¬ ¬ ¬ ¬ aTime = 0``
``¬ ¬ ¬ ¬ ¬ ¬ ReadIteration = 50``
``¬ ¬ ¬ ¬ ¬ ¬ for i in range(ReadIteration):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ start = self.mod_Time__.perf_counter()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Benchdata = Bench.read()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ aTime += self.mod_Time__.perf_counter()-start``
``¬ ¬ ¬ ¬ ¬ ¬ aTime = aTime/(ReadIteration+1)``
``¬ ¬ ¬ ¬ ¬ ¬ ReadSpeed = (1/(aTime))``
``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if stage == 4:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results.")``
``¬ ¬ ¬ ¬ ¬ ¬ Max1 = 0``
``¬ ¬ ¬ ¬ ¬ ¬ Min1 = 60``
``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY[i] > Max1:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max1 = FPSlistY[i]``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY[i] < Min1:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min1 = FPSlistY[i]``

``¬ ¬ ¬ ¬ ¬ ¬ Max2 = 0``
``¬ ¬ ¬ ¬ ¬ ¬ Min2 = 60``
``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY2[i] > Max2:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max2 = FPSlistY2[i]``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY2[i] < Min2:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min2 = FPSlistY2[i]``

``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results..")``
``¬ ¬ ¬ ¬ ¬ ¬ Max3 = 0``
``¬ ¬ ¬ ¬ ¬ ¬ Min3 = 60``
``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY3)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY3[i] > Max3:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max3 = FPSlistY3[i]``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY3[i] < Min3:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min3 = FPSlistY3[i]``

``¬ ¬ ¬ ¬ ¬ ¬ if Max2 > Max1:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max2``
``¬ ¬ ¬ ¬ ¬ ¬ elif Max3 > Max2:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max3``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max1``

``¬ ¬ ¬ ¬ ¬ ¬ self.RecommendedFPS = GlobalMax/2``

``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results...")``
``¬ ¬ ¬ ¬ ¬ ¬ multiplier = len(FPSlistY)/(realWidth-20)``
``¬ ¬ ¬ ¬ ¬ ¬ temp = []``
``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY[i])))``
``¬ ¬ ¬ ¬ ¬ ¬ FPSListY = temp``

``¬ ¬ ¬ ¬ ¬ ¬ temp = []``
``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY2[i])))``
``¬ ¬ ¬ ¬ ¬ ¬ FPSListY2 = temp``

``¬ ¬ ¬ ¬ ¬ ¬ temp = []``
``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY3[i])))``
``¬ ¬ ¬ ¬ ¬ ¬ FPSListY3 = temp``

``¬ ¬ ¬ ¬ ¬ ¬ Results1 = []``
``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results1.append([(FPSlistX[i]/multiplier), FPSListY[i]])``

``¬ ¬ ¬ ¬ ¬ ¬ Results2 = []``
``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results2.append([(FPSlistX2[i]/multiplier), FPSListY2[i]])``

``¬ ¬ ¬ ¬ ¬ ¬ Results3 = []``
``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY3)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results3.append([(FPSlistX3[i]/multiplier), FPSListY3[i]])``

``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``

``¬ ¬ ¬ ¬ ¬ if stage == 5:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Results")``

``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))``

``¬ ¬ ¬ ¬ ¬ ¬ FPSRect = self.mod_Pygame__.Rect(10, 130, realWidth-20, 300)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FPSRect, 0)``

``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*60)))), (realWidth-20, int(130+(300-((300/GlobalMax)*60)))))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SixtyFPSData, (13, int(130+(300-((300/GlobalMax)*60)))))``

``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*144)))), (realWidth-20, int(130+(300-((300/GlobalMax)*144)))))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(OneFourFourFPSData, (13, int(130+(300-((300/GlobalMax)*140)))))``

``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*240)))), (realWidth-20, int(130+(300-((300/GlobalMax)*240)))))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TwoFortyFPSData, (13, int(130+(300-((300/GlobalMax)*240)))))``

``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 255, 0), False, Results1)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 0, 255), False, Results2)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 0), False, Results3)``

``¬ ¬ ¬ ¬ ¬ ¬ HideRect = self.mod_Pygame__.Rect(0, 110, realWidth, 330)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.BackgroundCol, HideRect, 20)``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSinfoTEXT, ((realWidth-FPSinfoTEXTWidth)-3, 100))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FILEinfoTEXT, ((realWidth-FILEinfoTEXTWidth)-3, 430))``

``¬ ¬ ¬ ¬ ¬ ¬ FileResults = DataFont.render(f"Your device achieved a score of: {round(ReadSpeed, 2)}/100 ({round((100/100)*ReadSpeed)}%)", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ ¬ FileResultsWidth = FileResults.get_width()``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FileResults, ((realWidth-FileResultsWidth)-3, 460))``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(HARDWAREinfoTEXT, ((realWidth-HARDWAREinfoTEXTwidth)-3, 480))``

``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CPUhwINFO, ((realWidth-CPUhwINFOwidth)-3, 500))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(RAMhwINFO, ((realWidth-RAMhwINFOwidth)-3, 516))``

``¬ ¬ ¬ ¬ ¬ ¬ GreenInfo = InfoDetailsFont.render(f"Blank screen test (green); Minimum: {round(Min1, 4)} FPS, Maximum: {round(Max1, 4)} FPS", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ ¬ BlueInfo = InfoDetailsFont.render(f"Drawing test (blue); Minimum: {round(Min2, 4)} FPS, Maximum: {round(Max2, 4)} FPS", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ ¬ RedInfo = InfoDetailsFont.render(f"OpenGL test (red); Minimum: {round(Min3, 4)} FPS, Maximum: {round(Max3, 4)} FPS", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(GreenInfo, (3, 430))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BlueInfo, (3, 445))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(RedInfo, (3, 460))``

``¬ ¬ ¬ ¬ ¬ ¬ if resize == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ stage = 4``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ resize = False``

``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE) and stage <= 3) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE): ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ ¬ ¬ ¬ if (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_SPACE) and stage == 0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ stage += 1``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.VIDEORESIZE:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ resize = True``

``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_CaptionUtils>")``
   ``¬ class GenerateCaptions:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def GetLoadingCaption(self, num):``
``¬ ¬ ¬ if num == 0:``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (-)")``
``¬ ¬ ¬ elif num == 1:``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (\)")``
``¬ ¬ ¬ elif num == 2:``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (|)")``
``¬ ¬ ¬ elif num == 3:``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (/)")``
``¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading")``
``¬ ¬ ¬ self.mod_Pygame__.display.update()``

``¬ ¬ def GetNormalCaption(self, location):``
``¬ ¬ ¬ if self.Devmode >= 5 and self.Devmode <= 9:``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | you are: {10-self.Devmode} steps away from being a developer") ``
``¬ ¬ ¬ elif self.Devmode == 10: ``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | Developer Mode | Pos: {round(self.X, 2)}, {round(self.Y, 2)}, {round(self.Z, 2)} | V: {self.Total_move_x}, {self.Total_move_y}, {self.Total_move_z} FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: {int(self.aFPS/self.Iteration)} Iteration: {self.Iteration} | MemUsE: {self.mod_Psutil__.virtual_memory().percent} | CPUUsE: {self.mod_Psutil__.cpu_percent()} | Theme: {self.theme} | Thread Count: {self.mod_Threading__.active_count()}") ``
``¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location}")``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_CharacterDesigner>")``
   ``¬ class GenerateCharacterDesigner:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def CharacterDesigner(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol) ``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")``
``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) ``
``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.SecondFontCol)``
``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``

``¬ ¬ ¬ ¬ AchievementsFont = InfoTitleFont.render("Character Designer", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ tempFPS = self.FPS``

``¬ ¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS ``
``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``

``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get(): ``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE): ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1 ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1 ``

``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))``

``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
``¬ ¬ ¬ ¬ ¬ if not Message == None:``
``¬ ¬ ¬ ¬ ¬ ¬ return Message``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip() ``
``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_Credits>")``
   ``¬ class GenerateCredits:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def Credits(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip() ``
``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits")``
``¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
``¬ ¬ ¬ ¬ LargeCreditsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``
``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) ``
``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``
``¬ ¬ ¬ ¬ TitleHeight = TitleFont.get_height()``
``¬ ¬ ¬ ¬ CreditsFont = InfoTitleFont.render("Credits", self.aa, self.SecondFontCol) ``
``¬ ¬ ¬ ¬ Credits1 = LargeCreditsFont.render(f"Pycraft: v{self.version}", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits1Width = Credits1.get_width()``
``¬ ¬ ¬ ¬ Credits2 = LargeCreditsFont.render("Game Director: Tom Jebbo", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits2Width = Credits2.get_width()``
``¬ ¬ ¬ ¬ Credits3 = LargeCreditsFont.render("Art and Music Lead: Tom Jebbo", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits3Width = Credits3.get_width()``
``¬ ¬ ¬ ¬ Credits4 = LargeCreditsFont.render("Other Music Credits:", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits4Width = Credits4.get_width()``
``¬ ¬ ¬ ¬ Credits5 = LargeCreditsFont.render("Freesound: - Erokia's 'ambient wave compilation' @ freesound.org/s/473545", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits5Width = Credits5.get_width()``
``¬ ¬ ¬ ¬ Credits6 = LargeCreditsFont.render("Freesound: - Soundholder's 'ambient meadow near forest' @ freesound.org/s/425368", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits6Width = Credits6.get_width()``
``¬ ¬ ¬ ¬ Credits7 = LargeCreditsFont.render("Freesound: - monte32's 'Footsteps_6_Dirt_shoe' @ freesound.org/people/monte32/sounds/353799", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits7Width = Credits7.get_width()``
``¬ ¬ ¬ ¬ Credits8 = LargeCreditsFont.render("With thanks to the developers of:", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits8Width = Credits8.get_width()``
``¬ ¬ ¬ ¬ Credits9 = LargeCreditsFont.render("PSutil", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits9Width = Credits9.get_width()``
``¬ ¬ ¬ ¬ Credits10 = LargeCreditsFont.render("Python", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits10Width = Credits10.get_width()``
``¬ ¬ ¬ ¬ Credits11 = LargeCreditsFont.render("Pygame", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits11Width = Credits11.get_width()``
``¬ ¬ ¬ ¬ Credits12 = LargeCreditsFont.render("Numpy", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits12Width = Credits12.get_width()``
``¬ ¬ ¬ ¬ Credits13 = LargeCreditsFont.render("Nuitka", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits13Width = Credits13.get_width()``
``¬ ¬ ¬ ¬ Credits14 = LargeCreditsFont.render("CPUinfo", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits14Width = Credits14.get_width()``
``¬ ¬ ¬ ¬ Credits15 = LargeCreditsFont.render("PyInstaller", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits15Width = Credits15.get_width()``
``¬ ¬ ¬ ¬ Credits16 = LargeCreditsFont.render("PyAutoGUI", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits16Width = Credits16.get_width()``
``¬ ¬ ¬ ¬ Credits17 = LargeCreditsFont.render("PyWaveFront", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits17Width = Credits17.get_width()``
``¬ ¬ ¬ ¬ Credits18 = LargeCreditsFont.render("Microsoft's Visual Studio Code", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits18Width = Credits18.get_width()``
``¬ ¬ ¬ ¬ Credits19 = LargeCreditsFont.render("PIL (Pillow/Python Imaging Library)", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits19Width = Credits19.get_width()``
``¬ ¬ ¬ ¬ Credits20 = LargeCreditsFont.render("PyOpenGL (and PyOpenGL-accelerate)", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits20Width = Credits20.get_width()``
``¬ ¬ ¬ ¬ Credits21 = LargeCreditsFont.render("For more in depth accreditation please check the GitHub Page @ github.com/PycraftDeveloper/Pycraft", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits21Width = Credits21.get_width()``
``¬ ¬ ¬ ¬ Credits22 = LargeCreditsFont.render("With thanks to:", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits22Width = Credits22.get_width()``
``¬ ¬ ¬ ¬ Credits23 = LargeCreditsFont.render("All my wonderful followers on Twitter, and you for installing this game, that's massively appreciated!", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits23Width = Credits23.get_width()``
``¬ ¬ ¬ ¬ Credits24 = LargeCreditsFont.render("For full change-log please visit my aforementioned GitHub profile", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits24Width = Credits24.get_width()``
``¬ ¬ ¬ ¬ Credits25 = LargeCreditsFont.render("Disclaimer:", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits25Width = Credits25.get_width()``
``¬ ¬ ¬ ¬ Credits26 = VersionFont.render("The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ Credits26Width = Credits26.get_width()``
``¬ ¬ ¬ ¬ Credits27 = VersionFont.render("friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ Credits27Width = Credits27.get_width()``
``¬ ¬ ¬ ¬ Credits28 = VersionFont.render("my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ Credits28Width = Credits28.get_width()``
``¬ ¬ ¬ ¬ Credits29 = VersionFont.render("DOES NOT TAKE ANY RESPONSIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXTERNAL MODULES INSTALLED ONTO", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ Credits29Width = Credits29.get_width()``
``¬ ¬ ¬ ¬ Credits30 = VersionFont.render("YOUR COMPUTER (WHEN NOT CHOOSING THE RECOMMENDED EXECUTABLE VERSION) ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ Credits30Width = Credits30.get_width()``
``¬ ¬ ¬ ¬ Credits31 = VersionFont.render("RESPONSIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVICES MANAGER OR ADMINISTRATOR TO INSTALL AND USE", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ Credits31Width = Credits31.get_width()``
``¬ ¬ ¬ ¬ Credits32 = VersionFont.render("COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVICE, AND AT ANY POINT NO CONNECTION TO A", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ Credits32Width = Credits32.get_width()``
``¬ ¬ ¬ ¬ Credits33 = VersionFont.render("NETWORK IS REQUIRED. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you.", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ Credits33Width = Credits33.get_width()``
``¬ ¬ ¬ ¬ Credits34 = VersionFont.render("Thank You!", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ Credits34Width = Credits34.get_width()``
``¬ ¬ ¬ ¬ Credits34Height = Credits34.get_height()``

``¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
``¬ ¬ ¬ ¬ VisualYdisplacement = realHeight``
``¬ ¬ ¬ ¬ IntroYDisplacement = (realHeight-TitleHeight)/2``
``¬ ¬ ¬ ¬ timer = 5``
``¬ ¬ ¬ ¬ tempFPS = self.FPS``

``¬ ¬ ¬ ¬ EndClock = 0``
``¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
``¬ ¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS ``
``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``

``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get(): ``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE): ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1 ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1 ``

``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits and Change-Log")``
``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits1, ((realWidth-Credits1Width)/2, 0+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits2, ((realWidth-Credits2Width)/2, 115+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits3, ((realWidth-Credits3Width)/2, (115*2)+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits4, ((realWidth-Credits4Width)/2, (115*3)+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits5, ((realWidth-Credits5Width)/2, (115*3)+20+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits6, ((realWidth-Credits6Width)/2, (115*3)+40+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits7, ((realWidth-Credits7Width)/2, (115*3)+60+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits8, ((realWidth-Credits8Width)/2, 540+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits9, ((realWidth-Credits9Width)/2, 540+20+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits10, ((realWidth-Credits10Width)/2, 540+40+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits11, ((realWidth-Credits11Width)/2, 540+60+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits12, ((realWidth-Credits12Width)/2, 540+80+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits13, ((realWidth-Credits13Width)/2, 540+100+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits14, ((realWidth-Credits14Width)/2, 540+120+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits15, ((realWidth-Credits15Width)/2, 540+140+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits16, ((realWidth-Credits16Width)/2, 540+160+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits17, ((realWidth-Credits17Width)/2, 540+180+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits18, ((realWidth-Credits18Width)/2, 540+200+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits19, ((realWidth-Credits19Width)/2, 540+220+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits20, ((realWidth-Credits20Width)/2, 540+240+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits21, ((realWidth-Credits21Width)/2, 540+260+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits22, ((realWidth-Credits22Width)/2, 915+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits23, ((realWidth-Credits23Width)/2, 935+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits24, ((realWidth-Credits24Width)/2, 1050+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits25, ((realWidth-Credits25Width)/2, 1165+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits26, ((realWidth-Credits26Width)/2, 1167+15+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits27, ((realWidth-Credits27Width)/2, 1167+30+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits28, ((realWidth-Credits28Width)/2, 1167+45+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits29, ((realWidth-Credits29Width)/2, 1167+60+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits30, ((realWidth-Credits30Width)/2, 1167+75+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits31, ((realWidth-Credits31Width)/2, 1167+90+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits32, ((realWidth-Credits32Width)/2, 1167+105+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits33, ((realWidth-Credits33Width)/2, 1167+120+VisualYdisplacement))``

``¬ ¬ ¬ ¬ ¬ if timer >= 1:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))``
``¬ ¬ ¬ ¬ ¬ ¬ timer -= 1/(self.aFPS/self.Iteration)``
``¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement = realHeight``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ if IntroYDisplacement <= 0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, FullscreenX, 90)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if int(1402+VisualYdisplacement) <= int(realHeight/2):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, (realHeight-Credits34Height)/2))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement -= 60/(self.aFPS/self.Iteration)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if EndClock >= 5:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ EndClock += 1/(self.aFPS/self.Iteration)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, 1402+VisualYdisplacement))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement -= 60/(self.aFPS/self.Iteration)``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50+IntroYDisplacement))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ IntroYDisplacement -= 90/(self.aFPS/self.Iteration)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement = realHeight``

``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
``¬ ¬ ¬ ¬ ¬ if not Message == None:``
``¬ ¬ ¬ ¬ ¬ ¬ return Message``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip() ``
``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_DisplayUtils>")``
   ``¬ class DisplayUtils:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def UpdateDisplay(self): # Run tests to make sure windows not too small``
``¬ ¬ ¬ self.Data_aFPS = []``
``¬ ¬ ¬ self.Data_CPUUsE = []``
``¬ ¬ ¬ self.Data_eFPS = []``
``¬ ¬ ¬ self.Data_MemUsE = []``
``¬ ¬ ¬ self.Timer = 0``
``¬ ¬ ¬ self.Data_aFPS_Min = 60``
``¬ ¬ ¬ self.Data_aFPS_Max = 1``

``¬ ¬ ¬ self.Data_CPUUsE_Min = 60``
``¬ ¬ ¬ self.Data_CPUUsE_Max = 1``

``¬ ¬ ¬ self.Data_eFPS_Min = 60``
``¬ ¬ ¬ self.Data_eFPS_Max = 1``

``¬ ¬ ¬ self.Data_MemUsE_Min = 50``
``¬ ¬ ¬ self.Data_MemUsE_Max = 50``

``¬ ¬ ¬ self.Data_CPUUsE_Min = 50``
``¬ ¬ ¬ self.Data_CPUUsE_Max = 50``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = True``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.RESIZABLE)``
``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = False``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF)``
``¬ ¬ ¬ ¬ except Exception as error:``
``¬ ¬ ¬ ¬ ¬ self.Fullscreen = True``
``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight))``
``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ return Message``
``¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ return None``


``¬ ¬ def SetOPENGLdisplay(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == True:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == False:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
``¬ ¬ ¬ ¬ except Exception as error:``
``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ return Message``
``¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ return None``
``¬ ¬ ``
``¬ ¬ ``
``¬ ¬ def UpdateOPENGLdisplay(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = True``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = False``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
``¬ ¬ ¬ ¬ except:``
``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ ¬ self.Fullscreen = False``
``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ return Message``
``¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ return None``


``¬ ¬ def SetDisplay(self):``
``¬ ¬ ¬ self.Data_aFPS = []``
``¬ ¬ ¬ self.Data_CPUUsE = []``
``¬ ¬ ¬ self.Data_eFPS = []``
``¬ ¬ ¬ self.Data_MemUsE = []``
``¬ ¬ ¬ self.Timer = 0``
``¬ ¬ ¬ self.Data_aFPS_Min = 60``
``¬ ¬ ¬ self.Data_aFPS_Max = 1``

``¬ ¬ ¬ self.Data_CPUUsE_Min = 60``
``¬ ¬ ¬ self.Data_CPUUsE_Max = 1``

``¬ ¬ ¬ self.Data_eFPS_Min = 60``
``¬ ¬ ¬ self.Data_eFPS_Max = 1``

``¬ ¬ ¬ self.Data_MemUsE_Min = 50``
``¬ ¬ ¬ self.Data_MemUsE_Max = 50``

``¬ ¬ ¬ self.Data_CPUUsE_Min = 50``
``¬ ¬ ¬ self.Data_CPUUsE_Max = 50``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == True:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.RESIZABLE)``
``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == False:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF)``
``¬ ¬ ¬ ¬ except Exception as error:``
``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight))``
``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ return Message``
``¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ return None``


``¬ ¬ def GenerateMinDisplay(self, width, height):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((width, height), self.mod_Pygame__.RESIZABLE)``
``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ return Message``
``¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ return None``


``¬ ¬ def GetDisplayLocation(self):``
``¬ ¬ ¬ hwnd = self.mod_Pygame__.display.get_wm_info()["window"]``

``¬ ¬ ¬ prototype = self.mod_Ctypes__.WINFUNCTYPE(self.mod_Ctypes__.wintypes.BOOL, self.mod_Ctypes__.wintypes.HWND, self.mod_Ctypes__.POINTER(self.mod_Ctypes__.wintypes.RECT))``
``¬ ¬ ¬ paramflags = (1, "hwnd"), (2, "lprect")``

``¬ ¬ ¬ GetWindowRect = prototype(("GetWindowRect", self.mod_Ctypes__.windll.user32), paramflags)``

``¬ ¬ ¬ rect = GetWindowRect(hwnd)``

``¬ ¬ ¬ return rect.left+8, rect.top+31``


``¬ ¬ def GetPlayStatus(self):``
``¬ ¬ ¬ if self.mod_Pygame__.display.get_active() == True:``
``¬ ¬ ¬ ¬ tempFPS = self.FPS``
``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).unpause()``
``¬ ¬ ¬ ¬ if self.mod_Pygame__.mixer.Channel(2).get_busy() == 0 and self.LoadMusic == True:``
``¬ ¬ ¬ ¬ ¬ if self.music == True and self.CurrentlyPlaying == None:``
``¬ ¬ ¬ ¬ ¬ ¬ self.CurrentlyPlaying = "InvSound"``
``¬ ¬ ¬ ¬ ¬ ¬ self.LoadMusic = False``
``¬ ¬ ¬ ¬ ¬ ¬ MusicThread = self.mod_Threading__.Thread(target=self.mod_SoundUtils__.PlaySound.PlayInvSound, args=(self,))``
``¬ ¬ ¬ ¬ ¬ ¬ MusicThread.start()``
``¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ self.LoadMusic = True``
``¬ ¬ ¬ ¬ tempFPS = 15``
``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).pause()``
``¬ ¬ ¬ return tempFPS``
``¬ ¬ ``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_DrawingUtils>")``
   ``¬ class DrawRose:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def CreateRose(self, xScaleFact, yScaleFact, coloursARRAY):``
``¬ ¬ ¬ if coloursARRAY == False:``
``¬ ¬ ¬ ¬ coloursARRAY = []``
``¬ ¬ ¬ ¬ for i in range(32):``
``¬ ¬ ¬ ¬ ¬ coloursARRAY.append(self.ShapeCol)``

``¬ ¬ ¬ defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] ``
``¬ ¬ ¬ self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2)``
``¬ ¬ ¬ ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[0], (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[1], (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[2], (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[3], (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[4], (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[5], (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[6], (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[7], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[8], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[9], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[10], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[11], (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[12], (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[13], (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[14], (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[15], (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[16], (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[17], (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[18], (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[19], (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[20], (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[21], (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[22], (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[23], (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[24], (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[25], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[25], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[27], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[28], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[29], (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[30], (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[31], (575*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

``¬ class GenerateGraph:``
``¬ ¬ def __init__(self):``
``¬ ¬ ¬ pass``

``¬ ¬ def CreateDevmodeGraph(self, DataFont):``
``¬ ¬ ¬ if self.Devmode == 10:``
``¬ ¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ ¬ if ((self.realWidth/2)+100)+self.Timer >= self.realWidth:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS = []``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE = []``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS = []``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE = []``
``¬ ¬ ¬ ¬ ¬ ¬ self.Timer = 0``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Min = 60``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Max = 1``

``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = 60``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = 1``

``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Min = 60``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Max = 1``

``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Min = 50``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = 50``

``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = 50``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = 50``

``¬ ¬ ¬ ¬ ¬ BackingRect = self.mod_Pygame__.Rect((self.realWidth/2)+100, 0, self.realWidth, 200)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, BackingRect)``

``¬ ¬ ¬ ¬ ¬ if self.Timer >= 2:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_aFPS_Max)*(self.aFPS/(self.Iteration))])``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_eFPS_Max)*int(self.eFPS)])``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_MemUsE_Max)*(100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available])``

``¬ ¬ ¬ ¬ ¬ if (self.aFPS/(self.Iteration)) > self.Data_aFPS_Max:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Max = (self.aFPS/(self.Iteration))``
``¬ ¬ ¬ ¬ ¬ elif (self.aFPS/(self.Iteration)) < self.Data_aFPS_Min:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Min = (self.aFPS/(self.Iteration))``

``¬ ¬ ¬ ¬ ¬ if self.eFPS > self.Data_eFPS_Max:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Max = self.eFPS``
``¬ ¬ ¬ ¬ ¬ elif self.eFPS < self.Data_eFPS_Min:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Min = self.eFPS``

``¬ ¬ ¬ ¬ ¬ if (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available > self.Data_MemUsE_Max:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available``
``¬ ¬ ¬ ¬ ¬ elif (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available < self.Data_MemUsE_Max:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available``

``¬ ¬ ¬ ¬ ¬ self.Timer += 0.2``
``¬ ¬ ¬ ¬ ¬ if self.Timer >= 5:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 0), False, self.Data_aFPS)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 255, 0), False, self.Data_eFPS)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 0, 255), False, self.Data_MemUsE)``
``¬ ¬ ¬ ¬ ¬ if len(self.Data_CPUUsE) >= 2:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 255), False, self.Data_CPUUsE)``
``¬ ¬ ¬ ¬ ¬ runFont = DataFont.render(f"MemUsE: {self.mod_Psutil__.virtual_memory().percent}% | CPUUsE: {self.mod_Psutil__.cpu_percent()}% | FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: {int(self.aFPS/self.Iteration)} Iteration: {self.Iteration}", self.aa, (255, 255, 255)) ``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(runFont, ((self.realWidth/2)+105, 0))``
``¬ ¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
``¬ ¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_ExBenchmark>")``
   ``¬ class LoadBenchmark:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def run(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ FPSlistX = []``
``¬ ¬ ¬ ¬ FPSlistY = []``

``¬ ¬ ¬ ¬ FPSlistX2 = []``
``¬ ¬ ¬ ¬ FPSlistY2 = []``

``¬ ¬ ¬ ¬ FPSlistX3 = []``
``¬ ¬ ¬ ¬ FPSlistY3 = []``

``¬ ¬ ¬ ¬ SetFPS = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 200, 250, 300, 350, 500]``

``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((1280, 720))``

``¬ ¬ ¬ ¬ iteration = 0``
``¬ ¬ ¬ ¬ FPScounter = 0``
``¬ ¬ ¬ ¬ MaxIteration = 500``

``¬ ¬ ¬ ¬ while iteration < 7500:``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running Blank Window Benchmark @ {SetFPS[FPScounter]} FPS")``
``¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:``
``¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX.append(iteration)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY.append(self.clock.get_fps())``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``

``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``
``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])``
``¬ ¬ ¬ ¬ ¬ FPScounter += 1``
``¬ ¬ ¬ ¬ ¬ MaxIteration += 500``

``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Preparing Animated Benchmark")``

``¬ ¬ ¬ ¬ iteration = 0``
``¬ ¬ ¬ ¬ FPScounter = 0``
``¬ ¬ ¬ ¬ MaxIteration = 500``
``¬ ¬ ¬ ¬ run = 0``
``¬ ¬ ¬ ¬ y = 10``

``¬ ¬ ¬ ¬ while not iteration == 60:``
``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``

``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ iteration += 1``
``¬ ¬ ¬ ¬ ¬ self.clock.tick(60)``

``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ iteration = 0``
``¬ ¬ ¬ ¬ FPScounter = 0``
``¬ ¬ ¬ ¬ MaxIteration = 500``

``¬ ¬ ¬ ¬ while iteration < 7500:``
``¬ ¬ ¬ ¬ ¬ run += 1``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running Animated Window Benchmark @ {SetFPS[FPScounter]} FPS")``
``¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:``
``¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX2.append(iteration)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY2.append(self.clock.get_fps())``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``

``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``
``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])``
``¬ ¬ ¬ ¬ ¬ FPScounter += 1``
``¬ ¬ ¬ ¬ ¬ MaxIteration += 500``

``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Preparing OpenGL Benchmark")``

``¬ ¬ ¬ ¬ iteration = 0``
``¬ ¬ ¬ ¬ FPScounter = 0``
``¬ ¬ ¬ ¬ MaxIteration = 500``
``¬ ¬ ¬ ¬ run = 0``
``¬ ¬ ¬ ¬ y = 10``

``¬ ¬ ¬ ¬ while not iteration == 60:``
``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``

``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ iteration += 1``
``¬ ¬ ¬ ¬ ¬ self.clock.tick(60)``

``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((1280, 720), self.mod_Pygame__.OPENGL|self.mod_Pygame__.DOUBLEBUF)``

``¬ ¬ ¬ ¬ iteration = 0``
``¬ ¬ ¬ ¬ FPScounter = 0``
``¬ ¬ ¬ ¬ MaxIteration = 500``
``¬ ¬ ¬ ¬ vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))``
``¬ ¬ ¬ ¬ edges = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4), (6,7), (5,1), (5,4), (5,7))``

``¬ ¬ ¬ ¬ self.mod_OGLbenchmark__.LoadOGLBenchmark.CreateBenchmark(self)``

``¬ ¬ ¬ ¬ while iteration < 7500:``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running OpenGL Benchmark @ {SetFPS[FPScounter]} FPS")``
``¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:``
``¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX3.append(iteration)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY3.append(self.clock.get_fps())``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_OGLbenchmark__.LoadOGLBenchmark.RunBenchmark(self, edges, vertices)``
``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``

``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``
``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])``
``¬ ¬ ¬ ¬ ¬ FPScounter += 1``
``¬ ¬ ¬ ¬ ¬ MaxIteration += 500``

``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Finished Animated Benchmark")``
``¬ ¬ ¬ ¬ self.mod_Time__.sleep(5)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
``¬ ¬ ¬ ¬ return Message, None, None, None, None``
``¬ ¬ ¬ else:``

``¬ ¬ ¬ ¬ return None, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


``if not __name__ == "__main__":``
``¬ print("Started <Pycraft_GameEngine>")``
``¬ ``
``¬ from ShareDataUtil import Class_Startup_variables as SharedData``
``¬ ``
``¬ SharedData.mod_ModernGL_window_.setup_basic_logging(0)``
``¬ ``
``¬ ``
``¬ class Cubemap(SharedData.mod_Base__.CameraWindow):``
``¬ ¬ SharedData.mod_Base__.CameraWindow.title = f"Pycraft: v{SharedData.version}: Playing"``
``¬ ¬ SharedData.mod_Base__.CameraWindow.resource_dir = SharedData.base_folder``
``¬ ¬ ``
``¬ ¬ ``
``¬ ¬ def Exit(self, SharedData, Command):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ if SharedData.mod_Pygame__.mixer.Channel(3).get_busy() == True:``
``¬ ¬ ¬ ¬ ¬ SharedData.mod_Pygame__.mixer.Channel(3).stop()``
``¬ ¬ ¬ ¬ ¬ SharedData.mod_Pygame__.quit()``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = False``
``¬ ¬ ¬ except Exception as Error:``
``¬ ¬ ¬ ¬ print("GE", Error)``
``¬ ¬ ¬ ¬ pass``
``¬ ¬ ¬ self.wnd._set_fullscreen(False)``
``¬ ¬ ¬ self.wnd.close()``
``¬ ¬ ¬ self.wnd.destroy()``
``¬ ¬ ¬ SharedData.CurrentlyPlaying = None``
``¬ ¬ ¬ SharedData.LoadMusic = True``
``¬ ¬ ¬ SharedData.Command = Command``
``¬ ¬ ¬ if self.wnd.fullscreen == True:``
``¬ ¬ ¬ ¬ SharedData.Fullscreen = False``
``¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ SharedData.Fullscreen = True``


``¬ ¬ def __init__(self, **kwargs):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ super().__init__(**kwargs)``
``¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ self.size = self.wnd.buffer_size``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ WindowSize = SharedData.realWidth, SharedData.realHeight``
``¬ ¬ ¬ ¬ CurrentWindowSize = WindowSize``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ self.wnd.size = WindowSize``
``¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ self.camera.projection.update(near=0.1, far=100.0)``
``¬ ¬ ¬ ¬ self.camera.zoom = 2.5``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ self.obj = self.load_scene(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\Map\\map.obj")))``
``¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ self.cube = SharedData.mod_ModernGL_window_.geometry.cube(size=(20, 20, 20))``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ self.prog = self.load_program(SharedData.mod_OS__.path.join(SharedData.base_folder, ("programs//cubemap.glsl")))``

``¬ ¬ ¬ ¬ self.SkyBox_texture = self.load_texture_cube(``
``¬ ¬ ¬ ¬ ¬ neg_x=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg")),``
``¬ ¬ ¬ ¬ ¬ neg_y=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg")),``
``¬ ¬ ¬ ¬ ¬ neg_z=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg")),``
``¬ ¬ ¬ ¬ ¬ pos_x=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg")),``
``¬ ¬ ¬ ¬ ¬ pos_y=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg")),``
``¬ ¬ ¬ ¬ ¬ pos_z=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg")),``
``¬ ¬ ¬ ¬ ¬ flip_x=True,``
``¬ ¬ ¬ ¬ )``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ Prev_Mouse_Pos = (0,0)``
``¬ ¬ ¬ ¬ Mouse_Pos = (0,0)``
``¬ ¬ ¬ ¬ DeltaX, DeltaY = 0, 0``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ self.wnd.exit_key = None``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ MouseUnlock = True``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ Jump = False``
``¬ ¬ ¬ ¬ JumpID = 0``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ self.camera.position.y += 0.7``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ WkeydownTimer = 0``
``¬ ¬ ¬ ¬ AkeydownTimer = 0``
``¬ ¬ ¬ ¬ SkeydownTimer = 0``
``¬ ¬ ¬ ¬ DkeydownTimer = 0``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ RunForwardTimer = 0``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ FPS = 0``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ Iteration = 0``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.mod_Pygame__.mixer.get_busy() == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayAmbientSound(SharedData)``
``¬ ¬ ¬ ¬ ¬ except Exception as Error:``
``¬ ¬ ¬ ¬ ¬ ¬ print(Error)``
``¬ ¬ ¬ ¬ ¬ ¬ pass``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if Iteration == 0:``
``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.Fullscreen == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.fullscreen = True``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.fixed_aspect_ratio = SharedData.realWidth / SharedData.realHeight``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.window_size = SharedData.realWidth, SharedData.realHeight``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ CurrentWindowSize = self.window_size``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.position = (int((SharedData.FullscreenX-CurrentWindowSize[0])/2), int((SharedData.FullscreenY-CurrentWindowSize[1])/2))``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if Iteration >= 5000:``
``¬ ¬ ¬ ¬ ¬ ¬ Iteration = 0``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ start = SharedData.mod_Time__.perf_counter()``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.ctx.clear(1.0, 1.0, 1.0)``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ CurrentWindowSize = self.window_size``

``¬ ¬ ¬ ¬ ¬ Prev_Mouse_Pos = Mouse_Pos ``
``¬ ¬ ¬ ¬ ¬ Mouse_Pos = SharedData.mod_Pyautogui__.position()``
``¬ ¬ ¬ ¬ ¬ DeltaX, DeltaY = Mouse_Pos[0]-Prev_Mouse_Pos[0], Mouse_Pos[1]-Prev_Mouse_Pos[1]``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.ESCAPE):``
``¬ ¬ ¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "Undefined")``
``¬ ¬ ¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.W):``
``¬ ¬ ¬ ¬ ¬ ¬ RunForwardTimer += (1/FPS)``
``¬ ¬ ¬ ¬ ¬ ¬ if RunForwardTimer <= 10:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer += (1/FPS)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if WkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer = 0``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.x += 1.42``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer += (1/FPS)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if WkeydownTimer >= (SharedData.mod_Random__.randint(25, 75)/100):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer = 0``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.x += 2.2352``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ RunForwardTimer = 0``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.A):``
``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ AkeydownTimer += (1/FPS)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if AkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AkeydownTimer = 0``
``¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.z += 1.42``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.S):``
``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ SkeydownTimer += (1/FPS)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if SkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SkeydownTimer = 0``
``¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.x -= 1.42``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.D):``
``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ DkeydownTimer += (1/FPS)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if DkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ DkeydownTimer = 0``
``¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.z -= 1.42``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.E):``
``¬ ¬ ¬ ¬ ¬ ¬ if self.wnd._fullscreen == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot = SharedData.mod_Pyautogui__.screenshot(region=((0, 0, SharedData.FullscreenX, SharedData.FullscreenY)))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot.save(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ PosX, PosY = self.wnd.position``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot = SharedData.mod_Pyautogui__.screenshot(region=((PosX, PosY, SharedData.realWidth, SharedData.realHeight)))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot.save(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "Inventory")``
``¬ ¬ ¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.R):``
``¬ ¬ ¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "MapGUI")``
``¬ ¬ ¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.L):``
``¬ ¬ ¬ ¬ ¬ ¬ if MouseUnlock == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ MouseUnlock = False``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ MouseUnlock = True``
``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.SPACE):``
``¬ ¬ ¬ ¬ ¬ ¬ Jump = True``
``¬ ¬ ¬ ¬ ¬ ¬ JumpUP = True``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if Jump == True:``
``¬ ¬ ¬ ¬ ¬ ¬ if JumpID < 10 and JumpUP == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpID += 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.y += 0.1``
``¬ ¬ ¬ ¬ ¬ ¬ if JumpID == 10:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpUP = False``
``¬ ¬ ¬ ¬ ¬ ¬ if JumpID >= 0 and JumpUP == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpID -= 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.y -= 0.1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if JumpID == 0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Jump = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpID = 0``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.ctx.enable(SharedData.mod_ModernGL__.CULL_FACE | SharedData.mod_ModernGL__.DEPTH_TEST)``

``¬ ¬ ¬ ¬ ¬ cam = self.camera.matrix``
``¬ ¬ ¬ ¬ ¬ cam[3][0] = 0``
``¬ ¬ ¬ ¬ ¬ cam[3][1] = 0``
``¬ ¬ ¬ ¬ ¬ cam[3][2] = 0``

``¬ ¬ ¬ ¬ ¬ self.SkyBox_texture.use(location=0)``
``¬ ¬ ¬ ¬ ¬ self.prog['m_proj'].write(self.camera.projection.matrix)``
``¬ ¬ ¬ ¬ ¬ self.prog['m_camera'].write(cam)``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ ¬ ¬ if MouseUnlock == True:¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.rot_state(-DeltaX, -DeltaY)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = True``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = False``
``¬ ¬ ¬ ¬ ¬ except Exception as Error:``
``¬ ¬ ¬ ¬ ¬ ¬ print(Error)``
``¬ ¬ ¬ ¬ ¬ ¬ pass``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.ctx.front_face = 'cw'``
``¬ ¬ ¬ ¬ ¬ self.cube.render(self.prog)``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.ctx.front_face = 'ccw'``
``¬ ¬ ¬ ¬ ¬ self.obj.draw(projection_matrix=self.camera.projection.matrix, camera_matrix=self.camera.matrix)``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ ¬ ¬ self.wnd.swap_buffers()``
``¬ ¬ ¬ ¬ ¬ except Exception as Error:``
``¬ ¬ ¬ ¬ ¬ ¬ print(Error)``
``¬ ¬ ¬ ¬ ¬ ¬ pass``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ FPS = 1/(SharedData.mod_Time__.perf_counter()-start)``
``¬ ¬ ¬ ¬ ¬ Iteration += 1``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ print(''.join(SharedData.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
``¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "Undefined")``
``¬ ¬ ¬ ¬ SharedData.GameError = str(Message)``
``¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ``
``¬ class CreateEngine:``
``¬ ¬ ``
``¬ ¬ ``
``¬ ¬ def __init__(self):``
``¬ ¬ ¬ pass``
``¬ ¬ ``
``¬ ¬ ``
``¬ ¬ def GenerateLoadDisplay(self, LoadingFont, text, MainTitleFont, SecondaryFont, LoadingTextFont):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

``¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``

``¬ ¬ ¬ ¬ PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``
``¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))``

``¬ ¬ ¬ ¬ LoadingTitle = SecondaryFont.render("Loading", self.aa, self.SecondFontCol)``
``¬ ¬ ¬ ¬ self.Display.blit(LoadingTitle, (((self.realWidth-TitleWidth)/2)+55, 50))``

``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (self.ShapeCol), self.aa, [(100, self.realHeight-100), (self.realWidth-100, self.realHeight-100)], 3)``
``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (self.AccentCol), self.aa, self.Progress_Line)``

``¬ ¬ ¬ ¬ DisplayMessage = LoadingFont.render(self.ProgressMessageText, self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ DisplayMessageWidth = DisplayMessage.get_width()``
``¬ ¬ ¬ ¬ self.Display.blit(DisplayMessage, ((self.realWidth-DisplayMessageWidth)/2, self.realHeight-120))``

``¬ ¬ ¬ ¬ TextFontRendered = LoadingTextFont.render(f"{text}", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ TextFontRenderedWidth = TextFontRendered.get_width()``
``¬ ¬ ¬ ¬ self.Display.blit(TextFontRendered, ((self.realWidth-TextFontRenderedWidth)/2, self.realHeight-100))``
``¬ ¬ ¬ except Exception as error:``
``¬ ¬ ¬ ¬ print(error)``

``¬ ¬ def Play(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).fadeout(2000)``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_WAIT)``

``¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
``¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ self.mod_Globals__.Share.initialize(self)``
``¬ ¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ ¬ self.mod_ModernGL_window_.run_window_config(Cubemap)``
``¬ ¬ ¬ ¬ except Exception as Error:``
``¬ ¬ ¬ ¬ ¬ print(Error)``
``¬ ¬ ¬ ¬ ¬ pass``
``¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
``¬ ¬ ¬ ¬ return Message, "Undefined"``
``¬ ¬ ¬ ``
``¬ ¬ ¬ ``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_GetSavedData>")``
   ``¬ class LoadSaveFiles:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ def ReadMainSave(self):``
``¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'r') as openfile:``
``¬ ¬ ¬ ¬ save = self.mod_JSON__.load(openfile)``
``¬ ¬ ``
``¬ ¬ ¬ self.theme = save["theme"]``
``¬ ¬ ¬ self.RunFullStartup = save["startup"]``
``¬ ¬ ¬ self.crash = save["crash"]``
``¬ ¬ ¬ self.Fullscreen = save["WindowStatus"]``
``¬ ¬ ¬ self.RecommendedFPS = save["AdaptiveFPS"]``
``¬ ¬ ¬ self.Devmode = save["Devmode"]``
``¬ ¬ ¬ self.SettingsPreference = save["profile"]``
``¬ ¬ ¬ self.FPS = save["FPS"]``
``¬ ¬ ¬ self.aFPS = save["aFPS"]``
``¬ ¬ ¬ self.Iteration = save["Iteration"]``
``¬ ¬ ¬ self.FOV = save["FOV"]``
``¬ ¬ ¬ self.cameraANGspeed = save["cameraANGspeed"]``
``¬ ¬ ¬ self.RenderFOG = save["RenderFOG"]``
``¬ ¬ ¬ self.aa = save["aa"]``
``¬ ¬ ¬ self.X = save["X"]``
``¬ ¬ ¬ self.Y = save["Y"]``
``¬ ¬ ¬ self.Z = save["Z"]``
``¬ ¬ ¬ self.FanSky = save["FanSky"]``
``¬ ¬ ¬ self.FanPart = save["FanPart"]``
``¬ ¬ ¬ self.sound = save["sound"]``
``¬ ¬ ¬ self.soundVOL = save["soundVOL"]``
``¬ ¬ ¬ self.music = save["music"]``
``¬ ¬ ¬ self.musicVOL = save["musicVOL"]``
``¬ ¬ ¬ self.lastRun = save["lastRun"]``
``¬ ¬ ¬ self.SavedWidth = save["DisplayWidth"]``
``¬ ¬ ¬ self.SavedHeight = save["DisplayHeight"]``
``¬ ¬ ¬ self.Total_Vertices = save["Total_Vertices"]``
``¬ ¬ ¬ if self.Total_Vertices == 0:``
``¬ ¬ ¬ ¬ self.Total_Vertices = 1``

``¬ ¬ def RepairLostSave(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ SavedData = {"Total_Vertices":0, "theme":False, "profile":"Medium", "Devmode":0, "AdaptiveFPS": 60, "FPS":60, "aFPS":60, "Iteration":1, "FOV":75, "cameraANGspeed":3, "aa":True, "RenderFOG":True, "FanSky":True, "FanPart":True, "sound":True, "soundVOL":75, "music":True, "musicVOL":50, "X":0, "Y":0, "Z":0, "lastRun":"29/09/2021", 'startup':True, 'crash': False, 'DisplayWidth':1280, 'DisplayHeight':720, 'WindowStatus':True}``
``¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'w') as openfile:``
``¬ ¬ ¬ ¬ ¬ self.mod_JSON__.dump(SavedData, openfile)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ return Message``
``¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ return None``

``¬ ¬ def SaveTOconfigFILE(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ current_time = self.mod_Datetime__.datetime.now()``
``¬ ¬ ¬ ¬ currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"``
``¬ ¬ ¬ ¬ SavedData = {"Total_Vertices":self.Total_Vertices, "theme":self.theme, "profile":self.SettingsPreference, "Devmode":self.Devmode, "AdaptiveFPS": self.RecommendedFPS, "FPS":self.FPS, "aFPS":self.aFPS, "Iteration":self.Iteration, "FOV":self.FOV, "cameraANGspeed":self.cameraANGspeed, "aa":self.aa, "RenderFOG":self.RenderFOG, "FanSky":self.FanSky, "FanPart":self.FanPart, "sound":self.sound, "soundVOL":self.soundVOL, "music":self.music, "musicVOL":self.musicVOL, "X":self.X, "Y":self.Y, "Z":self.Z, "lastRun":currentDate, 'startup':self.RunFullStartup, 'crash': False, 'DisplayWidth':self.SavedWidth, 'DisplayHeight':self.SavedHeight, 'WindowStatus':self.Fullscreen}``
``¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'w') as openfile:``
``¬ ¬ ¬ ¬ ¬ self.mod_JSON__.dump(SavedData, openfile)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ return Message``
``¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ return None``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_HomeScreen>")``
   ``¬ class GenerateHomeScreen:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``
``¬ ¬ ``
``¬ ¬ def DisplayMessage(self, MessageFont, Message, Colour):``
``¬ ¬ ¬ MessageText = MessageFont.render(Message, self.aa, Colour)``
``¬ ¬ ¬ MessageTextWidth = MessageText.get_width()``
``¬ ¬ ¬ MessageTextHeight = MessageText.get_height()``
``¬ ¬ ¬ self.Display.blit(MessageText, ((self.realWidth-MessageTextWidth)/2, (self.realHeight-MessageTextHeight)))``
``¬ ¬ ¬ ``

``¬ ¬ def Home_Screen(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Home screen")``
``¬ ¬ ¬ ¬ Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()``
``¬ ¬ ¬ ¬ SelectorWidth = Selector.get_width()``
``¬ ¬ ¬ ¬ hover1 = False``
``¬ ¬ ¬ ¬ hover2 = False``
``¬ ¬ ¬ ¬ hover3 = False``
``¬ ¬ ¬ ¬ hover4 = False``
``¬ ¬ ¬ ¬ hover5 = False``
``¬ ¬ ¬ ¬ hover6 = False``
``¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) ``
``¬ ¬ ¬ ¬ PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``
``¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
``¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

``¬ ¬ ¬ ¬ SideFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20) ``
``¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20) ``
``¬ ¬ ¬ ¬ ButtonFont1 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
``¬ ¬ ¬ ¬ ButtonFont2 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
``¬ ¬ ¬ ¬ ButtonFont3 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
``¬ ¬ ¬ ¬ ButtonFont4 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
``¬ ¬ ¬ ¬ ButtonFont5 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
``¬ ¬ ¬ ¬ ButtonFont6 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
``¬ ¬ ¬ ¬ MessageFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``

``¬ ¬ ¬ ¬ oldTHEME = self.theme``
``¬ ¬ ¬ ¬ tempFPS = self.FPS``
``¬ ¬ ¬ ¬ coloursARRAY = []``

``¬ ¬ ¬ ¬ anim = False``

``¬ ¬ ¬ ¬ special = [30, 30, 30]``
``¬ ¬ ¬ ¬ TargetARRAY = []``

``¬ ¬ ¬ ¬ ColourDisplacement = 80``

``¬ ¬ ¬ ¬ increment = False``
``¬ ¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ ¬ coloursARRAY = []``
``¬ ¬ ¬ ¬ ¬ if anim == True:``
``¬ ¬ ¬ ¬ ¬ ¬ anim = False``
``¬ ¬ ¬ ¬ ¬ ¬ TargetARRAY = []``
``¬ ¬ ¬ ¬ ¬ ¬ for a in range(self.mod_Random__.randint(0, 32)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ TargetARRAY.append(a)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if len(TargetARRAY) == 0:``
``¬ ¬ ¬ ¬ ¬ ¬ TargetARRAY = [33]``
``¬ ¬ ¬ ¬ ¬ for i in range(32):``
``¬ ¬ ¬ ¬ ¬ ¬ for j in range(len(TargetARRAY)):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if i == TargetARRAY[j]:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ coloursARRAY.append(special)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ coloursARRAY.append(self.ShapeCol)``

``¬ ¬ ¬ ¬ ¬ if increment == False:``
``¬ ¬ ¬ ¬ ¬ ¬ if self.aFPS == 0 or self.Iteration == 0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement -= (self.mod_Random__.randint(0,10)/((self.FPS)/4))``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement -= (self.mod_Random__.randint(0,10)/((self.aFPS/self.Iteration)/4))``
``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = ColourDisplacement, ColourDisplacement, ColourDisplacement``
``¬ ¬ ¬ ¬ ¬ if increment == True:``
``¬ ¬ ¬ ¬ ¬ ¬ if self.aFPS == 0 or self.Iteration == 0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement += (self.mod_Random__.randint(0,10)/((self.FPS)/4))``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement += (self.mod_Random__.randint(0,10)/((self.aFPS/self.Iteration)/4))``
``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = ColourDisplacement, ColourDisplacement, ColourDisplacement``
``¬ ¬ ¬ ¬ ¬ if special[0] <= 30:``
``¬ ¬ ¬ ¬ ¬ ¬ increment = True``
``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = 30, 30, 30``
``¬ ¬ ¬ ¬ ¬ if special[0] >= 80:``
``¬ ¬ ¬ ¬ ¬ ¬ increment = False``
``¬ ¬ ¬ ¬ ¬ ¬ anim = True``
``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = 80, 80, 80``

``¬ ¬ ¬ ¬ ¬ if self.mod_Pygame__.mixer.Channel(3).get_busy() == 1:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(3).stop()``

``¬ ¬ ¬ ¬ ¬ if str(self.Display) == "<Surface(Dead Display)>":``
``¬ ¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``
``¬ ¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``

``¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
``¬ ¬ ¬ ¬ ¬ if not (self.realWidth == self.FullscreenX and self.realHeight == self.FullscreenY):``
``¬ ¬ ¬ ¬ ¬ ¬ self.SavedWidth, self.SavedHeight = self.mod_Pygame__.display.get_window_size()``

``¬ ¬ ¬ ¬ ¬ if self.SavedWidth == self.FullscreenX:``
``¬ ¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
``¬ ¬ ¬ ¬ ¬ if self.SavedHeight == self.FullscreenY:``
``¬ ¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``

``¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
``¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

``¬ ¬ ¬ ¬ ¬ yScaleFact = self.realHeight/720``
``¬ ¬ ¬ ¬ ¬ xScaleFact = self.realWidth/1280``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if not oldTHEME == self.theme:``
``¬ ¬ ¬ ¬ ¬ ¬ Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()``
``¬ ¬ ¬ ¬ ¬ ¬ SelectorWidth = Selector.get_width()``
``¬ ¬ ¬ ¬ ¬ ¬ oldTHEME = self.theme``

``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``
``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``
``¬ ¬ ¬ ¬ ¬ Mx, My = self.mod_Pygame__.mouse.get_pos() ``
``¬ ¬ ¬ ¬ ¬ PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``

``¬ ¬ ¬ ¬ ¬ Name = SideFont.render("By Tom Jebbo", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ NameHeight = Name.get_height()``

``¬ ¬ ¬ ¬ ¬ Version = VersionFont.render(f"Version: {self.version}", self.aa, self.FontCol) ``
``¬ ¬ ¬ ¬ ¬ VersionWidth = Version.get_width()``
``¬ ¬ ¬ ¬ ¬ VersionHeight = Version.get_height()``

``¬ ¬ ¬ ¬ ¬ Play = ButtonFont1.render("Play", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ PlayWidth = Play.get_width()``

``¬ ¬ ¬ ¬ ¬ SettingsText = ButtonFont2.render("Settings", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ SettingsWidth = SettingsText.get_width()``

``¬ ¬ ¬ ¬ ¬ Character_DesignerText = ButtonFont3.render("Character Designer", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ CharDesignerWidth = Character_DesignerText.get_width()``

``¬ ¬ ¬ ¬ ¬ AchievementsText = ButtonFont4.render("Achievements", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ AchievementsWidth = AchievementsText.get_width()``

``¬ ¬ ¬ ¬ ¬ Credits_and_Change_Log_Text = ButtonFont5.render("Credits", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ CreditsWidth = Credits_and_Change_Log_Text.get_width()``

``¬ ¬ ¬ ¬ ¬ BenchmarkText = ButtonFont6.render("Benchmark", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ BenchmarkWidth = BenchmarkText.get_width()``

``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "saveANDexit"``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYDOWN: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1 ``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True ``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONUP: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Home screen")``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ ButtonFont1.set_underline(hover1) ``
``¬ ¬ ¬ ¬ ¬ ButtonFont2.set_underline(hover2) ``
``¬ ¬ ¬ ¬ ¬ ButtonFont3.set_underline(hover3)``
``¬ ¬ ¬ ¬ ¬ ButtonFont4.set_underline(hover4)``
``¬ ¬ ¬ ¬ ¬ ButtonFont5.set_underline(hover5)``
``¬ ¬ ¬ ¬ ¬ ButtonFont6.set_underline(hover6)``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if My >= 202*yScaleFact and My <= 247*yScaleFact and Mx >= (self.realWidth-(PlayWidth+SelectorWidth))-2:``
``¬ ¬ ¬ ¬ ¬ ¬ hover1 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Play"``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ hover1 = False``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if My >= 252*yScaleFact and My <= 297*yScaleFact and Mx >= (self.realWidth-(SettingsWidth+SelectorWidth))-2: ``
``¬ ¬ ¬ ¬ ¬ ¬ hover2 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Settings"``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ hover2 = False``

``¬ ¬ ¬ ¬ ¬ if My >= 302*yScaleFact and My <= 347*yScaleFact and Mx >= (self.realWidth-(CharDesignerWidth+SelectorWidth)-2):``
``¬ ¬ ¬ ¬ ¬ ¬ hover3 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "CharacterDesigner"``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ hover3 = False``

``¬ ¬ ¬ ¬ ¬ if My >= 402*yScaleFact and My <= 447*yScaleFact and Mx >= (self.realWidth-(AchievementsWidth+SelectorWidth)-2):``
``¬ ¬ ¬ ¬ ¬ ¬ hover4 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Achievements"``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ hover4 = False``

``¬ ¬ ¬ ¬ ¬ if My >= 352*yScaleFact and My <= 397*yScaleFact and Mx >= (self.realWidth-(CreditsWidth+SelectorWidth)-2):``
``¬ ¬ ¬ ¬ ¬ ¬ hover5 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Credits"``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ hover5 = False``

``¬ ¬ ¬ ¬ ¬ if My >= 452*yScaleFact and My <= 497*yScaleFact and Mx >= (self.realWidth-(BenchmarkWidth+SelectorWidth)-2):``
``¬ ¬ ¬ ¬ ¬ ¬ hover6 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Benchmark"``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ hover6 = False``

``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if self.FromPlay == True:``
``¬ ¬ ¬ ¬ ¬ ¬ self.FromPlay = False``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_HomeScreen__.GenerateHomeScreen.DisplayMessage(self, MessageFont, "Loading", self.AccentCol)``

``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))``

``¬ ¬ ¬ ¬ ¬ self.Display.blit(Name, (0, (self.realHeight-NameHeight)))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Version, ((self.realWidth-VersionWidth)-2, (self.realHeight-VersionHeight)))``

``¬ ¬ ¬ ¬ ¬ self.Display.blit(Play, ((self.realWidth-PlayWidth)-2, 200*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(SettingsText, ((self.realWidth-SettingsWidth)-2, 250*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Character_DesignerText, ((self.realWidth-CharDesignerWidth)-2, 300*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits_and_Change_Log_Text, ((self.realWidth-CreditsWidth)-2, 350*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsText, ((self.realWidth-AchievementsWidth)-2, 400*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkText, ((self.realWidth-BenchmarkWidth)-2, 450*yScaleFact))``

``¬ ¬ ¬ ¬ ¬ if hover1 == True:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(PlayWidth+SelectorWidth)-2, 200*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ elif hover2 == True:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(SettingsWidth+SelectorWidth)-2, 250*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ elif hover3 == True:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(CharDesignerWidth+SelectorWidth)-2, 300*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ elif hover5 == True:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(CreditsWidth+SelectorWidth)-2, 350*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ elif hover4 == True:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(AchievementsWidth+SelectorWidth)-2, 400*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ elif hover6 == True:``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(BenchmarkWidth+SelectorWidth)-2, 450*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_ARROW)``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
``¬ ¬ ¬ ¬ ¬ if not Message == None:``
``¬ ¬ ¬ ¬ ¬ ¬ return Message, None``

``¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, xScaleFact, yScaleFact, coloursARRAY)``

``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
``¬ ¬ ¬ ¬ return Message, None``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_ImageUtils>")``
   ``¬ class ConvertImage:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def pilImageToSurface(self, pilImage):``
``¬ ¬ ¬ return self.mod_Pygame__.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode).convert()``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_Inventory>")``
   ``¬ class GenerateInventory:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def Inventory(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ Message = self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``
``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``

``¬ ¬ ¬ ¬ MainInventoryFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) ``
``¬ ¬ ¬ ¬ PycraftTitle = MainInventoryFont.render("Pycraft", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``

``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
``¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
``¬ ¬ ¬ ¬ AlphaSurface = self.mod_Pygame__.Surface((realWidth, realHeight), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
``¬ ¬ ¬ ¬ AlphaSurface.set_alpha(204) ``
``¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``

``¬ ¬ ¬ ¬ Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()``
``¬ ¬ ¬ ¬ SelectorWidth = Selector.get_width()``

``¬ ¬ ¬ ¬ hover1 = False ``
``¬ ¬ ¬ ¬ hover2 = False ``
``¬ ¬ ¬ ¬ hover3 = False ``
``¬ ¬ ¬ ¬ hover4 = False ``
``¬ ¬ ¬ ¬ hover5 = False ``
``¬ ¬ ¬ ¬ hover6 = False ``
``¬ ¬ ¬ ¬ hover7 = False``
``¬ ¬ ¬ ¬ hover8 = False``
``¬ ¬ ¬ ¬ mousebuttondown = False``

``¬ ¬ ¬ ¬ ButtonFont1 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
``¬ ¬ ¬ ¬ WeaponsText = ButtonFont1.render("Weapons", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ WeaponsTextWidth = WeaponsText.get_width()``
``¬ ¬ ¬ ¬ WeaponsTextHeight = WeaponsText.get_height()``

``¬ ¬ ¬ ¬ ButtonFont2 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
``¬ ¬ ¬ ¬ RangedWeaponsText = ButtonFont2.render("Ranged Weapons", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ RangedWeaponsTextWidth = RangedWeaponsText.get_width()``
``¬ ¬ ¬ ¬ RangedWeaponsTextHeight= RangedWeaponsText.get_height()``

``¬ ¬ ¬ ¬ ButtonFont3 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
``¬ ¬ ¬ ¬ ShieldsText = ButtonFont3.render("Shields", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ShieldsTextWidth = ShieldsText.get_width()``
``¬ ¬ ¬ ¬ ShieldsTextHeight = ShieldsText.get_height()``

``¬ ¬ ¬ ¬ ButtonFont4 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
``¬ ¬ ¬ ¬ ArmourText = ButtonFont4.render("Armour", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ArmourTextWidth = ArmourText.get_width()``
``¬ ¬ ¬ ¬ ArmourTextHeight = ArmourText.get_height()``

``¬ ¬ ¬ ¬ ButtonFont5 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
``¬ ¬ ¬ ¬ FoodText = ButtonFont5.render("Food", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ FoodTextWidth = FoodText.get_width()``
``¬ ¬ ¬ ¬ FoodTextHeight = FoodText.get_height()``

``¬ ¬ ¬ ¬ ButtonFont6 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
``¬ ¬ ¬ ¬ ItemsText = ButtonFont6.render("Items", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ItemsTextWidth = ItemsText.get_width()``
``¬ ¬ ¬ ¬ ItemsTextHeight = ItemsText.get_height()``

``¬ ¬ ¬ ¬ ButtonFont7 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
``¬ ¬ ¬ ¬ SpecialItemsText = ButtonFont7.render("Special Items", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ SpecialItemsTextWidth = SpecialItemsText.get_width()``
``¬ ¬ ¬ ¬ SpecialItemsTextHeight = SpecialItemsText.get_height()``

``¬ ¬ ¬ ¬ ButtonFont8 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
``¬ ¬ ¬ ¬ OptionsText = ButtonFont7.render("Options", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ OptionsTextWidth = OptionsText.get_width()``
``¬ ¬ ¬ ¬ OptionsTextHeight = OptionsText.get_height()``

``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Playing | Inventory")``

``¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``

``¬ ¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

``¬ ¬ ¬ ¬ ¬ yScaleFact = realHeight/720``
``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``

``¬ ¬ ¬ ¬ ¬ Mx, My = self.mod_Pygame__.mouse.get_pos() ``
``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

``¬ ¬ ¬ ¬ ¬ if self.aa == True:``
``¬ ¬ ¬ ¬ ¬ ¬ pilImage = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png"))).resize((realWidth, realHeight), self.mod_PIL_Image_.ANTIALIAS)``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ pilImage = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png"))).resize((realWidth, realHeight))``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ BLURRED_pilImage = pilImage.filter(self.mod_PIL_ImageFilter_.BoxBlur(4))``

``¬ ¬ ¬ ¬ ¬ PauseImg = self.mod_ImageUtils__.ConvertImage.pilImageToSurface(self, BLURRED_pilImage)``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(PauseImg, (0, 0))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(AlphaSurface, (0, 0))``

``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((realWidth-TitleWidth)/2, 0))``

``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_e):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Load3D = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.VIDEORESIZE:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface = self.mod_Pygame__.Surface((realWidth, realHeight), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.set_alpha(204)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True ``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONUP:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYDOWN:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface = self.mod_Pygame__.Surface((FullscreenX, FullscreenY), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.set_alpha(204) ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if My >= 202*yScaleFact and My <= 247*yScaleFact and Mx >= 1155:``
``¬ ¬ ¬ ¬ ¬ ¬ hover1 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip() ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ else: ``
``¬ ¬ ¬ ¬ ¬ ¬ hover1 = False ``

``¬ ¬ ¬ ¬ ¬ if My >= 252*yScaleFact and My <= 297*yScaleFact and Mx >= 1105: ``
``¬ ¬ ¬ ¬ ¬ ¬ hover2 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ hover2 = False``

``¬ ¬ ¬ ¬ ¬ if My >= 302*yScaleFact and My <= 347*yScaleFact and Mx >= 865:``
``¬ ¬ ¬ ¬ ¬ ¬ hover3 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ hover3 = False``

``¬ ¬ ¬ ¬ ¬ if My >= 402*yScaleFact and My <= 447*yScaleFact and Mx >= 1035:``
``¬ ¬ ¬ ¬ ¬ ¬ hover4 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ hover4 = False``

``¬ ¬ ¬ ¬ ¬ if My >= 352*yScaleFact and My <= 397*yScaleFact and Mx >= 880:``
``¬ ¬ ¬ ¬ ¬ ¬ hover5 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ hover5 = False``

``¬ ¬ ¬ ¬ ¬ if My >= 502*yScaleFact and My <= 547*yScaleFact and Mx >= 1095:``
``¬ ¬ ¬ ¬ ¬ ¬ hover6 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ hover6 = False``

``¬ ¬ ¬ ¬ ¬ if My >= 452*yScaleFact and My <= 497*yScaleFact and Mx >= 1095:``
``¬ ¬ ¬ ¬ ¬ ¬ hover7 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ hover7 = False``

``¬ ¬ ¬ ¬ ¬ if My >= 552*yScaleFact and My <= 597*yScaleFact and Mx >= 1095:``
``¬ ¬ ¬ ¬ ¬ ¬ hover8 = True``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ hover8 = False``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ ButtonFont1.set_underline(hover1) ``
``¬ ¬ ¬ ¬ ¬ ButtonFont2.set_underline(hover2) ``
``¬ ¬ ¬ ¬ ¬ ButtonFont3.set_underline(hover3)``
``¬ ¬ ¬ ¬ ¬ ButtonFont4.set_underline(hover4)``
``¬ ¬ ¬ ¬ ¬ ButtonFont5.set_underline(hover5)``
``¬ ¬ ¬ ¬ ¬ ButtonFont6.set_underline(hover6)``
``¬ ¬ ¬ ¬ ¬ ButtonFont7.set_underline(hover7)``
``¬ ¬ ¬ ¬ ¬ ButtonFont8.set_underline(hover8)``
``¬ ¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol) ``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(WeaponsText, ((realWidth-WeaponsTextWidth)-2, 200*yScaleFact)) # ???``

``¬ ¬ ¬ ¬ ¬ if hover1 == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(WeaponsTextWidth+SelectorWidth)-2, 200*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(RangedWeaponsText, ((realWidth-RangedWeaponsTextWidth)-2, 250*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ if hover2 == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(RangedWeaponsTextWidth+SelectorWidth)-2, 250*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(ShieldsText, ((realWidth-ShieldsTextWidth)-2, 300*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ if hover3 == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(ShieldsTextWidth+SelectorWidth)-2, 300*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(ArmourText, ((realWidth-ArmourTextWidth)-2, 350*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ if hover4 == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(FoodTextWidth+SelectorWidth)-2, 400*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(FoodText, ((realWidth-FoodTextWidth)-2, 400*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ if hover5 == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(ArmourTextWidth+SelectorWidth)-2, 350*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(ItemsText, ((realWidth-ItemsTextWidth)-2, 450*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ if hover6 == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(SpecialItemsTextWidth+SelectorWidth)-2, 500*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(SpecialItemsText, ((realWidth-SpecialItemsTextWidth)-2, 500*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ if hover7 == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(ItemsTextWidth+SelectorWidth)-2, 450*yScaleFact))``

``¬ ¬ ¬ ¬ ¬ self.Display.blit(OptionsText, ((realWidth-OptionsTextWidth)-2, 550*yScaleFact))``
``¬ ¬ ¬ ¬ ¬ if hover8 == True:``
``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(OptionsTextWidth+SelectorWidth)-2, 550*yScaleFact))``

``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``
``¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


``print("Started <Pycraft_main>")``
``class Startup:``
``¬ def __init__(Class_Startup_variables):``
``¬ ¬ try:``
``¬ ¬ ¬ import tkinter as tk``
``¬ ¬ ¬ Class_Startup_variables.mod_Tkinter__tk = tk # [Class_Startup_variables] mod (module) (module name) (subsection of module) (name references)``
``¬ ¬ ¬ import tkinter.ttk  # Class _ <class_name> _ variables``
``¬ ¬ ¬ Class_Startup_variables.mod_Tkinter_ttk_ = tkinter.ttk``
``¬ ¬ ¬ from tkinter import messagebox``
``¬ ¬ ¬ Class_Startup_variables.mod_Tkinter_messagebox_ = messagebox``
``¬ ¬ ¬ from PIL import Image, ImageFilter, ImageGrab, ImageTk``
``¬ ¬ ¬ Class_Startup_variables.mod_PIL_Image_ = Image``
``¬ ¬ ¬ Class_Startup_variables.mod_PIL_ImageFilter_ = ImageFilter``
``¬ ¬ ¬ Class_Startup_variables.mod_PIL_ImageTk_ = ImageTk``
``¬ ¬ ¬ Class_Startup_variables.mod_PIL_ImageGrab_ = ImageGrab``
``¬ ¬ ¬ import pygame``
``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__ = pygame``
``¬ ¬ ¬ import numpy``
``¬ ¬ ¬ Class_Startup_variables.mod_Numpy__ = numpy``
``¬ ¬ ¬ import os``
``¬ ¬ ¬ Class_Startup_variables.mod_OS__ = os``
``¬ ¬ ¬ import sys``
``¬ ¬ ¬ Class_Startup_variables.mod_Sys__ = sys``
``¬ ¬ ¬ import random``
``¬ ¬ ¬ Class_Startup_variables.mod_Random__ = random``
``¬ ¬ ¬ import time``
``¬ ¬ ¬ Class_Startup_variables.mod_Time__ = time``
``¬ ¬ ¬ import pygame.locals``
``¬ ¬ ¬ Class_Startup_variables.mod_Pygame_locals_ = pygame.locals``
``¬ ¬ ¬ import OpenGL``
``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL__ = OpenGL``
``¬ ¬ ¬ import OpenGL.GL``
``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL_GL_ = OpenGL.GL``
``¬ ¬ ¬ import OpenGL.GLU``
``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL_GLU_ = OpenGL.GLU``
``¬ ¬ ¬ import OpenGL.GLUT``
``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL_GLUT_ = OpenGL.GLUT``
``¬ ¬ ¬ import moderngl``
``¬ ¬ ¬ Class_Startup_variables.mod_ModernGL__ = moderngl``
``¬ ¬ ¬ import moderngl_window``
``¬ ¬ ¬ Class_Startup_variables.mod_ModernGL_window_ = moderngl_window``
``¬ ¬ ¬ import pyautogui``
``¬ ¬ ¬ Class_Startup_variables.mod_Pyautogui__ = pyautogui``
``¬ ¬ ¬ import psutil``
``¬ ¬ ¬ Class_Startup_variables.mod_Psutil__ = psutil``
``¬ ¬ ¬ import pywavefront``
``¬ ¬ ¬ Class_Startup_variables.mod_Pywavefront__ = pywavefront``
``¬ ¬ ¬ import timeit``
``¬ ¬ ¬ Class_Startup_variables.mod_Timeit__ = timeit``
``¬ ¬ ¬ import subprocess``
``¬ ¬ ¬ Class_Startup_variables.mod_Subprocess__ = subprocess``
``¬ ¬ ¬ import traceback``
``¬ ¬ ¬ Class_Startup_variables.mod_Traceback__ = traceback``
``¬ ¬ ¬ import datetime``
``¬ ¬ ¬ Class_Startup_variables.mod_Datetime__ = datetime``
``¬ ¬ ¬ import ctypes``
``¬ ¬ ¬ Class_Startup_variables.mod_Ctypes__ = ctypes``
``¬ ¬ ¬ import json``
``¬ ¬ ¬ Class_Startup_variables.mod_JSON__ = json``
``¬ ¬ ¬ import threading``
``¬ ¬ ¬ Class_Startup_variables.mod_Threading__ = threading``
``¬ ¬ ¬ import cpuinfo``
``¬ ¬ ¬ Class_Startup_variables.mod_CPUinfo__ = cpuinfo``
``¬ ¬ ¬ import array``
``¬ ¬ ¬ Class_Startup_variables.mod_Array__ = array``
``¬ ¬ ¬ import GPUtil``
``¬ ¬ ¬ Class_Startup_variables.mod_GPUtil__ = GPUtil``
``¬ ¬ ¬ from tabulate import tabulate``
``¬ ¬ ¬ Class_Startup_variables.mod_Tabulate_tabulate_ = tabulate``
``¬ ¬ ¬ from pyrr import Matrix44``
``¬ ¬ ¬ Class_Startup_variables.mod_Pyrr_Matrix44_ = Matrix44``
``¬ ¬ ¬ ``
``¬ ¬ ¬ moderngl.create_standalone_context()``
``¬ ¬ ¬ ``
``¬ ¬ ¬ os.environ['SDL_VIDEO_CENTERED'] = '1'``

``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.init()``
``¬ ¬ ¬ ``
``¬ ¬ ¬ import PycraftStartupTest``
``¬ ¬ ¬ Class_Startup_variables.mod_PycraftStartupTest__ = PycraftStartupTest``
``¬ ¬ ¬ import StartupAnimation``
``¬ ¬ ¬ Class_Startup_variables.mod_StartupAnimation__ = StartupAnimation``
``¬ ¬ ¬ import DisplayUtils``
``¬ ¬ ¬ Class_Startup_variables.mod_DisplayUtils__ = DisplayUtils``
``¬ ¬ ¬ import GetSavedData``
``¬ ¬ ¬ Class_Startup_variables.mod_GetSavedData__ = GetSavedData``
``¬ ¬ ¬ import ThemeUtils``
``¬ ¬ ¬ Class_Startup_variables.mod_ThemeUtils__ = ThemeUtils``
``¬ ¬ ¬ import HomeScreen``
``¬ ¬ ¬ Class_Startup_variables.mod_HomeScreen__ = HomeScreen``
``¬ ¬ ¬ import SoundUtils``
``¬ ¬ ¬ Class_Startup_variables.mod_SoundUtils__ = SoundUtils``
``¬ ¬ ¬ import DrawingUtils``
``¬ ¬ ¬ Class_Startup_variables.mod_DrawingUtils__ = DrawingUtils``
``¬ ¬ ¬ import CaptionUtils``
``¬ ¬ ¬ Class_Startup_variables.mod_CaptionUtils__ = CaptionUtils``
``¬ ¬ ¬ import Credits``
``¬ ¬ ¬ Class_Startup_variables.mod_Credits__ = Credits``
``¬ ¬ ¬ import TkinterUtils``
``¬ ¬ ¬ Class_Startup_variables.mod_TkinterUtils__ = TkinterUtils``
``¬ ¬ ¬ import Achievements``
``¬ ¬ ¬ Class_Startup_variables.mod_Achievements__ = Achievements``
``¬ ¬ ¬ import CharacterDesigner``
``¬ ¬ ¬ Class_Startup_variables.mod_CharacterDesigner__ = CharacterDesigner``
``¬ ¬ ¬ import Settings``
``¬ ¬ ¬ Class_Startup_variables.mod_Settings__ = Settings``
``¬ ¬ ¬ import Benchmark``
``¬ ¬ ¬ Class_Startup_variables.mod_Benchmark__ = Benchmark``
``¬ ¬ ¬ import ExBenchmark``
``¬ ¬ ¬ Class_Startup_variables.mod_ExBenchmark__ = ExBenchmark``
``¬ ¬ ¬ import OGLbenchmark``
``¬ ¬ ¬ Class_Startup_variables.mod_OGLbenchmark__ = OGLbenchmark``
``¬ ¬ ¬ import base``
``¬ ¬ ¬ Class_Startup_variables.mod_Base__ = base``
``¬ ¬ ¬ import ShareDataUtil``
``¬ ¬ ¬ Class_Startup_variables.mod_Globals__ = ShareDataUtil``
``¬ ¬ ¬ import TextUtils``
``¬ ¬ ¬ Class_Startup_variables.mod_TextUtils__ = TextUtils``
``¬ ¬ ¬ import Inventory``
``¬ ¬ ¬ Class_Startup_variables.mod_Inventory__ = Inventory``
``¬ ¬ ¬ import ImageUtils``
``¬ ¬ ¬ Class_Startup_variables.mod_ImageUtils__ = ImageUtils``
``¬ ¬ ¬ import MapGUI``
``¬ ¬ ¬ Class_Startup_variables.mod_MapGUI__ = MapGUI``
``¬ ¬ ¬ import ThreadingUtil``
``¬ ¬ ¬ Class_Startup_variables.mod_ThreadingUtil__ = ThreadingUtil``

``¬ ¬ ¬ Class_Startup_variables.aa = True``
``¬ ¬ ¬ Class_Startup_variables.AccentCol = (237, 125, 49)``
``¬ ¬ ¬ Class_Startup_variables.aFPS = 0``
``¬ ¬ ¬ Class_Startup_variables.BackgroundCol = [30, 30, 30]``
``¬ ¬ ¬ Class_Startup_variables.base_folder = os.path.dirname(__file__)``
``¬ ¬ ¬ Class_Startup_variables.cameraANGspeed = 3.5``
``¬ ¬ ¬ Class_Startup_variables.clock = pygame.time.Clock()``
``¬ ¬ ¬ Class_Startup_variables.Collisions = [False, 0]``
``¬ ¬ ¬ Class_Startup_variables.CompletePercent = 0``
``¬ ¬ ¬ Class_Startup_variables.ctx = 0``
``¬ ¬ ¬ Class_Startup_variables.Load_Progress = 0``
``¬ ¬ ¬ Class_Startup_variables.crash = False``
``¬ ¬ ¬ Class_Startup_variables.CurrentlyPlaying = None``

``¬ ¬ ¬ Class_Startup_variables.Data_aFPS_Min = 60``
``¬ ¬ ¬ Class_Startup_variables.Data_aFPS = []``
``¬ ¬ ¬ Class_Startup_variables.Data_aFPS_Max = 1``

``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Min = 60``
``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE = []``
``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Max = 1``

``¬ ¬ ¬ Class_Startup_variables.Data_eFPS_Min = 60``
``¬ ¬ ¬ Class_Startup_variables.Data_eFPS = []``
``¬ ¬ ¬ Class_Startup_variables.Data_eFPS_Max = 1``

``¬ ¬ ¬ Class_Startup_variables.Data_MemUsE_Min = 60``
``¬ ¬ ¬ Class_Startup_variables.Data_MemUsE = []``
``¬ ¬ ¬ Class_Startup_variables.Data_MemUsE_Max = 1``

``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Min = 60``
``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE = []``
``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Max = 1``
``¬ ¬ ¬ ``
``¬ ¬ ¬ Class_Startup_variables.Devmode = 0``
``¬ ¬ ¬ Class_Startup_variables.Display = 0``
``¬ ¬ ¬ Class_Startup_variables.eFPS = 60``
``¬ ¬ ¬ Class_Startup_variables.FanSky = True``
``¬ ¬ ¬ Class_Startup_variables.FanPart = True``
``¬ ¬ ¬ Class_Startup_variables.FontCol = (255, 255, 255)``
``¬ ¬ ¬ Class_Startup_variables.FOV = 70``
``¬ ¬ ¬ Class_Startup_variables.FromPlay = False``
``¬ ¬ ¬ Class_Startup_variables.Fullscreen = False``
``¬ ¬ ¬ Class_Startup_variables.FPS = 60``
``¬ ¬ ¬ Class_Startup_variables.FullscreenX, Class_Startup_variables.FullscreenY = pyautogui.size()``
``¬ ¬ ¬ Class_Startup_variables.GameError = None``
``¬ ¬ ¬ Class_Startup_variables.G3Dscale = 600000``
``¬ ¬ ¬ Class_Startup_variables.GetScreenGraphics = True``
``¬ ¬ ¬ Class_Startup_variables.HUD_Surface = None``
``¬ ¬ ¬ Class_Startup_variables.Iteration = 1``
``¬ ¬ ¬ Class_Startup_variables.lastRun = "29/09/2021"``
``¬ ¬ ¬ Class_Startup_variables.Load3D = True``
``¬ ¬ ¬ Class_Startup_variables.LoadMusic = True``
``¬ ¬ ¬ ``
``¬ ¬ ¬ Class_Startup_variables.Map = 0``
``¬ ¬ ¬ Class_Startup_variables.Map_box = 0``
``¬ ¬ ¬ Class_Startup_variables.Map_scale = 0``
``¬ ¬ ¬ Class_Startup_variables.Map_size = 0``
``¬ ¬ ¬ Class_Startup_variables.Map_trans = 0``
``¬ ¬ ¬ Class_Startup_variables.MapVerts = 0``
``¬ ¬ ¬ Class_Startup_variables.map_vertices = []``
``¬ ¬ ¬ Class_Startup_variables.max_Map_size = 0``
``¬ ¬ ¬ ``
``¬ ¬ ¬ Class_Startup_variables.HUD_object = 0``
``¬ ¬ ¬ Class_Startup_variables.HUD_box = 0``
``¬ ¬ ¬ Class_Startup_variables.HUD_scale = 0``
``¬ ¬ ¬ Class_Startup_variables.HUD_size = 0``
``¬ ¬ ¬ Class_Startup_variables.HUD_trans = 0``
``¬ ¬ ¬ Class_Startup_variables.HUDVerts = 0``
``¬ ¬ ¬ Class_Startup_variables.HUD_vertices = []``
``¬ ¬ ¬ Class_Startup_variables.max_HUD_size = 0``
``¬ ¬ ¬ ``
``¬ ¬ ¬ Class_Startup_variables.Map_max_v = 0``
``¬ ¬ ¬ Class_Startup_variables.Map_min_v = 0``
``¬ ¬ ¬ ``
``¬ ¬ ¬ Class_Startup_variables.HUD_max_v = 0``
``¬ ¬ ¬ Class_Startup_variables.HUD_min_v = 0``
``¬ ¬ ¬ ``
``¬ ¬ ¬ Class_Startup_variables.music = True``
``¬ ¬ ¬ Class_Startup_variables.musicVOL = 5``
``¬ ¬ ¬ Class_Startup_variables.Numpy_map_vertices = 0``
``¬ ¬ ¬ Class_Startup_variables.Progress_Line = []``
``¬ ¬ ¬ Class_Startup_variables.ProgressMessageText = "Initiating"``
``¬ ¬ ¬ Class_Startup_variables.realHeight = 720``
``¬ ¬ ¬ Class_Startup_variables.realWidth = 1280``
``¬ ¬ ¬ Class_Startup_variables.RecommendedFPS = 60``
``¬ ¬ ¬ Class_Startup_variables.RenderFOG = True``
``¬ ¬ ¬ Class_Startup_variables.RunFullStartup = False``
``¬ ¬ ¬ Class_Startup_variables.SecondFontCol = (100, 100, 100)``
``¬ ¬ ¬ Class_Startup_variables.SavedWidth = 1280``
``¬ ¬ ¬ Class_Startup_variables.SavedHeight = 720``
``¬ ¬ ¬ Class_Startup_variables.ShapeCol = (80, 80, 80)``
``¬ ¬ ¬ Class_Startup_variables.skybox_texture = 0``
``¬ ¬ ¬ Class_Startup_variables.sound = True``
``¬ ¬ ¬ Class_Startup_variables.soundVOL = 75``
``¬ ¬ ¬ Class_Startup_variables.Stop_Thread_Event = Class_Startup_variables.mod_Threading__.Event()``
``¬ ¬ ¬ Class_Startup_variables.SettingsPreference = "Medium"``
``¬ ¬ ¬ Class_Startup_variables.theme = False``
``¬ ¬ ¬ Class_Startup_variables.ThreadStatus = "Running"``
``¬ ¬ ¬ Class_Startup_variables.Timer = 0``
``¬ ¬ ¬ Class_Startup_variables.Total_move_x = 0``
``¬ ¬ ¬ Class_Startup_variables.Total_move_y = 0``
``¬ ¬ ¬ Class_Startup_variables.Total_move_z = 0``
``¬ ¬ ¬ Class_Startup_variables.TotalRotation = 0``
``¬ ¬ ¬ Class_Startup_variables.Total_Vertices = 0``
``¬ ¬ ¬ Class_Startup_variables.version = "0.9.3"``
``¬ ¬ ¬ Class_Startup_variables.vertex = 0``
``¬ ¬ ¬ Class_Startup_variables.X = 0``
``¬ ¬ ¬ Class_Startup_variables.Y = 0``
``¬ ¬ ¬ Class_Startup_variables.Z = 0``

``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.StartVariableChecking, args=(Class_Startup_variables,))``
``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.start()``
``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.name = "Thread_StartLongThread"``

``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.StartCPUlogging, args=(Class_Startup_variables,))``
``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.start()``
``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.name = "Thread_GetCPUMetrics"``

``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.AdaptiveMode, args=(Class_Startup_variables,))``
``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.start()``
``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.name = "Thread_AdaptiveMode"``
``¬ ¬ ¬ ``
``¬ ¬ ¬ Class_Startup_variables.mod_Globals__.Share.initialize(Class_Startup_variables)``
``¬ ¬ ¬ ``
``¬ ¬ ¬ import GameEngine``
``¬ ¬ ¬ Class_Startup_variables.mod_MainGameEngine__ = GameEngine``
``¬ ¬ except Exception as error:``
``¬ ¬ ¬ print(error)``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ import tkinter as tk``
``¬ ¬ ¬ ¬ root = tk.Tk()``
``¬ ¬ ¬ ¬ root.withdraw()``
``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Tkinter_messagebox_.showerror("Startup Fail", "Missing required modules")``
``¬ ¬ ¬ ¬ quit()``
``¬ ¬ ¬ except:``
``¬ ¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
``¬ ¬ ¬ ¬ ¬ sys.exit("0.0.0 -Thank you for playing")``
``¬ ¬ ¬ ¬ except:``
``¬ ¬ ¬ ¬ ¬ quit()``
``¬ ¬ ¬ ¬ ¬ ``
``¬ def crash(ErrorREPORT):``
``¬ ¬ Class_Startup_variables.Stop_Thread_Event.set()``
``¬ ¬ if not ErrorREPORT == None:``
``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
``¬ ¬ ¬ Class_Startup_variables.mod_Time__.sleep(1.01)``
``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.init()``
``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.mixer.stop()``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ Message = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.SaveTOconfigFILE(Class_Startup_variables)``
``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.init()``
``¬ ¬ ¬ ¬ Display = Class_Startup_variables.mod_Pygame__.display.set_mode((1280, 720))``
``¬ ¬ ¬ ¬ icon = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.set_icon(icon)``
``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.set_caption(f"Pycraft: An Error Occurred")``

``¬ ¬ ¬ ¬ MessageFont = Class_Startup_variables.mod_Pygame__.font.Font(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Fonts\\Book Antiqua.ttf")), 15)``

``¬ ¬ ¬ ¬ ErrorMessageText = MessageFont.render(str(ErrorREPORT), True, (255,0,0))``
``¬ ¬ ¬ ¬ ErrorMessageTextWidth = ErrorMessageText.get_width()``
``¬ ¬ ¬ ¬ ErrorMessageTextHeight = ErrorMessageText.get_height()``
``¬ ¬ ¬ ¬ Display = Class_Startup_variables.mod_Pygame__.display.set_mode((1280,720))``

``¬ ¬ ¬ ¬ IconImage = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Resources\\Error_Resources\\Icon.jpg")))``
``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.set_icon(IconImage)``
``¬ ¬ ¬ ¬ image = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Resources\\Error_Resources\\Error_Message.png")))``
``¬ ¬ ¬ ¬ Clock = Class_Startup_variables.mod_Pygame__.time.Clock()``
``¬ ¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ ¬ Display.fill((20,20,20))``
``¬ ¬ ¬ ¬ ¬ Display.blit(image, (0,0))``

``¬ ¬ ¬ ¬ ¬ Display.blit(ErrorMessageText, ((((1280/2)-ErrorMessageTextWidth)/2), (720-ErrorMessageTextHeight)/2))``

``¬ ¬ ¬ ¬ ¬ for event in Class_Startup_variables.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == Class_Startup_variables.mod_Pygame__.QUIT:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit(f"0.1.0- Thank you for playing")``

``¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ Clock.tick(30)``
``¬ ¬ ¬ except Exception as error:``
``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit(f"0.2.0- {error} Thank you for playing")``
``¬ ¬ else:``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
``¬ ¬ ¬ except Exception as error:``
``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit(f"0.3.0- {error} Thank you for playing")``
``¬ ¬ ¬ ¬ quit()``
``¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit("0.4.0- Thank you for playing")``
``¬ ¬ ¬ ¬ quit()``

``Class_Startup_variables = Startup()``
``try:``
``¬ Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.ReadMainSave(Class_Startup_variables)``
``except Exception as FileError:``
``¬ try:``
``¬ ¬ if str(FileError) == "Expecting value: line 1 column 1 (char 0)":``
``¬ ¬ ¬ Report = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.RepairLostSave(Class_Startup_variables)``
``¬ ¬ ¬ ErrorString = "Unable to access vital Saved Data, have attempted a fix successfully", FileError``
``¬ ¬ ¬ Message = "0.0.0- " + str(ErrorString)``
``¬ ¬ ¬ Startup.crash(Message)``
``¬ except Exception as Error:``
``¬ ¬ Message = "0.0.1- " + str(Error)``
``¬ ¬ Startup.crash(Message)``

``¬ Message = "0.2- " + str(FileError)``
``¬ Startup.crash(Message)``

``Message = Class_Startup_variables.mod_PycraftStartupTest__.StartupTest.PycraftSelfTest(Class_Startup_variables)``
``if not Message == None:``
``¬ Message = "0.0.3- " + str(Message)``
``¬ Startup.crash(Message)``

``if Class_Startup_variables.theme == False:``
``¬ Message = Class_Startup_variables.mod_ThemeUtils__.DetermineThemeColours.GetThemeGUI(Class_Startup_variables)``
``¬ if not Message == None:``
``¬ ¬ Message = "0.0.4- " + str(Message)``
``¬ ¬ Startup.crash(Message)``

``Message = Class_Startup_variables.mod_ThemeUtils__.DetermineThemeColours.GetColours(Class_Startup_variables)``

``if not Message == None:``
``¬ Message = "0.0.5- " + str(Message)``
``¬ Startup.crash(Message)``
``¬ ``
``Message = Class_Startup_variables.mod_StartupAnimation__.GenerateStartupScreen.Start(Class_Startup_variables)``
``if not Message == None:``
``¬ Message = "0.0.6- " + str(Message)``
``¬ Startup.crash(Message)``

``Class_Startup_variables.Command = "Undefined"``
``while True:``
``¬ if Class_Startup_variables.Command == "saveANDexit":``
``¬ ¬ Message = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.SaveTOconfigFILE(Class_Startup_variables)``
``¬ ¬ if not Message == None:``
``¬ ¬ ¬ Message = "0.0.7- " + str(Message)``
``¬ ¬ ¬ Startup.crash(Message)``
``¬ ¬ else:``
``¬ ¬ ¬ Class_Startup_variables.Stop_Thread_Event.set()``

``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.join()``
``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.join()``
``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.join()``
``¬ ¬ ¬ ``
``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
``¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit("0.5.0- Thank you for playing") # 0 = Order of running, 5 = 5th occurrence down page``
``¬ elif Class_Startup_variables.Command == "Credits":``
``¬ ¬ Message = Class_Startup_variables.mod_Credits__.GenerateCredits.Credits(Class_Startup_variables)``
``¬ ¬ if not Message == None:``
``¬ ¬ ¬ Message = "0.0.8- " + str(Message)``
``¬ ¬ ¬ Startup.crash(Message)``
``¬ ¬ Class_Startup_variables.Command = "Undefined"``
``¬ elif Class_Startup_variables.Command == "Achievements":``
``¬ ¬ Message = Class_Startup_variables.mod_Achievements__.GenerateAchievements.Achievements(Class_Startup_variables)``
``¬ ¬ if not Message == None:``
``¬ ¬ ¬ Message = "0.0.9- " + str(Message)``
``¬ ¬ ¬ Startup.crash(Message)``
``¬ ¬ Class_Startup_variables.Command = "Undefined"``
``¬ elif Class_Startup_variables.Command == "CharacterDesigner":``
``¬ ¬ Message = Class_Startup_variables.mod_CharacterDesigner__.GenerateCharacterDesigner.CharacterDesigner(Class_Startup_variables)``
``¬ ¬ if not Message == None:``
``¬ ¬ ¬ Message = "0.0.10- " + str(Message)``
``¬ ¬ ¬ Startup.crash(Message)``
``¬ ¬ Class_Startup_variables.Command = "Undefined"``
``¬ elif Class_Startup_variables.Command == "Settings":``
``¬ ¬ Message = Class_Startup_variables.mod_Settings__.GenerateSettings.settings(Class_Startup_variables)``
``¬ ¬ if not Message == None:``
``¬ ¬ ¬ Message = "0.0.11- " + str(Message)``
``¬ ¬ ¬ Startup.crash(Message)``
``¬ ¬ Class_Startup_variables.Command = "Undefined"``
``¬ elif Class_Startup_variables.Command == "Benchmark":``
``¬ ¬ Message = Class_Startup_variables.mod_Benchmark__.GenerateBenchmarkMenu.Benchmark(Class_Startup_variables)``
``¬ ¬ if not Message == None:``
``¬ ¬ ¬ Message = "0.0.12- " + str(Message)``
``¬ ¬ ¬ Startup.crash(Message)``
``¬ ¬ Class_Startup_variables.Command = "Undefined"``
``¬ elif Class_Startup_variables.Command == "Play":``
``¬ ¬ Message = Class_Startup_variables.mod_MainGameEngine__.CreateEngine.Play(Class_Startup_variables)``
``¬ ¬ if Message == None:``
``¬ ¬ ¬ Message = Class_Startup_variables.GameError``
``¬ ¬ if not Message == None:``
``¬ ¬ ¬ Message = "0.0.13- " + str(Message)``
``¬ ¬ ¬ Startup.crash(Message)``
``¬ ¬ Class_Startup_variables.mod_Pygame__.init()``
``¬ ¬ Class_Startup_variables.FromPlay = True``
``¬ ¬ Message = Class_Startup_variables.mod_DisplayUtils__.DisplayUtils.SetDisplay(Class_Startup_variables)``
``¬ ¬ if not Message == None:``
``¬ ¬ ¬ Message = "0.0.14- " + str(Message)``
``¬ ¬ ¬ Startup.crash(Message)``
``¬ elif Class_Startup_variables.Command == "Inventory":``
``¬ ¬ Message = Class_Startup_variables.mod_Inventory__.GenerateInventory.Inventory(Class_Startup_variables)``
``¬ ¬ if not Message == None:``
``¬ ¬ ¬ Message = "0.0.15- " + str(Message)``
``¬ ¬ ¬ Startup.crash(Message)``
``¬ ¬ Class_Startup_variables.Command = "Play"``
``¬ elif Class_Startup_variables.Command == "MapGUI":``
``¬ ¬ Message = Class_Startup_variables.mod_MapGUI__.GenerateMapGUI.MapGUI(Class_Startup_variables)``
``¬ ¬ if not Message == None:``
``¬ ¬ ¬ Message = "0.0.16- " + str(Message)``
``¬ ¬ ¬ Startup.crash(Message)``
``¬ ¬ Class_Startup_variables.Command = "Play"``
``¬ else:``
``¬ ¬ Message, Class_Startup_variables.Command = Class_Startup_variables.mod_HomeScreen__.GenerateHomeScreen.Home_Screen(Class_Startup_variables)``
``¬ ¬ if not Message == None:``
``¬ ¬ ¬ Message = "0.0.17- " + str(Message)``
``¬ ¬ ¬ Startup.crash(Message)``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_MapGUI>")``
   ``¬ class GenerateMapGUI:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def GetMapPos(self):``
``¬ ¬ ¬ x = 0``
``¬ ¬ ¬ z = 0``
``¬ ¬ ¬ if self.X == 0:``
``¬ ¬ ¬ ¬ x = 640``
``¬ ¬ ¬ if self.Z == 0:``
``¬ ¬ ¬ ¬ z = 360``
``¬ ¬ ¬ x -= 6``
``¬ ¬ ¬ z -= 19``
``¬ ¬ ¬ return (x,z)``


``¬ ¬ def MapGUI(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ Message = self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``
``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``

``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
``¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png")))``
``¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``
``¬ ¬ ¬ ¬ MapIcon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Marker.jpg"))).convert()``
``¬ ¬ ¬ ¬ zoom = 0``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Playing | Map")``
``¬ ¬ ¬ ¬ MouseUnlock = True``
``¬ ¬ ¬ ¬ X,Y = 0, 0``
``¬ ¬ ¬ ¬ key = ""``
``¬ ¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_r):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Load3D = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYDOWN:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ zoom = 0``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_w:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "w"``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_s:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "s"``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_d:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "d"``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_a:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "a"``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = self.mod_DisplayUtils__.DisplayUtils.UpdateOPENGLdisplay(self)``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYUP:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ key = ""``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEWHEEL:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if str(event.y)[0] == "-":``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ zoom -= 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ zoom += 1``
``¬ ¬ ¬ ¬ ¬ if zoom >= 2:``
``¬ ¬ ¬ ¬ ¬ ¬ zoom = 2``
``¬ ¬ ¬ ¬ ¬ if zoom <= 0:``
``¬ ¬ ¬ ¬ ¬ ¬ zoom = 0``
``¬ ¬ ¬ ¬ ¬ if key == "w":``
``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y -= 5``
``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y -= 10``
``¬ ¬ ¬ ¬ ¬ if key == "s":``
``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y += 5``
``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y += 10``
``¬ ¬ ¬ ¬ ¬ if key == "d":``
``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ X += 5``
``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ X += 10``
``¬ ¬ ¬ ¬ ¬ if key == "a":``
``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ X -= 5``
``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ X -= 10``
``¬ ¬ ¬ ¬ ¬ if zoom == 0:``
``¬ ¬ ¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((realWidth, realHeight),  self.mod_PIL_Image_.ANTIALIAS)``
``¬ ¬ ¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Map0, (0, 0))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MapIcon, GenerateMapGUI.GetMapPos(self))``
``¬ ¬ ¬ ¬ ¬ ¬ x, y = 0, 0``
``¬ ¬ ¬ ¬ ¬ elif zoom == 1:``
``¬ ¬ ¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((int(realWidth*1.75), int(realHeight*1.75)),  self.mod_PIL_Image_.ANTIALIAS) ``
``¬ ¬ ¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Map0, (X,Y))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MapIcon, GenerateMapGUI.GetMapPos(self))``
``¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
``¬ ¬ ¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((int(realWidth*2), int(realHeight*2)),  self.mod_PIL_Image_.ANTIALIAS) ``
``¬ ¬ ¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Map0, (X,Y))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MapIcon, GenerateMapGUI.GetMapPos(self))``
``¬ ¬ ¬ ¬ ¬ if zoom == 1:``
``¬ ¬ ¬ ¬ ¬ ¬ if X <= -955:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -955``
``¬ ¬ ¬ ¬ ¬ ¬ if Y <= -535:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -535``
``¬ ¬ ¬ ¬ ¬ ¬ if X >= -5:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -5``
``¬ ¬ ¬ ¬ ¬ ¬ if Y >= -5:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -5``
``¬ ¬ ¬ ¬ ¬ if zoom == 2:``
``¬ ¬ ¬ ¬ ¬ ¬ if X <= -1590:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -1590``
``¬ ¬ ¬ ¬ ¬ ¬ if Y <= -890:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -890``
``¬ ¬ ¬ ¬ ¬ ¬ if X >= -10:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -10``
``¬ ¬ ¬ ¬ ¬ ¬ if Y >= -10:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -10``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``
``¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_OGLBenchmark>")``
   ``¬ class LoadOGLBenchmark:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def Cube(self, edges, vertices):``
``¬ ¬ ¬ self.mod_OpenGL_GL_.glBegin(self.mod_OpenGL_GL_.GL_LINES)``
``¬ ¬ ¬ for edge in edges:``
``¬ ¬ ¬ ¬ for vertex in edge:``
``¬ ¬ ¬ ¬ ¬ self.mod_OpenGL_GL_.glVertex3fv(vertices[vertex])``
``¬ ¬ ¬ self.mod_OpenGL_GL_.glEnd()``

``¬ ¬ def CreateBenchmark(self):``
``¬ ¬ ¬ self.mod_OpenGL_GLU_.gluPerspective(45, (1280/720), 0.1, 50.0)``
``¬ ¬ ¬ self.mod_OpenGL_GL_.glTranslatef(0.0,0.0, -5)``

``¬ ¬ def RunBenchmark(self, edges, vertices):``
``¬ ¬ ¬ self.mod_OpenGL_GL_.glRotatef(1, 3, 1, 1)``
``¬ ¬ ¬ self.mod_OpenGL_GL_.glClear(self.mod_OpenGL_GL_.GL_COLOR_BUFFER_BIT|self.mod_OpenGL_GL_.GL_DEPTH_BUFFER_BIT)``
``¬ ¬ ¬ LoadOGLBenchmark.Cube(self, edges, vertices)``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_PycraftStartupTest>")``
   ``¬ class StartupTest:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def PycraftSelfTest(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ import OpenGL.GL as gl``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_mode((1280, 720), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL|self.mod_Pygame__.HIDDEN)``

``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``

``¬ ¬ ¬ ¬ OpenGLversion = str(gl.glGetString(gl.GL_VERSION))[2:5]``
``¬ ¬ ¬ ¬ SDLversion = self.mod_Pygame__.get_sdl_version()[0]``
``¬ ¬ ¬ ¬ RAM = (((self.mod_Psutil__.virtual_memory().available)/1000)/1000) # expressed in MB``

``¬ ¬ ¬ ¬ if float(OpenGLversion) < 2.8:``
``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``
``¬ ¬ ¬ ¬ ¬ root.withdraw()``
``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showerror("Invalid OpenGL version", f"OpenGL version: {OpenGLversion} is not supported; try a version greater than 2.7")``
``¬ ¬ ¬ ¬ ¬ quit()``
``¬ ¬ ¬ ¬ if SDLversion < 2:``
``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``
``¬ ¬ ¬ ¬ ¬ root.withdraw()``
``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showerror("Invalid SDL version", f"SDL version: {SDLversion} is not supported; try a version greater than or equal to 2")``
``¬ ¬ ¬ ¬ ¬ quit()``
``¬ ¬ ¬ ¬ if RAM < 100:``
``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``
``¬ ¬ ¬ ¬ ¬ root.withdraw()``
``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showerror("Minimum system requirements not met", f"Your system does not meet the minimum 100mb free memory specification needed to play this game")``
``¬ ¬ ¬ ¬ ¬ quit()``
``¬ ¬ ¬ ¬ if RAM < 200:``
``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``
``¬ ¬ ¬ ¬ ¬ root.withdraw()``
``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showwarning("Recommended system requirements not met", f"Your system's free memory does not meet the requirement recommended to play this game (200mb), you are still able to, however your experience may not be satisfactory")``
``¬ ¬ ¬ ¬ ¬ from PIL import Image, ImageTk, ImageGrab``
``¬ ¬ ¬ ¬ ¬ import OpenGL.GL``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ if self.mod_Sys__.platform == "win32" or self.mod_Sys__.platform == "win64":``
``¬ ¬ ¬ ¬ ¬ self.mod_OS__.environ["SDL_VIDEO_CENTERED"] = "1"``

``¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.init()``

``¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``

``¬ ¬ ¬ ¬ current_time = self.mod_Datetime__.datetime.now()``
``¬ ¬ ¬ ¬ currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"``
``¬ ¬ ¬ ¬ if not currentDate == self.lastRun or self.crash == True:``
``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
``¬ ¬ ¬ ¬ ¬ yScaleFact = realHeight/720``
``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``
``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
``¬ ¬ ¬ ¬ ¬ Title = TitleFont.render("Pycraft", True, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ TitleWidth = Title.get_width()``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Title, ((realWidth-TitleWidth)/2, 0))``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
``¬ ¬ ¬ ¬ ¬ defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2)``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Error_Resources\\Error_Message.png"))).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Error_Resources\\Icon.jpg"))).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Folder_Resources\\FolderIcon.ico"))).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg"))).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg"))).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg"))).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg"))).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg"))).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg"))).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, f"Resources\\General_Resources\\selectorICONlight.jpg")).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, f"Resources\\General_Resources\\selectorICONdark.jpg")).convert()``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\InventoryGeneral.wav")))``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
``¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
``¬ ¬ ¬ ¬ ¬ Title = TitleFont.render("Pycraft", True, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ TitleWidth = Title.get_width()``
``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Title, ((realWidth-TitleWidth)/2, 0))``
``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ yScaleFact = realHeight/720``
``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``
``¬ ¬ ¬ ¬ ¬ defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (575*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_Settings>")``
   ``¬ class GenerateSettings:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def settings(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Settings")``
``¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
``¬ ¬ ¬ ¬ LOWFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
``¬ ¬ ¬ ¬ MEDIUMFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
``¬ ¬ ¬ ¬ HIGHFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
``¬ ¬ ¬ ¬ ADAPTIVEFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
``¬ ¬ ¬ ¬ LightThemeFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
``¬ ¬ ¬ ¬ DarkThemeFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

``¬ ¬ ¬ ¬ TempMx = 0``
``¬ ¬ ¬ ¬ Mx, My = 0, 0``
``¬ ¬ ¬ ¬ mousebuttondown = False``

``¬ ¬ ¬ ¬ SettingsInformationFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

``¬ ¬ ¬ ¬ scroll = 50``

``¬ ¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``

``¬ ¬ ¬ ¬ ¬ TempMx = Mx``
``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``
``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``
``¬ ¬ ¬ ¬ ¬ Mx, My = self.mod_Pygame__.mouse.get_pos()``
``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``
``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1 ``
``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.MOUSEBUTTONDOWN: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True ``
``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.MOUSEBUTTONUP: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEWHEEL and realHeight <= 760:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_SIZENS)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if str(event.y)[0] == "-":``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ scroll -= 5``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ scroll += 5``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_ARROW)``

``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Settings")``

``¬ ¬ ¬ ¬ ¬ if scroll > 35:``
``¬ ¬ ¬ ¬ ¬ ¬ scroll = 35``
``¬ ¬ ¬ ¬ ¬ elif scroll < 0:``
``¬ ¬ ¬ ¬ ¬ ¬ scroll = 0``

``¬ ¬ ¬ ¬ ¬ titletFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ TitleWidth = titletFont.get_width()``

``¬ ¬ ¬ ¬ ¬ InfoFont = InfoTitleFont.render("Settings", self.aa, self.SecondFontCol)``

``¬ ¬ ¬ ¬ ¬ FPSFont = VersionFont.render(f"FPS: Actual: {int(self.eFPS)} Max: {int(self.FPS)} Average: {int((self.aFPS/self.Iteration))}", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ FOVFont = VersionFont.render(f"FOV: {self.FOV}", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ CamRotFont = VersionFont.render(f"Camera Rotation Speed: {round(self.cameraANGspeed, 1)}", self.aa, self.FontCol) ``
``¬ ¬ ¬ ¬ ¬ ModeFont = VersionFont.render("Mode;¬ ¬  ,¬ ¬ ¬ ¬  ,¬ ¬ ¬ ,¬ ¬   .", self.aa, self.FontCol) ``
``¬ ¬ ¬ ¬ ¬ AAFont = VersionFont.render(f"Anti-Aliasing: {self.aa}", self.aa, self.FontCol) ``
``¬ ¬ ¬ ¬ ¬ RenderFogFont = VersionFont.render(f"Render Fog: {self.RenderFOG}", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ FancySkyFont = VersionFont.render(f"Fancy Skies: {self.FanSky}", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ FancyParticleFont = VersionFont.render(f"Fancy Partices: {self.FanPart}", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ SoundFont = VersionFont.render(f"Sound: {self.sound}", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ SoundVoltFont = VersionFont.render(f"Sound Volume: {self.soundVOL}%", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ SoundVoltFont = VersionFont.render(f"Sound Volume: {self.soundVOL}%", self.aa, self.ShapeCol)``
``¬ ¬ ¬ ¬ ¬ MusicFont = VersionFont.render(f"Music: {self.music}", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ if self.music == True:``
``¬ ¬ ¬ ¬ ¬ ¬ MusicVoltFont = VersionFont.render(f"Music Volume: {self.musicVOL}%", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ MusicVoltFont = VersionFont.render(f"Music Volume: {self.musicVOL}%", self.aa, self.ShapeCol)``
``¬ ¬ ¬ ¬ ¬ ThemeFont = VersionFont.render(f"Theme:¬ ¬   ,¬ ¬   | Current Theme: {self.theme}", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ ThemeInformationFont = SettingsInformationFont.render("Gives you control over which theme you can use", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ ModeInformationFont = SettingsInformationFont.render("Gives you 4 separate per-sets for settings, Adaptive mode will automatically adjust your settings", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ FPSInformationFont = SettingsInformationFont.render("Controls the maximum frame rate the game will limit to, does not guarantee that FPS unfortunately", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ FOVInformationFont = SettingsInformationFont.render("Controls the FOV of the camera in-game", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ CameraRotationSpeedInformationFont = SettingsInformationFont.render("Controls the rotation speed of the camera in-game (1 is low, 5 is high)", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ AAInformationFont = SettingsInformationFont.render("Enables/Disables anti-aliasing in game and in the GUI, will give you a minor performance improvement, mainly for low powered devices", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ self.RenderFogInformationFont = SettingsInformationFont.render("Enables/Disables fog effects in game, for a small performance benefit", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ FancySkiesInformationFont = SettingsInformationFont.render("Enables/Disables a fancy sky box for better visuals in game, does not control anti aliasing for the sky box", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ FancyParticlesInformationFont = SettingsInformationFont.render("Enables/Disables particles in game as particles can have a significant performance decrease", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ SoundInformationFont = SettingsInformationFont.render("Enables/Disables sound effects in game, like for example the click sound and footsteps in game", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ SoundVolInformationFont = SettingsInformationFont.render("Controls the volume of the sound effects, where 100% is maximum and 0% is minimum volume", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ MusicInformationFont = SettingsInformationFont.render("Enables/Disables music in game, like for example the GUI music", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ MusicVolInformationFont = SettingsInformationFont.render("Controls the volume of the music, some effects may not apply until the game reloads", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ FPS_rect = self.mod_Pygame__.Rect(50, 180+scroll, 450*xScaleFact, 10)``
``¬ ¬ ¬ ¬ ¬ FOV_rect = self.mod_Pygame__.Rect(50, 230+scroll, 450*xScaleFact, 10)``
``¬ ¬ ¬ ¬ ¬ CAM_rect = self.mod_Pygame__.Rect(50, 280+scroll, 450*xScaleFact, 10)``
``¬ ¬ ¬ ¬ ¬ sound_rect = self.mod_Pygame__.Rect(50, 580+scroll, 450*xScaleFact, 10)``
``¬ ¬ ¬ ¬ ¬ music_rect = self.mod_Pygame__.Rect(50, 680+scroll, 450*xScaleFact, 10)``
``¬ ¬ ¬ ¬ ¬ aa_rect = self.mod_Pygame__.Rect(50, 330+scroll, 50, 10)``
``¬ ¬ ¬ ¬ ¬ RenderFOG_Rect = self.mod_Pygame__.Rect(50, 380+scroll, 50, 10)``
``¬ ¬ ¬ ¬ ¬ Fansky_Rect = self.mod_Pygame__.Rect(50, 430+scroll, 50, 10)``
``¬ ¬ ¬ ¬ ¬ FanPart_Rect = self.mod_Pygame__.Rect(50, 480+scroll, 50, 10)``
``¬ ¬ ¬ ¬ ¬ sound_Rect = self.mod_Pygame__.Rect(50, 530+scroll, 50, 10)``
``¬ ¬ ¬ ¬ ¬ music_Rect = self.mod_Pygame__.Rect(50, 630+scroll, 50, 10)``
``¬ ¬ ¬ ¬ ¬ slider_Rect = self.mod_Pygame__.Rect(realWidth-15, scroll, 10, 665)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FPS_rect, 0)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FOV_rect, 0)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, CAM_rect, 0)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, sound_rect, 0)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, music_rect, 0)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, aa_rect, 0)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, RenderFOG_Rect, 0)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, Fansky_Rect, 0)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FanPart_Rect, 0)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, sound_Rect, 0)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, music_Rect, 0)``
``¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ if My > 180+scroll and My < 190+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.FPS < 445: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS += 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.FPS > 15: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS -= 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FPS < 15:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 16``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FPS > 445:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 444``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (int(self.FPS+45)*xScaleFact, 185+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (int(self.FPS+45)*xScaleFact, 185+scroll), 9)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 230+scroll and My < 240+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.FOV < 98:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV += 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.FOV > 12:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV -= 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FOV < 12:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV = 13``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FOV > 98:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV = 97``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (int(self.FOV*5)*xScaleFact, 235+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (int(self.FOV*5)*xScaleFact, 235+scroll), 9)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 280+scroll and My < 290+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.cameraANGspeed < 5.0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed += 0.1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.cameraANGspeed > 0.0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed -= 0.1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.cameraANGspeed > 5.0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed = 4.9``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.cameraANGspeed <= 0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed = 0.1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 580+scroll and My < 590+scroll and self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.soundVOL < 100:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL += 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.soundVOL > 0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL -= 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.soundVOL > 100:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL = 100``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.soundVOL < 0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL = 0``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 680+scroll and My < 690+scroll and self.music == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.musicVOL < 100:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL += 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.musicVOL > 0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL -= 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.musicVOL > 100:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL = 100``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.musicVOL < 0:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL = 0``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 330+scroll and My < 340+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 335+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 335+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 335+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 335+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 380+scroll and My < 390+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 385+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 385+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 385+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 385+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 430+scroll and My < 440+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 435+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 435+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 435+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 435+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 480+scroll and My < 490+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 485+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 485+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 485+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 485+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 530+scroll and My < 540+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.sound = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.sound = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 535+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 535+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 535+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 535+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 630+scroll and My < 640+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.music = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).stop()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.LoadMusic = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.music = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 635+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 635+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 635+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 635+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.FPS+45)*xScaleFact), 185+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.FOV*5))*xScaleFact, 235+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)``

``¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 335+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 335+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False: ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 335+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 335+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 385+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 385+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 385+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 385+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 435+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 435+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 435+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 435+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 485+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 485+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 485+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 485+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 535+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 535+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 535+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 535+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 635+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 635+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 635+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 635+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 330+scroll and My < 340+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(AAInformationFont, (120, 325+scroll))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 335+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 335+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 335+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 335+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 380+scroll and My < 390+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(self.RenderFogInformationFont, (120, 375+scroll))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 385+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 385+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 385+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 385+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 430+scroll and My < 440+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FancySkiesInformationFont, (120, 425+scroll))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 435+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 435+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 435+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 435+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 480+scroll and My < 490+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FancyParticlesInformationFont, (120, 475+scroll))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 485+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 485+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 485+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 485+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 530+scroll and My < 540+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundInformationFont, (120, 525+scroll))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 535+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 535+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 535+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 535+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ ¬ if My > 630+scroll and My < 640+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicInformationFont, (120, 625+scroll))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 635+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 635+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 635+scroll), 9)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 635+scroll), 6)``

``¬ ¬ ¬ ¬ ¬ if My >= 65+scroll and My <= 75+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(ThemeInformationFont, (300, 67+scroll))``

``¬ ¬ ¬ ¬ ¬ if My >= 65+scroll and My <= 75+scroll and Mx >= 55 and Mx <= 95:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ LightTheme = LightThemeFont.render("Light", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ ¬ LightThemeFont.set_underline(True)``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "light"``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = self.mod_ThemeUtils__.DetermineThemeColours.GetColours(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = "1.8- " + str(Message)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ LightTheme = LightThemeFont.render("Light", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ ¬ LightThemeFont.set_underline(False)``

``¬ ¬ ¬ ¬ ¬ if My >= 65+scroll and My <= 75+scroll and Mx >= 95 and Mx <= 135:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ DarkTheme = DarkThemeFont.render("Dark", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ ¬ DarkThemeFont.set_underline(True)``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "dark"``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = self.mod_ThemeUtils__.DetermineThemeColours.GetColours(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = "1.8- " + str(Message)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ DarkTheme = DarkThemeFont.render("Dark", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ ¬ DarkThemeFont.set_underline(False)``

``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(ModeInformationFont, (300, 85+scroll))``

``¬ ¬ ¬ ¬ ¬ if My > 680+scroll and My < 690+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicVolInformationFont, (520*xScaleFact, 675+scroll))``

``¬ ¬ ¬ ¬ ¬ if My > 580+scroll and My < 590+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundVolInformationFont, (520*xScaleFact, 575+scroll))``

``¬ ¬ ¬ ¬ ¬ if My > 280+scroll and My < 290+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CameraRotationSpeedInformationFont, (520*xScaleFact, 275+scroll))``

``¬ ¬ ¬ ¬ ¬ if My > 230+scroll and My < 240+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FOVInformationFont, (520*xScaleFact, 225+scroll))``

``¬ ¬ ¬ ¬ ¬ if My > 180+scroll and My < 190+scroll:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSInformationFont, (520*xScaleFact, 175+scroll))``

``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 40 and Mx <= 80:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ LOWtFont = LOWFont.render("Low", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ ¬ LOWFont.set_underline(True)``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "Low"``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 15``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ LOWtFont = LOWFont.render("Low", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ ¬ LOWFont.set_underline(False)``

``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 90 and Mx <= 155:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMtFont = MEDIUMFont.render("Medium", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMFont.set_underline(True)``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "Medium"``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 30``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMtFont = MEDIUMFont.render("Medium", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMFont.set_underline(False)``

``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 165 and Mx <= 205:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ HIGHFontText = HIGHFont.render("High", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ ¬ HIGHFont.set_underline(True)``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "High"``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 60``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ HIGHFontText = HIGHFont.render("High", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ ¬ HIGHFont.set_underline(False)``

``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 215 and Mx <= 300:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEtFont = ADAPTIVEFont.render("Adaptive", self.aa, self.AccentCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEFont.set_underline(True)``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "Adaptive"``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = (self.mod_Psutil__.cpu_freq(percpu=True)[0][2])/35``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if (self.mod_Psutil__.cpu_freq(percpu=True)[0][2])/10 > 300 and self.mod_Psutil__.virtual_memory().total > 8589934592:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif (self.mod_Psutil__.cpu_freq(percpu=True)[0][2]) > 200 and self.mod_Psutil__.virtual_memory().total > 4294967296:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif (self.mod_Psutil__.cpu_freq(percpu=True)[0][2]) > 100 and self.mod_Psutil__.virtual_memory().total > 2147483648:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif (self.mod_Psutil__.cpu.freq(percpu=True)[0][2]) < 100 and (self.mod_Psutil__.cpu.freq(percpu=True)[0][2]) > 75 and self.mod_Psutil__.virtual_memory().total > 1073741824:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEtFont = ADAPTIVEFont.render("Adaptive", self.aa, self.FontCol)``
``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEFont.set_underline(False)``

``¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSFont, (0, 150+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(FOVFont, (0, 200+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(CamRotFont, (0, 250+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(ModeFont, (0, 85+scroll)) ``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(LOWtFont, (48, 85+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(MEDIUMtFont, (90, 85+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(HIGHFontText, (165, 85+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(ADAPTIVEtFont, (215, 85+scroll)) ``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(AAFont, (0, 300+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(RenderFogFont, (0, 350+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(FancySkyFont, (0, 400+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(FancyParticleFont, (0, 450+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundFont, (0, 500+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundVoltFont, (0, 550+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicFont, (0, 600+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicVoltFont, (0, 650+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(ThemeFont, (0, 65+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(LightTheme, (55, 65+scroll))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(DarkTheme, (95, 65+scroll))``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (int(self.FPS+45)*xScaleFact, 185+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (int(self.FOV*5)*xScaleFact, 235+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 6)``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 100)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(titletFont, ((realWidth-TitleWidth)/2, 0))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont, (((realWidth-TitleWidth)/2)+55, 50))``


``¬ ¬ ¬ ¬ ¬ if realHeight <= 760:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, slider_Rect, 0)``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ scroll = 50``

``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
``¬ ¬ ¬ ¬ ¬ if not Message == None:``
``¬ ¬ ¬ ¬ ¬ ¬ return Message``

``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip() ``
``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_ShareDataUtil>")``
   ``¬ class Share:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def initialize(Data): ``
``¬ ¬ ¬ global Class_Startup_variables``
``¬ ¬ ¬ Class_Startup_variables = Data``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_SoundUtils>")``
   ``¬ class PlaySound:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def PlayClickSound(self):``
``¬ ¬ ¬ channel1 = self.mod_Pygame__.mixer.Channel(0)``
``¬ ¬ ¬ clickMUSIC = self.mod_Pygame__.mixer.Sound(file=self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``
``¬ ¬ ¬ channel1.set_volume(self.soundVOL/100)``
``¬ ¬ ¬ channel1.play(clickMUSIC)``
``¬ ¬ ¬ self.mod_Pygame__.time.wait(40)``

``¬ ¬ def PlayFootstepsSound(self):``
``¬ ¬ ¬ channel2 = self.mod_Pygame__.mixer.Channel(1)``
``¬ ¬ ¬ Footsteps = self.mod_Pygame__.mixer.Sound(self.mod_OS__.path.join(self.base_folder, (f"Resources\\G3_Resources\\GameSounds\\footsteps{self.mod_Random__.randint(0, 5)}.wav")))``
``¬ ¬ ¬ channel2.set_volume(self.soundVOL/100)``
``¬ ¬ ¬ channel2.play(Footsteps)``


``¬ ¬ def PlayInvSound(self):``
``¬ ¬ ¬ channel3 = self.mod_Pygame__.mixer.Channel(2)``
``¬ ¬ ¬ InvGen = self.mod_Pygame__.mixer.Sound(file=self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\InventoryGeneral.wav")))``
``¬ ¬ ¬ channel3.set_volume(self.musicVOL/100)``
``¬ ¬ ¬ channel3.play(InvGen)``


``¬ ¬ def PlayAmbientSound(self):``
``¬ ¬ ¬ channel4 = self.mod_Pygame__.mixer.Channel(3)``
``¬ ¬ ¬ LoadAmb = self.mod_Pygame__.mixer.Sound(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\GameSounds\\FieldAmb.wav")))``
``¬ ¬ ¬ channel4.set_volume(self.soundVOL/100)``
``¬ ¬ ¬ channel4.play(LoadAmb)``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_StartupAnimation>")``
   ``¬ class GenerateStartupScreen:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def Start(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Welcome")``
``¬ ¬ ¬ ¬ PresentsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
``¬ ¬ ¬ ¬ PycraftFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
``¬ ¬ ¬ ¬ NameFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 45)``

``¬ ¬ ¬ ¬ NameText = NameFont.render("Tom Jebbo", True, self.FontCol)``
``¬ ¬ ¬ ¬ NameTextWidth = NameText.get_width()``
``¬ ¬ ¬ ¬ NameTextHeight = NameText.get_height()``

``¬ ¬ ¬ ¬ PresentsText = PresentsFont.render("presents", True, self.FontCol)``

``¬ ¬ ¬ ¬ PycraftText = PycraftFont.render("Pycraft", True, self.FontCol)``
``¬ ¬ ¬ ¬ PycraftTextWidth = PycraftText.get_width()``
``¬ ¬ ¬ ¬ PycraftTextHeight = PycraftText.get_height()``

``¬ ¬ ¬ ¬ iteration = 0``
``¬ ¬ ¬ ¬ clock = self.mod_Pygame__.time.Clock()``
``¬ ¬ ¬ ¬ if self.RunFullStartup == True:``
``¬ ¬ ¬ ¬ ¬ while iteration <= (60*3):``
``¬ ¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(NameText, ((self.realWidth-NameTextWidth)/2, (self.realHeight-NameTextHeight)/2))``
``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``

``¬ ¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
``¬ ¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ clock.tick(60)``
``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``
``¬ ¬ ¬ ¬ ¬ iteration = 0``

``¬ ¬ ¬ ¬ ¬ while iteration <= (60*2):``
``¬ ¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(NameText, ((self.realWidth-NameTextWidth)/2, (self.realHeight-NameTextHeight)/2))``
``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(PresentsText, ((((self.realWidth-NameTextWidth)/2)+120), ((self.realHeight-NameTextHeight)/2)+30))``
``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``

``¬ ¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
``¬ ¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ ¬ clock.tick(60)``
``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``

``¬ ¬ ¬ ¬ ¬ iteration = 0``

``¬ ¬ ¬ ¬ while iteration <= (60*3):``
``¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftText, ((self.realWidth-PycraftTextWidth)/2, (self.realHeight-PycraftTextHeight)/2))``
``¬ ¬ ¬ ¬ ¬ iteration += 1``

``¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
``¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ clock.tick(60)``
``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``

``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``

``¬ ¬ ¬ ¬ y = 0``
``¬ ¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftText, ((self.realWidth-PycraftTextWidth)/2, ((self.realHeight-PycraftTextHeight)/2)-y))``
``¬ ¬ ¬ ¬ ¬ y += 2``

``¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
``¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
``¬ ¬ ¬ ¬ ¬ clock.tick(60)``
``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``

``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``
``¬ ¬ ¬ ¬ ¬ if ((self.realHeight-PycraftTextHeight)/2)-y <= 0:``
``¬ ¬ ¬ ¬ ¬ ¬ self.RunFullStartup = False``
``¬ ¬ ¬ ¬ ¬ ¬ return None``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ self.RunFullStartup = False``
``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_TextUtils>")``
   ``¬ class GenerateText:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def LoadQuickText(self):``
``¬ ¬ ¬ LoadingText = ["Use W,A,S,D to move", "Use W to move forward", "Use S to move backward", "Use A to move left", "Use D to move right", "Access your inventory with E", "Access your map with R", "Use SPACE to jump", "Did you know there is a light mode?", "Did you know there is a dark mode?", "Check us out on GitHub", "Use ESC to remove camera movement", "Hold W to sprint", "Did you know you can change the sound volume in settings?", "Did you know you can change the music volume in settings?", "Did you know you can use L to lock the camera"]``
``¬ ¬ ¬ locat = self.mod_Random__.randint(0, (len(LoadingText)-1))``
``¬ ¬ ¬ text = LoadingText[locat]``
``¬ ¬ ¬ return text``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_ThemeUtils>")``
   ``¬ class DetermineThemeColours:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def GetColours(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ self.themeArray = [[(255, 255, 255), [30, 30, 30], (80, 80, 80), (237, 125, 49), (255, 255, 255)], [(0, 0, 0), [255, 255, 255], (80, 80, 80), (237, 125, 49), (100, 100, 100)]]``
``¬ ¬ ¬ ¬ if self.theme == "dark":``
``¬ ¬ ¬ ¬ ¬ self.FontCol = self.themeArray[0][0]``
``¬ ¬ ¬ ¬ ¬ self.BackgroundCol = self.themeArray[0][1]``
``¬ ¬ ¬ ¬ ¬ self.ShapeCol = self.themeArray[0][2]``
``¬ ¬ ¬ ¬ ¬ self.AccentCol = self.themeArray[0][3]``
``¬ ¬ ¬ ¬ ¬ self.SecondFontCol = self.themeArray[0][4]``
``¬ ¬ ¬ ¬ elif self.theme == "light":``
``¬ ¬ ¬ ¬ ¬ self.FontCol = self.themeArray[1][0]``
``¬ ¬ ¬ ¬ ¬ self.BackgroundCol = self.themeArray[1][1]``
``¬ ¬ ¬ ¬ ¬ self.ShapeCol = self.themeArray[1][2]``
``¬ ¬ ¬ ¬ ¬ self.AccentCol = self.themeArray[1][3]``
``¬ ¬ ¬ ¬ ¬ self.SecondFontCol = self.themeArray[1][4]``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ return Message``


``¬ ¬ def GetThemeGUI(self):``
``¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ clock = self.mod_Pygame__.time.Clock()``
``¬ ¬ ¬ ¬ TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
``¬ ¬ ¬ ¬ Title = TitleFont.render("Pycraft", True, (255, 255, 255))``
``¬ ¬ ¬ ¬ MiddleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
``¬ ¬ ¬ ¬ DarkModeFont = MiddleFont.render("Dark", True, (255, 255, 255))``
``¬ ¬ ¬ ¬ LightModeFont = MiddleFont.render("Light", True, (255, 255, 255))``
``¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ while self.theme == False:``
``¬ ¬ ¬ ¬ ¬ self.Display.fill([30, 30, 30])``
``¬ ¬ ¬ ¬ ¬ mX, mY = self.mod_Pygame__.mouse.get_pos()``
``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True``
``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONUP:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(Title, (540, 0))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(DarkModeFont, (320, 360))``
``¬ ¬ ¬ ¬ ¬ self.Display.blit(LightModeFont, (890, 360))``
``¬ ¬ ¬ ¬ ¬ DarkRect = self.mod_Pygame__.Rect(260, 300, 200, 160)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (80, 80, 80), DarkRect, 3)``
``¬ ¬ ¬ ¬ ¬ LightRect = self.mod_Pygame__.Rect(820, 300, 200, 160)``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (80, 80, 80), LightRect, 3)``
``¬ ¬ ¬ ¬ ¬ if mX >= 260 and mX <= 460 and mY >= 300 and mY <= 460:``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "dark"``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.base_folder = self.mod_OS__.path.dirname(__file__)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.set_volume(50)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.play()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ elif mX >= 820 and mX <= 980 and mY >= 300 and mY <= 460:``
``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "light"``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.base_folder = self.mod_OS__.path.dirname(__file__)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.set_volume(50)``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.play()``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``
``¬ ¬ ¬ ¬ ¬ clock.tick(60)``
``¬ ¬ ¬ except Exception as Message:``
``¬ ¬ ¬ ¬ Message = str(Message)+" in <Pycraft_ThemeUtils>"``
``¬ ¬ ¬ ¬ return Message``

``¬ ¬ ¬ return None``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_ThreadingUtils>")``
   ``¬ class ThreadingUtils:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def StartVariableChecking(self):``
``¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ if self.Iteration > 1000:``
``¬ ¬ ¬ ¬ ¬ self.aFPS = (self.aFPS/self.Iteration)``
``¬ ¬ ¬ ¬ ¬ self.Iteration = 1``
``¬ ¬ ¬ ¬ self.FPS = int(self.FPS)``
``¬ ¬ ¬ ¬ self.eFPS = int(self.eFPS)``

``¬ ¬ ¬ ¬ self.mod_Time__.sleep(1)``

``¬ ¬ ¬ ¬ if self.Stop_Thread_Event.is_set():``
``¬ ¬ ¬ ¬ ¬ break``
``¬ ¬ ``
``¬ ¬ def StartCPUlogging(self):``
``¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ if self.Devmode == 10:``
``¬ ¬ ¬ ¬ ¬ if self.Timer >= 2:``
``¬ ¬ ¬ ¬ ¬ ¬ CPUPercent = self.mod_Psutil__.cpu_percent(0.2)``
``¬ ¬ ¬ ¬ ¬ ¬ if CPUPercent > self.Data_CPUUsE_Max:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = CPUPercent``
``¬ ¬ ¬ ¬ ¬ ¬ elif CPUPercent < self.Data_CPUUsE_Min:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = CPUPercent``

``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE.append([((self.realWidth/2)+100)+(self.Timer-2), 200-(100/self.Data_CPUUsE_Max)*CPUPercent])``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(0.2)``
``¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(1)``

``¬ ¬ ¬ ¬ if self.Stop_Thread_Event.is_set():``
``¬ ¬ ¬ ¬ ¬ break``

``¬ ¬ def AdaptiveMode(self):``
``¬ ¬ ¬ while True:``
``¬ ¬ ¬ ¬ if self.Stop_Thread_Event.is_set():``
``¬ ¬ ¬ ¬ ¬ break``
``¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ if self.SettingsPreference == "Adaptive":``
``¬ ¬ ¬ ¬ ¬ CPUPercent = self.mod_Psutil__.cpu_percent()``
``¬ ¬ ¬ ¬ ¬ CoreCount = self.mod_Psutil__.cpu_count()``

``¬ ¬ ¬ ¬ ¬ try:``
``¬ ¬ ¬ ¬ ¬ ¬ gpus = self.mod_GPUtil__.getGPUs()``

``¬ ¬ ¬ ¬ ¬ ¬ GPUPercent = 0``
``¬ ¬ ¬ ¬ ¬ ¬ NumOfGPUs = 0``

``¬ ¬ ¬ ¬ ¬ ¬ for gpu in gpus:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ NumOfGPUs += 1``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ GPUPercent += gpu.load*100``

``¬ ¬ ¬ ¬ ¬ ¬ GPUPercent = GPUPercent/NumOfGPUs``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ except:``
``¬ ¬ ¬ ¬ ¬ ¬ GPUPercent = CPUPercent``

``¬ ¬ ¬ ¬ ¬ if (CPUPercent >= (100/CoreCount)) and (GPUPercent >= (100/CoreCount)):``
``¬ ¬ ¬ ¬ ¬ ¬ self.FPS -= 10``
``¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ if self.FPS < self.RecommendedFPS:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS += 10``
``¬ ¬ ¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not (self.FPS == self.RecommendedFPS):``
``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS -= 1``
``¬ ¬ ¬ ¬ ¬ ``
``¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(0.2)``
``¬ ¬ ¬ ¬ else:``
``¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(1)``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``


.. note::
    For information on this consult the above guide
   ``if not __name__ == "__main__":``
   ``¬ print("Started <Pycraft_TkinterUtils>")``
   ``¬ class TkinterInfo:``
   ``¬ ¬ def __init__(self):``
   ``¬ ¬ ¬ pass``

``¬ ¬ def CreateTkinterWindow(self):``
``¬ ¬ ¬ DataWindow = self.mod_Tkinter__tk.Tk()``
``¬ ¬ ¬ DataWindow.title("Player Information")``
``¬ ¬ ¬ DataWindow.configure(width = 500, height = 300) ``
``¬ ¬ ¬ DataWindow.configure(bg="lightblue") ``
``¬ ¬ ¬ VersionData = f"Pycraft: v{self.version}"``
``¬ ¬ ¬ CoordinatesData = f"Coordinates: x: {self.X} y: {self.Y} z: {self.Z} Facing: 0.0, 0.0, 0.0" ``
``¬ ¬ ¬ FPSData = f"FPS: Actual: {self.eFPS} Max: {self.FPS}" ``
``¬ ¬ ¬ VersionData = self.mod_Tkinter__tk.Label(DataWindow, text=VersionData) ``
``¬ ¬ ¬ CoordinatesData = self.mod_Tkinter__tk.Label(DataWindow, text=CoordinatesData) ``
``¬ ¬ ¬ FPSData = self.mod_Tkinter__tk.Label(DataWindow, text=FPSData) ``
``¬ ¬ ¬ VersionData.grid(row = 0, column = 0, columnspan = 2) ``
``¬ ¬ ¬ CoordinatesData.grid(row = 1, column = 0, columnspan = 2)``
``¬ ¬ ¬ FPSData.grid(row = 2, column = 0, columnspan = 2)``
``¬ ¬ ¬ DataWindow.mainloop() ``
``¬ ¬ ¬ DataWindow.quit()``

.. note::
    For information on this consult the above guide
   ``else:``
   ``¬ print("You need to run this as part of Pycraft")``
   ``¬ import tkinter as tk``
   ``¬ from tkinter import messagebox``
   ``¬ root = tk.Tk()``
   ``¬ root.withdraw()``
   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   ``¬ quit()``