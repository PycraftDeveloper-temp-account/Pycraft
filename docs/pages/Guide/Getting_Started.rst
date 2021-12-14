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
* Subroutines should avoid using global variables as much as possible, as this makes it easier to trace variables and possible bugs. (The exceptions here being the``Class_Startup_variables`` and ``self`` variables which are referenced throughout the different modules for Pycraft).
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

* All errors should be -where possible- stored in the variable``message``.

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

1. ``if not __name__ == "__main__":`` This checks to see if the place its called from (stored in the variable``__name__``) is not ``"__main__"``. The string ``"__main__"`` would be the data stored in the variable``__name__`` if the project was run on its own, which in this case we don't want so we only allow the code inside the if-statement to run if the data in ``__name__`` is not ``"__main__"``.
2. ``¬ print("Started <Pycraft_<name>>")`` Now we output data to the terminal if the program is running, this allows us to know if there are any errors preventing this module from loading, in which case the program would crash before that is outputted to the terminal, making us aware the error is in this module.
3. ``¬ class <name>:`` Now we are defining a class with a suitable name that represents what the subroutines in this class do; this allows us to group up our code to make it easier to edit, organise and debug later on, as well as saving on memory as not every function will need to be loaded at once.
4. ``¬ ¬ def __init__(self):`` Here we make sure the module is initialized correctly we do this because if we tried to call this standalone, and without the code that would stop this, then all references to variables and subroutines outside of this project would be invalid and cause issues. This is also where the variable 'self' is defined for all references in this class. This subroutine is a procedure, so does not return a value.
5. ``¬ ¬ ¬ pass`` Now we only put code in the``__init__`` procedure in some situations, like for example in ``GameEngine.py`` and ``main.py``, which is where the code that would go in this procedure is called, reducing the number of  the project uses.

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
3. ``¬ import tkinter as tk`` Now we are importing the tkinter module into the project, all code here must be standalone and not rely on code in other modules in the project, this way the project can be taken apart and this should still work. We store he imported module, "Tkinter" with the name``tk``, this shortens length and all references to "Tkinter" from how on in this indented block will use this name.
4. ``¬ from tkinter import messagebox`` Here we are importing specific sections of "Tkinter", in this case; ``messagebox``, this module allows us to make dialogue boxes that are commonplace in Windows and Apple based devices.
5. ``¬ root = tk.Tk()`` This of code is required to make the dialogue box, which is what we want. This will create a window to the default size "Tkinter" has defined, and initialises the``messagebox`` module, which we want.
6. ``¬ root.withdraw()`` We use this code to hide the window that appears by using the previous  ``root`` is the internal name for the window, as that is what the window created in the previous was stored in (as a variable).
7. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")`` Here we make our all to the``messagebox`` module, which has several pre-made dialogue boxes, we are using the``showerror`` pre-made dialogue box procedure here. We give it the caption of ``"Startup Fail"``, and then elaborate on the issue in the main body of the window, by displaying the text ``"You need to run this as part of Pycraft, please run the 'main.py' file"``.
8. ``¬ quit()`` This is Python's way of closing the project, we normally use``sys.exit`` for this, which you will see later on, because its  a bit cleaner on some IDLE's and terminals. However to reduce the length of this project, we use the built in function here instead.

Achievements
====================
Overview
++++++++++++++++++++
This module controls the displaying and processing of in-game achievements: This feature will be expanded upon when achievements are added and you can earn them in game.

The``GenerateAchievements`` class controls the rendering of the achievements GUI this can be accessed from the 'home screen' of Pycraft, currently this class only renders a blank window, which is coloured and has a title [Pycraft] and header [Achievements], but expect an update here when its possible to earn achievements in game!

The``Achievements(self)`` function, like most subroutines in Pycraft, takes``self`` to be its only input. It will return only an error, should one arise, which will be stored in the``messages`` variable. This subroutine is where the bulk of the processing for this class is done, this subroutine is responsible for the Achievements GUI which you can access through Pycraft's home screen.

Detailed Breakdown
++++++++++++++++++++


.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_Achievements>")``
        3: ``¬ class GenerateAchievements:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def Achievements(self):``

7: ``¬ ¬ ¬ try:``

8: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

9: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

10: ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")``

11: ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``

12: ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``

13: ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``


14: ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``

15: ``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``


16: ``¬ ¬ ¬ ¬ AchievementsFont = InfoTitleFont.render("Achievements", self.aa, self.SecondFontCol)``

17: ``¬ ¬ ¬ ¬ tempFPS = self.FPS``


18: ``¬ ¬ ¬ ¬ while True:``

19: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``


20: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``

21: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``

22: ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``

23: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``


24: ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``

25: ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``

26: ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``


27: ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``


28: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

29: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``

30: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

31: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

32: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``

33: ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:``

34: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:``

35: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``

36: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``

37: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``

38: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``

39: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``

40: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``

41: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``


42: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")``


43: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``


44: ``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``

45: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``

46: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``

47: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))``


48: ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``

49: ``¬ ¬ ¬ ¬ ¬ if not Message == None:``

50: ``¬ ¬ ¬ ¬ ¬ ¬ return Message``

51: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

52: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``

53: ``¬ ¬ ¬ except Exception as Message:``

54: ``¬ ¬ ¬ ¬ return Message``

55: ``else:``
56: ``¬ print("You need to run this as part of Pycraft")``
57: ``¬ import tkinter as tk``
58: ``¬ from tkinter import messagebox``
59: ``¬ root = tk.Tk()``
60: ``¬ root.withdraw()``
61: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
62: ``¬ quit()``


1: ``# Skip Indenting the start of this in documentation``



.. note::
   For information on this consult the above guide
        2: ``if not __name__ == "__main__":``
        3: ``print("Started <Pycraft_Base>")``

4: ``¬ print("Started <Pycraft_Base>")``


5: ``¬ import moderngl_window as mglw``

6: ``¬ from moderngl_window.scene.camera import KeyboardCamera, OrbitCamera``



7: ``¬ class CameraWindow(mglw.WindowConfig):``

8: ``¬ ¬ """Base class with built in 3D camera support"""``


9: ``¬ ¬ def __init__(self, **kwargs):``

10: ``¬ ¬ ¬ super().__init__(**kwargs)``

11: ``¬ ¬ ¬ self.camera = KeyboardCamera(self.wnd.keys, aspect_ratio=self.wnd.aspect_ratio)``

12: ``¬ ¬ ¬ self.camera_enabled = True``


13: ``¬ ¬ def key_event(self, key, action, modifiers):``

14: ``¬ ¬ ¬ keys = self.wnd.keys``


15: ``¬ ¬ ¬ if self.camera_enabled:``

16: ``¬ ¬ ¬ ¬ self.camera.key_input(key, action, modifiers)``


17: ``¬ ¬ ¬ if action == keys.ACTION_PRESS:``

18: ``¬ ¬ ¬ ¬ if key == keys.C:``

19: ``¬ ¬ ¬ ¬ ¬ self.camera_enabled = not self.camera_enabled``

20: ``¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = self.camera_enabled``

21: ``¬ ¬ ¬ ¬ ¬ self.wnd.cursor = not self.camera_enabled``

22: ``¬ ¬ ¬ ¬ if key == keys.SPACE:``

23: ``¬ ¬ ¬ ¬ ¬ self.timer.toggle_pause()``


24: ``¬ ¬ def mouse_position_event(self, x: int, y: int, dx, dy):``

25: ``¬ ¬ ¬ if self.camera_enabled:``

26: ``¬ ¬ ¬ ¬ self.camera.rot_state(-dx, -dy)``


27: ``¬ ¬ def resize(self, width: int, height: int):``

28: ``¬ ¬ ¬ self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)``



29: ``¬ class OrbitCameraWindow(mglw.WindowConfig):``

30: ``¬ ¬ """Base class with built in 3D orbit camera support"""``


31: ``¬ ¬ def __init__(self, **kwargs):``

32: ``¬ ¬ ¬ super().__init__(**kwargs)``

33: ``¬ ¬ ¬ self.camera = OrbitCamera(aspect_ratio=self.wnd.aspect_ratio)``

34: ``¬ ¬ ¬ self.camera_enabled = True``


35: ``¬ ¬ def key_event(self, key, action, modifiers):``

36: ``¬ ¬ ¬ keys = self.wnd.keys``


37: ``¬ ¬ ¬ if action == keys.ACTION_PRESS:``

38: ``¬ ¬ ¬ ¬ if key == keys.C:``

39: ``¬ ¬ ¬ ¬ ¬ self.camera_enabled = not self.camera_enabled``

40: ``¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = self.camera_enabled``

41: ``¬ ¬ ¬ ¬ ¬ self.wnd.cursor = not self.camera_enabled``

42: ``¬ ¬ ¬ ¬ if key == keys.SPACE:``

43: ``¬ ¬ ¬ ¬ ¬ self.timer.toggle_pause()``


44: ``¬ ¬ def mouse_position_event(self, x: int, y: int, dx, dy):``

45: ``¬ ¬ ¬ if self.camera_enabled:``

46: ``¬ ¬ ¬ ¬ self.camera.rot_state(dx, dy)``


47: ``¬ ¬ def mouse_scroll_event(self, x_offset: float, y_offset: float):``

48: ``¬ ¬ ¬ if self.camera_enabled:``

49: ``¬ ¬ ¬ ¬ self.camera.zoom_state(y_offset)``


50: ``¬ ¬ def resize(self, width: int, height: int):``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_Benchmark>")``
        3: ``¬ class GenerateBenchmarkMenu:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def Benchmark(self):``

7: ``¬ ¬ ¬ try:``

8: ``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).pause()``

9: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

10: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

11: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark")``

12: ``¬ ¬ ¬ ¬ self.VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

13: ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``

14: ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``

15: ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

16: ``¬ ¬ ¬ ¬ DetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``

17: ``¬ ¬ ¬ ¬ InfoDetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

18: ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``

19: ``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``


20: ``¬ ¬ ¬ ¬ BenchmarkFont = InfoTitleFont.render("Benchmark", self.aa, self.SecondFontCol)``

21: ``¬ ¬ ¬ ¬ FPSinfoTEXT = DetailsFont.render("FPS benchmark results", self.aa, self.FontCol)``

22: ``¬ ¬ ¬ ¬ FPSinfoTEXTWidth = FPSinfoTEXT.get_width()``

23: ``¬ ¬ ¬ ¬ FILEinfoTEXT = DetailsFont.render("Read test results", self.aa, self.FontCol)``

24: ``¬ ¬ ¬ ¬ FILEinfoTEXTWidth = FILEinfoTEXT.get_width()``

25: ``¬ ¬ ¬ ¬ HARDWAREinfoTEXT = DetailsFont.render("Hardware results", self.aa, self.FontCol)``

26: ``¬ ¬ ¬ ¬ HARDWAREinfoTEXTwidth = HARDWAREinfoTEXT.get_width()``


27: ``¬ ¬ ¬ ¬ SixtyFPSData = DataFont.render("60 Hz", self.aa, self.AccentCol)``

28: ``¬ ¬ ¬ ¬ OneFourFourFPSData = DataFont.render("144 Hz", self.aa, self.AccentCol)``

29: ``¬ ¬ ¬ ¬ TwoFortyFPSData = DataFont.render("240 Hz", self.aa, self.AccentCol)``


30: ``¬ ¬ ¬ ¬ InfoFont1 = DataFont.render("Welcome to Benchmark mode, press the SPACE bar to continue or press ANY other key to cancel, or press 'X'", self.aa, self.FontCol)``

31: ``¬ ¬ ¬ ¬ InfoFont2 = DataFont.render("Benchmark mode is used to make the 'ADAPTIVE' feature in settings function and also to give an indication of the experience you are likely to get on this device", self.aa, self.FontCol)``

32: ``¬ ¬ ¬ ¬ InfoFont3 = DataFont.render("Benchmark mode consists of several stages:", self.aa, self.FontCol)``

33: ``¬ ¬ ¬ ¬ InfoFont4 = DataFont.render("First it will gather some basic information about your system", self.aa, self.FontCol)``

34: ``¬ ¬ ¬ ¬ InfoFont5 = DataFont.render("Then it will test your maximum frame rate on a blank screen, then with a basic animation, and finally in a 3D OpenGL space", self.aa, self.FontCol)``

35: ``¬ ¬ ¬ ¬ InfoFont6 = DataFont.render("After its done that the focus moves on to a quick storage test, before finishing", self.aa, self.FontCol)``

36: ``¬ ¬ ¬ ¬ InfoFont7 = DataFont.render("Your results will then be displayed on screen with your frame rate scores on a line graph and the rest detailed to the right", self.aa, self.FontCol)``

37: ``¬ ¬ ¬ ¬ InfoFont8 = DataFont.render("During the time the benchmark is running the window may appear unresponsive, don't panic this can be expected.", self.aa, self.FontCol)``

38: ``¬ ¬ ¬ ¬ InfoFont9 = DataFont.render("In addition to achieve the best scores try to avoid doing anything else on the computer whilst the benchmark runs", self.aa, self.FontCol)``

39: ``¬ ¬ ¬ ¬ InfoFont10 = DataFont.render("This benchmark may show some system instability or cause your device to get warm, you use this at your own risk!", self.aa, (255, 0, 0))``


40: ``¬ ¬ ¬ ¬ stage = 0``


41: ``¬ ¬ ¬ ¬ resize = False``


42: ``¬ ¬ ¬ ¬ while True:``

43: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``


44: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``

45: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``

46: ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``

47: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``


48: ``¬ ¬ ¬ ¬ ¬ if stage == 0:``

49: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

50: ``¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``

51: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``

52: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``

53: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))``

54: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont1, (3, 100))``

55: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont2, (3, 130))``

56: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont3, (3, 145))``

57: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont4, (3, 160))``

58: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont5, (3, 175))``

59: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont6, (3, 190))``

60: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont7, (3, 220))``

61: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont8, (3, 235))``

62: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont9, (3, 250))``

63: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont10, (3, 280))``


64: ``¬ ¬ ¬ ¬ ¬ if stage == 1:``

65: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Getting System Information")``

66: ``¬ ¬ ¬ ¬ ¬ ¬ CPUid = f"{self.mod_CPUinfo__.get_cpu_info()['brand_raw']} w/{self.mod_Psutil__.cpu_count(logical=False)} cores @ {self.mod_Psutil__.cpu_freq().max} MHz"``

67: ``¬ ¬ ¬ ¬ ¬ ¬ RAMid = f"{round((((self.mod_Psutil__.virtual_memory().total)/1000)/1000/1000),2)} GB of memory, with {self.mod_Psutil__.virtual_memory().percent}% used"``

68: ``¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFO = DataFont.render(CPUid, self.aa, (255, 255, 255))``

69: ``¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFOwidth = CPUhwINFO.get_width()``


70: ``¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFO = DataFont.render(RAMid, self.aa, (255, 255, 255))``

71: ``¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFOwidth = RAMhwINFO.get_width()``

72: ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``


73: ``¬ ¬ ¬ ¬ ¬ if stage == 2:``

74: ``¬ ¬ ¬ ¬ ¬ ¬ try:``

75: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3 = self.mod_ExBenchmark__.LoadBenchmark.run(self)``

76: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:``

77: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message``

78: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``

79: ``¬ ¬ ¬ ¬ ¬ ¬ except:``

80: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Cancelled benchmark")``

81: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``

82: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

83: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Finished self.FPS based benchmarks")``

84: ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``


85: ``¬ ¬ ¬ ¬ ¬ if stage == 3:``

86: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Starting disk read test")``

87: ``¬ ¬ ¬ ¬ ¬ ¬ ReadIteration = 50``

88: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(ReadIteration):``

89: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:``

90: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Benchdata = Bench.read()``


91: ``¬ ¬ ¬ ¬ ¬ ¬ aTime = 0``

92: ``¬ ¬ ¬ ¬ ¬ ¬ ReadIteration = 50``

93: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(ReadIteration):``

94: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ start = self.mod_Time__.perf_counter()``

95: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:``

96: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Benchdata = Bench.read()``

97: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ aTime += self.mod_Time__.perf_counter()-start``

98: ``¬ ¬ ¬ ¬ ¬ ¬ aTime = aTime/(ReadIteration+1)``

99: ``¬ ¬ ¬ ¬ ¬ ¬ ReadSpeed = (1/(aTime))``

100: ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``


101: ``¬ ¬ ¬ ¬ ¬ if stage == 4:``

102: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results.")``

103: ``¬ ¬ ¬ ¬ ¬ ¬ Max1 = 0``

104: ``¬ ¬ ¬ ¬ ¬ ¬ Min1 = 60``

105: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):``

106: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY[i] > Max1:``

107: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max1 = FPSlistY[i]``

108: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY[i] < Min1:``

109: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min1 = FPSlistY[i]``


110: ``¬ ¬ ¬ ¬ ¬ ¬ Max2 = 0``

111: ``¬ ¬ ¬ ¬ ¬ ¬ Min2 = 60``

112: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``

113: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY2[i] > Max2:``

114: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max2 = FPSlistY2[i]``

115: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY2[i] < Min2:``

116: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min2 = FPSlistY2[i]``


117: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results..")``

118: ``¬ ¬ ¬ ¬ ¬ ¬ Max3 = 0``

119: ``¬ ¬ ¬ ¬ ¬ ¬ Min3 = 60``

120: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY3)):``

121: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY3[i] > Max3:``

122: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max3 = FPSlistY3[i]``

123: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY3[i] < Min3:``

124: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min3 = FPSlistY3[i]``


125: ``¬ ¬ ¬ ¬ ¬ ¬ if Max2 > Max1:``

126: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max2``

127: ``¬ ¬ ¬ ¬ ¬ ¬ elif Max3 > Max2:``

128: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max3``

129: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

130: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max1``


131: ``¬ ¬ ¬ ¬ ¬ ¬ self.RecommendedFPS = GlobalMax/2``


132: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results...")``

133: ``¬ ¬ ¬ ¬ ¬ ¬ multiplier = len(FPSlistY)/(realWidth-20)``

134: ``¬ ¬ ¬ ¬ ¬ ¬ temp = []``

135: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):``

136: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY[i])))``

137: ``¬ ¬ ¬ ¬ ¬ ¬ FPSListY = temp``


138: ``¬ ¬ ¬ ¬ ¬ ¬ temp = []``

139: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``

140: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY2[i])))``

141: ``¬ ¬ ¬ ¬ ¬ ¬ FPSListY2 = temp``


142: ``¬ ¬ ¬ ¬ ¬ ¬ temp = []``

143: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``

144: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY3[i])))``

145: ``¬ ¬ ¬ ¬ ¬ ¬ FPSListY3 = temp``


146: ``¬ ¬ ¬ ¬ ¬ ¬ Results1 = []``

147: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):``

148: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results1.append([(FPSlistX[i]/multiplier), FPSListY[i]])``


149: ``¬ ¬ ¬ ¬ ¬ ¬ Results2 = []``

150: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``

151: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results2.append([(FPSlistX2[i]/multiplier), FPSListY2[i]])``


152: ``¬ ¬ ¬ ¬ ¬ ¬ Results3 = []``

153: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY3)):``

154: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results3.append([(FPSlistX3[i]/multiplier), FPSListY3[i]])``


155: ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``


156: ``¬ ¬ ¬ ¬ ¬ if stage == 5:``

157: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Results")``


158: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``


159: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``

160: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))``


161: ``¬ ¬ ¬ ¬ ¬ ¬ FPSRect = self.mod_Pygame__.Rect(10, 130, realWidth-20, 300)``

162: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FPSRect, 0)``


163: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*60)))), (realWidth-20, int(130+(300-((300/GlobalMax)*60)))))``

164: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SixtyFPSData, (13, int(130+(300-((300/GlobalMax)*60)))))``


165: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*144)))), (realWidth-20, int(130+(300-((300/GlobalMax)*144)))))``

166: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(OneFourFourFPSData, (13, int(130+(300-((300/GlobalMax)*140)))))``


167: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*240)))), (realWidth-20, int(130+(300-((300/GlobalMax)*240)))))``

168: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TwoFortyFPSData, (13, int(130+(300-((300/GlobalMax)*240)))))``


169: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 255, 0), False, Results1)``

170: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 0, 255), False, Results2)``

171: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 0), False, Results3)``


172: ``¬ ¬ ¬ ¬ ¬ ¬ HideRect = self.mod_Pygame__.Rect(0, 110, realWidth, 330)``

173: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.BackgroundCol, HideRect, 20)``


174: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSinfoTEXT, ((realWidth-FPSinfoTEXTWidth)-3, 100))``

175: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FILEinfoTEXT, ((realWidth-FILEinfoTEXTWidth)-3, 430))``


176: ``¬ ¬ ¬ ¬ ¬ ¬ FileResults = DataFont.render(f"Your device achieved a score of: {round(ReadSpeed, 2)}/100 ({round((100/100)*ReadSpeed)}%)", self.aa, self.FontCol)``

177: ``¬ ¬ ¬ ¬ ¬ ¬ FileResultsWidth = FileResults.get_width()``

178: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FileResults, ((realWidth-FileResultsWidth)-3, 460))``


179: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(HARDWAREinfoTEXT, ((realWidth-HARDWAREinfoTEXTwidth)-3, 480))``


180: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CPUhwINFO, ((realWidth-CPUhwINFOwidth)-3, 500))``

181: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(RAMhwINFO, ((realWidth-RAMhwINFOwidth)-3, 516))``


182: ``¬ ¬ ¬ ¬ ¬ ¬ GreenInfo = InfoDetailsFont.render(f"Blank screen test (green); Minimum: {round(Min1, 4)} FPS, Maximum: {round(Max1, 4)} FPS", self.aa, self.FontCol)``

183: ``¬ ¬ ¬ ¬ ¬ ¬ BlueInfo = InfoDetailsFont.render(f"Drawing test (blue); Minimum: {round(Min2, 4)} FPS, Maximum: {round(Max2, 4)} FPS", self.aa, self.FontCol)``

184: ``¬ ¬ ¬ ¬ ¬ ¬ RedInfo = InfoDetailsFont.render(f"OpenGL test (red); Minimum: {round(Min3, 4)} FPS, Maximum: {round(Max3, 4)} FPS", self.aa, self.FontCol)``

185: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(GreenInfo, (3, 430))``

186: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BlueInfo, (3, 445))``

187: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(RedInfo, (3, 460))``


188: ``¬ ¬ ¬ ¬ ¬ ¬ if resize == True:``

189: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ stage = 4``

190: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ resize = False``


191: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

192: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE) and stage <= 3) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``

193: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

194: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

195: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``

196: ``¬ ¬ ¬ ¬ ¬ ¬ if (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_SPACE) and stage == 0:``

197: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ stage += 1``

198: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.VIDEORESIZE:``

199: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ resize = True``


200: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

201: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)``

202: ``¬ ¬ ¬ except Exception as Message:``

203: ``¬ ¬ ¬ ¬ return Message``

204: ``else:``
205: ``¬ print("You need to run this as part of Pycraft")``
206: ``¬ import tkinter as tk``
207: ``¬ from tkinter import messagebox``
208: ``¬ root = tk.Tk()``
209: ``¬ root.withdraw()``
210: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
211: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_CaptionUtils>")``
        3: ``¬ class GenerateCaptions:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def GetLoadingCaption(self, num):``

7: ``¬ ¬ ¬ if num == 0:``

8: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (-)")``

9: ``¬ ¬ ¬ elif num == 1:``

10: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (\)")``

11: ``¬ ¬ ¬ elif num == 2:``

12: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (|)")``

13: ``¬ ¬ ¬ elif num == 3:``

14: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (/)")``

15: ``¬ ¬ ¬ else:``

16: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading")``

17: ``¬ ¬ ¬ self.mod_Pygame__.display.update()``


18: ``¬ ¬ def GetNormalCaption(self, location):``

19: ``¬ ¬ ¬ if self.Devmode >= 5 and self.Devmode <= 9:``

20: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | you are: {10-self.Devmode} steps away from being a developer")``

21: ``¬ ¬ ¬ elif self.Devmode == 10:``

22: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | Developer Mode | Pos: {round(self.X, 2)}, {round(self.Y, 2)}, {round(self.Z, 2)} | V: {self.Total_move_x}, {self.Total_move_y}, {self.Total_move_z} FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: {int(self.aFPS/self.Iteration)} Iteration: {self.Iteration} | MemUsE: {self.mod_Psutil__.virtual_memory().percent} | CPUUsE: {self.mod_Psutil__.cpu_percent()} | Theme: {self.theme} | Thread Count: {self.mod_Threading__.active_count()}")``

23: ``¬ ¬ ¬ else:``

24: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location}")``


25: ``else:``
26: ``¬ print("You need to run this as part of Pycraft")``
27: ``¬ import tkinter as tk``
28: ``¬ from tkinter import messagebox``
29: ``¬ root = tk.Tk()``
30: ``¬ root.withdraw()``
31: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
32: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_CharacterDesigner>")``
        3: ``¬ class GenerateCharacterDesigner:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def CharacterDesigner(self):``

7: ``¬ ¬ ¬ try:``

8: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

9: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

10: ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")``

11: ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``

12: ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``

13: ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``


14: ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.SecondFontCol)``

15: ``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``


16: ``¬ ¬ ¬ ¬ AchievementsFont = InfoTitleFont.render("Character Designer", self.aa, self.FontCol)``

17: ``¬ ¬ ¬ ¬ tempFPS = self.FPS``


18: ``¬ ¬ ¬ ¬ while True:``

19: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``


20: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``

21: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``

22: ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``

23: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``


24: ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``

25: ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``

26: ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``


27: ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``


28: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

29: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``

30: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

31: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

32: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``

33: ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:``

34: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:``

35: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``

36: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``

37: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``

38: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``

39: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``

40: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``

41: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``


42: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")``


43: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``


44: ``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``

45: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``

46: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``

47: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))``


48: ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``

49: ``¬ ¬ ¬ ¬ ¬ if not Message == None:``

50: ``¬ ¬ ¬ ¬ ¬ ¬ return Message``

51: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

52: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``

53: ``¬ ¬ ¬ except Exception as Message:``

54: ``¬ ¬ ¬ ¬ return Message``

55: ``else:``
56: ``¬ print("You need to run this as part of Pycraft")``
57: ``¬ import tkinter as tk``
58: ``¬ from tkinter import messagebox``
59: ``¬ root = tk.Tk()``
60: ``¬ root.withdraw()``
61: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
62: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_Credits>")``
        3: ``¬ class GenerateCredits:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def Credits(self):``

7: ``¬ ¬ ¬ try:``

8: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

9: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

10: ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits")``

11: ``¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

12: ``¬ ¬ ¬ ¬ LargeCreditsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``

13: ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``

14: ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``

15: ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

16: ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``

17: ``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``

18: ``¬ ¬ ¬ ¬ TitleHeight = TitleFont.get_height()``

19: ``¬ ¬ ¬ ¬ CreditsFont = InfoTitleFont.render("Credits", self.aa, self.SecondFontCol)``

20: ``¬ ¬ ¬ ¬ Credits1 = LargeCreditsFont.render(f"Pycraft: v{self.version}", self.aa, self.FontCol)``

21: ``¬ ¬ ¬ ¬ Credits1Width = Credits1.get_width()``

22: ``¬ ¬ ¬ ¬ Credits2 = LargeCreditsFont.render("Game Director: Tom Jebbo", self.aa, self.FontCol)``

23: ``¬ ¬ ¬ ¬ Credits2Width = Credits2.get_width()``

24: ``¬ ¬ ¬ ¬ Credits3 = LargeCreditsFont.render("Art and Music Lead: Tom Jebbo", self.aa, self.FontCol)``

25: ``¬ ¬ ¬ ¬ Credits3Width = Credits3.get_width()``

26: ``¬ ¬ ¬ ¬ Credits4 = LargeCreditsFont.render("Other Music Credits:", self.aa, self.FontCol)``

27: ``¬ ¬ ¬ ¬ Credits4Width = Credits4.get_width()``

28: ``¬ ¬ ¬ ¬ Credits5 = LargeCreditsFont.render("Freesound: - Erokia's 'ambient wave compilation' @ freesound.org/s/473545", self.aa, self.FontCol)``

29: ``¬ ¬ ¬ ¬ Credits5Width = Credits5.get_width()``

30: ``¬ ¬ ¬ ¬ Credits6 = LargeCreditsFont.render("Freesound: - Soundholder's 'ambient meadow near forest' @ freesound.org/s/425368", self.aa, self.FontCol)``

31: ``¬ ¬ ¬ ¬ Credits6Width = Credits6.get_width()``

32: ``¬ ¬ ¬ ¬ Credits7 = LargeCreditsFont.render("Freesound: - monte32's 'Footsteps_6_Dirt_shoe' @ freesound.org/people/monte32/sounds/353799", self.aa, self.FontCol)``

33: ``¬ ¬ ¬ ¬ Credits7Width = Credits7.get_width()``

34: ``¬ ¬ ¬ ¬ Credits8 = LargeCreditsFont.render("With thanks to the developers of:", self.aa, self.FontCol)``

35: ``¬ ¬ ¬ ¬ Credits8Width = Credits8.get_width()``

36: ``¬ ¬ ¬ ¬ Credits9 = LargeCreditsFont.render("PSutil", self.aa, self.FontCol)``

37: ``¬ ¬ ¬ ¬ Credits9Width = Credits9.get_width()``

38: ``¬ ¬ ¬ ¬ Credits10 = LargeCreditsFont.render("Python", self.aa, self.FontCol)``

39: ``¬ ¬ ¬ ¬ Credits10Width = Credits10.get_width()``

40: ``¬ ¬ ¬ ¬ Credits11 = LargeCreditsFont.render("Pygame", self.aa, self.FontCol)``

41: ``¬ ¬ ¬ ¬ Credits11Width = Credits11.get_width()``

42: ``¬ ¬ ¬ ¬ Credits12 = LargeCreditsFont.render("Numpy", self.aa, self.FontCol)``

43: ``¬ ¬ ¬ ¬ Credits12Width = Credits12.get_width()``

44: ``¬ ¬ ¬ ¬ Credits13 = LargeCreditsFont.render("Nuitka", self.aa, self.FontCol)``

45: ``¬ ¬ ¬ ¬ Credits13Width = Credits13.get_width()``

46: ``¬ ¬ ¬ ¬ Credits14 = LargeCreditsFont.render("CPUinfo", self.aa, self.FontCol)``

47: ``¬ ¬ ¬ ¬ Credits14Width = Credits14.get_width()``

48: ``¬ ¬ ¬ ¬ Credits15 = LargeCreditsFont.render("PyInstaller", self.aa, self.FontCol)``

49: ``¬ ¬ ¬ ¬ Credits15Width = Credits15.get_width()``

50: ``¬ ¬ ¬ ¬ Credits16 = LargeCreditsFont.render("PyAutoGUI", self.aa, self.FontCol)``

51: ``¬ ¬ ¬ ¬ Credits16Width = Credits16.get_width()``

52: ``¬ ¬ ¬ ¬ Credits17 = LargeCreditsFont.render("PyWaveFront", self.aa, self.FontCol)``

53: ``¬ ¬ ¬ ¬ Credits17Width = Credits17.get_width()``

54: ``¬ ¬ ¬ ¬ Credits18 = LargeCreditsFont.render("Microsoft's Visual Studio Code", self.aa, self.FontCol)``

55: ``¬ ¬ ¬ ¬ Credits18Width = Credits18.get_width()``

56: ``¬ ¬ ¬ ¬ Credits19 = LargeCreditsFont.render("PIL (Pillow/Python Imaging Library)", self.aa, self.FontCol)``

57: ``¬ ¬ ¬ ¬ Credits19Width = Credits19.get_width()``

58: ``¬ ¬ ¬ ¬ Credits20 = LargeCreditsFont.render("PyOpenGL (and PyOpenGL-accelerate)", self.aa, self.FontCol)``

59: ``¬ ¬ ¬ ¬ Credits20Width = Credits20.get_width()``

60: ``¬ ¬ ¬ ¬ Credits21 = LargeCreditsFont.render("For more in depth accreditation please check the GitHub Page @ github.com/PycraftDeveloper/Pycraft", self.aa, self.FontCol)``

61: ``¬ ¬ ¬ ¬ Credits21Width = Credits21.get_width()``

62: ``¬ ¬ ¬ ¬ Credits22 = LargeCreditsFont.render("With thanks to:", self.aa, self.FontCol)``

63: ``¬ ¬ ¬ ¬ Credits22Width = Credits22.get_width()``

64: ``¬ ¬ ¬ ¬ Credits23 = LargeCreditsFont.render("All my wonderful followers on Twitter, and you for installing this game, that's massively appreciated!", self.aa, self.FontCol)``

65: ``¬ ¬ ¬ ¬ Credits23Width = Credits23.get_width()``

66: ``¬ ¬ ¬ ¬ Credits24 = LargeCreditsFont.render("For full change-log please visit my aforementioned GitHub profile", self.aa, self.FontCol)``

67: ``¬ ¬ ¬ ¬ Credits24Width = Credits24.get_width()``

68: ``¬ ¬ ¬ ¬ Credits25 = LargeCreditsFont.render("Disclaimer:", self.aa, self.FontCol)``

69: ``¬ ¬ ¬ ¬ Credits25Width = Credits25.get_width()``

70: ``¬ ¬ ¬ ¬ Credits26 = VersionFont.render("The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your", self.aa, self.AccentCol)``

71: ``¬ ¬ ¬ ¬ Credits26Width = Credits26.get_width()``

72: ``¬ ¬ ¬ ¬ Credits27 = VersionFont.render("friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve", self.aa, self.AccentCol)``

73: ``¬ ¬ ¬ ¬ Credits27Width = Credits27.get_width()``

74: ``¬ ¬ ¬ ¬ Credits28 = VersionFont.render("my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo", self.aa, self.AccentCol)``

75: ``¬ ¬ ¬ ¬ Credits28Width = Credits28.get_width()``

76: ``¬ ¬ ¬ ¬ Credits29 = VersionFont.render("DOES NOT TAKE ANY RESPONSIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXTERNAL MODULES INSTALLED ONTO", self.aa, self.AccentCol)``

77: ``¬ ¬ ¬ ¬ Credits29Width = Credits29.get_width()``

78: ``¬ ¬ ¬ ¬ Credits30 = VersionFont.render("YOUR COMPUTER (WHEN NOT CHOOSING THE RECOMMENDED EXECUTABLE VERSION) ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM", self.aa, self.AccentCol)``

79: ``¬ ¬ ¬ ¬ Credits30Width = Credits30.get_width()``

80: ``¬ ¬ ¬ ¬ Credits31 = VersionFont.render("RESPONSIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVICES MANAGER OR ADMINISTRATOR TO INSTALL AND USE", self.aa, self.AccentCol)``

81: ``¬ ¬ ¬ ¬ Credits31Width = Credits31.get_width()``

82: ``¬ ¬ ¬ ¬ Credits32 = VersionFont.render("COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVICE, AND AT ANY POINT NO CONNECTION TO A", self.aa, self.AccentCol)``

83: ``¬ ¬ ¬ ¬ Credits32Width = Credits32.get_width()``

84: ``¬ ¬ ¬ ¬ Credits33 = VersionFont.render("NETWORK IS REQUIRED. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you.", self.aa, self.AccentCol)``

85: ``¬ ¬ ¬ ¬ Credits33Width = Credits33.get_width()``

86: ``¬ ¬ ¬ ¬ Credits34 = VersionFont.render("Thank You!", self.aa, self.FontCol)``

87: ``¬ ¬ ¬ ¬ Credits34Width = Credits34.get_width()``

88: ``¬ ¬ ¬ ¬ Credits34Height = Credits34.get_height()``


89: ``¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

90: ``¬ ¬ ¬ ¬ VisualYdisplacement = realHeight``

91: ``¬ ¬ ¬ ¬ IntroYDisplacement = (realHeight-TitleHeight)/2``

92: ``¬ ¬ ¬ ¬ timer = 5``

93: ``¬ ¬ ¬ ¬ tempFPS = self.FPS``


94: ``¬ ¬ ¬ ¬ EndClock = 0``

95: ``¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``

96: ``¬ ¬ ¬ ¬ while True:``

97: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``


98: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``

99: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``

100: ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``

101: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``


102: ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``

103: ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``

104: ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``


105: ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``


106: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

107: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``

108: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

109: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

110: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``

111: ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:``

112: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:``

113: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``

114: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``

115: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``

116: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``

117: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``

118: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``

119: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``


120: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits and Change-Log")``

121: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

122: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits1, ((realWidth-Credits1Width)/2, 0+VisualYdisplacement))``

123: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits2, ((realWidth-Credits2Width)/2, 115+VisualYdisplacement))``

124: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits3, ((realWidth-Credits3Width)/2, (115*2)+VisualYdisplacement))``

125: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits4, ((realWidth-Credits4Width)/2, (115*3)+VisualYdisplacement))``

126: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits5, ((realWidth-Credits5Width)/2, (115*3)+20+VisualYdisplacement))``

127: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits6, ((realWidth-Credits6Width)/2, (115*3)+40+VisualYdisplacement))``

128: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits7, ((realWidth-Credits7Width)/2, (115*3)+60+VisualYdisplacement))``

129: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits8, ((realWidth-Credits8Width)/2, 540+VisualYdisplacement))``

130: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits9, ((realWidth-Credits9Width)/2, 540+20+VisualYdisplacement))``

131: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits10, ((realWidth-Credits10Width)/2, 540+40+VisualYdisplacement))``

132: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits11, ((realWidth-Credits11Width)/2, 540+60+VisualYdisplacement))``

133: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits12, ((realWidth-Credits12Width)/2, 540+80+VisualYdisplacement))``

134: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits13, ((realWidth-Credits13Width)/2, 540+100+VisualYdisplacement))``

135: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits14, ((realWidth-Credits14Width)/2, 540+120+VisualYdisplacement))``

136: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits15, ((realWidth-Credits15Width)/2, 540+140+VisualYdisplacement))``

137: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits16, ((realWidth-Credits16Width)/2, 540+160+VisualYdisplacement))``

138: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits17, ((realWidth-Credits17Width)/2, 540+180+VisualYdisplacement))``

139: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits18, ((realWidth-Credits18Width)/2, 540+200+VisualYdisplacement))``

140: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits19, ((realWidth-Credits19Width)/2, 540+220+VisualYdisplacement))``

141: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits20, ((realWidth-Credits20Width)/2, 540+240+VisualYdisplacement))``

142: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits21, ((realWidth-Credits21Width)/2, 540+260+VisualYdisplacement))``

143: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits22, ((realWidth-Credits22Width)/2, 915+VisualYdisplacement))``

144: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits23, ((realWidth-Credits23Width)/2, 935+VisualYdisplacement))``

145: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits24, ((realWidth-Credits24Width)/2, 1050+VisualYdisplacement))``

146: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits25, ((realWidth-Credits25Width)/2, 1165+VisualYdisplacement))``

147: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits26, ((realWidth-Credits26Width)/2, 1167+15+VisualYdisplacement))``

148: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits27, ((realWidth-Credits27Width)/2, 1167+30+VisualYdisplacement))``

149: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits28, ((realWidth-Credits28Width)/2, 1167+45+VisualYdisplacement))``

150: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits29, ((realWidth-Credits29Width)/2, 1167+60+VisualYdisplacement))``

151: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits30, ((realWidth-Credits30Width)/2, 1167+75+VisualYdisplacement))``

152: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits31, ((realWidth-Credits31Width)/2, 1167+90+VisualYdisplacement))``

153: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits32, ((realWidth-Credits32Width)/2, 1167+105+VisualYdisplacement))``

154: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits33, ((realWidth-Credits33Width)/2, 1167+120+VisualYdisplacement))``


155: ``¬ ¬ ¬ ¬ ¬ if timer >= 1:``

156: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))``

157: ``¬ ¬ ¬ ¬ ¬ ¬ timer -= 1/(self.aFPS/self.Iteration)``

158: ``¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement = realHeight``

159: ``¬ ¬ ¬ ¬ ¬ else:``

160: ``¬ ¬ ¬ ¬ ¬ ¬ if IntroYDisplacement <= 0:``

161: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, FullscreenX, 90)``

162: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``

163: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``

164: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50))``

165: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if int(1402+VisualYdisplacement) <= int(realHeight/2):``

166: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, (realHeight-Credits34Height)/2))``

167: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement -= 60/(self.aFPS/self.Iteration)``

168: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if EndClock >= 5:``

169: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``

170: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``

171: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ EndClock += 1/(self.aFPS/self.Iteration)``

172: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``

173: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, 1402+VisualYdisplacement))``

174: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement -= 60/(self.aFPS/self.Iteration)``

175: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

176: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``

177: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``

178: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))``

179: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50+IntroYDisplacement))``

180: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ IntroYDisplacement -= 90/(self.aFPS/self.Iteration)``

181: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement = realHeight``


182: ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``

183: ``¬ ¬ ¬ ¬ ¬ if not Message == None:``

184: ``¬ ¬ ¬ ¬ ¬ ¬ return Message``

185: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

186: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``

187: ``¬ ¬ ¬ except Exception as Message:``

188: ``¬ ¬ ¬ ¬ return Message``

189: ``else:``
190: ``¬ print("You need to run this as part of Pycraft")``
191: ``¬ import tkinter as tk``
192: ``¬ from tkinter import messagebox``
193: ``¬ root = tk.Tk()``
194: ``¬ root.withdraw()``
195: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
196: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_DisplayUtils>")``
        3: ``¬ class DisplayUtils:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``



6: ``¬ ¬ def UpdateDisplay(self): # Run tests to make sure windows not too small``

7: ``¬ ¬ ¬ self.Data_aFPS = []``

8: ``¬ ¬ ¬ self.Data_CPUUsE = []``

9: ``¬ ¬ ¬ self.Data_eFPS = []``

10: ``¬ ¬ ¬ self.Data_MemUsE = []``

11: ``¬ ¬ ¬ self.Timer = 0``

12: ``¬ ¬ ¬ self.Data_aFPS_Min = 60``

13: ``¬ ¬ ¬ self.Data_aFPS_Max = 1``


14: ``¬ ¬ ¬ self.Data_CPUUsE_Min = 60``

15: ``¬ ¬ ¬ self.Data_CPUUsE_Max = 1``


16: ``¬ ¬ ¬ self.Data_eFPS_Min = 60``

17: ``¬ ¬ ¬ self.Data_eFPS_Max = 1``


18: ``¬ ¬ ¬ self.Data_MemUsE_Min = 50``

19: ``¬ ¬ ¬ self.Data_MemUsE_Max = 50``


20: ``¬ ¬ ¬ self.Data_CPUUsE_Min = 50``

21: ``¬ ¬ ¬ self.Data_CPUUsE_Max = 50``

22: ``¬ ¬ ¬ try:``

23: ``¬ ¬ ¬ ¬ try:``

24: ``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``

25: ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``

26: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``

27: ``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:``

28: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``

29: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``

30: ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = True``

31: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.RESIZABLE)``

32: ``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:``

33: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``

34: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``

35: ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = False``

36: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF)``

37: ``¬ ¬ ¬ ¬ except Exception as error:``

38: ``¬ ¬ ¬ ¬ ¬ self.Fullscreen = True``

39: ``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``

40: ``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``

41: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``

42: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``

43: ``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight))``

44: ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``

45: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``

46: ``¬ ¬ ¬ except Exception as Message:``

47: ``¬ ¬ ¬ ¬ return Message``

48: ``¬ ¬ ¬ else:``

49: ``¬ ¬ ¬ ¬ return None``



50: ``¬ ¬ def SetOPENGLdisplay(self):``

51: ``¬ ¬ ¬ try:``

52: ``¬ ¬ ¬ ¬ try:``

53: ``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``

54: ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``

55: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``

56: ``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == True:``

57: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``

58: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``

59: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``

60: ``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == False:``

61: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``

62: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``

63: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``

64: ``¬ ¬ ¬ ¬ except Exception as error:``

65: ``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``

66: ``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``

67: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``

68: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``

69: ``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``

70: ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``

71: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``

72: ``¬ ¬ ¬ except Exception as Message:``

73: ``¬ ¬ ¬ ¬ return Message``

74: ``¬ ¬ ¬ else:``

75: ``¬ ¬ ¬ ¬ return None``



76: ``¬ ¬ def UpdateOPENGLdisplay(self):``

77: ``¬ ¬ ¬ try:``

78: ``¬ ¬ ¬ ¬ try:``

79: ``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``

80: ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``

81: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``

82: ``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:``

83: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``

84: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``

85: ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = True``

86: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``

87: ``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:``

88: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``

89: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``

90: ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = False``

91: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``

92: ``¬ ¬ ¬ ¬ except:``

93: ``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``

94: ``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``

95: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``

96: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``

97: ``¬ ¬ ¬ ¬ ¬ self.Fullscreen = False``

98: ``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``

99: ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``

100: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``

101: ``¬ ¬ ¬ except Exception as Message:``

102: ``¬ ¬ ¬ ¬ return Message``

103: ``¬ ¬ ¬ else:``

104: ``¬ ¬ ¬ ¬ return None``



105: ``¬ ¬ def SetDisplay(self):``

106: ``¬ ¬ ¬ self.Data_aFPS = []``

107: ``¬ ¬ ¬ self.Data_CPUUsE = []``

108: ``¬ ¬ ¬ self.Data_eFPS = []``

109: ``¬ ¬ ¬ self.Data_MemUsE = []``

110: ``¬ ¬ ¬ self.Timer = 0``

111: ``¬ ¬ ¬ self.Data_aFPS_Min = 60``

112: ``¬ ¬ ¬ self.Data_aFPS_Max = 1``


113: ``¬ ¬ ¬ self.Data_CPUUsE_Min = 60``

114: ``¬ ¬ ¬ self.Data_CPUUsE_Max = 1``


115: ``¬ ¬ ¬ self.Data_eFPS_Min = 60``

116: ``¬ ¬ ¬ self.Data_eFPS_Max = 1``


117: ``¬ ¬ ¬ self.Data_MemUsE_Min = 50``

118: ``¬ ¬ ¬ self.Data_MemUsE_Max = 50``


119: ``¬ ¬ ¬ self.Data_CPUUsE_Min = 50``

120: ``¬ ¬ ¬ self.Data_CPUUsE_Max = 50``

121: ``¬ ¬ ¬ try:``

122: ``¬ ¬ ¬ ¬ try:``

123: ``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``

124: ``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == True:``

125: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``

126: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``

127: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.RESIZABLE)``

128: ``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == False:``

129: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``

130: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``

131: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF)``

132: ``¬ ¬ ¬ ¬ except Exception as error:``

133: ``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``

134: ``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``

135: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``

136: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``

137: ``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight))``

138: ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``

139: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``

140: ``¬ ¬ ¬ except Exception as Message:``

141: ``¬ ¬ ¬ ¬ return Message``

142: ``¬ ¬ ¬ else:``

143: ``¬ ¬ ¬ ¬ return None``



144: ``¬ ¬ def GenerateMinDisplay(self, width, height):``

145: ``¬ ¬ ¬ try:``

146: ``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((width, height), self.mod_Pygame__.RESIZABLE)``

147: ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``

148: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``

149: ``¬ ¬ ¬ except Exception as Message:``

150: ``¬ ¬ ¬ ¬ return Message``

151: ``¬ ¬ ¬ else:``

152: ``¬ ¬ ¬ ¬ return None``



153: ``¬ ¬ def GetDisplayLocation(self):``

154: ``¬ ¬ ¬ hwnd = self.mod_Pygame__.display.get_wm_info()["window"]``


155: ``¬ ¬ ¬ prototype = self.mod_Ctypes__.WINFUNCTYPE(self.mod_Ctypes__.wintypes.BOOL, self.mod_Ctypes__.wintypes.HWND, self.mod_Ctypes__.POINTER(self.mod_Ctypes__.wintypes.RECT))``

156: ``¬ ¬ ¬ paramflags = (1, "hwnd"), (2, "lprect")``


157: ``¬ ¬ ¬ GetWindowRect = prototype(("GetWindowRect", self.mod_Ctypes__.windll.user32), paramflags)``


158: ``¬ ¬ ¬ rect = GetWindowRect(hwnd)``


159: ``¬ ¬ ¬ return rect.left+8, rect.top+31``



160: ``¬ ¬ def GetPlayStatus(self):``

161: ``¬ ¬ ¬ if self.mod_Pygame__.display.get_active() == True:``

162: ``¬ ¬ ¬ ¬ tempFPS = self.FPS``

163: ``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).unpause()``

164: ``¬ ¬ ¬ ¬ if self.mod_Pygame__.mixer.Channel(2).get_busy() == 0 and self.LoadMusic == True:``

165: ``¬ ¬ ¬ ¬ ¬ if self.music == True and self.CurrentlyPlaying == None:``

166: ``¬ ¬ ¬ ¬ ¬ ¬ self.CurrentlyPlaying = "InvSound"``

167: ``¬ ¬ ¬ ¬ ¬ ¬ self.LoadMusic = False``

168: ``¬ ¬ ¬ ¬ ¬ ¬ MusicThread = self.mod_Threading__.Thread(target=self.mod_SoundUtils__.PlaySound.PlayInvSound, args=(self,))``

169: ``¬ ¬ ¬ ¬ ¬ ¬ MusicThread.start()``

170: ``¬ ¬ ¬ else:``

171: ``¬ ¬ ¬ ¬ self.LoadMusic = True``

172: ``¬ ¬ ¬ ¬ tempFPS = 15``

173: ``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).pause()``

174: ``¬ ¬ ¬ return tempFPS``


175: ``else:``
176: ``¬ print("You need to run this as part of Pycraft")``
177: ``¬ import tkinter as tk``
178: ``¬ from tkinter import messagebox``
179: ``¬ root = tk.Tk()``
180: ``¬ root.withdraw()``
181: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
182: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_DrawingUtils>")``
        3: ``¬ class DrawRose:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def CreateRose(self, xScaleFact, yScaleFact, coloursARRAY):``

7: ``¬ ¬ ¬ if coloursARRAY == False:``

8: ``¬ ¬ ¬ ¬ coloursARRAY = []``

9: ``¬ ¬ ¬ ¬ for i in range(32):``

10: ``¬ ¬ ¬ ¬ ¬ coloursARRAY.append(self.ShapeCol)``


11: ``¬ ¬ ¬ defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)]``

12: ``¬ ¬ ¬ self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2)``


13: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[0], (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``

14: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[1], (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``

15: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[2], (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

16: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[3], (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

17: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[4], (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

18: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[5], (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``

19: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[6], (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``

20: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[7], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

21: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[8], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

22: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[9], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

23: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[10], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

24: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[11], (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``

25: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[12], (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``

26: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[13], (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

27: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[14], (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

28: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[15], (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

29: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[16], (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

30: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[17], (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``

31: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[18], (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``

32: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[19], (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

33: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[20], (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

34: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[21], (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

35: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[22], (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

36: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[23], (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``

37: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[24], (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``

38: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[25], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

39: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[25], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

40: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[27], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

41: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[28], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

42: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[29], (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

43: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[30], (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

44: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[31], (575*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``


45: ``¬ class GenerateGraph:``

46: ``¬ ¬ def __init__(self):``

47: ``¬ ¬ ¬ pass``


48: ``¬ ¬ def CreateDevmodeGraph(self, DataFont):``

49: ``¬ ¬ ¬ if self.Devmode == 10:``

50: ``¬ ¬ ¬ ¬ try:``

51: ``¬ ¬ ¬ ¬ ¬ if ((self.realWidth/2)+100)+self.Timer >= self.realWidth:``

52: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS = []``

53: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE = []``

54: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS = []``

55: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE = []``

56: ``¬ ¬ ¬ ¬ ¬ ¬ self.Timer = 0``

57: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Min = 60``

58: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Max = 1``


59: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = 60``

60: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = 1``


61: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Min = 60``

62: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Max = 1``


63: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Min = 50``

64: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = 50``


65: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = 50``

66: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = 50``


67: ``¬ ¬ ¬ ¬ ¬ BackingRect = self.mod_Pygame__.Rect((self.realWidth/2)+100, 0, self.realWidth, 200)``

68: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, BackingRect)``


69: ``¬ ¬ ¬ ¬ ¬ if self.Timer >= 2:``

70: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_aFPS_Max)*(self.aFPS/(self.Iteration))])``

71: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_eFPS_Max)*int(self.eFPS)])``

72: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_MemUsE_Max)*(100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available])``


73: ``¬ ¬ ¬ ¬ ¬ if (self.aFPS/(self.Iteration)) > self.Data_aFPS_Max:``

74: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Max = (self.aFPS/(self.Iteration))``

75: ``¬ ¬ ¬ ¬ ¬ elif (self.aFPS/(self.Iteration)) < self.Data_aFPS_Min:``

76: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Min = (self.aFPS/(self.Iteration))``


77: ``¬ ¬ ¬ ¬ ¬ if self.eFPS > self.Data_eFPS_Max:``

78: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Max = self.eFPS``

79: ``¬ ¬ ¬ ¬ ¬ elif self.eFPS < self.Data_eFPS_Min:``

80: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Min = self.eFPS``


81: ``¬ ¬ ¬ ¬ ¬ if (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available > self.Data_MemUsE_Max:``

82: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available``

83: ``¬ ¬ ¬ ¬ ¬ elif (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available < self.Data_MemUsE_Max:``

84: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available``


85: ``¬ ¬ ¬ ¬ ¬ self.Timer += 0.2``

86: ``¬ ¬ ¬ ¬ ¬ if self.Timer >= 5:``

87: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 0), False, self.Data_aFPS)``

88: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 255, 0), False, self.Data_eFPS)``

89: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 0, 255), False, self.Data_MemUsE)``

90: ``¬ ¬ ¬ ¬ ¬ if len(self.Data_CPUUsE) >= 2:``

91: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 255), False, self.Data_CPUUsE)``

92: ``¬ ¬ ¬ ¬ ¬ runFont = DataFont.render(f"MemUsE: {self.mod_Psutil__.virtual_memory().percent}% | CPUUsE: {self.mod_Psutil__.cpu_percent()}% | FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: {int(self.aFPS/self.Iteration)} Iteration: {self.Iteration}", self.aa, (255, 255, 255))``

93: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(runFont, ((self.realWidth/2)+105, 0))``

94: ``¬ ¬ ¬ ¬ except Exception as Message:``

95: ``¬ ¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``

96: ``¬ ¬ ¬ ¬ ¬ return Message``

97: ``else:``
98: ``¬ print("You need to run this as part of Pycraft")``
99: ``¬ import tkinter as tk``
100: ``¬ from tkinter import messagebox``
101: ``¬ root = tk.Tk()``
102: ``¬ root.withdraw()``
103: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
104: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_ExBenchmark>")``
        3: ``¬ class LoadBenchmark:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def run(self):``

7: ``¬ ¬ ¬ try:``

8: ``¬ ¬ ¬ ¬ FPSlistX = []``

9: ``¬ ¬ ¬ ¬ FPSlistY = []``


10: ``¬ ¬ ¬ ¬ FPSlistX2 = []``

11: ``¬ ¬ ¬ ¬ FPSlistY2 = []``


12: ``¬ ¬ ¬ ¬ FPSlistX3 = []``

13: ``¬ ¬ ¬ ¬ FPSlistY3 = []``


14: ``¬ ¬ ¬ ¬ SetFPS = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 200, 250, 300, 350, 500]``


15: ``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((1280, 720))``


16: ``¬ ¬ ¬ ¬ iteration = 0``

17: ``¬ ¬ ¬ ¬ FPScounter = 0``

18: ``¬ ¬ ¬ ¬ MaxIteration = 500``


19: ``¬ ¬ ¬ ¬ while iteration < 7500:``

20: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running Blank Window Benchmark @ {SetFPS[FPScounter]} FPS")``

21: ``¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:``

22: ``¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:``

23: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX.append(iteration)``

24: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY.append(self.clock.get_fps())``

25: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

26: ``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

27: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``

28: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``


29: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

30: ``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``

31: ``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])``

32: ``¬ ¬ ¬ ¬ ¬ FPScounter += 1``

33: ``¬ ¬ ¬ ¬ ¬ MaxIteration += 500``


34: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Preparing Animated Benchmark")``


35: ``¬ ¬ ¬ ¬ iteration = 0``

36: ``¬ ¬ ¬ ¬ FPScounter = 0``

37: ``¬ ¬ ¬ ¬ MaxIteration = 500``

38: ``¬ ¬ ¬ ¬ run = 0``

39: ``¬ ¬ ¬ ¬ y = 10``


40: ``¬ ¬ ¬ ¬ while not iteration == 60:``

41: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

42: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

43: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``

44: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``


45: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

46: ``¬ ¬ ¬ ¬ ¬ iteration += 1``

47: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(60)``



48: ``¬ ¬ ¬ ¬ iteration = 0``

49: ``¬ ¬ ¬ ¬ FPScounter = 0``

50: ``¬ ¬ ¬ ¬ MaxIteration = 500``


51: ``¬ ¬ ¬ ¬ while iteration < 7500:``

52: ``¬ ¬ ¬ ¬ ¬ run += 1``

53: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running Animated Window Benchmark @ {SetFPS[FPScounter]} FPS")``

54: ``¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:``

55: ``¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:``

56: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX2.append(iteration)``

57: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY2.append(self.clock.get_fps())``

58: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

59: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``

60: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``

61: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``

62: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``

63: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``

64: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``

65: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``

66: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``

67: ``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

68: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``

69: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``


70: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

71: ``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``

72: ``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])``

73: ``¬ ¬ ¬ ¬ ¬ FPScounter += 1``

74: ``¬ ¬ ¬ ¬ ¬ MaxIteration += 500``


75: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Preparing OpenGL Benchmark")``


76: ``¬ ¬ ¬ ¬ iteration = 0``

77: ``¬ ¬ ¬ ¬ FPScounter = 0``

78: ``¬ ¬ ¬ ¬ MaxIteration = 500``

79: ``¬ ¬ ¬ ¬ run = 0``

80: ``¬ ¬ ¬ ¬ y = 10``


81: ``¬ ¬ ¬ ¬ while not iteration == 60:``

82: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

83: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

84: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``

85: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``


86: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

87: ``¬ ¬ ¬ ¬ ¬ iteration += 1``

88: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(60)``


89: ``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((1280, 720), self.mod_Pygame__.OPENGL|self.mod_Pygame__.DOUBLEBUF)``


90: ``¬ ¬ ¬ ¬ iteration = 0``

91: ``¬ ¬ ¬ ¬ FPScounter = 0``

92: ``¬ ¬ ¬ ¬ MaxIteration = 500``

93: ``¬ ¬ ¬ ¬ vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))``

94: ``¬ ¬ ¬ ¬ edges = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4), (6,7), (5,1), (5,4), (5,7))``


95: ``¬ ¬ ¬ ¬ self.mod_OGLbenchmark__.LoadOGLBenchmark.CreateBenchmark(self)``


96: ``¬ ¬ ¬ ¬ while iteration < 7500:``

97: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running OpenGL Benchmark @ {SetFPS[FPScounter]} FPS")``

98: ``¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:``

99: ``¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:``

100: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX3.append(iteration)``

101: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY3.append(self.clock.get_fps())``

102: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_OGLbenchmark__.LoadOGLBenchmark.RunBenchmark(self, edges, vertices)``

103: ``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

104: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``

105: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``


106: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

107: ``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``

108: ``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])``

109: ``¬ ¬ ¬ ¬ ¬ FPScounter += 1``

110: ``¬ ¬ ¬ ¬ ¬ MaxIteration += 500``



111: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Finished Animated Benchmark")``

112: ``¬ ¬ ¬ ¬ self.mod_Time__.sleep(5)``

113: ``¬ ¬ ¬ except Exception as Message:``

114: ``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``

115: ``¬ ¬ ¬ ¬ return Message, None, None, None, None``

116: ``¬ ¬ ¬ else:``


117: ``¬ ¬ ¬ ¬ return None, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3``

118: ``else:``
119: ``¬ print("You need to run this as part of Pycraft")``
120: ``¬ import tkinter as tk``
121: ``¬ from tkinter import messagebox``
122: ``¬ root = tk.Tk()``
123: ``¬ root.withdraw()``
124: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
125: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_GameEngine>")``

3: ``¬ print("Started <Pycraft_GameEngine>")``


4: ``¬ from ShareDataUtil import Class_Startup_variables as SharedData``


5: ``¬ SharedData.mod_ModernGL_window_.setup_basic_logging(0)``



6: ``¬ class Cubemap(SharedData.mod_Base__.CameraWindow):``

7: ``¬ ¬ SharedData.mod_Base__.CameraWindow.title = f"Pycraft: v{SharedData.version}: Playing"``

8: ``¬ ¬ SharedData.mod_Base__.CameraWindow.resource_dir = SharedData.base_folder``



9: ``¬ ¬ def Exit(self, SharedData, Command):``

10: ``¬ ¬ ¬ try:``

11: ``¬ ¬ ¬ ¬ if SharedData.mod_Pygame__.mixer.Channel(3).get_busy() == True:``

12: ``¬ ¬ ¬ ¬ ¬ SharedData.mod_Pygame__.mixer.Channel(3).stop()``

13: ``¬ ¬ ¬ ¬ ¬ SharedData.mod_Pygame__.quit()``


14: ``¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = False``

15: ``¬ ¬ ¬ except Exception as Error:``

16: ``¬ ¬ ¬ ¬ print("GE", Error)``

17: ``¬ ¬ ¬ ¬ pass``

18: ``¬ ¬ ¬ self.wnd._set_fullscreen(False)``

19: ``¬ ¬ ¬ self.wnd.close()``

20: ``¬ ¬ ¬ self.wnd.destroy()``

21: ``¬ ¬ ¬ SharedData.CurrentlyPlaying = None``

22: ``¬ ¬ ¬ SharedData.LoadMusic = True``

23: ``¬ ¬ ¬ SharedData.Command = Command``

24: ``¬ ¬ ¬ if self.wnd.fullscreen == True:``

25: ``¬ ¬ ¬ ¬ SharedData.Fullscreen = False``

26: ``¬ ¬ ¬ else:``

27: ``¬ ¬ ¬ ¬ SharedData.Fullscreen = True``



28: ``¬ ¬ def __init__(self, **kwargs):``

29: ``¬ ¬ ¬ try:``

30: ``¬ ¬ ¬ ¬ super().__init__(**kwargs)``


31: ``¬ ¬ ¬ ¬ self.size = self.wnd.buffer_size``


32: ``¬ ¬ ¬ ¬ WindowSize = SharedData.realWidth, SharedData.realHeight``

33: ``¬ ¬ ¬ ¬ CurrentWindowSize = WindowSize``


34: ``¬ ¬ ¬ ¬ self.wnd.size = WindowSize``

35: ``¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = False``


36: ``¬ ¬ ¬ ¬ self.camera.projection.update(near=0.1, far=100.0)``

37: ``¬ ¬ ¬ ¬ self.camera.zoom = 2.5``


38: ``¬ ¬ ¬ ¬ self.obj = self.load_scene(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\Map\\map.obj")))``


39: ``¬ ¬ ¬ ¬ self.cube = SharedData.mod_ModernGL_window_.geometry.cube(size=(20, 20, 20))``


40: ``¬ ¬ ¬ ¬ self.prog = self.load_program(SharedData.mod_OS__.path.join(SharedData.base_folder, ("programs//cubemap.glsl")))``


41: ``¬ ¬ ¬ ¬ self.SkyBox_texture = self.load_texture_cube(``

42: ``¬ ¬ ¬ ¬ ¬ neg_x=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg")),``

43: ``¬ ¬ ¬ ¬ ¬ neg_y=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg")),``

44: ``¬ ¬ ¬ ¬ ¬ neg_z=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg")),``

45: ``¬ ¬ ¬ ¬ ¬ pos_x=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg")),``

46: ``¬ ¬ ¬ ¬ ¬ pos_y=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg")),``

47: ``¬ ¬ ¬ ¬ ¬ pos_z=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg")),``

48: ``¬ ¬ ¬ ¬ ¬ flip_x=True,``

49: ``¬ ¬ ¬ ¬ )``


50: ``¬ ¬ ¬ ¬ Prev_Mouse_Pos = (0,0)``

51: ``¬ ¬ ¬ ¬ Mouse_Pos = (0,0)``

52: ``¬ ¬ ¬ ¬ DeltaX, DeltaY = 0, 0``


53: ``¬ ¬ ¬ ¬ self.wnd.exit_key = None``


54: ``¬ ¬ ¬ ¬ MouseUnlock = True``


55: ``¬ ¬ ¬ ¬ Jump = False``

56: ``¬ ¬ ¬ ¬ JumpID = 0``


57: ``¬ ¬ ¬ ¬ self.camera.position.y += 0.7``


58: ``¬ ¬ ¬ ¬ WkeydownTimer = 0``

59: ``¬ ¬ ¬ ¬ AkeydownTimer = 0``

60: ``¬ ¬ ¬ ¬ SkeydownTimer = 0``

61: ``¬ ¬ ¬ ¬ DkeydownTimer = 0``


62: ``¬ ¬ ¬ ¬ RunForwardTimer = 0``


63: ``¬ ¬ ¬ ¬ FPS = 0``


64: ``¬ ¬ ¬ ¬ Iteration = 0``


65: ``¬ ¬ ¬ ¬ while True:``

66: ``¬ ¬ ¬ ¬ ¬ try:``

67: ``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.mod_Pygame__.mixer.get_busy() == False:``

68: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayAmbientSound(SharedData)``

69: ``¬ ¬ ¬ ¬ ¬ except Exception as Error:``

70: ``¬ ¬ ¬ ¬ ¬ ¬ print(Error)``

71: ``¬ ¬ ¬ ¬ ¬ ¬ pass``


72: ``¬ ¬ ¬ ¬ ¬ if Iteration == 0:``

73: ``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.Fullscreen == False:``

74: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.fullscreen = True``

75: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

76: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.fixed_aspect_ratio = SharedData.realWidth / SharedData.realHeight``

77: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.window_size = SharedData.realWidth, SharedData.realHeight``

78: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ CurrentWindowSize = self.window_size``

79: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.position = (int((SharedData.FullscreenX-CurrentWindowSize[0])/2), int((SharedData.FullscreenY-CurrentWindowSize[1])/2))``


80: ``¬ ¬ ¬ ¬ ¬ if Iteration >= 5000:``

81: ``¬ ¬ ¬ ¬ ¬ ¬ Iteration = 0``


82: ``¬ ¬ ¬ ¬ ¬ start = SharedData.mod_Time__.perf_counter()``


83: ``¬ ¬ ¬ ¬ ¬ self.ctx.clear(1.0, 1.0, 1.0)``


84: ``¬ ¬ ¬ ¬ ¬ CurrentWindowSize = self.window_size``


85: ``¬ ¬ ¬ ¬ ¬ Prev_Mouse_Pos = Mouse_Pos``

86: ``¬ ¬ ¬ ¬ ¬ Mouse_Pos = SharedData.mod_Pyautogui__.position()``

87: ``¬ ¬ ¬ ¬ ¬ DeltaX, DeltaY = Mouse_Pos[0]-Prev_Mouse_Pos[0], Mouse_Pos[1]-Prev_Mouse_Pos[1]``


88: ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.ESCAPE):``

89: ``¬ ¬ ¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "Undefined")``

90: ``¬ ¬ ¬ ¬ ¬ ¬ return None``

91: ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.W):``

92: ``¬ ¬ ¬ ¬ ¬ ¬ RunForwardTimer += (1/FPS)``

93: ``¬ ¬ ¬ ¬ ¬ ¬ if RunForwardTimer <= 10:``

94: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``

95: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer += (1/FPS)``

96: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if WkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``

97: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``

98: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer = 0``

99: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.x += 1.42``

100: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

101: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``

102: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer += (1/FPS)``

103: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if WkeydownTimer >= (SharedData.mod_Random__.randint(25, 75)/100):``

104: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``

105: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer = 0``

106: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.x += 2.2352``

107: ``¬ ¬ ¬ ¬ ¬ else:``

108: ``¬ ¬ ¬ ¬ ¬ ¬ RunForwardTimer = 0``


109: ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.A):``

110: ``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``

111: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ AkeydownTimer += (1/FPS)``

112: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if AkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``

113: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``

114: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AkeydownTimer = 0``

115: ``¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.z += 1.42``


116: ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.S):``

117: ``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``

118: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ SkeydownTimer += (1/FPS)``

119: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if SkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``

120: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``

121: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SkeydownTimer = 0``

122: ``¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.x -= 1.42``


123: ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.D):``

124: ``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``

125: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ DkeydownTimer += (1/FPS)``

126: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if DkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``

127: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``

128: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ DkeydownTimer = 0``

129: ``¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.z -= 1.42``


130: ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.E):``

131: ``¬ ¬ ¬ ¬ ¬ ¬ if self.wnd._fullscreen == True:``

132: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot = SharedData.mod_Pyautogui__.screenshot(region=((0, 0, SharedData.FullscreenX, SharedData.FullscreenY)))``

133: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot.save(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))``

134: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

135: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ PosX, PosY = self.wnd.position``

136: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot = SharedData.mod_Pyautogui__.screenshot(region=((PosX, PosY, SharedData.realWidth, SharedData.realHeight)))``

137: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot.save(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))``


138: ``¬ ¬ ¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "Inventory")``

139: ``¬ ¬ ¬ ¬ ¬ ¬ return None``


140: ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.R):``

141: ``¬ ¬ ¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "MapGUI")``

142: ``¬ ¬ ¬ ¬ ¬ ¬ return None``

143: ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.L):``

144: ``¬ ¬ ¬ ¬ ¬ ¬ if MouseUnlock == True:``

145: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ MouseUnlock = False``

146: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

147: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ MouseUnlock = True``

148: ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.SPACE):``

149: ``¬ ¬ ¬ ¬ ¬ ¬ Jump = True``

150: ``¬ ¬ ¬ ¬ ¬ ¬ JumpUP = True``


151: ``¬ ¬ ¬ ¬ ¬ if Jump == True:``

152: ``¬ ¬ ¬ ¬ ¬ ¬ if JumpID < 10 and JumpUP == True:``

153: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpID += 1``

154: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.y += 0.1``

155: ``¬ ¬ ¬ ¬ ¬ ¬ if JumpID == 10:``

156: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpUP = False``

157: ``¬ ¬ ¬ ¬ ¬ ¬ if JumpID >= 0 and JumpUP == False:``

158: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpID -= 1``

159: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.y -= 0.1``

160: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if JumpID == 0:``

161: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``

162: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``

163: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Jump = False``

164: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpID = 0``


165: ``¬ ¬ ¬ ¬ ¬ self.ctx.enable(SharedData.mod_ModernGL__.CULL_FACE | SharedData.mod_ModernGL__.DEPTH_TEST)``


166: ``¬ ¬ ¬ ¬ ¬ cam = self.camera.matrix``

167: ``¬ ¬ ¬ ¬ ¬ cam[3][0] = 0``

168: ``¬ ¬ ¬ ¬ ¬ cam[3][1] = 0``

169: ``¬ ¬ ¬ ¬ ¬ cam[3][2] = 0``


170: ``¬ ¬ ¬ ¬ ¬ self.SkyBox_texture.use(location=0)``

171: ``¬ ¬ ¬ ¬ ¬ self.prog['m_proj'].write(self.camera.projection.matrix)``

172: ``¬ ¬ ¬ ¬ ¬ self.prog['m_camera'].write(cam)``


173: ``¬ ¬ ¬ ¬ ¬ try:``

174: ``¬ ¬ ¬ ¬ ¬ ¬ if MouseUnlock == True:``

175: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.rot_state(-DeltaX, -DeltaY)``

176: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = True``

177: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

178: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = False``

179: ``¬ ¬ ¬ ¬ ¬ except Exception as Error:``

180: ``¬ ¬ ¬ ¬ ¬ ¬ print(Error)``

181: ``¬ ¬ ¬ ¬ ¬ ¬ pass``


182: ``¬ ¬ ¬ ¬ ¬ self.ctx.front_face = 'cw'``

183: ``¬ ¬ ¬ ¬ ¬ self.cube.render(self.prog)``


184: ``¬ ¬ ¬ ¬ ¬ self.ctx.front_face = 'ccw'``

185: ``¬ ¬ ¬ ¬ ¬ self.obj.draw(projection_matrix=self.camera.projection.matrix, camera_matrix=self.camera.matrix)``


186: ``¬ ¬ ¬ ¬ ¬ try:``

187: ``¬ ¬ ¬ ¬ ¬ ¬ self.wnd.swap_buffers()``

188: ``¬ ¬ ¬ ¬ ¬ except Exception as Error:``

189: ``¬ ¬ ¬ ¬ ¬ ¬ print(Error)``

190: ``¬ ¬ ¬ ¬ ¬ ¬ pass``


191: ``¬ ¬ ¬ ¬ ¬ FPS = 1/(SharedData.mod_Time__.perf_counter()-start)``

192: ``¬ ¬ ¬ ¬ ¬ Iteration += 1``

193: ``¬ ¬ ¬ except Exception as Message:``

194: ``¬ ¬ ¬ ¬ print(''.join(SharedData.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``

195: ``¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "Undefined")``

196: ``¬ ¬ ¬ ¬ SharedData.GameError = str(Message)``

197: ``¬ ¬ ¬ ¬ return None``




198: ``¬ class CreateEngine:``



199: ``¬ ¬ def __init__(self):``

200: ``¬ ¬ ¬ pass``



201: ``¬ ¬ def GenerateLoadDisplay(self, LoadingFont, text, MainTitleFont, SecondaryFont, LoadingTextFont):``

202: ``¬ ¬ ¬ try:``

203: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``


204: ``¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``


205: ``¬ ¬ ¬ ¬ PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``

206: ``¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``

207: ``¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))``


208: ``¬ ¬ ¬ ¬ LoadingTitle = SecondaryFont.render("Loading", self.aa, self.SecondFontCol)``

209: ``¬ ¬ ¬ ¬ self.Display.blit(LoadingTitle, (((self.realWidth-TitleWidth)/2)+55, 50))``


210: ``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (self.ShapeCol), self.aa, [(100, self.realHeight-100), (self.realWidth-100, self.realHeight-100)], 3)``

211: ``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (self.AccentCol), self.aa, self.Progress_Line)``


212: ``¬ ¬ ¬ ¬ DisplayMessage = LoadingFont.render(self.ProgressMessageText, self.aa, self.FontCol)``

213: ``¬ ¬ ¬ ¬ DisplayMessageWidth = DisplayMessage.get_width()``

214: ``¬ ¬ ¬ ¬ self.Display.blit(DisplayMessage, ((self.realWidth-DisplayMessageWidth)/2, self.realHeight-120))``


215: ``¬ ¬ ¬ ¬ TextFontRendered = LoadingTextFont.render(f"{text}", self.aa, self.FontCol)``

216: ``¬ ¬ ¬ ¬ TextFontRenderedWidth = TextFontRendered.get_width()``

217: ``¬ ¬ ¬ ¬ self.Display.blit(TextFontRendered, ((self.realWidth-TextFontRenderedWidth)/2, self.realHeight-100))``

218: ``¬ ¬ ¬ except Exception as error:``

219: ``¬ ¬ ¬ ¬ print(error)``


220: ``¬ ¬ def Play(self):``

221: ``¬ ¬ ¬ try:``

222: ``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).fadeout(2000)``


223: ``¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_WAIT)``


224: ``¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``

225: ``¬ ¬ ¬ ¬ self.mod_Pygame__.init()``

226: ``¬ ¬ ¬ ¬ self.mod_Globals__.Share.initialize(self)``

227: ``¬ ¬ ¬ ¬ try:``

228: ``¬ ¬ ¬ ¬ ¬ self.mod_ModernGL_window_.run_window_config(Cubemap)``

229: ``¬ ¬ ¬ ¬ except Exception as Error:``

230: ``¬ ¬ ¬ ¬ ¬ print(Error)``

231: ``¬ ¬ ¬ ¬ ¬ pass``

232: ``¬ ¬ ¬ ¬ return None``

233: ``¬ ¬ ¬ except Exception as Message:``

234: ``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``

235: ``¬ ¬ ¬ ¬ return Message, "Undefined"``



236: ``else:``
237: ``¬ print("You need to run this as part of Pycraft")``
238: ``¬ import tkinter as tk``
239: ``¬ from tkinter import messagebox``
240: ``¬ root = tk.Tk()``
241: ``¬ root.withdraw()``
242: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
243: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_GetSavedData>")``
        3: ``¬ class LoadSaveFiles:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def ReadMainSave(self):``

7: ``¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'r') as openfile:``

8: ``¬ ¬ ¬ ¬ save = self.mod_JSON__.load(openfile)``


9: ``¬ ¬ ¬ self.theme = save["theme"]``

10: ``¬ ¬ ¬ self.RunFullStartup = save["startup"]``

11: ``¬ ¬ ¬ self.crash = save["crash"]``

12: ``¬ ¬ ¬ self.Fullscreen = save["WindowStatus"]``

13: ``¬ ¬ ¬ self.RecommendedFPS = save["AdaptiveFPS"]``

14: ``¬ ¬ ¬ self.Devmode = save["Devmode"]``

15: ``¬ ¬ ¬ self.SettingsPreference = save["profile"]``

16: ``¬ ¬ ¬ self.FPS = save["FPS"]``

17: ``¬ ¬ ¬ self.aFPS = save["aFPS"]``

18: ``¬ ¬ ¬ self.Iteration = save["Iteration"]``

19: ``¬ ¬ ¬ self.FOV = save["FOV"]``

20: ``¬ ¬ ¬ self.cameraANGspeed = save["cameraANGspeed"]``

21: ``¬ ¬ ¬ self.RenderFOG = save["RenderFOG"]``

22: ``¬ ¬ ¬ self.aa = save["aa"]``

23: ``¬ ¬ ¬ self.X = save["X"]``

24: ``¬ ¬ ¬ self.Y = save["Y"]``

25: ``¬ ¬ ¬ self.Z = save["Z"]``

26: ``¬ ¬ ¬ self.FanSky = save["FanSky"]``

27: ``¬ ¬ ¬ self.FanPart = save["FanPart"]``

28: ``¬ ¬ ¬ self.sound = save["sound"]``

29: ``¬ ¬ ¬ self.soundVOL = save["soundVOL"]``

30: ``¬ ¬ ¬ self.music = save["music"]``

31: ``¬ ¬ ¬ self.musicVOL = save["musicVOL"]``

32: ``¬ ¬ ¬ self.lastRun = save["lastRun"]``

33: ``¬ ¬ ¬ self.SavedWidth = save["DisplayWidth"]``

34: ``¬ ¬ ¬ self.SavedHeight = save["DisplayHeight"]``

35: ``¬ ¬ ¬ self.Total_Vertices = save["Total_Vertices"]``

36: ``¬ ¬ ¬ if self.Total_Vertices == 0:``

37: ``¬ ¬ ¬ ¬ self.Total_Vertices = 1``


38: ``¬ ¬ def RepairLostSave(self):``

39: ``¬ ¬ ¬ try:``

40: ``¬ ¬ ¬ ¬ SavedData = {"Total_Vertices":0, "theme":False, "profile":"Medium", "Devmode":0, "AdaptiveFPS": 60, "FPS":60, "aFPS":60, "Iteration":1, "FOV":75, "cameraANGspeed":3, "aa":True, "RenderFOG":True, "FanSky":True, "FanPart":True, "sound":True, "soundVOL":75, "music":True, "musicVOL":50, "X":0, "Y":0, "Z":0, "lastRun":"29/09/2021", 'startup':True, 'crash': False, 'DisplayWidth':1280, 'DisplayHeight':720, 'WindowStatus':True}``

41: ``¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'w') as openfile:``

42: ``¬ ¬ ¬ ¬ ¬ self.mod_JSON__.dump(SavedData, openfile)``

43: ``¬ ¬ ¬ except Exception as Message:``

44: ``¬ ¬ ¬ ¬ return Message``

45: ``¬ ¬ ¬ else:``

46: ``¬ ¬ ¬ ¬ return None``


47: ``¬ ¬ def SaveTOconfigFILE(self):``

48: ``¬ ¬ ¬ try:``

49: ``¬ ¬ ¬ ¬ current_time = self.mod_Datetime__.datetime.now()``

50: ``¬ ¬ ¬ ¬ currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"``

51: ``¬ ¬ ¬ ¬ SavedData = {"Total_Vertices":self.Total_Vertices, "theme":self.theme, "profile":self.SettingsPreference, "Devmode":self.Devmode, "AdaptiveFPS": self.RecommendedFPS, "FPS":self.FPS, "aFPS":self.aFPS, "Iteration":self.Iteration, "FOV":self.FOV, "cameraANGspeed":self.cameraANGspeed, "aa":self.aa, "RenderFOG":self.RenderFOG, "FanSky":self.FanSky, "FanPart":self.FanPart, "sound":self.sound, "soundVOL":self.soundVOL, "music":self.music, "musicVOL":self.musicVOL, "X":self.X, "Y":self.Y, "Z":self.Z, "lastRun":currentDate, 'startup':self.RunFullStartup, 'crash': False, 'DisplayWidth':self.SavedWidth, 'DisplayHeight':self.SavedHeight, 'WindowStatus':self.Fullscreen}``

52: ``¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'w') as openfile:``

53: ``¬ ¬ ¬ ¬ ¬ self.mod_JSON__.dump(SavedData, openfile)``

54: ``¬ ¬ ¬ except Exception as Message:``

55: ``¬ ¬ ¬ ¬ return Message``

56: ``¬ ¬ ¬ else:``

57: ``¬ ¬ ¬ ¬ return None``

58: ``else:``
59: ``¬ print("You need to run this as part of Pycraft")``
60: ``¬ import tkinter as tk``
61: ``¬ from tkinter import messagebox``
62: ``¬ root = tk.Tk()``
63: ``¬ root.withdraw()``
64: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
65: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_HomeScreen>")``
        3: ``¬ class GenerateHomeScreen:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def DisplayMessage(self, MessageFont, Message, Colour):``

7: ``¬ ¬ ¬ MessageText = MessageFont.render(Message, self.aa, Colour)``

8: ``¬ ¬ ¬ MessageTextWidth = MessageText.get_width()``

9: ``¬ ¬ ¬ MessageTextHeight = MessageText.get_height()``

10: ``¬ ¬ ¬ self.Display.blit(MessageText, ((self.realWidth-MessageTextWidth)/2, (self.realHeight-MessageTextHeight)))``



11: ``¬ ¬ def Home_Screen(self):``

12: ``¬ ¬ ¬ try:``

13: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

14: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

15: ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Home screen")``

16: ``¬ ¬ ¬ ¬ Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()``

17: ``¬ ¬ ¬ ¬ SelectorWidth = Selector.get_width()``

18: ``¬ ¬ ¬ ¬ hover1 = False``

19: ``¬ ¬ ¬ ¬ hover2 = False``

20: ``¬ ¬ ¬ ¬ hover3 = False``

21: ``¬ ¬ ¬ ¬ hover4 = False``

22: ``¬ ¬ ¬ ¬ hover5 = False``

23: ``¬ ¬ ¬ ¬ hover6 = False``

24: ``¬ ¬ ¬ ¬ mousebuttondown = False``


25: ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``

26: ``¬ ¬ ¬ ¬ PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``

27: ``¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``

28: ``¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``

29: ``¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))``

30: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``


31: ``¬ ¬ ¬ ¬ SideFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``

32: ``¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``

33: ``¬ ¬ ¬ ¬ ButtonFont1 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

34: ``¬ ¬ ¬ ¬ ButtonFont2 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

35: ``¬ ¬ ¬ ¬ ButtonFont3 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

36: ``¬ ¬ ¬ ¬ ButtonFont4 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

37: ``¬ ¬ ¬ ¬ ButtonFont5 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

38: ``¬ ¬ ¬ ¬ ButtonFont6 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

39: ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

40: ``¬ ¬ ¬ ¬ MessageFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``


41: ``¬ ¬ ¬ ¬ oldTHEME = self.theme``

42: ``¬ ¬ ¬ ¬ tempFPS = self.FPS``

43: ``¬ ¬ ¬ ¬ coloursARRAY = []``


44: ``¬ ¬ ¬ ¬ anim = False``


45: ``¬ ¬ ¬ ¬ special = [30, 30, 30]``

46: ``¬ ¬ ¬ ¬ TargetARRAY = []``


47: ``¬ ¬ ¬ ¬ ColourDisplacement = 80``


48: ``¬ ¬ ¬ ¬ increment = False``

49: ``¬ ¬ ¬ ¬ while True:``

50: ``¬ ¬ ¬ ¬ ¬ coloursARRAY = []``

51: ``¬ ¬ ¬ ¬ ¬ if anim == True:``

52: ``¬ ¬ ¬ ¬ ¬ ¬ anim = False``

53: ``¬ ¬ ¬ ¬ ¬ ¬ TargetARRAY = []``

54: ``¬ ¬ ¬ ¬ ¬ ¬ for a in range(self.mod_Random__.randint(0, 32)):``

55: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ TargetARRAY.append(a)``


56: ``¬ ¬ ¬ ¬ ¬ if len(TargetARRAY) == 0:``

57: ``¬ ¬ ¬ ¬ ¬ ¬ TargetARRAY = [33]``

58: ``¬ ¬ ¬ ¬ ¬ for i in range(32):``

59: ``¬ ¬ ¬ ¬ ¬ ¬ for j in range(len(TargetARRAY)):``

60: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if i == TargetARRAY[j]:``

61: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ coloursARRAY.append(special)``

62: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``

63: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ coloursARRAY.append(self.ShapeCol)``


64: ``¬ ¬ ¬ ¬ ¬ if increment == False:``

65: ``¬ ¬ ¬ ¬ ¬ ¬ if self.aFPS == 0 or self.Iteration == 0:``

66: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement -= (self.mod_Random__.randint(0,10)/((self.FPS)/4))``

67: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

68: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement -= (self.mod_Random__.randint(0,10)/((self.aFPS/self.Iteration)/4))``

69: ``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = ColourDisplacement, ColourDisplacement, ColourDisplacement``

70: ``¬ ¬ ¬ ¬ ¬ if increment == True:``

71: ``¬ ¬ ¬ ¬ ¬ ¬ if self.aFPS == 0 or self.Iteration == 0:``

72: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement += (self.mod_Random__.randint(0,10)/((self.FPS)/4))``

73: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

74: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement += (self.mod_Random__.randint(0,10)/((self.aFPS/self.Iteration)/4))``

75: ``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = ColourDisplacement, ColourDisplacement, ColourDisplacement``

76: ``¬ ¬ ¬ ¬ ¬ if special[0] <= 30:``

77: ``¬ ¬ ¬ ¬ ¬ ¬ increment = True``

78: ``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = 30, 30, 30``

79: ``¬ ¬ ¬ ¬ ¬ if special[0] >= 80:``

80: ``¬ ¬ ¬ ¬ ¬ ¬ increment = False``

81: ``¬ ¬ ¬ ¬ ¬ ¬ anim = True``

82: ``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = 80, 80, 80``


83: ``¬ ¬ ¬ ¬ ¬ if self.mod_Pygame__.mixer.Channel(3).get_busy() == 1:``

84: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(3).stop()``


85: ``¬ ¬ ¬ ¬ ¬ if str(self.Display) == "<Surface(Dead Display)>":``

86: ``¬ ¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:``

87: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``

88: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:``

89: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``


90: ``¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``

91: ``¬ ¬ ¬ ¬ ¬ if not (self.realWidth == self.FullscreenX and self.realHeight == self.FullscreenY):``

92: ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedWidth, self.SavedHeight = self.mod_Pygame__.display.get_window_size()``


93: ``¬ ¬ ¬ ¬ ¬ if self.SavedWidth == self.FullscreenX:``

94: ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``

95: ``¬ ¬ ¬ ¬ ¬ if self.SavedHeight == self.FullscreenY:``

96: ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``


97: ``¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``

98: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``

99: ``¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``

100: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``


101: ``¬ ¬ ¬ ¬ ¬ yScaleFact = self.realHeight/720``

102: ``¬ ¬ ¬ ¬ ¬ xScaleFact = self.realWidth/1280``


103: ``¬ ¬ ¬ ¬ ¬ if not oldTHEME == self.theme:``

104: ``¬ ¬ ¬ ¬ ¬ ¬ Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()``

105: ``¬ ¬ ¬ ¬ ¬ ¬ SelectorWidth = Selector.get_width()``

106: ``¬ ¬ ¬ ¬ ¬ ¬ oldTHEME = self.theme``


107: ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``


108: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

109: ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``

110: ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``

111: ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``

112: ``¬ ¬ ¬ ¬ ¬ Mx, My = self.mod_Pygame__.mouse.get_pos()``

113: ``¬ ¬ ¬ ¬ ¬ PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``

114: ``¬ ¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``


115: ``¬ ¬ ¬ ¬ ¬ Name = SideFont.render("By Tom Jebbo", self.aa, self.FontCol)``

116: ``¬ ¬ ¬ ¬ ¬ NameHeight = Name.get_height()``


117: ``¬ ¬ ¬ ¬ ¬ Version = VersionFont.render(f"Version: {self.version}", self.aa, self.FontCol)``

118: ``¬ ¬ ¬ ¬ ¬ VersionWidth = Version.get_width()``

119: ``¬ ¬ ¬ ¬ ¬ VersionHeight = Version.get_height()``


120: ``¬ ¬ ¬ ¬ ¬ Play = ButtonFont1.render("Play", self.aa, self.FontCol)``

121: ``¬ ¬ ¬ ¬ ¬ PlayWidth = Play.get_width()``


122: ``¬ ¬ ¬ ¬ ¬ SettingsText = ButtonFont2.render("Settings", self.aa, self.FontCol)``

123: ``¬ ¬ ¬ ¬ ¬ SettingsWidth = SettingsText.get_width()``


124: ``¬ ¬ ¬ ¬ ¬ Character_DesignerText = ButtonFont3.render("Character Designer", self.aa, self.FontCol)``

125: ``¬ ¬ ¬ ¬ ¬ CharDesignerWidth = Character_DesignerText.get_width()``


126: ``¬ ¬ ¬ ¬ ¬ AchievementsText = ButtonFont4.render("Achievements", self.aa, self.FontCol)``

127: ``¬ ¬ ¬ ¬ ¬ AchievementsWidth = AchievementsText.get_width()``


128: ``¬ ¬ ¬ ¬ ¬ Credits_and_Change_Log_Text = ButtonFont5.render("Credits", self.aa, self.FontCol)``

129: ``¬ ¬ ¬ ¬ ¬ CreditsWidth = Credits_and_Change_Log_Text.get_width()``


130: ``¬ ¬ ¬ ¬ ¬ BenchmarkText = ButtonFont6.render("Benchmark", self.aa, self.FontCol)``

131: ``¬ ¬ ¬ ¬ ¬ BenchmarkWidth = BenchmarkText.get_width()``


132: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

133: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``

134: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

135: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

136: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "saveANDexit"``

137: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYDOWN:``

138: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:``

139: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``

140: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``

141: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``

142: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``

143: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``

144: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``

145: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``

146: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:``

147: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True``

148: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONUP:``

149: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``


150: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Home screen")``


151: ``¬ ¬ ¬ ¬ ¬ ButtonFont1.set_underline(hover1)``

152: ``¬ ¬ ¬ ¬ ¬ ButtonFont2.set_underline(hover2)``

153: ``¬ ¬ ¬ ¬ ¬ ButtonFont3.set_underline(hover3)``

154: ``¬ ¬ ¬ ¬ ¬ ButtonFont4.set_underline(hover4)``

155: ``¬ ¬ ¬ ¬ ¬ ButtonFont5.set_underline(hover5)``

156: ``¬ ¬ ¬ ¬ ¬ ButtonFont6.set_underline(hover6)``


157: ``¬ ¬ ¬ ¬ ¬ if My >= 202*yScaleFact and My <= 247*yScaleFact and Mx >= (self.realWidth-(PlayWidth+SelectorWidth))-2:``

158: ``¬ ¬ ¬ ¬ ¬ ¬ hover1 = True``

159: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

160: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

161: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

162: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Play"``

163: ``¬ ¬ ¬ ¬ ¬ else:``

164: ``¬ ¬ ¬ ¬ ¬ ¬ hover1 = False``


165: ``¬ ¬ ¬ ¬ ¬ if My >= 252*yScaleFact and My <= 297*yScaleFact and Mx >= (self.realWidth-(SettingsWidth+SelectorWidth))-2:``

166: ``¬ ¬ ¬ ¬ ¬ ¬ hover2 = True``

167: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

168: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

169: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

170: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

171: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

172: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Settings"``

173: ``¬ ¬ ¬ ¬ ¬ else:``

174: ``¬ ¬ ¬ ¬ ¬ ¬ hover2 = False``


175: ``¬ ¬ ¬ ¬ ¬ if My >= 302*yScaleFact and My <= 347*yScaleFact and Mx >= (self.realWidth-(CharDesignerWidth+SelectorWidth)-2):``

176: ``¬ ¬ ¬ ¬ ¬ ¬ hover3 = True``

177: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

178: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

179: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

180: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

181: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

182: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "CharacterDesigner"``

183: ``¬ ¬ ¬ ¬ ¬ else:``

184: ``¬ ¬ ¬ ¬ ¬ ¬ hover3 = False``


185: ``¬ ¬ ¬ ¬ ¬ if My >= 402*yScaleFact and My <= 447*yScaleFact and Mx >= (self.realWidth-(AchievementsWidth+SelectorWidth)-2):``

186: ``¬ ¬ ¬ ¬ ¬ ¬ hover4 = True``

187: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

188: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

189: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

190: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

191: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

192: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Achievements"``

193: ``¬ ¬ ¬ ¬ ¬ else:``

194: ``¬ ¬ ¬ ¬ ¬ ¬ hover4 = False``


195: ``¬ ¬ ¬ ¬ ¬ if My >= 352*yScaleFact and My <= 397*yScaleFact and Mx >= (self.realWidth-(CreditsWidth+SelectorWidth)-2):``

196: ``¬ ¬ ¬ ¬ ¬ ¬ hover5 = True``

197: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

198: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

199: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

200: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

201: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

202: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Credits"``

203: ``¬ ¬ ¬ ¬ ¬ else:``

204: ``¬ ¬ ¬ ¬ ¬ ¬ hover5 = False``


205: ``¬ ¬ ¬ ¬ ¬ if My >= 452*yScaleFact and My <= 497*yScaleFact and Mx >= (self.realWidth-(BenchmarkWidth+SelectorWidth)-2):``

206: ``¬ ¬ ¬ ¬ ¬ ¬ hover6 = True``

207: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

208: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

209: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

210: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

211: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

212: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Benchmark"``

213: ``¬ ¬ ¬ ¬ ¬ else:``

214: ``¬ ¬ ¬ ¬ ¬ ¬ hover6 = False``


215: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``


216: ``¬ ¬ ¬ ¬ ¬ if self.FromPlay == True:``

217: ``¬ ¬ ¬ ¬ ¬ ¬ self.FromPlay = False``

218: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_HomeScreen__.GenerateHomeScreen.DisplayMessage(self, MessageFont, "Loading", self.AccentCol)``


219: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))``


220: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Name, (0, (self.realHeight-NameHeight)))``

221: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Version, ((self.realWidth-VersionWidth)-2, (self.realHeight-VersionHeight)))``


222: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Play, ((self.realWidth-PlayWidth)-2, 200*yScaleFact))``

223: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(SettingsText, ((self.realWidth-SettingsWidth)-2, 250*yScaleFact))``

224: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Character_DesignerText, ((self.realWidth-CharDesignerWidth)-2, 300*yScaleFact))``

225: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits_and_Change_Log_Text, ((self.realWidth-CreditsWidth)-2, 350*yScaleFact))``

226: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsText, ((self.realWidth-AchievementsWidth)-2, 400*yScaleFact))``

227: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkText, ((self.realWidth-BenchmarkWidth)-2, 450*yScaleFact))``


228: ``¬ ¬ ¬ ¬ ¬ if hover1 == True:``

229: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(PlayWidth+SelectorWidth)-2, 200*yScaleFact))``

230: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

231: ``¬ ¬ ¬ ¬ ¬ elif hover2 == True:``

232: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(SettingsWidth+SelectorWidth)-2, 250*yScaleFact))``

233: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

234: ``¬ ¬ ¬ ¬ ¬ elif hover3 == True:``

235: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(CharDesignerWidth+SelectorWidth)-2, 300*yScaleFact))``

236: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

237: ``¬ ¬ ¬ ¬ ¬ elif hover5 == True:``

238: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(CreditsWidth+SelectorWidth)-2, 350*yScaleFact))``

239: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

240: ``¬ ¬ ¬ ¬ ¬ elif hover4 == True:``

241: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(AchievementsWidth+SelectorWidth)-2, 400*yScaleFact))``

242: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

243: ``¬ ¬ ¬ ¬ ¬ elif hover6 == True:``

244: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(BenchmarkWidth+SelectorWidth)-2, 450*yScaleFact))``

245: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

246: ``¬ ¬ ¬ ¬ ¬ else:``

247: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_ARROW)``


248: ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``

249: ``¬ ¬ ¬ ¬ ¬ if not Message == None:``

250: ``¬ ¬ ¬ ¬ ¬ ¬ return Message, None``


251: ``¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, xScaleFact, yScaleFact, coloursARRAY)``


252: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

253: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``

254: ``¬ ¬ ¬ except Exception as Message:``

255: ``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``

256: ``¬ ¬ ¬ ¬ return Message, None``

257: ``else:``
258: ``¬ print("You need to run this as part of Pycraft")``
259: ``¬ import tkinter as tk``
260: ``¬ from tkinter import messagebox``
261: ``¬ root = tk.Tk()``
262: ``¬ root.withdraw()``
263: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
264: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_ImageUtils>")``
        3: ``¬ class ConvertImage:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def pilImageToSurface(self, pilImage):``

7: ``¬ ¬ ¬ return self.mod_Pygame__.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode).convert()``

8: ``else:``
9: ``¬ print("You need to run this as part of Pycraft")``
10: ``¬ import tkinter as tk``
11: ``¬ from tkinter import messagebox``
12: ``¬ root = tk.Tk()``
13: ``¬ root.withdraw()``
14: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
15: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_Inventory>")``
        3: ``¬ class GenerateInventory:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def Inventory(self):``

7: ``¬ ¬ ¬ try:``

8: ``¬ ¬ ¬ ¬ Message = self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``

9: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

10: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``


11: ``¬ ¬ ¬ ¬ MainInventoryFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``

12: ``¬ ¬ ¬ ¬ PycraftTitle = MainInventoryFont.render("Pycraft", self.aa, self.FontCol)``

13: ``¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``


14: ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``

15: ``¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

16: ``¬ ¬ ¬ ¬ AlphaSurface = self.mod_Pygame__.Surface((realWidth, realHeight), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)``

17: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``

18: ``¬ ¬ ¬ ¬ AlphaSurface.set_alpha(204)``

19: ``¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``


20: ``¬ ¬ ¬ ¬ Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()``

21: ``¬ ¬ ¬ ¬ SelectorWidth = Selector.get_width()``


22: ``¬ ¬ ¬ ¬ hover1 = False``

23: ``¬ ¬ ¬ ¬ hover2 = False``

24: ``¬ ¬ ¬ ¬ hover3 = False``

25: ``¬ ¬ ¬ ¬ hover4 = False``

26: ``¬ ¬ ¬ ¬ hover5 = False``

27: ``¬ ¬ ¬ ¬ hover6 = False``

28: ``¬ ¬ ¬ ¬ hover7 = False``

29: ``¬ ¬ ¬ ¬ hover8 = False``

30: ``¬ ¬ ¬ ¬ mousebuttondown = False``


31: ``¬ ¬ ¬ ¬ ButtonFont1 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

32: ``¬ ¬ ¬ ¬ WeaponsText = ButtonFont1.render("Weapons", self.aa, self.FontCol)``

33: ``¬ ¬ ¬ ¬ WeaponsTextWidth = WeaponsText.get_width()``

34: ``¬ ¬ ¬ ¬ WeaponsTextHeight = WeaponsText.get_height()``


35: ``¬ ¬ ¬ ¬ ButtonFont2 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

36: ``¬ ¬ ¬ ¬ RangedWeaponsText = ButtonFont2.render("Ranged Weapons", self.aa, self.FontCol)``

37: ``¬ ¬ ¬ ¬ RangedWeaponsTextWidth = RangedWeaponsText.get_width()``

38: ``¬ ¬ ¬ ¬ RangedWeaponsTextHeight= RangedWeaponsText.get_height()``


39: ``¬ ¬ ¬ ¬ ButtonFont3 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

40: ``¬ ¬ ¬ ¬ ShieldsText = ButtonFont3.render("Shields", self.aa, self.FontCol)``

41: ``¬ ¬ ¬ ¬ ShieldsTextWidth = ShieldsText.get_width()``

42: ``¬ ¬ ¬ ¬ ShieldsTextHeight = ShieldsText.get_height()``


43: ``¬ ¬ ¬ ¬ ButtonFont4 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

44: ``¬ ¬ ¬ ¬ ArmourText = ButtonFont4.render("Armour", self.aa, self.FontCol)``

45: ``¬ ¬ ¬ ¬ ArmourTextWidth = ArmourText.get_width()``

46: ``¬ ¬ ¬ ¬ ArmourTextHeight = ArmourText.get_height()``


47: ``¬ ¬ ¬ ¬ ButtonFont5 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

48: ``¬ ¬ ¬ ¬ FoodText = ButtonFont5.render("Food", self.aa, self.FontCol)``

49: ``¬ ¬ ¬ ¬ FoodTextWidth = FoodText.get_width()``

50: ``¬ ¬ ¬ ¬ FoodTextHeight = FoodText.get_height()``


51: ``¬ ¬ ¬ ¬ ButtonFont6 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

52: ``¬ ¬ ¬ ¬ ItemsText = ButtonFont6.render("Items", self.aa, self.FontCol)``

53: ``¬ ¬ ¬ ¬ ItemsTextWidth = ItemsText.get_width()``

54: ``¬ ¬ ¬ ¬ ItemsTextHeight = ItemsText.get_height()``


55: ``¬ ¬ ¬ ¬ ButtonFont7 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

56: ``¬ ¬ ¬ ¬ SpecialItemsText = ButtonFont7.render("Special Items", self.aa, self.FontCol)``

57: ``¬ ¬ ¬ ¬ SpecialItemsTextWidth = SpecialItemsText.get_width()``

58: ``¬ ¬ ¬ ¬ SpecialItemsTextHeight = SpecialItemsText.get_height()``


59: ``¬ ¬ ¬ ¬ ButtonFont8 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

60: ``¬ ¬ ¬ ¬ OptionsText = ButtonFont7.render("Options", self.aa, self.FontCol)``

61: ``¬ ¬ ¬ ¬ OptionsTextWidth = OptionsText.get_width()``

62: ``¬ ¬ ¬ ¬ OptionsTextHeight = OptionsText.get_height()``


63: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Playing | Inventory")``


64: ``¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``


65: ``¬ ¬ ¬ ¬ while True:``

66: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``


67: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``

68: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``

69: ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``

70: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``


71: ``¬ ¬ ¬ ¬ ¬ yScaleFact = realHeight/720``

72: ``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``


73: ``¬ ¬ ¬ ¬ ¬ Mx, My = self.mod_Pygame__.mouse.get_pos()``

74: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``


75: ``¬ ¬ ¬ ¬ ¬ if self.aa == True:``

76: ``¬ ¬ ¬ ¬ ¬ ¬ pilImage = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png"))).resize((realWidth, realHeight), self.mod_PIL_Image_.ANTIALIAS)``

77: ``¬ ¬ ¬ ¬ ¬ else:``

78: ``¬ ¬ ¬ ¬ ¬ ¬ pilImage = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png"))).resize((realWidth, realHeight))``


79: ``¬ ¬ ¬ ¬ ¬ BLURRED_pilImage = pilImage.filter(self.mod_PIL_ImageFilter_.BoxBlur(4))``


80: ``¬ ¬ ¬ ¬ ¬ PauseImg = self.mod_ImageUtils__.ConvertImage.pilImageToSurface(self, BLURRED_pilImage)``

81: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(PauseImg, (0, 0))``

82: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AlphaSurface, (0, 0))``


83: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((realWidth-TitleWidth)/2, 0))``


84: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

85: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_e):``

86: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Load3D = False``

87: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

88: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

89: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``

90: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.VIDEORESIZE:``

91: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

92: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface = self.mod_Pygame__.Surface((realWidth, realHeight), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)``

93: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.set_alpha(204)``

94: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``

95: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:``

96: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True``

97: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONUP:``

98: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

99: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYDOWN:``

100: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``

101: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``

102: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface = self.mod_Pygame__.Surface((FullscreenX, FullscreenY), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)``

103: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.set_alpha(204)``

104: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``


105: ``¬ ¬ ¬ ¬ ¬ if My >= 202*yScaleFact and My <= 247*yScaleFact and Mx >= 1155:``

106: ``¬ ¬ ¬ ¬ ¬ ¬ hover1 = True``

107: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

108: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

109: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

110: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

111: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

112: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

113: ``¬ ¬ ¬ ¬ ¬ else:``

114: ``¬ ¬ ¬ ¬ ¬ ¬ hover1 = False``


115: ``¬ ¬ ¬ ¬ ¬ if My >= 252*yScaleFact and My <= 297*yScaleFact and Mx >= 1105:``

116: ``¬ ¬ ¬ ¬ ¬ ¬ hover2 = True``

117: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

118: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

119: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

120: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

121: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

122: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

123: ``¬ ¬ ¬ ¬ ¬ else:``

124: ``¬ ¬ ¬ ¬ ¬ ¬ hover2 = False``


125: ``¬ ¬ ¬ ¬ ¬ if My >= 302*yScaleFact and My <= 347*yScaleFact and Mx >= 865:``

126: ``¬ ¬ ¬ ¬ ¬ ¬ hover3 = True``

127: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

128: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

129: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

130: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

131: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

132: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

133: ``¬ ¬ ¬ ¬ ¬ else:``

134: ``¬ ¬ ¬ ¬ ¬ ¬ hover3 = False``


135: ``¬ ¬ ¬ ¬ ¬ if My >= 402*yScaleFact and My <= 447*yScaleFact and Mx >= 1035:``

136: ``¬ ¬ ¬ ¬ ¬ ¬ hover4 = True``

137: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

138: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

139: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

140: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

141: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

142: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

143: ``¬ ¬ ¬ ¬ ¬ else:``

144: ``¬ ¬ ¬ ¬ ¬ ¬ hover4 = False``


145: ``¬ ¬ ¬ ¬ ¬ if My >= 352*yScaleFact and My <= 397*yScaleFact and Mx >= 880:``

146: ``¬ ¬ ¬ ¬ ¬ ¬ hover5 = True``

147: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

148: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

149: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

150: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

151: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

152: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

153: ``¬ ¬ ¬ ¬ ¬ else:``

154: ``¬ ¬ ¬ ¬ ¬ ¬ hover5 = False``


155: ``¬ ¬ ¬ ¬ ¬ if My >= 502*yScaleFact and My <= 547*yScaleFact and Mx >= 1095:``

156: ``¬ ¬ ¬ ¬ ¬ ¬ hover6 = True``

157: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

158: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

159: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

160: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

161: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

162: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

163: ``¬ ¬ ¬ ¬ ¬ else:``

164: ``¬ ¬ ¬ ¬ ¬ ¬ hover6 = False``


165: ``¬ ¬ ¬ ¬ ¬ if My >= 452*yScaleFact and My <= 497*yScaleFact and Mx >= 1095:``

166: ``¬ ¬ ¬ ¬ ¬ ¬ hover7 = True``

167: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

168: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

169: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

170: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

171: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

172: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

173: ``¬ ¬ ¬ ¬ ¬ else:``

174: ``¬ ¬ ¬ ¬ ¬ ¬ hover7 = False``


175: ``¬ ¬ ¬ ¬ ¬ if My >= 552*yScaleFact and My <= 597*yScaleFact and Mx >= 1095:``

176: ``¬ ¬ ¬ ¬ ¬ ¬ hover8 = True``

177: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

178: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

179: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

180: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

181: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

182: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

183: ``¬ ¬ ¬ ¬ ¬ else:``

184: ``¬ ¬ ¬ ¬ ¬ ¬ hover8 = False``


185: ``¬ ¬ ¬ ¬ ¬ ButtonFont1.set_underline(hover1)``

186: ``¬ ¬ ¬ ¬ ¬ ButtonFont2.set_underline(hover2)``

187: ``¬ ¬ ¬ ¬ ¬ ButtonFont3.set_underline(hover3)``

188: ``¬ ¬ ¬ ¬ ¬ ButtonFont4.set_underline(hover4)``

189: ``¬ ¬ ¬ ¬ ¬ ButtonFont5.set_underline(hover5)``

190: ``¬ ¬ ¬ ¬ ¬ ButtonFont6.set_underline(hover6)``

191: ``¬ ¬ ¬ ¬ ¬ ButtonFont7.set_underline(hover7)``

192: ``¬ ¬ ¬ ¬ ¬ ButtonFont8.set_underline(hover8)``

193: ``¬ ¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``


194: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(WeaponsText, ((realWidth-WeaponsTextWidth)-2, 200*yScaleFact)) # ???``


195: ``¬ ¬ ¬ ¬ ¬ if hover1 == True:``

196: ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(WeaponsTextWidth+SelectorWidth)-2, 200*yScaleFact))``


197: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(RangedWeaponsText, ((realWidth-RangedWeaponsTextWidth)-2, 250*yScaleFact))``

198: ``¬ ¬ ¬ ¬ ¬ if hover2 == True:``

199: ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(RangedWeaponsTextWidth+SelectorWidth)-2, 250*yScaleFact))``


200: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(ShieldsText, ((realWidth-ShieldsTextWidth)-2, 300*yScaleFact))``

201: ``¬ ¬ ¬ ¬ ¬ if hover3 == True:``

202: ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(ShieldsTextWidth+SelectorWidth)-2, 300*yScaleFact))``


203: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(ArmourText, ((realWidth-ArmourTextWidth)-2, 350*yScaleFact))``

204: ``¬ ¬ ¬ ¬ ¬ if hover4 == True:``

205: ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(FoodTextWidth+SelectorWidth)-2, 400*yScaleFact))``


206: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(FoodText, ((realWidth-FoodTextWidth)-2, 400*yScaleFact))``

207: ``¬ ¬ ¬ ¬ ¬ if hover5 == True:``

208: ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(ArmourTextWidth+SelectorWidth)-2, 350*yScaleFact))``


209: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(ItemsText, ((realWidth-ItemsTextWidth)-2, 450*yScaleFact))``

210: ``¬ ¬ ¬ ¬ ¬ if hover6 == True:``

211: ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(SpecialItemsTextWidth+SelectorWidth)-2, 500*yScaleFact))``


212: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(SpecialItemsText, ((realWidth-SpecialItemsTextWidth)-2, 500*yScaleFact))``

213: ``¬ ¬ ¬ ¬ ¬ if hover7 == True:``

214: ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(ItemsTextWidth+SelectorWidth)-2, 450*yScaleFact))``


215: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(OptionsText, ((realWidth-OptionsTextWidth)-2, 550*yScaleFact))``

216: ``¬ ¬ ¬ ¬ ¬ if hover8 == True:``

217: ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(OptionsTextWidth+SelectorWidth)-2, 550*yScaleFact))``


218: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``

219: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)``

220: ``¬ ¬ ¬ except Exception as Message:``

221: ``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``

222: ``¬ ¬ ¬ ¬ return Message``

223: ``else:``
224: ``¬ print("You need to run this as part of Pycraft")``
225: ``¬ import tkinter as tk``
226: ``¬ from tkinter import messagebox``
227: ``¬ root = tk.Tk()``
228: ``¬ root.withdraw()``
229: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
230: ``¬ quit()``


1: ``print("Started <Pycraft_main>")``

2: ``class Startup:``

3: ``¬ def __init__(Class_Startup_variables):``

4: ``¬ ¬ try:``

5: ``¬ ¬ ¬ import tkinter as tk``

6: ``¬ ¬ ¬ Class_Startup_variables.mod_Tkinter__tk = tk # [Class_Startup_variables] mod (module) (module name) (subsection of module) (name references)``

7: ``¬ ¬ ¬ import tkinter.ttk  # Class _ <class_name> _ variables``

8: ``¬ ¬ ¬ Class_Startup_variables.mod_Tkinter_ttk_ = tkinter.ttk``

9: ``¬ ¬ ¬ from tkinter import messagebox``

10: ``¬ ¬ ¬ Class_Startup_variables.mod_Tkinter_messagebox_ = messagebox``

11: ``¬ ¬ ¬ from PIL import Image, ImageFilter, ImageGrab, ImageTk``

12: ``¬ ¬ ¬ Class_Startup_variables.mod_PIL_Image_ = Image``

13: ``¬ ¬ ¬ Class_Startup_variables.mod_PIL_ImageFilter_ = ImageFilter``

14: ``¬ ¬ ¬ Class_Startup_variables.mod_PIL_ImageTk_ = ImageTk``

15: ``¬ ¬ ¬ Class_Startup_variables.mod_PIL_ImageGrab_ = ImageGrab``

16: ``¬ ¬ ¬ import pygame``

17: ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__ = pygame``

18: ``¬ ¬ ¬ import numpy``

19: ``¬ ¬ ¬ Class_Startup_variables.mod_Numpy__ = numpy``

20: ``¬ ¬ ¬ import os``

21: ``¬ ¬ ¬ Class_Startup_variables.mod_OS__ = os``

22: ``¬ ¬ ¬ import sys``

23: ``¬ ¬ ¬ Class_Startup_variables.mod_Sys__ = sys``

24: ``¬ ¬ ¬ import random``

25: ``¬ ¬ ¬ Class_Startup_variables.mod_Random__ = random``

26: ``¬ ¬ ¬ import time``

27: ``¬ ¬ ¬ Class_Startup_variables.mod_Time__ = time``

28: ``¬ ¬ ¬ import pygame.locals``

29: ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame_locals_ = pygame.locals``

30: ``¬ ¬ ¬ import OpenGL``

31: ``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL__ = OpenGL``

32: ``¬ ¬ ¬ import OpenGL.GL``

33: ``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL_GL_ = OpenGL.GL``

34: ``¬ ¬ ¬ import OpenGL.GLU``

35: ``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL_GLU_ = OpenGL.GLU``

36: ``¬ ¬ ¬ import OpenGL.GLUT``

37: ``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL_GLUT_ = OpenGL.GLUT``

38: ``¬ ¬ ¬ import moderngl``

39: ``¬ ¬ ¬ Class_Startup_variables.mod_ModernGL__ = moderngl``

40: ``¬ ¬ ¬ import moderngl_window``

41: ``¬ ¬ ¬ Class_Startup_variables.mod_ModernGL_window_ = moderngl_window``

42: ``¬ ¬ ¬ import pyautogui``

43: ``¬ ¬ ¬ Class_Startup_variables.mod_Pyautogui__ = pyautogui``

44: ``¬ ¬ ¬ import psutil``

45: ``¬ ¬ ¬ Class_Startup_variables.mod_Psutil__ = psutil``

46: ``¬ ¬ ¬ import pywavefront``

47: ``¬ ¬ ¬ Class_Startup_variables.mod_Pywavefront__ = pywavefront``

48: ``¬ ¬ ¬ import timeit``

49: ``¬ ¬ ¬ Class_Startup_variables.mod_Timeit__ = timeit``

50: ``¬ ¬ ¬ import subprocess``

51: ``¬ ¬ ¬ Class_Startup_variables.mod_Subprocess__ = subprocess``

52: ``¬ ¬ ¬ import traceback``

53: ``¬ ¬ ¬ Class_Startup_variables.mod_Traceback__ = traceback``

54: ``¬ ¬ ¬ import datetime``

55: ``¬ ¬ ¬ Class_Startup_variables.mod_Datetime__ = datetime``

56: ``¬ ¬ ¬ import ctypes``

57: ``¬ ¬ ¬ Class_Startup_variables.mod_Ctypes__ = ctypes``

58: ``¬ ¬ ¬ import json``

59: ``¬ ¬ ¬ Class_Startup_variables.mod_JSON__ = json``

60: ``¬ ¬ ¬ import threading``

61: ``¬ ¬ ¬ Class_Startup_variables.mod_Threading__ = threading``

62: ``¬ ¬ ¬ import cpuinfo``

63: ``¬ ¬ ¬ Class_Startup_variables.mod_CPUinfo__ = cpuinfo``

64: ``¬ ¬ ¬ import array``

65: ``¬ ¬ ¬ Class_Startup_variables.mod_Array__ = array``

66: ``¬ ¬ ¬ import GPUtil``

67: ``¬ ¬ ¬ Class_Startup_variables.mod_GPUtil__ = GPUtil``

68: ``¬ ¬ ¬ from tabulate import tabulate``

69: ``¬ ¬ ¬ Class_Startup_variables.mod_Tabulate_tabulate_ = tabulate``

70: ``¬ ¬ ¬ from pyrr import Matrix44``

71: ``¬ ¬ ¬ Class_Startup_variables.mod_Pyrr_Matrix44_ = Matrix44``


72: ``¬ ¬ ¬ moderngl.create_standalone_context()``


73: ``¬ ¬ ¬ os.environ['SDL_VIDEO_CENTERED'] = '1'``


74: ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.init()``


75: ``¬ ¬ ¬ import PycraftStartupTest``

76: ``¬ ¬ ¬ Class_Startup_variables.mod_PycraftStartupTest__ = PycraftStartupTest``

77: ``¬ ¬ ¬ import StartupAnimation``

78: ``¬ ¬ ¬ Class_Startup_variables.mod_StartupAnimation__ = StartupAnimation``

79: ``¬ ¬ ¬ import DisplayUtils``

80: ``¬ ¬ ¬ Class_Startup_variables.mod_DisplayUtils__ = DisplayUtils``

81: ``¬ ¬ ¬ import GetSavedData``

82: ``¬ ¬ ¬ Class_Startup_variables.mod_GetSavedData__ = GetSavedData``

83: ``¬ ¬ ¬ import ThemeUtils``

84: ``¬ ¬ ¬ Class_Startup_variables.mod_ThemeUtils__ = ThemeUtils``

85: ``¬ ¬ ¬ import HomeScreen``

86: ``¬ ¬ ¬ Class_Startup_variables.mod_HomeScreen__ = HomeScreen``

87: ``¬ ¬ ¬ import SoundUtils``

88: ``¬ ¬ ¬ Class_Startup_variables.mod_SoundUtils__ = SoundUtils``

89: ``¬ ¬ ¬ import DrawingUtils``

90: ``¬ ¬ ¬ Class_Startup_variables.mod_DrawingUtils__ = DrawingUtils``

91: ``¬ ¬ ¬ import CaptionUtils``

92: ``¬ ¬ ¬ Class_Startup_variables.mod_CaptionUtils__ = CaptionUtils``

93: ``¬ ¬ ¬ import Credits``

94: ``¬ ¬ ¬ Class_Startup_variables.mod_Credits__ = Credits``

95: ``¬ ¬ ¬ import TkinterUtils``

96: ``¬ ¬ ¬ Class_Startup_variables.mod_TkinterUtils__ = TkinterUtils``

97: ``¬ ¬ ¬ import Achievements``

98: ``¬ ¬ ¬ Class_Startup_variables.mod_Achievements__ = Achievements``

99: ``¬ ¬ ¬ import CharacterDesigner``

100: ``¬ ¬ ¬ Class_Startup_variables.mod_CharacterDesigner__ = CharacterDesigner``

101: ``¬ ¬ ¬ import Settings``

102: ``¬ ¬ ¬ Class_Startup_variables.mod_Settings__ = Settings``

103: ``¬ ¬ ¬ import Benchmark``

104: ``¬ ¬ ¬ Class_Startup_variables.mod_Benchmark__ = Benchmark``

105: ``¬ ¬ ¬ import ExBenchmark``

106: ``¬ ¬ ¬ Class_Startup_variables.mod_ExBenchmark__ = ExBenchmark``

107: ``¬ ¬ ¬ import OGLbenchmark``

108: ``¬ ¬ ¬ Class_Startup_variables.mod_OGLbenchmark__ = OGLbenchmark``

109: ``¬ ¬ ¬ import base``

110: ``¬ ¬ ¬ Class_Startup_variables.mod_Base__ = base``

111: ``¬ ¬ ¬ import ShareDataUtil``

112: ``¬ ¬ ¬ Class_Startup_variables.mod_Globals__ = ShareDataUtil``

113: ``¬ ¬ ¬ import TextUtils``

114: ``¬ ¬ ¬ Class_Startup_variables.mod_TextUtils__ = TextUtils``

115: ``¬ ¬ ¬ import Inventory``

116: ``¬ ¬ ¬ Class_Startup_variables.mod_Inventory__ = Inventory``

117: ``¬ ¬ ¬ import ImageUtils``

118: ``¬ ¬ ¬ Class_Startup_variables.mod_ImageUtils__ = ImageUtils``

119: ``¬ ¬ ¬ import MapGUI``

120: ``¬ ¬ ¬ Class_Startup_variables.mod_MapGUI__ = MapGUI``

121: ``¬ ¬ ¬ import ThreadingUtil``

122: ``¬ ¬ ¬ Class_Startup_variables.mod_ThreadingUtil__ = ThreadingUtil``


123: ``¬ ¬ ¬ Class_Startup_variables.aa = True``

124: ``¬ ¬ ¬ Class_Startup_variables.AccentCol = (237, 125, 49)``

125: ``¬ ¬ ¬ Class_Startup_variables.aFPS = 0``

126: ``¬ ¬ ¬ Class_Startup_variables.BackgroundCol = [30, 30, 30]``

127: ``¬ ¬ ¬ Class_Startup_variables.base_folder = os.path.dirname(__file__)``

128: ``¬ ¬ ¬ Class_Startup_variables.cameraANGspeed = 3.5``

129: ``¬ ¬ ¬ Class_Startup_variables.clock = pygame.time.Clock()``

130: ``¬ ¬ ¬ Class_Startup_variables.Collisions = [False, 0]``

131: ``¬ ¬ ¬ Class_Startup_variables.CompletePercent = 0``

132: ``¬ ¬ ¬ Class_Startup_variables.ctx = 0``

133: ``¬ ¬ ¬ Class_Startup_variables.Load_Progress = 0``

134: ``¬ ¬ ¬ Class_Startup_variables.crash = False``

135: ``¬ ¬ ¬ Class_Startup_variables.CurrentlyPlaying = None``


136: ``¬ ¬ ¬ Class_Startup_variables.Data_aFPS_Min = 60``

137: ``¬ ¬ ¬ Class_Startup_variables.Data_aFPS = []``

138: ``¬ ¬ ¬ Class_Startup_variables.Data_aFPS_Max = 1``


139: ``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Min = 60``

140: ``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE = []``

141: ``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Max = 1``


142: ``¬ ¬ ¬ Class_Startup_variables.Data_eFPS_Min = 60``

143: ``¬ ¬ ¬ Class_Startup_variables.Data_eFPS = []``

144: ``¬ ¬ ¬ Class_Startup_variables.Data_eFPS_Max = 1``


145: ``¬ ¬ ¬ Class_Startup_variables.Data_MemUsE_Min = 60``

146: ``¬ ¬ ¬ Class_Startup_variables.Data_MemUsE = []``

147: ``¬ ¬ ¬ Class_Startup_variables.Data_MemUsE_Max = 1``


148: ``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Min = 60``

149: ``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE = []``

150: ``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Max = 1``


151: ``¬ ¬ ¬ Class_Startup_variables.Devmode = 0``

152: ``¬ ¬ ¬ Class_Startup_variables.Display = 0``

153: ``¬ ¬ ¬ Class_Startup_variables.eFPS = 60``

154: ``¬ ¬ ¬ Class_Startup_variables.FanSky = True``

155: ``¬ ¬ ¬ Class_Startup_variables.FanPart = True``

156: ``¬ ¬ ¬ Class_Startup_variables.FontCol = (255, 255, 255)``

157: ``¬ ¬ ¬ Class_Startup_variables.FOV = 70``

158: ``¬ ¬ ¬ Class_Startup_variables.FromPlay = False``

159: ``¬ ¬ ¬ Class_Startup_variables.Fullscreen = False``

160: ``¬ ¬ ¬ Class_Startup_variables.FPS = 60``

161: ``¬ ¬ ¬ Class_Startup_variables.FullscreenX, Class_Startup_variables.FullscreenY = pyautogui.size()``

162: ``¬ ¬ ¬ Class_Startup_variables.GameError = None``

163: ``¬ ¬ ¬ Class_Startup_variables.G3Dscale = 600000``

164: ``¬ ¬ ¬ Class_Startup_variables.GetScreenGraphics = True``

165: ``¬ ¬ ¬ Class_Startup_variables.HUD_Surface = None``

166: ``¬ ¬ ¬ Class_Startup_variables.Iteration = 1``

167: ``¬ ¬ ¬ Class_Startup_variables.lastRun = "29/09/2021"``

168: ``¬ ¬ ¬ Class_Startup_variables.Load3D = True``

169: ``¬ ¬ ¬ Class_Startup_variables.LoadMusic = True``


170: ``¬ ¬ ¬ Class_Startup_variables.Map = 0``

171: ``¬ ¬ ¬ Class_Startup_variables.Map_box = 0``

172: ``¬ ¬ ¬ Class_Startup_variables.Map_scale = 0``

173: ``¬ ¬ ¬ Class_Startup_variables.Map_size = 0``

174: ``¬ ¬ ¬ Class_Startup_variables.Map_trans = 0``

175: ``¬ ¬ ¬ Class_Startup_variables.MapVerts = 0``

176: ``¬ ¬ ¬ Class_Startup_variables.map_vertices = []``

177: ``¬ ¬ ¬ Class_Startup_variables.max_Map_size = 0``


178: ``¬ ¬ ¬ Class_Startup_variables.HUD_object = 0``

179: ``¬ ¬ ¬ Class_Startup_variables.HUD_box = 0``

180: ``¬ ¬ ¬ Class_Startup_variables.HUD_scale = 0``

181: ``¬ ¬ ¬ Class_Startup_variables.HUD_size = 0``

182: ``¬ ¬ ¬ Class_Startup_variables.HUD_trans = 0``

183: ``¬ ¬ ¬ Class_Startup_variables.HUDVerts = 0``

184: ``¬ ¬ ¬ Class_Startup_variables.HUD_vertices = []``

185: ``¬ ¬ ¬ Class_Startup_variables.max_HUD_size = 0``


186: ``¬ ¬ ¬ Class_Startup_variables.Map_max_v = 0``

187: ``¬ ¬ ¬ Class_Startup_variables.Map_min_v = 0``


188: ``¬ ¬ ¬ Class_Startup_variables.HUD_max_v = 0``

189: ``¬ ¬ ¬ Class_Startup_variables.HUD_min_v = 0``


190: ``¬ ¬ ¬ Class_Startup_variables.music = True``

191: ``¬ ¬ ¬ Class_Startup_variables.musicVOL = 5``

192: ``¬ ¬ ¬ Class_Startup_variables.Numpy_map_vertices = 0``

193: ``¬ ¬ ¬ Class_Startup_variables.Progress_Line = []``

194: ``¬ ¬ ¬ Class_Startup_variables.ProgressMessageText = "Initiating"``

195: ``¬ ¬ ¬ Class_Startup_variables.realHeight = 720``

196: ``¬ ¬ ¬ Class_Startup_variables.realWidth = 1280``

197: ``¬ ¬ ¬ Class_Startup_variables.RecommendedFPS = 60``

198: ``¬ ¬ ¬ Class_Startup_variables.RenderFOG = True``

199: ``¬ ¬ ¬ Class_Startup_variables.RunFullStartup = False``

200: ``¬ ¬ ¬ Class_Startup_variables.SecondFontCol = (100, 100, 100)``

201: ``¬ ¬ ¬ Class_Startup_variables.SavedWidth = 1280``

202: ``¬ ¬ ¬ Class_Startup_variables.SavedHeight = 720``

203: ``¬ ¬ ¬ Class_Startup_variables.ShapeCol = (80, 80, 80)``

204: ``¬ ¬ ¬ Class_Startup_variables.skybox_texture = 0``

205: ``¬ ¬ ¬ Class_Startup_variables.sound = True``

206: ``¬ ¬ ¬ Class_Startup_variables.soundVOL = 75``

207: ``¬ ¬ ¬ Class_Startup_variables.Stop_Thread_Event = Class_Startup_variables.mod_Threading__.Event()``

208: ``¬ ¬ ¬ Class_Startup_variables.SettingsPreference = "Medium"``

209: ``¬ ¬ ¬ Class_Startup_variables.theme = False``

210: ``¬ ¬ ¬ Class_Startup_variables.ThreadStatus = "Running"``

211: ``¬ ¬ ¬ Class_Startup_variables.Timer = 0``

212: ``¬ ¬ ¬ Class_Startup_variables.Total_move_x = 0``

213: ``¬ ¬ ¬ Class_Startup_variables.Total_move_y = 0``

214: ``¬ ¬ ¬ Class_Startup_variables.Total_move_z = 0``

215: ``¬ ¬ ¬ Class_Startup_variables.TotalRotation = 0``

216: ``¬ ¬ ¬ Class_Startup_variables.Total_Vertices = 0``

217: ``¬ ¬ ¬ Class_Startup_variables.version = "0.9.3"``

218: ``¬ ¬ ¬ Class_Startup_variables.vertex = 0``

219: ``¬ ¬ ¬ Class_Startup_variables.X = 0``

220: ``¬ ¬ ¬ Class_Startup_variables.Y = 0``

221: ``¬ ¬ ¬ Class_Startup_variables.Z = 0``


222: ``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.StartVariableChecking, args=(Class_Startup_variables,))``

223: ``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.start()``

224: ``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.name = "Thread_StartLongThread"``


225: ``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.StartCPUlogging, args=(Class_Startup_variables,))``

226: ``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.start()``

227: ``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.name = "Thread_GetCPUMetrics"``


228: ``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.AdaptiveMode, args=(Class_Startup_variables,))``

229: ``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.start()``

230: ``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.name = "Thread_AdaptiveMode"``


231: ``¬ ¬ ¬ Class_Startup_variables.mod_Globals__.Share.initialize(Class_Startup_variables)``


232: ``¬ ¬ ¬ import GameEngine``

233: ``¬ ¬ ¬ Class_Startup_variables.mod_MainGameEngine__ = GameEngine``

234: ``¬ ¬ except Exception as error:``

235: ``¬ ¬ ¬ print(error)``

236: ``¬ ¬ ¬ try:``

237: ``¬ ¬ ¬ ¬ import tkinter as tk``

238: ``¬ ¬ ¬ ¬ root = tk.Tk()``

239: ``¬ ¬ ¬ ¬ root.withdraw()``

240: ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Tkinter_messagebox_.showerror("Startup Fail", "Missing required modules")``

241: ``¬ ¬ ¬ ¬ quit()``

242: ``¬ ¬ ¬ except:``

243: ``¬ ¬ ¬ ¬ try:``

244: ``¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``

245: ``¬ ¬ ¬ ¬ ¬ sys.exit("0.0.0 -Thank you for playing")``

246: ``¬ ¬ ¬ ¬ except:``

247: ``¬ ¬ ¬ ¬ ¬ quit()``


248: ``¬ def crash(ErrorREPORT):``

249: ``¬ ¬ Class_Startup_variables.Stop_Thread_Event.set()``

250: ``¬ ¬ if not ErrorREPORT == None:``

251: ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``

252: ``¬ ¬ ¬ Class_Startup_variables.mod_Time__.sleep(1.01)``

253: ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.init()``

254: ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.mixer.stop()``

255: ``¬ ¬ ¬ try:``

256: ``¬ ¬ ¬ ¬ Message = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.SaveTOconfigFILE(Class_Startup_variables)``

257: ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.quit()``

258: ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.init()``

259: ``¬ ¬ ¬ ¬ Display = Class_Startup_variables.mod_Pygame__.display.set_mode((1280, 720))``

260: ``¬ ¬ ¬ ¬ icon = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``

261: ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.set_icon(icon)``

262: ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.set_caption(f"Pycraft: An Error Occurred")``


263: ``¬ ¬ ¬ ¬ MessageFont = Class_Startup_variables.mod_Pygame__.font.Font(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Fonts\\Book Antiqua.ttf")), 15)``


264: ``¬ ¬ ¬ ¬ ErrorMessageText = MessageFont.render(str(ErrorREPORT), True, (255,0,0))``

265: ``¬ ¬ ¬ ¬ ErrorMessageTextWidth = ErrorMessageText.get_width()``

266: ``¬ ¬ ¬ ¬ ErrorMessageTextHeight = ErrorMessageText.get_height()``

267: ``¬ ¬ ¬ ¬ Display = Class_Startup_variables.mod_Pygame__.display.set_mode((1280,720))``


268: ``¬ ¬ ¬ ¬ IconImage = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Resources\\Error_Resources\\Icon.jpg")))``

269: ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.set_icon(IconImage)``

270: ``¬ ¬ ¬ ¬ image = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Resources\\Error_Resources\\Error_Message.png")))``

271: ``¬ ¬ ¬ ¬ Clock = Class_Startup_variables.mod_Pygame__.time.Clock()``

272: ``¬ ¬ ¬ ¬ while True:``

273: ``¬ ¬ ¬ ¬ ¬ Display.fill((20,20,20))``

274: ``¬ ¬ ¬ ¬ ¬ Display.blit(image, (0,0))``


275: ``¬ ¬ ¬ ¬ ¬ Display.blit(ErrorMessageText, ((((1280/2)-ErrorMessageTextWidth)/2), (720-ErrorMessageTextHeight)/2))``


276: ``¬ ¬ ¬ ¬ ¬ for event in Class_Startup_variables.mod_Pygame__.event.get():``

277: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == Class_Startup_variables.mod_Pygame__.QUIT:``

278: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.join()``

279: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.join()``

280: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.join()``


281: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``

282: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit(f"0.1.0- Thank you for playing")``


283: ``¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.flip()``

284: ``¬ ¬ ¬ ¬ ¬ Clock.tick(30)``

285: ``¬ ¬ ¬ except Exception as error:``

286: ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit(f"0.2.0- {error} Thank you for playing")``

287: ``¬ ¬ else:``

288: ``¬ ¬ ¬ try:``

289: ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``

290: ``¬ ¬ ¬ except Exception as error:``

291: ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit(f"0.3.0- {error} Thank you for playing")``

292: ``¬ ¬ ¬ ¬ quit()``

293: ``¬ ¬ ¬ else:``

294: ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit("0.4.0- Thank you for playing")``

295: ``¬ ¬ ¬ ¬ quit()``


296: ``Class_Startup_variables = Startup()``

297: ``try:``

298: ``¬ Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.ReadMainSave(Class_Startup_variables)``

299: ``except Exception as FileError:``

300: ``¬ try:``

301: ``¬ ¬ if str(FileError) == "Expecting value: line 1 column 1 (char 0)":``

302: ``¬ ¬ ¬ Report = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.RepairLostSave(Class_Startup_variables)``

303: ``¬ ¬ ¬ ErrorString = "Unable to access vital Saved Data, have attempted a fix successfully", FileError``

304: ``¬ ¬ ¬ Message = "0.0.0- " + str(ErrorString)``

305: ``¬ ¬ ¬ Startup.crash(Message)``

306: ``¬ except Exception as Error:``

307: ``¬ ¬ Message = "0.0.1- " + str(Error)``

308: ``¬ ¬ Startup.crash(Message)``


309: ``¬ Message = "0.2- " + str(FileError)``

310: ``¬ Startup.crash(Message)``


311: ``Message = Class_Startup_variables.mod_PycraftStartupTest__.StartupTest.PycraftSelfTest(Class_Startup_variables)``

312: ``if not Message == None:``

313: ``¬ Message = "0.0.3- " + str(Message)``

314: ``¬ Startup.crash(Message)``


315: ``if Class_Startup_variables.theme == False:``

316: ``¬ Message = Class_Startup_variables.mod_ThemeUtils__.DetermineThemeColours.GetThemeGUI(Class_Startup_variables)``

317: ``¬ if not Message == None:``

318: ``¬ ¬ Message = "0.0.4- " + str(Message)``

319: ``¬ ¬ Startup.crash(Message)``


320: ``Message = Class_Startup_variables.mod_ThemeUtils__.DetermineThemeColours.GetColours(Class_Startup_variables)``


321: ``if not Message == None:``

322: ``¬ Message = "0.0.5- " + str(Message)``

323: ``¬ Startup.crash(Message)``


324: ``Message = Class_Startup_variables.mod_StartupAnimation__.GenerateStartupScreen.Start(Class_Startup_variables)``

325: ``if not Message == None:``

326: ``¬ Message = "0.0.6- " + str(Message)``

327: ``¬ Startup.crash(Message)``


328: ``Class_Startup_variables.Command = "Undefined"``

329: ``while True:``

330: ``¬ if Class_Startup_variables.Command == "saveANDexit":``

331: ``¬ ¬ Message = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.SaveTOconfigFILE(Class_Startup_variables)``

332: ``¬ ¬ if not Message == None:``

333: ``¬ ¬ ¬ Message = "0.0.7- " + str(Message)``

334: ``¬ ¬ ¬ Startup.crash(Message)``

335: ``¬ ¬ else:``

336: ``¬ ¬ ¬ Class_Startup_variables.Stop_Thread_Event.set()``


337: ``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.join()``

338: ``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.join()``

339: ``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.join()``


340: ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``

341: ``¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit("0.5.0- Thank you for playing") # 0 = Order of running, 5 = 5th occurrence down page``

342: ``¬ elif Class_Startup_variables.Command == "Credits":``

343: ``¬ ¬ Message = Class_Startup_variables.mod_Credits__.GenerateCredits.Credits(Class_Startup_variables)``

344: ``¬ ¬ if not Message == None:``

345: ``¬ ¬ ¬ Message = "0.0.8- " + str(Message)``

346: ``¬ ¬ ¬ Startup.crash(Message)``

347: ``¬ ¬ Class_Startup_variables.Command = "Undefined"``

348: ``¬ elif Class_Startup_variables.Command == "Achievements":``

349: ``¬ ¬ Message = Class_Startup_variables.mod_Achievements__.GenerateAchievements.Achievements(Class_Startup_variables)``

350: ``¬ ¬ if not Message == None:``

351: ``¬ ¬ ¬ Message = "0.0.9- " + str(Message)``

352: ``¬ ¬ ¬ Startup.crash(Message)``

353: ``¬ ¬ Class_Startup_variables.Command = "Undefined"``

354: ``¬ elif Class_Startup_variables.Command == "CharacterDesigner":``

355: ``¬ ¬ Message = Class_Startup_variables.mod_CharacterDesigner__.GenerateCharacterDesigner.CharacterDesigner(Class_Startup_variables)``

356: ``¬ ¬ if not Message == None:``

357: ``¬ ¬ ¬ Message = "0.0.10- " + str(Message)``

358: ``¬ ¬ ¬ Startup.crash(Message)``

359: ``¬ ¬ Class_Startup_variables.Command = "Undefined"``

360: ``¬ elif Class_Startup_variables.Command == "Settings":``

361: ``¬ ¬ Message = Class_Startup_variables.mod_Settings__.GenerateSettings.settings(Class_Startup_variables)``

362: ``¬ ¬ if not Message == None:``

363: ``¬ ¬ ¬ Message = "0.0.11- " + str(Message)``

364: ``¬ ¬ ¬ Startup.crash(Message)``

365: ``¬ ¬ Class_Startup_variables.Command = "Undefined"``

366: ``¬ elif Class_Startup_variables.Command == "Benchmark":``

367: ``¬ ¬ Message = Class_Startup_variables.mod_Benchmark__.GenerateBenchmarkMenu.Benchmark(Class_Startup_variables)``

368: ``¬ ¬ if not Message == None:``

369: ``¬ ¬ ¬ Message = "0.0.12- " + str(Message)``

370: ``¬ ¬ ¬ Startup.crash(Message)``

371: ``¬ ¬ Class_Startup_variables.Command = "Undefined"``

372: ``¬ elif Class_Startup_variables.Command == "Play":``

373: ``¬ ¬ Message = Class_Startup_variables.mod_MainGameEngine__.CreateEngine.Play(Class_Startup_variables)``

374: ``¬ ¬ if Message == None:``

375: ``¬ ¬ ¬ Message = Class_Startup_variables.GameError``

376: ``¬ ¬ if not Message == None:``

377: ``¬ ¬ ¬ Message = "0.0.13- " + str(Message)``

378: ``¬ ¬ ¬ Startup.crash(Message)``

379: ``¬ ¬ Class_Startup_variables.mod_Pygame__.init()``

380: ``¬ ¬ Class_Startup_variables.FromPlay = True``

381: ``¬ ¬ Message = Class_Startup_variables.mod_DisplayUtils__.DisplayUtils.SetDisplay(Class_Startup_variables)``

382: ``¬ ¬ if not Message == None:``

383: ``¬ ¬ ¬ Message = "0.0.14- " + str(Message)``

384: ``¬ ¬ ¬ Startup.crash(Message)``

385: ``¬ elif Class_Startup_variables.Command == "Inventory":``

386: ``¬ ¬ Message = Class_Startup_variables.mod_Inventory__.GenerateInventory.Inventory(Class_Startup_variables)``

387: ``¬ ¬ if not Message == None:``

388: ``¬ ¬ ¬ Message = "0.0.15- " + str(Message)``

389: ``¬ ¬ ¬ Startup.crash(Message)``

390: ``¬ ¬ Class_Startup_variables.Command = "Play"``

391: ``¬ elif Class_Startup_variables.Command == "MapGUI":``

392: ``¬ ¬ Message = Class_Startup_variables.mod_MapGUI__.GenerateMapGUI.MapGUI(Class_Startup_variables)``

393: ``¬ ¬ if not Message == None:``

394: ``¬ ¬ ¬ Message = "0.0.16- " + str(Message)``

395: ``¬ ¬ ¬ Startup.crash(Message)``

396: ``¬ ¬ Class_Startup_variables.Command = "Play"``

397: ``¬ else:``

398: ``¬ ¬ Message, Class_Startup_variables.Command = Class_Startup_variables.mod_HomeScreen__.GenerateHomeScreen.Home_Screen(Class_Startup_variables)``

399: ``¬ ¬ if not Message == None:``

400: ``¬ ¬ ¬ Message = "0.0.17- " + str(Message)``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_MapGUI>")``
        3: ``¬ class GenerateMapGUI:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def GetMapPos(self):``

7: ``¬ ¬ ¬ x = 0``

8: ``¬ ¬ ¬ z = 0``

9: ``¬ ¬ ¬ if self.X == 0:``

10: ``¬ ¬ ¬ ¬ x = 640``

11: ``¬ ¬ ¬ if self.Z == 0:``

12: ``¬ ¬ ¬ ¬ z = 360``

13: ``¬ ¬ ¬ x -= 6``

14: ``¬ ¬ ¬ z -= 19``

15: ``¬ ¬ ¬ return (x,z)``



16: ``¬ ¬ def MapGUI(self):``

17: ``¬ ¬ ¬ try:``

18: ``¬ ¬ ¬ ¬ Message = self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``

19: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

20: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``


21: ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``

22: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``

23: ``¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png")))``

24: ``¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``

25: ``¬ ¬ ¬ ¬ MapIcon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Marker.jpg"))).convert()``

26: ``¬ ¬ ¬ ¬ zoom = 0``

27: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Playing | Map")``

28: ``¬ ¬ ¬ ¬ MouseUnlock = True``

29: ``¬ ¬ ¬ ¬ X,Y = 0, 0``

30: ``¬ ¬ ¬ ¬ key = ""``

31: ``¬ ¬ ¬ ¬ while True:``

32: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``


33: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``

34: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``

35: ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``

36: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``


37: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

38: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

39: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_r):``

40: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Load3D = False``

41: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

42: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

43: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``

44: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYDOWN:``

45: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE:``

46: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ zoom = 0``

47: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_w:``

48: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "w"``

49: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_s:``

50: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "s"``

51: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_d:``

52: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "d"``

53: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_a:``

54: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "a"``

55: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``

56: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = self.mod_DisplayUtils__.DisplayUtils.UpdateOPENGLdisplay(self)``

57: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYUP:``

58: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ key = ""``

59: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEWHEEL:``

60: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if str(event.y)[0] == "-":``

61: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ zoom -= 1``

62: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``

63: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ zoom += 1``

64: ``¬ ¬ ¬ ¬ ¬ if zoom >= 2:``

65: ``¬ ¬ ¬ ¬ ¬ ¬ zoom = 2``

66: ``¬ ¬ ¬ ¬ ¬ if zoom <= 0:``

67: ``¬ ¬ ¬ ¬ ¬ ¬ zoom = 0``

68: ``¬ ¬ ¬ ¬ ¬ if key == "w":``

69: ``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``

70: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y -= 5``

71: ``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``

72: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y -= 10``

73: ``¬ ¬ ¬ ¬ ¬ if key == "s":``

74: ``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``

75: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y += 5``

76: ``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``

77: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y += 10``

78: ``¬ ¬ ¬ ¬ ¬ if key == "d":``

79: ``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``

80: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X += 5``

81: ``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``

82: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X += 10``

83: ``¬ ¬ ¬ ¬ ¬ if key == "a":``

84: ``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``

85: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X -= 5``

86: ``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``

87: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X -= 10``

88: ``¬ ¬ ¬ ¬ ¬ if zoom == 0:``

89: ``¬ ¬ ¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((realWidth, realHeight),  self.mod_PIL_Image_.ANTIALIAS)``

90: ``¬ ¬ ¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``

91: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Map0, (0, 0))``

92: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MapIcon, GenerateMapGUI.GetMapPos(self))``

93: ``¬ ¬ ¬ ¬ ¬ ¬ x, y = 0, 0``

94: ``¬ ¬ ¬ ¬ ¬ elif zoom == 1:``

95: ``¬ ¬ ¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((int(realWidth*1.75), int(realHeight*1.75)),  self.mod_PIL_Image_.ANTIALIAS)``

96: ``¬ ¬ ¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``

97: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Map0, (X,Y))``

98: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MapIcon, GenerateMapGUI.GetMapPos(self))``

99: ``¬ ¬ ¬ ¬ ¬ elif zoom == 2:``

100: ``¬ ¬ ¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((int(realWidth*2), int(realHeight*2)),  self.mod_PIL_Image_.ANTIALIAS)``

101: ``¬ ¬ ¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``

102: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Map0, (X,Y))``

103: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MapIcon, GenerateMapGUI.GetMapPos(self))``

104: ``¬ ¬ ¬ ¬ ¬ if zoom == 1:``

105: ``¬ ¬ ¬ ¬ ¬ ¬ if X <= -955:``

106: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -955``

107: ``¬ ¬ ¬ ¬ ¬ ¬ if Y <= -535:``

108: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -535``

109: ``¬ ¬ ¬ ¬ ¬ ¬ if X >= -5:``

110: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -5``

111: ``¬ ¬ ¬ ¬ ¬ ¬ if Y >= -5:``

112: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -5``

113: ``¬ ¬ ¬ ¬ ¬ if zoom == 2:``

114: ``¬ ¬ ¬ ¬ ¬ ¬ if X <= -1590:``

115: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -1590``

116: ``¬ ¬ ¬ ¬ ¬ ¬ if Y <= -890:``

117: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -890``

118: ``¬ ¬ ¬ ¬ ¬ ¬ if X >= -10:``

119: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -10``

120: ``¬ ¬ ¬ ¬ ¬ ¬ if Y >= -10:``

121: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -10``

122: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``

123: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)``

124: ``¬ ¬ ¬ except Exception as Message:``

125: ``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``

126: ``¬ ¬ ¬ ¬ return Message``

127: ``else:``
128: ``¬ print("You need to run this as part of Pycraft")``
129: ``¬ import tkinter as tk``
130: ``¬ from tkinter import messagebox``
131: ``¬ root = tk.Tk()``
132: ``¬ root.withdraw()``
133: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
134: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_OGLBenchmark>")``
        3: ``¬ class LoadOGLBenchmark:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def Cube(self, edges, vertices):``

7: ``¬ ¬ ¬ self.mod_OpenGL_GL_.glBegin(self.mod_OpenGL_GL_.GL_LINES)``

8: ``¬ ¬ ¬ for edge in edges:``

9: ``¬ ¬ ¬ ¬ for vertex in edge:``

10: ``¬ ¬ ¬ ¬ ¬ self.mod_OpenGL_GL_.glVertex3fv(vertices[vertex])``

11: ``¬ ¬ ¬ self.mod_OpenGL_GL_.glEnd()``


12: ``¬ ¬ def CreateBenchmark(self):``

13: ``¬ ¬ ¬ self.mod_OpenGL_GLU_.gluPerspective(45, (1280/720), 0.1, 50.0)``

14: ``¬ ¬ ¬ self.mod_OpenGL_GL_.glTranslatef(0.0,0.0, -5)``


15: ``¬ ¬ def RunBenchmark(self, edges, vertices):``

16: ``¬ ¬ ¬ self.mod_OpenGL_GL_.glRotatef(1, 3, 1, 1)``

17: ``¬ ¬ ¬ self.mod_OpenGL_GL_.glClear(self.mod_OpenGL_GL_.GL_COLOR_BUFFER_BIT|self.mod_OpenGL_GL_.GL_DEPTH_BUFFER_BIT)``

18: ``¬ ¬ ¬ LoadOGLBenchmark.Cube(self, edges, vertices)``

19: ``else:``
20: ``¬ print("You need to run this as part of Pycraft")``
21: ``¬ import tkinter as tk``
22: ``¬ from tkinter import messagebox``
23: ``¬ root = tk.Tk()``
24: ``¬ root.withdraw()``
25: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
26: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_PycraftStartupTest>")``
        3: ``¬ class StartupTest:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def PycraftSelfTest(self):``

7: ``¬ ¬ ¬ try:``

8: ``¬ ¬ ¬ ¬ import OpenGL.GL as gl``

9: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_mode((1280, 720), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL|self.mod_Pygame__.HIDDEN)``


10: ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``

11: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``


12: ``¬ ¬ ¬ ¬ OpenGLversion = str(gl.glGetString(gl.GL_VERSION))[2:5]``

13: ``¬ ¬ ¬ ¬ SDLversion = self.mod_Pygame__.get_sdl_version()[0]``

14: ``¬ ¬ ¬ ¬ RAM = (((self.mod_Psutil__.virtual_memory().available)/1000)/1000) # expressed in MB``


15: ``¬ ¬ ¬ ¬ if float(OpenGLversion) < 2.8:``

16: ``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``

17: ``¬ ¬ ¬ ¬ ¬ root.withdraw()``

18: ``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showerror("Invalid OpenGL version", f"OpenGL version: {OpenGLversion} is not supported; try a version greater than 2.7")``

19: ``¬ ¬ ¬ ¬ ¬ quit()``

20: ``¬ ¬ ¬ ¬ if SDLversion < 2:``

21: ``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``

22: ``¬ ¬ ¬ ¬ ¬ root.withdraw()``

23: ``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showerror("Invalid SDL version", f"SDL version: {SDLversion} is not supported; try a version greater than or equal to 2")``

24: ``¬ ¬ ¬ ¬ ¬ quit()``

25: ``¬ ¬ ¬ ¬ if RAM < 100:``

26: ``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``

27: ``¬ ¬ ¬ ¬ ¬ root.withdraw()``

28: ``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showerror("Minimum system requirements not met", f"Your system does not meet the minimum 100mb free memory specification needed to play this game")``

29: ``¬ ¬ ¬ ¬ ¬ quit()``

30: ``¬ ¬ ¬ ¬ if RAM < 200:``

31: ``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``

32: ``¬ ¬ ¬ ¬ ¬ root.withdraw()``

33: ``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showwarning("Recommended system requirements not met", f"Your system's free memory does not meet the requirement recommended to play this game (200mb), you are still able to, however your experience may not be satisfactory")``

34: ``¬ ¬ ¬ ¬ ¬ from PIL import Image, ImageTk, ImageGrab``

35: ``¬ ¬ ¬ ¬ ¬ import OpenGL.GL``


36: ``¬ ¬ ¬ ¬ if self.mod_Sys__.platform == "win32" or self.mod_Sys__.platform == "win64":``

37: ``¬ ¬ ¬ ¬ ¬ self.mod_OS__.environ["SDL_VIDEO_CENTERED"] = "1"``


38: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``

39: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.init()``


40: ``¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``


41: ``¬ ¬ ¬ ¬ current_time = self.mod_Datetime__.datetime.now()``

42: ``¬ ¬ ¬ ¬ currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"``

43: ``¬ ¬ ¬ ¬ if not currentDate == self.lastRun or self.crash == True:``

44: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

45: ``¬ ¬ ¬ ¬ ¬ yScaleFact = realHeight/720``

46: ``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``

47: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

48: ``¬ ¬ ¬ ¬ ¬ TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``

49: ``¬ ¬ ¬ ¬ ¬ Title = TitleFont.render("Pycraft", True, self.FontCol)``

50: ``¬ ¬ ¬ ¬ ¬ TitleWidth = Title.get_width()``

51: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Title, ((realWidth-TitleWidth)/2, 0))``

52: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``

53: ``¬ ¬ ¬ ¬ ¬ defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)]``

54: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2)``

55: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``

56: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``

57: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``

58: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

59: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

60: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

61: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``

62: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``

63: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

64: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

65: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

66: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``

67: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``

68: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

69: ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

70: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``

71: ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Error_Resources\\Error_Message.png"))).convert()``

72: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``

73: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``

74: ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Error_Resources\\Icon.jpg"))).convert()``

75: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``

76: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``

77: ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Folder_Resources\\FolderIcon.ico"))).convert()``

78: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``

79: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

80: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``

81: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

82: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

83: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

84: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``

85: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``

86: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``

87: ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg"))).convert()``

88: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

89: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``

90: ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg"))).convert()``

91: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``

92: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

93: ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg"))).convert()``

94: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``

95: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

96: ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg"))).convert()``

97: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``

98: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

99: ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg"))).convert()``

100: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``

101: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``

102: ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg"))).convert()``

103: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``

104: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``

105: ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, f"Resources\\General_Resources\\selectorICONlight.jpg")).convert()``

106: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``

107: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

108: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

109: ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, f"Resources\\General_Resources\\selectorICONdark.jpg")).convert()``

110: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``

111: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

112: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

113: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\InventoryGeneral.wav")))``

114: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``

115: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

116: ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``

117: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``

118: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

119: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``

120: ``¬ ¬ ¬ ¬ else:``

121: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

122: ``¬ ¬ ¬ ¬ ¬ TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``

123: ``¬ ¬ ¬ ¬ ¬ Title = TitleFont.render("Pycraft", True, self.FontCol)``

124: ``¬ ¬ ¬ ¬ ¬ TitleWidth = Title.get_width()``

125: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

126: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Title, ((realWidth-TitleWidth)/2, 0))``

127: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``


128: ``¬ ¬ ¬ ¬ ¬ yScaleFact = realHeight/720``

129: ``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``

130: ``¬ ¬ ¬ ¬ ¬ defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)]``

131: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2)``

132: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``

133: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``

134: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

135: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

136: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

137: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``

138: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``

139: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

140: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

141: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

142: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

143: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``

144: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``

145: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

146: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

147: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

148: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

149: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``

150: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``

151: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

152: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

153: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

154: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

155: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``

156: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``

157: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``

158: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``

159: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

160: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

161: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

162: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``

163: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (575*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

164: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``

165: ``¬ ¬ ¬ except Exception as Message:``

166: ``¬ ¬ ¬ ¬ return Message``

167: ``else:``
168: ``¬ print("You need to run this as part of Pycraft")``
169: ``¬ import tkinter as tk``
170: ``¬ from tkinter import messagebox``
171: ``¬ root = tk.Tk()``
172: ``¬ root.withdraw()``
173: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
174: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_Settings>")``
        3: ``¬ class GenerateSettings:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def settings(self):``

7: ``¬ ¬ ¬ try:``

8: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

9: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

10: ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Settings")``

11: ``¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

12: ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``

13: ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``

14: ``¬ ¬ ¬ ¬ LOWFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

15: ``¬ ¬ ¬ ¬ MEDIUMFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

16: ``¬ ¬ ¬ ¬ HIGHFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

17: ``¬ ¬ ¬ ¬ ADAPTIVEFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

18: ``¬ ¬ ¬ ¬ LightThemeFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

19: ``¬ ¬ ¬ ¬ DarkThemeFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

20: ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``


21: ``¬ ¬ ¬ ¬ TempMx = 0``

22: ``¬ ¬ ¬ ¬ Mx, My = 0, 0``

23: ``¬ ¬ ¬ ¬ mousebuttondown = False``


24: ``¬ ¬ ¬ ¬ SettingsInformationFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``


25: ``¬ ¬ ¬ ¬ scroll = 50``


26: ``¬ ¬ ¬ ¬ while True:``

27: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``


28: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``

29: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``

30: ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``

31: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``


32: ``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``


33: ``¬ ¬ ¬ ¬ ¬ TempMx = Mx``

34: ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``

35: ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``

36: ``¬ ¬ ¬ ¬ ¬ Mx, My = self.mod_Pygame__.mouse.get_pos()``

37: ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``

38: ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``

39: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

40: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``

41: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

42: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

43: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``

44: ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:``

45: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:``

46: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``

47: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``

48: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``

49: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``

50: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``

51: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``

52: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``

53: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``

54: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``

55: ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:``

56: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True``

57: ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.MOUSEBUTTONUP:``

58: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

59: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEWHEEL and realHeight <= 760:``

60: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_SIZENS)``

61: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if str(event.y)[0] == "-":``

62: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ scroll -= 5``

63: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``

64: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ scroll += 5``

65: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

66: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_ARROW)``


67: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Settings")``


68: ``¬ ¬ ¬ ¬ ¬ if scroll > 35:``

69: ``¬ ¬ ¬ ¬ ¬ ¬ scroll = 35``

70: ``¬ ¬ ¬ ¬ ¬ elif scroll < 0:``

71: ``¬ ¬ ¬ ¬ ¬ ¬ scroll = 0``


72: ``¬ ¬ ¬ ¬ ¬ titletFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``

73: ``¬ ¬ ¬ ¬ ¬ TitleWidth = titletFont.get_width()``


74: ``¬ ¬ ¬ ¬ ¬ InfoFont = InfoTitleFont.render("Settings", self.aa, self.SecondFontCol)``


75: ``¬ ¬ ¬ ¬ ¬ FPSFont = VersionFont.render(f"FPS: Actual: {int(self.eFPS)} Max: {int(self.FPS)} Average: {int((self.aFPS/self.Iteration))}", self.aa, self.FontCol)``

76: ``¬ ¬ ¬ ¬ ¬ FOVFont = VersionFont.render(f"FOV: {self.FOV}", self.aa, self.FontCol)``

77: ``¬ ¬ ¬ ¬ ¬ CamRotFont = VersionFont.render(f"Camera Rotation Speed: {round(self.cameraANGspeed, 1)}", self.aa, self.FontCol)``

78: ``¬ ¬ ¬ ¬ ¬ ModeFont = VersionFont.render("Mode;         ,                 ,            ,          .", self.aa, self.FontCol)``

79: ``¬ ¬ ¬ ¬ ¬ AAFont = VersionFont.render(f"Anti-Aliasing: {self.aa}", self.aa, self.FontCol)``

80: ``¬ ¬ ¬ ¬ ¬ RenderFogFont = VersionFont.render(f"Render Fog: {self.RenderFOG}", self.aa, self.FontCol)``

81: ``¬ ¬ ¬ ¬ ¬ FancySkyFont = VersionFont.render(f"Fancy Skies: {self.FanSky}", self.aa, self.FontCol)``

82: ``¬ ¬ ¬ ¬ ¬ FancyParticleFont = VersionFont.render(f"Fancy Partices: {self.FanPart}", self.aa, self.FontCol)``

83: ``¬ ¬ ¬ ¬ ¬ SoundFont = VersionFont.render(f"Sound: {self.sound}", self.aa, self.FontCol)``

84: ``¬ ¬ ¬ ¬ ¬ if self.sound == True:``

85: ``¬ ¬ ¬ ¬ ¬ ¬ SoundVoltFont = VersionFont.render(f"Sound Volume: {self.soundVOL}%", self.aa, self.FontCol)``

86: ``¬ ¬ ¬ ¬ ¬ else:``

87: ``¬ ¬ ¬ ¬ ¬ ¬ SoundVoltFont = VersionFont.render(f"Sound Volume: {self.soundVOL}%", self.aa, self.ShapeCol)``

88: ``¬ ¬ ¬ ¬ ¬ MusicFont = VersionFont.render(f"Music: {self.music}", self.aa, self.FontCol)``

89: ``¬ ¬ ¬ ¬ ¬ if self.music == True:``

90: ``¬ ¬ ¬ ¬ ¬ ¬ MusicVoltFont = VersionFont.render(f"Music Volume: {self.musicVOL}%", self.aa, self.FontCol)``

91: ``¬ ¬ ¬ ¬ ¬ else:``

92: ``¬ ¬ ¬ ¬ ¬ ¬ MusicVoltFont = VersionFont.render(f"Music Volume: {self.musicVOL}%", self.aa, self.ShapeCol)``

93: ``¬ ¬ ¬ ¬ ¬ ThemeFont = VersionFont.render(f"Theme:          ,          | Current Theme: {self.theme}", self.aa, self.FontCol)``

94: ``¬ ¬ ¬ ¬ ¬ ThemeInformationFont = SettingsInformationFont.render("Gives you control over which theme you can use", self.aa, self.AccentCol)``

95: ``¬ ¬ ¬ ¬ ¬ ModeInformationFont = SettingsInformationFont.render("Gives you 4 separate per-sets for settings, Adaptive mode will automatically adjust your settings", self.aa, self.AccentCol)``

96: ``¬ ¬ ¬ ¬ ¬ FPSInformationFont = SettingsInformationFont.render("Controls the maximum frame rate the game will limit to, does not guarantee that FPS unfortunately", self.aa, self.AccentCol)``

97: ``¬ ¬ ¬ ¬ ¬ FOVInformationFont = SettingsInformationFont.render("Controls the FOV of the camera in-game", self.aa, self.AccentCol)``

98: ``¬ ¬ ¬ ¬ ¬ CameraRotationSpeedInformationFont = SettingsInformationFont.render("Controls the rotation speed of the camera in-game (1 is low, 5 is high)", self.aa, self.AccentCol)``

99: ``¬ ¬ ¬ ¬ ¬ AAInformationFont = SettingsInformationFont.render("Enables/Disables anti-aliasing in game and in the GUI, will give you a minor performance improvement, mainly for low powered devices", self.aa, self.AccentCol)``

100: ``¬ ¬ ¬ ¬ ¬ self.RenderFogInformationFont = SettingsInformationFont.render("Enables/Disables fog effects in game, for a small performance benefit", self.aa, self.AccentCol)``

101: ``¬ ¬ ¬ ¬ ¬ FancySkiesInformationFont = SettingsInformationFont.render("Enables/Disables a fancy sky box for better visuals in game, does not control anti aliasing for the sky box", self.aa, self.AccentCol)``

102: ``¬ ¬ ¬ ¬ ¬ FancyParticlesInformationFont = SettingsInformationFont.render("Enables/Disables particles in game as particles can have a significant performance decrease", self.aa, self.AccentCol)``

103: ``¬ ¬ ¬ ¬ ¬ SoundInformationFont = SettingsInformationFont.render("Enables/Disables sound effects in game, like for example the click sound and footsteps in game", self.aa, self.AccentCol)``

104: ``¬ ¬ ¬ ¬ ¬ SoundVolInformationFont = SettingsInformationFont.render("Controls the volume of the sound effects, where 100% is maximum and 0% is minimum volume", self.aa, self.AccentCol)``

105: ``¬ ¬ ¬ ¬ ¬ MusicInformationFont = SettingsInformationFont.render("Enables/Disables music in game, like for example the GUI music", self.aa, self.AccentCol)``

106: ``¬ ¬ ¬ ¬ ¬ MusicVolInformationFont = SettingsInformationFont.render("Controls the volume of the music, some effects may not apply until the game reloads", self.aa, self.AccentCol)``

107: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

108: ``¬ ¬ ¬ ¬ ¬ FPS_rect = self.mod_Pygame__.Rect(50, 180+scroll, 450*xScaleFact, 10)``

109: ``¬ ¬ ¬ ¬ ¬ FOV_rect = self.mod_Pygame__.Rect(50, 230+scroll, 450*xScaleFact, 10)``

110: ``¬ ¬ ¬ ¬ ¬ CAM_rect = self.mod_Pygame__.Rect(50, 280+scroll, 450*xScaleFact, 10)``

111: ``¬ ¬ ¬ ¬ ¬ sound_rect = self.mod_Pygame__.Rect(50, 580+scroll, 450*xScaleFact, 10)``

112: ``¬ ¬ ¬ ¬ ¬ music_rect = self.mod_Pygame__.Rect(50, 680+scroll, 450*xScaleFact, 10)``

113: ``¬ ¬ ¬ ¬ ¬ aa_rect = self.mod_Pygame__.Rect(50, 330+scroll, 50, 10)``

114: ``¬ ¬ ¬ ¬ ¬ RenderFOG_Rect = self.mod_Pygame__.Rect(50, 380+scroll, 50, 10)``

115: ``¬ ¬ ¬ ¬ ¬ Fansky_Rect = self.mod_Pygame__.Rect(50, 430+scroll, 50, 10)``

116: ``¬ ¬ ¬ ¬ ¬ FanPart_Rect = self.mod_Pygame__.Rect(50, 480+scroll, 50, 10)``

117: ``¬ ¬ ¬ ¬ ¬ sound_Rect = self.mod_Pygame__.Rect(50, 530+scroll, 50, 10)``

118: ``¬ ¬ ¬ ¬ ¬ music_Rect = self.mod_Pygame__.Rect(50, 630+scroll, 50, 10)``

119: ``¬ ¬ ¬ ¬ ¬ slider_Rect = self.mod_Pygame__.Rect(realWidth-15, scroll, 10, 665)``

120: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FPS_rect, 0)``

121: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FOV_rect, 0)``

122: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, CAM_rect, 0)``

123: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, sound_rect, 0)``

124: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, music_rect, 0)``

125: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, aa_rect, 0)``

126: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, RenderFOG_Rect, 0)``

127: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, Fansky_Rect, 0)``

128: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FanPart_Rect, 0)``

129: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, sound_Rect, 0)``

130: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, music_Rect, 0)``

131: ``¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

132: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 180+scroll and My < 190+scroll:``

133: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

134: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.FPS < 445:``

135: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS += 1``

136: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.FPS > 15:``

137: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS -= 1``

138: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FPS < 15:``

139: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 16``

140: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FPS > 445:``

141: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 444``

142: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (int(self.FPS+45)*xScaleFact, 185+scroll), 9)``

143: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

144: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (int(self.FPS+45)*xScaleFact, 185+scroll), 9)``


145: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 230+scroll and My < 240+scroll:``

146: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

147: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.FOV < 98:``

148: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV += 1``

149: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.FOV > 12:``

150: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV -= 1``

151: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FOV < 12:``

152: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV = 13``

153: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FOV > 98:``

154: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV = 97``

155: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (int(self.FOV*5)*xScaleFact, 235+scroll), 9)``

156: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

157: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (int(self.FOV*5)*xScaleFact, 235+scroll), 9)``


158: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 280+scroll and My < 290+scroll:``

159: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

160: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.cameraANGspeed < 5.0:``

161: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed += 0.1``

162: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.cameraANGspeed > 0.0:``

163: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed -= 0.1``

164: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.cameraANGspeed > 5.0:``

165: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed = 4.9``

166: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.cameraANGspeed <= 0:``

167: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed = 0.1``

168: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)``

169: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

170: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)``


171: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 580+scroll and My < 590+scroll and self.sound == True:``

172: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

173: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.soundVOL < 100:``

174: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL += 1``

175: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.soundVOL > 0:``

176: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL -= 1``

177: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.soundVOL > 100:``

178: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL = 100``

179: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.soundVOL < 0:``

180: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL = 0``

181: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)``

182: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

183: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)``


184: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 680+scroll and My < 690+scroll and self.music == True:``

185: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

186: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.musicVOL < 100:``

187: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL += 1``

188: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.musicVOL > 0:``

189: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL -= 1``

190: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.musicVOL > 100:``

191: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL = 100``

192: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.musicVOL < 0:``

193: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL = 0``

194: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)``

195: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

196: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)``


197: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 330+scroll and My < 340+scroll:``

198: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

199: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True:``

200: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``

201: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

202: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

203: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

204: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False:``

205: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``

206: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

207: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

208: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

209: ``¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True:``

210: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 335+scroll), 9)``

211: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 335+scroll), 6)``

212: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False:``

213: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 335+scroll), 9)``

214: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 335+scroll), 6)``


215: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 380+scroll and My < 390+scroll:``

216: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

217: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``

218: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = False``

219: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

220: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

221: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

222: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``

223: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = True``

224: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

225: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

226: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

227: ``¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``

228: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 385+scroll), 9)``

229: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 385+scroll), 6)``

230: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``

231: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 385+scroll), 9)``

232: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 385+scroll), 6)``


233: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 430+scroll and My < 440+scroll:``

234: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

235: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``

236: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = False``

237: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

238: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

239: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

240: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``

241: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``

242: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

243: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

244: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

245: ``¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``

246: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 435+scroll), 9)``

247: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 435+scroll), 6)``

248: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``

249: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 435+scroll), 9)``

250: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 435+scroll), 6)``


251: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 480+scroll and My < 490+scroll:``

252: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

253: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``

254: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``

255: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

256: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

257: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

258: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``

259: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = True``

260: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

261: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

262: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

263: ``¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``

264: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 485+scroll), 9)``

265: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 485+scroll), 6)``

266: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``

267: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 485+scroll), 9)``

268: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 485+scroll), 6)``


269: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 530+scroll and My < 540+scroll:``

270: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

271: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

272: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.sound = False``

273: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

274: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

275: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

276: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``

277: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.sound = True``

278: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

279: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

280: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

281: ``¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

282: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 535+scroll), 9)``

283: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 535+scroll), 6)``

284: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``

285: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 535+scroll), 9)``

286: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 535+scroll), 6)``


287: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 630+scroll and My < 640+scroll:``

288: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

289: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``

290: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.music = False``

291: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).stop()``

292: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

293: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

294: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

295: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``

296: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.LoadMusic = True``

297: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.music = True``

298: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

299: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

300: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

301: ``¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``

302: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 635+scroll), 9)``

303: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 635+scroll), 6)``

304: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``

305: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 635+scroll), 9)``

306: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 635+scroll), 6)``

307: ``¬ ¬ ¬ ¬ ¬ else:``

308: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)``

309: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.FPS+45)*xScaleFact), 185+scroll), 9)``

310: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)``

311: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.FOV*5))*xScaleFact, 235+scroll), 9)``

312: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)``


313: ``¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True:``

314: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 335+scroll), 9)``

315: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 335+scroll), 6)``

316: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False:``

317: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 335+scroll), 9)``

318: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 335+scroll), 6)``


319: ``¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``

320: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 385+scroll), 9)``

321: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 385+scroll), 6)``

322: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``

323: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 385+scroll), 9)``

324: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 385+scroll), 6)``


325: ``¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``

326: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 435+scroll), 9)``

327: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 435+scroll), 6)``

328: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``

329: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 435+scroll), 9)``

330: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 435+scroll), 6)``


331: ``¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``

332: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 485+scroll), 9)``

333: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 485+scroll), 6)``

334: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``

335: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 485+scroll), 9)``

336: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 485+scroll), 6)``


337: ``¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

338: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 535+scroll), 9)``

339: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 535+scroll), 6)``

340: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``

341: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 535+scroll), 9)``

342: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 535+scroll), 6)``


343: ``¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``

344: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 635+scroll), 9)``

345: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 635+scroll), 6)``

346: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``

347: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 635+scroll), 9)``

348: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 635+scroll), 6)``


349: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 330+scroll and My < 340+scroll:``

350: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

351: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(AAInformationFont, (120, 325+scroll))``

352: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True:``

353: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 335+scroll), 9)``

354: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 335+scroll), 6)``

355: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False:``

356: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 335+scroll), 9)``

357: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 335+scroll), 6)``


358: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 380+scroll and My < 390+scroll:``

359: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

360: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(self.RenderFogInformationFont, (120, 375+scroll))``

361: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``

362: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 385+scroll), 9)``

363: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 385+scroll), 6)``

364: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``

365: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 385+scroll), 9)``

366: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 385+scroll), 6)``


367: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 430+scroll and My < 440+scroll:``

368: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

369: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FancySkiesInformationFont, (120, 425+scroll))``

370: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``

371: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 435+scroll), 9)``

372: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 435+scroll), 6)``

373: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``

374: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 435+scroll), 9)``

375: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 435+scroll), 6)``


376: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 480+scroll and My < 490+scroll:``

377: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FancyParticlesInformationFont, (120, 475+scroll))``

378: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

379: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``

380: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 485+scroll), 9)``

381: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 485+scroll), 6)``

382: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``

383: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 485+scroll), 9)``

384: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 485+scroll), 6)``


385: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 530+scroll and My < 540+scroll:``

386: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundInformationFont, (120, 525+scroll))``

387: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

388: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

389: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 535+scroll), 9)``

390: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 535+scroll), 6)``

391: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``

392: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 535+scroll), 9)``

393: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 535+scroll), 6)``


394: ``¬ ¬ ¬ ¬ ¬ ¬ if My > 630+scroll and My < 640+scroll:``

395: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

396: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicInformationFont, (120, 625+scroll))``

397: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``

398: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 635+scroll), 9)``

399: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 635+scroll), 6)``

400: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``

401: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 635+scroll), 9)``

402: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 635+scroll), 6)``


403: ``¬ ¬ ¬ ¬ ¬ if My >= 65+scroll and My <= 75+scroll:``

404: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

405: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(ThemeInformationFont, (300, 67+scroll))``


406: ``¬ ¬ ¬ ¬ ¬ if My >= 65+scroll and My <= 75+scroll and Mx >= 55 and Mx <= 95:``

407: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

408: ``¬ ¬ ¬ ¬ ¬ ¬ LightTheme = LightThemeFont.render("Light", self.aa, self.AccentCol)``

409: ``¬ ¬ ¬ ¬ ¬ ¬ LightThemeFont.set_underline(True)``

410: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

411: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "light"``

412: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = self.mod_ThemeUtils__.DetermineThemeColours.GetColours(self)``

413: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:``

414: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = "1.8- " + str(Message)``

415: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message``

416: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

417: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

418: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

419: ``¬ ¬ ¬ ¬ ¬ else:``

420: ``¬ ¬ ¬ ¬ ¬ ¬ LightTheme = LightThemeFont.render("Light", self.aa, self.FontCol)``

421: ``¬ ¬ ¬ ¬ ¬ ¬ LightThemeFont.set_underline(False)``


422: ``¬ ¬ ¬ ¬ ¬ if My >= 65+scroll and My <= 75+scroll and Mx >= 95 and Mx <= 135:``

423: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

424: ``¬ ¬ ¬ ¬ ¬ ¬ DarkTheme = DarkThemeFont.render("Dark", self.aa, self.AccentCol)``

425: ``¬ ¬ ¬ ¬ ¬ ¬ DarkThemeFont.set_underline(True)``

426: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

427: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "dark"``

428: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = self.mod_ThemeUtils__.DetermineThemeColours.GetColours(self)``

429: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:``

430: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = "1.8- " + str(Message)``

431: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message``

432: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

433: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

434: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

435: ``¬ ¬ ¬ ¬ ¬ else:``

436: ``¬ ¬ ¬ ¬ ¬ ¬ DarkTheme = DarkThemeFont.render("Dark", self.aa, self.FontCol)``

437: ``¬ ¬ ¬ ¬ ¬ ¬ DarkThemeFont.set_underline(False)``


438: ``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll:``

439: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

440: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(ModeInformationFont, (300, 85+scroll))``


441: ``¬ ¬ ¬ ¬ ¬ if My > 680+scroll and My < 690+scroll:``

442: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

443: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicVolInformationFont, (520*xScaleFact, 675+scroll))``


444: ``¬ ¬ ¬ ¬ ¬ if My > 580+scroll and My < 590+scroll:``

445: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

446: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundVolInformationFont, (520*xScaleFact, 575+scroll))``


447: ``¬ ¬ ¬ ¬ ¬ if My > 280+scroll and My < 290+scroll:``

448: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

449: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CameraRotationSpeedInformationFont, (520*xScaleFact, 275+scroll))``


450: ``¬ ¬ ¬ ¬ ¬ if My > 230+scroll and My < 240+scroll:``

451: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

452: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FOVInformationFont, (520*xScaleFact, 225+scroll))``


453: ``¬ ¬ ¬ ¬ ¬ if My > 180+scroll and My < 190+scroll:``

454: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

455: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSInformationFont, (520*xScaleFact, 175+scroll))``


456: ``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 40 and Mx <= 80:``

457: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

458: ``¬ ¬ ¬ ¬ ¬ ¬ LOWtFont = LOWFont.render("Low", self.aa, self.AccentCol)``

459: ``¬ ¬ ¬ ¬ ¬ ¬ LOWFont.set_underline(True)``

460: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

461: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "Low"``

462: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 15``

463: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``

464: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = False``

465: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = False``

466: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``

467: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

468: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

469: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

470: ``¬ ¬ ¬ ¬ ¬ else:``

471: ``¬ ¬ ¬ ¬ ¬ ¬ LOWtFont = LOWFont.render("Low", self.aa, self.FontCol)``

472: ``¬ ¬ ¬ ¬ ¬ ¬ LOWFont.set_underline(False)``


473: ``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 90 and Mx <= 155:``

474: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

475: ``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMtFont = MEDIUMFont.render("Medium", self.aa, self.AccentCol)``

476: ``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMFont.set_underline(True)``

477: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

478: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "Medium"``

479: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 30``

480: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``

481: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = False``

482: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``

483: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``

484: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

485: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

486: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

487: ``¬ ¬ ¬ ¬ ¬ else:``

488: ``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMtFont = MEDIUMFont.render("Medium", self.aa, self.FontCol)``

489: ``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMFont.set_underline(False)``


490: ``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 165 and Mx <= 205:``

491: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

492: ``¬ ¬ ¬ ¬ ¬ ¬ HIGHFontText = HIGHFont.render("High", self.aa, self.AccentCol)``

493: ``¬ ¬ ¬ ¬ ¬ ¬ HIGHFont.set_underline(True)``

494: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

495: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "High"``

496: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 60``

497: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``

498: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = True``

499: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``

500: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = True``

501: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

502: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

503: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

504: ``¬ ¬ ¬ ¬ ¬ else:``

505: ``¬ ¬ ¬ ¬ ¬ ¬ HIGHFontText = HIGHFont.render("High", self.aa, self.FontCol)``

506: ``¬ ¬ ¬ ¬ ¬ ¬ HIGHFont.set_underline(False)``


507: ``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 215 and Mx <= 300:``

508: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``

509: ``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEtFont = ADAPTIVEFont.render("Adaptive", self.aa, self.AccentCol)``

510: ``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEFont.set_underline(True)``

511: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

512: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "Adaptive"``

513: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = (self.mod_Psutil__.cpu_freq(percpu=True)[0][2])/35``

514: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if (self.mod_Psutil__.cpu_freq(percpu=True)[0][2])/10 > 300 and self.mod_Psutil__.virtual_memory().total > 8589934592:``

515: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``

516: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = True``

517: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``

518: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = True``

519: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif (self.mod_Psutil__.cpu_freq(percpu=True)[0][2]) > 200 and self.mod_Psutil__.virtual_memory().total > 4294967296:``

520: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``

521: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = True``

522: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``

523: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``

524: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif (self.mod_Psutil__.cpu_freq(percpu=True)[0][2]) > 100 and self.mod_Psutil__.virtual_memory().total > 2147483648:``

525: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``

526: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = False``

527: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``

528: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``

529: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif (self.mod_Psutil__.cpu.freq(percpu=True)[0][2]) < 100 and (self.mod_Psutil__.cpu.freq(percpu=True)[0][2]) > 75 and self.mod_Psutil__.virtual_memory().total > 1073741824:``

530: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``

531: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = False``

532: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = False``

533: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``

534: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``

535: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``

536: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

537: ``¬ ¬ ¬ ¬ ¬ else:``

538: ``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEtFont = ADAPTIVEFont.render("Adaptive", self.aa, self.FontCol)``

539: ``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEFont.set_underline(False)``


540: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSFont, (0, 150+scroll))``

541: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(FOVFont, (0, 200+scroll))``

542: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(CamRotFont, (0, 250+scroll))``

543: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(ModeFont, (0, 85+scroll))``

544: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(LOWtFont, (48, 85+scroll))``

545: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(MEDIUMtFont, (90, 85+scroll))``

546: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(HIGHFontText, (165, 85+scroll))``

547: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(ADAPTIVEtFont, (215, 85+scroll))``

548: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AAFont, (0, 300+scroll))``

549: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(RenderFogFont, (0, 350+scroll))``

550: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(FancySkyFont, (0, 400+scroll))``

551: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(FancyParticleFont, (0, 450+scroll))``

552: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundFont, (0, 500+scroll))``

553: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundVoltFont, (0, 550+scroll))``

554: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicFont, (0, 600+scroll))``

555: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicVoltFont, (0, 650+scroll))``

556: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(ThemeFont, (0, 65+scroll))``

557: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(LightTheme, (55, 65+scroll))``

558: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(DarkTheme, (95, 65+scroll))``

559: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (int(self.FPS+45)*xScaleFact, 185+scroll), 6)``

560: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (int(self.FOV*5)*xScaleFact, 235+scroll), 6)``

561: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 6)``

562: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 6)``

563: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 6)``


564: ``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 100)``

565: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``

566: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(titletFont, ((realWidth-TitleWidth)/2, 0))``

567: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont, (((realWidth-TitleWidth)/2)+55, 50))``



568: ``¬ ¬ ¬ ¬ ¬ if realHeight <= 760:``

569: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, slider_Rect, 0)``

570: ``¬ ¬ ¬ ¬ ¬ else:``

571: ``¬ ¬ ¬ ¬ ¬ ¬ scroll = 50``


572: ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``

573: ``¬ ¬ ¬ ¬ ¬ if not Message == None:``

574: ``¬ ¬ ¬ ¬ ¬ ¬ return Message``


575: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

576: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``

577: ``¬ ¬ ¬ except Exception as Message:``

578: ``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``

579: ``¬ ¬ ¬ ¬ return Message``

580: ``else:``
581: ``¬ print("You need to run this as part of Pycraft")``
582: ``¬ import tkinter as tk``
583: ``¬ from tkinter import messagebox``
584: ``¬ root = tk.Tk()``
585: ``¬ root.withdraw()``
586: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
587: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_ShareDataUtil>")``

3: ``¬ print("Started <Pycraft_ShareDataUtil>")``


4: ``¬ class Share:``



5: ``¬ ¬ def __init__(self):``

6: ``¬ ¬ ¬ pass``



7: ``¬ ¬ def initialize(Data):``

8: ``¬ ¬ ¬ global Class_Startup_variables``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_SoundUtils>")``
        3: ``¬ class PlaySound:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def PlayClickSound(self):``

7: ``¬ ¬ ¬ channel1 = self.mod_Pygame__.mixer.Channel(0)``

8: ``¬ ¬ ¬ clickMUSIC = self.mod_Pygame__.mixer.Sound(file=self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``

9: ``¬ ¬ ¬ channel1.set_volume(self.soundVOL/100)``

10: ``¬ ¬ ¬ channel1.play(clickMUSIC)``

11: ``¬ ¬ ¬ self.mod_Pygame__.time.wait(40)``


12: ``¬ ¬ def PlayFootstepsSound(self):``

13: ``¬ ¬ ¬ channel2 = self.mod_Pygame__.mixer.Channel(1)``

14: ``¬ ¬ ¬ Footsteps = self.mod_Pygame__.mixer.Sound(self.mod_OS__.path.join(self.base_folder, (f"Resources\\G3_Resources\\GameSounds\\footsteps{self.mod_Random__.randint(0, 5)}.wav")))``

15: ``¬ ¬ ¬ channel2.set_volume(self.soundVOL/100)``

16: ``¬ ¬ ¬ channel2.play(Footsteps)``



17: ``¬ ¬ def PlayInvSound(self):``

18: ``¬ ¬ ¬ channel3 = self.mod_Pygame__.mixer.Channel(2)``

19: ``¬ ¬ ¬ InvGen = self.mod_Pygame__.mixer.Sound(file=self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\InventoryGeneral.wav")))``

20: ``¬ ¬ ¬ channel3.set_volume(self.musicVOL/100)``

21: ``¬ ¬ ¬ channel3.play(InvGen)``



22: ``¬ ¬ def PlayAmbientSound(self):``

23: ``¬ ¬ ¬ channel4 = self.mod_Pygame__.mixer.Channel(3)``

24: ``¬ ¬ ¬ LoadAmb = self.mod_Pygame__.mixer.Sound(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\GameSounds\\FieldAmb.wav")))``

25: ``¬ ¬ ¬ channel4.set_volume(self.soundVOL/100)``

26: ``¬ ¬ ¬ channel4.play(LoadAmb)``

27: ``else:``
28: ``¬ print("You need to run this as part of Pycraft")``
29: ``¬ import tkinter as tk``
30: ``¬ from tkinter import messagebox``
31: ``¬ root = tk.Tk()``
32: ``¬ root.withdraw()``
33: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
34: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_StartupAnimation>")``
        3: ``¬ class GenerateStartupScreen:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def Start(self):``

7: ``¬ ¬ ¬ try:``

8: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

9: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

10: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Welcome")``

11: ``¬ ¬ ¬ ¬ PresentsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``

12: ``¬ ¬ ¬ ¬ PycraftFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``

13: ``¬ ¬ ¬ ¬ NameFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 45)``


14: ``¬ ¬ ¬ ¬ NameText = NameFont.render("Tom Jebbo", True, self.FontCol)``

15: ``¬ ¬ ¬ ¬ NameTextWidth = NameText.get_width()``

16: ``¬ ¬ ¬ ¬ NameTextHeight = NameText.get_height()``


17: ``¬ ¬ ¬ ¬ PresentsText = PresentsFont.render("presents", True, self.FontCol)``


18: ``¬ ¬ ¬ ¬ PycraftText = PycraftFont.render("Pycraft", True, self.FontCol)``

19: ``¬ ¬ ¬ ¬ PycraftTextWidth = PycraftText.get_width()``

20: ``¬ ¬ ¬ ¬ PycraftTextHeight = PycraftText.get_height()``


21: ``¬ ¬ ¬ ¬ iteration = 0``

22: ``¬ ¬ ¬ ¬ clock = self.mod_Pygame__.time.Clock()``

23: ``¬ ¬ ¬ ¬ if self.RunFullStartup == True:``

24: ``¬ ¬ ¬ ¬ ¬ while iteration <= (60*3):``

25: ``¬ ¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``

26: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

27: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(NameText, ((self.realWidth-NameTextWidth)/2, (self.realHeight-NameTextHeight)/2))``

28: ``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``


29: ``¬ ¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``

30: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``

31: ``¬ ¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``

32: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``


33: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

34: ``¬ ¬ ¬ ¬ ¬ ¬ clock.tick(60)``

35: ``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

36: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``

37: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``


38: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``

39: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``

40: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``

41: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``

42: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``

43: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``

44: ``¬ ¬ ¬ ¬ ¬ iteration = 0``


45: ``¬ ¬ ¬ ¬ ¬ while iteration <= (60*2):``

46: ``¬ ¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``

47: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

48: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(NameText, ((self.realWidth-NameTextWidth)/2, (self.realHeight-NameTextHeight)/2))``

49: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(PresentsText, ((((self.realWidth-NameTextWidth)/2)+120), ((self.realHeight-NameTextHeight)/2)+30))``

50: ``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``


51: ``¬ ¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``

52: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``

53: ``¬ ¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``

54: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``


55: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

56: ``¬ ¬ ¬ ¬ ¬ ¬ clock.tick(60)``

57: ``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

58: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``

59: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``


60: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``

61: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``

62: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``

63: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``

64: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``

65: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``


66: ``¬ ¬ ¬ ¬ ¬ iteration = 0``


67: ``¬ ¬ ¬ ¬ while iteration <= (60*3):``

68: ``¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``

69: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

70: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftText, ((self.realWidth-PycraftTextWidth)/2, (self.realHeight-PycraftTextHeight)/2))``

71: ``¬ ¬ ¬ ¬ ¬ iteration += 1``


72: ``¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``

73: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``

74: ``¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``

75: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``


76: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

77: ``¬ ¬ ¬ ¬ ¬ clock.tick(60)``

78: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

79: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``

80: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``


81: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``

82: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``

83: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``


84: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``

85: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``

86: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``


87: ``¬ ¬ ¬ ¬ y = 0``

88: ``¬ ¬ ¬ ¬ while True:``

89: ``¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``

90: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

91: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftText, ((self.realWidth-PycraftTextWidth)/2, ((self.realHeight-PycraftTextHeight)/2)-y))``

92: ``¬ ¬ ¬ ¬ ¬ y += 2``


93: ``¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``

94: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``

95: ``¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``

96: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``


97: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

98: ``¬ ¬ ¬ ¬ ¬ clock.tick(60)``

99: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

100: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``

101: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``


102: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``

103: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``

104: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``


105: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``

106: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``

107: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``

108: ``¬ ¬ ¬ ¬ ¬ if ((self.realHeight-PycraftTextHeight)/2)-y <= 0:``

109: ``¬ ¬ ¬ ¬ ¬ ¬ self.RunFullStartup = False``

110: ``¬ ¬ ¬ ¬ ¬ ¬ return None``

111: ``¬ ¬ ¬ except Exception as Message:``

112: ``¬ ¬ ¬ ¬ self.RunFullStartup = False``

113: ``¬ ¬ ¬ ¬ return Message``

114: ``else:``
115: ``¬ print("You need to run this as part of Pycraft")``
116: ``¬ import tkinter as tk``
117: ``¬ from tkinter import messagebox``
118: ``¬ root = tk.Tk()``
119: ``¬ root.withdraw()``
120: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
121: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_TextUtils>")``
        3: ``¬ class GenerateText:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def LoadQuickText(self):``

7: ``¬ ¬ ¬ LoadingText = ["Use W,A,S,D to move", "Use W to move forward", "Use S to move backward", "Use A to move left", "Use D to move right", "Access your inventory with E", "Access your map with R", "Use SPACE to jump", "Did you know there is a light mode?", "Did you know there is a dark mode?", "Check us out on GitHub", "Use ESC to remove camera movement", "Hold W to sprint", "Did you know you can change the sound volume in settings?", "Did you know you can change the music volume in settings?", "Did you know you can use L to lock the camera"]``

8: ``¬ ¬ ¬ locat = self.mod_Random__.randint(0, (len(LoadingText)-1))``

9: ``¬ ¬ ¬ text = LoadingText[locat]``

10: ``¬ ¬ ¬ return text``

11: ``else:``
12: ``¬ print("You need to run this as part of Pycraft")``
13: ``¬ import tkinter as tk``
14: ``¬ from tkinter import messagebox``
15: ``¬ root = tk.Tk()``
16: ``¬ root.withdraw()``
17: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
18: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_ThemeUtils>")``
        3: ``¬ class DetermineThemeColours:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def GetColours(self):``

7: ``¬ ¬ ¬ try:``

8: ``¬ ¬ ¬ ¬ self.themeArray = [[(255, 255, 255), [30, 30, 30], (80, 80, 80), (237, 125, 49), (255, 255, 255)], [(0, 0, 0), [255, 255, 255], (80, 80, 80), (237, 125, 49), (100, 100, 100)]]``

9: ``¬ ¬ ¬ ¬ if self.theme == "dark":``

10: ``¬ ¬ ¬ ¬ ¬ self.FontCol = self.themeArray[0][0]``

11: ``¬ ¬ ¬ ¬ ¬ self.BackgroundCol = self.themeArray[0][1]``

12: ``¬ ¬ ¬ ¬ ¬ self.ShapeCol = self.themeArray[0][2]``

13: ``¬ ¬ ¬ ¬ ¬ self.AccentCol = self.themeArray[0][3]``

14: ``¬ ¬ ¬ ¬ ¬ self.SecondFontCol = self.themeArray[0][4]``

15: ``¬ ¬ ¬ ¬ elif self.theme == "light":``

16: ``¬ ¬ ¬ ¬ ¬ self.FontCol = self.themeArray[1][0]``

17: ``¬ ¬ ¬ ¬ ¬ self.BackgroundCol = self.themeArray[1][1]``

18: ``¬ ¬ ¬ ¬ ¬ self.ShapeCol = self.themeArray[1][2]``

19: ``¬ ¬ ¬ ¬ ¬ self.AccentCol = self.themeArray[1][3]``

20: ``¬ ¬ ¬ ¬ ¬ self.SecondFontCol = self.themeArray[1][4]``

21: ``¬ ¬ ¬ except Exception as Message:``

22: ``¬ ¬ ¬ ¬ return Message``



23: ``¬ ¬ def GetThemeGUI(self):``

24: ``¬ ¬ ¬ try:``

25: ``¬ ¬ ¬ ¬ clock = self.mod_Pygame__.time.Clock()``

26: ``¬ ¬ ¬ ¬ TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``

27: ``¬ ¬ ¬ ¬ Title = TitleFont.render("Pycraft", True, (255, 255, 255))``

28: ``¬ ¬ ¬ ¬ MiddleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``

29: ``¬ ¬ ¬ ¬ DarkModeFont = MiddleFont.render("Dark", True, (255, 255, 255))``

30: ``¬ ¬ ¬ ¬ LightModeFont = MiddleFont.render("Light", True, (255, 255, 255))``

31: ``¬ ¬ ¬ ¬ mousebuttondown = False``

32: ``¬ ¬ ¬ ¬ while self.theme == False:``

33: ``¬ ¬ ¬ ¬ ¬ self.Display.fill([30, 30, 30])``

34: ``¬ ¬ ¬ ¬ ¬ mX, mY = self.mod_Pygame__.mouse.get_pos()``

35: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``

36: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``

37: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``


38: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``

39: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``

40: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``


41: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``

42: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``

43: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:``

44: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True``

45: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONUP:``

46: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``


47: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Title, (540, 0))``

48: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(DarkModeFont, (320, 360))``

49: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(LightModeFont, (890, 360))``

50: ``¬ ¬ ¬ ¬ ¬ DarkRect = self.mod_Pygame__.Rect(260, 300, 200, 160)``

51: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (80, 80, 80), DarkRect, 3)``

52: ``¬ ¬ ¬ ¬ ¬ LightRect = self.mod_Pygame__.Rect(820, 300, 200, 160)``

53: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (80, 80, 80), LightRect, 3)``

54: ``¬ ¬ ¬ ¬ ¬ if mX >= 260 and mX <= 460 and mY >= 300 and mY <= 460:``

55: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

56: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "dark"``

57: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.base_folder = self.mod_OS__.path.dirname(__file__)``

58: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``


59: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.set_volume(50)``


60: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.play()``

61: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

62: ``¬ ¬ ¬ ¬ ¬ elif mX >= 820 and mX <= 980 and mY >= 300 and mY <= 460:``

63: ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``

64: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "light"``

65: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.base_folder = self.mod_OS__.path.dirname(__file__)``

66: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``


67: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.set_volume(50)``


68: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.play()``

69: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

70: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``

71: ``¬ ¬ ¬ ¬ ¬ clock.tick(60)``

72: ``¬ ¬ ¬ except Exception as Message:``

73: ``¬ ¬ ¬ ¬ Message = str(Message)+" in <Pycraft_ThemeUtils>"``

74: ``¬ ¬ ¬ ¬ return Message``


75: ``¬ ¬ ¬ return None``

76: ``else:``
77: ``¬ print("You need to run this as part of Pycraft")``
78: ``¬ import tkinter as tk``
79: ``¬ from tkinter import messagebox``
80: ``¬ root = tk.Tk()``
81: ``¬ root.withdraw()``
82: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
83: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_ThreadingUtils>")``
        3: ``¬ class ThreadingUtils:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def StartVariableChecking(self):``

7: ``¬ ¬ ¬ while True:``

8: ``¬ ¬ ¬ ¬ if self.Iteration > 1000:``

9: ``¬ ¬ ¬ ¬ ¬ self.aFPS = (self.aFPS/self.Iteration)``

10: ``¬ ¬ ¬ ¬ ¬ self.Iteration = 1``

11: ``¬ ¬ ¬ ¬ self.FPS = int(self.FPS)``

12: ``¬ ¬ ¬ ¬ self.eFPS = int(self.eFPS)``


13: ``¬ ¬ ¬ ¬ self.mod_Time__.sleep(1)``


14: ``¬ ¬ ¬ ¬ if self.Stop_Thread_Event.is_set():``

15: ``¬ ¬ ¬ ¬ ¬ break``


16: ``¬ ¬ def StartCPUlogging(self):``

17: ``¬ ¬ ¬ while True:``

18: ``¬ ¬ ¬ ¬ if self.Devmode == 10:``

19: ``¬ ¬ ¬ ¬ ¬ if self.Timer >= 2:``

20: ``¬ ¬ ¬ ¬ ¬ ¬ CPUPercent = self.mod_Psutil__.cpu_percent(0.2)``

21: ``¬ ¬ ¬ ¬ ¬ ¬ if CPUPercent > self.Data_CPUUsE_Max:``

22: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = CPUPercent``

23: ``¬ ¬ ¬ ¬ ¬ ¬ elif CPUPercent < self.Data_CPUUsE_Min:``

24: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = CPUPercent``


25: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE.append([((self.realWidth/2)+100)+(self.Timer-2), 200-(100/self.Data_CPUUsE_Max)*CPUPercent])``

26: ``¬ ¬ ¬ ¬ ¬ else:``

27: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(0.2)``

28: ``¬ ¬ ¬ ¬ else:``

29: ``¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(1)``


30: ``¬ ¬ ¬ ¬ if self.Stop_Thread_Event.is_set():``

31: ``¬ ¬ ¬ ¬ ¬ break``


32: ``¬ ¬ def AdaptiveMode(self):``

33: ``¬ ¬ ¬ while True:``

34: ``¬ ¬ ¬ ¬ if self.Stop_Thread_Event.is_set():``

35: ``¬ ¬ ¬ ¬ ¬ break``


36: ``¬ ¬ ¬ ¬ if self.SettingsPreference == "Adaptive":``

37: ``¬ ¬ ¬ ¬ ¬ CPUPercent = self.mod_Psutil__.cpu_percent()``

38: ``¬ ¬ ¬ ¬ ¬ CoreCount = self.mod_Psutil__.cpu_count()``


39: ``¬ ¬ ¬ ¬ ¬ try:``

40: ``¬ ¬ ¬ ¬ ¬ ¬ gpus = self.mod_GPUtil__.getGPUs()``


41: ``¬ ¬ ¬ ¬ ¬ ¬ GPUPercent = 0``

42: ``¬ ¬ ¬ ¬ ¬ ¬ NumOfGPUs = 0``


43: ``¬ ¬ ¬ ¬ ¬ ¬ for gpu in gpus:``

44: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ NumOfGPUs += 1``

45: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ GPUPercent += gpu.load*100``


46: ``¬ ¬ ¬ ¬ ¬ ¬ GPUPercent = GPUPercent/NumOfGPUs``


47: ``¬ ¬ ¬ ¬ ¬ except:``

48: ``¬ ¬ ¬ ¬ ¬ ¬ GPUPercent = CPUPercent``


49: ``¬ ¬ ¬ ¬ ¬ if (CPUPercent >= (100/CoreCount)) and (GPUPercent >= (100/CoreCount)):``

50: ``¬ ¬ ¬ ¬ ¬ ¬ self.FPS -= 10``

51: ``¬ ¬ ¬ ¬ ¬ else:``

52: ``¬ ¬ ¬ ¬ ¬ ¬ if self.FPS < self.RecommendedFPS:``

53: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS += 10``

54: ``¬ ¬ ¬ ¬ ¬ ¬ else:``

55: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not (self.FPS == self.RecommendedFPS):``

56: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS -= 1``


57: ``¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(0.2)``

58: ``¬ ¬ ¬ ¬ else:``

59: ``¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(1)``



60: ``else:``
61: ``¬ print("You need to run this as part of Pycraft")``
62: ``¬ import tkinter as tk``
63: ``¬ from tkinter import messagebox``
64: ``¬ root = tk.Tk()``
65: ``¬ root.withdraw()``
66: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
67: ``¬ quit()``




.. note::
   For information on this consult the above guide
        1: ``if not __name__ == "__main__":``
        2: ``print("Started <Pycraft_TkinterUtils>")``
        3: ``¬ class TkinterInfo:``
        4: ``¬ ¬ def __init__(self):``
        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def CreateTkinterWindow(self):``

7: ``¬ ¬ ¬ DataWindow = self.mod_Tkinter__tk.Tk()``

8: ``¬ ¬ ¬ DataWindow.title("Player Information")``

9: ``¬ ¬ ¬ DataWindow.configure(width = 500, height = 300)``

10: ``¬ ¬ ¬ DataWindow.configure(bg="lightblue")``

11: ``¬ ¬ ¬ VersionData = f"Pycraft: v{self.version}"``

12: ``¬ ¬ ¬ CoordinatesData = f"Coordinates: x: {self.X} y: {self.Y} z: {self.Z} Facing: 0.0, 0.0, 0.0"``

13: ``¬ ¬ ¬ FPSData = f"FPS: Actual: {self.eFPS} Max: {self.FPS}"``

14: ``¬ ¬ ¬ VersionData = self.mod_Tkinter__tk.Label(DataWindow, text=VersionData)``

15: ``¬ ¬ ¬ CoordinatesData = self.mod_Tkinter__tk.Label(DataWindow, text=CoordinatesData)``

16: ``¬ ¬ ¬ FPSData = self.mod_Tkinter__tk.Label(DataWindow, text=FPSData)``

17: ``¬ ¬ ¬ VersionData.grid(row = 0, column = 0, columnspan = 2)``

18: ``¬ ¬ ¬ CoordinatesData.grid(row = 1, column = 0, columnspan = 2)``

19: ``¬ ¬ ¬ FPSData.grid(row = 2, column = 0, columnspan = 2)``

20: ``¬ ¬ ¬ DataWindow.mainloop()``

21: ``¬ ¬ ¬ DataWindow.quit()``

22: ``else:``
23: ``¬ print("You need to run this as part of Pycraft")``
24: ``¬ import tkinter as tk``
25: ``¬ from tkinter import messagebox``
26: ``¬ root = tk.Tk()``
27: ``¬ root.withdraw()``
28: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
29: ``¬ quit()``