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

3. ``¬ from tkinter import messagebox`` Here we are importing specific sections of "Tkinter", in this case; ``messagebox``, this module allows us to make dialogue boxes that are commonplace in Windows and Apple based devices.

4. ``¬ root = tk.Tk()`` This of code is required to make the dialogue box, which is what we want. This will create a window to the default size "Tkinter" has defined, and initialises the ``messagebox`` module, which we want.

5. ``¬ root.withdraw()`` We use this code to hide the window that appears by using the previous  ``root`` is the internal name for the window, as that is what the window created in the previous was stored in (as a variable).

6. ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")`` Here we make our all to the ``messagebox`` module, which has several pre-made dialogue boxes, we are using the ``showerror`` pre-made dialogue box procedure here. We give it the caption of ``"Startup Fail"``, and then elaborate on the issue in the main body of the window, by displaying the text ``"You need to run this as part of Pycraft, please run the 'main.py' file"``.

7. ``¬ quit()`` This is Python's way of closing the project, we normally use ``sys.exit`` for this, which you will see later on, because its  a bit cleaner on some IDLE's and terminals. However to reduce the length of this project, we use the built in function here instead.

Achievements
====================
Overview
++++++++++++++++++++
This module controls the displaying and processing of in-game achievements: This feature will be expanded upon when achievements are added and you can earn them in game.

The ``GenerateAchievements`` class controls the rendering of the achievements GUI this can be accessed from the 'home screen' of Pycraft, currently this class only renders a blank window, which is coloured and has a title [Pycraft] and header [Achievements], but expect an update here when its possible to earn achievements in game!

The ``Achievements(self)`` function, like most subroutines in Pycraft, takes ``self`` to be its only input. It will return only an error, should one arise, which will be stored in the ``messages`` variable. This subroutine is where the bulk of the processing for this class is done, this subroutine is responsible for the Achievements GUI which you can access through Pycraft's home screen.

Detailed Breakdown
++++++++++++++++++++
1. ``if not __name__ == "__main__":`` For information on this consult the above guide
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

18. ``while True:``
19. ``realWidth, realHeight = self.mod_Pygame__.display.get_window_size()``

20. ``if realWidth < 1280:``
21. ``self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)``
22. ``if realHeight < 720:``
23. ``self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)``

24. ``self.eFPS = self.clock.get_fps()``
25. ``self.aFPS += self.eFPS``
26. ``self.Iteration += 1``

27. ``tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)``

28. ``for event in self.mod_Pygame__.event.get():``
29. ``if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):``
30. ``if self.sound == True:``
31. ``self.mod_SoundUtils__.PlaySound.PlayClickSound(self)``
32. ``return None``
33. ``elif event.type == self.mod_Pygame__.KEYDOWN:``
34. ``if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:``
35. ``self.Devmode += 1``
36. ``if event.key == self.mod_Pygame__.K_q:``
37. ``self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)``
38. ``if event.key == self.mod_Pygame__.K_F11:``
39. ``self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)``
40. ``if event.key == self.mod_Pygame__.K_x:``
41. ``self.Devmode = 1``

42. ``self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")``

43. ``self.Display.fill(self.BackgroundCol)``

44. ``cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)``
45. ``self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)``
46. ``self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))``
47. ``self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))``

48. ``Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)``
49. ``if not Message == None:``
50. ``return Message``
51. ``self.mod_Pygame__.display.flip()``
52. ``self.clock.tick(tempFPS)``
53. ``except Exception as Message:``
54. ``return Message``
55. ``else:``
56. ``print("You need to run this as part of Pycraft")``
57. ``import tkinter as tk``
58. ``from tkinter import messagebox``
59. ``root = tk.Tk()``
60. ``root.withdraw()``
61. ``messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")``
62. ``quit()``