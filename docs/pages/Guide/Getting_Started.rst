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
   1. ``if not __name__ == "__main__":``
   2. ``¬ print("Started <Pycraft_Achievements>")``
   3. ``¬ class GenerateAchievements:``
   4. ``¬ ¬ def __init__(self):``
   5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def Achievements(self):``
7. ``¬ ¬ ¬ try:``
8. ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
9. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
10. ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")``
11. ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
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
25. ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``
26. ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``

27. ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``

28. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
29. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``
30. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
31. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
32. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
33. ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:``
34. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:``
35. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``
36. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
37. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
38. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
39. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
40. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``
41. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``

42. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")``
43. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
44. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

45. ``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``
46. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
47. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
48. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))``

49. ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
50. ``¬ ¬ ¬ ¬ ¬ if not Message == None:``
51. ``¬ ¬ ¬ ¬ ¬ ¬ return Message``
52. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
53. ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
54. ``¬ ¬ ¬ except Exception as Message:``
55. ``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
   56. ``else:``
   57. ``¬ print("You need to run this as part of Pycraft")``
   58. ``¬ import tkinter as tk``
   59. ``¬ from tkinter import messagebox``
   60. ``¬ root = tk.Tk()``
   61. ``¬ root.withdraw()``
   62. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   63. ``¬ quit()``


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
9. ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
10. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
11. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark")``
12. ``¬ ¬ ¬ ¬ self.VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
13. ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
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
52. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
53. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))``
54. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont1, (3, 100))``
55. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont2, (3, 130))``
56. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont3, (3, 145))``
57. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont4, (3, 160))``
58. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont5, (3, 175))``
59. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont6, (3, 190))``
60. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont7, (3, 220))``
61. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont8, (3, 235))``
62. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont9, (3, 250))``
63. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont10, (3, 280))``

64. ``¬ ¬ ¬ ¬ ¬ if stage == 1:``
65. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Getting System Information")``
66. ``¬ ¬ ¬ ¬ ¬ ¬ CPUid = f"{self.mod_CPUinfo__.get_cpu_info()['brand_raw']} w/{self.mod_Psutil__.cpu_count(logical=False)} cores @ {self.mod_Psutil__.cpu_freq().max} MHz"``
67. ``¬ ¬ ¬ ¬ ¬ ¬ RAMid = f"{round((((self.mod_Psutil__.virtual_memory().total)/1000)/1000/1000),2)} GB of memory, with {self.mod_Psutil__.virtual_memory().percent}% used"``
68. ``¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFO = DataFont.render(CPUid, self.aa, (255, 255, 255))``
69. ``¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFOwidth = CPUhwINFO.get_width()``

70. ``¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFO = DataFont.render(RAMid, self.aa, (255, 255, 255))``
71. ``¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFOwidth = RAMhwINFO.get_width()``
72. ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``

73. ``¬ ¬ ¬ ¬ ¬ if stage == 2:``
74. ``¬ ¬ ¬ ¬ ¬ ¬ try:``
75. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3 = self.mod_ExBenchmark__.LoadBenchmark.run(self)``
76. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:``
77. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message``
78. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``
79. ``¬ ¬ ¬ ¬ ¬ ¬ except:``
80. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Cancelled benchmark")``
81. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
82. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
83. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Finished self.FPS based benchmarks")``
84. ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``

85. ``¬ ¬ ¬ ¬ ¬ if stage == 3:``
86. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Starting disk read test")``
87. ``¬ ¬ ¬ ¬ ¬ ¬ ReadIteration = 50``
88. ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(ReadIteration):``
89. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:``
90. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Benchdata = Bench.read()``

91. ``¬ ¬ ¬ ¬ ¬ ¬ aTime = 0``
92. ``¬ ¬ ¬ ¬ ¬ ¬ ReadIteration = 50``
93. ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(ReadIteration):``
94. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ start = self.mod_Time__.perf_counter()``
95. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:``
96. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Benchdata = Bench.read()``
97. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ aTime += self.mod_Time__.perf_counter()-start``
98. ``¬ ¬ ¬ ¬ ¬ ¬ aTime = aTime/(ReadIteration+1)``
99. ``¬ ¬ ¬ ¬ ¬ ¬ ReadSpeed = (1/(aTime))``
100. ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``

101. ``¬ ¬ ¬ ¬ ¬ if stage == 4:``
102. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results.")``
103. ``¬ ¬ ¬ ¬ ¬ ¬ Max1 = 0``
104. ``¬ ¬ ¬ ¬ ¬ ¬ Min1 = 60``
105. ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):``
106. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY[i] > Max1:``
107. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max1 = FPSlistY[i]``
108. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY[i] < Min1:``
109. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min1 = FPSlistY[i]``

110. ``¬ ¬ ¬ ¬ ¬ ¬ Max2 = 0``
111. ``¬ ¬ ¬ ¬ ¬ ¬ Min2 = 60``
112. ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``
113. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY2[i] > Max2:``
114. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max2 = FPSlistY2[i]``
115. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY2[i] < Min2:``
116. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min2 = FPSlistY2[i]``

117. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results..")``
118. ``¬ ¬ ¬ ¬ ¬ ¬ Max3 = 0``
119. ``¬ ¬ ¬ ¬ ¬ ¬ Min3 = 60``
120. ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY3)):``
121. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY3[i] > Max3:``
122. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max3 = FPSlistY3[i]``
123. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY3[i] < Min3:``
124. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min3 = FPSlistY3[i]``

125. ``¬ ¬ ¬ ¬ ¬ ¬ if Max2 > Max1:``
126. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max2``
127. ``¬ ¬ ¬ ¬ ¬ ¬ elif Max3 > Max2:``
128. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max3``
129. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
130. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max1``

131. ``¬ ¬ ¬ ¬ ¬ ¬ self.RecommendedFPS = GlobalMax/2``

132. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results...")``
133. ``¬ ¬ ¬ ¬ ¬ ¬ multiplier = len(FPSlistY)/(realWidth-20)``
134. ``¬ ¬ ¬ ¬ ¬ ¬ temp = []``
135. ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):``
136. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY[i])))``
137. ``¬ ¬ ¬ ¬ ¬ ¬ FPSListY = temp``

138. ``¬ ¬ ¬ ¬ ¬ ¬ temp = []``
139. ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``
140. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY2[i])))``
141. ``¬ ¬ ¬ ¬ ¬ ¬ FPSListY2 = temp``

142. ``¬ ¬ ¬ ¬ ¬ ¬ temp = []``
143. ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``
144. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY3[i])))``
145. ``¬ ¬ ¬ ¬ ¬ ¬ FPSListY3 = temp``

146. ``¬ ¬ ¬ ¬ ¬ ¬ Results1 = []``
147. ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):``
148. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results1.append([(FPSlistX[i]/multiplier), FPSListY[i]])``

149. ``¬ ¬ ¬ ¬ ¬ ¬ Results2 = []``
150. ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):``
151. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results2.append([(FPSlistX2[i]/multiplier), FPSListY2[i]])``

152. ``¬ ¬ ¬ ¬ ¬ ¬ Results3 = []``
153. ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY3)):``
154. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results3.append([(FPSlistX3[i]/multiplier), FPSListY3[i]])``

155. ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1``

156. ``¬ ¬ ¬ ¬ ¬ if stage == 5:``
157. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Results")``

158. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

159. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
160. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))``

161. ``¬ ¬ ¬ ¬ ¬ ¬ FPSRect = self.mod_Pygame__.Rect(10, 130, realWidth-20, 300)``
162. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FPSRect, 0)``

163. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*60)))), (realWidth-20, int(130+(300-((300/GlobalMax)*60)))))``
164. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SixtyFPSData, (13, int(130+(300-((300/GlobalMax)*60)))))``

165. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*144)))), (realWidth-20, int(130+(300-((300/GlobalMax)*144)))))``
166. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(OneFourFourFPSData, (13, int(130+(300-((300/GlobalMax)*140)))))``

167. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*240)))), (realWidth-20, int(130+(300-((300/GlobalMax)*240)))))``
168. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TwoFortyFPSData, (13, int(130+(300-((300/GlobalMax)*240)))))``

169. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 255, 0), False, Results1)``
170. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 0, 255), False, Results2)``
171. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 0), False, Results3)``

172. ``¬ ¬ ¬ ¬ ¬ ¬ HideRect = self.mod_Pygame__.Rect(0, 110, realWidth, 330)``
173. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.BackgroundCol, HideRect, 20)``

174. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSinfoTEXT, ((realWidth-FPSinfoTEXTWidth)-3, 100))``
175. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FILEinfoTEXT, ((realWidth-FILEinfoTEXTWidth)-3, 430))``

176. ``¬ ¬ ¬ ¬ ¬ ¬ FileResults = DataFont.render(f"Your device achieved a score of: {round(ReadSpeed, 2)}/100 ({round((100/100)*ReadSpeed)}%)", self.aa, self.FontCol)``
177. ``¬ ¬ ¬ ¬ ¬ ¬ FileResultsWidth = FileResults.get_width()``
178. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FileResults, ((realWidth-FileResultsWidth)-3, 460))``

179. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(HARDWAREinfoTEXT, ((realWidth-HARDWAREinfoTEXTwidth)-3, 480))``

180. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CPUhwINFO, ((realWidth-CPUhwINFOwidth)-3, 500))``
181. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(RAMhwINFO, ((realWidth-RAMhwINFOwidth)-3, 516))``

182. ``¬ ¬ ¬ ¬ ¬ ¬ GreenInfo = InfoDetailsFont.render(f"Blank screen test (green); Minimum: {round(Min1, 4)} FPS, Maximum: {round(Max1, 4)} FPS", self.aa, self.FontCol)``
183. ``¬ ¬ ¬ ¬ ¬ ¬ BlueInfo = InfoDetailsFont.render(f"Drawing test (blue); Minimum: {round(Min2, 4)} FPS, Maximum: {round(Max2, 4)} FPS", self.aa, self.FontCol)``
184. ``¬ ¬ ¬ ¬ ¬ ¬ RedInfo = InfoDetailsFont.render(f"OpenGL test (red); Minimum: {round(Min3, 4)} FPS, Maximum: {round(Max3, 4)} FPS", self.aa, self.FontCol)``
185. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(GreenInfo, (3, 430))``
186. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BlueInfo, (3, 445))``
187. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(RedInfo, (3, 460))``

188. ``¬ ¬ ¬ ¬ ¬ ¬ if resize == True:``
189. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ stage = 4``
190. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ resize = False``

191. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
192. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE) and stage <= 3) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``
193. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
194. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
195. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
196. ``¬ ¬ ¬ ¬ ¬ ¬ if (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_SPACE) and stage == 0:``
197. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ stage += 1``
198. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.VIDEORESIZE:``
199. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ resize = True``

200. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
201. ``¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)``
202. ``¬ ¬ ¬ except Exception as Message:``
203. ``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    204.   ``else:``
    205.   ``¬ print("You need to run this as part of Pycraft")``
    206.   ``¬ import tkinter as tk``
    207.   ``¬ from tkinter import messagebox``
    208.   ``¬ root = tk.Tk()``
    209.   ``¬ root.withdraw()``
    210.   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    211.   ``¬ quit()``


CaptionUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_CaptionUtils>")``
    3. ``¬ class GenerateCaptions:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

1. ``¬ ¬ def GetLoadingCaption(self, num):``
2. ``¬ ¬ ¬ if num == 0:``
3. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (-)")``
4. ``¬ ¬ ¬ elif num == 1:``
5.  ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (\)")``
6.  ``¬ ¬ ¬ elif num == 2:``
7.  ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (|)")``
8.  ``¬ ¬ ¬ elif num == 3:``
9.  ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (/)")``
10. ``¬ ¬ ¬ else:``
11. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading")``
12. ``¬ ¬ ¬ self.mod_Pygame__.display.update()``

13. ``¬ ¬ def GetNormalCaption(self, location):``
14. ``¬ ¬ ¬ if self.Devmode >= 5 and self.Devmode <= 9:``
15. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | you are: {10-self.Devmode} steps away from being a developer")``
16. ``¬ ¬ ¬ elif self.Devmode == 10:``
17. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | Developer Mode | Pos: {round(self.X, 2)}, {round(self.Y, 2)}, {round(self.Z, 2)} | V: {self.Total_move_x}, {self.Total_move_y}, {self.Total_move_z} FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: {int(self.aFPS/self.Iteration)} Iteration: {self.Iteration} | MemUsE: {self.mod_Psutil__.virtual_memory().percent} | CPUUsE: {self.mod_Psutil__.cpu_percent()} | Theme: {self.theme} | Thread Count: {self.mod_Threading__.active_count()}")``
18. ``¬ ¬ ¬ else:``
19. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location}")``

.. note::
    For information on this consult the above guide
    25. ``else:``
    26. ``¬ print("You need to run this as part of Pycraft")``
    27. ``¬ import tkinter as tk``
    28. ``¬ from tkinter import messagebox``
    29. ``¬ root = tk.Tk()``
    30. ``¬ root.withdraw()``
    31. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    32. ``¬ quit()``


Character Designer
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_CharacterDesigner>")``
    3. ``¬ class GenerateCharacterDesigner:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def CharacterDesigner(self):``
7. ``¬ ¬ ¬ try:``
8. ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
9. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
10. ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")``
11. ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
12. ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
13. ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

14. ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.SecondFontCol)``
15. ``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``

16. ``¬ ¬ ¬ ¬ AchievementsFont = InfoTitleFont.render("Character Designer", self.aa, self.FontCol)``
17. ``¬ ¬ ¬ ¬ tempFPS = self.FPS``

18. ``¬ ¬ ¬ ¬ while True:``
19. ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

20. ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
21. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
22. ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
23. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

24. ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
25. ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``
26. ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``

27. ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``

28. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
29. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``
30. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
31. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
32. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
33. ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:``
34. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:``
35. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``
36. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
37. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
38. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
39. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
40. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``
41. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``

42. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")``
43. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
44. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

45. ``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``
46. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
47. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
48. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))``

49. ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
50. ``¬ ¬ ¬ ¬ ¬ if not Message == None:``
51. ``¬ ¬ ¬ ¬ ¬ ¬ return Message``
52. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
53. ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
54. ``¬ ¬ ¬ except Exception as Message:``
55. ``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    56. ``else:``
    55. ``¬ print("You need to run this as part of Pycraft")``
    57. ``¬ import tkinter as tk``
    58. ``¬ from tkinter import messagebox``
    59. ``¬ root = tk.Tk()``
    60. ``¬ root.withdraw()``
    61. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    62. ``¬ quit()``


Credits
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_Credits>")``
    3. ``¬ class GenerateCredits:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def Credits(self):``
7. ``¬ ¬ ¬ try:``
8. ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
9. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
10. ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits")``
11. ``¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
12. ``¬ ¬ ¬ ¬ LargeCreditsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``
13. ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
14. ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
15. ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
16. ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
17. ``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()``
18. ``¬ ¬ ¬ ¬ TitleHeight = TitleFont.get_height()``
19. ``¬ ¬ ¬ ¬ CreditsFont = InfoTitleFont.render("Credits", self.aa, self.SecondFontCol)``
20. ``¬ ¬ ¬ ¬ Credits1 = LargeCreditsFont.render(f"Pycraft: v{self.version}", self.aa, self.FontCol)``
21. ``¬ ¬ ¬ ¬ Credits1Width = Credits1.get_width()``
22. ``¬ ¬ ¬ ¬ Credits2 = LargeCreditsFont.render("Game Director: Tom Jebbo", self.aa, self.FontCol)``
23. ``¬ ¬ ¬ ¬ Credits2Width = Credits2.get_width()``
24. ``¬ ¬ ¬ ¬ Credits3 = LargeCreditsFont.render("Art and Music Lead: Tom Jebbo", self.aa, self.FontCol)``
25. ``¬ ¬ ¬ ¬ Credits3Width = Credits3.get_width()``
26. ``¬ ¬ ¬ ¬ Credits4 = LargeCreditsFont.render("Other Music Credits:", self.aa, self.FontCol)``
27. ``¬ ¬ ¬ ¬ Credits4Width = Credits4.get_width()``
28. ``¬ ¬ ¬ ¬ Credits5 = LargeCreditsFont.render("Freesound: - Erokia's 'ambient wave compilation' @ freesound.org/s/473545", self.aa, self.FontCol)``
29. ``¬ ¬ ¬ ¬ Credits5Width = Credits5.get_width()``
30. ``¬ ¬ ¬ ¬ Credits6 = LargeCreditsFont.render("Freesound: - Soundholder's 'ambient meadow near forest' @ freesound.org/s/425368", self.aa, self.FontCol)``
31. ``¬ ¬ ¬ ¬ Credits6Width = Credits6.get_width()``
32. ``¬ ¬ ¬ ¬ Credits7 = LargeCreditsFont.render("Freesound: - monte32's 'Footsteps_6_Dirt_shoe' @ freesound.org/people/monte32/sounds/353799", self.aa, self.FontCol)``
33. ``¬ ¬ ¬ ¬ Credits7Width = Credits7.get_width()``
34. ``¬ ¬ ¬ ¬ Credits8 = LargeCreditsFont.render("With thanks to the developers of:", self.aa, self.FontCol)``
35. ``¬ ¬ ¬ ¬ Credits8Width = Credits8.get_width()``
36. ``¬ ¬ ¬ ¬ Credits9 = LargeCreditsFont.render("PSutil", self.aa, self.FontCol)``
37. ``¬ ¬ ¬ ¬ Credits9Width = Credits9.get_width()``
38. ``¬ ¬ ¬ ¬ Credits10 = LargeCreditsFont.render("Python", self.aa, self.FontCol)``
39. ``¬ ¬ ¬ ¬ Credits10Width = Credits10.get_width()``
40. ``¬ ¬ ¬ ¬ Credits11 = LargeCreditsFont.render("Pygame", self.aa, self.FontCol)``
41. ``¬ ¬ ¬ ¬ Credits11Width = Credits11.get_width()``
42. ``¬ ¬ ¬ ¬ Credits12 = LargeCreditsFont.render("Numpy", self.aa, self.FontCol)``
43. ``¬ ¬ ¬ ¬ Credits12Width = Credits12.get_width()``
44. ``¬ ¬ ¬ ¬ Credits13 = LargeCreditsFont.render("Nuitka", self.aa, self.FontCol)``
45. ``¬ ¬ ¬ ¬ Credits13Width = Credits13.get_width()``
46. ``¬ ¬ ¬ ¬ Credits14 = LargeCreditsFont.render("CPUinfo", self.aa, self.FontCol)``
47. ``¬ ¬ ¬ ¬ Credits14Width = Credits14.get_width()``
48. ``¬ ¬ ¬ ¬ Credits15 = LargeCreditsFont.render("PyInstaller", self.aa, self.FontCol)``
49. ``¬ ¬ ¬ ¬ Credits15Width = Credits15.get_width()``
50. ``¬ ¬ ¬ ¬ Credits16 = LargeCreditsFont.render("PyAutoGUI", self.aa, self.FontCol)``
51. ``¬ ¬ ¬ ¬ Credits16Width = Credits16.get_width()``
52. ``¬ ¬ ¬ ¬ Credits17 = LargeCreditsFont.render("PyWaveFront", self.aa, self.FontCol)``
53. ``¬ ¬ ¬ ¬ Credits17Width = Credits17.get_width()``
54. ``¬ ¬ ¬ ¬ Credits18 = LargeCreditsFont.render("Microsoft's Visual Studio Code", self.aa, self.FontCol)``
55. ``¬ ¬ ¬ ¬ Credits18Width = Credits18.get_width()``
56. ``¬ ¬ ¬ ¬ Credits19 = LargeCreditsFont.render("PIL (Pillow/Python Imaging Library)", self.aa, self.FontCol)``
57. ``¬ ¬ ¬ ¬ Credits19Width = Credits19.get_width()``
58. ``¬ ¬ ¬ ¬ Credits20 = LargeCreditsFont.render("PyOpenGL (and PyOpenGL-accelerate)", self.aa, self.FontCol)``
59. ``¬ ¬ ¬ ¬ Credits20Width = Credits20.get_width()``
60. ``¬ ¬ ¬ ¬ Credits21 = LargeCreditsFont.render("For more in depth accreditation please check the GitHub Page @ github.com/PycraftDeveloper/Pycraft", self.aa, self.FontCol)``
61. ``¬ ¬ ¬ ¬ Credits21Width = Credits21.get_width()``
62. ``¬ ¬ ¬ ¬ Credits22 = LargeCreditsFont.render("With thanks to:", self.aa, self.FontCol)``
63. ``¬ ¬ ¬ ¬ Credits22Width = Credits22.get_width()``
64. ``¬ ¬ ¬ ¬ Credits23 = LargeCreditsFont.render("All my wonderful followers on Twitter, and you for installing this game, that's massively appreciated!", self.aa, self.FontCol)``
65. ``¬ ¬ ¬ ¬ Credits23Width = Credits23.get_width()``
66. ``¬ ¬ ¬ ¬ Credits24 = LargeCreditsFont.render("For full change-log please visit my aforementioned GitHub profile", self.aa, self.FontCol)``
67. ``¬ ¬ ¬ ¬ Credits24Width = Credits24.get_width()``
68. ``¬ ¬ ¬ ¬ Credits25 = LargeCreditsFont.render("Disclaimer:", self.aa, self.FontCol)``
69. ``¬ ¬ ¬ ¬ Credits25Width = Credits25.get_width()``
70. ``¬ ¬ ¬ ¬ Credits26 = VersionFont.render("The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your", self.aa, self.AccentCol)``
71. ``¬ ¬ ¬ ¬ Credits26Width = Credits26.get_width()``
72. ``¬ ¬ ¬ ¬ Credits27 = VersionFont.render("friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve", self.aa, self.AccentCol)``
73. ``¬ ¬ ¬ ¬ Credits27Width = Credits27.get_width()``
74. ``¬ ¬ ¬ ¬ Credits28 = VersionFont.render("my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo", self.aa, self.AccentCol)``
75. ``¬ ¬ ¬ ¬ Credits28Width = Credits28.get_width()``
76. ``¬ ¬ ¬ ¬ Credits29 = VersionFont.render("DOES NOT TAKE ANY RESPONSIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXTERNAL MODULES INSTALLED ONTO", self.aa, self.AccentCol)``
77. ``¬ ¬ ¬ ¬ Credits29Width = Credits29.get_width()``
78. ``¬ ¬ ¬ ¬ Credits30 = VersionFont.render("YOUR COMPUTER (WHEN NOT CHOOSING THE RECOMMENDED EXECUTABLE VERSION) ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM", self.aa, self.AccentCol)``
79. ``¬ ¬ ¬ ¬ Credits30Width = Credits30.get_width()``
80. ``¬ ¬ ¬ ¬ Credits31 = VersionFont.render("RESPONSIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVICES MANAGER OR ADMINISTRATOR TO INSTALL AND USE", self.aa, self.AccentCol)``
81. ``¬ ¬ ¬ ¬ Credits31Width = Credits31.get_width()``
82. ``¬ ¬ ¬ ¬ Credits32 = VersionFont.render("COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVICE, AND AT ANY POINT NO CONNECTION TO A", self.aa, self.AccentCol)``
83. ``¬ ¬ ¬ ¬ Credits32Width = Credits32.get_width()``
84. ``¬ ¬ ¬ ¬ Credits33 = VersionFont.render("NETWORK IS REQUIRED. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you.", self.aa, self.AccentCol)``
85. ``¬ ¬ ¬ ¬ Credits33Width = Credits33.get_width()``
86. ``¬ ¬ ¬ ¬ Credits34 = VersionFont.render("Thank You!", self.aa, self.FontCol)``
87. ``¬ ¬ ¬ ¬ Credits34Width = Credits34.get_width()``
88. ``¬ ¬ ¬ ¬ Credits34Height = Credits34.get_height()``

89. ``¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
90. ``¬ ¬ ¬ ¬ VisualYdisplacement = realHeight``
91. ``¬ ¬ ¬ ¬ IntroYDisplacement = (realHeight-TitleHeight)/2``
92. ``¬ ¬ ¬ ¬ timer = 5``
93. ``¬ ¬ ¬ ¬ tempFPS = self.FPS``

94. ``¬ ¬ ¬ ¬ EndClock = 0``
95. ``¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
96. ``¬ ¬ ¬ ¬ while True:``
97. ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

98. ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
99. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
100. ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
101. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

102. ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
103. ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``
104. ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``
105. ``¬ ¬ ¬ ¬ ¬ ``
106. ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``

107. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
108. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``
109. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
110. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
111. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
112. ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:``
113. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:``
114. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``
115. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
116. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
117. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
118. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
119. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``
120. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``

121. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits and Change-Log")``
122. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
123. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits1, ((realWidth-Credits1Width)/2, 0+VisualYdisplacement))``
124. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits2, ((realWidth-Credits2Width)/2, 115+VisualYdisplacement))``
125. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits3, ((realWidth-Credits3Width)/2, (115*2)+VisualYdisplacement))``
126. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits4, ((realWidth-Credits4Width)/2, (115*3)+VisualYdisplacement))``
127. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits5, ((realWidth-Credits5Width)/2, (115*3)+20+VisualYdisplacement))``
128. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits6, ((realWidth-Credits6Width)/2, (115*3)+40+VisualYdisplacement))``
129. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits7, ((realWidth-Credits7Width)/2, (115*3)+60+VisualYdisplacement))``
130. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits8, ((realWidth-Credits8Width)/2, 540+VisualYdisplacement))``
131. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits9, ((realWidth-Credits9Width)/2, 540+20+VisualYdisplacement))``
132. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits10, ((realWidth-Credits10Width)/2, 540+40+VisualYdisplacement))``
133. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits11, ((realWidth-Credits11Width)/2, 540+60+VisualYdisplacement))``
134. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits12, ((realWidth-Credits12Width)/2, 540+80+VisualYdisplacement))``
135. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits13, ((realWidth-Credits13Width)/2, 540+100+VisualYdisplacement))``
136. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits14, ((realWidth-Credits14Width)/2, 540+120+VisualYdisplacement))``
137. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits15, ((realWidth-Credits15Width)/2, 540+140+VisualYdisplacement))``
138. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits16, ((realWidth-Credits16Width)/2, 540+160+VisualYdisplacement))``
139. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits17, ((realWidth-Credits17Width)/2, 540+180+VisualYdisplacement))``
140. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits18, ((realWidth-Credits18Width)/2, 540+200+VisualYdisplacement))``
141. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits19, ((realWidth-Credits19Width)/2, 540+220+VisualYdisplacement))``
142. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits20, ((realWidth-Credits20Width)/2, 540+240+VisualYdisplacement))``
143. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits21, ((realWidth-Credits21Width)/2, 540+260+VisualYdisplacement))``
144. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits22, ((realWidth-Credits22Width)/2, 915+VisualYdisplacement))``
145. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits23, ((realWidth-Credits23Width)/2, 935+VisualYdisplacement))``
146. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits24, ((realWidth-Credits24Width)/2, 1050+VisualYdisplacement))``
147. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits25, ((realWidth-Credits25Width)/2, 1165+VisualYdisplacement))``
148. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits26, ((realWidth-Credits26Width)/2, 1167+15+VisualYdisplacement))``
149. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits27, ((realWidth-Credits27Width)/2, 1167+30+VisualYdisplacement))``
150. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits28, ((realWidth-Credits28Width)/2, 1167+45+VisualYdisplacement))``
151. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits29, ((realWidth-Credits29Width)/2, 1167+60+VisualYdisplacement))``
152. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits30, ((realWidth-Credits30Width)/2, 1167+75+VisualYdisplacement))``
153. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits31, ((realWidth-Credits31Width)/2, 1167+90+VisualYdisplacement))``
154. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits32, ((realWidth-Credits32Width)/2, 1167+105+VisualYdisplacement))``
155. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits33, ((realWidth-Credits33Width)/2, 1167+120+VisualYdisplacement))``

156. ``¬ ¬ ¬ ¬ ¬ if timer >= 1:``
157. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))``
158. ``¬ ¬ ¬ ¬ ¬ ¬ timer -= 1/(self.aFPS/self.Iteration)``
159. ``¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement = realHeight``
160. ``¬ ¬ ¬ ¬ ¬ else:``
161. ``¬ ¬ ¬ ¬ ¬ ¬ if IntroYDisplacement <= 0:``
162. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, FullscreenX, 90)``
163. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
164. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
165. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50))``
166. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if int(1402+VisualYdisplacement) <= int(realHeight/2):``
167. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, (realHeight-Credits34Height)/2))``
168. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement -= 60/(self.aFPS/self.Iteration)``
169. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if EndClock >= 5:``
170. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
171. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
172. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ EndClock += 1/(self.aFPS/self.Iteration)``
173. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
174. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, 1402+VisualYdisplacement))``
175. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement -= 60/(self.aFPS/self.Iteration)``
176. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
177. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``
178. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
179. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))``
180. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50+IntroYDisplacement))``
181. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ IntroYDisplacement -= 90/(self.aFPS/self.Iteration)``
182. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement = realHeight``

183. ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
184. ``¬ ¬ ¬ ¬ ¬ if not Message == None:``
185. ``¬ ¬ ¬ ¬ ¬ ¬ return Message``
186. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
187. ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
188. ``¬ ¬ ¬ except Exception as Message:``
189. ``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    190. ``else:``
    191. ``¬ print("You need to run this as part of Pycraft")``
    192. ``¬ import tkinter as tk``
    193. ``¬ from tkinter import messagebox``
    194. ``¬ root = tk.Tk()``
    195. ``¬ root.withdraw()``
    196. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    197. ``¬ quit()``


DisplayUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++
.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_DisplayUtils>")``
    3. ``¬ class DisplayUtils:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def UpdateDisplay(self): # Run tests to make sure windows not too small``
7. ``¬ ¬ ¬ self.Data_aFPS = []``
8. ``¬ ¬ ¬ self.Data_CPUUsE = []``
9. ``¬ ¬ ¬ self.Data_eFPS = []``
10. ``¬ ¬ ¬ self.Data_MemUsE = []``
11. ``¬ ¬ ¬ self.Timer = 0``
12. ``¬ ¬ ¬ self.Data_aFPS_Min = 60``
13. ``¬ ¬ ¬ self.Data_aFPS_Max = 1``

14. ``¬ ¬ ¬ self.Data_CPUUsE_Min = 60``
15. ``¬ ¬ ¬ self.Data_CPUUsE_Max = 1``

16. ``¬ ¬ ¬ self.Data_eFPS_Min = 60``
17. ``¬ ¬ ¬ self.Data_eFPS_Max = 1``

18. ``¬ ¬ ¬ self.Data_MemUsE_Min = 50``
19. ``¬ ¬ ¬ self.Data_MemUsE_Max = 50``

20. ``¬ ¬ ¬ self.Data_CPUUsE_Min = 50``
21. ``¬ ¬ ¬ self.Data_CPUUsE_Max = 50``
22. ``¬ ¬ ¬ try:``
23. ``¬ ¬ ¬ ¬ try:``
24. ``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
25. ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
26. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
27. ``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:``
28. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
29. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
30. ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = True``
31. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.RESIZABLE)``
32. ``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:``
33. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
34. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
35. ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = False``
36. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF)``
37. ``¬ ¬ ¬ ¬ except Exception as error:``
38. ``¬ ¬ ¬ ¬ ¬ self.Fullscreen = True``
39. ``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
40. ``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``
41. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
42. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
43. ``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight))``
44. ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
45. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
46. ``¬ ¬ ¬ except Exception as Message:``
47. ``¬ ¬ ¬ ¬ return Message``
48. ``¬ ¬ ¬ else:``
49. ``¬ ¬ ¬ ¬ return None``

50. ``¬ ¬ def SetOPENGLdisplay(self):``
51. ``¬ ¬ ¬ try:``
52. ``¬ ¬ ¬ ¬ try:``
53. ``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
54. ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
55. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
56. ``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == True:``
57. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
58. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
59. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
60. ``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == False:``
61. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
62. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
63. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
64. ``¬ ¬ ¬ ¬ except Exception as error:``
65. ``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
66. ``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``
67. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
68. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
69. ``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
70. ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
71. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
72. ``¬ ¬ ¬ except Exception as Message:``
73. ``¬ ¬ ¬ ¬ return Message``
74. ``¬ ¬ ¬ else:``
75. ``¬ ¬ ¬ ¬ return None``

76. ``¬ ¬ def UpdateOPENGLdisplay(self):``
77. ``¬ ¬ ¬ try:``
78. ``¬ ¬ ¬ ¬ try:``
79. ``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
80. ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
81. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
82. ``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:``
83. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
84. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
85. ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = True``
86. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
87. ``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:``
88. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
89. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
90. ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = False``
91. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
92. ``¬ ¬ ¬ ¬ except:``
93. ``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
94. ``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``
95. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
96. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
97. ``¬ ¬ ¬ ¬ ¬ self.Fullscreen = False``
98.  ``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)``
99.  ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
100. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
101. ``¬ ¬ ¬ except Exception as Message:``
102. ``¬ ¬ ¬ ¬ return Message``
103. ``¬ ¬ ¬ else:``
104. ``¬ ¬ ¬ ¬ return None``

105. ``¬ ¬ def SetDisplay(self):``
106. ``¬ ¬ ¬ self.Data_aFPS = []``
107. ``¬ ¬ ¬ self.Data_CPUUsE = []``
108. ``¬ ¬ ¬ self.Data_eFPS = []``
109. ``¬ ¬ ¬ self.Data_MemUsE = []``
110. ``¬ ¬ ¬ self.Timer = 0``
111. ``¬ ¬ ¬ self.Data_aFPS_Min = 60``
112. ``¬ ¬ ¬ self.Data_aFPS_Max = 1``

113. ``¬ ¬ ¬ self.Data_CPUUsE_Min = 60``
114. ``¬ ¬ ¬ self.Data_CPUUsE_Max = 1``

115. ``¬ ¬ ¬ self.Data_eFPS_Min = 60``
116. ``¬ ¬ ¬ self.Data_eFPS_Max = 1``

117. ``¬ ¬ ¬ self.Data_MemUsE_Min = 50``
118. ``¬ ¬ ¬ self.Data_MemUsE_Max = 50``

119. ``¬ ¬ ¬ self.Data_CPUUsE_Min = 50``
120. ``¬ ¬ ¬ self.Data_CPUUsE_Max = 50``
121. ``¬ ¬ ¬ try:``
122. ``¬ ¬ ¬ ¬ try:``
123. ``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``
124. ``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == True:``
125. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
126. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
127. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.RESIZABLE)``
128. ``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == False:``
129. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
130. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
131. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF)``
132. ``¬ ¬ ¬ ¬ except Exception as error:``
133. ``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
134. ``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``
135. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
136. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
137. ``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight))``
138. ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
139. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
140. ``¬ ¬ ¬ except Exception as Message:``
141. ``¬ ¬ ¬ ¬ return Message``
142. ``¬ ¬ ¬ else:``
143. ``¬ ¬ ¬ ¬ return None``

144. ``¬ ¬ def GenerateMinDisplay(self, width, height):``
145. ``¬ ¬ ¬ try:``
146. ``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((width, height), self.mod_Pygame__.RESIZABLE)``
147. ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
148. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
149. ``¬ ¬ ¬ except Exception as Message:``
150. ``¬ ¬ ¬ ¬ return Message``
151. ``¬ ¬ ¬ else:``
152. ``¬ ¬ ¬ ¬ return None``

153. ``¬ ¬ def GetDisplayLocation(self):``
154. ``¬ ¬ ¬ hwnd = self.mod_Pygame__.display.get_wm_info()["window"]``

155. ``¬ ¬ ¬ prototype = self.mod_Ctypes__.WINFUNCTYPE(self.mod_Ctypes__.wintypes.BOOL, self.mod_Ctypes__.wintypes.HWND, self.mod_Ctypes__.POINTER(self.mod_Ctypes__.wintypes.RECT))``
156. ``¬ ¬ ¬ paramflags = (1, "hwnd"), (2, "lprect")``

157. ``¬ ¬ ¬ GetWindowRect = prototype(("GetWindowRect", self.mod_Ctypes__.windll.user32), paramflags)``

158. ``¬ ¬ ¬ rect = GetWindowRect(hwnd)``

159. ``¬ ¬ ¬ return rect.left+8, rect.top+31``

160. ``¬ ¬ def GetPlayStatus(self):``
161. ``¬ ¬ ¬ if self.mod_Pygame__.display.get_active() == True:``
162. ``¬ ¬ ¬ ¬ tempFPS = self.FPS``
163. ``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).unpause()``
164. ``¬ ¬ ¬ ¬ if self.mod_Pygame__.mixer.Channel(2).get_busy() == 0 and self.LoadMusic == True:``
165. ``¬ ¬ ¬ ¬ ¬ if self.music == True and self.CurrentlyPlaying == None:``
166. ``¬ ¬ ¬ ¬ ¬ ¬ self.CurrentlyPlaying = "InvSound"``
167. ``¬ ¬ ¬ ¬ ¬ ¬ self.LoadMusic = False``
168. ``¬ ¬ ¬ ¬ ¬ ¬ MusicThread = self.mod_Threading__.Thread(target=self.mod_SoundUtils__.PlaySound.PlayInvSound, args=(self,))``
169. ``¬ ¬ ¬ ¬ ¬ ¬ MusicThread.start()``
170. ``¬ ¬ ¬ else:``
171. ``¬ ¬ ¬ ¬ self.LoadMusic = True``
172. ``¬ ¬ ¬ ¬ tempFPS = 15``
173. ``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).pause()``
174. ``¬ ¬ ¬ return tempFPS``

.. note::
    For information on this consult the above guide
    175.   ``else:``
    176.   ``¬ print("You need to run this as part of Pycraft")``
    177.   ``¬ import tkinter as tk``
    178.   ``¬ from tkinter import messagebox``
    179.   ``¬ root = tk.Tk()``
    180.   ``¬ root.withdraw()``
    181.   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    182.   ``¬ quit()``


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

13.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[0], (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``
14.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[1], (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
15.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[2], (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
16.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[3], (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
17.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[4], (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
18.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[5], (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``
19.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[6], (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
20.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[7], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
21.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[8], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
22.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[9], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
23.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[10], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
24.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[11], (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``
25.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[12], (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
26.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[13], (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
27.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[14], (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
28.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[15], (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
29.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[16], (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
30.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[17], (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``
31.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[18], (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``
32.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[19], (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
33.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[20], (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
34.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[21], (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
35.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[22], (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
36.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[23], (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``
37.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[24], (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
38.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[25], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
39.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[25], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
40.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[27], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
41.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[28], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
42.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[29], (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
43.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[30], (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
44.	``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[31], (575*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``

45.	``¬ class GenerateGraph:``
46.	``¬ ¬ def __init__(self):``
47.	``¬ ¬ ¬ pass``

48.	``¬ ¬ def CreateDevmodeGraph(self, DataFont):``
49.	``¬ ¬ ¬ if self.Devmode == 10:``
50.	``¬ ¬ ¬ ¬ try:``
51.	``¬ ¬ ¬ ¬ ¬ if ((self.realWidth/2)+100)+self.Timer >= self.realWidth:``
52.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS = []``
53.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE = []``
54.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS = []``
55.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE = []``
56.	``¬ ¬ ¬ ¬ ¬ ¬ self.Timer = 0``
57.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Min = 60``
58.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Max = 1``

59.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = 60``
60.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = 1``

61.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Min = 60``
62.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Max = 1``

63.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Min = 50``
64.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = 50``

65.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = 50``
66.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = 50``

67.	``¬ ¬ ¬ ¬ ¬ BackingRect = self.mod_Pygame__.Rect((self.realWidth/2)+100, 0, self.realWidth, 200)``
68.	``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, BackingRect)``

69.	``¬ ¬ ¬ ¬ ¬ if self.Timer >= 2:``
70.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_aFPS_Max)*(self.aFPS/(self.Iteration))])``
71.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_eFPS_Max)*int(self.eFPS)])``
72.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_MemUsE_Max)*(100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available])``

73.	``¬ ¬ ¬ ¬ ¬ if (self.aFPS/(self.Iteration)) > self.Data_aFPS_Max:``
74.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Max = (self.aFPS/(self.Iteration))``
75.	``¬ ¬ ¬ ¬ ¬ elif (self.aFPS/(self.Iteration)) < self.Data_aFPS_Min:``
76.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Min = (self.aFPS/(self.Iteration))``

77.	``¬ ¬ ¬ ¬ ¬ if self.eFPS > self.Data_eFPS_Max:``
78.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Max = self.eFPS``
79.	``¬ ¬ ¬ ¬ ¬ elif self.eFPS < self.Data_eFPS_Min:``
80.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Min = self.eFPS``

81.	``¬ ¬ ¬ ¬ ¬ if (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available > self.Data_MemUsE_Max:``
82.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available``
83.	``¬ ¬ ¬ ¬ ¬ elif (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available < self.Data_MemUsE_Max:``
84.	``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available``

85.	``¬ ¬ ¬ ¬ ¬ self.Timer += 0.2``
86.	``¬ ¬ ¬ ¬ ¬ if self.Timer >= 5:``
87.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 0), False, self.Data_aFPS)``
88.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 255, 0), False, self.Data_eFPS)``
89.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 0, 255), False, self.Data_MemUsE)``
90.	``¬ ¬ ¬ ¬ ¬ if len(self.Data_CPUUsE) >= 2:``
91.	``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 255), False, self.Data_CPUUsE)``
92.	``¬ ¬ ¬ ¬ ¬ runFont = DataFont.render(f"MemUsE: {self.mod_Psutil__.virtual_memory().percent}% | CPUUsE: {self.mod_Psutil__.cpu_percent()}% | FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: {int(self.aFPS/self.Iteration)} Iteration: {self.Iteration}", self.aa, (255, 255, 255))``
93.	``¬ ¬ ¬ ¬ ¬ self.Display.blit(runFont, ((self.realWidth/2)+105, 0))``
94.	``¬ ¬ ¬ ¬ except Exception as Message:``
95.	``¬ ¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
96.	``¬ ¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    97.	``else:``
    98.	``¬ print("You need to run this as part of Pycraft")``
    99.	``¬ import tkinter as tk``
    100.	``¬ from tkinter import messagebox``
    101.	``¬ root = tk.Tk()``
    102.	``¬ root.withdraw()``
    103.	``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    104.	``¬ quit()``


ExBenchmark
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++
.. note::
For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_ExBenchmark>")``
    3. ``¬ class LoadBenchmark:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

1. ``¬ ¬ def run(self):``
2. ``¬ ¬ ¬ try:``
3. ``¬ ¬ ¬ ¬ FPSlistX = []``
4. ``¬ ¬ ¬ ¬ FPSlistY = []``

5.  ``¬ ¬ ¬ ¬ FPSlistX2 = []``
6.  ``¬ ¬ ¬ ¬ FPSlistY2 = []``

7.  ``¬ ¬ ¬ ¬ FPSlistX3 = []``
8.  ``¬ ¬ ¬ ¬ FPSlistY3 = []``

9.  ``¬ ¬ ¬ ¬ SetFPS = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 200, 250, 300, 350, 500]``

10. ``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((1280, 720))``

11. ``¬ ¬ ¬ ¬ iteration = 0``
12. ``¬ ¬ ¬ ¬ FPScounter = 0``
13. ``¬ ¬ ¬ ¬ MaxIteration = 500``

14. ``¬ ¬ ¬ ¬ while iteration < 7500:``
15. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running Blank Window Benchmark @ {SetFPS[FPScounter]} FPS")``
16. ``¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:``
17. ``¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:``
18. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX.append(iteration)``
19. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY.append(self.clock.get_fps())``
20. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
21. ``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
22. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
23. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``

24. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
25. ``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``
26. ``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])``
27. ``¬ ¬ ¬ ¬ ¬ FPScounter += 1``
28. ``¬ ¬ ¬ ¬ ¬ MaxIteration += 500``

29. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Preparing Animated Benchmark")``

30. ``¬ ¬ ¬ ¬ iteration = 0``
31. ``¬ ¬ ¬ ¬ FPScounter = 0``
32. ``¬ ¬ ¬ ¬ MaxIteration = 500``
33. ``¬ ¬ ¬ ¬ run = 0``
34. ``¬ ¬ ¬ ¬ y = 10``

35. ``¬ ¬ ¬ ¬ while not iteration == 60:``
36. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
37. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
38. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
39. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``

40. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
41. ``¬ ¬ ¬ ¬ ¬ iteration += 1``
42. ``¬ ¬ ¬ ¬ ¬ self.clock.tick(60)``

43. ``¬ ¬ ¬ ¬ iteration = 0``
44. ``¬ ¬ ¬ ¬ FPScounter = 0``
45. ``¬ ¬ ¬ ¬ MaxIteration = 500``

46. ``¬ ¬ ¬ ¬ while iteration < 7500:``
47. ``¬ ¬ ¬ ¬ ¬ run += 1``
48. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running Animated Window Benchmark @ {SetFPS[FPScounter]} FPS")``
49. ``¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:``
50. ``¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:``
51. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX2.append(iteration)``
52. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY2.append(self.clock.get_fps())``
53. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
54. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
55. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
56. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
57. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
58. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
59. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
60. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
61. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)``
62. ``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
63. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
64. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``

65. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
66. ``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``
67. ``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])``
68. ``¬ ¬ ¬ ¬ ¬ FPScounter += 1``
69. ``¬ ¬ ¬ ¬ ¬ MaxIteration += 500``

70. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Preparing OpenGL Benchmark")``

71. ``¬ ¬ ¬ ¬ iteration = 0``
72. ``¬ ¬ ¬ ¬ FPScounter = 0``
73. ``¬ ¬ ¬ ¬ MaxIteration = 500``
74. ``¬ ¬ ¬ ¬ run = 0``
75. ``¬ ¬ ¬ ¬ y = 10``

76. ``¬ ¬ ¬ ¬ while not iteration == 60:``
77. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
78. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
79. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
80. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return False``

81. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
82. ``¬ ¬ ¬ ¬ ¬ iteration += 1``
83. ``¬ ¬ ¬ ¬ ¬ self.clock.tick(60)``

84. ``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((1280, 720), self.mod_Pygame__.OPENGL|self.mod_Pygame__.DOUBLEBUF)``

85. ``¬ ¬ ¬ ¬ iteration = 0``
86. ``¬ ¬ ¬ ¬ FPScounter = 0``
87. ``¬ ¬ ¬ ¬ MaxIteration = 500``
88. ``¬ ¬ ¬ ¬ vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))``
89. ``¬ ¬ ¬ ¬ edges = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4), (6,7), (5,1), (5,4), (5,7))``

90. ``¬ ¬ ¬ ¬ self.mod_OGLbenchmark__.LoadOGLBenchmark.CreateBenchmark(self)``

91. ``¬ ¬ ¬ ¬ while iteration < 7500:``
92. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running OpenGL Benchmark @ {SetFPS[FPScounter]} FPS")``
93. ``¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:``
94. ``¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:``
95.  ``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX3.append(iteration)``
96.  ``¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY3.append(self.clock.get_fps())``
97.  ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_OGLbenchmark__.LoadOGLBenchmark.RunBenchmark(self, edges, vertices)``
98.  ``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
99.  ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):``
100. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``

101. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
102. ``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``
103. ``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])``
104. ``¬ ¬ ¬ ¬ ¬ FPScounter += 1``
105. ``¬ ¬ ¬ ¬ ¬ MaxIteration += 500``

106. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Finished Animated Benchmark")``
107. ``¬ ¬ ¬ ¬ self.mod_Time__.sleep(5)``
108. ``¬ ¬ ¬ except Exception as Message:``
109. ``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
110. ``¬ ¬ ¬ ¬ return Message, None, None, None, None``
111. ``¬ ¬ ¬ else:``

112. ``¬ ¬ ¬ ¬ return None, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3``

.. note::
For information on this consult the above guide
    1.   ``else:``
    2.   ``¬ print("You need to run this as part of Pycraft")``
    3.   ``¬ import tkinter as tk``
    4.   ``¬ from tkinter import messagebox``
    5.   ``¬ root = tk.Tk()``
    6.   ``¬ root.withdraw()``
    7.   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    8.   ``¬ quit()``


GameEngine
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

1. ``if not __name__ == "__main__":``
2. ``¬ print("Started <Pycraft_GameEngine>")``

3. ``¬ from ShareDataUtil import Class_Startup_variables as SharedData``

4. ``¬ SharedData.mod_ModernGL_window_.setup_basic_logging(0)``

5. ``¬ class Cubemap(SharedData.mod_Base__.CameraWindow):``
6. ``¬ ¬ SharedData.mod_Base__.CameraWindow.title = f"Pycraft: v{SharedData.version}: Playing"``
7. ``¬ ¬ SharedData.mod_Base__.CameraWindow.resource_dir = SharedData.base_folder``

8. ``¬ ¬ def Exit(self, SharedData, Command):``
9. ``¬ ¬ ¬ try:``
10. ``¬ ¬ ¬ ¬ if SharedData.mod_Pygame__.mixer.Channel(3).get_busy() == True:``
11. ``¬ ¬ ¬ ¬ ¬ SharedData.mod_Pygame__.mixer.Channel(3).stop()``
12. ``¬ ¬ ¬ ¬ ¬ SharedData.mod_Pygame__.quit()``

13. ``¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = False``
14. ``¬ ¬ ¬ except Exception as Error:``
15. ``¬ ¬ ¬ ¬ print("GE", Error)``
16. ``¬ ¬ ¬ ¬ pass``
17. ``¬ ¬ ¬ self.wnd._set_fullscreen(False)``
18. ``¬ ¬ ¬ self.wnd.close()``
19. ``¬ ¬ ¬ self.wnd.destroy()``
20. ``¬ ¬ ¬ SharedData.CurrentlyPlaying = None``
21. ``¬ ¬ ¬ SharedData.LoadMusic = True``
22. ``¬ ¬ ¬ SharedData.Command = Command``
23. ``¬ ¬ ¬ if self.wnd.fullscreen == True:``
24. ``¬ ¬ ¬ ¬ SharedData.Fullscreen = False``
25. ``¬ ¬ ¬ else:``
26. ``¬ ¬ ¬ ¬ SharedData.Fullscreen = True``

27. ``¬ ¬ def __init__(self, **kwargs):``
28. ``¬ ¬ ¬ try:``
29. ``¬ ¬ ¬ ¬ super().__init__(**kwargs)``

30. ``¬ ¬ ¬ ¬ self.size = self.wnd.buffer_size``

31. ``¬ ¬ ¬ ¬ WindowSize = SharedData.realWidth, SharedData.realHeight``
32. ``¬ ¬ ¬ ¬ CurrentWindowSize = WindowSize``

33. ``¬ ¬ ¬ ¬ self.wnd.size = WindowSize``
34. ``¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = False``

35. ``¬ ¬ ¬ ¬ self.camera.projection.update(near=0.1, far=100.0)``
36. ``¬ ¬ ¬ ¬ self.camera.zoom = 2.5``

37. ``¬ ¬ ¬ ¬ self.obj = self.load_scene(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\Map\\map.obj")))``

38. ``¬ ¬ ¬ ¬ self.cube = SharedData.mod_ModernGL_window_.geometry.cube(size=(20, 20, 20))``

39. ``¬ ¬ ¬ ¬ self.prog = self.load_program(SharedData.mod_OS__.path.join(SharedData.base_folder, ("programs//cubemap.glsl")))``

40. ``¬ ¬ ¬ ¬ self.SkyBox_texture = self.load_texture_cube(``
41. ``¬ ¬ ¬ ¬ ¬ neg_x=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg")),``
42. ``¬ ¬ ¬ ¬ ¬ neg_y=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg")),``
43. ``¬ ¬ ¬ ¬ ¬ neg_z=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg")),``
44. ``¬ ¬ ¬ ¬ ¬ pos_x=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg")),``
45. ``¬ ¬ ¬ ¬ ¬ pos_y=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg")),``
46. ``¬ ¬ ¬ ¬ ¬ pos_z=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg")),``
47. ``¬ ¬ ¬ ¬ ¬ flip_x=True,)``

48. ``¬ ¬ ¬ ¬ Prev_Mouse_Pos = (0,0)``
49. ``¬ ¬ ¬ ¬ Mouse_Pos = (0,0)``
50. ``¬ ¬ ¬ ¬ DeltaX, DeltaY = 0, 0``

51. ``¬ ¬ ¬ ¬ self.wnd.exit_key = None``

52. ``¬ ¬ ¬ ¬ MouseUnlock = True``

53. ``¬ ¬ ¬ ¬ Jump = False``
54. ``¬ ¬ ¬ ¬ JumpID = 0``

55. ``¬ ¬ ¬ ¬ self.camera.position.y += 0.7``

56. ``¬ ¬ ¬ ¬ WkeydownTimer = 0``
57. ``¬ ¬ ¬ ¬ AkeydownTimer = 0``
58. ``¬ ¬ ¬ ¬ SkeydownTimer = 0``
59. ``¬ ¬ ¬ ¬ DkeydownTimer = 0``

60. ``¬ ¬ ¬ ¬ RunForwardTimer = 0``

61. ``¬ ¬ ¬ ¬ FPS = 0``

62. ``¬ ¬ ¬ ¬ Iteration = 0``

63. ``¬ ¬ ¬ ¬ while True:``
64. ``¬ ¬ ¬ ¬ ¬ try:``
65. ``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.mod_Pygame__.mixer.get_busy() == False:``
66. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayAmbientSound(SharedData)``
67. ``¬ ¬ ¬ ¬ ¬ except Exception as Error:``
68. ``¬ ¬ ¬ ¬ ¬ ¬ print(Error)``
69. ``¬ ¬ ¬ ¬ ¬ ¬ pass``

70. ``¬ ¬ ¬ ¬ ¬ if Iteration == 0:``
71. ``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.Fullscreen == False:``
72. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.fullscreen = True``
73. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
74. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.fixed_aspect_ratio = SharedData.realWidth / SharedData.realHeight``
75. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.window_size = SharedData.realWidth, SharedData.realHeight``
76. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ CurrentWindowSize = self.window_size``
77. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.position = (int((SharedData.FullscreenX-CurrentWindowSize[0])/2), int((SharedData.FullscreenY-CurrentWindowSize[1])/2))``

78. ``¬ ¬ ¬ ¬ ¬ if Iteration >= 5000:``
79. ``¬ ¬ ¬ ¬ ¬ ¬ Iteration = 0``

80. ``¬ ¬ ¬ ¬ ¬ start = SharedData.mod_Time__.perf_counter()``

81. ``¬ ¬ ¬ ¬ ¬ self.ctx.clear(1.0, 1.0, 1.0)``

82. ``¬ ¬ ¬ ¬ ¬ CurrentWindowSize = self.window_size``

83. ``¬ ¬ ¬ ¬ ¬ Prev_Mouse_Pos = Mouse_Pos``
84. ``¬ ¬ ¬ ¬ ¬ Mouse_Pos = SharedData.mod_Pyautogui__.position()``
85. ``¬ ¬ ¬ ¬ ¬ DeltaX, DeltaY = Mouse_Pos[0]-Prev_Mouse_Pos[0], Mouse_Pos[1]-Prev_Mouse_Pos[1]``

86. ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.ESCAPE):``
87. ``¬ ¬ ¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "Undefined")``
88. ``¬ ¬ ¬ ¬ ¬ ¬ return None``
89. ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.W):``
90. ``¬ ¬ ¬ ¬ ¬ ¬ RunForwardTimer += (1/FPS)``
91. ``¬ ¬ ¬ ¬ ¬ ¬ if RunForwardTimer <= 10:``
92. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``
93. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer += (1/FPS)``
94. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if WkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``
95. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
96. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer = 0``
97. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.x += 1.42``
98. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
99. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``
100. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer += (1/FPS)``
101. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if WkeydownTimer >= (SharedData.mod_Random__.randint(25, 75)/100):``
102. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
103. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ WkeydownTimer = 0``
104. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.x += 2.2352``
105. ``¬ ¬ ¬ ¬ ¬ else:``
106. ``¬ ¬ ¬ ¬ ¬ ¬ RunForwardTimer = 0``

107. ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.A):``
108. ``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``
109. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ AkeydownTimer += (1/FPS)``
110. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if AkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``
111. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
112. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AkeydownTimer = 0``
113. ``¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.z += 1.42``

114. ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.S):``
115. ``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``
116. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ SkeydownTimer += (1/FPS)``
117. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if SkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``
118. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
119. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SkeydownTimer = 0``
120. ``¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.x -= 1.42``

121. ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.D):``
122. ``¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``
123. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ DkeydownTimer += (1/FPS)``
124. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if DkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):``
125. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
126. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ DkeydownTimer = 0``
127. ``¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.z -= 1.42``

128. ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.E):``
129. ``¬ ¬ ¬ ¬ ¬ ¬ if self.wnd._fullscreen == True:``
130. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot = SharedData.mod_Pyautogui__.screenshot(region=((0, 0, SharedData.FullscreenX, SharedData.FullscreenY)))``
131. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot.save(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))``
132. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
133. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ PosX, PosY = self.wnd.position``
134. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot = SharedData.mod_Pyautogui__.screenshot(region=((PosX, PosY, SharedData.realWidth, SharedData.realHeight)))``
135. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ myScreenshot.save(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))``

136. ``¬ ¬ ¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "Inventory")``
137. ``¬ ¬ ¬ ¬ ¬ ¬ return None``

138. ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.R):``
139. ``¬ ¬ ¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "MapGUI")``
140. ``¬ ¬ ¬ ¬ ¬ ¬ return None``
141. ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.L):``
142. ``¬ ¬ ¬ ¬ ¬ ¬ if MouseUnlock == True:``
143. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ MouseUnlock = False``
144. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
145. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ MouseUnlock = True``
146. ``¬ ¬ ¬ ¬ ¬ if self.wnd.is_key_pressed(self.wnd.keys.SPACE):``
147. ``¬ ¬ ¬ ¬ ¬ ¬ Jump = True``
148. ``¬ ¬ ¬ ¬ ¬ ¬ JumpUP = True``

149. ``¬ ¬ ¬ ¬ ¬ if Jump == True:``
150. ``¬ ¬ ¬ ¬ ¬ ¬ if JumpID < 10 and JumpUP == True:``
151. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpID += 1``
152. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.y += 0.1``
153. ``¬ ¬ ¬ ¬ ¬ ¬ if JumpID == 10:``
154. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpUP = False``
155. ``¬ ¬ ¬ ¬ ¬ ¬ if JumpID >= 0 and JumpUP == False:``
156. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpID -= 1``
157. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.position.y -= 0.1``
158. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if JumpID == 0:``
159. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if SharedData.sound == True:``
160. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)``
161. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Jump = False``
162. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ JumpID = 0``

163. ``¬ ¬ ¬ ¬ ¬ self.ctx.enable(SharedData.mod_ModernGL__.CULL_FACE | SharedData.mod_ModernGL__.DEPTH_TEST)``

164. ``¬ ¬ ¬ ¬ ¬ cam = self.camera.matrix``
165. ``¬ ¬ ¬ ¬ ¬ cam[3][0] = 0``
166. ``¬ ¬ ¬ ¬ ¬ cam[3][1] = 0``
167. ``¬ ¬ ¬ ¬ ¬ cam[3][2] = 0``

168. ``¬ ¬ ¬ ¬ ¬ self.SkyBox_texture.use(location=0)``
169. ``¬ ¬ ¬ ¬ ¬ self.prog['m_proj'].write(self.camera.projection.matrix)``
170. ``¬ ¬ ¬ ¬ ¬ self.prog['m_camera'].write(cam)``

171. ``¬ ¬ ¬ ¬ ¬ try:``
172. ``¬ ¬ ¬ ¬ ¬ ¬ if MouseUnlock == True:¬ ¬ ¬ ¬ ¬ ¬ ``
173. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.camera.rot_state(-DeltaX, -DeltaY)``
174. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = True``
175. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
176. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = False``
177. ``¬ ¬ ¬ ¬ ¬ except Exception as Error:``
178. ``¬ ¬ ¬ ¬ ¬ ¬ print(Error)``
179. ``¬ ¬ ¬ ¬ ¬ ¬ pass``

180. ``¬ ¬ ¬ ¬ ¬ self.ctx.front_face = 'cw'``
181. ``¬ ¬ ¬ ¬ ¬ self.cube.render(self.prog)``

182. ``¬ ¬ ¬ ¬ ¬ self.ctx.front_face = 'ccw'``
183. ``¬ ¬ ¬ ¬ ¬ self.obj.draw(projection_matrix=self.camera.projection.matrix, camera_matrix=self.camera.matrix)``

184. ``¬ ¬ ¬ ¬ ¬ try:``
185. ``¬ ¬ ¬ ¬ ¬ ¬ self.wnd.swap_buffers()``
186. ``¬ ¬ ¬ ¬ ¬ except Exception as Error:``
187. ``¬ ¬ ¬ ¬ ¬ ¬ print(Error)``
188. ``¬ ¬ ¬ ¬ ¬ ¬ pass``

189. ``¬ ¬ ¬ ¬ ¬ FPS = 1/(SharedData.mod_Time__.perf_counter()-start)``
190. ``¬ ¬ ¬ ¬ ¬ Iteration += 1``
191. ``¬ ¬ ¬ except Exception as Message:``
192. ``¬ ¬ ¬ ¬ print(''.join(SharedData.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
193. ``¬ ¬ ¬ ¬ Cubemap.Exit(self, SharedData, "Undefined")``
194. ``¬ ¬ ¬ ¬ SharedData.GameError = str(Message)``
195. ``¬ ¬ ¬ ¬ return None``

196. ``¬ class CreateEngine:``

197. ``¬ ¬ def __init__(self):``
198. ``¬ ¬ ¬ pass``

199. ``¬ ¬ def GenerateLoadDisplay(self, LoadingFont, text, MainTitleFont, SecondaryFont, LoadingTextFont):``
200. ``¬ ¬ ¬ try:``
201. ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

202. ``¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``

203. ``¬ ¬ ¬ ¬ PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
204. ``¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``
205. ``¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))``

206. ``¬ ¬ ¬ ¬ LoadingTitle = SecondaryFont.render("Loading", self.aa, self.SecondFontCol)``
207. ``¬ ¬ ¬ ¬ self.Display.blit(LoadingTitle, (((self.realWidth-TitleWidth)/2)+55, 50))``

208. ``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (self.ShapeCol), self.aa, [(100, self.realHeight-100), (self.realWidth-100, self.realHeight-100)], 3)``
209. ``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (self.AccentCol), self.aa, self.Progress_Line)``

210. ``¬ ¬ ¬ ¬ DisplayMessage = LoadingFont.render(self.ProgressMessageText, self.aa, self.FontCol)``
211. ``¬ ¬ ¬ ¬ DisplayMessageWidth = DisplayMessage.get_width()``
212. ``¬ ¬ ¬ ¬ self.Display.blit(DisplayMessage, ((self.realWidth-DisplayMessageWidth)/2, self.realHeight-120))``

213. ``¬ ¬ ¬ ¬ TextFontRendered = LoadingTextFont.render(f"{text}", self.aa, self.FontCol)``
214. ``¬ ¬ ¬ ¬ TextFontRenderedWidth = TextFontRendered.get_width()``
215. ``¬ ¬ ¬ ¬ self.Display.blit(TextFontRendered, ((self.realWidth-TextFontRenderedWidth)/2, self.realHeight-100))``
216. ``¬ ¬ ¬ except Exception as error:``
217. ``¬ ¬ ¬ ¬ print(error)``

218. ``¬ ¬ def Play(self):``
219. ``¬ ¬ ¬ try:``
220. ``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).fadeout(2000)``
221. ``¬ ¬ ¬ ¬ ``
222. ``¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_WAIT)``

223. ``¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
224. ``¬ ¬ ¬ ¬ self.mod_Pygame__.init()``
225. ``¬ ¬ ¬ ¬ self.mod_Globals__.Share.initialize(self)``
226. ``¬ ¬ ¬ ¬ try:``
227. ``¬ ¬ ¬ ¬ ¬ self.mod_ModernGL_window_.run_window_config(Cubemap)``
228. ``¬ ¬ ¬ ¬ except Exception as Error:``
229. ``¬ ¬ ¬ ¬ ¬ print(Error)``
230. ``¬ ¬ ¬ ¬ ¬ pass``
231. ``¬ ¬ ¬ ¬ return None``
232. ``¬ ¬ ¬ except Exception as Message:``
233. ``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
234. ``¬ ¬ ¬ ¬ return Message, "Undefined"``

.. note::
    For information on this consult the above guide
    1.   ``else:``
    2.   ``¬ print("You need to run this as part of Pycraft")``
    3.   ``¬ import tkinter as tk``
    4.   ``¬ from tkinter import messagebox``
    5.   ``¬ root = tk.Tk()``
    6.   ``¬ root.withdraw()``
    7.   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    8.   ``¬ quit()``


GetSavedData
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_GetSavedData>")``
    3. ``¬ class LoadSaveFiles:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

1. ``¬ ¬ def ReadMainSave(self):``
2. ``¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'r') as openfile:``
3. ``¬ ¬ ¬ ¬ save = self.mod_JSON__.load(openfile)``
4.  ``¬ ¬ ¬ self.theme = save["theme"]``
5.  ``¬ ¬ ¬ self.RunFullStartup = save["startup"]``
6.  ``¬ ¬ ¬ self.crash = save["crash"]``
7.  ``¬ ¬ ¬ self.Fullscreen = save["WindowStatus"]``
8.  ``¬ ¬ ¬ self.RecommendedFPS = save["AdaptiveFPS"]``
9.  ``¬ ¬ ¬ self.Devmode = save["Devmode"]``
10. ``¬ ¬ ¬ self.SettingsPreference = save["profile"]``
11. ``¬ ¬ ¬ self.FPS = save["FPS"]``
12. ``¬ ¬ ¬ self.aFPS = save["aFPS"]``
13. ``¬ ¬ ¬ self.Iteration = save["Iteration"]``
14. ``¬ ¬ ¬ self.FOV = save["FOV"]``
15. ``¬ ¬ ¬ self.cameraANGspeed = save["cameraANGspeed"]``
16. ``¬ ¬ ¬ self.RenderFOG = save["RenderFOG"]``
17. ``¬ ¬ ¬ self.aa = save["aa"]``
18. ``¬ ¬ ¬ self.X = save["X"]``
19. ``¬ ¬ ¬ self.Y = save["Y"]``
20. ``¬ ¬ ¬ self.Z = save["Z"]``
21. ``¬ ¬ ¬ self.FanSky = save["FanSky"]``
22. ``¬ ¬ ¬ self.FanPart = save["FanPart"]``
23. ``¬ ¬ ¬ self.sound = save["sound"]``
24. ``¬ ¬ ¬ self.soundVOL = save["soundVOL"]``
25. ``¬ ¬ ¬ self.music = save["music"]``
26. ``¬ ¬ ¬ self.musicVOL = save["musicVOL"]``
27. ``¬ ¬ ¬ self.lastRun = save["lastRun"]``
28. ``¬ ¬ ¬ self.SavedWidth = save["DisplayWidth"]``
29. ``¬ ¬ ¬ self.SavedHeight = save["DisplayHeight"]``
30. ``¬ ¬ ¬ self.Total_Vertices = save["Total_Vertices"]``
31. ``¬ ¬ ¬ if self.Total_Vertices == 0:``
32. ``¬ ¬ ¬ ¬ self.Total_Vertices = 1``

33. ``¬ ¬ def RepairLostSave(self):``
34. ``¬ ¬ ¬ try:``
35. ``¬ ¬ ¬ ¬ SavedData = {"Total_Vertices":0, "theme":False, "profile":"Medium", "Devmode":0, "AdaptiveFPS": 60, "FPS":60, "aFPS":60, "Iteration":1, "FOV":75, "cameraANGspeed":3, "aa":True, "RenderFOG":True, "FanSky":True, "FanPart":True, "sound":True, "soundVOL":75, "music":True, "musicVOL":50, "X":0, "Y":0, "Z":0, "lastRun":"29/09/2021", 'startup':True, 'crash': False, 'DisplayWidth':1280, 'DisplayHeight':720, 'WindowStatus':True}``
36. ``¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'w') as openfile:``
37. ``¬ ¬ ¬ ¬ ¬ self.mod_JSON__.dump(SavedData, openfile)``
38. ``¬ ¬ ¬ except Exception as Message:``
39. ``¬ ¬ ¬ ¬ return Message``
40. ``¬ ¬ ¬ else:``
41. ``¬ ¬ ¬ ¬ return None``

42. ``¬ ¬ def SaveTOconfigFILE(self):``
43. ``¬ ¬ ¬ try:``
44. ``¬ ¬ ¬ ¬ current_time = self.mod_Datetime__.datetime.now()``
45. ``¬ ¬ ¬ ¬ currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"``
46. ``¬ ¬ ¬ ¬ SavedData = {"Total_Vertices":self.Total_Vertices, "theme":self.theme, "profile":self.SettingsPreference, "Devmode":self.Devmode, "AdaptiveFPS": self.RecommendedFPS, "FPS":self.FPS, "aFPS":self.aFPS, "Iteration":self.Iteration, "FOV":self.FOV, "cameraANGspeed":self.cameraANGspeed, "aa":self.aa, "RenderFOG":self.RenderFOG, "FanSky":self.FanSky, "FanPart":self.FanPart, "sound":self.sound, "soundVOL":self.soundVOL, "music":self.music, "musicVOL":self.musicVOL, "X":self.X, "Y":self.Y, "Z":self.Z, "lastRun":currentDate, 'startup':self.RunFullStartup, 'crash': False, 'DisplayWidth':self.SavedWidth, 'DisplayHeight':self.SavedHeight, 'WindowStatus':self.Fullscreen}``
47. ``¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'w') as openfile:``
48. ``¬ ¬ ¬ ¬ ¬ self.mod_JSON__.dump(SavedData, openfile)``
49. ``¬ ¬ ¬ except Exception as Message:``
50. ``¬ ¬ ¬ ¬ return Message``
51. ``¬ ¬ ¬ else:``
52. ``¬ ¬ ¬ ¬ return None``

.. note::
    For information on this consult the above guide
    60. ``else:``
    61. ``¬ print("You need to run this as part of Pycraft")``
    62. ``¬ import tkinter as tk``
    63. ``¬ from tkinter import messagebox``
    64. ``¬ root = tk.Tk()``
    65. ``¬ root.withdraw()``
    66. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    67. ``¬ quit()``


HomeScreen
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_HomeScreen>")``
    3. ``¬ class GenerateHomeScreen:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def DisplayMessage(self, MessageFont, Message, Colour):``
7. ``¬ ¬ ¬ MessageText = MessageFont.render(Message, self.aa, Colour)``
8. ``¬ ¬ ¬ MessageTextWidth = MessageText.get_width()``
9. ``¬ ¬ ¬ MessageTextHeight = MessageText.get_height()``
10. ``¬ ¬ ¬ self.Display.blit(MessageText, ((self.realWidth-MessageTextWidth)/2, (self.realHeight-MessageTextHeight)))``

11. ``¬ ¬ def Home_Screen(self):``
12. ``¬ ¬ ¬ try:``
13. ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
14. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
15. ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Home screen")``
16. ``¬ ¬ ¬ ¬ Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()``
17. ``¬ ¬ ¬ ¬ SelectorWidth = Selector.get_width()``
18. ``¬ ¬ ¬ ¬ hover1 = False``
19. ``¬ ¬ ¬ ¬ hover2 = False``
20. ``¬ ¬ ¬ ¬ hover3 = False``
21. ``¬ ¬ ¬ ¬ hover4 = False``
22. ``¬ ¬ ¬ ¬ hover5 = False``
23. ``¬ ¬ ¬ ¬ hover6 = False``
24. ``¬ ¬ ¬ ¬ mousebuttondown = False``

25. ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
26. ``¬ ¬ ¬ ¬ PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
27. ``¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``
28. ``¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
29. ``¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))``
30. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``

31. ``¬ ¬ ¬ ¬ SideFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``
32. ``¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``
33. ``¬ ¬ ¬ ¬ ButtonFont1 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
34. ``¬ ¬ ¬ ¬ ButtonFont2 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
35. ``¬ ¬ ¬ ¬ ButtonFont3 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
36. ``¬ ¬ ¬ ¬ ButtonFont4 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
37. ``¬ ¬ ¬ ¬ ButtonFont5 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
38. ``¬ ¬ ¬ ¬ ButtonFont6 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
39. ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
40. ``¬ ¬ ¬ ¬ MessageFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)``

41. ``¬ ¬ ¬ ¬ oldTHEME = self.theme``
42. ``¬ ¬ ¬ ¬ tempFPS = self.FPS``
43. ``¬ ¬ ¬ ¬ coloursARRAY = []``

44. ``¬ ¬ ¬ ¬ anim = False``

45. ``¬ ¬ ¬ ¬ special = [30, 30, 30]``
46. ``¬ ¬ ¬ ¬ TargetARRAY = []``

47. ``¬ ¬ ¬ ¬ ColourDisplacement = 80``

48. ``¬ ¬ ¬ ¬ increment = False``
49. ``¬ ¬ ¬ ¬ while True:``
50. ``¬ ¬ ¬ ¬ ¬ coloursARRAY = []``
51. ``¬ ¬ ¬ ¬ ¬ if anim == True:``
52. ``¬ ¬ ¬ ¬ ¬ ¬ anim = False``
53. ``¬ ¬ ¬ ¬ ¬ ¬ TargetARRAY = []``
54. ``¬ ¬ ¬ ¬ ¬ ¬ for a in range(self.mod_Random__.randint(0, 32)):``
55. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ TargetARRAY.append(a)``

56. ``¬ ¬ ¬ ¬ ¬ if len(TargetARRAY) == 0:``
57. ``¬ ¬ ¬ ¬ ¬ ¬ TargetARRAY = [33]``
58. ``¬ ¬ ¬ ¬ ¬ for i in range(32):``
59. ``¬ ¬ ¬ ¬ ¬ ¬ for j in range(len(TargetARRAY)):``
60. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if i == TargetARRAY[j]:``
61. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ coloursARRAY.append(special)``
62. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
63. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ coloursARRAY.append(self.ShapeCol)``

64. ``¬ ¬ ¬ ¬ ¬ if increment == False:``
65. ``¬ ¬ ¬ ¬ ¬ ¬ if self.aFPS == 0 or self.Iteration == 0:``
66. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement -= (self.mod_Random__.randint(0,10)/((self.FPS)/4))``
67. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
68. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement -= (self.mod_Random__.randint(0,10)/((self.aFPS/self.Iteration)/4))``
69. ``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = ColourDisplacement, ColourDisplacement, ColourDisplacement``
70. ``¬ ¬ ¬ ¬ ¬ if increment == True:``
71. ``¬ ¬ ¬ ¬ ¬ ¬ if self.aFPS == 0 or self.Iteration == 0:``
72. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement += (self.mod_Random__.randint(0,10)/((self.FPS)/4))``
73. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
74. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ColourDisplacement += (self.mod_Random__.randint(0,10)/((self.aFPS/self.Iteration)/4))``
75. ``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = ColourDisplacement, ColourDisplacement, ColourDisplacement``
76. ``¬ ¬ ¬ ¬ ¬ if special[0] <= 30:``
77. ``¬ ¬ ¬ ¬ ¬ ¬ increment = True``
78. ``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = 30, 30, 30``
79. ``¬ ¬ ¬ ¬ ¬ if special[0] >= 80:``
80. ``¬ ¬ ¬ ¬ ¬ ¬ increment = False``
81. ``¬ ¬ ¬ ¬ ¬ ¬ anim = True``
82. ``¬ ¬ ¬ ¬ ¬ ¬ special[0], special[1], special[2] = 80, 80, 80``

83. ``¬ ¬ ¬ ¬ ¬ if self.mod_Pygame__.mixer.Channel(3).get_busy() == 1:``
84. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(3).stop()``

85. ``¬ ¬ ¬ ¬ ¬ if str(self.Display) == "<Surface(Dead Display)>":``
86. ``¬ ¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:``
87. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``
88. ``¬ ¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:``
89. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``

90. ``¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
91. ``¬ ¬ ¬ ¬ ¬ if not (self.realWidth == self.FullscreenX and self.realHeight == self.FullscreenY):``
92. ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedWidth, self.SavedHeight = self.mod_Pygame__.display.get_window_size()``

93. ``¬ ¬ ¬ ¬ ¬ if self.SavedWidth == self.FullscreenX:``
94. ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280``
95. ``¬ ¬ ¬ ¬ ¬ if self.SavedHeight == self.FullscreenY:``
96. ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720``

97. ``¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
98. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
99. ``¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
100. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

101. ``¬ ¬ ¬ ¬ ¬ yScaleFact = self.realHeight/720``
102. ``¬ ¬ ¬ ¬ ¬ xScaleFact = self.realWidth/1280``

103. ``¬ ¬ ¬ ¬ ¬ if not oldTHEME == self.theme:``
104. ``¬ ¬ ¬ ¬ ¬ ¬ Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()``
105. ``¬ ¬ ¬ ¬ ¬ ¬ SelectorWidth = Selector.get_width()``
106. ``¬ ¬ ¬ ¬ ¬ ¬ oldTHEME = self.theme``

107. ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``

108. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
109. ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
110. ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``
111. ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``
112. ``¬ ¬ ¬ ¬ ¬ Mx, My = self.mod_Pygame__.mouse.get_pos()``
113. ``¬ ¬ ¬ ¬ ¬ PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
114. ``¬ ¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``

115. ``¬ ¬ ¬ ¬ ¬ Name = SideFont.render("By Tom Jebbo", self.aa, self.FontCol)``
116. ``¬ ¬ ¬ ¬ ¬ NameHeight = Name.get_height()``

117. ``¬ ¬ ¬ ¬ ¬ Version = VersionFont.render(f"Version: {self.version}", self.aa, self.FontCol)``
118. ``¬ ¬ ¬ ¬ ¬ VersionWidth = Version.get_width()``
119. ``¬ ¬ ¬ ¬ ¬ VersionHeight = Version.get_height()``

120. ``¬ ¬ ¬ ¬ ¬ Play = ButtonFont1.render("Play", self.aa, self.FontCol)``
121. ``¬ ¬ ¬ ¬ ¬ PlayWidth = Play.get_width()``

122. ``¬ ¬ ¬ ¬ ¬ SettingsText = ButtonFont2.render("Settings", self.aa, self.FontCol)``
123. ``¬ ¬ ¬ ¬ ¬ SettingsWidth = SettingsText.get_width()``

124. ``¬ ¬ ¬ ¬ ¬ Character_DesignerText = ButtonFont3.render("Character Designer", self.aa, self.FontCol)``
125. ``¬ ¬ ¬ ¬ ¬ CharDesignerWidth = Character_DesignerText.get_width()``

126. ``¬ ¬ ¬ ¬ ¬ AchievementsText = ButtonFont4.render("Achievements", self.aa, self.FontCol)``
127. ``¬ ¬ ¬ ¬ ¬ AchievementsWidth = AchievementsText.get_width()``

128. ``¬ ¬ ¬ ¬ ¬ Credits_and_Change_Log_Text = ButtonFont5.render("Credits", self.aa, self.FontCol)``
129. ``¬ ¬ ¬ ¬ ¬ CreditsWidth = Credits_and_Change_Log_Text.get_width()``

130. ``¬ ¬ ¬ ¬ ¬ BenchmarkText = ButtonFont6.render("Benchmark", self.aa, self.FontCol)``
131. ``¬ ¬ ¬ ¬ ¬ BenchmarkWidth = BenchmarkText.get_width()``

132. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
133. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``
134. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
135. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
136. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "saveANDexit"``
137. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYDOWN:``
138. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:``
139. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``
140. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
141. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
142. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
143. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
144. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``
145. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``
146. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:``
147. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True``
148. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONUP:``
149. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

150. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Home screen")``

151. ``¬ ¬ ¬ ¬ ¬ ButtonFont1.set_underline(hover1)``
152. ``¬ ¬ ¬ ¬ ¬ ButtonFont2.set_underline(hover2)``
153. ``¬ ¬ ¬ ¬ ¬ ButtonFont3.set_underline(hover3)``
154. ``¬ ¬ ¬ ¬ ¬ ButtonFont4.set_underline(hover4)``
155. ``¬ ¬ ¬ ¬ ¬ ButtonFont5.set_underline(hover5)``
156. ``¬ ¬ ¬ ¬ ¬ ButtonFont6.set_underline(hover6)``

157. ``¬ ¬ ¬ ¬ ¬ if My >= 202*yScaleFact and My <= 247*yScaleFact and Mx >= (self.realWidth-(PlayWidth+SelectorWidth))-2:``
158. ``¬ ¬ ¬ ¬ ¬ ¬ hover1 = True``
159. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
160. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
161. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
162. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Play"``
163. ``¬ ¬ ¬ ¬ ¬ else:``
164. ``¬ ¬ ¬ ¬ ¬ ¬ hover1 = False``
165. ``¬ ¬ ¬ ¬ ¬ ``
166. ``¬ ¬ ¬ ¬ ¬ if My >= 252*yScaleFact and My <= 297*yScaleFact and Mx >= (self.realWidth-(SettingsWidth+SelectorWidth))-2:``
167. ``¬ ¬ ¬ ¬ ¬ ¬ hover2 = True``
168. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
169. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
170. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
171. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
172. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
173. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Settings"``
174. ``¬ ¬ ¬ ¬ ¬ else:``
175. ``¬ ¬ ¬ ¬ ¬ ¬ hover2 = False``

176. ``¬ ¬ ¬ ¬ ¬ if My >= 302*yScaleFact and My <= 347*yScaleFact and Mx >= (self.realWidth-(CharDesignerWidth+SelectorWidth)-2):``
177. ``¬ ¬ ¬ ¬ ¬ ¬ hover3 = True``
178. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
179. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
180. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
181. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
182. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
183. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "CharacterDesigner"``
184. ``¬ ¬ ¬ ¬ ¬ else:``
185. ``¬ ¬ ¬ ¬ ¬ ¬ hover3 = False``

186. ``¬ ¬ ¬ ¬ ¬ if My >= 402*yScaleFact and My <= 447*yScaleFact and Mx >= (self.realWidth-(AchievementsWidth+SelectorWidth)-2):``
187. ``¬ ¬ ¬ ¬ ¬ ¬ hover4 = True``
188. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
189. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
190. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
191. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
192. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
193. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Achievements"``
194. ``¬ ¬ ¬ ¬ ¬ else:``
195. ``¬ ¬ ¬ ¬ ¬ ¬ hover4 = False``

196. ``¬ ¬ ¬ ¬ ¬ if My >= 352*yScaleFact and My <= 397*yScaleFact and Mx >= (self.realWidth-(CreditsWidth+SelectorWidth)-2):``
197. ``¬ ¬ ¬ ¬ ¬ ¬ hover5 = True``
198. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
199. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
200. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
201. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
202. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
203. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Credits"``
204. ``¬ ¬ ¬ ¬ ¬ else:``
205. ``¬ ¬ ¬ ¬ ¬ ¬ hover5 = False``

206. ``¬ ¬ ¬ ¬ ¬ if My >= 452*yScaleFact and My <= 497*yScaleFact and Mx >= (self.realWidth-(BenchmarkWidth+SelectorWidth)-2):``
207. ``¬ ¬ ¬ ¬ ¬ ¬ hover6 = True``
208. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
209. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
210. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
211. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
212. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
213. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None, "Benchmark"``
214. ``¬ ¬ ¬ ¬ ¬ else:``
215. ``¬ ¬ ¬ ¬ ¬ ¬ hover6 = False``

216. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
217. ``¬ ¬ ¬ ¬ ¬ ``
218. ``¬ ¬ ¬ ¬ ¬ if self.FromPlay == True:``
219. ``¬ ¬ ¬ ¬ ¬ ¬ self.FromPlay = False``
220. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_HomeScreen__.GenerateHomeScreen.DisplayMessage(self, MessageFont, "Loading", self.AccentCol)``

221. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))``

222. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Name, (0, (self.realHeight-NameHeight)))``
223. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Version, ((self.realWidth-VersionWidth)-2, (self.realHeight-VersionHeight)))``

224. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Play, ((self.realWidth-PlayWidth)-2, 200*yScaleFact))``
225. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(SettingsText, ((self.realWidth-SettingsWidth)-2, 250*yScaleFact))``
226. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Character_DesignerText, ((self.realWidth-CharDesignerWidth)-2, 300*yScaleFact))``
227. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits_and_Change_Log_Text, ((self.realWidth-CreditsWidth)-2, 350*yScaleFact))``
228. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsText, ((self.realWidth-AchievementsWidth)-2, 400*yScaleFact))``
229. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkText, ((self.realWidth-BenchmarkWidth)-2, 450*yScaleFact))``

230. ``¬ ¬ ¬ ¬ ¬ if hover1 == True:``
231. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(PlayWidth+SelectorWidth)-2, 200*yScaleFact))``
232. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
233. ``¬ ¬ ¬ ¬ ¬ elif hover2 == True:``
234. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(SettingsWidth+SelectorWidth)-2, 250*yScaleFact))``
235. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
236. ``¬ ¬ ¬ ¬ ¬ elif hover3 == True:``
237. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(CharDesignerWidth+SelectorWidth)-2, 300*yScaleFact))``
238. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
239. ``¬ ¬ ¬ ¬ ¬ elif hover5 == True:``
240. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(CreditsWidth+SelectorWidth)-2, 350*yScaleFact))``
241. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
242. ``¬ ¬ ¬ ¬ ¬ elif hover4 == True:``
243. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(AchievementsWidth+SelectorWidth)-2, 400*yScaleFact))``
244. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
245. ``¬ ¬ ¬ ¬ ¬ elif hover6 == True:``
246. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Selector, (self.realWidth-(BenchmarkWidth+SelectorWidth)-2, 450*yScaleFact))``
247. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
248. ``¬ ¬ ¬ ¬ ¬ else:``
249. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_ARROW)``

250. ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
251. ``¬ ¬ ¬ ¬ ¬ if not Message == None:``
252. ``¬ ¬ ¬ ¬ ¬ ¬ return Message, None``

253. ``¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, xScaleFact, yScaleFact, coloursARRAY)``

254. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
255. ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
256. ``¬ ¬ ¬ except Exception as Message:``
257. ``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
258. ``¬ ¬ ¬ ¬ return Message, None``

.. note::
    259.	For information on this consult the above guide
    260. ``else:``
    261. ``¬ print("You need to run this as part of Pycraft")``
    262. ``¬ import tkinter as tk``
    263. ``¬ from tkinter import messagebox``
    264. ``¬ root = tk.Tk()``
    265. ``¬ root.withdraw()``
    266. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    267. ``¬ quit()``


ImageUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_ImageUtils>")``
    3. ``¬ class ConvertImage:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

1. ``¬ ¬ def pilImageToSurface(self, pilImage):``
2. ``¬ ¬ ¬ return self.mod_Pygame__.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode).convert()``

.. note::
    For information on this consult the above guide
    8. ``else:``
    9. ``¬ print("You need to run this as part of Pycraft")``
    10. ``¬ import tkinter as tk``
    11. ``¬ from tkinter import messagebox``
    12. ``¬ root = tk.Tk()``
    13. ``¬ root.withdraw()``
    14. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    15. ``¬ quit()``


Inventory
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_Inventory>")``
    3. ``¬ class GenerateInventory:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def Inventory(self):``
7. ``¬ ¬ ¬ try:``
8. ``¬ ¬ ¬ ¬ Message = self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``
9. ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
10. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``

11. ``¬ ¬ ¬ ¬ MainInventoryFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
12. ``¬ ¬ ¬ ¬ PycraftTitle = MainInventoryFont.render("Pycraft", self.aa, self.FontCol)``
13. ``¬ ¬ ¬ ¬ TitleWidth = PycraftTitle.get_width()``

14. ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
15. ``¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
16. ``¬ ¬ ¬ ¬ AlphaSurface = self.mod_Pygame__.Surface((realWidth, realHeight), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)``
17. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
18. ``¬ ¬ ¬ ¬ AlphaSurface.set_alpha(204)``
19. ``¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``

20. ``¬ ¬ ¬ ¬ Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()``
21. ``¬ ¬ ¬ ¬ SelectorWidth = Selector.get_width()``

22. ``¬ ¬ ¬ ¬ hover1 = False``
23. ``¬ ¬ ¬ ¬ hover2 = False``
24. ``¬ ¬ ¬ ¬ hover3 = False``
25. ``¬ ¬ ¬ ¬ hover4 = False``
26. ``¬ ¬ ¬ ¬ hover5 = False``
27. ``¬ ¬ ¬ ¬ hover6 = False``
28. ``¬ ¬ ¬ ¬ hover7 = False``
29. ``¬ ¬ ¬ ¬ hover8 = False``
30. ``¬ ¬ ¬ ¬ mousebuttondown = False``

31. ``¬ ¬ ¬ ¬ ButtonFont1 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
32. ``¬ ¬ ¬ ¬ WeaponsText = ButtonFont1.render("Weapons", self.aa, self.FontCol)``
33. ``¬ ¬ ¬ ¬ WeaponsTextWidth = WeaponsText.get_width()``
34. ``¬ ¬ ¬ ¬ WeaponsTextHeight = WeaponsText.get_height()``

35. ``¬ ¬ ¬ ¬ ButtonFont2 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
36. ``¬ ¬ ¬ ¬ RangedWeaponsText = ButtonFont2.render("Ranged Weapons", self.aa, self.FontCol)``
37. ``¬ ¬ ¬ ¬ RangedWeaponsTextWidth = RangedWeaponsText.get_width()``
38. ``¬ ¬ ¬ ¬ RangedWeaponsTextHeight= RangedWeaponsText.get_height()``

39. ``¬ ¬ ¬ ¬ ButtonFont3 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
40. ``¬ ¬ ¬ ¬ ShieldsText = ButtonFont3.render("Shields", self.aa, self.FontCol)``
41. ``¬ ¬ ¬ ¬ ShieldsTextWidth = ShieldsText.get_width()``
42. ``¬ ¬ ¬ ¬ ShieldsTextHeight = ShieldsText.get_height()``

43. ``¬ ¬ ¬ ¬ ButtonFont4 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
44. ``¬ ¬ ¬ ¬ ArmourText = ButtonFont4.render("Armour", self.aa, self.FontCol)``
45. ``¬ ¬ ¬ ¬ ArmourTextWidth = ArmourText.get_width()``
46. ``¬ ¬ ¬ ¬ ArmourTextHeight = ArmourText.get_height()``

47. ``¬ ¬ ¬ ¬ ButtonFont5 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
48. ``¬ ¬ ¬ ¬ FoodText = ButtonFont5.render("Food", self.aa, self.FontCol)``
49. ``¬ ¬ ¬ ¬ FoodTextWidth = FoodText.get_width()``
50. ``¬ ¬ ¬ ¬ FoodTextHeight = FoodText.get_height()``

51. ``¬ ¬ ¬ ¬ ButtonFont6 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
52. ``¬ ¬ ¬ ¬ ItemsText = ButtonFont6.render("Items", self.aa, self.FontCol)``
53. ``¬ ¬ ¬ ¬ ItemsTextWidth = ItemsText.get_width()``
54. ``¬ ¬ ¬ ¬ ItemsTextHeight = ItemsText.get_height()``

55. ``¬ ¬ ¬ ¬ ButtonFont7 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
56. ``¬ ¬ ¬ ¬ SpecialItemsText = ButtonFont7.render("Special Items", self.aa, self.FontCol)``
57. ``¬ ¬ ¬ ¬ SpecialItemsTextWidth = SpecialItemsText.get_width()``
58. ``¬ ¬ ¬ ¬ SpecialItemsTextHeight = SpecialItemsText.get_height()``

59. ``¬ ¬ ¬ ¬ ButtonFont8 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
60. ``¬ ¬ ¬ ¬ OptionsText = ButtonFont7.render("Options", self.aa, self.FontCol)``
61. ``¬ ¬ ¬ ¬ OptionsTextWidth = OptionsText.get_width()``
62. ``¬ ¬ ¬ ¬ OptionsTextHeight = OptionsText.get_height()``

63. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Playing | Inventory")``

64. ``¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()``

65. ``¬ ¬ ¬ ¬ while True:``
66. ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

67. ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
68. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
69. ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
70. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

71. ``¬ ¬ ¬ ¬ ¬ yScaleFact = realHeight/720``
72. ``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``

73. ``¬ ¬ ¬ ¬ ¬ Mx, My = self.mod_Pygame__.mouse.get_pos()``
74. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``

75. ``¬ ¬ ¬ ¬ ¬ if self.aa == True:``
76. ``¬ ¬ ¬ ¬ ¬ ¬ pilImage = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png"))).resize((realWidth, realHeight), self.mod_PIL_Image_.ANTIALIAS)``
77. ``¬ ¬ ¬ ¬ ¬ else:``
78. ``¬ ¬ ¬ ¬ ¬ ¬ pilImage = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png"))).resize((realWidth, realHeight))``

79. ``¬ ¬ ¬ ¬ ¬ BLURRED_pilImage = pilImage.filter(self.mod_PIL_ImageFilter_.BoxBlur(4))``

80. ``¬ ¬ ¬ ¬ ¬ PauseImg = self.mod_ImageUtils__.ConvertImage.pilImageToSurface(self, BLURRED_pilImage)``
81. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(PauseImg, (0, 0))``
82. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AlphaSurface, (0, 0))``

83. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftTitle, ((realWidth-TitleWidth)/2, 0))``

84. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
85. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_e):``
86. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Load3D = False``
87. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
88. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
89. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
90. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.VIDEORESIZE:``
91. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
92. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface = self.mod_Pygame__.Surface((realWidth, realHeight), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)``
93. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.set_alpha(204)``
94. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``
95. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:``
96. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True``
97. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONUP:``
98. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
99.  ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYDOWN:``
100. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
101. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
102. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface = self.mod_Pygame__.Surface((FullscreenX, FullscreenY), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)``
103. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.set_alpha(204)``
104. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``
105. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
106. ``¬ ¬ ¬ ¬ ¬ if My >= 202*yScaleFact and My <= 247*yScaleFact and Mx >= 1155:``
107. ``¬ ¬ ¬ ¬ ¬ ¬ hover1 = True``
108. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
109. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
110. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
111. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
112. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
113. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
114. ``¬ ¬ ¬ ¬ ¬ else:``
115. ``¬ ¬ ¬ ¬ ¬ ¬ hover1 = False``

116. ``¬ ¬ ¬ ¬ ¬ if My >= 252*yScaleFact and My <= 297*yScaleFact and Mx >= 1105:``
117. ``¬ ¬ ¬ ¬ ¬ ¬ hover2 = True``
118. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
119. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
120. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
121. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
122. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
123. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
124. ``¬ ¬ ¬ ¬ ¬ else:``
125. ``¬ ¬ ¬ ¬ ¬ ¬ hover2 = False``

126. ``¬ ¬ ¬ ¬ ¬ if My >= 302*yScaleFact and My <= 347*yScaleFact and Mx >= 865:``
127. ``¬ ¬ ¬ ¬ ¬ ¬ hover3 = True``
128. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
129. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
130. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
131. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
132. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
133. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
134. ``¬ ¬ ¬ ¬ ¬ else:``
135. ``¬ ¬ ¬ ¬ ¬ ¬ hover3 = False``

136. ``¬ ¬ ¬ ¬ ¬ if My >= 402*yScaleFact and My <= 447*yScaleFact and Mx >= 1035:``
137. ``¬ ¬ ¬ ¬ ¬ ¬ hover4 = True``
138. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
139. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
140. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
141. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
142. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
143. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
144. ``¬ ¬ ¬ ¬ ¬ else:``
145. ``¬ ¬ ¬ ¬ ¬ ¬ hover4 = False``

146. ``¬ ¬ ¬ ¬ ¬ if My >= 352*yScaleFact and My <= 397*yScaleFact and Mx >= 880:``
147. ``¬ ¬ ¬ ¬ ¬ ¬ hover5 = True``
148. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
149. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
150. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
151. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
152. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
153. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
154. ``¬ ¬ ¬ ¬ ¬ else:``
155. ``¬ ¬ ¬ ¬ ¬ ¬ hover5 = False``

156. ``¬ ¬ ¬ ¬ ¬ if My >= 502*yScaleFact and My <= 547*yScaleFact and Mx >= 1095:``
157. ``¬ ¬ ¬ ¬ ¬ ¬ hover6 = True``
158. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
159. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
160. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
161. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
162. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
163. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
164. ``¬ ¬ ¬ ¬ ¬ else:``
165. ``¬ ¬ ¬ ¬ ¬ ¬ hover6 = False``

166. ``¬ ¬ ¬ ¬ ¬ if My >= 452*yScaleFact and My <= 497*yScaleFact and Mx >= 1095:``
167. ``¬ ¬ ¬ ¬ ¬ ¬ hover7 = True``
168. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
169. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
170. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
171. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
172. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
173. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
174. ``¬ ¬ ¬ ¬ ¬ else:``
175. ``¬ ¬ ¬ ¬ ¬ ¬ hover7 = False``

176. ``¬ ¬ ¬ ¬ ¬ if My >= 552*yScaleFact and My <= 597*yScaleFact and Mx >= 1095:``
177. ``¬ ¬ ¬ ¬ ¬ ¬ hover8 = True``
178. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
179. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
180. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
181. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
182. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
183. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
184. ``¬ ¬ ¬ ¬ ¬ else:``
185. ``¬ ¬ ¬ ¬ ¬ ¬ hover8 = False``

186. ``¬ ¬ ¬ ¬ ¬ ButtonFont1.set_underline(hover1)``
187. ``¬ ¬ ¬ ¬ ¬ ButtonFont2.set_underline(hover2)``
188. ``¬ ¬ ¬ ¬ ¬ ButtonFont3.set_underline(hover3)``
189. ``¬ ¬ ¬ ¬ ¬ ButtonFont4.set_underline(hover4)``
190. ``¬ ¬ ¬ ¬ ¬ ButtonFont5.set_underline(hover5)``
191. ``¬ ¬ ¬ ¬ ¬ ButtonFont6.set_underline(hover6)``
192. ``¬ ¬ ¬ ¬ ¬ ButtonFont7.set_underline(hover7)``
193. ``¬ ¬ ¬ ¬ ¬ ButtonFont8.set_underline(hover8)``
194. ``¬ ¬ ¬ ¬ ¬ AlphaSurface.fill(self.BackgroundCol)``

195. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(WeaponsText, ((realWidth-WeaponsTextWidth)-2, 200*yScaleFact)) # ???``

196. ``¬ ¬ ¬ ¬ ¬ if hover1 == True:``
197. ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(WeaponsTextWidth+SelectorWidth)-2, 200*yScaleFact))``

198. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(RangedWeaponsText, ((realWidth-RangedWeaponsTextWidth)-2, 250*yScaleFact))``
199. ``¬ ¬ ¬ ¬ ¬ if hover2 == True:``
200. ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(RangedWeaponsTextWidth+SelectorWidth)-2, 250*yScaleFact))``

201. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(ShieldsText, ((realWidth-ShieldsTextWidth)-2, 300*yScaleFact))``
202. ``¬ ¬ ¬ ¬ ¬ if hover3 == True:``
203. ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(ShieldsTextWidth+SelectorWidth)-2, 300*yScaleFact))``

204. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(ArmourText, ((realWidth-ArmourTextWidth)-2, 350*yScaleFact))``
205. ``¬ ¬ ¬ ¬ ¬ if hover4 == True:``
206. ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(FoodTextWidth+SelectorWidth)-2, 400*yScaleFact))``

207. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(FoodText, ((realWidth-FoodTextWidth)-2, 400*yScaleFact))``
208. ``¬ ¬ ¬ ¬ ¬ if hover5 == True:``
209. ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(ArmourTextWidth+SelectorWidth)-2, 350*yScaleFact))``

210. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(ItemsText, ((realWidth-ItemsTextWidth)-2, 450*yScaleFact))``
211. ``¬ ¬ ¬ ¬ ¬ if hover6 == True:``
212. ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(SpecialItemsTextWidth+SelectorWidth)-2, 500*yScaleFact))``

213. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(SpecialItemsText, ((realWidth-SpecialItemsTextWidth)-2, 500*yScaleFact))``
214. ``¬ ¬ ¬ ¬ ¬ if hover7 == True:``
215. ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(ItemsTextWidth+SelectorWidth)-2, 450*yScaleFact))``

216. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(OptionsText, ((realWidth-OptionsTextWidth)-2, 550*yScaleFact))``
217. ``¬ ¬ ¬ ¬ ¬ if hover8 == True:``
218. ``¬ ¬ ¬ ¬ ¬ ¬ AlphaSurface.blit(Selector, (realWidth-(OptionsTextWidth+SelectorWidth)-2, 550*yScaleFact))``

219. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``
220. ``¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)``
221. ``¬ ¬ ¬ except Exception as Message:``
222. ``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
223. ``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    1.   ``else:``
    2.   ``¬ print("You need to run this as part of Pycraft")``
    3.   ``¬ import tkinter as tk``
    4.   ``¬ from tkinter import messagebox``
    5.   ``¬ root = tk.Tk()``
    6.   ``¬ root.withdraw()``
    7.   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    8.   ``¬ quit()``


Main
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

1. ``print("Started <Pycraft_main>")``
2. ``class Startup:``
3. ``¬ def __init__(Class_Startup_variables):``
4. ``¬ ¬ try:``
5. ``¬ ¬ ¬ import tkinter as tk``
6. ``¬ ¬ ¬ Class_Startup_variables.mod_Tkinter__tk = tk # [Class_Startup_variables] mod (module) (module name) (subsection of module) (name references)``
7. ``¬ ¬ ¬ import tkinter.ttk  # Class _ <class_name> _ variables``
8. ``¬ ¬ ¬ Class_Startup_variables.mod_Tkinter_ttk_ = tkinter.ttk``
9. ``¬ ¬ ¬ from tkinter import messagebox``
10. ``¬ ¬ ¬ Class_Startup_variables.mod_Tkinter_messagebox_ = messagebox``
11. ``¬ ¬ ¬ from PIL import Image, ImageFilter, ImageGrab, ImageTk``
12. ``¬ ¬ ¬ Class_Startup_variables.mod_PIL_Image_ = Image``
13. ``¬ ¬ ¬ Class_Startup_variables.mod_PIL_ImageFilter_ = ImageFilter``
14. ``¬ ¬ ¬ Class_Startup_variables.mod_PIL_ImageTk_ = ImageTk``
15. ``¬ ¬ ¬ Class_Startup_variables.mod_PIL_ImageGrab_ = ImageGrab``
16. ``¬ ¬ ¬ import pygame``
17. ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__ = pygame``
18. ``¬ ¬ ¬ import numpy``
19. ``¬ ¬ ¬ Class_Startup_variables.mod_Numpy__ = numpy``
20. ``¬ ¬ ¬ import os``
21. ``¬ ¬ ¬ Class_Startup_variables.mod_OS__ = os``
22. ``¬ ¬ ¬ import sys``
23. ``¬ ¬ ¬ Class_Startup_variables.mod_Sys__ = sys``
24. ``¬ ¬ ¬ import random``
25. ``¬ ¬ ¬ Class_Startup_variables.mod_Random__ = random``
26. ``¬ ¬ ¬ import time``
27. ``¬ ¬ ¬ Class_Startup_variables.mod_Time__ = time``
28. ``¬ ¬ ¬ import pygame.locals``
29. ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame_locals_ = pygame.locals``
30. ``¬ ¬ ¬ import OpenGL``
31. ``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL__ = OpenGL``
32. ``¬ ¬ ¬ import OpenGL.GL``
33. ``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL_GL_ = OpenGL.GL``
34. ``¬ ¬ ¬ import OpenGL.GLU``
35. ``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL_GLU_ = OpenGL.GLU``
36. ``¬ ¬ ¬ import OpenGL.GLUT``
37. ``¬ ¬ ¬ Class_Startup_variables.mod_OpenGL_GLUT_ = OpenGL.GLUT``
38. ``¬ ¬ ¬ import moderngl``
39. ``¬ ¬ ¬ Class_Startup_variables.mod_ModernGL__ = moderngl``
40. ``¬ ¬ ¬ import moderngl_window``
41. ``¬ ¬ ¬ Class_Startup_variables.mod_ModernGL_window_ = moderngl_window``
42. ``¬ ¬ ¬ import pyautogui``
43. ``¬ ¬ ¬ Class_Startup_variables.mod_Pyautogui__ = pyautogui``
44. ``¬ ¬ ¬ import psutil``
45. ``¬ ¬ ¬ Class_Startup_variables.mod_Psutil__ = psutil``
46. ``¬ ¬ ¬ import pywavefront``
47. ``¬ ¬ ¬ Class_Startup_variables.mod_Pywavefront__ = pywavefront``
48. ``¬ ¬ ¬ import timeit``
49. ``¬ ¬ ¬ Class_Startup_variables.mod_Timeit__ = timeit``
50. ``¬ ¬ ¬ import subprocess``
51. ``¬ ¬ ¬ Class_Startup_variables.mod_Subprocess__ = subprocess``
52. ``¬ ¬ ¬ import traceback``
53. ``¬ ¬ ¬ Class_Startup_variables.mod_Traceback__ = traceback``
54. ``¬ ¬ ¬ import datetime``
55. ``¬ ¬ ¬ Class_Startup_variables.mod_Datetime__ = datetime``
56. ``¬ ¬ ¬ import ctypes``
57. ``¬ ¬ ¬ Class_Startup_variables.mod_Ctypes__ = ctypes``
58. ``¬ ¬ ¬ import json``
59. ``¬ ¬ ¬ Class_Startup_variables.mod_JSON__ = json``
60. ``¬ ¬ ¬ import threading``
61. ``¬ ¬ ¬ Class_Startup_variables.mod_Threading__ = threading``
62. ``¬ ¬ ¬ import cpuinfo``
63. ``¬ ¬ ¬ Class_Startup_variables.mod_CPUinfo__ = cpuinfo``
64. ``¬ ¬ ¬ import array``
65. ``¬ ¬ ¬ Class_Startup_variables.mod_Array__ = array``
66. ``¬ ¬ ¬ import GPUtil``
67. ``¬ ¬ ¬ Class_Startup_variables.mod_GPUtil__ = GPUtil``
68. ``¬ ¬ ¬ from tabulate import tabulate``
69. ``¬ ¬ ¬ Class_Startup_variables.mod_Tabulate_tabulate_ = tabulate``
70. ``¬ ¬ ¬ from pyrr import Matrix44``
71. ``¬ ¬ ¬ Class_Startup_variables.mod_Pyrr_Matrix44_ = Matrix44``

72. ``¬ ¬ ¬ moderngl.create_standalone_context()``

73. ``¬ ¬ ¬ os.environ['SDL_VIDEO_CENTERED'] = '1'``

74. ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.init()``

75. ``¬ ¬ ¬ import PycraftStartupTest``
76. ``¬ ¬ ¬ Class_Startup_variables.mod_PycraftStartupTest__ = PycraftStartupTest``
77. ``¬ ¬ ¬ import StartupAnimation``
78. ``¬ ¬ ¬ Class_Startup_variables.mod_StartupAnimation__ = StartupAnimation``
79. ``¬ ¬ ¬ import DisplayUtils``
80. ``¬ ¬ ¬ Class_Startup_variables.mod_DisplayUtils__ = DisplayUtils``
81. ``¬ ¬ ¬ import GetSavedData``
82. ``¬ ¬ ¬ Class_Startup_variables.mod_GetSavedData__ = GetSavedData``
83. ``¬ ¬ ¬ import ThemeUtils``
84. ``¬ ¬ ¬ Class_Startup_variables.mod_ThemeUtils__ = ThemeUtils``
85. ``¬ ¬ ¬ import HomeScreen``
86. ``¬ ¬ ¬ Class_Startup_variables.mod_HomeScreen__ = HomeScreen``
87. ``¬ ¬ ¬ import SoundUtils``
88. ``¬ ¬ ¬ Class_Startup_variables.mod_SoundUtils__ = SoundUtils``
89. ``¬ ¬ ¬ import DrawingUtils``
90. ``¬ ¬ ¬ Class_Startup_variables.mod_DrawingUtils__ = DrawingUtils``
91. ``¬ ¬ ¬ import CaptionUtils``
92. ``¬ ¬ ¬ Class_Startup_variables.mod_CaptionUtils__ = CaptionUtils``
93. ``¬ ¬ ¬ import Credits``
94. ``¬ ¬ ¬ Class_Startup_variables.mod_Credits__ = Credits``
95. ``¬ ¬ ¬ import TkinterUtils``
96. ``¬ ¬ ¬ Class_Startup_variables.mod_TkinterUtils__ = TkinterUtils``
97.  ``¬ ¬ ¬ import Achievements``
98.  ``¬ ¬ ¬ Class_Startup_variables.mod_Achievements__ = Achievements``
99.  ``¬ ¬ ¬ import CharacterDesigner``
100. ``¬ ¬ ¬ Class_Startup_variables.mod_CharacterDesigner__ = CharacterDesigner``
101. ``¬ ¬ ¬ import Settings``
102. ``¬ ¬ ¬ Class_Startup_variables.mod_Settings__ = Settings``
103. ``¬ ¬ ¬ import Benchmark``
104. ``¬ ¬ ¬ Class_Startup_variables.mod_Benchmark__ = Benchmark``
105. ``¬ ¬ ¬ import ExBenchmark``
106. ``¬ ¬ ¬ Class_Startup_variables.mod_ExBenchmark__ = ExBenchmark``
107. ``¬ ¬ ¬ import OGLbenchmark``
108. ``¬ ¬ ¬ Class_Startup_variables.mod_OGLbenchmark__ = OGLbenchmark``
109. ``¬ ¬ ¬ import base``
110. ``¬ ¬ ¬ Class_Startup_variables.mod_Base__ = base``
111. ``¬ ¬ ¬ import ShareDataUtil``
112. ``¬ ¬ ¬ Class_Startup_variables.mod_Globals__ = ShareDataUtil``
113. ``¬ ¬ ¬ import TextUtils``
114. ``¬ ¬ ¬ Class_Startup_variables.mod_TextUtils__ = TextUtils``
115. ``¬ ¬ ¬ import Inventory``
116. ``¬ ¬ ¬ Class_Startup_variables.mod_Inventory__ = Inventory``
117. ``¬ ¬ ¬ import ImageUtils``
118. ``¬ ¬ ¬ Class_Startup_variables.mod_ImageUtils__ = ImageUtils``
119. ``¬ ¬ ¬ import MapGUI``
120. ``¬ ¬ ¬ Class_Startup_variables.mod_MapGUI__ = MapGUI``
121. ``¬ ¬ ¬ import ThreadingUtil``
122. ``¬ ¬ ¬ Class_Startup_variables.mod_ThreadingUtil__ = ThreadingUtil``

123. ``¬ ¬ ¬ Class_Startup_variables.aa = True``
124. ``¬ ¬ ¬ Class_Startup_variables.AccentCol = (237, 125, 49)``
125. ``¬ ¬ ¬ Class_Startup_variables.aFPS = 0``
126. ``¬ ¬ ¬ Class_Startup_variables.BackgroundCol = [30, 30, 30]``
127. ``¬ ¬ ¬ Class_Startup_variables.base_folder = os.path.dirname(__file__)``
128. ``¬ ¬ ¬ Class_Startup_variables.cameraANGspeed = 3.5``
129. ``¬ ¬ ¬ Class_Startup_variables.clock = pygame.time.Clock()``
130. ``¬ ¬ ¬ Class_Startup_variables.Collisions = [False, 0]``
131. ``¬ ¬ ¬ Class_Startup_variables.CompletePercent = 0``
132. ``¬ ¬ ¬ Class_Startup_variables.ctx = 0``
133. ``¬ ¬ ¬ Class_Startup_variables.Load_Progress = 0``
134. ``¬ ¬ ¬ Class_Startup_variables.crash = False``
135. ``¬ ¬ ¬ Class_Startup_variables.CurrentlyPlaying = None``

136. ``¬ ¬ ¬ Class_Startup_variables.Data_aFPS_Min = 60``
137. ``¬ ¬ ¬ Class_Startup_variables.Data_aFPS = []``
138. ``¬ ¬ ¬ Class_Startup_variables.Data_aFPS_Max = 1``

139. ``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Min = 60``
140. ``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE = []``
141. ``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Max = 1``

142. ``¬ ¬ ¬ Class_Startup_variables.Data_eFPS_Min = 60``
143. ``¬ ¬ ¬ Class_Startup_variables.Data_eFPS = []``
144. ``¬ ¬ ¬ Class_Startup_variables.Data_eFPS_Max = 1``

145. ``¬ ¬ ¬ Class_Startup_variables.Data_MemUsE_Min = 60``
146. ``¬ ¬ ¬ Class_Startup_variables.Data_MemUsE = []``
147. ``¬ ¬ ¬ Class_Startup_variables.Data_MemUsE_Max = 1``

148. ``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Min = 60``
149. ``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE = []``
150. ``¬ ¬ ¬ Class_Startup_variables.Data_CPUUsE_Max = 1``

151. ``¬ ¬ ¬ Class_Startup_variables.Devmode = 0``
152. ``¬ ¬ ¬ Class_Startup_variables.Display = 0``
153. ``¬ ¬ ¬ Class_Startup_variables.eFPS = 60``
154. ``¬ ¬ ¬ Class_Startup_variables.FanSky = True``
155. ``¬ ¬ ¬ Class_Startup_variables.FanPart = True``
156. ``¬ ¬ ¬ Class_Startup_variables.FontCol = (255, 255, 255)``
157. ``¬ ¬ ¬ Class_Startup_variables.FOV = 70``
158. ``¬ ¬ ¬ Class_Startup_variables.FromPlay = False``
159. ``¬ ¬ ¬ Class_Startup_variables.Fullscreen = False``
160. ``¬ ¬ ¬ Class_Startup_variables.FPS = 60``
161. ``¬ ¬ ¬ Class_Startup_variables.FullscreenX, Class_Startup_variables.FullscreenY = pyautogui.size()``
162. ``¬ ¬ ¬ Class_Startup_variables.GameError = None``
163. ``¬ ¬ ¬ Class_Startup_variables.G3Dscale = 600000``
164. ``¬ ¬ ¬ Class_Startup_variables.GetScreenGraphics = True``
165. ``¬ ¬ ¬ Class_Startup_variables.HUD_Surface = None``
166. ``¬ ¬ ¬ Class_Startup_variables.Iteration = 1``
167. ``¬ ¬ ¬ Class_Startup_variables.lastRun = "29/09/2021"``
168. ``¬ ¬ ¬ Class_Startup_variables.Load3D = True``
169. ``¬ ¬ ¬ Class_Startup_variables.LoadMusic = True``

170. ``¬ ¬ ¬ Class_Startup_variables.Map = 0``
171. ``¬ ¬ ¬ Class_Startup_variables.Map_box = 0``
172. ``¬ ¬ ¬ Class_Startup_variables.Map_scale = 0``
173. ``¬ ¬ ¬ Class_Startup_variables.Map_size = 0``
174. ``¬ ¬ ¬ Class_Startup_variables.Map_trans = 0``
175. ``¬ ¬ ¬ Class_Startup_variables.MapVerts = 0``
176. ``¬ ¬ ¬ Class_Startup_variables.map_vertices = []``
177. ``¬ ¬ ¬ Class_Startup_variables.max_Map_size = 0``

178. ``¬ ¬ ¬ Class_Startup_variables.HUD_object = 0``
179. ``¬ ¬ ¬ Class_Startup_variables.HUD_box = 0``
180. ``¬ ¬ ¬ Class_Startup_variables.HUD_scale = 0``
181. ``¬ ¬ ¬ Class_Startup_variables.HUD_size = 0``
182. ``¬ ¬ ¬ Class_Startup_variables.HUD_trans = 0``
183. ``¬ ¬ ¬ Class_Startup_variables.HUDVerts = 0``
184. ``¬ ¬ ¬ Class_Startup_variables.HUD_vertices = []``
185. ``¬ ¬ ¬ Class_Startup_variables.max_HUD_size = 0``
186. ``¬ ¬ ¬ ``
187. ``¬ ¬ ¬ Class_Startup_variables.Map_max_v = 0``
188. ``¬ ¬ ¬ Class_Startup_variables.Map_min_v = 0``

189. ``¬ ¬ ¬ Class_Startup_variables.HUD_max_v = 0``
190. ``¬ ¬ ¬ Class_Startup_variables.HUD_min_v = 0``

191. ``¬ ¬ ¬ Class_Startup_variables.music = True``
192. ``¬ ¬ ¬ Class_Startup_variables.musicVOL = 5``
193. ``¬ ¬ ¬ Class_Startup_variables.Numpy_map_vertices = 0``
194. ``¬ ¬ ¬ Class_Startup_variables.Progress_Line = []``
195. ``¬ ¬ ¬ Class_Startup_variables.ProgressMessageText = "Initiating"``
196. ``¬ ¬ ¬ Class_Startup_variables.realHeight = 720``
197. ``¬ ¬ ¬ Class_Startup_variables.realWidth = 1280``
198. ``¬ ¬ ¬ Class_Startup_variables.RecommendedFPS = 60``
199. ``¬ ¬ ¬ Class_Startup_variables.RenderFOG = True``
200. ``¬ ¬ ¬ Class_Startup_variables.RunFullStartup = False``
201. ``¬ ¬ ¬ Class_Startup_variables.SecondFontCol = (100, 100, 100)``
202. ``¬ ¬ ¬ Class_Startup_variables.SavedWidth = 1280``
203. ``¬ ¬ ¬ Class_Startup_variables.SavedHeight = 720``
204. ``¬ ¬ ¬ Class_Startup_variables.ShapeCol = (80, 80, 80)``
205. ``¬ ¬ ¬ Class_Startup_variables.skybox_texture = 0``
206. ``¬ ¬ ¬ Class_Startup_variables.sound = True``
207. ``¬ ¬ ¬ Class_Startup_variables.soundVOL = 75``
208. ``¬ ¬ ¬ Class_Startup_variables.Stop_Thread_Event = Class_Startup_variables.mod_Threading__.Event()``
209. ``¬ ¬ ¬ Class_Startup_variables.SettingsPreference = "Medium"``
210. ``¬ ¬ ¬ Class_Startup_variables.theme = False``
211. ``¬ ¬ ¬ Class_Startup_variables.ThreadStatus = "Running"``
212. ``¬ ¬ ¬ Class_Startup_variables.Timer = 0``
213. ``¬ ¬ ¬ Class_Startup_variables.Total_move_x = 0``
214. ``¬ ¬ ¬ Class_Startup_variables.Total_move_y = 0``
215. ``¬ ¬ ¬ Class_Startup_variables.Total_move_z = 0``
216. ``¬ ¬ ¬ Class_Startup_variables.TotalRotation = 0``
217. ``¬ ¬ ¬ Class_Startup_variables.Total_Vertices = 0``
218. ``¬ ¬ ¬ Class_Startup_variables.version = "0.9.3"``
219. ``¬ ¬ ¬ Class_Startup_variables.vertex = 0``
220. ``¬ ¬ ¬ Class_Startup_variables.X = 0``
221. ``¬ ¬ ¬ Class_Startup_variables.Y = 0``
222. ``¬ ¬ ¬ Class_Startup_variables.Z = 0``

223. ``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.StartVariableChecking, args=(Class_Startup_variables,))``
224. ``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.start()``
225. ``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.name = "Thread_StartLongThread"``

226. ``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.StartCPUlogging, args=(Class_Startup_variables,))``
227. ``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.start()``
228. ``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.name = "Thread_GetCPUMetrics"``

229. ``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.AdaptiveMode, args=(Class_Startup_variables,))``
230. ``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.start()``
231. ``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.name = "Thread_AdaptiveMode"``
232. ``¬ ¬ ¬ ``
233. ``¬ ¬ ¬ Class_Startup_variables.mod_Globals__.Share.initialize(Class_Startup_variables)``
234. ``¬ ¬ ¬ ``
235. ``¬ ¬ ¬ import GameEngine``
236. ``¬ ¬ ¬ Class_Startup_variables.mod_MainGameEngine__ = GameEngine``
237. ``¬ ¬ except Exception as error:``
238. ``¬ ¬ ¬ print(error)``
239. ``¬ ¬ ¬ try:``
240. ``¬ ¬ ¬ ¬ import tkinter as tk``
241. ``¬ ¬ ¬ ¬ root = tk.Tk()``
242. ``¬ ¬ ¬ ¬ root.withdraw()``
243. ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Tkinter_messagebox_.showerror("Startup Fail", "Missing required modules")``
244. ``¬ ¬ ¬ ¬ quit()``
245. ``¬ ¬ ¬ except:``
246. ``¬ ¬ ¬ ¬ try:``
247. ``¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
248. ``¬ ¬ ¬ ¬ ¬ sys.exit("0.0.0 -Thank you for playing")``
249. ``¬ ¬ ¬ ¬ except:``
250. ``¬ ¬ ¬ ¬ ¬ quit()``
251. ``¬ ¬ ¬ ¬ ¬ ``
252. ``¬ def crash(ErrorREPORT):``
253. ``¬ ¬ Class_Startup_variables.Stop_Thread_Event.set()``
254. ``¬ ¬ if not ErrorREPORT == None:``
255. ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
256. ``¬ ¬ ¬ Class_Startup_variables.mod_Time__.sleep(1.01)``
257. ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.init()``
258. ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.mixer.stop()``
259. ``¬ ¬ ¬ try:``
260. ``¬ ¬ ¬ ¬ Message = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.SaveTOconfigFILE(Class_Startup_variables)``
261. ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.quit()``
262. ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.init()``
263. ``¬ ¬ ¬ ¬ Display = Class_Startup_variables.mod_Pygame__.display.set_mode((1280, 720))``
264. ``¬ ¬ ¬ ¬ icon = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
265. ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.set_icon(icon)``
266. ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.set_caption(f"Pycraft: An Error Occurred")``

267. ``¬ ¬ ¬ ¬ MessageFont = Class_Startup_variables.mod_Pygame__.font.Font(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Fonts\\Book Antiqua.ttf")), 15)``

268. ``¬ ¬ ¬ ¬ ErrorMessageText = MessageFont.render(str(ErrorREPORT), True, (255,0,0))``
269. ``¬ ¬ ¬ ¬ ErrorMessageTextWidth = ErrorMessageText.get_width()``
270. ``¬ ¬ ¬ ¬ ErrorMessageTextHeight = ErrorMessageText.get_height()``
271. ``¬ ¬ ¬ ¬ Display = Class_Startup_variables.mod_Pygame__.display.set_mode((1280,720))``

272. ``¬ ¬ ¬ ¬ IconImage = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Resources\\Error_Resources\\Icon.jpg")))``
273. ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.set_icon(IconImage)``
274. ``¬ ¬ ¬ ¬ image = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Resources\\Error_Resources\\Error_Message.png")))``
275. ``¬ ¬ ¬ ¬ Clock = Class_Startup_variables.mod_Pygame__.time.Clock()``
276. ``¬ ¬ ¬ ¬ while True:``
277. ``¬ ¬ ¬ ¬ ¬ Display.fill((20,20,20))``
278. ``¬ ¬ ¬ ¬ ¬ Display.blit(image, (0,0))``

279. ``¬ ¬ ¬ ¬ ¬ Display.blit(ErrorMessageText, ((((1280/2)-ErrorMessageTextWidth)/2), (720-ErrorMessageTextHeight)/2))``

280. ``¬ ¬ ¬ ¬ ¬ for event in Class_Startup_variables.mod_Pygame__.event.get():``
281. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == Class_Startup_variables.mod_Pygame__.QUIT:``
282. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.join()``
283. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.join()``
284. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.join()``
285. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
286. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
287. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit(f"0.1.0- Thank you for playing")``

288. ``¬ ¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.display.flip()``
289. ``¬ ¬ ¬ ¬ ¬ Clock.tick(30)``
290. ``¬ ¬ ¬ except Exception as error:``
291. ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit(f"0.2.0- {error} Thank you for playing")``
292. ``¬ ¬ else:``
293. ``¬ ¬ ¬ try:``
294. ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
295. ``¬ ¬ ¬ except Exception as error:``
296. ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit(f"0.3.0- {error} Thank you for playing")``
297. ``¬ ¬ ¬ ¬ quit()``
298. ``¬ ¬ ¬ else:``
299. ``¬ ¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit("0.4.0- Thank you for playing")``
300. ``¬ ¬ ¬ ¬ quit()``

301. ``Class_Startup_variables = Startup()``
302. ``try:``
303. ``¬ Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.ReadMainSave(Class_Startup_variables)``
304. ``except Exception as FileError:``
305. ``¬ try:``
306. ``¬ ¬ if str(FileError) == "Expecting value: line 1 column 1 (char 0)":``
307. ``¬ ¬ ¬ Report = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.RepairLostSave(Class_Startup_variables)``
308. ``¬ ¬ ¬ ErrorString = "Unable to access vital Saved Data, have attempted a fix successfully", FileError``
309. ``¬ ¬ ¬ Message = "0.0.0- " + str(ErrorString)``
310. ``¬ ¬ ¬ Startup.crash(Message)``
311. ``¬ except Exception as Error:``
312. ``¬ ¬ Message = "0.0.1- " + str(Error)``
313. ``¬ ¬ Startup.crash(Message)``

314. ``¬ Message = "0.2- " + str(FileError)``
315. ``¬ Startup.crash(Message)``

316. ``Message = Class_Startup_variables.mod_PycraftStartupTest__.StartupTest.PycraftSelfTest(Class_Startup_variables)``
317. ``if not Message == None:``
318. ``¬ Message = "0.0.3- " + str(Message)``
319. ``¬ Startup.crash(Message)``

320. ``if Class_Startup_variables.theme == False:``
321. ``¬ Message = Class_Startup_variables.mod_ThemeUtils__.DetermineThemeColours.GetThemeGUI(Class_Startup_variables)``
322. ``¬ if not Message == None:``
323. ``¬ ¬ Message = "0.0.4- " + str(Message)``
324. ``¬ ¬ Startup.crash(Message)``

325. ``Message = Class_Startup_variables.mod_ThemeUtils__.DetermineThemeColours.GetColours(Class_Startup_variables)``

326. ``if not Message == None:``
327. ``¬ Message = "0.0.5- " + str(Message)``
328. ``¬ Startup.crash(Message)``
329. ``¬ ``
330. ``Message = Class_Startup_variables.mod_StartupAnimation__.GenerateStartupScreen.Start(Class_Startup_variables)``
331. ``if not Message == None:``
332. ``¬ Message = "0.0.6- " + str(Message)``
333. ``¬ Startup.crash(Message)``

334. ``Class_Startup_variables.Command = "Undefined"``
335. ``while True:``
336. ``¬ if Class_Startup_variables.Command == "saveANDexit":``
337. ``¬ ¬ Message = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.SaveTOconfigFILE(Class_Startup_variables)``
338. ``¬ ¬ if not Message == None:``
339. ``¬ ¬ ¬ Message = "0.0.7- " + str(Message)``
340. ``¬ ¬ ¬ Startup.crash(Message)``
341. ``¬ ¬ else:``
342. ``¬ ¬ ¬ Class_Startup_variables.Stop_Thread_Event.set()``

343. ``¬ ¬ ¬ Class_Startup_variables.Thread_StartLongThread.join()``
344. ``¬ ¬ ¬ Class_Startup_variables.Thread_AdaptiveMode.join()``
345. ``¬ ¬ ¬ Class_Startup_variables.Thread_GetCPUMetrics.join()``
346. ``¬ ¬ ¬ ``
347. ``¬ ¬ ¬ Class_Startup_variables.mod_Pygame__.quit()``
348. ``¬ ¬ ¬ Class_Startup_variables.mod_Sys__.exit("0.5.0- Thank you for playing") # 0 = Order of running, 5 = 5th occurrence down page``
349. ``¬ elif Class_Startup_variables.Command == "Credits":``
350. ``¬ ¬ Message = Class_Startup_variables.mod_Credits__.GenerateCredits.Credits(Class_Startup_variables)``
351. ``¬ ¬ if not Message == None:``
352. ``¬ ¬ ¬ Message = "0.0.8- " + str(Message)``
353. ``¬ ¬ ¬ Startup.crash(Message)``
354. ``¬ ¬ Class_Startup_variables.Command = "Undefined"``
355. ``¬ elif Class_Startup_variables.Command == "Achievements":``
356. ``¬ ¬ Message = Class_Startup_variables.mod_Achievements__.GenerateAchievements.Achievements(Class_Startup_variables)``
357. ``¬ ¬ if not Message == None:``
358. ``¬ ¬ ¬ Message = "0.0.9- " + str(Message)``
359. ``¬ ¬ ¬ Startup.crash(Message)``
360. ``¬ ¬ Class_Startup_variables.Command = "Undefined"``
361. ``¬ elif Class_Startup_variables.Command == "CharacterDesigner":``
362. ``¬ ¬ Message = Class_Startup_variables.mod_CharacterDesigner__.GenerateCharacterDesigner.CharacterDesigner(Class_Startup_variables)``
363. ``¬ ¬ if not Message == None:``
364. ``¬ ¬ ¬ Message = "0.0.10- " + str(Message)``
365. ``¬ ¬ ¬ Startup.crash(Message)``
366. ``¬ ¬ Class_Startup_variables.Command = "Undefined"``
367. ``¬ elif Class_Startup_variables.Command == "Settings":``
368. ``¬ ¬ Message = Class_Startup_variables.mod_Settings__.GenerateSettings.settings(Class_Startup_variables)``
369. ``¬ ¬ if not Message == None:``
370. ``¬ ¬ ¬ Message = "0.0.11- " + str(Message)``
371. ``¬ ¬ ¬ Startup.crash(Message)``
372. ``¬ ¬ Class_Startup_variables.Command = "Undefined"``
373. ``¬ elif Class_Startup_variables.Command == "Benchmark":``
374. ``¬ ¬ Message = Class_Startup_variables.mod_Benchmark__.GenerateBenchmarkMenu.Benchmark(Class_Startup_variables)``
375. ``¬ ¬ if not Message == None:``
376. ``¬ ¬ ¬ Message = "0.0.12- " + str(Message)``
377. ``¬ ¬ ¬ Startup.crash(Message)``
378. ``¬ ¬ Class_Startup_variables.Command = "Undefined"``
379. ``¬ elif Class_Startup_variables.Command == "Play":``
380. ``¬ ¬ Message = Class_Startup_variables.mod_MainGameEngine__.CreateEngine.Play(Class_Startup_variables)``
381. ``¬ ¬ if Message == None:``
382. ``¬ ¬ ¬ Message = Class_Startup_variables.GameError``
383. ``¬ ¬ if not Message == None:``
384. ``¬ ¬ ¬ Message = "0.0.13- " + str(Message)``
385. ``¬ ¬ ¬ Startup.crash(Message)``
386. ``¬ ¬ Class_Startup_variables.mod_Pygame__.init()``
387. ``¬ ¬ Class_Startup_variables.FromPlay = True``
388. ``¬ ¬ Message = Class_Startup_variables.mod_DisplayUtils__.DisplayUtils.SetDisplay(Class_Startup_variables)``
389. ``¬ ¬ if not Message == None:``
390. ``¬ ¬ ¬ Message = "0.0.14- " + str(Message)``
391. ``¬ ¬ ¬ Startup.crash(Message)``
392. ``¬ elif Class_Startup_variables.Command == "Inventory":``
393. ``¬ ¬ Message = Class_Startup_variables.mod_Inventory__.GenerateInventory.Inventory(Class_Startup_variables)``
394. ``¬ ¬ if not Message == None:``
395. ``¬ ¬ ¬ Message = "0.0.15- " + str(Message)``
396. ``¬ ¬ ¬ Startup.crash(Message)``
397. ``¬ ¬ Class_Startup_variables.Command = "Play"``
398. ``¬ elif Class_Startup_variables.Command == "MapGUI":``
399. ``¬ ¬ Message = Class_Startup_variables.mod_MapGUI__.GenerateMapGUI.MapGUI(Class_Startup_variables)``
400. ``¬ ¬ if not Message == None:``
401. ``¬ ¬ ¬ Message = "0.0.16- " + str(Message)``
402. ``¬ ¬ ¬ Startup.crash(Message)``
403. ``¬ ¬ Class_Startup_variables.Command = "Play"``
404. ``¬ else:``
405. ``¬ ¬ Message, Class_Startup_variables.Command = Class_Startup_variables.mod_HomeScreen__.GenerateHomeScreen.Home_Screen(Class_Startup_variables)``
406. ``¬ ¬ if not Message == None:``
407. ``¬ ¬ ¬ Message = "0.0.17- " + str(Message)``
408. ``¬ ¬ ¬ Startup.crash(Message)``


MapGUI
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_MapGUI>")``
    3. ``¬ class GenerateMapGUI:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

1. ``¬ ¬ def GetMapPos(self):``
2. ``¬ ¬ ¬ x = 0``
3. ``¬ ¬ ¬ z = 0``
4. ``¬ ¬ ¬ if self.X == 0:``
5.  ``¬ ¬ ¬ ¬ x = 640``
6.  ``¬ ¬ ¬ if self.Z == 0:``
7.  ``¬ ¬ ¬ ¬ z = 360``
8.  ``¬ ¬ ¬ x -= 6``
9.  ``¬ ¬ ¬ z -= 19``
10. ``¬ ¬ ¬ return (x,z)``

11. ``¬ ¬ def MapGUI(self):``
12. ``¬ ¬ ¬ try:``
13. ``¬ ¬ ¬ ¬ Message = self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``
14. ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
15. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``

16. ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
17. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``
18. ``¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png")))``
19. ``¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``
20. ``¬ ¬ ¬ ¬ MapIcon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Marker.jpg"))).convert()``
21. ``¬ ¬ ¬ ¬ zoom = 0``
22. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Playing | Map")``
23. ``¬ ¬ ¬ ¬ MouseUnlock = True``
24. ``¬ ¬ ¬ ¬ X,Y = 0, 0``
25. ``¬ ¬ ¬ ¬ key = ""``
26. ``¬ ¬ ¬ ¬ while True:``
27. ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
28. ``¬ ¬ ¬ ¬ ¬ ``
29. ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
30. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
31. ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
32. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``
33. ``¬ ¬ ¬ ¬ ¬ ``
34. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
35. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
36. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_r):``
37. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Load3D = False``
38. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
39. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
40. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
41. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYDOWN:``
42. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE:``
43. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ zoom = 0``
44. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_w:``
45. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "w"``
46. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_s:``
47. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "s"``
48. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_d:``
49. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "d"``
50. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_a:``
51. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ key = "a"``
52. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
53. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = self.mod_DisplayUtils__.DisplayUtils.UpdateOPENGLdisplay(self)``
54. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.KEYUP:``
55. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ key = ""``
56. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEWHEEL:``
57. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if str(event.y)[0] == "-":``
58. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ zoom -= 1``
59. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
60. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ zoom += 1``
61. ``¬ ¬ ¬ ¬ ¬ if zoom >= 2:``
62. ``¬ ¬ ¬ ¬ ¬ ¬ zoom = 2``
63. ``¬ ¬ ¬ ¬ ¬ if zoom <= 0:``
64. ``¬ ¬ ¬ ¬ ¬ ¬ zoom = 0``
65. ``¬ ¬ ¬ ¬ ¬ if key == "w":``
66. ``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``
67. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y -= 5``
68. ``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
69. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y -= 10``
70. ``¬ ¬ ¬ ¬ ¬ if key == "s":``
71. ``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``
72. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y += 5``
73. ``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
74. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y += 10``
75. ``¬ ¬ ¬ ¬ ¬ if key == "d":``
76. ``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``
77. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X += 5``
78. ``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
79. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X += 10``
80. ``¬ ¬ ¬ ¬ ¬ if key == "a":``
81. ``¬ ¬ ¬ ¬ ¬ ¬ if zoom == 1:``
82. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X -= 5``
83. ``¬ ¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
84. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X -= 10``
85. ``¬ ¬ ¬ ¬ ¬ if zoom == 0:``
86. ``¬ ¬ ¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((realWidth, realHeight),  self.mod_PIL_Image_.ANTIALIAS)``
87. ``¬ ¬ ¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``
88. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Map0, (0, 0))``
89. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MapIcon, GenerateMapGUI.GetMapPos(self))``
90. ``¬ ¬ ¬ ¬ ¬ ¬ x, y = 0, 0``
91. ``¬ ¬ ¬ ¬ ¬ elif zoom == 1:``
92. ``¬ ¬ ¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((int(realWidth*1.75), int(realHeight*1.75)),  self.mod_PIL_Image_.ANTIALIAS)``
93. ``¬ ¬ ¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``
94. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Map0, (X,Y))``
95.  ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MapIcon, GenerateMapGUI.GetMapPos(self))``
96.  ``¬ ¬ ¬ ¬ ¬ elif zoom == 2:``
97.  ``¬ ¬ ¬ ¬ ¬ ¬ MapPIL =  self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\Map_Resources\\Full_Map.png"))).resize((int(realWidth*2), int(realHeight*2)),  self.mod_PIL_Image_.ANTIALIAS)``
98.  ``¬ ¬ ¬ ¬ ¬ ¬ Map0 = self.mod_Pygame__.image.fromstring(MapPIL.tobytes(), MapPIL.size, MapPIL.mode)``
99.  ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Map0, (X,Y))``
100. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MapIcon, GenerateMapGUI.GetMapPos(self))``
101. ``¬ ¬ ¬ ¬ ¬ if zoom == 1:``
102. ``¬ ¬ ¬ ¬ ¬ ¬ if X <= -955:``
103. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -955``
104. ``¬ ¬ ¬ ¬ ¬ ¬ if Y <= -535:``
105. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -535``
106. ``¬ ¬ ¬ ¬ ¬ ¬ if X >= -5:``
107. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -5``
108. ``¬ ¬ ¬ ¬ ¬ ¬ if Y >= -5:``
109. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -5``
110. ``¬ ¬ ¬ ¬ ¬ if zoom == 2:``
111. ``¬ ¬ ¬ ¬ ¬ ¬ if X <= -1590:``
112. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -1590``
113. ``¬ ¬ ¬ ¬ ¬ ¬ if Y <= -890:``
114. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -890``
115. ``¬ ¬ ¬ ¬ ¬ ¬ if X >= -10:``
116. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ X = -10``
117. ``¬ ¬ ¬ ¬ ¬ ¬ if Y >= -10:``
118. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Y = -10``
119. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``
120. ``¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)``
121. ``¬ ¬ ¬ except Exception as Message:``
122. ``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
123. ``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    1.   ``else:``
    2.   ``¬ print("You need to run this as part of Pycraft")``
    3.   ``¬ import tkinter as tk``
    4.   ``¬ from tkinter import messagebox``
    5.   ``¬ root = tk.Tk()``
    6.   ``¬ root.withdraw()``
    7.   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    8.   ``¬ quit()``


OGLBenchmark
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_OGLBenchmark>")``
    3. ``¬ class LoadOGLBenchmark:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

1. ``¬ ¬ def Cube(self, edges, vertices):``
2. ``¬ ¬ ¬ self.mod_OpenGL_GL_.glBegin(self.mod_OpenGL_GL_.GL_LINES)``
3. ``¬ ¬ ¬ for edge in edges:``
4. ``¬ ¬ ¬ ¬ for vertex in edge:``
5.  ``¬ ¬ ¬ ¬ ¬ self.mod_OpenGL_GL_.glVertex3fv(vertices[vertex])``
6.  ``¬ ¬ ¬ self.mod_OpenGL_GL_.glEnd()``

7.  ``¬ ¬ def CreateBenchmark(self):``
8.  ``¬ ¬ ¬ self.mod_OpenGL_GLU_.gluPerspective(45, (1280/720), 0.1, 50.0)``
9.  ``¬ ¬ ¬ self.mod_OpenGL_GL_.glTranslatef(0.0,0.0, -5)``

10. ``¬ ¬ def RunBenchmark(self, edges, vertices):``
11. ``¬ ¬ ¬ self.mod_OpenGL_GL_.glRotatef(1, 3, 1, 1)``
12. ``¬ ¬ ¬ self.mod_OpenGL_GL_.glClear(self.mod_OpenGL_GL_.GL_COLOR_BUFFER_BIT|self.mod_OpenGL_GL_.GL_DEPTH_BUFFER_BIT)``
13. ``¬ ¬ ¬ LoadOGLBenchmark.Cube(self, edges, vertices)``

.. note::
    For information on this consult the above guide
    19. ``else:``
    20. ``¬ print("You need to run this as part of Pycraft")``
    21. ``¬ import tkinter as tk``
    22. ``¬ from tkinter import messagebox``
    23. ``¬ root = tk.Tk()``
    24. ``¬ root.withdraw()``
    25. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    26. ``¬ quit()``


PycraftStartupTest
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_PycraftStartupTest>")``
    3. ``¬ class StartupTest:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def PycraftSelfTest(self):``
7. ``¬ ¬ ¬ try:``
8. ``¬ ¬ ¬ ¬ import OpenGL.GL as gl``
9. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_mode((1280, 720), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL|self.mod_Pygame__.HIDDEN)``

10. ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()``
11. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)``

12. ``¬ ¬ ¬ ¬ OpenGLversion = str(gl.glGetString(gl.GL_VERSION))[2:5]``
13. ``¬ ¬ ¬ ¬ SDLversion = self.mod_Pygame__.get_sdl_version()[0]``
14. ``¬ ¬ ¬ ¬ RAM = (((self.mod_Psutil__.virtual_memory().available)/1000)/1000) # expressed in MB``

15. ``¬ ¬ ¬ ¬ if float(OpenGLversion) < 2.8:``
16. ``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``
17. ``¬ ¬ ¬ ¬ ¬ root.withdraw()``
18. ``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showerror("Invalid OpenGL version", f"OpenGL version: {OpenGLversion} is not supported; try a version greater than 2.7")``
19. ``¬ ¬ ¬ ¬ ¬ quit()``
20. ``¬ ¬ ¬ ¬ if SDLversion < 2:``
21. ``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``
22. ``¬ ¬ ¬ ¬ ¬ root.withdraw()``
23. ``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showerror("Invalid SDL version", f"SDL version: {SDLversion} is not supported; try a version greater than or equal to 2")``
24. ``¬ ¬ ¬ ¬ ¬ quit()``
25. ``¬ ¬ ¬ ¬ if RAM < 100:``
26. ``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``
27. ``¬ ¬ ¬ ¬ ¬ root.withdraw()``
28. ``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showerror("Minimum system requirements not met", f"Your system does not meet the minimum 100mb free memory specification needed to play this game")``
29. ``¬ ¬ ¬ ¬ ¬ quit()``
30. ``¬ ¬ ¬ ¬ if RAM < 200:``
31. ``¬ ¬ ¬ ¬ ¬ root = self.mod_Tkinter__tk.Tk()``
32. ``¬ ¬ ¬ ¬ ¬ root.withdraw()``
33. ``¬ ¬ ¬ ¬ ¬ self.mod_Tkinter_messagebox_.showwarning("Recommended system requirements not met", f"Your system's free memory does not meet the requirement recommended to play this game (200mb), you are still able to, however your experience may not be satisfactory")``
34. ``¬ ¬ ¬ ¬ ¬ from PIL import Image, ImageTk, ImageGrab``
35. ``¬ ¬ ¬ ¬ ¬ import OpenGL.GL``
36. ``¬ ¬ ¬ ¬ ¬ ``
37. ``¬ ¬ ¬ ¬ if self.mod_Sys__.platform == "win32" or self.mod_Sys__.platform == "win64":``
38. ``¬ ¬ ¬ ¬ ¬ self.mod_OS__.environ["SDL_VIDEO_CENTERED"] = "1"``

39. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()``
40. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.init()``

41. ``¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)``

42. ``¬ ¬ ¬ ¬ current_time = self.mod_Datetime__.datetime.now()``
43. ``¬ ¬ ¬ ¬ currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"``
44. ``¬ ¬ ¬ ¬ if not currentDate == self.lastRun or self.crash == True:``
45. ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
46. ``¬ ¬ ¬ ¬ ¬ yScaleFact = realHeight/720``
47. ``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``
48. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
49. ``¬ ¬ ¬ ¬ ¬ TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
50. ``¬ ¬ ¬ ¬ ¬ Title = TitleFont.render("Pycraft", True, self.FontCol)``
51. ``¬ ¬ ¬ ¬ ¬ TitleWidth = Title.get_width()``
52. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Title, ((realWidth-TitleWidth)/2, 0))``
53. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
54. ``¬ ¬ ¬ ¬ ¬ defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] ``
55. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2)``
56. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
57. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``
58. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
59. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
60. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
61. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
62. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``
63. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
64. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
65. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
66. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
67. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
68. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
69. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
70. ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
71. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
72. ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Error_Resources\\Error_Message.png"))).convert()``
73. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
74. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``
75. ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Error_Resources\\Icon.jpg"))).convert()``
76. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
77. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
78. ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Folder_Resources\\FolderIcon.ico"))).convert()``
79. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
80. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
81. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
82. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
83. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
84. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
85. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``
86. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``
87. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
88. ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg"))).convert()``
89. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
90. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
91. ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg"))).convert()``
92. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
93. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
94. ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg"))).convert()``
95. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
96. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
97. ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg"))).convert()``
98. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
99. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
100. ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg"))).convert()``
101. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
102. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``
103. ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg"))).convert()``
104. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
105. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
106. ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, f"Resources\\General_Resources\\selectorICONlight.jpg")).convert()``
107. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
108. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
109. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
110. ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, f"Resources\\General_Resources\\selectorICONdark.jpg")).convert()``
111. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)``
112. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
113. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
114. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\InventoryGeneral.wav")))``
115. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)``
116. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
117. ``¬ ¬ ¬ ¬ ¬ data = self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``
118. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)``
119. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
120. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``
121. ``¬ ¬ ¬ ¬ else:``
122. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
123. ``¬ ¬ ¬ ¬ ¬ TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
124. ``¬ ¬ ¬ ¬ ¬ Title = TitleFont.render("Pycraft", True, self.FontCol)``
125. ``¬ ¬ ¬ ¬ ¬ TitleWidth = Title.get_width()``
126. ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``
127. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Title, ((realWidth-TitleWidth)/2, 0))``
128. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)``

129. ``¬ ¬ ¬ ¬ ¬ yScaleFact = realHeight/720``
130. ``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``
131. ``¬ ¬ ¬ ¬ ¬ defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] ``
132. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2)``
133. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``
134. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
135. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
136. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
137. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
138. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``
139. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
140. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
141. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
142. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
143. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
144. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``
145. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
146. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
147. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
148. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
149. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
150. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``
151. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)``
152. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
153. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
154. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
155. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
156. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)``
157. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)``
158. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)``
159. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)``
160. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
161. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
162. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
163. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)``
164. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (575*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)``
165. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``
166. ``¬ ¬ ¬ except Exception as Message:``
167. ``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    1.   ``else:``
    2.   ``¬ print("You need to run this as part of Pycraft")``
    3.   ``¬ import tkinter as tk``
    4.   ``¬ from tkinter import messagebox``
    5.   ``¬ root = tk.Tk()``
    6.   ``¬ root.withdraw()``
    7.   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    8.   ``¬ quit()``


Settings
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_Settings>")``
    3. ``¬ class GenerateSettings:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

1. ``¬ ¬ def settings(self):``
2. ``¬ ¬ ¬ try:``
3. ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
4. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
5.  ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Settings")``
6.  ``¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
7.  ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
8.  ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
9.  ``¬ ¬ ¬ ¬ LOWFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
10. ``¬ ¬ ¬ ¬ MEDIUMFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
11. ``¬ ¬ ¬ ¬ HIGHFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
12. ``¬ ¬ ¬ ¬ ADAPTIVEFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
13. ``¬ ¬ ¬ ¬ LightThemeFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
14. ``¬ ¬ ¬ ¬ DarkThemeFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``
15. ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

16. ``¬ ¬ ¬ ¬ TempMx = 0``
17. ``¬ ¬ ¬ ¬ Mx, My = 0, 0``
18. ``¬ ¬ ¬ ¬ mousebuttondown = False``

19. ``¬ ¬ ¬ ¬ SettingsInformationFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)``

20. ``¬ ¬ ¬ ¬ scroll = 50``

21. ``¬ ¬ ¬ ¬ while True:``
22. ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

23. ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:``
24. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
25. ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:``
26. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

27. ``¬ ¬ ¬ ¬ ¬ xScaleFact = realWidth/1280``

28. ``¬ ¬ ¬ ¬ ¬ TempMx = Mx``
29. ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``
30. ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1``
31. ``¬ ¬ ¬ ¬ ¬ Mx, My = self.mod_Pygame__.mouse.get_pos()``
32. ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()``
33. ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS``
34. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
35. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``
36. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
37. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
38. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None``
39. ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:``
40. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:``
41. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1``
42. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``
43. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``
44. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:``
45. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
46. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:``
47. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
48. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:``
49. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1``
50. ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:``
51. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True``
52. ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.MOUSEBUTTONUP:``
53. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
54. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEWHEEL and realHeight <= 760:``
55. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_SIZENS)``
56. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if str(event.y)[0] == "-":``
57. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ scroll -= 5``
58. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:``
59. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ scroll += 5``
60. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
61. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_ARROW)``

62. ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Settings")``

63. ``¬ ¬ ¬ ¬ ¬ if scroll > 35:``
64. ``¬ ¬ ¬ ¬ ¬ ¬ scroll = 35``
65. ``¬ ¬ ¬ ¬ ¬ elif scroll < 0:``
66. ``¬ ¬ ¬ ¬ ¬ ¬ scroll = 0``

67. ``¬ ¬ ¬ ¬ ¬ titletFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)``
68. ``¬ ¬ ¬ ¬ ¬ TitleWidth = titletFont.get_width()``

69. ``¬ ¬ ¬ ¬ ¬ InfoFont = InfoTitleFont.render("Settings", self.aa, self.SecondFontCol)``

70. ``¬ ¬ ¬ ¬ ¬ FPSFont = VersionFont.render(f"FPS: Actual: {int(self.eFPS)} Max: {int(self.FPS)} Average: {int((self.aFPS/self.Iteration))}", self.aa, self.FontCol)``
71. ``¬ ¬ ¬ ¬ ¬ FOVFont = VersionFont.render(f"FOV: {self.FOV}", self.aa, self.FontCol)``
72. ``¬ ¬ ¬ ¬ ¬ CamRotFont = VersionFont.render(f"Camera Rotation Speed: {round(self.cameraANGspeed, 1)}", self.aa, self.FontCol)``
73. ``¬ ¬ ¬ ¬ ¬ ModeFont = VersionFont.render("Mode;¬ ¬  ,¬ ¬ ¬ ¬  ,¬ ¬ ¬ ,¬ ¬   .", self.aa, self.FontCol)``
74. ``¬ ¬ ¬ ¬ ¬ AAFont = VersionFont.render(f"Anti-Aliasing: {self.aa}", self.aa, self.FontCol)``
75. ``¬ ¬ ¬ ¬ ¬ RenderFogFont = VersionFont.render(f"Render Fog: {self.RenderFOG}", self.aa, self.FontCol)``
76. ``¬ ¬ ¬ ¬ ¬ FancySkyFont = VersionFont.render(f"Fancy Skies: {self.FanSky}", self.aa, self.FontCol)``
77. ``¬ ¬ ¬ ¬ ¬ FancyParticleFont = VersionFont.render(f"Fancy Partices: {self.FanPart}", self.aa, self.FontCol)``
78. ``¬ ¬ ¬ ¬ ¬ SoundFont = VersionFont.render(f"Sound: {self.sound}", self.aa, self.FontCol)``
79. ``¬ ¬ ¬ ¬ ¬ if self.sound == True:``
80. ``¬ ¬ ¬ ¬ ¬ ¬ SoundVoltFont = VersionFont.render(f"Sound Volume: {self.soundVOL}%", self.aa, self.FontCol)``
81. ``¬ ¬ ¬ ¬ ¬ else:``
82. ``¬ ¬ ¬ ¬ ¬ ¬ SoundVoltFont = VersionFont.render(f"Sound Volume: {self.soundVOL}%", self.aa, self.ShapeCol)``
83. ``¬ ¬ ¬ ¬ ¬ MusicFont = VersionFont.render(f"Music: {self.music}", self.aa, self.FontCol)``
84. ``¬ ¬ ¬ ¬ ¬ if self.music == True:``
85. ``¬ ¬ ¬ ¬ ¬ ¬ MusicVoltFont = VersionFont.render(f"Music Volume: {self.musicVOL}%", self.aa, self.FontCol)``
86. ``¬ ¬ ¬ ¬ ¬ else:``
87. ``¬ ¬ ¬ ¬ ¬ ¬ MusicVoltFont = VersionFont.render(f"Music Volume: {self.musicVOL}%", self.aa, self.ShapeCol)``
88. ``¬ ¬ ¬ ¬ ¬ ThemeFont = VersionFont.render(f"Theme:¬ ¬   ,¬ ¬   | Current Theme: {self.theme}", self.aa, self.FontCol)``
89. ``¬ ¬ ¬ ¬ ¬ ThemeInformationFont = SettingsInformationFont.render("Gives you control over which theme you can use", self.aa, self.AccentCol)``
90. ``¬ ¬ ¬ ¬ ¬ ModeInformationFont = SettingsInformationFont.render("Gives you 4 separate per-sets for settings, Adaptive mode will automatically adjust your settings", self.aa, self.AccentCol)``
91. ``¬ ¬ ¬ ¬ ¬ FPSInformationFont = SettingsInformationFont.render("Controls the maximum frame rate the game will limit to, does not guarantee that FPS unfortunately", self.aa, self.AccentCol)``
92. ``¬ ¬ ¬ ¬ ¬ FOVInformationFont = SettingsInformationFont.render("Controls the FOV of the camera in-game", self.aa, self.AccentCol)``
93. ``¬ ¬ ¬ ¬ ¬ CameraRotationSpeedInformationFont = SettingsInformationFont.render("Controls the rotation speed of the camera in-game (1 is low, 5 is high)", self.aa, self.AccentCol)``
94. ``¬ ¬ ¬ ¬ ¬ AAInformationFont = SettingsInformationFont.render("Enables/Disables anti-aliasing in game and in the GUI, will give you a minor performance improvement, mainly for low powered devices", self.aa, self.AccentCol)``
95.  ``¬ ¬ ¬ ¬ ¬ self.RenderFogInformationFont = SettingsInformationFont.render("Enables/Disables fog effects in game, for a small performance benefit", self.aa, self.AccentCol)``
96.  ``¬ ¬ ¬ ¬ ¬ FancySkiesInformationFont = SettingsInformationFont.render("Enables/Disables a fancy sky box for better visuals in game, does not control anti aliasing for the sky box", self.aa, self.AccentCol)``
97.  ``¬ ¬ ¬ ¬ ¬ FancyParticlesInformationFont = SettingsInformationFont.render("Enables/Disables particles in game as particles can have a significant performance decrease", self.aa, self.AccentCol)``
98.  ``¬ ¬ ¬ ¬ ¬ SoundInformationFont = SettingsInformationFont.render("Enables/Disables sound effects in game, like for example the click sound and footsteps in game", self.aa, self.AccentCol)``
99.  ``¬ ¬ ¬ ¬ ¬ SoundVolInformationFont = SettingsInformationFont.render("Controls the volume of the sound effects, where 100% is maximum and 0% is minimum volume", self.aa, self.AccentCol)``
100. ``¬ ¬ ¬ ¬ ¬ MusicInformationFont = SettingsInformationFont.render("Enables/Disables music in game, like for example the GUI music", self.aa, self.AccentCol)``
101. ``¬ ¬ ¬ ¬ ¬ MusicVolInformationFont = SettingsInformationFont.render("Controls the volume of the music, some effects may not apply until the game reloads", self.aa, self.AccentCol)``
102. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
103. ``¬ ¬ ¬ ¬ ¬ FPS_rect = self.mod_Pygame__.Rect(50, 180+scroll, 450*xScaleFact, 10)``
104. ``¬ ¬ ¬ ¬ ¬ FOV_rect = self.mod_Pygame__.Rect(50, 230+scroll, 450*xScaleFact, 10)``
105. ``¬ ¬ ¬ ¬ ¬ CAM_rect = self.mod_Pygame__.Rect(50, 280+scroll, 450*xScaleFact, 10)``
106. ``¬ ¬ ¬ ¬ ¬ sound_rect = self.mod_Pygame__.Rect(50, 580+scroll, 450*xScaleFact, 10)``
107. ``¬ ¬ ¬ ¬ ¬ music_rect = self.mod_Pygame__.Rect(50, 680+scroll, 450*xScaleFact, 10)``
108. ``¬ ¬ ¬ ¬ ¬ aa_rect = self.mod_Pygame__.Rect(50, 330+scroll, 50, 10)``
109. ``¬ ¬ ¬ ¬ ¬ RenderFOG_Rect = self.mod_Pygame__.Rect(50, 380+scroll, 50, 10)``
110. ``¬ ¬ ¬ ¬ ¬ Fansky_Rect = self.mod_Pygame__.Rect(50, 430+scroll, 50, 10)``
111. ``¬ ¬ ¬ ¬ ¬ FanPart_Rect = self.mod_Pygame__.Rect(50, 480+scroll, 50, 10)``
112. ``¬ ¬ ¬ ¬ ¬ sound_Rect = self.mod_Pygame__.Rect(50, 530+scroll, 50, 10)``
113. ``¬ ¬ ¬ ¬ ¬ music_Rect = self.mod_Pygame__.Rect(50, 630+scroll, 50, 10)``
114. ``¬ ¬ ¬ ¬ ¬ slider_Rect = self.mod_Pygame__.Rect(realWidth-15, scroll, 10, 665)``
115. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FPS_rect, 0)``
116. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FOV_rect, 0)``
117. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, CAM_rect, 0)``
118. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, sound_rect, 0)``
119. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, music_rect, 0)``
120. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, aa_rect, 0)``
121. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, RenderFOG_Rect, 0)``
122. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, Fansky_Rect, 0)``
123. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FanPart_Rect, 0)``
124. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, sound_Rect, 0)``
125. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, music_Rect, 0)``
126. ``¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
127. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 180+scroll and My < 190+scroll:``
128. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
129. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.FPS < 445:``
130. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS += 1``
131. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.FPS > 15:``
132. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS -= 1``
133. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FPS < 15:``
134. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 16``
135. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FPS > 445:``
136. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 444``
137. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (int(self.FPS+45)*xScaleFact, 185+scroll), 9)``
138. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
139. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (int(self.FPS+45)*xScaleFact, 185+scroll), 9)``

140. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 230+scroll and My < 240+scroll:``
141. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
142. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.FOV < 98:``
143. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV += 1``
144. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.FOV > 12:``
145. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV -= 1``
146. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FOV < 12:``
147. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV = 13``
148. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FOV > 98:``
149. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FOV = 97``
150. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (int(self.FOV*5)*xScaleFact, 235+scroll), 9)``
151. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
152. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (int(self.FOV*5)*xScaleFact, 235+scroll), 9)``

153. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 280+scroll and My < 290+scroll:``
154. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
155. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.cameraANGspeed < 5.0:``
156. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed += 0.1``
157. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.cameraANGspeed > 0.0:``
158. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed -= 0.1``
159. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.cameraANGspeed > 5.0:``
160. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed = 4.9``
161. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.cameraANGspeed <= 0:``
162. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.cameraANGspeed = 0.1``
163. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)``
164. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
165. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)``

166. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 580+scroll and My < 590+scroll and self.sound == True:``
167. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
168. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.soundVOL < 100:``
169. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL += 1``
170. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.soundVOL > 0:``
171. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL -= 1``
172. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.soundVOL > 100:``
173. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL = 100``
174. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.soundVOL < 0:``
175. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.soundVOL = 0``
176. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)``
177. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
178. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)``

179. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 680+scroll and My < 690+scroll and self.music == True:``
180. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
181. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if Mx > TempMx and self.musicVOL < 100:``
182. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL += 1``
183. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Mx < TempMx and self.musicVOL > 0:``
184. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL -= 1``
185. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.musicVOL > 100:``
186. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL = 100``
187. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.musicVOL < 0:``
188. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.musicVOL = 0``
189. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)``
190. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
191. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)``

192. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 330+scroll and My < 340+scroll:``
193. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
194. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True:``
195. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``
196. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
197. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
198. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
199. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False:``
200. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``
201. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
202. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
203. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
204. ``¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True:``
205. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 335+scroll), 9)``
206. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 335+scroll), 6)``
207. ``¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False:``
208. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 335+scroll), 9)``
209. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 335+scroll), 6)``

210. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 380+scroll and My < 390+scroll:``
211. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
212. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``
213. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = False``
214. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
215. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
216. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
217. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``
218. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = True``
219. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
220. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
221. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
222. ``¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``
223. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 385+scroll), 9)``
224. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 385+scroll), 6)``
225. ``¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``
226. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 385+scroll), 9)``
227. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 385+scroll), 6)``

228. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 430+scroll and My < 440+scroll:``
229. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
230. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``
231. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = False``
232. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
233. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
234. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
235. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``
236. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
237. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
238. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
239. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
240. ``¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``
241. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 435+scroll), 9)``
242. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 435+scroll), 6)``
243. ``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``
244. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 435+scroll), 9)``
245. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 435+scroll), 6)``

246. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 480+scroll and My < 490+scroll:``
247. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
248. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``
249. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
250. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
251. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
252. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
253. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``
254. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = True``
255. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
256. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
257. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
258. ``¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``
259. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 485+scroll), 9)``
260. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 485+scroll), 6)``
261. ``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``
262. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 485+scroll), 9)``
263. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 485+scroll), 6)``

264. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 530+scroll and My < 540+scroll:``
265. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
266. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
267. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.sound = False``
268. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
269. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
270. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
271. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``
272. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.sound = True``
273. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
274. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
275. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
276. ``¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
277. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 535+scroll), 9)``
278. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 535+scroll), 6)``
279. ``¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``
280. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 535+scroll), 9)``
281. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 535+scroll), 6)``

282. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 630+scroll and My < 640+scroll:``
283. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
284. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``
285. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.music = False``
286. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).stop()``
287. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
288. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
289. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
290. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``
291. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.LoadMusic = True``
292. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.music = True``
293. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
294. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
295. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
296. ``¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``
297. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 635+scroll), 9)``
298. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 635+scroll), 6)``
299. ``¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``
300. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 635+scroll), 9)``
301. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 635+scroll), 6)``
302. ``¬ ¬ ¬ ¬ ¬ else:``
303. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 9)``
304. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.FPS+45)*xScaleFact), 185+scroll), 9)``
305. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 9)``
306. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.FOV*5))*xScaleFact, 235+scroll), 9)``
307. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 9)``

308. ``¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True:``
309. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 335+scroll), 9)``
310. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 335+scroll), 6)``
311. ``¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False:``
312. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 335+scroll), 9)``
313. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 335+scroll), 6)``

314. ``¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``
315. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 385+scroll), 9)``
316. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 385+scroll), 6)``
317. ``¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``
318. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 385+scroll), 9)``
319. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 385+scroll), 6)``

320. ``¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``
321. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 435+scroll), 9)``
322. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 435+scroll), 6)``
323. ``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``
324. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 435+scroll), 9)``
325. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 435+scroll), 6)``

326. ``¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``
327. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 485+scroll), 9)``
328. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 485+scroll), 6)``
329. ``¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``
330. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 485+scroll), 9)``
331. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 485+scroll), 6)``

332. ``¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
333. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 535+scroll), 9)``
334. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 535+scroll), 6)``
335. ``¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``
336. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 535+scroll), 9)``
337. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 535+scroll), 6)``

338. ``¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``
339. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (90, 635+scroll), 9)``
340. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 635+scroll), 6)``
341. ``¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``
342. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, (255, 255, 255), (60, 635+scroll), 9)``
343. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 635+scroll), 6)``

344. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 330+scroll and My < 340+scroll:``
345. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
346. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(AAInformationFont, (120, 325+scroll))``
347. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.aa == True:``
348. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 335+scroll), 9)``
349. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 335+scroll), 6)``
350. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.aa == False:``
351. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 335+scroll), 9)``
352. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 335+scroll), 6)``

353. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 380+scroll and My < 390+scroll:``
354. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
355. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(self.RenderFogInformationFont, (120, 375+scroll))``
356. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.RenderFOG == True:``
357. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 385+scroll), 9)``
358. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 385+scroll), 6)``
359. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.RenderFOG == False:``
360. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 385+scroll), 9)``
361. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 385+scroll), 6)``

362. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 430+scroll and My < 440+scroll:``
363. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
364. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FancySkiesInformationFont, (120, 425+scroll))``
365. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanSky == True:``
366. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 435+scroll), 9)``
367. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 435+scroll), 6)``
368. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanSky == False:``
369. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 435+scroll), 9)``
370. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 435+scroll), 6)``

371. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 480+scroll and My < 490+scroll:``
372. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FancyParticlesInformationFont, (120, 475+scroll))``
373. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
374. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.FanPart == True:``
375. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 485+scroll), 9)``
376. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 485+scroll), 6)``
377. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.FanPart == False:``
378. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 485+scroll), 9)``
379. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 485+scroll), 6)``

380. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 530+scroll and My < 540+scroll:``
381. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundInformationFont, (120, 525+scroll))``
382. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
383. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
384. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 535+scroll), 9)``
385. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 535+scroll), 6)``
386. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.sound == False:``
387. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 535+scroll), 9)``
388. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 535+scroll), 6)``

389. ``¬ ¬ ¬ ¬ ¬ ¬ if My > 630+scroll and My < 640+scroll:``
390. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
391. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicInformationFont, (120, 625+scroll))``
392. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.music == True:``
393. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (90, 635+scroll), 9)``
394. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (90, 635+scroll), 6)``
395. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif self.music == False:``
396. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.AccentCol, (60, 635+scroll), 9)``
397. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (60, 635+scroll), 6)``

398. ``¬ ¬ ¬ ¬ ¬ if My >= 65+scroll and My <= 75+scroll:``
399. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
400. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(ThemeInformationFont, (300, 67+scroll))``

401. ``¬ ¬ ¬ ¬ ¬ if My >= 65+scroll and My <= 75+scroll and Mx >= 55 and Mx <= 95:``
402. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
403. ``¬ ¬ ¬ ¬ ¬ ¬ LightTheme = LightThemeFont.render("Light", self.aa, self.AccentCol)``
404. ``¬ ¬ ¬ ¬ ¬ ¬ LightThemeFont.set_underline(True)``
405. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
406. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "light"``
407. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = self.mod_ThemeUtils__.DetermineThemeColours.GetColours(self)``
408. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:``
409. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = "1.8- " + str(Message)``
410. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message``
411. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
412. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
413. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
414. ``¬ ¬ ¬ ¬ ¬ else:``
415. ``¬ ¬ ¬ ¬ ¬ ¬ LightTheme = LightThemeFont.render("Light", self.aa, self.FontCol)``
416. ``¬ ¬ ¬ ¬ ¬ ¬ LightThemeFont.set_underline(False)``

417. ``¬ ¬ ¬ ¬ ¬ if My >= 65+scroll and My <= 75+scroll and Mx >= 95 and Mx <= 135:``
418. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
419. ``¬ ¬ ¬ ¬ ¬ ¬ DarkTheme = DarkThemeFont.render("Dark", self.aa, self.AccentCol)``
420. ``¬ ¬ ¬ ¬ ¬ ¬ DarkThemeFont.set_underline(True)``
421. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
422. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "dark"``
423. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = self.mod_ThemeUtils__.DetermineThemeColours.GetColours(self)``
424. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:``
425. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Message = "1.8- " + str(Message)``
426. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message``
427. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
428. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
429. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
430. ``¬ ¬ ¬ ¬ ¬ else:``
431. ``¬ ¬ ¬ ¬ ¬ ¬ DarkTheme = DarkThemeFont.render("Dark", self.aa, self.FontCol)``
432. ``¬ ¬ ¬ ¬ ¬ ¬ DarkThemeFont.set_underline(False)``

433. ``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll:``
434. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
435. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(ModeInformationFont, (300, 85+scroll))``

436. ``¬ ¬ ¬ ¬ ¬ if My > 680+scroll and My < 690+scroll:``
437. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
438. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicVolInformationFont, (520*xScaleFact, 675+scroll))``

439. ``¬ ¬ ¬ ¬ ¬ if My > 580+scroll and My < 590+scroll:``
440. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
441. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundVolInformationFont, (520*xScaleFact, 575+scroll))``

442. ``¬ ¬ ¬ ¬ ¬ if My > 280+scroll and My < 290+scroll:``
443. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
444. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CameraRotationSpeedInformationFont, (520*xScaleFact, 275+scroll))``

445. ``¬ ¬ ¬ ¬ ¬ if My > 230+scroll and My < 240+scroll:``
446. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
447. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FOVInformationFont, (520*xScaleFact, 225+scroll))``

448. ``¬ ¬ ¬ ¬ ¬ if My > 180+scroll and My < 190+scroll:``
449. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
450. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSInformationFont, (520*xScaleFact, 175+scroll))``

451. ``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 40 and Mx <= 80:``
452. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
453. ``¬ ¬ ¬ ¬ ¬ ¬ LOWtFont = LOWFont.render("Low", self.aa, self.AccentCol)``
454. ``¬ ¬ ¬ ¬ ¬ ¬ LOWFont.set_underline(True)``
455. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
456. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "Low"``
457. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 15``
458. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``
459. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = False``
460. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = False``
461. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
462. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
463. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
464. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
465. ``¬ ¬ ¬ ¬ ¬ else:``
466. ``¬ ¬ ¬ ¬ ¬ ¬ LOWtFont = LOWFont.render("Low", self.aa, self.FontCol)``
467. ``¬ ¬ ¬ ¬ ¬ ¬ LOWFont.set_underline(False)``

468. ``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 90 and Mx <= 155:``
469. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
470. ``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMtFont = MEDIUMFont.render("Medium", self.aa, self.AccentCol)``
471. ``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMFont.set_underline(True)``
472. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
473. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "Medium"``
474. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 30``
475. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``
476. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = False``
477. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
478. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
479. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
480. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
481. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
482. ``¬ ¬ ¬ ¬ ¬ else:``
483. ``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMtFont = MEDIUMFont.render("Medium", self.aa, self.FontCol)``
484. ``¬ ¬ ¬ ¬ ¬ ¬ MEDIUMFont.set_underline(False)``

485. ``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 165 and Mx <= 205:``
486. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
487. ``¬ ¬ ¬ ¬ ¬ ¬ HIGHFontText = HIGHFont.render("High", self.aa, self.AccentCol)``
488. ``¬ ¬ ¬ ¬ ¬ ¬ HIGHFont.set_underline(True)``
489. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
490. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "High"``
491. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = 60``
492. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``
493. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFOG = True``
494. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
495. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = True``
496. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
497. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
498. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
499. ``¬ ¬ ¬ ¬ ¬ else:``
500. ``¬ ¬ ¬ ¬ ¬ ¬ HIGHFontText = HIGHFont.render("High", self.aa, self.FontCol)``
501. ``¬ ¬ ¬ ¬ ¬ ¬ HIGHFont.set_underline(False)``

502. ``¬ ¬ ¬ ¬ ¬ if My >= 85+scroll and My <= 95+scroll and Mx >= 215 and Mx <= 300:``
503. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)``
504. ``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEtFont = ADAPTIVEFont.render("Adaptive", self.aa, self.AccentCol)``
505. ``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEFont.set_underline(True)``
506. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
507. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.SettingsPreference = "Adaptive"``
508. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS = (self.mod_Psutil__.cpu_freq(percpu=True)[0][2])/35``
509. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if (self.mod_Psutil__.cpu_freq(percpu=True)[0][2])/10 > 300 and self.mod_Psutil__.virtual_memory().total > 8589934592:``
510. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``
511. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = True``
512. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
513. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = True``
514. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif (self.mod_Psutil__.cpu_freq(percpu=True)[0][2]) > 200 and self.mod_Psutil__.virtual_memory().total > 4294967296:``
515. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = True``
516. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = True``
517. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
518. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
519. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif (self.mod_Psutil__.cpu_freq(percpu=True)[0][2]) > 100 and self.mod_Psutil__.virtual_memory().total > 2147483648:``
520. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``
521. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = False``
522. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = True``
523. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
524. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ elif (self.mod_Psutil__.cpu.freq(percpu=True)[0][2]) < 100 and (self.mod_Psutil__.cpu.freq(percpu=True)[0][2]) > 75 and self.mod_Psutil__.virtual_memory().total > 1073741824:``
525. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.aa = False``
526. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.RenderFog = False``
527. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanSky = False``
528. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FanPart = False``
529. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:``
530. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
531. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
532. ``¬ ¬ ¬ ¬ ¬ else:``
533. ``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEtFont = ADAPTIVEFont.render("Adaptive", self.aa, self.FontCol)``
534. ``¬ ¬ ¬ ¬ ¬ ¬ ADAPTIVEFont.set_underline(False)``

535. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSFont, (0, 150+scroll))``
536. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(FOVFont, (0, 200+scroll))``
537. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(CamRotFont, (0, 250+scroll))``
538. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(ModeFont, (0, 85+scroll))``
539. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(LOWtFont, (48, 85+scroll))``
540. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(MEDIUMtFont, (90, 85+scroll))``
541. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(HIGHFontText, (165, 85+scroll))``
542. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(ADAPTIVEtFont, (215, 85+scroll))``
543. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AAFont, (0, 300+scroll))``
544. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(RenderFogFont, (0, 350+scroll))``
545. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(FancySkyFont, (0, 400+scroll))``
546. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(FancyParticleFont, (0, 450+scroll))``
547. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundFont, (0, 500+scroll))``
548. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(SoundVoltFont, (0, 550+scroll))``
549. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicFont, (0, 600+scroll))``
550. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(MusicVoltFont, (0, 650+scroll))``
551. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(ThemeFont, (0, 65+scroll))``
552. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(LightTheme, (55, 65+scroll))``
553. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(DarkTheme, (95, 65+scroll))``

554. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (int(self.FPS+45)*xScaleFact, 185+scroll), 6)``
555. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, (int(self.FOV*5)*xScaleFact, 235+scroll), 6)``
556. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, ((int(self.cameraANGspeed*89)+45)*xScaleFact, 285+scroll), 6)``
557. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, ((int(self.soundVOL*4.4)+50)*xScaleFact, 585+scroll), 6)``
558. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.circle(self.Display, self.ShapeCol, ((int(self.musicVOL*4.4)+50)*xScaleFact, 685+scroll), 6)``
559. ``¬ ¬ ¬ ¬ ¬ ``
560. ``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 100)``
561. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
562. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(titletFont, ((realWidth-TitleWidth)/2, 0))``
563. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont, (((realWidth-TitleWidth)/2)+55, 50))``

564. ``¬ ¬ ¬ ¬ ¬ if realHeight <= 760:``
565. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, slider_Rect, 0)``
566. ``¬ ¬ ¬ ¬ ¬ else:``
567. ``¬ ¬ ¬ ¬ ¬ ¬ scroll = 50``

568. ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
569. ``¬ ¬ ¬ ¬ ¬ if not Message == None:``
570. ``¬ ¬ ¬ ¬ ¬ ¬ return Message``

571. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
572. ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)``
573. ``¬ ¬ ¬ except Exception as Message:``
574. ``¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))``
575. ``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    1.   ``else:``
    2.   ``¬ print("You need to run this as part of Pycraft")``
    3.   ``¬ import tkinter as tk``
    4.   ``¬ from tkinter import messagebox``
    5.   ``¬ root = tk.Tk()``
    6.   ``¬ root.withdraw()``
    7.   ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    8.   ``¬ quit()``


ShareDataUtil
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_ShareDataUtil>")``
    3. ``¬ class Share:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

1. ``¬ ¬ def initialize(Data):``
2. ``¬ ¬ ¬ global Class_Startup_variables``
3. ``¬ ¬ ¬ Class_Startup_variables = Data``


SoundUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_SoundUtils>")``
    3. ``¬ class PlaySound:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def PlayClickSound(self):``
7. ``¬ ¬ ¬ channel1 = self.mod_Pygame__.mixer.Channel(0)``
8. ``¬ ¬ ¬ clickMUSIC = self.mod_Pygame__.mixer.Sound(file=self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``
9. ``¬ ¬ ¬ channel1.set_volume(self.soundVOL/100)``
10. ``¬ ¬ ¬ channel1.play(clickMUSIC)``
11. ``¬ ¬ ¬ self.mod_Pygame__.time.wait(40)``

12. ``¬ ¬ def PlayFootstepsSound(self):``
13. ``¬ ¬ ¬ channel2 = self.mod_Pygame__.mixer.Channel(1)``
14. ``¬ ¬ ¬ Footsteps = self.mod_Pygame__.mixer.Sound(self.mod_OS__.path.join(self.base_folder, (f"Resources\\G3_Resources\\GameSounds\\footsteps{self.mod_Random__.randint(0, 5)}.wav")))``
15. ``¬ ¬ ¬ channel2.set_volume(self.soundVOL/100)``
16. ``¬ ¬ ¬ channel2.play(Footsteps)``

17. ``¬ ¬ def PlayInvSound(self):``
18. ``¬ ¬ ¬ channel3 = self.mod_Pygame__.mixer.Channel(2)``
19. ``¬ ¬ ¬ InvGen = self.mod_Pygame__.mixer.Sound(file=self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\InventoryGeneral.wav")))``
20. ``¬ ¬ ¬ channel3.set_volume(self.musicVOL/100)``
21. ``¬ ¬ ¬ channel3.play(InvGen)``

22. ``¬ ¬ def PlayAmbientSound(self):``
23. ``¬ ¬ ¬ channel4 = self.mod_Pygame__.mixer.Channel(3)``
24. ``¬ ¬ ¬ LoadAmb = self.mod_Pygame__.mixer.Sound(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\GameSounds\\FieldAmb.wav")))``
25. ``¬ ¬ ¬ channel4.set_volume(self.soundVOL/100)``
26. ``¬ ¬ ¬ channel4.play(LoadAmb)``

.. note::
    For information on this consult the above guide
    27. ``else:``
    28. ``¬ print("You need to run this as part of Pycraft")``
    29. ``¬ import tkinter as tk``
    30. ``¬ from tkinter import messagebox``
    31. ``¬ root = tk.Tk()``
    32. ``¬ root.withdraw()``
    33. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    34. ``¬ quit()``


StartupAnimation
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_StartupAnimation>")``
    3. ``¬ class GenerateStartupScreen:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def Start(self):``
7. ``¬ ¬ ¬ try:``
8. ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
9. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
10. ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Welcome")``
11. ``¬ ¬ ¬ ¬ PresentsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)``
12. ``¬ ¬ ¬ ¬ PycraftFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
13. ``¬ ¬ ¬ ¬ NameFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 45)``

14. ``¬ ¬ ¬ ¬ NameText = NameFont.render("Tom Jebbo", True, self.FontCol)``
15. ``¬ ¬ ¬ ¬ NameTextWidth = NameText.get_width()``
16. ``¬ ¬ ¬ ¬ NameTextHeight = NameText.get_height()``

17. ``¬ ¬ ¬ ¬ PresentsText = PresentsFont.render("presents", True, self.FontCol)``

18. ``¬ ¬ ¬ ¬ PycraftText = PycraftFont.render("Pycraft", True, self.FontCol)``
19. ``¬ ¬ ¬ ¬ PycraftTextWidth = PycraftText.get_width()``
20. ``¬ ¬ ¬ ¬ PycraftTextHeight = PycraftText.get_height()``

21. ``¬ ¬ ¬ ¬ iteration = 0``
22. ``¬ ¬ ¬ ¬ clock = self.mod_Pygame__.time.Clock()``
23. ``¬ ¬ ¬ ¬ if self.RunFullStartup == True:``
24. ``¬ ¬ ¬ ¬ ¬ while iteration <= (60*3):``
25. ``¬ ¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
26. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
27. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(NameText, ((self.realWidth-NameTextWidth)/2, (self.realHeight-NameTextHeight)/2))``
28. ``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``

29. ``¬ ¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
30. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
31. ``¬ ¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
32. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``
33
34. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
35. ``¬ ¬ ¬ ¬ ¬ ¬ clock.tick(60)``
36. ``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
37. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
38. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

39. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
40. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
41. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
42. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
43. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
44. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``
45. ``¬ ¬ ¬ ¬ ¬ iteration = 0``

46. ``¬ ¬ ¬ ¬ ¬ while iteration <= (60*2):``
47. ``¬ ¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
48. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
49. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(NameText, ((self.realWidth-NameTextWidth)/2, (self.realHeight-NameTextHeight)/2))``
50. ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(PresentsText, ((((self.realWidth-NameTextWidth)/2)+120), ((self.realHeight-NameTextHeight)/2)+30))``
51. ``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1``

52. ``¬ ¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
53. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
54. ``¬ ¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
55. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

56. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
57. ``¬ ¬ ¬ ¬ ¬ ¬ clock.tick(60)``
58. ``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
59. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
60. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

61. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
62. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
63. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
64. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
65. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
66. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``

67. ``¬ ¬ ¬ ¬ ¬ iteration = 0``

68. ``¬ ¬ ¬ ¬ while iteration <= (60*3):``
69. ``¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
70. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
71. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftText, ((self.realWidth-PycraftTextWidth)/2, (self.realHeight-PycraftTextHeight)/2))``
72. ``¬ ¬ ¬ ¬ ¬ iteration += 1``

73. ``¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
74. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
75. ``¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
76. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

77. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
78. ``¬ ¬ ¬ ¬ ¬ clock.tick(60)``
79. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
80. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
81. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

82. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
83. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
84. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``

85. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
86. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
87. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``

88. ``¬ ¬ ¬ ¬ y = 0``
89. ``¬ ¬ ¬ ¬ while True:``
90. ``¬ ¬ ¬ ¬ ¬ self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()``
91. ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)``
92. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(PycraftText, ((self.realWidth-PycraftTextWidth)/2, ((self.realHeight-PycraftTextHeight)/2)-y))``
93. ``¬ ¬ ¬ ¬ ¬ y += 2``

94. ``¬ ¬ ¬ ¬ ¬ if self.realWidth < 1280:``
95. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
96. ``¬ ¬ ¬ ¬ ¬ if self.realHeight < 720:``
97. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

98. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()``
99. ``¬ ¬ ¬ ¬ ¬ clock.tick(60)``
100. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
101. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
102. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

103. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
104. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
105. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``

106. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
107. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
108. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ quit()``
109. ``¬ ¬ ¬ ¬ ¬ if ((self.realHeight-PycraftTextHeight)/2)-y <= 0:``
110. ``¬ ¬ ¬ ¬ ¬ ¬ self.RunFullStartup = False``
111. ``¬ ¬ ¬ ¬ ¬ ¬ return None``
112. ``¬ ¬ ¬ except Exception as Message:``
113. ``¬ ¬ ¬ ¬ self.RunFullStartup = False``
114. ``¬ ¬ ¬ ¬ return Message``

.. note::
    For information on this consult the above guide
    115. ``else:``
    116. ``¬ print("You need to run this as part of Pycraft")``
    117. ``¬ import tkinter as tk``
    118. ``¬ from tkinter import messagebox``
    119. ``¬ root = tk.Tk()``
    120. ``¬ root.withdraw()``
    121. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    122. ``¬ quit()``


TextUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_TextUtils>")``
    3. ``¬ class GenerateText:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def LoadQuickText(self):``
7. ``¬ ¬ ¬ LoadingText = ["Use W,A,S,D to move", "Use W to move forward", "Use S to move backward", "Use A to move left", "Use D to move right", "Access your inventory with E", "Access your map with R", "Use SPACE to jump", "Did you know there is a light mode?", "Did you know there is a dark mode?", "Check us out on GitHub", "Use ESC to remove camera movement", "Hold W to sprint", "Did you know you can change the sound volume in settings?", "Did you know you can change the music volume in settings?", "Did you know you can use L to lock the camera"]``
8. ``¬ ¬ ¬ locat = self.mod_Random__.randint(0, (len(LoadingText)-1))``
9. ``¬ ¬ ¬ text = LoadingText[locat]``
10. ``¬ ¬ ¬ return text``

.. note::
    For information on this consult the above guide
    11. ``else:``
    12. ``¬ print("You need to run this as part of Pycraft")``
    13. ``¬ import tkinter as tk``
    14. ``¬ from tkinter import messagebox``
    15. ``¬ root = tk.Tk()``
    16. ``¬ root.withdraw()``
    17. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    18. ``¬ quit()``


ThemeUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_ThemeUtils>")``
    3. ``¬ class DetermineThemeColours:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def GetColours(self):``
7. ``¬ ¬ ¬ try:``
8. ``¬ ¬ ¬ ¬ self.themeArray = [[(255, 255, 255), [30, 30, 30], (80, 80, 80), (237, 125, 49), (255, 255, 255)], [(0, 0, 0), [255, 255, 255], (80, 80, 80), (237, 125, 49), (100, 100, 100)]]``
9. ``¬ ¬ ¬ ¬ if self.theme == "dark":``
10. ``¬ ¬ ¬ ¬ ¬ self.FontCol = self.themeArray[0][0]``
11. ``¬ ¬ ¬ ¬ ¬ self.BackgroundCol = self.themeArray[0][1]``
12. ``¬ ¬ ¬ ¬ ¬ self.ShapeCol = self.themeArray[0][2]``
13. ``¬ ¬ ¬ ¬ ¬ self.AccentCol = self.themeArray[0][3]``
14. ``¬ ¬ ¬ ¬ ¬ self.SecondFontCol = self.themeArray[0][4]``
15. ``¬ ¬ ¬ ¬ elif self.theme == "light":``
16. ``¬ ¬ ¬ ¬ ¬ self.FontCol = self.themeArray[1][0]``
17. ``¬ ¬ ¬ ¬ ¬ self.BackgroundCol = self.themeArray[1][1]``
18. ``¬ ¬ ¬ ¬ ¬ self.ShapeCol = self.themeArray[1][2]``
19. ``¬ ¬ ¬ ¬ ¬ self.AccentCol = self.themeArray[1][3]``
20. ``¬ ¬ ¬ ¬ ¬ self.SecondFontCol = self.themeArray[1][4]``
21. ``¬ ¬ ¬ except Exception as Message:``
22. ``¬ ¬ ¬ ¬ return Message``


23. ``¬ ¬ def GetThemeGUI(self):``
24. ``¬ ¬ ¬ try:``
25. ``¬ ¬ ¬ ¬ clock = self.mod_Pygame__.time.Clock()``
26. ``¬ ¬ ¬ ¬ TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)``
27. ``¬ ¬ ¬ ¬ Title = TitleFont.render("Pycraft", True, (255, 255, 255))``
28. ``¬ ¬ ¬ ¬ MiddleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)``
29. ``¬ ¬ ¬ ¬ DarkModeFont = MiddleFont.render("Dark", True, (255, 255, 255))``
30. ``¬ ¬ ¬ ¬ LightModeFont = MiddleFont.render("Light", True, (255, 255, 255))``
31. ``¬ ¬ ¬ ¬ mousebuttondown = False``
32. ``¬ ¬ ¬ ¬ while self.theme == False:``
33. ``¬ ¬ ¬ ¬ ¬ self.Display.fill([30, 30, 30])``
34. ``¬ ¬ ¬ ¬ ¬ mX, mY = self.mod_Pygame__.mouse.get_pos()``
35. ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():``
36. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT:``
37. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Stop_Thread_Event.set()``

38. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
39. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_AdaptiveMode.join()``
40. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Thread_StartLongThread.join()``
41. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
42. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.quit()``
43. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Sys__.exit("Thanks for playing")``
44. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:``
45. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = True``
46. ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.MOUSEBUTTONUP:``
47. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``

48. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Title, (540, 0))``
49. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(DarkModeFont, (320, 360))``
50. ``¬ ¬ ¬ ¬ ¬ self.Display.blit(LightModeFont, (890, 360))``
51. ``¬ ¬ ¬ ¬ ¬ DarkRect = self.mod_Pygame__.Rect(260, 300, 200, 160)``
52. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (80, 80, 80), DarkRect, 3)``
53. ``¬ ¬ ¬ ¬ ¬ LightRect = self.mod_Pygame__.Rect(820, 300, 200, 160)``
54. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (80, 80, 80), LightRect, 3)``
55. ``¬ ¬ ¬ ¬ ¬ if mX >= 260 and mX <= 460 and mY >= 300 and mY <= 460:``
56. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
57. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "dark"``
58. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.base_folder = self.mod_OS__.path.dirname(__file__)``
59. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``
60. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
61. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.set_volume(50)``
62. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
63. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.play()``
64. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
65. ``¬ ¬ ¬ ¬ ¬ elif mX >= 820 and mX <= 980 and mY >= 300 and mY <= 460:``
66. ``¬ ¬ ¬ ¬ ¬ ¬ if mousebuttondown == True:``
67. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.theme = "light"``
68. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.base_folder = self.mod_OS__.path.dirname(__file__)``
69. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))``
70. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
71. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.set_volume(50)``
72. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ``
73. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.music.play()``
74. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ mousebuttondown = False``
75. ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()``
76. ``¬ ¬ ¬ ¬ ¬ clock.tick(60)``
77. ``¬ ¬ ¬ except Exception as Message:``
78. ``¬ ¬ ¬ ¬ Message = str(Message)+" in <Pycraft_ThemeUtils>"``
79. ``¬ ¬ ¬ ¬ return Message``

80. ``¬ ¬ ¬ return None``

.. note::
    For information on this consult the above guide
    81. ``else:``
    82. ``¬ print("You need to run this as part of Pycraft")``
    84. ``¬ import tkinter as tk``
    84. ``¬ from tkinter import messagebox``
    85. ``¬ root = tk.Tk()``
    86. ``¬ root.withdraw()``
    87. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
    88. ``¬ quit()``


ThreadingUtils
====================
Overview
++++++++++++++++++++

Detailed Breakdown
++++++++++++++++++++

.. note::
    For information on this consult the above guide
    1. ``if not __name__ == "__main__":``
    2. ``¬ print("Started <Pycraft_ThreadingUtils>")``
    3. ``¬ class ThreadingUtils:``
    4. ``¬ ¬ def __init__(self):``
    5. ``¬ ¬ ¬ pass``

6. ``¬ ¬ def StartVariableChecking(self):``
7. ``¬ ¬ ¬ while True:``
8. ``¬ ¬ ¬ ¬ if self.Iteration > 1000:``
9. ``¬ ¬ ¬ ¬ ¬ self.aFPS = (self.aFPS/self.Iteration)``
10. ``¬ ¬ ¬ ¬ ¬ self.Iteration = 1``
11. ``¬ ¬ ¬ ¬ self.FPS = int(self.FPS)``
12. ``¬ ¬ ¬ ¬ self.eFPS = int(self.eFPS)``

13. ``¬ ¬ ¬ ¬ self.mod_Time__.sleep(1)``

14. ``¬ ¬ ¬ ¬ if self.Stop_Thread_Event.is_set():``
15. ``¬ ¬ ¬ ¬ ¬ break``
16. ``¬ ¬ ``
17. ``¬ ¬ def StartCPUlogging(self):``
18. ``¬ ¬ ¬ while True:``
19. ``¬ ¬ ¬ ¬ if self.Devmode == 10:``
20. ``¬ ¬ ¬ ¬ ¬ if self.Timer >= 2:``
21. ``¬ ¬ ¬ ¬ ¬ ¬ CPUPercent = self.mod_Psutil__.cpu_percent(0.2)``
22. ``¬ ¬ ¬ ¬ ¬ ¬ if CPUPercent > self.Data_CPUUsE_Max:``
23. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = CPUPercent``
24. ``¬ ¬ ¬ ¬ ¬ ¬ elif CPUPercent < self.Data_CPUUsE_Min:``
25. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = CPUPercent``

26. ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE.append([((self.realWidth/2)+100)+(self.Timer-2), 200-(100/self.Data_CPUUsE_Max)*CPUPercent])``
27. ``¬ ¬ ¬ ¬ ¬ else:``
28. ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(0.2)``
29. ``¬ ¬ ¬ ¬ else:``
30. ``¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(1)``

31. ``¬ ¬ ¬ ¬ if self.Stop_Thread_Event.is_set():``
32. ``¬ ¬ ¬ ¬ ¬ break``

33. ``¬ ¬ def AdaptiveMode(self):``
34. ``¬ ¬ ¬ while True:``
35. ``¬ ¬ ¬ ¬ if self.Stop_Thread_Event.is_set():``
36. ``¬ ¬ ¬ ¬ ¬ break``
37. ``¬ ¬ ¬ ¬ ``
38. ``¬ ¬ ¬ ¬ if self.SettingsPreference == "Adaptive":``
39. ``¬ ¬ ¬ ¬ ¬ CPUPercent = self.mod_Psutil__.cpu_percent()``
40. ``¬ ¬ ¬ ¬ ¬ CoreCount = self.mod_Psutil__.cpu_count()``

41. ``¬ ¬ ¬ ¬ ¬ try:``
42. ``¬ ¬ ¬ ¬ ¬ ¬ gpus = self.mod_GPUtil__.getGPUs()``

43. ``¬ ¬ ¬ ¬ ¬ ¬ GPUPercent = 0``
44. ``¬ ¬ ¬ ¬ ¬ ¬ NumOfGPUs = 0``

45. ``¬ ¬ ¬ ¬ ¬ ¬ for gpu in gpus:``
46. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ NumOfGPUs += 1``
47. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ GPUPercent += gpu.load*100``

48. ``¬ ¬ ¬ ¬ ¬ ¬ GPUPercent = GPUPercent/NumOfGPUs``
49. ``¬ ¬ ¬ ¬ ¬ ``
50. ``¬ ¬ ¬ ¬ ¬ except:``
51. ``¬ ¬ ¬ ¬ ¬ ¬ GPUPercent = CPUPercent``

52. ``¬ ¬ ¬ ¬ ¬ if (CPUPercent >= (100/CoreCount)) and (GPUPercent >= (100/CoreCount)):``
53. ``¬ ¬ ¬ ¬ ¬ ¬ self.FPS -= 10``
54. ``¬ ¬ ¬ ¬ ¬ else:``
55. ``¬ ¬ ¬ ¬ ¬ ¬ if self.FPS < self.RecommendedFPS:``
56. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS += 10``
57. ``¬ ¬ ¬ ¬ ¬ ¬ else:``
58. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not (self.FPS == self.RecommendedFPS):``
59. ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.FPS -= 1``
60. ``¬ ¬ ¬ ¬ ¬ ``
61. ``¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(0.2)``
62. ``¬ ¬ ¬ ¬ else:``
63. ``¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(1)``

.. note::
    For information on this consult the above guide
   1.  ``else:``
   2.  ``¬ print("You need to run this as part of Pycraft")``
   3.  ``¬ import tkinter as tk``
   4.  ``¬ from tkinter import messagebox``
   5.  ``¬ root = tk.Tk()``
   6.  ``¬ root.withdraw()``
   7.  ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
   8.  ``¬ quit()``


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
9. ``¬ ¬ ¬ DataWindow.configure(width = 500, height = 300)``
10. ``¬ ¬ ¬ DataWindow.configure(bg="lightblue")``
11. ``¬ ¬ ¬ VersionData = f"Pycraft: v{self.version}"``
12. ``¬ ¬ ¬ CoordinatesData = f"Coordinates: x: {self.X} y: {self.Y} z: {self.Z} Facing: 0.0, 0.0, 0.0"``
13. ``¬ ¬ ¬ FPSData = f"FPS: Actual: {self.eFPS} Max: {self.FPS}"``
14. ``¬ ¬ ¬ VersionData = self.mod_Tkinter__tk.Label(DataWindow, text=VersionData)``
15. ``¬ ¬ ¬ CoordinatesData = self.mod_Tkinter__tk.Label(DataWindow, text=CoordinatesData)``
16. ``¬ ¬ ¬ FPSData = self.mod_Tkinter__tk.Label(DataWindow, text=FPSData)``
17. ``¬ ¬ ¬ VersionData.grid(row = 0, column = 0, columnspan = 2)``
18. ``¬ ¬ ¬ CoordinatesData.grid(row = 1, column = 0, columnspan = 2)``
19. ``¬ ¬ ¬ FPSData.grid(row = 2, column = 0, columnspan = 2)``
20. ``¬ ¬ ¬ DataWindow.mainloop()``
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