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
   1. ``if not __name__ == "__main__":``
   2. ``¬ print("Started <Pycraft_Achievements>")``
   3. ``¬ class GenerateAchievements:``
   4. ``¬ ¬ def __init__(self):``
   5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def Achievements(self):``
7. ``¬ ¬ ¬ try:``
8. ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol) ``
9. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
10. ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")``
11. ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) ``
12. ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
13. ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

14. ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
15. ``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``

16. ``¬ ¬ ¬ ¬ AchievementsFont = InfoTitleFont.render("Achievements", self.aa, self.SecondFontCol)``
17. ``¬ ¬ ¬ ¬ tempFPS = self.FPS``

18. ``¬ ¬ ¬ ¬ while True:``
19. ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

20. ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
21. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
22. ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
23. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

24. ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
25. ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS ``
26. ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``
27. ``¬ ¬ ¬ ¬ ¬ ``
28. ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``

29. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get(): ``
30. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE): ``
31. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
32. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
33. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
34. ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN: ``
35. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10: ``
36. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1 ``
37. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
38. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
37. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
38. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
39. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x: ``
40. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1 ``

41. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")``
42. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
43. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

44. ``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``
45. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
46. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
47. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))``

48. ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
49. ``¬ ¬ ¬ ¬ ¬ if not Message == None:``
50. ``¬ ¬ ¬ ¬ ¬ ¬ return Message``
51. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip() ``
52. ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
53. ``¬ ¬ ¬ except Exception as Message:``
54. ``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
   55. ``else:``
   56. ``¬ print("You need to run this as part of Pycraft")``
   57. ``¬ import tkinter as tk``
   58. ``¬ from tkinter import messagebox``
   59. ``¬ root = tk.Tk()``
   60. ``¬ root.withdraw()``
   61. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   62. ``¬ quit()``


Base
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

1. ``if not __name__ == "__main__":``
2. ``¬ print("Started <Pycraft_Base>")``

3. ``¬ import moderngl_window as mglw``
4. ``¬ from moderngl_window.scene.camera import KeyboardCamera, OrbitCamera``


5. ``¬ class CameraWindow(mglw.WindowConfig):``
6. ``¬ ¬ """Base class with built in 3D camera support"""``

7. ``¬ ¬ def __init__(self, **kwargs):``
8. ``¬ ¬ ¬ super().__init__(**kwargs)``
9. ``¬ ¬ ¬ self.camera = KeyboardCamera(self.wnd.keys, aspect_ratio=self.wnd.aspect_ratio)``
10. ``¬ ¬ ¬ self.camera_enabled = True``

11. ``¬ ¬ def key_event(self, key, action, modifiers):``
12. ``¬ ¬ ¬ keys = self.wnd.keys``

13. ``¬ ¬ ¬ if self.camera_enabled:``
14. ``¬ ¬ ¬ ¬ self.camera.key_input(key, action, modifiers)``

15. ``¬ ¬ ¬ if action == keys.ACTION_PRESS:``
16. ``¬ ¬ ¬ ¬ if key == keys.C:``
17. ``¬ ¬ ¬ ¬ ¬ self.camera_enabled = not self.camera_enabled``
18. ``¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = self.camera_enabled``
19. ``¬ ¬ ¬ ¬ ¬ self.wnd.cursor = not self.camera_enabled``
20. ``¬ ¬ ¬ ¬ if key == keys.SPACE:``
21. ``¬ ¬ ¬ ¬ ¬ self.timer.toggle_pause()``

22. ``¬ ¬ def mouse_position_event(self, x: int, y: int, dx, dy):``
23. ``¬ ¬ ¬ if self.camera_enabled:``
24. ``¬ ¬ ¬ ¬ self.camera.rot_state(-dx, -dy)``

25. ``¬ ¬ def resize(self, width: int, height: int):``
26. ``¬ ¬ ¬ self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)``


27. ``¬ class OrbitCameraWindow(mglw.WindowConfig):``
28. ``¬ ¬ """Base class with built in 3D orbit camera support"""``

29. ``¬ ¬ def __init__(self, **kwargs):``
30. ``¬ ¬ ¬ super().__init__(**kwargs)``
31. ``¬ ¬ ¬ self.camera = OrbitCamera(aspect_ratio=self.wnd.aspect_ratio)``
32. ``¬ ¬ ¬ self.camera_enabled = True``

33. ``¬ ¬ def key_event(self, key, action, modifiers):``
34. ``¬ ¬ ¬ keys = self.wnd.keys``

35. ``¬ ¬ ¬ if action == keys.ACTION_PRESS:``
36. ``¬ ¬ ¬ ¬ if key == keys.C:``
37. ``¬ ¬ ¬ ¬ ¬ self.camera_enabled = not self.camera_enabled``
38. ``¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = self.camera_enabled``
39. ``¬ ¬ ¬ ¬ ¬ self.wnd.cursor = not self.camera_enabled``
40. ``¬ ¬ ¬ ¬ if key == keys.SPACE:``
41. ``¬ ¬ ¬ ¬ ¬ self.timer.toggle_pause()``

42. ``¬ ¬ def mouse_position_event(self, x: int, y: int, dx, dy):``
43. ``¬ ¬ ¬ if self.camera_enabled:``
44. ``¬ ¬ ¬ ¬ self.camera.rot_state(dx, dy)``

45. ``¬ ¬ def mouse_scroll_event(self, x_offset: float, y_offset: float):``
46. ``¬ ¬ ¬ if self.camera_enabled:``
47. ``¬ ¬ ¬ ¬ self.camera.zoom_state(y_offset)``

48. ``¬ ¬ def resize(self, width: int, height: int):``
49. ``¬ ¬ ¬ self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)``

Benchmark
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
   1. ``if not __name__ == "__main__":``
   2. ``¬ print("Started <Pycraft_Benchmark>")``
   3. ``¬ class GenerateBenchmarkMenu:``
   4. ``¬ ¬ def __init__(self):``
   5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def Benchmark(self):``
7. ``¬ ¬ ¬ try:``
8. ``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).pause()``
9. ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol) ``
10. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
11. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark")``
12. ``¬ ¬ ¬ ¬ self.VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15) ``
13. ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) ``
14. ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
15. ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
16. ``¬ ¬ ¬ ¬ DetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``
17. ``¬ ¬ ¬ ¬ InfoDetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
18. ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
19. ``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``

20. ``¬ ¬ ¬ ¬ BenchmarkFont = InfoTitleFont.render("Benchmark", self.aa, self.SecondFontCol)``
21. ``¬ ¬ ¬ ¬ FPSinfoTEXT = DetailsFont.render("FPS benchmark results", self.aa, self.FontCol)``
22. ``¬ ¬ ¬ ¬ FPSinfoTEXTWidth = FPSinfoTEXT.get_width()``
23. ``¬ ¬ ¬ ¬ FILEinfoTEXT = DetailsFont.render("Read test results", self.aa, self.FontCol)``
24. ``¬ ¬ ¬ ¬ FILEinfoTEXTWidth = FILEinfoTEXT.get_width()``
25. ``¬ ¬ ¬ ¬ HARDWAREinfoTEXT = DetailsFont.render("Hardware results", self.aa, self.FontCol)``
26. ``¬ ¬ ¬ ¬ HARDWAREinfoTEXTwidth = HARDWAREinfoTEXT.get_width()``

27. ``¬ ¬ ¬ ¬ SixtyFPSData = DataFont.render("60 Hz", self.aa, self.AccentCol)``
28. ``¬ ¬ ¬ ¬ OneFourFourFPSData = DataFont.render("144 Hz", self.aa, self.AccentCol)``
29. ``¬ ¬ ¬ ¬ TwoFortyFPSData = DataFont.render("240 Hz", self.aa, self.AccentCol)``

30. ``¬ ¬ ¬ ¬ InfoFont1 = DataFont.render("Welcome to Benchmark mode, press the SPACE bar to continue or press ANY other key to cancel, or press 'X'", self.aa, self.FontCol)``
31. ``¬ ¬ ¬ ¬ InfoFont2 = DataFont.render("Benchmark mode is used to make the 'ADAPTIVE' feature in settings function and also to give an indication of the experience you are likely to get on this device", self.aa, self.FontCol)``
32. ``¬ ¬ ¬ ¬ InfoFont3 = DataFont.render("Benchmark mode consists of several stages:", self.aa, self.FontCol)``
33. ``¬ ¬ ¬ ¬ InfoFont4 = DataFont.render("First it will gather some basic information about your system", self.aa, self.FontCol)``
34. ``¬ ¬ ¬ ¬ InfoFont5 = DataFont.render("Then it will test your maximum frame rate on a blank screen, then with a basic animation, and finally in a 3D OpenGL space", self.aa, self.FontCol)``
35. ``¬ ¬ ¬ ¬ InfoFont6 = DataFont.render("After its done that the focus moves on to a quick storage test, before finishing", self.aa, self.FontCol)``
36. ``¬ ¬ ¬ ¬ InfoFont7 = DataFont.render("Your results will then be displayed on screen with your frame rate scores on a line graph and the rest detailed to the right", self.aa, self.FontCol)``
37. ``¬ ¬ ¬ ¬ InfoFont8 = DataFont.render("During the time the benchmark is running the window may appear unresponsive, don't panic this can be expected.", self.aa, self.FontCol)``
38. ``¬ ¬ ¬ ¬ InfoFont9 = DataFont.render("In addition to achieve the best scores try to avoid doing anything else on the computer whilst the benchmark runs", self.aa, self.FontCol)``
39. ``¬ ¬ ¬ ¬ InfoFont10 = DataFont.render("This benchmark may show some system instability or cause your device to get warm, you use this at your own risk!", self.aa, (255, 0, 0))``

40. ``¬ ¬ ¬ ¬ stage = 0``

41. ``¬ ¬ ¬ ¬ resize = False``

42. ``¬ ¬ ¬ ¬ while True:``
43. ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

44. ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
45. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
46. ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
47. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

48. ``¬ ¬ ¬ ¬ ¬ if stage == 0:``
49. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
50. ``¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``
51. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
52.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
53.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))``
54.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont1, (3, 100))``
55.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont2, (3, 130))``
56.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont3, (3, 145))``
57.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont4, (3, 160))``
58.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont5, (3, 175))``
59.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont6, (3, 190))``
60.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont7, (3, 220))``
61.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont8, (3, 235))``
62.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont9, (3, 250))``
63.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont10, (3, 280))``

64.	``¬ ¬ ¬ ¬ ¬ if stage == 1:``
65.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Getting System Information")``
66.	``¬ ¬ ¬ ¬ ¬ ¬ CPUid = f"{self.mod_CPUinfo__.get_cpu_info()['brand_raw']} w/{self.mod_Psutil__.cpu_count(logical=False)} cores @ {self.mod_Psutil__.cpu_freq().max} MHz"``
67.	``¬ ¬ ¬ ¬ ¬ ¬ RAMid = f"{round((((self.mod_Psutil__.virtual_memory().total)/1000)/1000/1000),2)} GB of memory, with {self.mod_Psutil__.virtual_memory().percent}% used"``
68.	``¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFO = DataFont.render(CPUid, self.aa, (255, 255, 255))``
69.	``¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFOwidth = CPUhwINFO.get_width()``

70.	``¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFO = DataFont.render(RAMid, self.aa, (255, 255, 255))``
71.	``¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFOwidth = RAMhwINFO.get_width()``
72.	``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``

73.	``¬ ¬ ¬ ¬ ¬ if stage == 2:``
74.	``¬ ¬ ¬ ¬ ¬ ¬ try:``
75.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3 = self.mod_ExBenchmark__.LoadBenchmark.run(self)``
76.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:``
77.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message``
78.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``
79.	``¬ ¬ ¬ ¬ ¬ ¬ except:``
80.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Cancelled benchmark")``
81.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
82.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
83.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Finished self.FPS based benchmarks")``
84.	``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``

85.	``¬ ¬ ¬ ¬ ¬ if stage == 3:``
86.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Starting disk read test")``
87.	``¬ ¬ ¬ ¬ ¬ ¬ ReadIteration = 50``
88.	``¬ ¬ ¬ ¬ ¬ ¬ for i in range(ReadIteration):``
89.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:``
90.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Benchdata = Bench.read()``

91.	``¬ ¬ ¬ ¬ ¬ ¬ aTime = 0``
92.	``¬ ¬ ¬ ¬ ¬ ¬ ReadIteration = 50``
93.	``¬ ¬ ¬ ¬ ¬ ¬ for i in range(ReadIteration):``
94.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ start = self.mod_Time__.perf_counter()``
95.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:``
96.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Benchdata = Bench.read()``
97.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ aTime += self.mod_Time__.perf_counter()-start``
98.	``¬ ¬ ¬ ¬ ¬ ¬ aTime = aTime/(ReadIteration+1)``
99.	``¬ ¬ ¬ ¬ ¬ ¬ ReadSpeed = (1/(aTime))``
100.	``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``
101.	``¬ ¬ ¬ ¬ ¬ ``
102.	``¬ ¬ ¬ ¬ ¬ if stage == 4:``
103.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results.")``
104.	``¬ ¬ ¬ ¬ ¬ ¬ Max1 = 0``
105.	``¬ ¬ ¬ ¬ ¬ ¬ Min1 = 60``
106.	``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):``
107.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY[i] > Max1:``
108.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max1 = FPSlistY[i]``
109.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY[i] < Min1:``
110.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min1 = FPSlistY[i]``

111.	``¬ ¬ ¬ ¬ ¬ ¬ Max2 = 0``
112.	``¬ ¬ ¬ ¬ ¬ ¬ Min2 = 60``
113.	``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``
114.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY2[i] > Max2:``
115.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max2 = FPSlistY2[i]``
116.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY2[i] < Min2:``
117.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min2 = FPSlistY2[i]``

118.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results..")``
119.	``¬ ¬ ¬ ¬ ¬ ¬ Max3 = 0``
120.	``¬ ¬ ¬ ¬ ¬ ¬ Min3 = 60``
121.	``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY3)):``
122.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY3[i] > Max3:``
123.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max3 = FPSlistY3[i]``
124.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY3[i] < Min3:``
125.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min3 = FPSlistY3[i]``

126.	``¬ ¬ ¬ ¬ ¬ ¬ if Max2 > Max1:``
127.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max2``
128.	``¬ ¬ ¬ ¬ ¬ ¬ elif Max3 > Max2:``
129.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max3``
130.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
131.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max1``

132.	``¬ ¬ ¬ ¬ ¬ ¬ self.RecommendedFPS = GlobalMax/2``

133.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results...")``
134.	``¬ ¬ ¬ ¬ ¬ ¬ multiplier = len(FPSlistY)/(realWidth-20)``
135.	``¬ ¬ ¬ ¬ ¬ ¬ temp = []``
136.	``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):``
137.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY[i])))``
138.	``¬ ¬ ¬ ¬ ¬ ¬ FPSListY = temp``

139.	``¬ ¬ ¬ ¬ ¬ ¬ temp = []``
140.	``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``
141.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY2[i])))``
142.	``¬ ¬ ¬ ¬ ¬ ¬ FPSListY2 = temp``

143.	``¬ ¬ ¬ ¬ ¬ ¬ temp = []``
144.	``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``
145.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY3[i])))``
146.	``¬ ¬ ¬ ¬ ¬ ¬ FPSListY3 = temp``

147.	``¬ ¬ ¬ ¬ ¬ ¬ Results1 = []``
148.	``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):``
149.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results1.append([(FPSlistX[i]/multiplier), FPSListY[i]])``

150.	``¬ ¬ ¬ ¬ ¬ ¬ Results2 = []``
151.	``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``
152.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results2.append([(FPSlistX2[i]/multiplier), FPSListY2[i]])``

153.	``¬ ¬ ¬ ¬ ¬ ¬ Results3 = []``
154.	``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY3)):``
155.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results3.append([(FPSlistX3[i]/multiplier), FPSListY3[i]])``

156.	``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``

157.	``¬ ¬ ¬ ¬ ¬ if stage == 5:``
158.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Results")``

159.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

160.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
161.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))``

162.	``¬ ¬ ¬ ¬ ¬ ¬ FPSRect = self.mod_Pygame__.Rect(10, 130, realWidth-20, 300)``
163.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FPSRect, 0)``

164.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*60)))), (realWidth-20, int(130+(300-((300/GlobalMax)*60)))))``
165.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SixtyFPSData, (13, int(130+(300-((300/GlobalMax)*60)))))``

166.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*144)))), (realWidth-20, int(130+(300-((300/GlobalMax)*144)))))``
167.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(OneFourFourFPSData, (13, int(130+(300-((300/GlobalMax)*140)))))``

168.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*240)))), (realWidth-20, int(130+(300-((300/GlobalMax)*240)))))``
169.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TwoFortyFPSData, (13, int(130+(300-((300/GlobalMax)*240)))))``

170.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 255, 0), False, Results1)``
171.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 0, 255), False, Results2)``
172.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 0), False, Results3)``

173.	``¬ ¬ ¬ ¬ ¬ ¬ HideRect = self.mod_Pygame__.Rect(0, 110, realWidth, 330)``
174.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.BackgroundCol, HideRect, 20)``
175.	``¬ ¬ ¬ ¬ ¬ ¬ ``
176.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSinfoTEXT, ((realWidth-FPSinfoTEXTWidth)-3, 100))``
177.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FILEinfoTEXT, ((realWidth-FILEinfoTEXTWidth)-3, 430))``

178.	``¬ ¬ ¬ ¬ ¬ ¬ FileResults = DataFont.render(f"Your device achieved a score of: {round(ReadSpeed, 2)}/100 ({round((100/100)*ReadSpeed)}%)", self.aa, self.FontCol)``
179.	``¬ ¬ ¬ ¬ ¬ ¬ FileResultsWidth = FileResults.get_width()``
180.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FileResults, ((realWidth-FileResultsWidth)-3, 460))``
181.	``¬ ¬ ¬ ¬ ¬ ¬ ``
182.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(HARDWAREinfoTEXT, ((realWidth-HARDWAREinfoTEXTwidth)-3, 480))``

183.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CPUhwINFO, ((realWidth-CPUhwINFOwidth)-3, 500))``
184.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(RAMhwINFO, ((realWidth-RAMhwINFOwidth)-3, 516))``

185.	``¬ ¬ ¬ ¬ ¬ ¬ GreenInfo = InfoDetailsFont.render(f"Blank screen test (green); Minimum: {round(Min1, 4)} FPS, Maximum: {round(Max1, 4)} FPS", self.aa, self.FontCol)``
186.	``¬ ¬ ¬ ¬ ¬ ¬ BlueInfo = InfoDetailsFont.render(f"Drawing test (blue); Minimum: {round(Min2, 4)} FPS, Maximum: {round(Max2, 4)} FPS", self.aa, self.FontCol)``
187.	``¬ ¬ ¬ ¬ ¬ ¬ RedInfo = InfoDetailsFont.render(f"OpenGL test (red); Minimum: {round(Min3, 4)} FPS, Maximum: {round(Max3, 4)} FPS", self.aa, self.FontCol)``
188.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(GreenInfo, (3, 430))``
189.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BlueInfo, (3, 445))``
190.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(RedInfo, (3, 460))``

191.	``¬ ¬ ¬ ¬ ¬ ¬ if resize == True:``
192.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ stage = 4``
193.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ resize = False``

194.	``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
195.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE) and stage <= 3) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE): ``
196.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
197.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
198.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
199.	``¬ ¬ ¬ ¬ ¬ ¬ if (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_SPACE) and stage == 0:``
200.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ stage += 1``
201.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.VIDEORESIZE:``
202.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ resize = True``

203.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
204.	``¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)``
205.	``¬ ¬ ¬ except Exception as Message:``
206.	``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    207.	``else:``
    208.	``¬ print("You need to run this as part of Pycraft")``
    209.	``¬ import tkinter as tk``
    210.	``¬ from tkinter import messagebox``
    211.	``¬ root = tk.Tk()``
    212.	``¬ root.withdraw()``
    213.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    214.	``¬ quit()``


CaptionUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_CaptionUtils>")``
    3.	``¬ class GenerateCaptions:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def GetLoadingCaption(self, num):``
7.	``¬ ¬ ¬ if num == 0:``
8.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (-)")``
9.	``¬ ¬ ¬ elif num == 1:``
10.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (\)")``
11.	``¬ ¬ ¬ elif num == 2:``
12.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (|)")``
13.	``¬ ¬ ¬ elif num == 3:``
14.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (/)")``
15.	``¬ ¬ ¬ else:``
16.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading")``
17.	``¬ ¬ ¬ self.mod_Pygame__.display.update()``

18.	``¬ ¬ def GetNormalCaption(self, location):``
19.	``¬ ¬ ¬ if self.Devmode >= 5 and self.Devmode <= 9:``
20.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | you are: {10-self.Devmode} steps away from being a developer") ``
21.	``¬ ¬ ¬ elif self.Devmode == 10: ``
22.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | Developer Mode | Pos: {round(self.X, 2)}, {round(self.Y, 2)}, {round(self.Z, 2)} | V: {self.Total_move_x}, {self.Total_move_y}, {self.Total_move_z} FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: {int(self.aFPS/self.Iteration)} Iteration: {self.Iteration} | MemUsE: {self.mod_Psutil__.virtual_memory().percent} | CPUUsE: {self.mod_Psutil__.cpu_percent()} | Theme: {self.theme} | Thread Count: {self.mod_Threading__.active_count()}") ``
23.	``¬ ¬ ¬ else:``
24.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location}")``

.. note::
    For information on this consult the above guide
    25.	``else:``
    26.	``¬ print("You need to run this as part of Pycraft")``
    27.	``¬ import tkinter as tk``
    28.	``¬ from tkinter import messagebox``
    29.	``¬ root = tk.Tk()``
    30.	``¬ root.withdraw()``
    31.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    32.	``¬ quit()``


Character Designer
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_CharacterDesigner>")``
    3.	``¬ class GenerateCharacterDesigner:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def CharacterDesigner(self):``
7.	``¬ ¬ ¬ try:``
8.	``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol) ``
9.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
10.	``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")``
11.	``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) ``
12.	``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
13.	``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

14.	``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.SecondFontCol)``
15.	``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``

16.	``¬ ¬ ¬ ¬ AchievementsFont = InfoTitleFont.render("Character Designer", self.aa, self.FontCol)``
17.	``¬ ¬ ¬ ¬ tempFPS = self.FPS``

18.	``¬ ¬ ¬ ¬ while True:``
19.	``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

20.	``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
21.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
22.	``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
23.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

24.	``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
25.	``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS ``
26.	``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``
27.	``¬ ¬ ¬ ¬ ¬ ``
28.	``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``

29.	``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get(): ``
30.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE): ``
31.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
32.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
33.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
34.	``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN: ``
35.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10: ``
36.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1 ``
37.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
38.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
39.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
40.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
41.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x: ``
42.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1 ``

43.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")``
44.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
45.	``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

46.	``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``
47.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
48.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
49.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))``

50.	``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
51.	``¬ ¬ ¬ ¬ ¬ if not Message == None:``
52.	``¬ ¬ ¬ ¬ ¬ ¬ return Message``
53.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip() ``
54.	``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
55.	``¬ ¬ ¬ except Exception as Message:``
56.	``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    57.	``else:``
    58.	``¬ print("You need to run this as part of Pycraft")``
    59.	``¬ import tkinter as tk``
    60.	``¬ from tkinter import messagebox``
    61.	``¬ root = tk.Tk()``
    62.	``¬ root.withdraw()``
    63.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    64.	``¬ quit()``


Credits
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_Credits>")``
    3.	``¬ class GenerateCredits:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def Credits(self):``
7.	``¬ ¬ ¬ try:``
8.	``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
9.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip() ``
10.	``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits")``
11.	``¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
12.	``¬ ¬ ¬ ¬ LargeCreditsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``
13.	``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) ``
14.	``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
15.	``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
16.	``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
17.	``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``
18.	``¬ ¬ ¬ ¬ TitleHeight = TitleFont.get_height()``
19.	``¬ ¬ ¬ ¬ CreditsFont = InfoTitleFont.render("Credits", self.aa, self.SecondFontCol) ``
20.	``¬ ¬ ¬ ¬ Credits1 = LargeCreditsFont.render(f"Pycraft: v{self.version}", self.aa, self.FontCol)``
21.	``¬ ¬ ¬ ¬ Credits1Width = Credits1.get_width()``
22.	``¬ ¬ ¬ ¬ Credits2 = LargeCreditsFont.render("Game Director: Tom Jebbo", self.aa, self.FontCol)``
23.	``¬ ¬ ¬ ¬ Credits2Width = Credits2.get_width()``
24.	``¬ ¬ ¬ ¬ Credits3 = LargeCreditsFont.render("Art and Music Lead: Tom Jebbo", self.aa, self.FontCol)``
25.	``¬ ¬ ¬ ¬ Credits3Width = Credits3.get_width()``
26.	``¬ ¬ ¬ ¬ Credits4 = LargeCreditsFont.render("Other Music Credits:", self.aa, self.FontCol)``
27.	``¬ ¬ ¬ ¬ Credits4Width = Credits4.get_width()``
28.	``¬ ¬ ¬ ¬ Credits5 = LargeCreditsFont.render("Freesound: - Erokia's 'ambient wave compilation' @ freesound.org/s/473545", self.aa, self.FontCol)``
29.	``¬ ¬ ¬ ¬ Credits5Width = Credits5.get_width()``
30.	``¬ ¬ ¬ ¬ Credits6 = LargeCreditsFont.render("Freesound: - Soundholder's 'ambient meadow near forest' @ freesound.org/s/425368", self.aa, self.FontCol)``
31.	``¬ ¬ ¬ ¬ Credits6Width = Credits6.get_width()``
32.	``¬ ¬ ¬ ¬ Credits7 = LargeCreditsFont.render("Freesound: - monte32's 'Footsteps_6_Dirt_shoe' @ freesound.org/people/monte32/sounds/353799", self.aa, self.FontCol)``
33.	``¬ ¬ ¬ ¬ Credits7Width = Credits7.get_width()``
34.	``¬ ¬ ¬ ¬ Credits8 = LargeCreditsFont.render("With thanks to the developers of:", self.aa, self.FontCol)``
35.	``¬ ¬ ¬ ¬ Credits8Width = Credits8.get_width()``
36.	``¬ ¬ ¬ ¬ Credits9 = LargeCreditsFont.render("PSutil", self.aa, self.FontCol)``
37.	``¬ ¬ ¬ ¬ Credits9Width = Credits9.get_width()``
38.	``¬ ¬ ¬ ¬ Credits10 = LargeCreditsFont.render("Python", self.aa, self.FontCol)``
39.	``¬ ¬ ¬ ¬ Credits10Width = Credits10.get_width()``
40.	``¬ ¬ ¬ ¬ Credits11 = LargeCreditsFont.render("Pygame", self.aa, self.FontCol)``
41.	``¬ ¬ ¬ ¬ Credits11Width = Credits11.get_width()``
42.	``¬ ¬ ¬ ¬ Credits12 = LargeCreditsFont.render("Numpy", self.aa, self.FontCol)``
43.	``¬ ¬ ¬ ¬ Credits12Width = Credits12.get_width()``
44.	``¬ ¬ ¬ ¬ Credits13 = LargeCreditsFont.render("Nuitka", self.aa, self.FontCol)``
45.	``¬ ¬ ¬ ¬ Credits13Width = Credits13.get_width()``
46.	``¬ ¬ ¬ ¬ Credits14 = LargeCreditsFont.render("CPUinfo", self.aa, self.FontCol)``
47.	``¬ ¬ ¬ ¬ Credits14Width = Credits14.get_width()``
48.	``¬ ¬ ¬ ¬ Credits15 = LargeCreditsFont.render("PyInstaller", self.aa, self.FontCol)``
49.	``¬ ¬ ¬ ¬ Credits15Width = Credits15.get_width()``
50.	``¬ ¬ ¬ ¬ Credits16 = LargeCreditsFont.render("PyAutoGUI", self.aa, self.FontCol)``
51.	``¬ ¬ ¬ ¬ Credits16Width = Credits16.get_width()``
52.	``¬ ¬ ¬ ¬ Credits17 = LargeCreditsFont.render("PyWaveFront", self.aa, self.FontCol)``
53.	``¬ ¬ ¬ ¬ Credits17Width = Credits17.get_width()``
54.	``¬ ¬ ¬ ¬ Credits18 = LargeCreditsFont.render("Microsoft's Visual Studio Code", self.aa, self.FontCol)``
55.	``¬ ¬ ¬ ¬ Credits18Width = Credits18.get_width()``
56.	``¬ ¬ ¬ ¬ Credits19 = LargeCreditsFont.render("PIL (Pillow/Python Imaging Library)", self.aa, self.FontCol)``
57.	``¬ ¬ ¬ ¬ Credits19Width = Credits19.get_width()``
58.	``¬ ¬ ¬ ¬ Credits20 = LargeCreditsFont.render("PyOpenGL (and PyOpenGL-accelerate)", self.aa, self.FontCol)``
59.	``¬ ¬ ¬ ¬ Credits20Width = Credits20.get_width()``
60.	``¬ ¬ ¬ ¬ Credits21 = LargeCreditsFont.render("For more in depth accreditation please check the GitHub Page @ github.com/PycraftDeveloper/Pycraft", self.aa, self.FontCol)``
61.	``¬ ¬ ¬ ¬ Credits21Width = Credits21.get_width()``
62.	``¬ ¬ ¬ ¬ Credits22 = LargeCreditsFont.render("With thanks to:", self.aa, self.FontCol)``
63.	``¬ ¬ ¬ ¬ Credits22Width = Credits22.get_width()``
64.	``¬ ¬ ¬ ¬ Credits23 = LargeCreditsFont.render("All my wonderful followers on Twitter, and you for installing this game, that's massively appreciated!", self.aa, self.FontCol)``
65.	``¬ ¬ ¬ ¬ Credits23Width = Credits23.get_width()``
66.	``¬ ¬ ¬ ¬ Credits24 = LargeCreditsFont.render("For full change-log please visit my aforementioned GitHub profile", self.aa, self.FontCol)``
67.	``¬ ¬ ¬ ¬ Credits24Width = Credits24.get_width()``
68.	``¬ ¬ ¬ ¬ Credits25 = LargeCreditsFont.render("Disclaimer:", self.aa, self.FontCol)``
69.	``¬ ¬ ¬ ¬ Credits25Width = Credits25.get_width()``
70.	``¬ ¬ ¬ ¬ Credits26 = VersionFont.render("The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your", self.aa, self.AccentCol)``
71.	``¬ ¬ ¬ ¬ Credits26Width = Credits26.get_width()``
72.	``¬ ¬ ¬ ¬ Credits27 = VersionFont.render("friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve", self.aa, self.AccentCol)``
73.	``¬ ¬ ¬ ¬ Credits27Width = Credits27.get_width()``
74.	``¬ ¬ ¬ ¬ Credits28 = VersionFont.render("my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo", self.aa, self.AccentCol)``
75.	``¬ ¬ ¬ ¬ Credits28Width = Credits28.get_width()``
76.	``¬ ¬ ¬ ¬ Credits29 = VersionFont.render("DOES NOT TAKE ANY RESPONSIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXTERNAL MODULES INSTALLED ONTO", self.aa, self.AccentCol)``
77.	``¬ ¬ ¬ ¬ Credits29Width = Credits29.get_width()``
78.	``¬ ¬ ¬ ¬ Credits30 = VersionFont.render("YOUR COMPUTER (WHEN NOT CHOOSING THE RECOMMENDED EXECUTABLE VERSION) ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM", self.aa, self.AccentCol)``
79.	``¬ ¬ ¬ ¬ Credits30Width = Credits30.get_width()``
80.	``¬ ¬ ¬ ¬ Credits31 = VersionFont.render("RESPONSIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVICES MANAGER OR ADMINISTRATOR TO INSTALL AND USE", self.aa, self.AccentCol)``
81.	``¬ ¬ ¬ ¬ Credits31Width = Credits31.get_width()``
82.	``¬ ¬ ¬ ¬ Credits32 = VersionFont.render("COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVICE, AND AT ANY POINT NO CONNECTION TO A", self.aa, self.AccentCol)``
83.	``¬ ¬ ¬ ¬ Credits32Width = Credits32.get_width()``
84.	``¬ ¬ ¬ ¬ Credits33 = VersionFont.render("NETWORK IS REQUIRED. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you.", self.aa, self.AccentCol)``
85.	``¬ ¬ ¬ ¬ Credits33Width = Credits33.get_width()``
86.	``¬ ¬ ¬ ¬ Credits34 = VersionFont.render("Thank You!", self.aa, self.FontCol)``
87.	``¬ ¬ ¬ ¬ Credits34Width = Credits34.get_width()``
88.	``¬ ¬ ¬ ¬ Credits34Height = Credits34.get_height()``

89.	``¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
90.	``¬ ¬ ¬ ¬ VisualYdisplacement = realHeight``
91.	``¬ ¬ ¬ ¬ IntroYDisplacement = (realHeight-TitleHeight)/2``
92.	``¬ ¬ ¬ ¬ timer = 5``
93.	``¬ ¬ ¬ ¬ tempFPS = self.FPS``

94.	``¬ ¬ ¬ ¬ EndClock = 0``
95.	``¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
96.	``¬ ¬ ¬ ¬ while True:``
97.	``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

98.	``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
99.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
100.	``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
101.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

102.	``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
103.	``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS ``
104.	``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``
105.	``¬ ¬ ¬ ¬ ¬ ``
106.	``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``

107.	``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get(): ``
108.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE): ``
109.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
110.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
111.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
112.	``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN: ``
113.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10: ``
114.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1 ``
115.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
116.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
117.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
118.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
119.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x: ``
120.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1 ``

121.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits and Change-Log")``
122.	``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
123.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits1, ((realWidth-Credits1Width)/2, 0+VisualYdisplacement))``
124.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits2, ((realWidth-Credits2Width)/2, 115+VisualYdisplacement))``
125.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits3, ((realWidth-Credits3Width)/2, (115*2)+VisualYdisplacement))``
126.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits4, ((realWidth-Credits4Width)/2, (115*3)+VisualYdisplacement))``
127.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits5, ((realWidth-Credits5Width)/2, (115*3)+20+VisualYdisplacement))``
128.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits6, ((realWidth-Credits6Width)/2, (115*3)+40+VisualYdisplacement))``
129.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits7, ((realWidth-Credits7Width)/2, (115*3)+60+VisualYdisplacement))``
130.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits8, ((realWidth-Credits8Width)/2, 540+VisualYdisplacement))``
131.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits9, ((realWidth-Credits9Width)/2, 540+20+VisualYdisplacement))``
132.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits10, ((realWidth-Credits10Width)/2, 540+40+VisualYdisplacement))``
133.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits11, ((realWidth-Credits11Width)/2, 540+60+VisualYdisplacement))``
134.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits12, ((realWidth-Credits12Width)/2, 540+80+VisualYdisplacement))``
135.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits13, ((realWidth-Credits13Width)/2, 540+100+VisualYdisplacement))``
136.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits14, ((realWidth-Credits14Width)/2, 540+120+VisualYdisplacement))``
137.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits15, ((realWidth-Credits15Width)/2, 540+140+VisualYdisplacement))``
138.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits16, ((realWidth-Credits16Width)/2, 540+160+VisualYdisplacement))``
139.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits17, ((realWidth-Credits17Width)/2, 540+180+VisualYdisplacement))``
140.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits18, ((realWidth-Credits18Width)/2, 540+200+VisualYdisplacement))``
141.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits19, ((realWidth-Credits19Width)/2, 540+220+VisualYdisplacement))``
142.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits20, ((realWidth-Credits20Width)/2, 540+240+VisualYdisplacement))``
143.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits21, ((realWidth-Credits21Width)/2, 540+260+VisualYdisplacement))``
144.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits22, ((realWidth-Credits22Width)/2, 915+VisualYdisplacement))``
145.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits23, ((realWidth-Credits23Width)/2, 935+VisualYdisplacement))``
146.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits24, ((realWidth-Credits24Width)/2, 1050+VisualYdisplacement))``
147.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits25, ((realWidth-Credits25Width)/2, 1165+VisualYdisplacement))``
148.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits26, ((realWidth-Credits26Width)/2, 1167+15+VisualYdisplacement))``
149.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits27, ((realWidth-Credits27Width)/2, 1167+30+VisualYdisplacement))``
150.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits28, ((realWidth-Credits28Width)/2, 1167+45+VisualYdisplacement))``
151.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits29, ((realWidth-Credits29Width)/2, 1167+60+VisualYdisplacement))``
152.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits30, ((realWidth-Credits30Width)/2, 1167+75+VisualYdisplacement))``
153.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits31, ((realWidth-Credits31Width)/2, 1167+90+VisualYdisplacement))``
154.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits32, ((realWidth-Credits32Width)/2, 1167+105+VisualYdisplacement))``
155.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits33, ((realWidth-Credits33Width)/2, 1167+120+VisualYdisplacement))``

156.	``¬ ¬ ¬ ¬ ¬ if timer >= 1:``
157.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))``
158.	``¬ ¬ ¬ ¬ ¬ ¬ timer -= 1/(self.aFPS/self.Iteration)``
159.	``¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement = realHeight``
160.	``¬ ¬ ¬ ¬ ¬ else:``
161.	``¬ ¬ ¬ ¬ ¬ ¬ if IntroYDisplacement <= 0:``
162.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, FullscreenX, 90)``
163.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
164.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
165.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50))``
166.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if int(1402+VisualYdisplacement) <= int(realHeight/2):``
167.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, (realHeight-Credits34Height)/2))``
168.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement -= 60/(self.aFPS/self.Iteration)``
169.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if EndClock >= 5:``
170.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
171.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
172.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ EndClock += 1/(self.aFPS/self.Iteration)``
173.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
174.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, 1402+VisualYdisplacement))``
175.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement -= 60/(self.aFPS/self.Iteration)``
176.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
177.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``
178.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
179.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))``
180.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50+IntroYDisplacement))``
181.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ IntroYDisplacement -= 90/(self.aFPS/self.Iteration)``
182.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement = realHeight``

183.	``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
184.	``¬ ¬ ¬ ¬ ¬ if not Message == None:``
185.	``¬ ¬ ¬ ¬ ¬ ¬ return Message``
186.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip() ``
187.	``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
188.	``¬ ¬ ¬ except Exception as Message:``
189.	``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    190.	``else:``
    191.	``¬ print("You need to run this as part of Pycraft")``
    192.	``¬ import tkinter as tk``
    193.	``¬ from tkinter import messagebox``
    194.	``¬ root = tk.Tk()``
    195.	``¬ root.withdraw()``
    196.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    197.	``¬ quit()``


DisplayUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_DisplayUtils>")``
    3.	``¬ class DisplayUtils:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def UpdateDisplay(self): # Run tests to make sure windows not too small``
7.	``¬ ¬ ¬ self.Data_aFPS = []``
8.	``¬ ¬ ¬ self.Data_CPUUsE = []``
9.	``¬ ¬ ¬ self.Data_eFPS = []``
10.	``¬ ¬ ¬ self.Data_MemUsE = []``
11.	``¬ ¬ ¬ self.Timer = 0``
12.	``¬ ¬ ¬ self.Data_aFPS_Min = 60``
13.	``¬ ¬ ¬ self.Data_aFPS_Max = 1``

14.	``¬ ¬ ¬ self.Data_CPUUsE_Min = 60``
15.	``¬ ¬ ¬ self.Data_CPUUsE_Max = 1``

16.	``¬ ¬ ¬ self.Data_eFPS_Min = 60``
17.	``¬ ¬ ¬ self.Data_eFPS_Max = 1``

18.	``¬ ¬ ¬ self.Data_MemUsE_Min = 50``
19.	``¬ ¬ ¬ self.Data_MemUsE_Max = 50``

20.	``¬ ¬ ¬ self.Data_CPUUsE_Min = 50``
21.	``¬ ¬ ¬ self.Data_CPUUsE_Max = 50``
22.	``¬ ¬ ¬ try:``
23.	``¬ ¬ ¬ ¬ try:``
24.	``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
25.	``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
26.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
27.	``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:``
28.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
29.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
30.	``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = True``
31.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.RESIZABLE)``
32.	``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:``
33.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
34.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
35.	``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = False``
36.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF)``
37.	``¬ ¬ ¬ ¬ except Exception as error:``
38.	``¬ ¬ ¬ ¬ ¬ self.Fullscreen = True``
39.	``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
40.	``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``
41.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
42.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
43.	``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight))``
44.	``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
45.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
46.	``¬ ¬ ¬ except Exception as Message:``
47.	``¬ ¬ ¬ ¬ return Message``
48.	``¬ ¬ ¬ else:``
49.	``¬ ¬ ¬ ¬ return None``


50.	``¬ ¬ def SetOPENGLdisplay(self):``
51.	``¬ ¬ ¬ try:``
52.	``¬ ¬ ¬ ¬ try:``
53.	``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
54.	``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
55.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
56.	``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == True:``
57.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
58.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
59.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
60.	``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == False:``
61.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
62.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
63.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
64.	``¬ ¬ ¬ ¬ except Exception as error:``
65.	``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
66.	``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``
67.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
68.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
69.	``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
70.	``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
71.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
72.	``¬ ¬ ¬ except Exception as Message:``
73.	``¬ ¬ ¬ ¬ return Message``
74.	``¬ ¬ ¬ else:``
75.	``¬ ¬ ¬ ¬ return None``
76.	``¬ ¬ ``
77.	``¬ ¬ ``
78.	``¬ ¬ def UpdateOPENGLdisplay(self):``
79.	``¬ ¬ ¬ try:``
80.	``¬ ¬ ¬ ¬ try:``
81.	``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
82.	``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
83.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
84.	``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:``
85.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
86.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
87.	``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = True``
88.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
89.	``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:``
90.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
91.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
92.	``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = False``
93.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
94.	``¬ ¬ ¬ ¬ except:``
95.	``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
96.	``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``
97.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
98.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
99.	``¬ ¬ ¬ ¬ ¬ self.Fullscreen = False``
100.	``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
101.	``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
102.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
103.	``¬ ¬ ¬ except Exception as Message:``
104.	``¬ ¬ ¬ ¬ return Message``
105.	``¬ ¬ ¬ else:``
106.	``¬ ¬ ¬ ¬ return None``


107.	``¬ ¬ def SetDisplay(self):``
108.	``¬ ¬ ¬ self.Data_aFPS = []``
109.	``¬ ¬ ¬ self.Data_CPUUsE = []``
110.	``¬ ¬ ¬ self.Data_eFPS = []``
111.	``¬ ¬ ¬ self.Data_MemUsE = []``
112.	``¬ ¬ ¬ self.Timer = 0``
113.	``¬ ¬ ¬ self.Data_aFPS_Min = 60``
114.	``¬ ¬ ¬ self.Data_aFPS_Max = 1``

115.	``¬ ¬ ¬ self.Data_CPUUsE_Min = 60``
116.	``¬ ¬ ¬ self.Data_CPUUsE_Max = 1``

117.	``¬ ¬ ¬ self.Data_eFPS_Min = 60``
118.	``¬ ¬ ¬ self.Data_eFPS_Max = 1``

119.	``¬ ¬ ¬ self.Data_MemUsE_Min = 50``
120.	``¬ ¬ ¬ self.Data_MemUsE_Max = 50``

121.	``¬ ¬ ¬ self.Data_CPUUsE_Min = 50``
122.	``¬ ¬ ¬ self.Data_CPUUsE_Max = 50``
123.	``¬ ¬ ¬ try:``
124.	``¬ ¬ ¬ ¬ try:``
125.	``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
126.	``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == True:``
127.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
128.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
129.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.RESIZABLE)``
130.	``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == False:``
131.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
132.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
133.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF)``
134.	``¬ ¬ ¬ ¬ except Exception as error:``
135.	``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
136.	``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``
137.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
138.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
139.	``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight))``
140.	``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
141.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
142.	``¬ ¬ ¬ except Exception as Message:``
143.	``¬ ¬ ¬ ¬ return Message``
144.	``¬ ¬ ¬ else:``
145.	``¬ ¬ ¬ ¬ return None``


146.	``¬ ¬ def GenerateMinDisplay(self, width, height):``
147.	``¬ ¬ ¬ try:``
148.	``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((width, height), self.mod_Pygame__.RESIZABLE)``
149.	``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
150.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
151.	``¬ ¬ ¬ except Exception as Message:``
152.	``¬ ¬ ¬ ¬ return Message``
153.	``¬ ¬ ¬ else:``
154.	``¬ ¬ ¬ ¬ return None``


155.	``¬ ¬ def GetDisplayLocation(self):``
156.	``¬ ¬ ¬ hwnd = self.mod_Pygame__.display.get_wm_info()["window"]``

157.	``¬ ¬ ¬ prototype = self.mod_Ctypes__.WINFUNCTYPE(self.mod_Ctypes__.wintypes.BOOL, self.mod_Ctypes__.wintypes.HWND, self.mod_Ctypes__.POINTER(self.mod_Ctypes__.wintypes.RECT))``
158.	``¬ ¬ ¬ paramflags = (1, "hwnd"), (2, "lprect")``

159.	``¬ ¬ ¬ GetWindowRect = prototype(("GetWindowRect", self.mod_Ctypes__.windll.user32), paramflags)``

160.	``¬ ¬ ¬ rect = GetWindowRect(hwnd)``

161.	``¬ ¬ ¬ return rect.left+8, rect.top+31``


162.	``¬ ¬ def GetPlayStatus(self):``
163.	``¬ ¬ ¬ if self.mod_Pygame__.display.get_active() == True:``
164.	``¬ ¬ ¬ ¬ tempFPS = self.FPS``
165.	``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).unpause()``
166.	``¬ ¬ ¬ ¬ if self.mod_Pygame__.mixer.Channel(2).get_busy() == 0 and self.LoadMusic == True:``
167.	``¬ ¬ ¬ ¬ ¬ if self.music == True and self.CurrentlyPlaying == None:``
168.	``¬ ¬ ¬ ¬ ¬ ¬ self.CurrentlyPlaying = "InvSound"``
169.	``¬ ¬ ¬ ¬ ¬ ¬ self.LoadMusic = False``
170.	``¬ ¬ ¬ ¬ ¬ ¬ MusicThread = self.mod_Threading__.Thread(target=self.mod_SoundUtils__.PlaySound.PlayInvSound, args=(self,))``
171.	``¬ ¬ ¬ ¬ ¬ ¬ MusicThread.start()``
172.	``¬ ¬ ¬ else:``
173.	``¬ ¬ ¬ ¬ self.LoadMusic = True``
174.	``¬ ¬ ¬ ¬ tempFPS = 15``
175.	``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).pause()``
176.	``¬ ¬ ¬ return tempFPS``
177.	``¬ ¬ ``

.. note::
    For information on this consult the above guide
    178.	``else:``
    179.	``¬ print("You need to run this as part of Pycraft")``
    180.	``¬ import tkinter as tk``
    181.	``¬ from tkinter import messagebox``
    182.	``¬ root = tk.Tk()``
    183.	``¬ root.withdraw()``
    184.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    185.	``¬ quit()``


DrawingUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_DrawingUtils>")``
    3.	``¬ class DrawRose:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def CreateRose(self, xScaleFact, yScaleFact, coloursARRAY):``
7.	``¬ ¬ ¬ if coloursARRAY == False:``
8.	``¬ ¬ ¬ ¬ coloursARRAY = []``
9.	``¬ ¬ ¬ ¬ for i in range(32):``
10.	``¬ ¬ ¬ ¬ ¬ coloursARRAY.append(self.ShapeCol)``

11.	``¬ ¬ ¬ defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] ``
12.	``¬ ¬ ¬ self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2)``
13.	``¬ ¬ ¬ ``
14.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[0], (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
15.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[1], (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
16.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[2], (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
17.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[3], (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
18.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[4], (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
19.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[5], (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
20.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[6], (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
21.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[7], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
22.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[8], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
23.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[9], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
24.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[10], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
25.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[11], (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) ``
26.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[12], (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
27.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[13], (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
28.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[14], (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
29.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[15], (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
30.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[16], (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
31.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[17], (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
32.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[18], (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) ``
33.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[19], (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
34.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[20], (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
35.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[21], (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
36.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[22], (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
37.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[23], (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
38.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[24], (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
39.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[25], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
40.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[25], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
41.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[27], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
42.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[28], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
43.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[29], (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
44.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[30], (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
45.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[31], (575*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

46.	``¬ class GenerateGraph:``
47.	``¬ ¬ def __init__(self):``
48.	``¬ ¬ ¬ pass``

49.	``¬ ¬ def CreateDevmodeGraph(self, DataFont):``
50.	``¬ ¬ ¬ if self.Devmode == 10:``
51.	``¬ ¬ ¬ ¬ try:``
52.	``¬ ¬ ¬ ¬ ¬ if ((self.realWidth/2)+100)+self.Timer >= self.realWidth:``
53.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS = []``
54.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE = []``
55.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS = []``
56.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE = []``
57.	``¬ ¬ ¬ ¬ ¬ ¬ self.Timer = 0``
58.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Min = 60``
59.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Max = 1``

60.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = 60``
61.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = 1``

62.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Min = 60``
63.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Max = 1``

64.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Min = 50``
65.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = 50``

66.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = 50``
67.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = 50``

68.	``¬ ¬ ¬ ¬ ¬ BackingRect = self.mod_Pygame__.Rect((self.realWidth/2)+100, 0, self.realWidth, 200)``
69.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, BackingRect)``

70.	``¬ ¬ ¬ ¬ ¬ if self.Timer >= 2:``
71.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_aFPS_Max)*(self.aFPS/(self.Iteration))])``
72.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_eFPS_Max)*int(self.eFPS)])``
73.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_MemUsE_Max)*(100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available])``

74.	``¬ ¬ ¬ ¬ ¬ if (self.aFPS/(self.Iteration)) > self.Data_aFPS_Max:``
75.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Max = (self.aFPS/(self.Iteration))``
76.	``¬ ¬ ¬ ¬ ¬ elif (self.aFPS/(self.Iteration)) < self.Data_aFPS_Min:``
77.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Min = (self.aFPS/(self.Iteration))``

78.	``¬ ¬ ¬ ¬ ¬ if self.eFPS > self.Data_eFPS_Max:``
79.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Max = self.eFPS``
80.	``¬ ¬ ¬ ¬ ¬ elif self.eFPS < self.Data_eFPS_Min:``
81.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Min = self.eFPS``

82.	``¬ ¬ ¬ ¬ ¬ if (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available > self.Data_MemUsE_Max:``
83.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available``
84.	``¬ ¬ ¬ ¬ ¬ elif (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available < self.Data_MemUsE_Max:``
85.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available``

86.	``¬ ¬ ¬ ¬ ¬ self.Timer += 0.2``
87.	``¬ ¬ ¬ ¬ ¬ if self.Timer >= 5:``
88.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 0), False, self.Data_aFPS)``
89.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 255, 0), False, self.Data_eFPS)``
90.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 0, 255), False, self.Data_MemUsE)``
91.	``¬ ¬ ¬ ¬ ¬ if len(self.Data_CPUUsE) >= 2:``
92.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 255), False, self.Data_CPUUsE)``
93.	``¬ ¬ ¬ ¬ ¬ runFont = DataFont.render(f"MemUsE: {self.mod_Psutil__.virtual_memory().percent}% | CPUUsE: {self.mod_Psutil__.cpu_percent()}% | FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: {int(self.aFPS/self.Iteration)} Iteration: {self.Iteration}", self.aa, (255, 255, 255)) ``
94.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(runFont, ((self.realWidth/2)+105, 0))``
95.	``¬ ¬ ¬ ¬ except Exception as Message:``
96.	``¬ ¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
97.	``¬ ¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    98.	``else:``
    99.	``¬ print("You need to run this as part of Pycraft")``
    100.	``¬ import tkinter as tk``
    101.	``¬ from tkinter import messagebox``
    102.	``¬ root = tk.Tk()``
    103.	``¬ root.withdraw()``
    104.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    105.	``¬ quit()``


ExBenchmark
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_ExBenchmark>")``
    3.	``¬ class LoadBenchmark:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def run(self):``
7.	``¬ ¬ ¬ try:``
8.	``¬ ¬ ¬ ¬ FPSlistX = []``
9.	``¬ ¬ ¬ ¬ FPSlistY = []``

10.	``¬ ¬ ¬ ¬ FPSlistX2 = []``
11.	``¬ ¬ ¬ ¬ FPSlistY2 = []``

12.	``¬ ¬ ¬ ¬ FPSlistX3 = []``
13.	``¬ ¬ ¬ ¬ FPSlistY3 = []``

14.	``¬ ¬ ¬ ¬ SetFPS = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 200, 250, 300, 350, 500]``

15.	``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((1280, 720))``

16.	``¬ ¬ ¬ ¬ iteration = 0``
17.	``¬ ¬ ¬ ¬ FPScounter = 0``
18.	``¬ ¬ ¬ ¬ MaxIteration = 500``

19.	``¬ ¬ ¬ ¬ while iteration < 7500:``
20.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running Blank Window Benchmark @ {SetFPS[FPScounter]} FPS")``
21.	``¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:``
22.	``¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:``
23.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX.append(iteration)``
24.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY.append(self.clock.get_fps())``
25.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
26.	``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
27.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
28.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``

29.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
30.	``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``
31.	``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])``
32.	``¬ ¬ ¬ ¬ ¬ FPScounter += 1``
33.	``¬ ¬ ¬ ¬ ¬ MaxIteration += 500``

34.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Preparing Animated Benchmark")``

35.	``¬ ¬ ¬ ¬ iteration = 0``
36.	``¬ ¬ ¬ ¬ FPScounter = 0``
37.	``¬ ¬ ¬ ¬ MaxIteration = 500``
38.	``¬ ¬ ¬ ¬ run = 0``
39.	``¬ ¬ ¬ ¬ y = 10``

40.	``¬ ¬ ¬ ¬ while not iteration == 60:``
41.	``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
42.	``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
43.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
44.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``

45.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
46.	``¬ ¬ ¬ ¬ ¬ iteration += 1``
47.	``¬ ¬ ¬ ¬ ¬ self.clock.tick(60)``

48.	``¬ ¬ ¬ ¬ ¬ ¬ ``
49.	``¬ ¬ ¬ ¬ iteration = 0``
50.	``¬ ¬ ¬ ¬ FPScounter = 0``
51.	``¬ ¬ ¬ ¬ MaxIteration = 500``

52.	``¬ ¬ ¬ ¬ while iteration < 7500:``
53.	``¬ ¬ ¬ ¬ ¬ run += 1``
54.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running Animated Window Benchmark @ {SetFPS[FPScounter]} FPS")``
55.	``¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:``
56.	``¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:``
57.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX2.append(iteration)``
58.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY2.append(self.clock.get_fps())``
59.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
60.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
61.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
62.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
63.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
64.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
65.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
66.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
67.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
68.	``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
69.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
70.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``

71.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
72.	``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``
73.	``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])``
74.	``¬ ¬ ¬ ¬ ¬ FPScounter += 1``
75.	``¬ ¬ ¬ ¬ ¬ MaxIteration += 500``

76.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Preparing OpenGL Benchmark")``

77.	``¬ ¬ ¬ ¬ iteration = 0``
78.	``¬ ¬ ¬ ¬ FPScounter = 0``
79.	``¬ ¬ ¬ ¬ MaxIteration = 500``
80.	``¬ ¬ ¬ ¬ run = 0``
81.	``¬ ¬ ¬ ¬ y = 10``

82.	``¬ ¬ ¬ ¬ while not iteration == 60:``
83.	``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
84.	``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
85.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
86.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``

87.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
88.	``¬ ¬ ¬ ¬ ¬ iteration += 1``
89.	``¬ ¬ ¬ ¬ ¬ self.clock.tick(60)``

90.	``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((1280, 720), self.mod_Pygame__.OPENGL|self.mod_Pygame__.DOUBLEBUF)``

91.	``¬ ¬ ¬ ¬ iteration = 0``
92.	``¬ ¬ ¬ ¬ FPScounter = 0``
93.	``¬ ¬ ¬ ¬ MaxIteration = 500``
94.	``¬ ¬ ¬ ¬ vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))``
95.	``¬ ¬ ¬ ¬ edges = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4), (6,7), (5,1), (5,4), (5,7))``

96.	``¬ ¬ ¬ ¬ self.mod_OGLbenchmark__.LoadOGLBenchmark.CreateBenchmark(self)``

97.	``¬ ¬ ¬ ¬ while iteration < 7500:``
98.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running OpenGL Benchmark @ {SetFPS[FPScounter]} FPS")``
99.	``¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:``
100.	``¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:``
101.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX3.append(iteration)``
102.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY3.append(self.clock.get_fps())``
103.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_OGLbenchmark__.LoadOGLBenchmark.RunBenchmark(self, edges, vertices)``
104.	``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
105.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
106.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``

107.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
108.	``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``
109.	``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])``
110.	``¬ ¬ ¬ ¬ ¬ FPScounter += 1``
111.	``¬ ¬ ¬ ¬ ¬ MaxIteration += 500``

112.	``¬ ¬ ¬ ¬ ¬ ``
113.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Finished Animated Benchmark")``
114.	``¬ ¬ ¬ ¬ self.mod_Time__.sleep(5)``
115.	``¬ ¬ ¬ except Exception as Message:``
116.	``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
117.	``¬ ¬ ¬ ¬ return Message, None, None, None, None``
118.	``¬ ¬ ¬ else:``

119.	``¬ ¬ ¬ ¬ return None, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3``

.. note::
    For information on this consult the above guide
    120.	``else:``
    121.	``¬ print("You need to run this as part of Pycraft")``
    122.	``¬ import tkinter as tk``
    123.	``¬ from tkinter import messagebox``
    124.	``¬ root = tk.Tk()``
    125.	``¬ root.withdraw()``
    126.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    127.	``¬ quit()``


GameEngine
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

1.	``if not __name__ == "__main__":``
2.	``¬ print("Started <Pycraft_GameEngine>")``
3.	``¬ ``
4.	``¬ from ShareDataUtil import Class_Startup_variables as SharedData``
5.	``¬ ``
6.	``¬ SharedData.mod_ModernGL_window_.setup_basic_logging(0)``
7.	``¬ ``
8.	``¬ ``
9.	``¬ class Cubemap(SharedData.mod_Base__.CameraWindow):``
10.	``¬ ¬ SharedData.mod_Base__.CameraWindow.title = f"Pycraft: v{SharedData.version}: Playing"``
11.	``¬ ¬ SharedData.mod_Base__.CameraWindow.resource_dir = SharedData.base_folder``
12.	``¬ ¬ ``
13.	``¬ ¬ ``
14.	``¬ ¬ def Exit(self, SharedData, Command):``
15.	``¬ ¬ ¬ try:``
16.	``¬ ¬ ¬ ¬ if SharedData.mod_Pygame__.mixer.Channel(3).get_busy() == True:``
17.	``¬ ¬ ¬ ¬ ¬ SharedData.mod_Pygame__.mixer.Channel(3).stop()``
18.	``¬ ¬ ¬ ¬ ¬ SharedData.mod_Pygame__.quit()``
19.	``¬ ¬ ¬ ¬ ¬ ``
20.	``¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = False``
21.	``¬ ¬ ¬ except Exception as Error:``
22.	``¬ ¬ ¬ ¬ print("GE", Error)``
23.	``¬ ¬ ¬ ¬ pass``
24.	``¬ ¬ ¬ self.wnd._set_fullscreen(False)``
25.	``¬ ¬ ¬ self.wnd.close()``
26.	``¬ ¬ ¬ self.wnd.destroy()``
27.	``¬ ¬ ¬ SharedData.CurrentlyPlaying = None``
28.	``¬ ¬ ¬ SharedData.LoadMusic = True``
29.	``¬ ¬ ¬ SharedData.Command = Command``
30.	``¬ ¬ ¬ if self.wnd.fullscreen == True:``
31.	``¬ ¬ ¬ ¬ SharedData.Fullscreen = False``
32.	``¬ ¬ ¬ else:``
33.	``¬ ¬ ¬ ¬ SharedData.Fullscreen = True``


34.	``¬ ¬ def __init__(self, **kwargs):``
35.	``¬ ¬ ¬ try:``
36.	``¬ ¬ ¬ ¬ super().__init__(**kwargs)``
37.	``¬ ¬ ¬ ``
38.	``¬ ¬ ¬ ¬ self.size = self.wnd.buffer_size``
39.	``¬ ¬ ¬ ¬ ¬ ¬ ``
40.	``¬ ¬ ¬ ¬ WindowSize = SharedData.realWidth, SharedData.realHeight``
41.	``¬ ¬ ¬ ¬ CurrentWindowSize = WindowSize``
42.	``¬ ¬ ¬ ¬ ``
43.	``¬ ¬ ¬ ¬ self.wnd.size = WindowSize``
44.	``¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = False``
45.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
46.	``¬ ¬ ¬ ¬ self.camera.projection.update(near=0.1, far=100.0)``
47.	``¬ ¬ ¬ ¬ self.camera.zoom = 2.5``
48.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
49.	``¬ ¬ ¬ ¬ self.obj = self.load_scene(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\Map\\map.obj")))``
50.	``¬ ¬ ¬ ``
51.	``¬ ¬ ¬ ¬ self.cube = SharedData.mod_ModernGL_window_.geometry.cube(size=(20, 20, 20))``
52.	``¬ ¬ ¬ ¬ ``
53.	``¬ ¬ ¬ ¬ self.prog = self.load_program(SharedData.mod_OS__.path.join(SharedData.base_folder, ("programs//cubemap.glsl")))``

54.	``¬ ¬ ¬ ¬ self.SkyBox_texture = self.load_texture_cube(``
55.	``¬ ¬ ¬ ¬ ¬ neg_x=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg")),``
56.	``¬ ¬ ¬ ¬ ¬ neg_y=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg")),``
57.	``¬ ¬ ¬ ¬ ¬ neg_z=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg")),``
58.	``¬ ¬ ¬ ¬ ¬ pos_x=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg")),``
59.	``¬ ¬ ¬ ¬ ¬ pos_y=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg")),``
60.	``¬ ¬ ¬ ¬ ¬ pos_z=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg")),``
61.	``¬ ¬ ¬ ¬ ¬ flip_x=True,``
62.	``¬ ¬ ¬ ¬ )``
63.	``¬ ¬ ¬ ¬ ¬ ``
64.	``¬ ¬ ¬ ¬ Prev_Mouse_Pos = (0,0)``
65.	``¬ ¬ ¬ ¬ Mouse_Pos = (0,0)``
66.	``¬ ¬ ¬ ¬ DeltaX, DeltaY = 0, 0``
67.	``¬ ¬ ¬ ¬ ``
68.	``¬ ¬ ¬ ¬ self.wnd.exit_key = None``
69.	``¬ ¬ ¬ ¬ ``
70.	``¬ ¬ ¬ ¬ MouseUnlock = True``
71.	``¬ ¬ ¬ ¬ ``
72.	``¬ ¬ ¬ ¬ Jump = False``
73.	``¬ ¬ ¬ ¬ JumpID = 0``
74.	``¬ ¬ ¬ ¬ ``
75.	``¬ ¬ ¬ ¬ self.camera.position.y += 0.7``
76.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
77.	``¬ ¬ ¬ ¬ WkeydownTimer = 0``
78.	``¬ ¬ ¬ ¬ AkeydownTimer = 0``
79.	``¬ ¬ ¬ ¬ SkeydownTimer = 0``
80.	``¬ ¬ ¬ ¬ DkeydownTimer = 0``
81.	``¬ ¬ ¬ ¬ ``
82.	``¬ ¬ ¬ ¬ RunForwardTimer = 0``
83.	``¬ ¬ ¬ ¬ ``
84.	``¬ ¬ ¬ ¬ FPS = 0``
85.	``¬ ¬ ¬ ¬ ``
86.	``¬ ¬ ¬ ¬ Iteration = 0``
87.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
88.	``¬ ¬ ¬ ¬ while True:``
89.	``¬ ¬ ¬ ¬ ¬ try:``
90.	``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.mod_Pygame__.mixer.get_busy() == False:``
91.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayAmbientSound(SharedData)``
92.	``¬ ¬ ¬ ¬ ¬ except Exception as Error:``
93.	``¬ ¬ ¬ ¬ ¬ ¬ print(Error)``
94.	``¬ ¬ ¬ ¬ ¬ ¬ pass``
95.	``¬ ¬ ¬ ¬ ¬ ¬ ``
96.	``¬ ¬ ¬ ¬ ¬ if Iteration == 0:``
97.	``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.Fullscreen == False:``
98.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.fullscreen = True``
99.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
100.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.fixed_aspect_ratio = SharedData.realWidth / SharedData.realHeight``
101.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.window_size = SharedData.realWidth, SharedData.realHeight``
102.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ CurrentWindowSize = self.window_size``
103.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.position = (int((SharedData.FullscreenX-CurrentWindowSize[0])/2), int((SharedData.FullscreenY-CurrentWindowSize[1])/2))``
104.	``¬ ¬ ¬ ¬ ¬ ``
105.	``¬ ¬ ¬ ¬ ¬ if Iteration >= 5000:``
106.	``¬ ¬ ¬ ¬ ¬ ¬ Iteration = 0``
107.	``¬ ¬ ¬ ¬ ¬ ¬ ``
108.	``¬ ¬ ¬ ¬ ¬ start = SharedData.mod_Time__.perf_counter()``
109.	``¬ ¬ ¬ ¬ ¬ ``
110.	``¬ ¬ ¬ ¬ ¬ self.ctx.clear(1.0, 1.0, 1.0)``
111.	``¬ ¬ ¬ ¬ ¬ ``
112.	``¬ ¬ ¬ ¬ ¬ CurrentWindowSize = self.window_size``

113.	``¬ ¬ ¬ ¬ ¬ Prev_Mouse_Pos = Mouse_Pos ``
114.	``¬ ¬ ¬ ¬ ¬ Mouse_Pos = SharedData.mod_Pyautogui__.position()``
115.	``¬ ¬ ¬ ¬ ¬ DeltaX, DeltaY = Mouse_Pos[0]-Prev_Mouse_Pos[0], Mouse_Pos[1]-Prev_Mouse_Pos[1]``
116.	``¬ ¬ ¬ ¬ ¬ ``
117.	``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.ESCAPE):``
118.	``¬ ¬ ¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "Undefined")``
119.	``¬ ¬ ¬ ¬ ¬ ¬ return None``
120.	``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.W):``
121.	``¬ ¬ ¬ ¬ ¬ ¬ RunForwardTimer += (1/FPS)``
122.	``¬ ¬ ¬ ¬ ¬ ¬ if RunForwardTimer <= 10:``
123.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True: ``
124.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer += (1/FPS)``
125.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if WkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``
126.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
127.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer = 0``
128.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.x += 1.42``
129.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
130.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``
131.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer += (1/FPS)``
132.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if WkeydownTimer >= (SharedData.mod_Random__.randint(25, 75)/100):``
133.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
134.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer = 0``
135.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.x += 2.2352``
136.	``¬ ¬ ¬ ¬ ¬ else:``
137.	``¬ ¬ ¬ ¬ ¬ ¬ RunForwardTimer = 0``
138.	``¬ ¬ ¬ ¬ ¬ ¬ ``
139.	``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.A):``
140.	``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True: ``
141.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ AkeydownTimer += (1/FPS)``
142.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if AkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``
143.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
144.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AkeydownTimer = 0``
145.	``¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.z += 1.42``
146.	``¬ ¬ ¬ ¬ ¬ ¬ ``
147.	``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.S):``
148.	``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True: ``
149.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ SkeydownTimer += (1/FPS)``
150.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if SkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``
151.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
152.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SkeydownTimer = 0``
153.	``¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.x -= 1.42``
154.	``¬ ¬ ¬ ¬ ¬ ¬ ``
155.	``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.D):``
156.	``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True: ``
157.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ DkeydownTimer += (1/FPS)``
158.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if DkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``
159.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
160.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ DkeydownTimer = 0``
161.	``¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.z -= 1.42``
162.	``¬ ¬ ¬ ¬ ¬ ¬ ``
163.	``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.E):``
164.	``¬ ¬ ¬ ¬ ¬ ¬ if self.wnd._fullscreen == True:``
165.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot = SharedData.mod_Pyautogui__.screenshot(region=((0, 0, SharedData.FullscreenX, SharedData.FullscreenY)))``
166.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot.save(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))``
167.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
168.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ PosX, PosY = self.wnd.position``
169.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot = SharedData.mod_Pyautogui__.screenshot(region=((PosX, PosY, SharedData.realWidth, SharedData.realHeight)))``
170.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot.save(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))``
171.	``¬ ¬ ¬ ¬ ¬ ¬ ``
172.	``¬ ¬ ¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "Inventory")``
173.	``¬ ¬ ¬ ¬ ¬ ¬ return None``
174.	``¬ ¬ ¬ ¬ ¬ ``
175.	``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.R):``
176.	``¬ ¬ ¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "MapGUI")``
177.	``¬ ¬ ¬ ¬ ¬ ¬ return None``
178.	``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.L):``
179.	``¬ ¬ ¬ ¬ ¬ ¬ if MouseUnlock == True:``
180.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ MouseUnlock = False``
181.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
182.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ MouseUnlock = True``
183.	``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.SPACE):``
184.	``¬ ¬ ¬ ¬ ¬ ¬ Jump = True``
185.	``¬ ¬ ¬ ¬ ¬ ¬ JumpUP = True``
186.	``¬ ¬ ¬ ¬ ¬ ¬ ``
187.	``¬ ¬ ¬ ¬ ¬ if Jump == True:``
188.	``¬ ¬ ¬ ¬ ¬ ¬ if JumpID < 10 and JumpUP == True:``
189.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpID += 1``
190.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.y += 0.1``
191.	``¬ ¬ ¬ ¬ ¬ ¬ if JumpID == 10:``
192.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpUP = False``
193.	``¬ ¬ ¬ ¬ ¬ ¬ if JumpID >= 0 and JumpUP == False:``
194.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpID -= 1``
195.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.y -= 0.1``
196.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if JumpID == 0:``
197.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``
198.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
199.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Jump = False``
200.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpID = 0``
201.	``¬ ¬ ¬ ¬ ¬ ``
202.	``¬ ¬ ¬ ¬ ¬ self.ctx.enable(SharedData.mod_ModernGL__.CULL_FACE | SharedData.mod_ModernGL__.DEPTH_TEST)``

203.	``¬ ¬ ¬ ¬ ¬ cam = self.camera.matrix``
204.	``¬ ¬ ¬ ¬ ¬ cam[3][0] = 0``
205.	``¬ ¬ ¬ ¬ ¬ cam[3][1] = 0``
206.	``¬ ¬ ¬ ¬ ¬ cam[3][2] = 0``

207.	``¬ ¬ ¬ ¬ ¬ self.SkyBox_texture.use(location=0)``
208.	``¬ ¬ ¬ ¬ ¬ self.prog['m_proj'].write(self.camera.projection.matrix)``
209.	``¬ ¬ ¬ ¬ ¬ self.prog['m_camera'].write(cam)``
210.	``¬ ¬ ¬ ¬ ¬ ``
211.	``¬ ¬ ¬ ¬ ¬ try:``
212.	``¬ ¬ ¬ ¬ ¬ ¬ if MouseUnlock == True:¬ ¬ ¬ ¬ ¬ ¬ ``
213.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.rot_state(-DeltaX, -DeltaY)``
214.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = True``
215.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
216.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = False``
217.	``¬ ¬ ¬ ¬ ¬ except Exception as Error:``
218.	``¬ ¬ ¬ ¬ ¬ ¬ print(Error)``
219.	``¬ ¬ ¬ ¬ ¬ ¬ pass``
220.	``¬ ¬ ¬ ¬ ¬ ``
221.	``¬ ¬ ¬ ¬ ¬ self.ctx.front_face = 'cw'``
222.	``¬ ¬ ¬ ¬ ¬ self.cube.render(self.prog)``
223.	``¬ ¬ ¬ ¬ ¬ ``
224.	``¬ ¬ ¬ ¬ ¬ self.ctx.front_face = 'ccw'``
225.	``¬ ¬ ¬ ¬ ¬ self.obj.draw(projection_matrix=self.camera.projection.matrix, camera_matrix=self.camera.matrix)``
226.	``¬ ¬ ¬ ¬ ¬ ``
227.	``¬ ¬ ¬ ¬ ¬ try:``
228.	``¬ ¬ ¬ ¬ ¬ ¬ self.wnd.swap_buffers()``
229.	``¬ ¬ ¬ ¬ ¬ except Exception as Error:``
230.	``¬ ¬ ¬ ¬ ¬ ¬ print(Error)``
231.	``¬ ¬ ¬ ¬ ¬ ¬ pass``
232.	``¬ ¬ ¬ ¬ ¬ ``
233.	``¬ ¬ ¬ ¬ ¬ FPS = 1/(SharedData.mod_Time__.perf_counter()-start)``
234.	``¬ ¬ ¬ ¬ ¬ Iteration += 1``
235.	``¬ ¬ ¬ except Exception as Message:``
236.	``¬ ¬ ¬ ¬ print(''.join(SharedData.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
237.	``¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "Undefined")``
238.	``¬ ¬ ¬ ¬ SharedData.GameError = str(Message)``
239.	``¬ ¬ ¬ ¬ return None``
240.	``¬ ¬ ¬ ¬ ``
241.	``¬ ¬ ¬ ¬ ``
242.	``¬ ¬ ¬ ¬ ``
243.	``¬ class CreateEngine:``
244.	``¬ ¬ ``
245.	``¬ ¬ ``
246.	``¬ ¬ def __init__(self):``
247.	``¬ ¬ ¬ pass``
248.	``¬ ¬ ``
249.	``¬ ¬ ``
250.	``¬ ¬ def GenerateLoadDisplay(self, LoadingFont, text, MainTitleFont, SecondaryFont, LoadingTextFont):``
251.	``¬ ¬ ¬ try:``
252.	``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

253.	``¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``

254.	``¬ ¬ ¬ ¬ PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
255.	``¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``
256.	``¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))``

257.	``¬ ¬ ¬ ¬ LoadingTitle = SecondaryFont.render("Loading", self.aa, self.SecondFontCol)``
258.	``¬ ¬ ¬ ¬ self.Display.blit(LoadingTitle, (((self.realWidth-TitleWidth)/2)+55, 50))``

259.	``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (self.ShapeCol), self.aa, [(100, self.realHeight-100), (self.realWidth-100, self.realHeight-100)], 3)``
260.	``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (self.AccentCol), self.aa, self.Progress_Line)``

261.	``¬ ¬ ¬ ¬ DisplayMessage = LoadingFont.render(self.ProgressMessageText, self.aa, self.FontCol)``
262.	``¬ ¬ ¬ ¬ DisplayMessageWidth = DisplayMessage.get_width()``
263.	``¬ ¬ ¬ ¬ self.Display.blit(DisplayMessage, ((self.realWidth-DisplayMessageWidth)/2, self.realHeight-120))``

264.	``¬ ¬ ¬ ¬ TextFontRendered = LoadingTextFont.render(f"{text}", self.aa, self.FontCol)``
265.	``¬ ¬ ¬ ¬ TextFontRenderedWidth = TextFontRendered.get_width()``
266.	``¬ ¬ ¬ ¬ self.Display.blit(TextFontRendered, ((self.realWidth-TextFontRenderedWidth)/2, self.realHeight-100))``
267.	``¬ ¬ ¬ except Exception as error:``
268.	``¬ ¬ ¬ ¬ print(error)``

269.	``¬ ¬ def Play(self):``
270.	``¬ ¬ ¬ try:``
271.	``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).fadeout(2000)``
272.	``¬ ¬ ¬ ¬ ``
273.	``¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_WAIT)``

274.	``¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
275.	``¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
276.	``¬ ¬ ¬ ¬ self.mod_Globals__.Share.initialize(self)``
277.	``¬ ¬ ¬ ¬ try:``
278.	``¬ ¬ ¬ ¬ ¬ self.mod_ModernGL_window_.run_window_config(Cubemap)``
279.	``¬ ¬ ¬ ¬ except Exception as Error:``
280.	``¬ ¬ ¬ ¬ ¬ print(Error)``
281.	``¬ ¬ ¬ ¬ ¬ pass``
282.	``¬ ¬ ¬ ¬ return None``
283.	``¬ ¬ ¬ except Exception as Message:``
284.	``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
285.	``¬ ¬ ¬ ¬ return Message, "Undefined"``
286.	``¬ ¬ ¬ ``
287.	``¬ ¬ ¬ ``

.. note::
    For information on this consult the above guide
    288.	``else:``
    289.	``¬ print("You need to run this as part of Pycraft")``
    290.	``¬ import tkinter as tk``
    291.	``¬ from tkinter import messagebox``
    292.	``¬ root = tk.Tk()``
    293.	``¬ root.withdraw()``
    294.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    295.	``¬ quit()``


GetSavedData
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_GetSavedData>")``
    3.	``¬ class LoadSaveFiles:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``
6.	``¬ ¬ ¬ ¬ ¬ ¬ ``
7.	``¬ ¬ def ReadMainSave(self):``
8.	``¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'r') as openfile:``
9.	``¬ ¬ ¬ ¬ save = self.mod_JSON__.load(openfile)``
10.	``¬ ¬ ``
11.	``¬ ¬ ¬ self.theme = save["theme"]``
12.	``¬ ¬ ¬ self.RunFullStartup = save["startup"]``
13.	``¬ ¬ ¬ self.crash = save["crash"]``
14.	``¬ ¬ ¬ self.Fullscreen = save["WindowStatus"]``
15.	``¬ ¬ ¬ self.RecommendedFPS = save["AdaptiveFPS"]``
16.	``¬ ¬ ¬ self.Devmode = save["Devmode"]``
17.	``¬ ¬ ¬ self.SettingsPreference = save["profile"]``
18.	``¬ ¬ ¬ self.FPS = save["FPS"]``
19.	``¬ ¬ ¬ self.aFPS = save["aFPS"]``
20.	``¬ ¬ ¬ self.Iteration = save["Iteration"]``
21.	``¬ ¬ ¬ self.FOV = save["FOV"]``
22.	``¬ ¬ ¬ self.cameraANGspeed = save["cameraANGspeed"]``
23.	``¬ ¬ ¬ self.RenderFOG = save["RenderFOG"]``
24.	``¬ ¬ ¬ self.aa = save["aa"]``
25.	``¬ ¬ ¬ self.X = save["X"]``
26.	``¬ ¬ ¬ self.Y = save["Y"]``
27.	``¬ ¬ ¬ self.Z = save["Z"]``
28.	``¬ ¬ ¬ self.FanSky = save["FanSky"]``
29.	``¬ ¬ ¬ self.FanPart = save["FanPart"]``
30.	``¬ ¬ ¬ self.sound = save["sound"]``
31.	``¬ ¬ ¬ self.soundVOL = save["soundVOL"]``
32.	``¬ ¬ ¬ self.music = save["music"]``
33.	``¬ ¬ ¬ self.musicVOL = save["musicVOL"]``
34.	``¬ ¬ ¬ self.lastRun = save["lastRun"]``
35.	``¬ ¬ ¬ self.SavedWidth = save["DisplayWidth"]``
36.	``¬ ¬ ¬ self.SavedHeight = save["DisplayHeight"]``
37.	``¬ ¬ ¬ self.Total_Vertices = save["Total_Vertices"]``
38.	``¬ ¬ ¬ if self.Total_Vertices == 0:``
39.	``¬ ¬ ¬ ¬ self.Total_Vertices = 1``

40.	``¬ ¬ def RepairLostSave(self):``
41.	``¬ ¬ ¬ try:``
42.	``¬ ¬ ¬ ¬ SavedData = {"Total_Vertices":0, "theme":False, "profile":"Medium", "Devmode":0, "AdaptiveFPS": 60, "FPS":60, "aFPS":60, "Iteration":1, "FOV":75, "cameraANGspeed":3, "aa":True, "RenderFOG":True, "FanSky":True, "FanPart":True, "sound":True, "soundVOL":75, "music":True, "musicVOL":50, "X":0, "Y":0, "Z":0, "lastRun":"29/09/2021", 'startup':True, 'crash': False, 'DisplayWidth':1280, 'DisplayHeight':720, 'WindowStatus':True}``
43.	``¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'w') as openfile:``
44.	``¬ ¬ ¬ ¬ ¬ self.mod_JSON__.dump(SavedData, openfile)``
45.	``¬ ¬ ¬ except Exception as Message:``
46.	``¬ ¬ ¬ ¬ return Message``
47.	``¬ ¬ ¬ else:``
48.	``¬ ¬ ¬ ¬ return None``

49.	``¬ ¬ def SaveTOconfigFILE(self):``
50.	``¬ ¬ ¬ try:``
51.	``¬ ¬ ¬ ¬ current_time = self.mod_Datetime__.datetime.now()``
52.	``¬ ¬ ¬ ¬ currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"``
53.	``¬ ¬ ¬ ¬ SavedData = {"Total_Vertices":self.Total_Vertices, "theme":self.theme, "profile":self.SettingsPreference, "Devmode":self.Devmode, "AdaptiveFPS": self.RecommendedFPS, "FPS":self.FPS, "aFPS":self.aFPS, "Iteration":self.Iteration, "FOV":self.FOV, "cameraANGspeed":self.cameraANGspeed, "aa":self.aa, "RenderFOG":self.RenderFOG, "FanSky":self.FanSky, "FanPart":self.FanPart, "sound":self.sound, "soundVOL":self.soundVOL, "music":self.music, "musicVOL":self.musicVOL, "X":self.X, "Y":self.Y, "Z":self.Z, "lastRun":currentDate, 'startup':self.RunFullStartup, 'crash': False, 'DisplayWidth':self.SavedWidth, 'DisplayHeight':self.SavedHeight, 'WindowStatus':self.Fullscreen}``
54.	``¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'w') as openfile:``
55.	``¬ ¬ ¬ ¬ ¬ self.mod_JSON__.dump(SavedData, openfile)``
56.	``¬ ¬ ¬ except Exception as Message:``
57.	``¬ ¬ ¬ ¬ return Message``
58.	``¬ ¬ ¬ else:``
59.	``¬ ¬ ¬ ¬ return None``

.. note::
    For information on this consult the above guide
    60.	``else:``
    61.	``¬ print("You need to run this as part of Pycraft")``
    62.	``¬ import tkinter as tk``
    63.	``¬ from tkinter import messagebox``
    64.	``¬ root = tk.Tk()``
    65.	``¬ root.withdraw()``
    66.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    67.	``¬ quit()``


HomeScreen
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_HomeScreen>")``
    3.	``¬ class GenerateHomeScreen:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``
6.	``¬ ¬ ``
7.	``¬ ¬ def DisplayMessage(self, MessageFont, Message, Colour):``
8.	``¬ ¬ ¬ MessageText = MessageFont.render(Message, self.aa, Colour)``
9.	``¬ ¬ ¬ MessageTextWidth = MessageText.get_width()``
10.	``¬ ¬ ¬ MessageTextHeight = MessageText.get_height()``
11.	``¬ ¬ ¬ self.Display.blit(MessageText, ((self.realWidth-MessageTextWidth)/2, (self.realHeight-MessageTextHeight)))``
12.	``¬ ¬ ¬ ``

13.	``¬ ¬ def Home_Screen(self):``
14.	``¬ ¬ ¬ try:``
15.	``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
16.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
17.	``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Home screen")``
18.	``¬ ¬ ¬ ¬ Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()``
19.	``¬ ¬ ¬ ¬ SelectorWidth = Selector.get_width()``
20.	``¬ ¬ ¬ ¬ hover1 = False``
21.	``¬ ¬ ¬ ¬ hover2 = False``
22.	``¬ ¬ ¬ ¬ hover3 = False``
23.	``¬ ¬ ¬ ¬ hover4 = False``
24.	``¬ ¬ ¬ ¬ hover5 = False``
25.	``¬ ¬ ¬ ¬ hover6 = False``
26.	``¬ ¬ ¬ ¬ mousebuttondown = False``
27.	``¬ ¬ ¬ ¬ ``
28.	``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) ``
29.	``¬ ¬ ¬ ¬ PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
30.	``¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``
31.	``¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
32.	``¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))``
33.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

34.	``¬ ¬ ¬ ¬ SideFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20) ``
35.	``¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20) ``
36.	``¬ ¬ ¬ ¬ ButtonFont1 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
37.	``¬ ¬ ¬ ¬ ButtonFont2 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
38.	``¬ ¬ ¬ ¬ ButtonFont3 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
39.	``¬ ¬ ¬ ¬ ButtonFont4 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
40.	``¬ ¬ ¬ ¬ ButtonFont5 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
41.	``¬ ¬ ¬ ¬ ButtonFont6 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
42.	``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
43.	``¬ ¬ ¬ ¬ MessageFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``

44.	``¬ ¬ ¬ ¬ oldTHEME = self.theme``
45.	``¬ ¬ ¬ ¬ tempFPS = self.FPS``
46.	``¬ ¬ ¬ ¬ coloursARRAY = []``

47.	``¬ ¬ ¬ ¬ anim = False``

48.	``¬ ¬ ¬ ¬ special = [30, 30, 30]``
49.	``¬ ¬ ¬ ¬ TargetARRAY = []``

50.	``¬ ¬ ¬ ¬ ColourDisplacement = 80``

51.	``¬ ¬ ¬ ¬ increment = False``
52.	``¬ ¬ ¬ ¬ while True:``
53.	``¬ ¬ ¬ ¬ ¬ coloursARRAY = []``
54.	``¬ ¬ ¬ ¬ ¬ if anim == True:``
55.	``¬ ¬ ¬ ¬ ¬ ¬ anim = False``
56.	``¬ ¬ ¬ ¬ ¬ ¬ TargetARRAY = []``
57.	``¬ ¬ ¬ ¬ ¬ ¬ for a in range(self.mod_Random__.randint(0, 32)):``
58.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ TargetARRAY.append(a)``
59.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
60.	``¬ ¬ ¬ ¬ ¬ if len(TargetARRAY) == 0:``
61.	``¬ ¬ ¬ ¬ ¬ ¬ TargetARRAY = [33]``
62.	``¬ ¬ ¬ ¬ ¬ for i in range(32):``
63.	``¬ ¬ ¬ ¬ ¬ ¬ for j in range(len(TargetARRAY)):``
64.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if i == TargetARRAY[j]:``
65.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ coloursARRAY.append(special)``
66.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
67.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ coloursARRAY.append(self.ShapeCol)``

68.	``¬ ¬ ¬ ¬ ¬ if increment == False:``
69.	``¬ ¬ ¬ ¬ ¬ ¬ if self.aFPS == 0 or self.Iteration == 0:``
70.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement -= (self.mod_Random__.randint(0,10)/((self.FPS)/4))``
71.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
72.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement -= (self.mod_Random__.randint(0,10)/((self.aFPS/self.Iteration)/4))``
73.	``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = ColourDisplacement, ColourDisplacement, ColourDisplacement``
74.	``¬ ¬ ¬ ¬ ¬ if increment == True:``
75.	``¬ ¬ ¬ ¬ ¬ ¬ if self.aFPS == 0 or self.Iteration == 0:``
76.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement += (self.mod_Random__.randint(0,10)/((self.FPS)/4))``
77.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
78.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement += (self.mod_Random__.randint(0,10)/((self.aFPS/self.Iteration)/4))``
79.	``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = ColourDisplacement, ColourDisplacement, ColourDisplacement``
80.	``¬ ¬ ¬ ¬ ¬ if special[0] <= 30:``
81.	``¬ ¬ ¬ ¬ ¬ ¬ increment = True``
82.	``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = 30, 30, 30``
83.	``¬ ¬ ¬ ¬ ¬ if special[0] >= 80:``
84.	``¬ ¬ ¬ ¬ ¬ ¬ increment = False``
85.	``¬ ¬ ¬ ¬ ¬ ¬ anim = True``
86.	``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = 80, 80, 80``

87.	``¬ ¬ ¬ ¬ ¬ if self.mod_Pygame__.mixer.Channel(3).get_busy() == 1:``
88.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(3).stop()``

89.	``¬ ¬ ¬ ¬ ¬ if str(self.Display) == "<Surface(Dead Display)>":``
90.	``¬ ¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:``
91.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``
92.	``¬ ¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:``
93.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``

94.	``¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
95.	``¬ ¬ ¬ ¬ ¬ if not (self.realWidth == self.FullscreenX and self.realHeight == self.FullscreenY):``
96.	``¬ ¬ ¬ ¬ ¬ ¬ self.SavedWidth, self.SavedHeight = self.mod_Pygame__.display.get_window_size()``

97.	``¬ ¬ ¬ ¬ ¬ if self.SavedWidth == self.FullscreenX:``
98.	``¬ ¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
99.	``¬ ¬ ¬ ¬ ¬ if self.SavedHeight == self.FullscreenY:``
100.	``¬ ¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``

101.	``¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
102.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
103.	``¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
104.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

105.	``¬ ¬ ¬ ¬ ¬ yScaleFact = self.realHeight/720``
106.	``¬ ¬ ¬ ¬ ¬ xScaleFact = self.realWidth/1280``
107.	``¬ ¬ ¬ ¬ ¬ ``
108.	``¬ ¬ ¬ ¬ ¬ if not oldTHEME == self.theme:``
109.	``¬ ¬ ¬ ¬ ¬ ¬ Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()``
110.	``¬ ¬ ¬ ¬ ¬ ¬ SelectorWidth = Selector.get_width()``
111.	``¬ ¬ ¬ ¬ ¬ ¬ oldTHEME = self.theme``

112.	``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``
113.	``¬ ¬ ¬ ¬ ¬ ¬ ``
114.	``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
115.	``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
116.	``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``
117.	``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``
118.	``¬ ¬ ¬ ¬ ¬ Mx, My = self.mod_Pygame__.mouse.get_pos() ``
119.	``¬ ¬ ¬ ¬ ¬ PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
120.	``¬ ¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``

121.	``¬ ¬ ¬ ¬ ¬ Name = SideFont.render("By Tom Jebbo", self.aa, self.FontCol)``
122.	``¬ ¬ ¬ ¬ ¬ NameHeight = Name.get_height()``

123.	``¬ ¬ ¬ ¬ ¬ Version = VersionFont.render(f"Version: {self.version}", self.aa, self.FontCol) ``
124.	``¬ ¬ ¬ ¬ ¬ VersionWidth = Version.get_width()``
125.	``¬ ¬ ¬ ¬ ¬ VersionHeight = Version.get_height()``

126.	``¬ ¬ ¬ ¬ ¬ Play = ButtonFont1.render("Play", self.aa, self.FontCol)``
127.	``¬ ¬ ¬ ¬ ¬ PlayWidth = Play.get_width()``

128.	``¬ ¬ ¬ ¬ ¬ SettingsText = ButtonFont2.render("Settings", self.aa, self.FontCol)``
129.	``¬ ¬ ¬ ¬ ¬ SettingsWidth = SettingsText.get_width()``

130.	``¬ ¬ ¬ ¬ ¬ Character_DesignerText = ButtonFont3.render("Character Designer", self.aa, self.FontCol)``
131.	``¬ ¬ ¬ ¬ ¬ CharDesignerWidth = Character_DesignerText.get_width()``

132.	``¬ ¬ ¬ ¬ ¬ AchievementsText = ButtonFont4.render("Achievements", self.aa, self.FontCol)``
133.	``¬ ¬ ¬ ¬ ¬ AchievementsWidth = AchievementsText.get_width()``

134.	``¬ ¬ ¬ ¬ ¬ Credits_and_Change_Log_Text = ButtonFont5.render("Credits", self.aa, self.FontCol)``
135.	``¬ ¬ ¬ ¬ ¬ CreditsWidth = Credits_and_Change_Log_Text.get_width()``

136.	``¬ ¬ ¬ ¬ ¬ BenchmarkText = ButtonFont6.render("Benchmark", self.aa, self.FontCol)``
137.	``¬ ¬ ¬ ¬ ¬ BenchmarkWidth = BenchmarkText.get_width()``

138.	``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
139.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``
140.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
141.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
142.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "saveANDexit"``
143.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYDOWN: ``
144.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10: ``
145.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``
146.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
147.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
148.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
149.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
150.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``
151.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1 ``
152.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN: ``
153.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True ``
154.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONUP: ``
155.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

156.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Home screen")``
157.	``¬ ¬ ¬ ¬ ¬ ``
158.	``¬ ¬ ¬ ¬ ¬ ButtonFont1.set_underline(hover1) ``
159.	``¬ ¬ ¬ ¬ ¬ ButtonFont2.set_underline(hover2) ``
160.	``¬ ¬ ¬ ¬ ¬ ButtonFont3.set_underline(hover3)``
161.	``¬ ¬ ¬ ¬ ¬ ButtonFont4.set_underline(hover4)``
162.	``¬ ¬ ¬ ¬ ¬ ButtonFont5.set_underline(hover5)``
163.	``¬ ¬ ¬ ¬ ¬ ButtonFont6.set_underline(hover6)``
164.	``¬ ¬ ¬ ¬ ¬ ``
165.	``¬ ¬ ¬ ¬ ¬ if My >= 202*yScaleFact and My <= 247*yScaleFact and Mx >= (self.realWidth-(PlayWidth+SelectorWidth))-2:``
166.	``¬ ¬ ¬ ¬ ¬ ¬ hover1 = True``
167.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
168.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
169.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
170.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Play"``
171.	``¬ ¬ ¬ ¬ ¬ else:``
172.	``¬ ¬ ¬ ¬ ¬ ¬ hover1 = False``
173.	``¬ ¬ ¬ ¬ ¬ ``
174.	``¬ ¬ ¬ ¬ ¬ if My >= 252*yScaleFact and My <= 297*yScaleFact and Mx >= (self.realWidth-(SettingsWidth+SelectorWidth))-2: ``
175.	``¬ ¬ ¬ ¬ ¬ ¬ hover2 = True``
176.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
177.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
178.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
179.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
180.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
181.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Settings"``
182.	``¬ ¬ ¬ ¬ ¬ else:``
183.	``¬ ¬ ¬ ¬ ¬ ¬ hover2 = False``

184.	``¬ ¬ ¬ ¬ ¬ if My >= 302*yScaleFact and My <= 347*yScaleFact and Mx >= (self.realWidth-(CharDesignerWidth+SelectorWidth)-2):``
185.	``¬ ¬ ¬ ¬ ¬ ¬ hover3 = True``
186.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
187.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
188.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
189.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
190.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
191.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "CharacterDesigner"``
192.	``¬ ¬ ¬ ¬ ¬ else:``
193.	``¬ ¬ ¬ ¬ ¬ ¬ hover3 = False``

194.	``¬ ¬ ¬ ¬ ¬ if My >= 402*yScaleFact and My <= 447*yScaleFact and Mx >= (self.realWidth-(AchievementsWidth+SelectorWidth)-2):``
195.	``¬ ¬ ¬ ¬ ¬ ¬ hover4 = True``
196.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
197.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
198.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
199.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
200.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
201.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Achievements"``
202.	``¬ ¬ ¬ ¬ ¬ else:``
203.	``¬ ¬ ¬ ¬ ¬ ¬ hover4 = False``

204.	``¬ ¬ ¬ ¬ ¬ if My >= 352*yScaleFact and My <= 397*yScaleFact and Mx >= (self.realWidth-(CreditsWidth+SelectorWidth)-2):``
205.	``¬ ¬ ¬ ¬ ¬ ¬ hover5 = True``
206.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
207.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
208.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
209.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
210.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
211.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Credits"``
212.	``¬ ¬ ¬ ¬ ¬ else:``
213.	``¬ ¬ ¬ ¬ ¬ ¬ hover5 = False``

214.	``¬ ¬ ¬ ¬ ¬ if My >= 452*yScaleFact and My <= 497*yScaleFact and Mx >= (self.realWidth-(BenchmarkWidth+SelectorWidth)-2):``
215.	``¬ ¬ ¬ ¬ ¬ ¬ hover6 = True``
216.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
217.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
218.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
219.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
220.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
221.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Benchmark"``
222.	``¬ ¬ ¬ ¬ ¬ else:``
223.	``¬ ¬ ¬ ¬ ¬ ¬ hover6 = False``

224.	``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
225.	``¬ ¬ ¬ ¬ ¬ ``
226.	``¬ ¬ ¬ ¬ ¬ if self.FromPlay == True:``
227.	``¬ ¬ ¬ ¬ ¬ ¬ self.FromPlay = False``
228.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_HomeScreen__.GenerateHomeScreen.DisplayMessage(self, MessageFont, "Loading", self.AccentCol)``

229.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))``

230.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Name, (0, (self.realHeight-NameHeight)))``
231.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Version, ((self.realWidth-VersionWidth)-2, (self.realHeight-VersionHeight)))``

232.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Play, ((self.realWidth-PlayWidth)-2, 200*yScaleFact))``
233.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(SettingsText, ((self.realWidth-SettingsWidth)-2, 250*yScaleFact))``
234.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Character_DesignerText, ((self.realWidth-CharDesignerWidth)-2, 300*yScaleFact))``
235.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits_and_Change_Log_Text, ((self.realWidth-CreditsWidth)-2, 350*yScaleFact))``
236.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsText, ((self.realWidth-AchievementsWidth)-2, 400*yScaleFact))``
237.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkText, ((self.realWidth-BenchmarkWidth)-2, 450*yScaleFact))``

238.	``¬ ¬ ¬ ¬ ¬ if hover1 == True:``
239.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(PlayWidth+SelectorWidth)-2, 200*yScaleFact))``
240.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
241.	``¬ ¬ ¬ ¬ ¬ elif hover2 == True:``
242.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(SettingsWidth+SelectorWidth)-2, 250*yScaleFact))``
243.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
244.	``¬ ¬ ¬ ¬ ¬ elif hover3 == True:``
245.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(CharDesignerWidth+SelectorWidth)-2, 300*yScaleFact))``
246.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
247.	``¬ ¬ ¬ ¬ ¬ elif hover5 == True:``
248.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(CreditsWidth+SelectorWidth)-2, 350*yScaleFact))``
249.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
250.	``¬ ¬ ¬ ¬ ¬ elif hover4 == True:``
251.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(AchievementsWidth+SelectorWidth)-2, 400*yScaleFact))``
252.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
253.	``¬ ¬ ¬ ¬ ¬ elif hover6 == True:``
254.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(BenchmarkWidth+SelectorWidth)-2, 450*yScaleFact))``
255.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
256.	``¬ ¬ ¬ ¬ ¬ else:``
257.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_ARROW)``
258.	``¬ ¬ ¬ ¬ ¬ ¬ ``
259.	``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
260.	``¬ ¬ ¬ ¬ ¬ if not Message == None:``
261.	``¬ ¬ ¬ ¬ ¬ ¬ return Message, None``

262.	``¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, xScaleFact, yScaleFact, coloursARRAY)``

263.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
264.	``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
265.	``¬ ¬ ¬ except Exception as Message:``
266.	``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
267.	``¬ ¬ ¬ ¬ return Message, None``

.. note::
    For information on this consult the above guide
    268.	``else:``
    269.	``¬ print("You need to run this as part of Pycraft")``
    270.	``¬ import tkinter as tk``
    271.	``¬ from tkinter import messagebox``
    272.	``¬ root = tk.Tk()``
    273.	``¬ root.withdraw()``
    274.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    275.	``¬ quit()``


ImageUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_ImageUtils>")``
    3.	``¬ class ConvertImage:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def pilImageToSurface(self, pilImage):``
7.	``¬ ¬ ¬ return self.mod_Pygame__.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode).convert()``

.. note::
    For information on this consult the above guide
    8.	``else:``
    9.	``¬ print("You need to run this as part of Pycraft")``
    10.	``¬ import tkinter as tk``
    11.	``¬ from tkinter import messagebox``
    12.	``¬ root = tk.Tk()``
    13.	``¬ root.withdraw()``
    14.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    15.	``¬ quit()``


Inventory
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_Inventory>")``
    3.	``¬ class GenerateInventory:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def Inventory(self):``
7.	``¬ ¬ ¬ try:``
8.	``¬ ¬ ¬ ¬ Message = self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``
9.	``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
10.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``

11.	``¬ ¬ ¬ ¬ MainInventoryFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) ``
12.	``¬ ¬ ¬ ¬ PycraftTitle = MainInventoryFont.render("Pycraft", self.aa, self.FontCol)``
13.	``¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``

14.	``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
15.	``¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
16.	``¬ ¬ ¬ ¬ AlphaSurface = self.mod_Pygame__.Surface((realWidth, realHeight), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)``
17.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
18.	``¬ ¬ ¬ ¬ AlphaSurface.set_alpha(204) ``
19.	``¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``

20.	``¬ ¬ ¬ ¬ Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()``
21.	``¬ ¬ ¬ ¬ SelectorWidth = Selector.get_width()``

22.	``¬ ¬ ¬ ¬ hover1 = False ``
23.	``¬ ¬ ¬ ¬ hover2 = False ``
24.	``¬ ¬ ¬ ¬ hover3 = False ``
25.	``¬ ¬ ¬ ¬ hover4 = False ``
26.	``¬ ¬ ¬ ¬ hover5 = False ``
27.	``¬ ¬ ¬ ¬ hover6 = False ``
28.	``¬ ¬ ¬ ¬ hover7 = False``
29.	``¬ ¬ ¬ ¬ hover8 = False``
30.	``¬ ¬ ¬ ¬ mousebuttondown = False``

31.	``¬ ¬ ¬ ¬ ButtonFont1 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
32.	``¬ ¬ ¬ ¬ WeaponsText = ButtonFont1.render("Weapons", self.aa, self.FontCol)``
33.	``¬ ¬ ¬ ¬ WeaponsTextWidth = WeaponsText.get_width()``
34.	``¬ ¬ ¬ ¬ WeaponsTextHeight = WeaponsText.get_height()``

35.	``¬ ¬ ¬ ¬ ButtonFont2 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
36.	``¬ ¬ ¬ ¬ RangedWeaponsText = ButtonFont2.render("Ranged Weapons", self.aa, self.FontCol)``
37.	``¬ ¬ ¬ ¬ RangedWeaponsTextWidth = RangedWeaponsText.get_width()``
38.	``¬ ¬ ¬ ¬ RangedWeaponsTextHeight= RangedWeaponsText.get_height()``

39.	``¬ ¬ ¬ ¬ ButtonFont3 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
40.	``¬ ¬ ¬ ¬ ShieldsText = ButtonFont3.render("Shields", self.aa, self.FontCol)``
41.	``¬ ¬ ¬ ¬ ShieldsTextWidth = ShieldsText.get_width()``
42.	``¬ ¬ ¬ ¬ ShieldsTextHeight = ShieldsText.get_height()``

43.	``¬ ¬ ¬ ¬ ButtonFont4 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
44.	``¬ ¬ ¬ ¬ ArmourText = ButtonFont4.render("Armour", self.aa, self.FontCol)``
45.	``¬ ¬ ¬ ¬ ArmourTextWidth = ArmourText.get_width()``
46.	``¬ ¬ ¬ ¬ ArmourTextHeight = ArmourText.get_height()``

47.	``¬ ¬ ¬ ¬ ButtonFont5 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
48.	``¬ ¬ ¬ ¬ FoodText = ButtonFont5.render("Food", self.aa, self.FontCol)``
49.	``¬ ¬ ¬ ¬ FoodTextWidth = FoodText.get_width()``
50.	``¬ ¬ ¬ ¬ FoodTextHeight = FoodText.get_height()``

51.	``¬ ¬ ¬ ¬ ButtonFont6 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
52.	``¬ ¬ ¬ ¬ ItemsText = ButtonFont6.render("Items", self.aa, self.FontCol)``
53.	``¬ ¬ ¬ ¬ ItemsTextWidth = ItemsText.get_width()``
54.	``¬ ¬ ¬ ¬ ItemsTextHeight = ItemsText.get_height()``

55.	``¬ ¬ ¬ ¬ ButtonFont7 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
56.	``¬ ¬ ¬ ¬ SpecialItemsText = ButtonFont7.render("Special Items", self.aa, self.FontCol)``
57.	``¬ ¬ ¬ ¬ SpecialItemsTextWidth = SpecialItemsText.get_width()``
58.	``¬ ¬ ¬ ¬ SpecialItemsTextHeight = SpecialItemsText.get_height()``

59.	``¬ ¬ ¬ ¬ ButtonFont8 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) ``
60.	``¬ ¬ ¬ ¬ OptionsText = ButtonFont7.render("Options", self.aa, self.FontCol)``
61.	``¬ ¬ ¬ ¬ OptionsTextWidth = OptionsText.get_width()``
62.	``¬ ¬ ¬ ¬ OptionsTextHeight = OptionsText.get_height()``

63.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Playing | Inventory")``

64.	``¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``

65.	``¬ ¬ ¬ ¬ while True:``
66.	``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

67.	``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
68.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
69.	``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
70.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

71.	``¬ ¬ ¬ ¬ ¬ yScaleFact = realHeight/720``
72.	``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``

73.	``¬ ¬ ¬ ¬ ¬ Mx, My = self.mod_Pygame__.mouse.get_pos() ``
74.	``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

75.	``¬ ¬ ¬ ¬ ¬ if self.aa == True:``
76.	``¬ ¬ ¬ ¬ ¬ ¬ pilImage = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png"))).resize((realWidth, realHeight), self.mod_PIL_Image_.ANTIALIAS)``
77.	``¬ ¬ ¬ ¬ ¬ else:``
78.	``¬ ¬ ¬ ¬ ¬ ¬ pilImage = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png"))).resize((realWidth, realHeight))``
79.	``¬ ¬ ¬ ¬ ¬ ``
80.	``¬ ¬ ¬ ¬ ¬ BLURRED_pilImage = pilImage.filter(self.mod_PIL_ImageFilter_.BoxBlur(4))``

81.	``¬ ¬ ¬ ¬ ¬ PauseImg = self.mod_ImageUtils__.ConvertImage.pilImageToSurface(self, BLURRED_pilImage)``
82.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(PauseImg, (0, 0))``
83.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(AlphaSurface, (0, 0))``

84.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((realWidth-TitleWidth)/2, 0))``

85.	``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
86.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_e):``
87.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Load3D = False``
88.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
89.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
90.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
91.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.VIDEORESIZE:``
92.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
93.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface = self.mod_Pygame__.Surface((realWidth, realHeight), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)``
94.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.set_alpha(204)``
95.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``
96.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:``
97.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True ``
98.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONUP:``
99.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
100.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYDOWN:``
101.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
102.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
103.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface = self.mod_Pygame__.Surface((FullscreenX, FullscreenY), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)``
104.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.set_alpha(204) ``
105.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``
106.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
107.	``¬ ¬ ¬ ¬ ¬ if My >= 202*yScaleFact and My <= 247*yScaleFact and Mx >= 1155:``
108.	``¬ ¬ ¬ ¬ ¬ ¬ hover1 = True``
109.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
110.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
111.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip() ``
112.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
113.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
114.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
115.	``¬ ¬ ¬ ¬ ¬ else: ``
116.	``¬ ¬ ¬ ¬ ¬ ¬ hover1 = False ``

117.	``¬ ¬ ¬ ¬ ¬ if My >= 252*yScaleFact and My <= 297*yScaleFact and Mx >= 1105: ``
118.	``¬ ¬ ¬ ¬ ¬ ¬ hover2 = True``
119.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
120.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
121.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
122.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
123.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
124.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
125.	``¬ ¬ ¬ ¬ ¬ else:``
126.	``¬ ¬ ¬ ¬ ¬ ¬ hover2 = False``

127.	``¬ ¬ ¬ ¬ ¬ if My >= 302*yScaleFact and My <= 347*yScaleFact and Mx >= 865:``
128.	``¬ ¬ ¬ ¬ ¬ ¬ hover3 = True``
129.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
130.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
131.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
132.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
133.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
134.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
135.	``¬ ¬ ¬ ¬ ¬ else:``
136.	``¬ ¬ ¬ ¬ ¬ ¬ hover3 = False``

137.	``¬ ¬ ¬ ¬ ¬ if My >= 402*yScaleFact and My <= 447*yScaleFact and Mx >= 1035:``
138.	``¬ ¬ ¬ ¬ ¬ ¬ hover4 = True``
139.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
140.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
141.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
142.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
143.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
144.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
145.	``¬ ¬ ¬ ¬ ¬ else:``
146.	``¬ ¬ ¬ ¬ ¬ ¬ hover4 = False``

147.	``¬ ¬ ¬ ¬ ¬ if My >= 352*yScaleFact and My <= 397*yScaleFact and Mx >= 880:``
148.	``¬ ¬ ¬ ¬ ¬ ¬ hover5 = True``
149.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
150.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
151.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
152.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
153.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
154.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
155.	``¬ ¬ ¬ ¬ ¬ else:``
156.	``¬ ¬ ¬ ¬ ¬ ¬ hover5 = False``

157.	``¬ ¬ ¬ ¬ ¬ if My >= 502*yScaleFact and My <= 547*yScaleFact and Mx >= 1095:``
158.	``¬ ¬ ¬ ¬ ¬ ¬ hover6 = True``
159.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
160.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
161.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
162.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
163.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
164.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
165.	``¬ ¬ ¬ ¬ ¬ else:``
166.	``¬ ¬ ¬ ¬ ¬ ¬ hover6 = False``

167.	``¬ ¬ ¬ ¬ ¬ if My >= 452*yScaleFact and My <= 497*yScaleFact and Mx >= 1095:``
168.	``¬ ¬ ¬ ¬ ¬ ¬ hover7 = True``
169.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
170.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
171.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
172.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
173.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
174.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
175.	``¬ ¬ ¬ ¬ ¬ else:``
176.	``¬ ¬ ¬ ¬ ¬ ¬ hover7 = False``

177.	``¬ ¬ ¬ ¬ ¬ if My >= 552*yScaleFact and My <= 597*yScaleFact and Mx >= 1095:``
178.	``¬ ¬ ¬ ¬ ¬ ¬ hover8 = True``
179.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
180.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
181.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
182.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
183.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
184.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
185.	``¬ ¬ ¬ ¬ ¬ else:``
186.	``¬ ¬ ¬ ¬ ¬ ¬ hover8 = False``
187.	``¬ ¬ ¬ ¬ ¬ ``
188.	``¬ ¬ ¬ ¬ ¬ ButtonFont1.set_underline(hover1) ``
189.	``¬ ¬ ¬ ¬ ¬ ButtonFont2.set_underline(hover2) ``
190.	``¬ ¬ ¬ ¬ ¬ ButtonFont3.set_underline(hover3)``
191.	``¬ ¬ ¬ ¬ ¬ ButtonFont4.set_underline(hover4)``
192.	``¬ ¬ ¬ ¬ ¬ ButtonFont5.set_underline(hover5)``
193.	``¬ ¬ ¬ ¬ ¬ ButtonFont6.set_underline(hover6)``
194.	``¬ ¬ ¬ ¬ ¬ ButtonFont7.set_underline(hover7)``
195.	``¬ ¬ ¬ ¬ ¬ ButtonFont8.set_underline(hover8)``
196.	``¬ ¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol) ``
197.	``¬ ¬ ¬ ¬ ¬ ¬ ``
198.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(WeaponsText, ((realWidth-WeaponsTextWidth)-2, 200*yScaleFact)) # ???``

199.	``¬ ¬ ¬ ¬ ¬ if hover1 == True: ``
200.	``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(WeaponsTextWidth+SelectorWidth)-2, 200*yScaleFact))``
201.	``¬ ¬ ¬ ¬ ¬ ¬ ``
202.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(RangedWeaponsText, ((realWidth-RangedWeaponsTextWidth)-2, 250*yScaleFact))``
203.	``¬ ¬ ¬ ¬ ¬ if hover2 == True: ``
204.	``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(RangedWeaponsTextWidth+SelectorWidth)-2, 250*yScaleFact))``
205.	``¬ ¬ ¬ ¬ ¬ ¬ ``
206.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(ShieldsText, ((realWidth-ShieldsTextWidth)-2, 300*yScaleFact))``
207.	``¬ ¬ ¬ ¬ ¬ if hover3 == True: ``
208.	``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(ShieldsTextWidth+SelectorWidth)-2, 300*yScaleFact))``
209.	``¬ ¬ ¬ ¬ ¬ ¬ ``
210.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(ArmourText, ((realWidth-ArmourTextWidth)-2, 350*yScaleFact))``
211.	``¬ ¬ ¬ ¬ ¬ if hover4 == True: ``
212.	``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(FoodTextWidth+SelectorWidth)-2, 400*yScaleFact))``
213.	``¬ ¬ ¬ ¬ ¬ ¬ ``
214.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(FoodText, ((realWidth-FoodTextWidth)-2, 400*yScaleFact))``
215.	``¬ ¬ ¬ ¬ ¬ if hover5 == True: ``
216.	``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(ArmourTextWidth+SelectorWidth)-2, 350*yScaleFact))``
217.	``¬ ¬ ¬ ¬ ¬ ¬ ``
218.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(ItemsText, ((realWidth-ItemsTextWidth)-2, 450*yScaleFact))``
219.	``¬ ¬ ¬ ¬ ¬ if hover6 == True: ``
220.	``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(SpecialItemsTextWidth+SelectorWidth)-2, 500*yScaleFact))``
221.	``¬ ¬ ¬ ¬ ¬ ¬ ``
222.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(SpecialItemsText, ((realWidth-SpecialItemsTextWidth)-2, 500*yScaleFact))``
223.	``¬ ¬ ¬ ¬ ¬ if hover7 == True: ``
224.	``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(ItemsTextWidth+SelectorWidth)-2, 450*yScaleFact))``

225.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(OptionsText, ((realWidth-OptionsTextWidth)-2, 550*yScaleFact))``
226.	``¬ ¬ ¬ ¬ ¬ if hover8 == True:``
227.	``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(OptionsTextWidth+SelectorWidth)-2, 550*yScaleFact))``

228.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``
229.	``¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)``
230.	``¬ ¬ ¬ except Exception as Message:``
231.	``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
232.	``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    233.	``else:``
    234.	``¬ print("You need to run this as part of Pycraft")``
    235.	``¬ import tkinter as tk``
    236.	``¬ from tkinter import messagebox``
    237.	``¬ root = tk.Tk()``
    238.	``¬ root.withdraw()``
    239.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    240.	``¬ quit()``


Main
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

1.	``print("Started <Pycraft_main>")``
2.	``class Startup:``
3.	``¬ def __init__(Class_Startup_variables):``
4.	``¬ ¬ try:``
5.	``¬ ¬ ¬ import tkinter as tk``
6.	``¬ ¬ ¬ Class_Startup_variables.mod_Tkinter__tk = tk # [Class_Startup_variables] mod (module) (module name) (subsection of module) (name references)``
7.	``¬ ¬ ¬ import tkinter.ttk  # Class _ <class_name> _ variables``
8.	``¬ ¬ ¬ Class_Startup_variables.mod_Tkinter_ttk_ = tkinter.ttk``
9.	``¬ ¬ ¬ from tkinter import messagebox``
10.	``¬ ¬ ¬ Class_Startup_variables.mod_Tkinter_messagebox_ = messagebox``
11.	``¬ ¬ ¬ from PIL import Image, ImageFilter, ImageGrab, ImageTk``
12.	``¬ ¬ ¬ Class_Startup_variables.mod_PIL_Image_ = Image``
13.	``¬ ¬ ¬ Class_Startup_variables.mod_PIL_ImageFilter_ = ImageFilter``
14.	``¬ ¬ ¬ Class_Startup_variables.mod_PIL_ImageTk_ = ImageTk``
15.	``¬ ¬ ¬ Class_Startup_variables.mod_PIL_ImageGrab_ = ImageGrab``
16.	``¬ ¬ ¬ import pygame``
17.	``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__ = pygame``
18.	``¬ ¬ ¬ import numpy``
19.	``¬ ¬ ¬ Class_Startup_variables.mod_Numpy__ = numpy``
20.	``¬ ¬ ¬ import os``
21.	``¬ ¬ ¬ Class_Startup_variables.mod_OS__ = os``
22.	``¬ ¬ ¬ import sys``
23.	``¬ ¬ ¬ Class_Startup_variables.mod_Sys__ = sys``
24.	``¬ ¬ ¬ import random``
25.	``¬ ¬ ¬ Class_Startup_variables.mod_Random__ = random``
26.	``¬ ¬ ¬ import time``
27.	``¬ ¬ ¬ Class_Startup_variables.mod_Time__ = time``
28.	``¬ ¬ ¬ import pygame.locals``
29.	``¬ ¬ ¬ Class_Startup_variables.mod_Pygame_locals_ = pygame.locals``
30.	``¬ ¬ ¬ import OpenGL``
31.	``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL__ = OpenGL``
32.	``¬ ¬ ¬ import OpenGL.GL``
33.	``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL_GL_ = OpenGL.GL``
34.	``¬ ¬ ¬ import OpenGL.GLU``
35.	``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL_GLU_ = OpenGL.GLU``
36.	``¬ ¬ ¬ import OpenGL.GLUT``
37.	``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL_GLUT_ = OpenGL.GLUT``
38.	``¬ ¬ ¬ import moderngl``
39.	``¬ ¬ ¬ Class_Startup_variables.mod_ModernGL__ = moderngl``
40.	``¬ ¬ ¬ import moderngl_window``
41.	``¬ ¬ ¬ Class_Startup_variables.mod_ModernGL_window_ = moderngl_window``
42.	``¬ ¬ ¬ import pyautogui``
43.	``¬ ¬ ¬ Class_Startup_variables.mod_Pyautogui__ = pyautogui``
44.	``¬ ¬ ¬ import psutil``
45.	``¬ ¬ ¬ Class_Startup_variables.mod_Psutil__ = psutil``
46.	``¬ ¬ ¬ import pywavefront``
47.	``¬ ¬ ¬ Class_Startup_variables.mod_Pywavefront__ = pywavefront``
48.	``¬ ¬ ¬ import timeit``
49.	``¬ ¬ ¬ Class_Startup_variables.mod_Timeit__ = timeit``
50.	``¬ ¬ ¬ import subprocess``
51.	``¬ ¬ ¬ Class_Startup_variables.mod_Subprocess__ = subprocess``
52.	``¬ ¬ ¬ import traceback``
53.	``¬ ¬ ¬ Class_Startup_variables.mod_Traceback__ = traceback``
54.	``¬ ¬ ¬ import datetime``
55.	``¬ ¬ ¬ Class_Startup_variables.mod_Datetime__ = datetime``
56.	``¬ ¬ ¬ import ctypes``
57.	``¬ ¬ ¬ Class_Startup_variables.mod_Ctypes__ = ctypes``
58.	``¬ ¬ ¬ import json``
59.	``¬ ¬ ¬ Class_Startup_variables.mod_JSON__ = json``
60.	``¬ ¬ ¬ import threading``
61.	``¬ ¬ ¬ Class_Startup_variables.mod_Threading__ = threading``
62.	``¬ ¬ ¬ import cpuinfo``
63.	``¬ ¬ ¬ Class_Startup_variables.mod_CPUinfo__ = cpuinfo``
64.	``¬ ¬ ¬ import array``
65.	``¬ ¬ ¬ Class_Startup_variables.mod_Array__ = array``
66.	``¬ ¬ ¬ import GPUtil``
67.	``¬ ¬ ¬ Class_Startup_variables.mod_GPUtil__ = GPUtil``
68.	``¬ ¬ ¬ from tabulate import tabulate``
69.	``¬ ¬ ¬ Class_Startup_variables.mod_Tabulate_tabulate_ = tabulate``
70.	``¬ ¬ ¬ from pyrr import Matrix44``
71.	``¬ ¬ ¬ Class_Startup_variables.mod_Pyrr_Matrix44_ = Matrix44``
72.	``¬ ¬ ¬ ``
73.	``¬ ¬ ¬ moderngl.create_standalone_context()``
74.	``¬ ¬ ¬ ``
75.	``¬ ¬ ¬ os.environ['SDL_VIDEO_CENTERED'] = '1'``

76.	``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.init()``
77.	``¬ ¬ ¬ ``
78.	``¬ ¬ ¬ import PycraftStartupTest``
79.	``¬ ¬ ¬ Class_Startup_variables.mod_PycraftStartupTest__ = PycraftStartupTest``
80.	``¬ ¬ ¬ import StartupAnimation``
81.	``¬ ¬ ¬ Class_Startup_variables.mod_StartupAnimation__ = StartupAnimation``
82.	``¬ ¬ ¬ import DisplayUtils``
83.	``¬ ¬ ¬ Class_Startup_variables.mod_DisplayUtils__ = DisplayUtils``
84.	``¬ ¬ ¬ import GetSavedData``
85.	``¬ ¬ ¬ Class_Startup_variables.mod_GetSavedData__ = GetSavedData``
86.	``¬ ¬ ¬ import ThemeUtils``
87.	``¬ ¬ ¬ Class_Startup_variables.mod_ThemeUtils__ = ThemeUtils``
88.	``¬ ¬ ¬ import HomeScreen``
89.	``¬ ¬ ¬ Class_Startup_variables.mod_HomeScreen__ = HomeScreen``
90.	``¬ ¬ ¬ import SoundUtils``
91.	``¬ ¬ ¬ Class_Startup_variables.mod_SoundUtils__ = SoundUtils``
92.	``¬ ¬ ¬ import DrawingUtils``
93.	``¬ ¬ ¬ Class_Startup_variables.mod_DrawingUtils__ = DrawingUtils``
94.	``¬ ¬ ¬ import CaptionUtils``
95.	``¬ ¬ ¬ Class_Startup_variables.mod_CaptionUtils__ = CaptionUtils``
96.	``¬ ¬ ¬ import Credits``
97.	``¬ ¬ ¬ Class_Startup_variables.mod_Credits__ = Credits``
98.	``¬ ¬ ¬ import TkinterUtils``
99.	``¬ ¬ ¬ Class_Startup_variables.mod_TkinterUtils__ = TkinterUtils``
100.	``¬ ¬ ¬ import Achievements``
101.	``¬ ¬ ¬ Class_Startup_variables.mod_Achievements__ = Achievements``
102.	``¬ ¬ ¬ import CharacterDesigner``
103.	``¬ ¬ ¬ Class_Startup_variables.mod_CharacterDesigner__ = CharacterDesigner``
104.	``¬ ¬ ¬ import Settings``
105.	``¬ ¬ ¬ Class_Startup_variables.mod_Settings__ = Settings``
106.	``¬ ¬ ¬ import Benchmark``
107.	``¬ ¬ ¬ Class_Startup_variables.mod_Benchmark__ = Benchmark``
108.	``¬ ¬ ¬ import ExBenchmark``
109.	``¬ ¬ ¬ Class_Startup_variables.mod_ExBenchmark__ = ExBenchmark``
110.	``¬ ¬ ¬ import OGLbenchmark``
111.	``¬ ¬ ¬ Class_Startup_variables.mod_OGLbenchmark__ = OGLbenchmark``
112.	``¬ ¬ ¬ import base``
113.	``¬ ¬ ¬ Class_Startup_variables.mod_Base__ = base``
114.	``¬ ¬ ¬ import ShareDataUtil``
115.	``¬ ¬ ¬ Class_Startup_variables.mod_Globals__ = ShareDataUtil``
116.	``¬ ¬ ¬ import TextUtils``
117.	``¬ ¬ ¬ Class_Startup_variables.mod_TextUtils__ = TextUtils``
118.	``¬ ¬ ¬ import Inventory``
119.	``¬ ¬ ¬ Class_Startup_variables.mod_Inventory__ = Inventory``
120.	``¬ ¬ ¬ import ImageUtils``
121.	``¬ ¬ ¬ Class_Startup_variables.mod_ImageUtils__ = ImageUtils``
122.	``¬ ¬ ¬ import MapGUI``
123.	``¬ ¬ ¬ Class_Startup_variables.mod_MapGUI__ = MapGUI``
124.	``¬ ¬ ¬ import ThreadingUtil``
125.	``¬ ¬ ¬ Class_Startup_variables.mod_ThreadingUtil__ = ThreadingUtil``

126.	``¬ ¬ ¬ Class_Startup_variables.aa = True``
127.	``¬ ¬ ¬ Class_Startup_variables.AccentCol = (237, 125, 49)``
128.	``¬ ¬ ¬ Class_Startup_variables.aFPS = 0``
129.	``¬ ¬ ¬ Class_Startup_variables.BackgroundCol = [30, 30, 30]``
130.	``¬ ¬ ¬ Class_Startup_variables.base_folder = os.path.dirname(__file__)``
131.	``¬ ¬ ¬ Class_Startup_variables.cameraANGspeed = 3.5``
132.	``¬ ¬ ¬ Class_Startup_variables.clock = pygame.time.Clock()``
133.	``¬ ¬ ¬ Class_Startup_variables.Collisions = [False, 0]``
134.	``¬ ¬ ¬ Class_Startup_variables.CompletePercent = 0``
135.	``¬ ¬ ¬ Class_Startup_variables.ctx = 0``
136.	``¬ ¬ ¬ Class_Startup_variables.Load_Progress = 0``
137.	``¬ ¬ ¬ Class_Startup_variables.crash = False``
138.	``¬ ¬ ¬ Class_Startup_variables.CurrentlyPlaying = None``

139.	``¬ ¬ ¬ Class_Startup_variables.Data_aFPS_Min = 60``
140.	``¬ ¬ ¬ Class_Startup_variables.Data_aFPS = []``
141.	``¬ ¬ ¬ Class_Startup_variables.Data_aFPS_Max = 1``

142.	``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Min = 60``
143.	``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE = []``
144.	``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Max = 1``

145.	``¬ ¬ ¬ Class_Startup_variables.Data_eFPS_Min = 60``
146.	``¬ ¬ ¬ Class_Startup_variables.Data_eFPS = []``
147.	``¬ ¬ ¬ Class_Startup_variables.Data_eFPS_Max = 1``

148.	``¬ ¬ ¬ Class_Startup_variables.Data_MemUsE_Min = 60``
149.	``¬ ¬ ¬ Class_Startup_variables.Data_MemUsE = []``
150.	``¬ ¬ ¬ Class_Startup_variables.Data_MemUsE_Max = 1``

151.	``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Min = 60``
152.	``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE = []``
153.	``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Max = 1``
154.	``¬ ¬ ¬ ``
155.	``¬ ¬ ¬ Class_Startup_variables.Devmode = 0``
156.	``¬ ¬ ¬ Class_Startup_variables.Display = 0``
157.	``¬ ¬ ¬ Class_Startup_variables.eFPS = 60``
158.	``¬ ¬ ¬ Class_Startup_variables.FanSky = True``
159.	``¬ ¬ ¬ Class_Startup_variables.FanPart = True``
160.	``¬ ¬ ¬ Class_Startup_variables.FontCol = (255, 255, 255)``
161.	``¬ ¬ ¬ Class_Startup_variables.FOV = 70``
162.	``¬ ¬ ¬ Class_Startup_variables.FromPlay = False``
163.	``¬ ¬ ¬ Class_Startup_variables.Fullscreen = False``
164.	``¬ ¬ ¬ Class_Startup_variables.FPS = 60``
165.	``¬ ¬ ¬ Class_Startup_variables.FullscreenX, Class_Startup_variables.FullscreenY = pyautogui.size()``
166.	``¬ ¬ ¬ Class_Startup_variables.GameError = None``
167.	``¬ ¬ ¬ Class_Startup_variables.G3Dscale = 600000``
168.	``¬ ¬ ¬ Class_Startup_variables.GetScreenGraphics = True``
169.	``¬ ¬ ¬ Class_Startup_variables.HUD_Surface = None``
170.	``¬ ¬ ¬ Class_Startup_variables.Iteration = 1``
171.	``¬ ¬ ¬ Class_Startup_variables.lastRun = "29/09/2021"``
172.	``¬ ¬ ¬ Class_Startup_variables.Load3D = True``
173.	``¬ ¬ ¬ Class_Startup_variables.LoadMusic = True``
174.	``¬ ¬ ¬ ``
175.	``¬ ¬ ¬ Class_Startup_variables.Map = 0``
176.	``¬ ¬ ¬ Class_Startup_variables.Map_box = 0``
177.	``¬ ¬ ¬ Class_Startup_variables.Map_scale = 0``
178.	``¬ ¬ ¬ Class_Startup_variables.Map_size = 0``
179.	``¬ ¬ ¬ Class_Startup_variables.Map_trans = 0``
180.	``¬ ¬ ¬ Class_Startup_variables.MapVerts = 0``
181.	``¬ ¬ ¬ Class_Startup_variables.map_vertices = []``
182.	``¬ ¬ ¬ Class_Startup_variables.max_Map_size = 0``
183.	``¬ ¬ ¬ ``
184.	``¬ ¬ ¬ Class_Startup_variables.HUD_object = 0``
185.	``¬ ¬ ¬ Class_Startup_variables.HUD_box = 0``
186.	``¬ ¬ ¬ Class_Startup_variables.HUD_scale = 0``
187.	``¬ ¬ ¬ Class_Startup_variables.HUD_size = 0``
188.	``¬ ¬ ¬ Class_Startup_variables.HUD_trans = 0``
189.	``¬ ¬ ¬ Class_Startup_variables.HUDVerts = 0``
190.	``¬ ¬ ¬ Class_Startup_variables.HUD_vertices = []``
191.	``¬ ¬ ¬ Class_Startup_variables.max_HUD_size = 0``
192.	``¬ ¬ ¬ ``
193.	``¬ ¬ ¬ Class_Startup_variables.Map_max_v = 0``
194.	``¬ ¬ ¬ Class_Startup_variables.Map_min_v = 0``
195.	``¬ ¬ ¬ ``
196.	``¬ ¬ ¬ Class_Startup_variables.HUD_max_v = 0``
197.	``¬ ¬ ¬ Class_Startup_variables.HUD_min_v = 0``
198.	``¬ ¬ ¬ ``
199.	``¬ ¬ ¬ Class_Startup_variables.music = True``
200.	``¬ ¬ ¬ Class_Startup_variables.musicVOL = 5``
201.	``¬ ¬ ¬ Class_Startup_variables.Numpy_map_vertices = 0``
202.	``¬ ¬ ¬ Class_Startup_variables.Progress_Line = []``
203.	``¬ ¬ ¬ Class_Startup_variables.ProgressMessageText = "Initiating"``
204.	``¬ ¬ ¬ Class_Startup_variables.realHeight = 720``
205.	``¬ ¬ ¬ Class_Startup_variables.realWidth = 1280``
206.	``¬ ¬ ¬ Class_Startup_variables.RecommendedFPS = 60``
207.	``¬ ¬ ¬ Class_Startup_variables.RenderFOG = True``
208.	``¬ ¬ ¬ Class_Startup_variables.RunFullStartup = False``
209.	``¬ ¬ ¬ Class_Startup_variables.SecondFontCol = (100, 100, 100)``
210.	``¬ ¬ ¬ Class_Startup_variables.SavedWidth = 1280``
211.	``¬ ¬ ¬ Class_Startup_variables.SavedHeight = 720``
212.	``¬ ¬ ¬ Class_Startup_variables.ShapeCol = (80, 80, 80)``
213.	``¬ ¬ ¬ Class_Startup_variables.skybox_texture = 0``
214.	``¬ ¬ ¬ Class_Startup_variables.sound = True``
215.	``¬ ¬ ¬ Class_Startup_variables.soundVOL = 75``
216.	``¬ ¬ ¬ Class_Startup_variables.Stop_Thread_Event = Class_Startup_variables.mod_Threading__.Event()``
217.	``¬ ¬ ¬ Class_Startup_variables.SettingsPreference = "Medium"``
218.	``¬ ¬ ¬ Class_Startup_variables.theme = False``
219.	``¬ ¬ ¬ Class_Startup_variables.ThreadStatus = "Running"``
220.	``¬ ¬ ¬ Class_Startup_variables.Timer = 0``
221.	``¬ ¬ ¬ Class_Startup_variables.Total_move_x = 0``
222.	``¬ ¬ ¬ Class_Startup_variables.Total_move_y = 0``
223.	``¬ ¬ ¬ Class_Startup_variables.Total_move_z = 0``
224.	``¬ ¬ ¬ Class_Startup_variables.TotalRotation = 0``
225.	``¬ ¬ ¬ Class_Startup_variables.Total_Vertices = 0``
226.	``¬ ¬ ¬ Class_Startup_variables.version = "0.9.3"``
227.	``¬ ¬ ¬ Class_Startup_variables.vertex = 0``
228.	``¬ ¬ ¬ Class_Startup_variables.X = 0``
229.	``¬ ¬ ¬ Class_Startup_variables.Y = 0``
230.	``¬ ¬ ¬ Class_Startup_variables.Z = 0``

231.	``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.StartVariableChecking, args=(Class_Startup_variables,))``
232.	``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.start()``
233.	``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.name = "Thread_StartLongThread"``

234.	``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.StartCPUlogging, args=(Class_Startup_variables,))``
235.	``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.start()``
236.	``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.name = "Thread_GetCPUMetrics"``

237.	``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.AdaptiveMode, args=(Class_Startup_variables,))``
238.	``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.start()``
239.	``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.name = "Thread_AdaptiveMode"``
240.	``¬ ¬ ¬ ``
241.	``¬ ¬ ¬ Class_Startup_variables.mod_Globals__.Share.initialize(Class_Startup_variables)``
242.	``¬ ¬ ¬ ``
243.	``¬ ¬ ¬ import GameEngine``
244.	``¬ ¬ ¬ Class_Startup_variables.mod_MainGameEngine__ = GameEngine``
245.	``¬ ¬ except Exception as error:``
246.	``¬ ¬ ¬ print(error)``
247.	``¬ ¬ ¬ try:``
248.	``¬ ¬ ¬ ¬ import tkinter as tk``
249.	``¬ ¬ ¬ ¬ root = tk.Tk()``
250.	``¬ ¬ ¬ ¬ root.withdraw()``
251.	``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Tkinter_messagebox_.showerror("Startup Fail", "Missing required modules")``
252.	``¬ ¬ ¬ ¬ quit()``
253.	``¬ ¬ ¬ except:``
254.	``¬ ¬ ¬ ¬ try:``
255.	``¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
256.	``¬ ¬ ¬ ¬ ¬ sys.exit("0.0.0 -Thank you for playing")``
257.	``¬ ¬ ¬ ¬ except:``
258.	``¬ ¬ ¬ ¬ ¬ quit()``
259.	``¬ ¬ ¬ ¬ ¬ ``
260.	``¬ def crash(ErrorREPORT):``
261.	``¬ ¬ Class_Startup_variables.Stop_Thread_Event.set()``
262.	``¬ ¬ if not ErrorREPORT == None:``
263.	``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
264.	``¬ ¬ ¬ Class_Startup_variables.mod_Time__.sleep(1.01)``
265.	``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.init()``
266.	``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.mixer.stop()``
267.	``¬ ¬ ¬ try:``
268.	``¬ ¬ ¬ ¬ Message = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.SaveTOconfigFILE(Class_Startup_variables)``
269.	``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.quit()``
270.	``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.init()``
271.	``¬ ¬ ¬ ¬ Display = Class_Startup_variables.mod_Pygame__.display.set_mode((1280, 720))``
272.	``¬ ¬ ¬ ¬ icon = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
273.	``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.set_icon(icon)``
274.	``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.set_caption(f"Pycraft: An Error Occurred")``

275.	``¬ ¬ ¬ ¬ MessageFont = Class_Startup_variables.mod_Pygame__.font.Font(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Fonts\\Book Antiqua.ttf")), 15)``

276.	``¬ ¬ ¬ ¬ ErrorMessageText = MessageFont.render(str(ErrorREPORT), True, (255,0,0))``
277.	``¬ ¬ ¬ ¬ ErrorMessageTextWidth = ErrorMessageText.get_width()``
278.	``¬ ¬ ¬ ¬ ErrorMessageTextHeight = ErrorMessageText.get_height()``
279.	``¬ ¬ ¬ ¬ Display = Class_Startup_variables.mod_Pygame__.display.set_mode((1280,720))``

280.	``¬ ¬ ¬ ¬ IconImage = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Resources\\Error_Resources\\Icon.jpg")))``
281.	``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.set_icon(IconImage)``
282.	``¬ ¬ ¬ ¬ image = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Resources\\Error_Resources\\Error_Message.png")))``
283.	``¬ ¬ ¬ ¬ Clock = Class_Startup_variables.mod_Pygame__.time.Clock()``
284.	``¬ ¬ ¬ ¬ while True:``
285.	``¬ ¬ ¬ ¬ ¬ Display.fill((20,20,20))``
286.	``¬ ¬ ¬ ¬ ¬ Display.blit(image, (0,0))``

287.	``¬ ¬ ¬ ¬ ¬ Display.blit(ErrorMessageText, ((((1280/2)-ErrorMessageTextWidth)/2), (720-ErrorMessageTextHeight)/2))``

288.	``¬ ¬ ¬ ¬ ¬ for event in Class_Startup_variables.mod_Pygame__.event.get():``
289.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == Class_Startup_variables.mod_Pygame__.QUIT:``
290.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.join()``
291.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.join()``
292.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.join()``
293.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
294.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
295.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit(f"0.1.0- Thank you for playing")``

296.	``¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.flip()``
297.	``¬ ¬ ¬ ¬ ¬ Clock.tick(30)``
298.	``¬ ¬ ¬ except Exception as error:``
299.	``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit(f"0.2.0- {error} Thank you for playing")``
300.	``¬ ¬ else:``
301.	``¬ ¬ ¬ try:``
302.	``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
303.	``¬ ¬ ¬ except Exception as error:``
304.	``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit(f"0.3.0- {error} Thank you for playing")``
305.	``¬ ¬ ¬ ¬ quit()``
306.	``¬ ¬ ¬ else:``
307.	``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit("0.4.0- Thank you for playing")``
308.	``¬ ¬ ¬ ¬ quit()``

309.	``Class_Startup_variables = Startup()``
310.	``try:``
311.	``¬ Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.ReadMainSave(Class_Startup_variables)``
312.	``except Exception as FileError:``
313.	``¬ try:``
314.	``¬ ¬ if str(FileError) == "Expecting value: line 1 column 1 (char 0)":``
315.	``¬ ¬ ¬ Report = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.RepairLostSave(Class_Startup_variables)``
316.	``¬ ¬ ¬ ErrorString = "Unable to access vital Saved Data, have attempted a fix successfully", FileError``
317.	``¬ ¬ ¬ Message = "0.0.0- " + str(ErrorString)``
318.	``¬ ¬ ¬ Startup.crash(Message)``
319.	``¬ except Exception as Error:``
320.	``¬ ¬ Message = "0.0.1- " + str(Error)``
321.	``¬ ¬ Startup.crash(Message)``

322.	``¬ Message = "0.2- " + str(FileError)``
323.	``¬ Startup.crash(Message)``

324.	``Message = Class_Startup_variables.mod_PycraftStartupTest__.StartupTest.PycraftSelfTest(Class_Startup_variables)``
325.	``if not Message == None:``
326.	``¬ Message = "0.0.3- " + str(Message)``
327.	``¬ Startup.crash(Message)``

328.	``if Class_Startup_variables.theme == False:``
329.	``¬ Message = Class_Startup_variables.mod_ThemeUtils__.DetermineThemeColours.GetThemeGUI(Class_Startup_variables)``
330.	``¬ if not Message == None:``
331.	``¬ ¬ Message = "0.0.4- " + str(Message)``
332.	``¬ ¬ Startup.crash(Message)``

333.	``Message = Class_Startup_variables.mod_ThemeUtils__.DetermineThemeColours.GetColours(Class_Startup_variables)``

334.	``if not Message == None:``
335.	``¬ Message = "0.0.5- " + str(Message)``
336.	``¬ Startup.crash(Message)``
337.	``¬ ``
338.	``Message = Class_Startup_variables.mod_StartupAnimation__.GenerateStartupScreen.Start(Class_Startup_variables)``
339.	``if not Message == None:``
340.	``¬ Message = "0.0.6- " + str(Message)``
341.	``¬ Startup.crash(Message)``

342.	``Class_Startup_variables.Command = "Undefined"``
343.	``while True:``
344.	``¬ if Class_Startup_variables.Command == "saveANDexit":``
345.	``¬ ¬ Message = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.SaveTOconfigFILE(Class_Startup_variables)``
346.	``¬ ¬ if not Message == None:``
347.	``¬ ¬ ¬ Message = "0.0.7- " + str(Message)``
348.	``¬ ¬ ¬ Startup.crash(Message)``
349.	``¬ ¬ else:``
350.	``¬ ¬ ¬ Class_Startup_variables.Stop_Thread_Event.set()``

351.	``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.join()``
352.	``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.join()``
353.	``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.join()``
354.	``¬ ¬ ¬ ``
355.	``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
356.	``¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit("0.5.0- Thank you for playing") # 0 = Order of running, 5 = 5th occurrence down page``
357.	``¬ elif Class_Startup_variables.Command == "Credits":``
358.	``¬ ¬ Message = Class_Startup_variables.mod_Credits__.GenerateCredits.Credits(Class_Startup_variables)``
359.	``¬ ¬ if not Message == None:``
360.	``¬ ¬ ¬ Message = "0.0.8- " + str(Message)``
361.	``¬ ¬ ¬ Startup.crash(Message)``
362.	``¬ ¬ Class_Startup_variables.Command = "Undefined"``
363.	``¬ elif Class_Startup_variables.Command == "Achievements":``
364.	``¬ ¬ Message = Class_Startup_variables.mod_Achievements__.GenerateAchievements.Achievements(Class_Startup_variables)``
365.	``¬ ¬ if not Message == None:``
366.	``¬ ¬ ¬ Message = "0.0.9- " + str(Message)``
367.	``¬ ¬ ¬ Startup.crash(Message)``
368.	``¬ ¬ Class_Startup_variables.Command = "Undefined"``
369.	``¬ elif Class_Startup_variables.Command == "CharacterDesigner":``
370.	``¬ ¬ Message = Class_Startup_variables.mod_CharacterDesigner__.GenerateCharacterDesigner.CharacterDesigner(Class_Startup_variables)``
371.	``¬ ¬ if not Message == None:``
372.	``¬ ¬ ¬ Message = "0.0.10- " + str(Message)``
373.	``¬ ¬ ¬ Startup.crash(Message)``
374.	``¬ ¬ Class_Startup_variables.Command = "Undefined"``
375.	``¬ elif Class_Startup_variables.Command == "Settings":``
376.	``¬ ¬ Message = Class_Startup_variables.mod_Settings__.GenerateSettings.settings(Class_Startup_variables)``
377.	``¬ ¬ if not Message == None:``
378.	``¬ ¬ ¬ Message = "0.0.11- " + str(Message)``
379.	``¬ ¬ ¬ Startup.crash(Message)``
380.	``¬ ¬ Class_Startup_variables.Command = "Undefined"``
381.	``¬ elif Class_Startup_variables.Command == "Benchmark":``
382.	``¬ ¬ Message = Class_Startup_variables.mod_Benchmark__.GenerateBenchmarkMenu.Benchmark(Class_Startup_variables)``
383.	``¬ ¬ if not Message == None:``
384.	``¬ ¬ ¬ Message = "0.0.12- " + str(Message)``
385.	``¬ ¬ ¬ Startup.crash(Message)``
386.	``¬ ¬ Class_Startup_variables.Command = "Undefined"``
387.	``¬ elif Class_Startup_variables.Command == "Play":``
388.	``¬ ¬ Message = Class_Startup_variables.mod_MainGameEngine__.CreateEngine.Play(Class_Startup_variables)``
389.	``¬ ¬ if Message == None:``
390.	``¬ ¬ ¬ Message = Class_Startup_variables.GameError``
391.	``¬ ¬ if not Message == None:``
392.	``¬ ¬ ¬ Message = "0.0.13- " + str(Message)``
393.	``¬ ¬ ¬ Startup.crash(Message)``
394.	``¬ ¬ Class_Startup_variables.mod_Pygame__.init()``
395.	``¬ ¬ Class_Startup_variables.FromPlay = True``
396.	``¬ ¬ Message = Class_Startup_variables.mod_DisplayUtils__.DisplayUtils.SetDisplay(Class_Startup_variables)``
397.	``¬ ¬ if not Message == None:``
398.	``¬ ¬ ¬ Message = "0.0.14- " + str(Message)``
399.	``¬ ¬ ¬ Startup.crash(Message)``
400.	``¬ elif Class_Startup_variables.Command == "Inventory":``
401.	``¬ ¬ Message = Class_Startup_variables.mod_Inventory__.GenerateInventory.Inventory(Class_Startup_variables)``
402.	``¬ ¬ if not Message == None:``
403.	``¬ ¬ ¬ Message = "0.0.15- " + str(Message)``
404.	``¬ ¬ ¬ Startup.crash(Message)``
405.	``¬ ¬ Class_Startup_variables.Command = "Play"``
406.	``¬ elif Class_Startup_variables.Command == "MapGUI":``
407.	``¬ ¬ Message = Class_Startup_variables.mod_MapGUI__.GenerateMapGUI.MapGUI(Class_Startup_variables)``
408.	``¬ ¬ if not Message == None:``
409.	``¬ ¬ ¬ Message = "0.0.16- " + str(Message)``
410.	``¬ ¬ ¬ Startup.crash(Message)``
411.	``¬ ¬ Class_Startup_variables.Command = "Play"``
412.	``¬ else:``
413.	``¬ ¬ Message, Class_Startup_variables.Command = Class_Startup_variables.mod_HomeScreen__.GenerateHomeScreen.Home_Screen(Class_Startup_variables)``
414.	``¬ ¬ if not Message == None:``
415.	``¬ ¬ ¬ Message = "0.0.17- " + str(Message)``
416.	``¬ ¬ ¬ Startup.crash(Message)``


MapGUI
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_MapGUI>")``
    3.	``¬ class GenerateMapGUI:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def GetMapPos(self):``
7.	``¬ ¬ ¬ x = 0``
8.	``¬ ¬ ¬ z = 0``
9.	``¬ ¬ ¬ if self.X == 0:``
10.	``¬ ¬ ¬ ¬ x = 640``
11.	``¬ ¬ ¬ if self.Z == 0:``
12.	``¬ ¬ ¬ ¬ z = 360``
13.	``¬ ¬ ¬ x -= 6``
14.	``¬ ¬ ¬ z -= 19``
15.	``¬ ¬ ¬ return (x,z)``


16.	``¬ ¬ def MapGUI(self):``
17.	``¬ ¬ ¬ try:``
18.	``¬ ¬ ¬ ¬ Message = self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``
19.	``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
20.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``

21.	``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
22.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
23.	``¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png")))``
24.	``¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``
25.	``¬ ¬ ¬ ¬ MapIcon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Marker.jpg"))).convert()``
26.	``¬ ¬ ¬ ¬ zoom = 0``
27.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Playing | Map")``
28.	``¬ ¬ ¬ ¬ MouseUnlock = True``
29.	``¬ ¬ ¬ ¬ X,Y = 0, 0``
30.	``¬ ¬ ¬ ¬ key = ""``
31.	``¬ ¬ ¬ ¬ while True:``
32.	``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
33.	``¬ ¬ ¬ ¬ ¬ ``
34.	``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
35.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
36.	``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
37.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``
38.	``¬ ¬ ¬ ¬ ¬ ``
39.	``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
40.	``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
41.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_r):``
42.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Load3D = False``
43.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
44.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
45.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
46.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYDOWN:``
47.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE:``
48.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ zoom = 0``
49.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_w:``
50.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "w"``
51.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_s:``
52.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "s"``
53.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_d:``
54.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "d"``
55.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_a:``
56.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "a"``
57.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
58.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = self.mod_DisplayUtils__.DisplayUtils.UpdateOPENGLdisplay(self)``
59.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYUP:``
60.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ key = ""``
61.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEWHEEL:``
62.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if str(event.y)[0] == "-":``
63.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ zoom -= 1``
64.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
65.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ zoom += 1``
66.	``¬ ¬ ¬ ¬ ¬ if zoom >= 2:``
67.	``¬ ¬ ¬ ¬ ¬ ¬ zoom = 2``
68.	``¬ ¬ ¬ ¬ ¬ if zoom <= 0:``
69.	``¬ ¬ ¬ ¬ ¬ ¬ zoom = 0``
70.	``¬ ¬ ¬ ¬ ¬ if key == "w":``
71.	``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``
72.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y -= 5``
73.	``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
74.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y -= 10``
75.	``¬ ¬ ¬ ¬ ¬ if key == "s":``
76.	``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``
77.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y += 5``
78.	``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
79.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y += 10``
80.	``¬ ¬ ¬ ¬ ¬ if key == "d":``
81.	``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``
82.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ X += 5``
83.	``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
84.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ X += 10``
85.	``¬ ¬ ¬ ¬ ¬ if key == "a":``
86.	``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``
87.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ X -= 5``
88.	``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
89.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ X -= 10``
90.	``¬ ¬ ¬ ¬ ¬ if zoom == 0:``
91.	``¬ ¬ ¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((realWidth, realHeight),  self.mod_PIL_Image_.ANTIALIAS)``
92.	``¬ ¬ ¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``
93.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Map0, (0, 0))``
94.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MapIcon, GenerateMapGUI.GetMapPos(self))``
95.	``¬ ¬ ¬ ¬ ¬ ¬ x, y = 0, 0``
96.	``¬ ¬ ¬ ¬ ¬ elif zoom == 1:``
97.	``¬ ¬ ¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((int(realWidth*1.75), int(realHeight*1.75)),  self.mod_PIL_Image_.ANTIALIAS) ``
98.	``¬ ¬ ¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``
99.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Map0, (X,Y))``
100.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MapIcon, GenerateMapGUI.GetMapPos(self))``
101.	``¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
102.	``¬ ¬ ¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((int(realWidth*2), int(realHeight*2)),  self.mod_PIL_Image_.ANTIALIAS) ``
103.	``¬ ¬ ¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``
104.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Map0, (X,Y))``
105.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MapIcon, GenerateMapGUI.GetMapPos(self))``
106.	``¬ ¬ ¬ ¬ ¬ if zoom == 1:``
107.	``¬ ¬ ¬ ¬ ¬ ¬ if X <= -955:``
108.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -955``
109.	``¬ ¬ ¬ ¬ ¬ ¬ if Y <= -535:``
110.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -535``
111.	``¬ ¬ ¬ ¬ ¬ ¬ if X >= -5:``
112.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -5``
113.	``¬ ¬ ¬ ¬ ¬ ¬ if Y >= -5:``
114.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -5``
115.	``¬ ¬ ¬ ¬ ¬ if zoom == 2:``
116.	``¬ ¬ ¬ ¬ ¬ ¬ if X <= -1590:``
117.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -1590``
118.	``¬ ¬ ¬ ¬ ¬ ¬ if Y <= -890:``
119.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -890``
120.	``¬ ¬ ¬ ¬ ¬ ¬ if X >= -10:``
121.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -10``
122.	``¬ ¬ ¬ ¬ ¬ ¬ if Y >= -10:``
123.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -10``
124.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``
125.	``¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)``
126.	``¬ ¬ ¬ except Exception as Message:``
127.	``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
128.	``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    129.	``else:``
    130.	``¬ print("You need to run this as part of Pycraft")``
    131.	``¬ import tkinter as tk``
    132.	``¬ from tkinter import messagebox``
    133.	``¬ root = tk.Tk()``
    134.	``¬ root.withdraw()``
    135.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    136.	``¬ quit()``


OGLBenchmark
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_OGLBenchmark>")``
    3.	``¬ class LoadOGLBenchmark:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def Cube(self, edges, vertices):``
7.	``¬ ¬ ¬ self.mod_OpenGL_GL_.glBegin(self.mod_OpenGL_GL_.GL_LINES)``
8.	``¬ ¬ ¬ for edge in edges:``
9.	``¬ ¬ ¬ ¬ for vertex in edge:``
10.	``¬ ¬ ¬ ¬ ¬ self.mod_OpenGL_GL_.glVertex3fv(vertices[vertex])``
11.	``¬ ¬ ¬ self.mod_OpenGL_GL_.glEnd()``

12.	``¬ ¬ def CreateBenchmark(self):``
13.	``¬ ¬ ¬ self.mod_OpenGL_GLU_.gluPerspective(45, (1280/720), 0.1, 50.0)``
14.	``¬ ¬ ¬ self.mod_OpenGL_GL_.glTranslatef(0.0,0.0, -5)``

15.	``¬ ¬ def RunBenchmark(self, edges, vertices):``
16.	``¬ ¬ ¬ self.mod_OpenGL_GL_.glRotatef(1, 3, 1, 1)``
17.	``¬ ¬ ¬ self.mod_OpenGL_GL_.glClear(self.mod_OpenGL_GL_.GL_COLOR_BUFFER_BIT|self.mod_OpenGL_GL_.GL_DEPTH_BUFFER_BIT)``
18.	``¬ ¬ ¬ LoadOGLBenchmark.Cube(self, edges, vertices)``

.. note::
    For information on this consult the above guide
    19.	``else:``
    20.	``¬ print("You need to run this as part of Pycraft")``
    21.	``¬ import tkinter as tk``
    22.	``¬ from tkinter import messagebox``
    23.	``¬ root = tk.Tk()``
    24.	``¬ root.withdraw()``
    25.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    26.	``¬ quit()``


PycraftStartupTest
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_PycraftStartupTest>")``
    3.	``¬ class StartupTest:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def PycraftSelfTest(self):``
7.	``¬ ¬ ¬ try:``
8.	``¬ ¬ ¬ ¬ import OpenGL.GL as gl``
9.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_mode((1280, 720), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL|self.mod_Pygame__.HIDDEN)``

10.	``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
11.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``

12.	``¬ ¬ ¬ ¬ OpenGLversion = str(gl.glGetString(gl.GL_VERSION))[2:5]``
13.	``¬ ¬ ¬ ¬ SDLversion = self.mod_Pygame__.get_sdl_version()[0]``
14.	``¬ ¬ ¬ ¬ RAM = (((self.mod_Psutil__.virtual_memory().available)/1000)/1000) # expressed in MB``

15.	``¬ ¬ ¬ ¬ if float(OpenGLversion) < 2.8:``
16.	``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``
17.	``¬ ¬ ¬ ¬ ¬ root.withdraw()``
18.	``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showerror("Invalid OpenGL version", f"OpenGL version: {OpenGLversion} is not supported; try a version greater than 2.7")``
19.	``¬ ¬ ¬ ¬ ¬ quit()``
20.	``¬ ¬ ¬ ¬ if SDLversion < 2:``
21.	``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``
22.	``¬ ¬ ¬ ¬ ¬ root.withdraw()``
23.	``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showerror("Invalid SDL version", f"SDL version: {SDLversion} is not supported; try a version greater than or equal to 2")``
24.	``¬ ¬ ¬ ¬ ¬ quit()``
25.	``¬ ¬ ¬ ¬ if RAM < 100:``
26.	``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``
27.	``¬ ¬ ¬ ¬ ¬ root.withdraw()``
28.	``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showerror("Minimum system requirements not met", f"Your system does not meet the minimum 100mb free memory specification needed to play this game")``
29.	``¬ ¬ ¬ ¬ ¬ quit()``
30.	``¬ ¬ ¬ ¬ if RAM < 200:``
31.	``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``
32.	``¬ ¬ ¬ ¬ ¬ root.withdraw()``
33.	``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showwarning("Recommended system requirements not met", f"Your system's free memory does not meet the requirement recommended to play this game (200mb), you are still able to, however your experience may not be satisfactory")``
34.	``¬ ¬ ¬ ¬ ¬ from PIL import Image, ImageTk, ImageGrab``
35.	``¬ ¬ ¬ ¬ ¬ import OpenGL.GL``
36.	``¬ ¬ ¬ ¬ ¬ ``
37.	``¬ ¬ ¬ ¬ if self.mod_Sys__.platform == "win32" or self.mod_Sys__.platform == "win64":``
38.	``¬ ¬ ¬ ¬ ¬ self.mod_OS__.environ["SDL_VIDEO_CENTERED"] = "1"``

39.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
40.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.init()``

41.	``¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``

42.	``¬ ¬ ¬ ¬ current_time = self.mod_Datetime__.datetime.now()``
43.	``¬ ¬ ¬ ¬ currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"``
44.	``¬ ¬ ¬ ¬ if not currentDate == self.lastRun or self.crash == True:``
45.	``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
46.	``¬ ¬ ¬ ¬ ¬ yScaleFact = realHeight/720``
47.	``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``
48.	``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
49.	``¬ ¬ ¬ ¬ ¬ TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
50.	``¬ ¬ ¬ ¬ ¬ Title = TitleFont.render("Pycraft", True, self.FontCol)``
51.	``¬ ¬ ¬ ¬ ¬ TitleWidth = Title.get_width()``
52.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Title, ((realWidth-TitleWidth)/2, 0))``
53.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
54.	``¬ ¬ ¬ ¬ ¬ defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] ``
55.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2)``
56.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
57.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
58.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
59.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
60.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
61.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
62.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
63.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
64.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
65.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
66.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
67.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
68.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
69.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
70.	``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
71.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
72.	``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Error_Resources\\Error_Message.png"))).convert()``
73.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
74.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) ``
75.	``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Error_Resources\\Icon.jpg"))).convert()``
76.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
77.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
78.	``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Folder_Resources\\FolderIcon.ico"))).convert()``
79.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
80.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
81.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
82.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
83.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
84.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
85.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
86.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``
87.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
88.	``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg"))).convert()``
89.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
90.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
91.	``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg"))).convert()``
92.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
93.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
94.	``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg"))).convert()``
95.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
96.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
97.	``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg"))).convert()``
98.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
99.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
100.	``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg"))).convert()``
101.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
102.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
103.	``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg"))).convert()``
104.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
105.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
106.	``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, f"Resources\\General_Resources\\selectorICONlight.jpg")).convert()``
107.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
108.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
109.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
110.	``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, f"Resources\\General_Resources\\selectorICONdark.jpg")).convert()``
111.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
112.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
113.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
114.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\InventoryGeneral.wav")))``
115.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
116.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
117.	``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``
118.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
119.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
120.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
121.	``¬ ¬ ¬ ¬ else:``
122.	``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
123.	``¬ ¬ ¬ ¬ ¬ TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
124.	``¬ ¬ ¬ ¬ ¬ Title = TitleFont.render("Pycraft", True, self.FontCol)``
125.	``¬ ¬ ¬ ¬ ¬ TitleWidth = Title.get_width()``
126.	``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
127.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Title, ((realWidth-TitleWidth)/2, 0))``
128.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
129.	``¬ ¬ ¬ ¬ ¬ ``
130.	``¬ ¬ ¬ ¬ ¬ yScaleFact = realHeight/720``
131.	``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``
132.	``¬ ¬ ¬ ¬ ¬ defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] ``
133.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2) ``
134.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
135.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
136.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
137.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
138.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
139.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
140.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
141.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
142.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
143.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
144.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
145.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) ``
146.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
147.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
148.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
149.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
150.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
151.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
152.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) ``
153.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
154.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
155.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
156.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
157.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) ``
158.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) ``
159.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) ``
160.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) ``
161.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) ``
162.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) ``
163.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
164.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
165.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (575*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
166.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``
167.	``¬ ¬ ¬ except Exception as Message:``
168.	``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    169.	``else:``
    170.	``¬ print("You need to run this as part of Pycraft")``
    171.	``¬ import tkinter as tk``
    172.	``¬ from tkinter import messagebox``
    173.	``¬ root = tk.Tk()``
    174.	``¬ root.withdraw()``
    175.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    176.	``¬ quit()``


Settings
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_Settings>")``
    3.	``¬ class GenerateSettings:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def settings(self):``
7.	``¬ ¬ ¬ try:``
8.	``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
9.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
10.	``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Settings")``
11.	``¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
12.	``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
13.	``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
14.	``¬ ¬ ¬ ¬ LOWFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
15.	``¬ ¬ ¬ ¬ MEDIUMFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
16.	``¬ ¬ ¬ ¬ HIGHFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
17.	``¬ ¬ ¬ ¬ ADAPTIVEFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
18.	``¬ ¬ ¬ ¬ LightThemeFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
19.	``¬ ¬ ¬ ¬ DarkThemeFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
20.	``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

21.	``¬ ¬ ¬ ¬ TempMx = 0``
22.	``¬ ¬ ¬ ¬ Mx, My = 0, 0``
23.	``¬ ¬ ¬ ¬ mousebuttondown = False``

24.	``¬ ¬ ¬ ¬ SettingsInformationFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

25.	``¬ ¬ ¬ ¬ scroll = 50``

26.	``¬ ¬ ¬ ¬ while True:``
27.	``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

28.	``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
29.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
30.	``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
31.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

32.	``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``

33.	``¬ ¬ ¬ ¬ ¬ TempMx = Mx``
34.	``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``
35.	``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``
36.	``¬ ¬ ¬ ¬ ¬ Mx, My = self.mod_Pygame__.mouse.get_pos()``
37.	``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
38.	``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``
39.	``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
40.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``
41.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
42.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
43.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
44.	``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:``
45.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:``
46.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``
47.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``
48.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``
49.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
50.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
51.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
52.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
53.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x: ``
54.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1 ``
55.	``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.MOUSEBUTTONDOWN: ``
56.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True ``
57.	``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.MOUSEBUTTONUP: ``
58.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
59.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEWHEEL and realHeight <= 760:``
60.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_SIZENS)``
61.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if str(event.y)[0] == "-":``
62.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ scroll -= 5``
63.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
64.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ scroll += 5``
65.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
66.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_ARROW)``

67.	``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Settings")``

68.	``¬ ¬ ¬ ¬ ¬ if scroll > 35:``
69.	``¬ ¬ ¬ ¬ ¬ ¬ scroll = 35``
70.	``¬ ¬ ¬ ¬ ¬ elif scroll < 0:``
71.	``¬ ¬ ¬ ¬ ¬ ¬ scroll = 0``

72.	``¬ ¬ ¬ ¬ ¬ titletFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
73.	``¬ ¬ ¬ ¬ ¬ TitleWidth = titletFont.get_width()``

74.	``¬ ¬ ¬ ¬ ¬ InfoFont = InfoTitleFont.render("Settings", self.aa, self.SecondFontCol)``

75.	``¬ ¬ ¬ ¬ ¬ FPSFont = VersionFont.render(f"FPS: Actual: {int(self.eFPS)} Max: {int(self.FPS)} Average: {int((self.aFPS/self.Iteration))}", self.aa, self.FontCol)``
76.	``¬ ¬ ¬ ¬ ¬ FOVFont = VersionFont.render(f"FOV: {self.FOV}", self.aa, self.FontCol)``
77.	``¬ ¬ ¬ ¬ ¬ CamRotFont = VersionFont.render(f"Camera Rotation Speed: {round(self.cameraANGspeed, 1)}", self.aa, self.FontCol) ``
78.	``¬ ¬ ¬ ¬ ¬ ModeFont = VersionFont.render("Mode;¬ ¬  ,¬ ¬ ¬ ¬  ,¬ ¬ ¬ ,¬ ¬   .", self.aa, self.FontCol) ``
79.	``¬ ¬ ¬ ¬ ¬ AAFont = VersionFont.render(f"Anti-Aliasing: {self.aa}", self.aa, self.FontCol) ``
80.	``¬ ¬ ¬ ¬ ¬ RenderFogFont = VersionFont.render(f"Render Fog: {self.RenderFOG}", self.aa, self.FontCol)``
81.	``¬ ¬ ¬ ¬ ¬ FancySkyFont = VersionFont.render(f"Fancy Skies: {self.FanSky}", self.aa, self.FontCol)``
82.	``¬ ¬ ¬ ¬ ¬ FancyParticleFont = VersionFont.render(f"Fancy Partices: {self.FanPart}", self.aa, self.FontCol)``
83.	``¬ ¬ ¬ ¬ ¬ SoundFont = VersionFont.render(f"Sound: {self.sound}", self.aa, self.FontCol)``
84.	``¬ ¬ ¬ ¬ ¬ if self.sound == True:``
85.	``¬ ¬ ¬ ¬ ¬ ¬ SoundVoltFont = VersionFont.render(f"Sound Volume: {self.soundVOL}%", self.aa, self.FontCol)``
86.	``¬ ¬ ¬ ¬ ¬ else:``
87.	``¬ ¬ ¬ ¬ ¬ ¬ SoundVoltFont = VersionFont.render(f"Sound Volume: {self.soundVOL}%", self.aa, self.ShapeCol)``
88.	``¬ ¬ ¬ ¬ ¬ MusicFont = VersionFont.render(f"Music: {self.music}", self.aa, self.FontCol)``
89.	``¬ ¬ ¬ ¬ ¬ if self.music == True:``
90.	``¬ ¬ ¬ ¬ ¬ ¬ MusicVoltFont = VersionFont.render(f"Music Volume: {self.musicVOL}%", self.aa, self.FontCol)``
91.	``¬ ¬ ¬ ¬ ¬ else:``
92.	``¬ ¬ ¬ ¬ ¬ ¬ MusicVoltFont = VersionFont.render(f"Music Volume: {self.musicVOL}%", self.aa, self.ShapeCol)``
93.	``¬ ¬ ¬ ¬ ¬ ThemeFont = VersionFont.render(f"Theme:¬ ¬   ,¬ ¬   | Current Theme: {self.theme}", self.aa, self.FontCol)``
94.	``¬ ¬ ¬ ¬ ¬ ThemeInformationFont = SettingsInformationFont.render("Gives you control over which theme you can use", self.aa, self.AccentCol)``
95.	``¬ ¬ ¬ ¬ ¬ ModeInformationFont = SettingsInformationFont.render("Gives you 4 separate per-sets for settings, Adaptive mode will automatically adjust your settings", self.aa, self.AccentCol)``
96.	``¬ ¬ ¬ ¬ ¬ FPSInformationFont = SettingsInformationFont.render("Controls the maximum frame rate the game will limit to, does not guarantee that FPS unfortunately", self.aa, self.AccentCol)``
97.	``¬ ¬ ¬ ¬ ¬ FOVInformationFont = SettingsInformationFont.render("Controls the FOV of the camera in-game", self.aa, self.AccentCol)``
98.	``¬ ¬ ¬ ¬ ¬ CameraRotationSpeedInformationFont = SettingsInformationFont.render("Controls the rotation speed of the camera in-game (1 is low, 5 is high)", self.aa, self.AccentCol)``
99.	``¬ ¬ ¬ ¬ ¬ AAInformationFont = SettingsInformationFont.render("Enables/Disables anti-aliasing in game and in the GUI, will give you a minor performance improvement, mainly for low powered devices", self.aa, self.AccentCol)``
100.	``¬ ¬ ¬ ¬ ¬ self.RenderFogInformationFont = SettingsInformationFont.render("Enables/Disables fog effects in game, for a small performance benefit", self.aa, self.AccentCol)``
101.	``¬ ¬ ¬ ¬ ¬ FancySkiesInformationFont = SettingsInformationFont.render("Enables/Disables a fancy sky box for better visuals in game, does not control anti aliasing for the sky box", self.aa, self.AccentCol)``
102.	``¬ ¬ ¬ ¬ ¬ FancyParticlesInformationFont = SettingsInformationFont.render("Enables/Disables particles in game as particles can have a significant performance decrease", self.aa, self.AccentCol)``
103.	``¬ ¬ ¬ ¬ ¬ SoundInformationFont = SettingsInformationFont.render("Enables/Disables sound effects in game, like for example the click sound and footsteps in game", self.aa, self.AccentCol)``
104.	``¬ ¬ ¬ ¬ ¬ SoundVolInformationFont = SettingsInformationFont.render("Controls the volume of the sound effects, where 100% is maximum and 0% is minimum volume", self.aa, self.AccentCol)``
105.	``¬ ¬ ¬ ¬ ¬ MusicInformationFont = SettingsInformationFont.render("Enables/Disables music in game, like for example the GUI music", self.aa, self.AccentCol)``
106.	``¬ ¬ ¬ ¬ ¬ MusicVolInformationFont = SettingsInformationFont.render("Controls the volume of the music, some effects may not apply until the game reloads", self.aa, self.AccentCol)``
107.	``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
108.	``¬ ¬ ¬ ¬ ¬ FPS_rect = self.mod_Pygame__.Rect(50, 180+scroll, 450*xScaleFact, 10)``
109.	``¬ ¬ ¬ ¬ ¬ FOV_rect = self.mod_Pygame__.Rect(50, 230+scroll, 450*xScaleFact, 10)``
110.	``¬ ¬ ¬ ¬ ¬ CAM_rect = self.mod_Pygame__.Rect(50, 280+scroll, 450*xScaleFact, 10)``
111.	``¬ ¬ ¬ ¬ ¬ sound_rect = self.mod_Pygame__.Rect(50, 580+scroll, 450*xScaleFact, 10)``
112.	``¬ ¬ ¬ ¬ ¬ music_rect = self.mod_Pygame__.Rect(50, 680+scroll, 450*xScaleFact, 10)``
113.	``¬ ¬ ¬ ¬ ¬ aa_rect = self.mod_Pygame__.Rect(50, 330+scroll, 50, 10)``
114.	``¬ ¬ ¬ ¬ ¬ RenderFOG_Rect = self.mod_Pygame__.Rect(50, 380+scroll, 50, 10)``
115.	``¬ ¬ ¬ ¬ ¬ Fansky_Rect = self.mod_Pygame__.Rect(50, 430+scroll, 50, 10)``
116.	``¬ ¬ ¬ ¬ ¬ FanPart_Rect = self.mod_Pygame__.Rect(50, 480+scroll, 50, 10)``
117.	``¬ ¬ ¬ ¬ ¬ sound_Rect = self.mod_Pygame__.Rect(50, 530+scroll, 50, 10)``
118.	``¬ ¬ ¬ ¬ ¬ music_Rect = self.mod_Pygame__.Rect(50, 630+scroll, 50, 10)``
119.	``¬ ¬ ¬ ¬ ¬ slider_Rect = self.mod_Pygame__.Rect(realWidth-15, scroll, 10, 665)``
120.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FPS_rect, 0)``
121.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FOV_rect, 0)``
122.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, CAM_rect, 0)``
123.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, sound_rect, 0)``
124.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, music_rect, 0)``
125.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, aa_rect, 0)``
126.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, RenderFOG_Rect, 0)``
127.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, Fansky_Rect, 0)``
128.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FanPart_Rect, 0)``
129.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, sound_Rect, 0)``
130.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, music_Rect, 0)``
131.	``¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
132.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 180+scroll and My < 190+scroll:``
133.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
134.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.FPS < 445: ``
135.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS += 1``
136.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.FPS > 15: ``
137.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS -= 1``
138.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FPS < 15:``
139.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 16``
140.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FPS > 445:``
141.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 444``
142.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (int(self.FPS+45)*xScaleFact, 185+scroll), 9)``
143.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
144.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (int(self.FPS+45)*xScaleFact, 185+scroll), 9)``

145.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 230+scroll and My < 240+scroll:``
146.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
147.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.FOV < 98:``
148.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV += 1``
149.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.FOV > 12:``
150.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV -= 1``
151.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FOV < 12:``
152.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV = 13``
153.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FOV > 98:``
154.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV = 97``
155.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (int(self.FOV*5)*xScaleFact, 235+scroll), 9)``
156.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
157.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (int(self.FOV*5)*xScaleFact, 235+scroll), 9)``

158.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 280+scroll and My < 290+scroll:``
159.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
160.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.cameraANGspeed < 5.0:``
161.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed += 0.1``
162.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.cameraANGspeed > 0.0:``
163.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed -= 0.1``
164.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.cameraANGspeed > 5.0:``
165.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed = 4.9``
166.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.cameraANGspeed <= 0:``
167.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed = 0.1``
168.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)``
169.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
170.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)``

171.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 580+scroll and My < 590+scroll and self.sound == True:``
172.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
173.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.soundVOL < 100:``
174.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL += 1``
175.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.soundVOL > 0:``
176.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL -= 1``
177.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.soundVOL > 100:``
178.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL = 100``
179.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.soundVOL < 0:``
180.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL = 0``
181.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)``
182.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
183.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)``

184.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 680+scroll and My < 690+scroll and self.music == True: ``
185.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
186.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.musicVOL < 100:``
187.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL += 1``
188.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.musicVOL > 0:``
189.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL -= 1``
190.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.musicVOL > 100:``
191.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL = 100``
192.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.musicVOL < 0:``
193.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL = 0``
194.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)``
195.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
196.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)``

197.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 330+scroll and My < 340+scroll:``
198.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
199.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True: ``
200.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False ``
201.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
202.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
203.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
204.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False: ``
205.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True ``
206.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
207.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
208.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
209.	``¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True: ``
210.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 335+scroll), 9)``
211.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 335+scroll), 6)``
212.	``¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False: ``
213.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 335+scroll), 9)``
214.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 335+scroll), 6)``

215.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 380+scroll and My < 390+scroll:``
216.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
217.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``
218.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = False``
219.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
220.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
221.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
222.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``
223.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = True``
224.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
225.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
226.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
227.	``¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``
228.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 385+scroll), 9)``
229.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 385+scroll), 6)``
230.	``¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``
231.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 385+scroll), 9)``
232.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 385+scroll), 6)``

233.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 430+scroll and My < 440+scroll:``
234.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
235.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``
236.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = False``
237.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
238.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
239.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
240.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``
241.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
242.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
243.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
244.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
245.	``¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``
246.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 435+scroll), 9)``
247.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 435+scroll), 6)``
248.	``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``
249.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 435+scroll), 9)``
250.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 435+scroll), 6)``

251.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 480+scroll and My < 490+scroll:``
252.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
253.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``
254.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
255.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
256.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
257.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
258.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``
259.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = True``
260.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
261.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
262.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
263.	``¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``
264.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 485+scroll), 9)``
265.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 485+scroll), 6)``
266.	``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``
267.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 485+scroll), 9)``
268.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 485+scroll), 6)``

269.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 530+scroll and My < 540+scroll:``
270.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
271.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
272.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.sound = False``
273.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
274.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
275.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
276.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``
277.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.sound = True``
278.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
279.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
280.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
281.	``¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
282.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 535+scroll), 9)``
283.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 535+scroll), 6)``
284.	``¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``
285.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 535+scroll), 9)``
286.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 535+scroll), 6)``

287.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 630+scroll and My < 640+scroll:``
288.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
289.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``
290.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.music = False``
291.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).stop()``
292.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
293.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
294.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
295.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``
296.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.LoadMusic = True``
297.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.music = True``
298.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
299.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
300.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
301.	``¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``
302.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 635+scroll), 9)``
303.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 635+scroll), 6)``
304.	``¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``
305.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 635+scroll), 9)``
306.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 635+scroll), 6)``
307.	``¬ ¬ ¬ ¬ ¬ else:``
308.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)``
309.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.FPS+45)*xScaleFact), 185+scroll), 9)``
310.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)``
311.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.FOV*5))*xScaleFact, 235+scroll), 9)``
312.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)``

313.	``¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True: ``
314.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 335+scroll), 9)``
315.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 335+scroll), 6)``
316.	``¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False: ``
317.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 335+scroll), 9)``
318.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 335+scroll), 6)``

319.	``¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``
320.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 385+scroll), 9)``
321.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 385+scroll), 6)``
322.	``¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``
323.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 385+scroll), 9)``
324.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 385+scroll), 6)``

325.	``¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``
326.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 435+scroll), 9)``
327.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 435+scroll), 6)``
328.	``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``
329.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 435+scroll), 9)``
330.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 435+scroll), 6)``

331.	``¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``
332.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 485+scroll), 9)``
333.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 485+scroll), 6)``
334.	``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``
335.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 485+scroll), 9)``
336.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 485+scroll), 6)``

337.	``¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
338.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 535+scroll), 9)``
339.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 535+scroll), 6)``
340.	``¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``
341.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 535+scroll), 9)``
342.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 535+scroll), 6)``

343.	``¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``
344.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 635+scroll), 9)``
345.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 635+scroll), 6)``
346.	``¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``
347.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 635+scroll), 9)``
348.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 635+scroll), 6)``

349.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 330+scroll and My < 340+scroll:``
350.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
351.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(AAInformationFont, (120, 325+scroll))``
352.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True:``
353.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 335+scroll), 9)``
354.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 335+scroll), 6)``
355.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False:``
356.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 335+scroll), 9)``
357.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 335+scroll), 6)``

358.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 380+scroll and My < 390+scroll:``
359.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
360.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(self.RenderFogInformationFont, (120, 375+scroll))``
361.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``
362.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 385+scroll), 9)``
363.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 385+scroll), 6)``
364.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``
365.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 385+scroll), 9)``
366.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 385+scroll), 6)``

367.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 430+scroll and My < 440+scroll:``
368.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
369.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FancySkiesInformationFont, (120, 425+scroll))``
370.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``
371.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 435+scroll), 9)``
372.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 435+scroll), 6)``
373.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``
374.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 435+scroll), 9)``
375.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 435+scroll), 6)``

376.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 480+scroll and My < 490+scroll:``
377.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FancyParticlesInformationFont, (120, 475+scroll))``
378.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
379.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``
380.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 485+scroll), 9)``
381.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 485+scroll), 6)``
382.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``
383.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 485+scroll), 9)``
384.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 485+scroll), 6)``

385.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 530+scroll and My < 540+scroll:``
386.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundInformationFont, (120, 525+scroll))``
387.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
388.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
389.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 535+scroll), 9)``
390.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 535+scroll), 6)``
391.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``
392.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 535+scroll), 9)``
393.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 535+scroll), 6)``

394.	``¬ ¬ ¬ ¬ ¬ ¬ if My > 630+scroll and My < 640+scroll:``
395.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
396.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicInformationFont, (120, 625+scroll))``
397.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``
398.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 635+scroll), 9)``
399.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 635+scroll), 6)``
400.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``
401.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 635+scroll), 9)``
402.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 635+scroll), 6)``

403.	``¬ ¬ ¬ ¬ ¬ if My >= 65+scroll and My <= 75+scroll:``
404.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
405.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(ThemeInformationFont, (300, 67+scroll))``

406.	``¬ ¬ ¬ ¬ ¬ if My >= 65+scroll and My <= 75+scroll and Mx >= 55 and Mx <= 95:``
407.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
408.	``¬ ¬ ¬ ¬ ¬ ¬ LightTheme = LightThemeFont.render("Light", self.aa, self.AccentCol)``
409.	``¬ ¬ ¬ ¬ ¬ ¬ LightThemeFont.set_underline(True)``
410.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
411.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "light"``
412.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = self.mod_ThemeUtils__.DetermineThemeColours.GetColours(self)``
413.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:``
414.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = "1.8- " + str(Message)``
415.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message``
416.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
417.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
418.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
419.	``¬ ¬ ¬ ¬ ¬ else:``
420.	``¬ ¬ ¬ ¬ ¬ ¬ LightTheme = LightThemeFont.render("Light", self.aa, self.FontCol)``
421.	``¬ ¬ ¬ ¬ ¬ ¬ LightThemeFont.set_underline(False)``

422.	``¬ ¬ ¬ ¬ ¬ if My >= 65+scroll and My <= 75+scroll and Mx >= 95 and Mx <= 135:``
423.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
424.	``¬ ¬ ¬ ¬ ¬ ¬ DarkTheme = DarkThemeFont.render("Dark", self.aa, self.AccentCol)``
425.	``¬ ¬ ¬ ¬ ¬ ¬ DarkThemeFont.set_underline(True)``
426.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
427.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "dark"``
428.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = self.mod_ThemeUtils__.DetermineThemeColours.GetColours(self)``
429.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:``
430.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = "1.8- " + str(Message)``
431.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message``
432.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
433.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
434.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
435.	``¬ ¬ ¬ ¬ ¬ else:``
436.	``¬ ¬ ¬ ¬ ¬ ¬ DarkTheme = DarkThemeFont.render("Dark", self.aa, self.FontCol)``
437.	``¬ ¬ ¬ ¬ ¬ ¬ DarkThemeFont.set_underline(False)``

438.	``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll:``
439.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
440.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(ModeInformationFont, (300, 85+scroll))``

441.	``¬ ¬ ¬ ¬ ¬ if My > 680+scroll and My < 690+scroll:``
442.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
443.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicVolInformationFont, (520*xScaleFact, 675+scroll))``

444.	``¬ ¬ ¬ ¬ ¬ if My > 580+scroll and My < 590+scroll:``
445.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
446.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundVolInformationFont, (520*xScaleFact, 575+scroll))``

447.	``¬ ¬ ¬ ¬ ¬ if My > 280+scroll and My < 290+scroll:``
448.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
449.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CameraRotationSpeedInformationFont, (520*xScaleFact, 275+scroll))``

450.	``¬ ¬ ¬ ¬ ¬ if My > 230+scroll and My < 240+scroll:``
451.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
452.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FOVInformationFont, (520*xScaleFact, 225+scroll))``

453.	``¬ ¬ ¬ ¬ ¬ if My > 180+scroll and My < 190+scroll:``
454.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
455.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSInformationFont, (520*xScaleFact, 175+scroll))``

456.	``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 40 and Mx <= 80:``
457.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
458.	``¬ ¬ ¬ ¬ ¬ ¬ LOWtFont = LOWFont.render("Low", self.aa, self.AccentCol)``
459.	``¬ ¬ ¬ ¬ ¬ ¬ LOWFont.set_underline(True)``
460.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
461.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "Low"``
462.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 15``
463.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``
464.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = False``
465.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = False``
466.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
467.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
468.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
469.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
470.	``¬ ¬ ¬ ¬ ¬ else:``
471.	``¬ ¬ ¬ ¬ ¬ ¬ LOWtFont = LOWFont.render("Low", self.aa, self.FontCol)``
472.	``¬ ¬ ¬ ¬ ¬ ¬ LOWFont.set_underline(False)``

473.	``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 90 and Mx <= 155:``
474.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
475.	``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMtFont = MEDIUMFont.render("Medium", self.aa, self.AccentCol)``
476.	``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMFont.set_underline(True)``
477.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
478.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "Medium"``
479.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 30``
480.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``
481.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = False``
482.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
483.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
484.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
485.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
486.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
487.	``¬ ¬ ¬ ¬ ¬ else:``
488.	``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMtFont = MEDIUMFont.render("Medium", self.aa, self.FontCol)``
489.	``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMFont.set_underline(False)``

490.	``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 165 and Mx <= 205:``
491.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
492.	``¬ ¬ ¬ ¬ ¬ ¬ HIGHFontText = HIGHFont.render("High", self.aa, self.AccentCol)``
493.	``¬ ¬ ¬ ¬ ¬ ¬ HIGHFont.set_underline(True)``
494.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
495.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "High"``
496.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 60``
497.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``
498.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = True``
499.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
500.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = True``
501.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
502.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
503.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
504.	``¬ ¬ ¬ ¬ ¬ else:``
505.	``¬ ¬ ¬ ¬ ¬ ¬ HIGHFontText = HIGHFont.render("High", self.aa, self.FontCol)``
506.	``¬ ¬ ¬ ¬ ¬ ¬ HIGHFont.set_underline(False)``

507.	``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 215 and Mx <= 300:``
508.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
509.	``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEtFont = ADAPTIVEFont.render("Adaptive", self.aa, self.AccentCol)``
510.	``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEFont.set_underline(True)``
511.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
512.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "Adaptive"``
513.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = (self.mod_Psutil__.cpu_freq(percpu=True)[0][2])/35``
514.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if (self.mod_Psutil__.cpu_freq(percpu=True)[0][2])/10 > 300 and self.mod_Psutil__.virtual_memory().total > 8589934592:``
515.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``
516.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = True``
517.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
518.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = True``
519.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif (self.mod_Psutil__.cpu_freq(percpu=True)[0][2]) > 200 and self.mod_Psutil__.virtual_memory().total > 4294967296:``
520.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``
521.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = True``
522.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
523.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
524.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif (self.mod_Psutil__.cpu_freq(percpu=True)[0][2]) > 100 and self.mod_Psutil__.virtual_memory().total > 2147483648:``
525.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``
526.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = False``
527.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
528.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
529.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif (self.mod_Psutil__.cpu.freq(percpu=True)[0][2]) < 100 and (self.mod_Psutil__.cpu.freq(percpu=True)[0][2]) > 75 and self.mod_Psutil__.virtual_memory().total > 1073741824:``
530.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``
531.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = False``
532.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = False``
533.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
534.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
535.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
536.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
537.	``¬ ¬ ¬ ¬ ¬ else:``
538.	``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEtFont = ADAPTIVEFont.render("Adaptive", self.aa, self.FontCol)``
539.	``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEFont.set_underline(False)``

540.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSFont, (0, 150+scroll))``
541.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(FOVFont, (0, 200+scroll))``
542.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(CamRotFont, (0, 250+scroll))``
543.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(ModeFont, (0, 85+scroll)) ``
544.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(LOWtFont, (48, 85+scroll))``
545.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(MEDIUMtFont, (90, 85+scroll))``
546.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(HIGHFontText, (165, 85+scroll))``
547.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(ADAPTIVEtFont, (215, 85+scroll)) ``
548.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(AAFont, (0, 300+scroll))``
549.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(RenderFogFont, (0, 350+scroll))``
550.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(FancySkyFont, (0, 400+scroll))``
551.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(FancyParticleFont, (0, 450+scroll))``
552.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundFont, (0, 500+scroll))``
553.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundVoltFont, (0, 550+scroll))``
554.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicFont, (0, 600+scroll))``
555.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicVoltFont, (0, 650+scroll))``
556.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(ThemeFont, (0, 65+scroll))``
557.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(LightTheme, (55, 65+scroll))``
558.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(DarkTheme, (95, 65+scroll))``
559.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (int(self.FPS+45)*xScaleFact, 185+scroll), 6)``
560.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (int(self.FOV*5)*xScaleFact, 235+scroll), 6)``
561.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 6)``
562.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 6)``
563.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 6)``
564.	``¬ ¬ ¬ ¬ ¬ ``
565.	``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 100)``
566.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
567.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(titletFont, ((realWidth-TitleWidth)/2, 0))``
568.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont, (((realWidth-TitleWidth)/2)+55, 50))``


569.	``¬ ¬ ¬ ¬ ¬ if realHeight <= 760:``
570.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, slider_Rect, 0)``
571.	``¬ ¬ ¬ ¬ ¬ else:``
572.	``¬ ¬ ¬ ¬ ¬ ¬ scroll = 50``

573.	``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
574.	``¬ ¬ ¬ ¬ ¬ if not Message == None:``
575.	``¬ ¬ ¬ ¬ ¬ ¬ return Message``

576.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip() ``
577.	``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
578.	``¬ ¬ ¬ except Exception as Message:``
579.	``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
580.	``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    581.	``else:``
    582.	``¬ print("You need to run this as part of Pycraft")``
    583.	``¬ import tkinter as tk``
    584.	``¬ from tkinter import messagebox``
    585.	``¬ root = tk.Tk()``
    586.	``¬ root.withdraw()``
    587.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    588.	``¬ quit()``


ShareDataUtil
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_ShareDataUtil>")``
    3.	``¬ class Share:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

    6.	``¬ ¬ def initialize(Data): ``
    7.	``¬ ¬ ¬ global Class_Startup_variables``
    8.	``¬ ¬ ¬ Class_Startup_variables = Data``


SoundUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_SoundUtils>")``
    3.	``¬ class PlaySound:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def PlayClickSound(self):``
7.	``¬ ¬ ¬ channel1 = self.mod_Pygame__.mixer.Channel(0)``
8.	``¬ ¬ ¬ clickMUSIC = self.mod_Pygame__.mixer.Sound(file=self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``
9.	``¬ ¬ ¬ channel1.set_volume(self.soundVOL/100)``
10.	``¬ ¬ ¬ channel1.play(clickMUSIC)``
11.	``¬ ¬ ¬ self.mod_Pygame__.time.wait(40)``

12.	``¬ ¬ def PlayFootstepsSound(self):``
13.	``¬ ¬ ¬ channel2 = self.mod_Pygame__.mixer.Channel(1)``
14.	``¬ ¬ ¬ Footsteps = self.mod_Pygame__.mixer.Sound(self.mod_OS__.path.join(self.base_folder, (f"Resources\\G3_Resources\\GameSounds\\footsteps{self.mod_Random__.randint(0, 5)}.wav")))``
15.	``¬ ¬ ¬ channel2.set_volume(self.soundVOL/100)``
16.	``¬ ¬ ¬ channel2.play(Footsteps)``


17.	``¬ ¬ def PlayInvSound(self):``
18.	``¬ ¬ ¬ channel3 = self.mod_Pygame__.mixer.Channel(2)``
19.	``¬ ¬ ¬ InvGen = self.mod_Pygame__.mixer.Sound(file=self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\InventoryGeneral.wav")))``
20.	``¬ ¬ ¬ channel3.set_volume(self.musicVOL/100)``
21.	``¬ ¬ ¬ channel3.play(InvGen)``


22.	``¬ ¬ def PlayAmbientSound(self):``
23.	``¬ ¬ ¬ channel4 = self.mod_Pygame__.mixer.Channel(3)``
24.	``¬ ¬ ¬ LoadAmb = self.mod_Pygame__.mixer.Sound(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\GameSounds\\FieldAmb.wav")))``
25.	``¬ ¬ ¬ channel4.set_volume(self.soundVOL/100)``
26.	``¬ ¬ ¬ channel4.play(LoadAmb)``

.. note::
    For information on this consult the above guide
    27.	``else:``
    28.	``¬ print("You need to run this as part of Pycraft")``
    29.	``¬ import tkinter as tk``
    30.	``¬ from tkinter import messagebox``
    31.	``¬ root = tk.Tk()``
    32.	``¬ root.withdraw()``
    33.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    34.	``¬ quit()``


StartupAnimation
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_StartupAnimation>")``
    3.	``¬ class GenerateStartupScreen:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def Start(self):``
7.	``¬ ¬ ¬ try:``
8.	``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
9.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
10.	``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Welcome")``
11.	``¬ ¬ ¬ ¬ PresentsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
12.	``¬ ¬ ¬ ¬ PycraftFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
13.	``¬ ¬ ¬ ¬ NameFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 45)``

14.	``¬ ¬ ¬ ¬ NameText = NameFont.render("Tom Jebbo", True, self.FontCol)``
15.	``¬ ¬ ¬ ¬ NameTextWidth = NameText.get_width()``
16.	``¬ ¬ ¬ ¬ NameTextHeight = NameText.get_height()``

17.	``¬ ¬ ¬ ¬ PresentsText = PresentsFont.render("presents", True, self.FontCol)``

18.	``¬ ¬ ¬ ¬ PycraftText = PycraftFont.render("Pycraft", True, self.FontCol)``
19.	``¬ ¬ ¬ ¬ PycraftTextWidth = PycraftText.get_width()``
20.	``¬ ¬ ¬ ¬ PycraftTextHeight = PycraftText.get_height()``

21.	``¬ ¬ ¬ ¬ iteration = 0``
22.	``¬ ¬ ¬ ¬ clock = self.mod_Pygame__.time.Clock()``
23.	``¬ ¬ ¬ ¬ if self.RunFullStartup == True:``
24.	``¬ ¬ ¬ ¬ ¬ while iteration <= (60*3):``
25.	``¬ ¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
26.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
27.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(NameText, ((self.realWidth-NameTextWidth)/2, (self.realHeight-NameTextHeight)/2))``
28.	``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``

29.	``¬ ¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
30.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
31.	``¬ ¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
32.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``
33.	``¬ ¬ ¬ ¬ ¬ ¬ ``
34.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
35.	``¬ ¬ ¬ ¬ ¬ ¬ clock.tick(60)``
36.	``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
37.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
38.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

39.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
40.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
41.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
42.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
43.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
44.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``
45.	``¬ ¬ ¬ ¬ ¬ iteration = 0``

46.	``¬ ¬ ¬ ¬ ¬ while iteration <= (60*2):``
47.	``¬ ¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
48.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
49.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(NameText, ((self.realWidth-NameTextWidth)/2, (self.realHeight-NameTextHeight)/2))``
50.	``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(PresentsText, ((((self.realWidth-NameTextWidth)/2)+120), ((self.realHeight-NameTextHeight)/2)+30))``
51.	``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``

52.	``¬ ¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
53.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
54.	``¬ ¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
55.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

56.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
57.	``¬ ¬ ¬ ¬ ¬ ¬ clock.tick(60)``
58.	``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
59.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
60.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

61.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
62.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
63.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
64.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
65.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
66.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``

67.	``¬ ¬ ¬ ¬ ¬ iteration = 0``

68.	``¬ ¬ ¬ ¬ while iteration <= (60*3):``
69.	``¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
70.	``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
71.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftText, ((self.realWidth-PycraftTextWidth)/2, (self.realHeight-PycraftTextHeight)/2))``
72.	``¬ ¬ ¬ ¬ ¬ iteration += 1``

73.	``¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
74.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
75.	``¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
76.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

77.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
78.	``¬ ¬ ¬ ¬ ¬ clock.tick(60)``
79.	``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
80.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
81.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

82.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
83.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
84.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``

85.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
86.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
87.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``

88.	``¬ ¬ ¬ ¬ y = 0``
89.	``¬ ¬ ¬ ¬ while True:``
90.	``¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
91.	``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
92.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftText, ((self.realWidth-PycraftTextWidth)/2, ((self.realHeight-PycraftTextHeight)/2)-y))``
93.	``¬ ¬ ¬ ¬ ¬ y += 2``

94.	``¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
95.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
96.	``¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
97.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

98.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
99.	``¬ ¬ ¬ ¬ ¬ clock.tick(60)``
100.	``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
101.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
102.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

103.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
104.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
105.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``

106.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
107.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
108.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``
109.	``¬ ¬ ¬ ¬ ¬ if ((self.realHeight-PycraftTextHeight)/2)-y <= 0:``
110.	``¬ ¬ ¬ ¬ ¬ ¬ self.RunFullStartup = False``
111.	``¬ ¬ ¬ ¬ ¬ ¬ return None``
112.	``¬ ¬ ¬ except Exception as Message:``
113.	``¬ ¬ ¬ ¬ self.RunFullStartup = False``
114.	``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    115.	``else:``
    116.	``¬ print("You need to run this as part of Pycraft")``
    117.	``¬ import tkinter as tk``
    118.	``¬ from tkinter import messagebox``
    119.	``¬ root = tk.Tk()``
    120.	``¬ root.withdraw()``
    121.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    122.	``¬ quit()``


TextUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_TextUtils>")``
    3.	``¬ class GenerateText:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def LoadQuickText(self):``
7.	``¬ ¬ ¬ LoadingText = ["Use W,A,S,D to move", "Use W to move forward", "Use S to move backward", "Use A to move left", "Use D to move right", "Access your inventory with E", "Access your map with R", "Use SPACE to jump", "Did you know there is a light mode?", "Did you know there is a dark mode?", "Check us out on GitHub", "Use ESC to remove camera movement", "Hold W to sprint", "Did you know you can change the sound volume in settings?", "Did you know you can change the music volume in settings?", "Did you know you can use L to lock the camera"]``
8.	``¬ ¬ ¬ locat = self.mod_Random__.randint(0, (len(LoadingText)-1))``
9.	``¬ ¬ ¬ text = LoadingText[locat]``
10.	``¬ ¬ ¬ return text``

.. note::
    For information on this consult the above guide
    11.	``else:``
    12.	``¬ print("You need to run this as part of Pycraft")``
    13.	``¬ import tkinter as tk``
    14.	``¬ from tkinter import messagebox``
    15.	``¬ root = tk.Tk()``
    16.	``¬ root.withdraw()``
    17.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    18.	``¬ quit()``


ThemeUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_ThemeUtils>")``
    3.	``¬ class DetermineThemeColours:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def GetColours(self):``
7.	``¬ ¬ ¬ try:``
8.	``¬ ¬ ¬ ¬ self.themeArray = [[(255, 255, 255), [30, 30, 30], (80, 80, 80), (237, 125, 49), (255, 255, 255)], [(0, 0, 0), [255, 255, 255], (80, 80, 80), (237, 125, 49), (100, 100, 100)]]``
9.	``¬ ¬ ¬ ¬ if self.theme == "dark":``
10.	``¬ ¬ ¬ ¬ ¬ self.FontCol = self.themeArray[0][0]``
11.	``¬ ¬ ¬ ¬ ¬ self.BackgroundCol = self.themeArray[0][1]``
12.	``¬ ¬ ¬ ¬ ¬ self.ShapeCol = self.themeArray[0][2]``
13.	``¬ ¬ ¬ ¬ ¬ self.AccentCol = self.themeArray[0][3]``
14.	``¬ ¬ ¬ ¬ ¬ self.SecondFontCol = self.themeArray[0][4]``
15.	``¬ ¬ ¬ ¬ elif self.theme == "light":``
16.	``¬ ¬ ¬ ¬ ¬ self.FontCol = self.themeArray[1][0]``
17.	``¬ ¬ ¬ ¬ ¬ self.BackgroundCol = self.themeArray[1][1]``
18.	``¬ ¬ ¬ ¬ ¬ self.ShapeCol = self.themeArray[1][2]``
19.	``¬ ¬ ¬ ¬ ¬ self.AccentCol = self.themeArray[1][3]``
20.	``¬ ¬ ¬ ¬ ¬ self.SecondFontCol = self.themeArray[1][4]``
21.	``¬ ¬ ¬ except Exception as Message:``
22.	``¬ ¬ ¬ ¬ return Message``


23.	``¬ ¬ def GetThemeGUI(self):``
24.	``¬ ¬ ¬ try:``
25.	``¬ ¬ ¬ ¬ clock = self.mod_Pygame__.time.Clock()``
26.	``¬ ¬ ¬ ¬ TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
27.	``¬ ¬ ¬ ¬ Title = TitleFont.render("Pycraft", True, (255, 255, 255))``
28.	``¬ ¬ ¬ ¬ MiddleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
29.	``¬ ¬ ¬ ¬ DarkModeFont = MiddleFont.render("Dark", True, (255, 255, 255))``
30.	``¬ ¬ ¬ ¬ LightModeFont = MiddleFont.render("Light", True, (255, 255, 255))``
31.	``¬ ¬ ¬ ¬ mousebuttondown = False``
32.	``¬ ¬ ¬ ¬ while self.theme == False:``
33.	``¬ ¬ ¬ ¬ ¬ self.Display.fill([30, 30, 30])``
34.	``¬ ¬ ¬ ¬ ¬ mX, mY = self.mod_Pygame__.mouse.get_pos()``
35.	``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
36.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
37.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

38.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
39.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
40.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
41.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
42.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
43.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
44.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:``
45.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True``
46.	``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONUP:``
47.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
48.	``¬ ¬ ¬ ¬ ¬ ¬ ``
49.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(Title, (540, 0))``
50.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(DarkModeFont, (320, 360))``
51.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(LightModeFont, (890, 360))``
52.	``¬ ¬ ¬ ¬ ¬ DarkRect = self.mod_Pygame__.Rect(260, 300, 200, 160)``
53.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (80, 80, 80), DarkRect, 3)``
54.	``¬ ¬ ¬ ¬ ¬ LightRect = self.mod_Pygame__.Rect(820, 300, 200, 160)``
55.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (80, 80, 80), LightRect, 3)``
56.	``¬ ¬ ¬ ¬ ¬ if mX >= 260 and mX <= 460 and mY >= 300 and mY <= 460:``
57.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
58.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "dark"``
59.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.base_folder = self.mod_OS__.path.dirname(__file__)``
60.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``
61.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
62.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.set_volume(50)``
63.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
64.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.play()``
65.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
66.	``¬ ¬ ¬ ¬ ¬ elif mX >= 820 and mX <= 980 and mY >= 300 and mY <= 460:``
67.	``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
68.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "light"``
69.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.base_folder = self.mod_OS__.path.dirname(__file__)``
70.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``
71.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
72.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.set_volume(50)``
73.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
74.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.play()``
75.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
76.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``
77.	``¬ ¬ ¬ ¬ ¬ clock.tick(60)``
78.	``¬ ¬ ¬ except Exception as Message:``
79.	``¬ ¬ ¬ ¬ Message = str(Message)+" in <Pycraft_ThemeUtils>"``
80.	``¬ ¬ ¬ ¬ return Message``

81.	``¬ ¬ ¬ return None``

.. note::
    For information on this consult the above guide
    82.	``else:``
    83.	``¬ print("You need to run this as part of Pycraft")``
    84.	``¬ import tkinter as tk``
    85.	``¬ from tkinter import messagebox``
    86.	``¬ root = tk.Tk()``
    87.	``¬ root.withdraw()``
    88.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    89.	``¬ quit()``


ThreadingUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1.	``if not __name__ == "__main__":``
    2.	``¬ print("Started <Pycraft_ThreadingUtils>")``
    3.	``¬ class ThreadingUtils:``
    4.	``¬ ¬ def __init__(self):``
    5.	``¬ ¬ ¬ pass``

6.	``¬ ¬ def StartVariableChecking(self):``
7.	``¬ ¬ ¬ while True:``
8.	``¬ ¬ ¬ ¬ if self.Iteration > 1000:``
9.	``¬ ¬ ¬ ¬ ¬ self.aFPS = (self.aFPS/self.Iteration)``
10.	``¬ ¬ ¬ ¬ ¬ self.Iteration = 1``
11.	``¬ ¬ ¬ ¬ self.FPS = int(self.FPS)``
12.	``¬ ¬ ¬ ¬ self.eFPS = int(self.eFPS)``

13.	``¬ ¬ ¬ ¬ self.mod_Time__.sleep(1)``

14.	``¬ ¬ ¬ ¬ if self.Stop_Thread_Event.is_set():``
15.	``¬ ¬ ¬ ¬ ¬ break``
16.	``¬ ¬ ``
17.	``¬ ¬ def StartCPUlogging(self):``
18.	``¬ ¬ ¬ while True:``
19.	``¬ ¬ ¬ ¬ if self.Devmode == 10:``
20.	``¬ ¬ ¬ ¬ ¬ if self.Timer >= 2:``
21.	``¬ ¬ ¬ ¬ ¬ ¬ CPUPercent = self.mod_Psutil__.cpu_percent(0.2)``
22.	``¬ ¬ ¬ ¬ ¬ ¬ if CPUPercent > self.Data_CPUUsE_Max:``
23.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = CPUPercent``
24.	``¬ ¬ ¬ ¬ ¬ ¬ elif CPUPercent < self.Data_CPUUsE_Min:``
25.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = CPUPercent``

26.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE.append([((self.realWidth/2)+100)+(self.Timer-2), 200-(100/self.Data_CPUUsE_Max)*CPUPercent])``
27.	``¬ ¬ ¬ ¬ ¬ else:``
28.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(0.2)``
29.	``¬ ¬ ¬ ¬ else:``
30.	``¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(1)``

31.	``¬ ¬ ¬ ¬ if self.Stop_Thread_Event.is_set():``
32.	``¬ ¬ ¬ ¬ ¬ break``

33.	``¬ ¬ def AdaptiveMode(self):``
34.	``¬ ¬ ¬ while True:``
35.	``¬ ¬ ¬ ¬ if self.Stop_Thread_Event.is_set():``
36.	``¬ ¬ ¬ ¬ ¬ break``
37.	``¬ ¬ ¬ ¬ ``
38.	``¬ ¬ ¬ ¬ if self.SettingsPreference == "Adaptive":``
39.	``¬ ¬ ¬ ¬ ¬ CPUPercent = self.mod_Psutil__.cpu_percent()``
40.	``¬ ¬ ¬ ¬ ¬ CoreCount = self.mod_Psutil__.cpu_count()``

41.	``¬ ¬ ¬ ¬ ¬ try:``
42.	``¬ ¬ ¬ ¬ ¬ ¬ gpus = self.mod_GPUtil__.getGPUs()``

43.	``¬ ¬ ¬ ¬ ¬ ¬ GPUPercent = 0``
44.	``¬ ¬ ¬ ¬ ¬ ¬ NumOfGPUs = 0``

45.	``¬ ¬ ¬ ¬ ¬ ¬ for gpu in gpus:``
46.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ NumOfGPUs += 1``
47.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ GPUPercent += gpu.load*100``

48.	``¬ ¬ ¬ ¬ ¬ ¬ GPUPercent = GPUPercent/NumOfGPUs``
49.	``¬ ¬ ¬ ¬ ¬ ``
50.	``¬ ¬ ¬ ¬ ¬ except:``
51.	``¬ ¬ ¬ ¬ ¬ ¬ GPUPercent = CPUPercent``

52.	``¬ ¬ ¬ ¬ ¬ if (CPUPercent >= (100/CoreCount)) and (GPUPercent >= (100/CoreCount)):``
53.	``¬ ¬ ¬ ¬ ¬ ¬ self.FPS -= 10``
54.	``¬ ¬ ¬ ¬ ¬ else:``
55.	``¬ ¬ ¬ ¬ ¬ ¬ if self.FPS < self.RecommendedFPS:``
56.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS += 10``
57.	``¬ ¬ ¬ ¬ ¬ ¬ else:``
58.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not (self.FPS == self.RecommendedFPS):``
59.	``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS -= 1``
60.	``¬ ¬ ¬ ¬ ¬ ``
61.	``¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(0.2)``
62.	``¬ ¬ ¬ ¬ else:``
63.	``¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(1)``

.. note::
    For information on this consult the above guide
   64. ``else:``
   65. ``¬ print("You need to run this as part of Pycraft")``
   66. ``¬ import tkinter as tk``
   67. ``¬ from tkinter import messagebox``
   68. ``¬ root = tk.Tk()``
   69. ``¬ root.withdraw()``
   70. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   71. ``¬ quit()``


TkinterUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
   1. ``if not __name__ == "__main__":``
   2. ``¬ print("Started <Pycraft_TkinterUtils>")``
   3. ``¬ class TkinterInfo:``
   4. ``¬ ¬ def __init__(self):``
   5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def CreateTkinterWindow(self):``
7. ``¬ ¬ ¬ DataWindow = self.mod_Tkinter__tk.Tk()``
8. ``¬ ¬ ¬ DataWindow.title("Player Information")``
9. ``¬ ¬ ¬ DataWindow.configure(width = 500, height = 300) ``
10. ``¬ ¬ ¬ DataWindow.configure(bg="lightblue") ``
11. ``¬ ¬ ¬ VersionData = f"Pycraft: v{self.version}"``
12. ``¬ ¬ ¬ CoordinatesData = f"Coordinates: x: {self.X} y: {self.Y} z: {self.Z} Facing: 0.0, 0.0, 0.0" ``
13. ``¬ ¬ ¬ FPSData = f"FPS: Actual: {self.eFPS} Max: {self.FPS}" ``
14. ``¬ ¬ ¬ VersionData = self.mod_Tkinter__tk.Label(DataWindow, text=VersionData) ``
15. ``¬ ¬ ¬ CoordinatesData = self.mod_Tkinter__tk.Label(DataWindow, text=CoordinatesData) ``
16. ``¬ ¬ ¬ FPSData = self.mod_Tkinter__tk.Label(DataWindow, text=FPSData) ``
17. ``¬ ¬ ¬ VersionData.grid(row = 0, column = 0, columnspan = 2) ``
18. ``¬ ¬ ¬ CoordinatesData.grid(row = 1, column = 0, columnspan = 2)``
19. ``¬ ¬ ¬ FPSData.grid(row = 2, column = 0, columnspan = 2)``
20. ``¬ ¬ ¬ DataWindow.mainloop() ``
21. ``¬ ¬ ¬ DataWindow.quit()``

.. note::
    For information on this consult the above guide
   22. ``else:``
   23. ``¬ print("You need to run this as part of Pycraft")``
   24. ``¬ import tkinter as tk``
   25. ``¬ from tkinter import messagebox``
   26. ``¬ root = tk.Tk()``
   27. ``¬ root.withdraw()``
   28. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   29. ``¬ quit()``
