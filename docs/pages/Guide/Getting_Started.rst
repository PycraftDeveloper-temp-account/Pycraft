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
             
* All modules should also be proceeded by the following code, the 'else' here is important, this connects to the 'if' statement we created above:

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

The ``GenerateAchievements`` class controls the rendering of the achievements GUI this can be accessed from the 'home screen' of Pycraft, currently this class only renders a blank window, which is coloured and has a title [Pycraft] and header [Achievements], but expect an update here when its possible to earn achievements in game!

The ``Achievements(self)`` function, like most subroutines in Pycraft, takes ``self`` to be its only input. It will return only an error, should one arise, which will be stored in the ``messages`` variable. This subroutine is where the bulk of the processing for this class is done, this subroutine is responsible for the Achievements GUI which you can access through Pycraft's home screen.

Detailed Breakdown
++++++++++++++++++++


.. note::
   For information on this consult the above guide

        1: ``if not __name__ == "__main__":``

        2: ``print("Started <Pycraft_Achievements>")``

        3: ``¬ class GenerateAchievements:``

        4: ``¬ ¬ def __init__(self):``

        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def Achievements(self):`` This line defines the Achievements class, this is whHere all achievements you have earned in-game will be displayed. You access this from the home screen and at present does very little, as thHere isn't much in game to do, and no achievements to earn. This procedure will be getting an update before Pycraft v0.11. This takes, as most subroutines only takes the variable 'self' which is defined in 'main.py'.

7: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

8: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

9: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

10: ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")`` This calls the 'GetNormalCaption' subroutine in 'CaptionUtils.py', This tool takes values from the variable 'self', which stores lots of the global variables stored in the entire program, and also a second input which, in this case its "Achievements" is asked for, this is useful for allowing the user to know what GUI they are in. The variable 'self' is called when the player has activated 'Devmode', (by pressing SPACE 10 times), this brings up lots of details in the caption regarding what the program is doing and the resources its using.

11: ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 60.

12: ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 35.

13: ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 15.


14: ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)`` Takes the font, which we stored in the variable 'MainTitleFont' and uses it to render the text "Pycraft", with the user's preference on anti-aliasing, 'aa' and the colour defined in 'ThemeUtils.py', the resulting Pygame.surface object is stored in the variable 'TitleFont'.

15: ``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()`` Gets the width (in pixels) of the Pygame.surface object 'TitleFont


16: ``¬ ¬ ¬ ¬ AchievementsFont = InfoTitleFont.render("Achievements", self.aa, self.SecondFontCol)`` Takes the font we loaded previously into the variable 'InfoTitleFont' and render the text 'Achievements, with the anti-aliasing based on the user's preference, and colour defined based on the user's colour theme.

17: ``¬ ¬ ¬ ¬ tempFPS = self.FPS`` This is used to temporarily store the game's target FPS, this is used later to slow the game down when minimised.


18: ``¬ ¬ ¬ ¬ while True:`` Enters the project's game loop

19: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()`` Gets the width and height of the current Pygame window (in pixels), this is used in working out whHere everything should be scaled in-game if the window is resized.


20: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:`` Detects if the window has been made smaller than the minimum width, 1280 pixels

21: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)`` If the window is smaller than 1280 pixels, then reset the display's WIDTH to 1280. ThHere is no limit to how large the display can be.

22: ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:`` Detects if the window has been made smaller than the minimum height, 720 pixels

23: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)`` If the window is smaller than 720 pixels, then reset the display's HEIGHT to 720. ThHere is no limit to how large the display can be.


24: ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()`` Gets the current window frame-rate (in Hz)

25: ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS`` Adds the current framerate to a variable which is used to calculate the mean average FPS in game (in Hz)

26: ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1`` Used as frequency in calculating the mean average FPS (in Hz)


27: ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)`` This line of code is used to control what happens when the display is minimised, for more information, see the documentation for this subroutine. This subroutine will return an integer, this is stored in the variable 'tempFPS', which is used to set the windows FPS (in Hz).


28: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, hHere we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

29: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):`` This controls when the display should close (if on the 'Home-Screen') or returning back to the previous window (typically the 'Home-Screen'), to do this you can press the 'x' at the top of the display, or by pressing 'ESC or ESCAPE' which is handy when in full-screen modes.

30: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:`` This if-statement controls if sound should be played or not based on the user's preference in 'Settings.py', the user's preference is stored when the program closes.

31: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)`` This line calls the subroutine; 'PlayClickSound' in 'SoundUtils.py', if the user has allowed sound to play in settings, then interacting with the display will cause the click sound to play; volume and other parameters for this subroutine are stored in the global variable 'self'.

32: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If thHere is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'Home-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'Home-Screen'.

33: ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:`` This line detects if any key is pressed on a keyboard, used when detecting events like pressing keys to navigate the GUIs or moving in-game.

34: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:`` This line of code is used as part of the activation for 'Devmode' which you activate by pressing SPACE 10 times. HHere we are detecting is the SPACE key has been pressed and 'Devmode' is not already active.

35: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1`` This line increases the value of the variable 'Devmode' by 1. When the variable 'Devmode' is equal to 0, then 'Devmode' is activated.

36: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:`` Detects if the key 'q' is pressed (not case sensitive).

37: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)`` If the key 'q' is pressed, then we load up the secondary window in 'TkinterUtils.py', this, like 'Devmode' displays information about the running program. This feature may be deprecated at a later date, but this isn't clear yet. All the data the subroutine needs to access is sent through the parameter 'self' which is a global variable.

38: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:`` This line detects if the function key 'F11' has been pressed.

39: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)`` If the function key 'F11' has been pressed, then resize the display by toggling full-screen. (The 'F11' key is commonly assigned to this in other applications).

40: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:`` Detects if the key 'x' is pressed (NOT case sensitive).

41: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1`` This resets 'Devmode' to 1, turning the feature off. This can be used to cancel counting the number of spaces pressed too.


42: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")`` This calls the 'GetNormalCaption' subroutine in 'CaptionUtils.py', This tool takes values from the variable 'self', which stores lots of the global variables stored in the entire program, and also a second input which, in this case its "Achievements" is asked for, this is useful for allowing the user to know what GUI they are in. The variable 'self' is called when the player has activated 'Devmode', (by pressing SPACE 10 times), this brings up lots of details in the caption regarding what the program is doing and the resources its using.


43: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.


44: ``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)`` This line defines the dimensions of a rectangle in Pygame, in this case the rectangle will be drawn at (0, 0) (x, y) with a width of 1280 and a height of 90. (all values hHere are in pixels and (0, 0) (x, y) is the top-left corner of the GUI (so thats 90 pixels DOWN)).

45: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)`` This line draws a rectangle to the display with 'self.Display', the colour to fill the rectangle is the colour of the background to Pycraft (This is a setting the user can change in the GUI in 'Settings.py') with the dimensions of the previously created Pygame Rect object called; 'cover_Rect'.

46: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))`` This line takes the Pygame.surface object 'TitleFont' and draws it onto the window (stored in the variable 'self.Display', at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. The coordinates are (x, y).

47: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))`` This line takes the Pygame.surface object 'AchievementsFont' and draws it onto the window (stored in the variable 'self.Display'), at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. We also add an offset of 55 pixels to make sure the two titles don't overlap.


48: ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)`` This line calls the subroutine 'CreateDevmodeGraph', this subroutine is responsible for drawing the graph you see at the top-right of most Pycraft GUI's. It takes the variable 'self' as a parameter, this code will return any errors, which are stored in the variable 'Message'. If thHere are no errors then the subroutine will return 'None'. The second parameter 'DataFont' is the currently loaded font which is used for rendering the text at the top of the graph.

49: ``¬ ¬ ¬ ¬ ¬ if not Message == None:`` This line detects if thHere are any errors stored in the variable 'Message'. All important errors are stored in this variable. This error detection may be moved to a thread at a later date.

50: ``¬ ¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', whHere they can be suitably handled.

51: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

52: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)`` This line of code controls how fast the GUI should refresh, defaulting to the user's preference unless the window is minimised, in which case its set to 15 FPS. All values for FPS are in (Hz) and this line of code specifies the maximum FPS of the window, but this does not guarantee that FPS.

53: ``¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

54: ``¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', whHere they can be suitably handled.



.. note::
   For information on this consult the above guide

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

        2: ``print("Started <Pycraft_Base>")``

3: ``¬ print("Started <Pycraft_Base>")`` This line outputs only when the project is first called in 'main.py', if the code continues to print the next line then no syntax errors occurred when initialising this module.


4: ``¬ import moderngl_window as mglw`` HHere we are importing the external module 'ModernGL_Window'. All calls to the module furthermore in this module will reference 'mglw'.

5: ``¬ from moderngl_window.scene.camera import KeyboardCamera, OrbitCamera`` HHere we are importing specific classes and code from the module 'ModernGL_Window'. We do this because they may not be added by default when importing that external module as a whole.



6: ``¬ class CameraWindow(mglw.WindowConfig):`` HHere we are creating a class called 'CameraWindow', we will reference this later on in the 'GameEngine.py', this class controls the basic window functionality of 'GameEngine.py'.

7: ``¬ ¬ """Base class with built in 3D camera support"""`` 


8: ``¬ ¬ def __init__(self, **kwargs):`` HHere we are initialising the class by defining and assigning some key variables which will be used frequently in all ModernGL enabled windows.

9: ``¬ ¬ ¬ super().__init__(**kwargs)`` 

10: ``¬ ¬ ¬ self.camera = KeyboardCamera(self.wnd.keys, aspect_ratio=self.wnd.aspect_ratio)`` HHere we setting the global variable self.camera to a specific ModernGL object, its important to note, references to 'self' in this module do not relate to the 'self' variable used in other programs. This line of code creates a camera object (which we use to move around and rotate in 'GameEngine.py'). This line of code also detects keypresses in ModernGL_window enabled GUI's ('GameEngine.py' mainly) and sets the aspect ratio. This setting is specified in 'GameEngine.py'.

11: ``¬ ¬ ¬ self.camera_enabled = True`` This line confirms that we are using the camera as our main view in 'GameEngine.py'.


12: ``¬ ¬ def key_event(self, key, action, modifiers):`` This line of code defines a subroutine that detects keypresses on Moderngl enabled GUIs. This acts similarly to 'pygame.event.get()'.

13: ``¬ ¬ ¬ keys = self.wnd.keys`` This line of code gets a list of the keys that are on a typical keyboard as well as their 'state', essentially this means if the key is pressed or not.


14: ``¬ ¬ ¬ if self.camera_enabled:`` This line controls wether to accept keyboard inputs or not from the camera.

15: ``¬ ¬ ¬ ¬ self.camera.key_input(key, action, modifiers)`` This line of code gets the keyboard inputs from the camera. Its hHere whHere the state of each key specified in the variable 'keys'.


16: ``¬ ¬ ¬ if action == keys.ACTION_PRESS:`` This line detects if a key is pressed (essentially 'event.type == pygame.KEYDOWN' for Pygame)

17: ``¬ ¬ ¬ ¬ if key == keys.C:`` This if-statement controls what to do if the 'C' key is pressed down.

18: ``¬ ¬ ¬ ¬ ¬ self.camera_enabled = not self.camera_enabled`` This line toggles if the camera is enabled or not, and thus whHere to get events from.

19: ``¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = self.camera_enabled`` This line controls wether the mouse should be hidden or not based on if the camera is enabled or not; (If the camera is enabled (so 'True') then the mouse will be hidden and if the camera is disabled (so 'False') then the mouse will show and be able to leave the window.

20: ``¬ ¬ ¬ ¬ ¬ self.wnd.cursor = not self.camera_enabled`` In some implementations of the game, a cursor may show like crosshair in game, this line toggles wether to show that or not, based on if the camera is enabled or not (So if the camera is enabled, therefore the mouse will be invisible and the cursor will take the control of the mouse).

21: ``¬ ¬ ¬ ¬ if key == keys.SPACE:`` Detects if the SPACE key is pressed.

22: ``¬ ¬ ¬ ¬ ¬ self.timer.toggle_pause()`` Controls wether to continue running the program, or to pause it until the SPACE key is pressed again. This works like pausing and unpausing a video.


23: ``¬ ¬ def mouse_position_event(self, x: int, y: int, dx, dy):`` This subroutine controls how the camera should move based on the movement of the mouse.

24: ``¬ ¬ ¬ if self.camera_enabled:`` This line controls wether to accept keyboard inputs or not from the camera.

25: ``¬ ¬ ¬ ¬ self.camera.rot_state(-dx, -dy)`` This line of code will move the camera based on a vector of mouse movement (direction and magnitude, so for example left 60 pixels, or right 10).


26: ``¬ ¬ def resize(self, width: int, height: int):`` This subroutine controls what to do if the window is resized.

27: ``¬ ¬ ¬ self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)`` This subroutine will set the aspect ratio of the project to make sure every pixel in the window is being used, this stops black/white bars forming around the window if it is resized and the aspect ratio's don't match.



28: ``¬ class OrbitCameraWindow(mglw.WindowConfig):`` This class 'OrbitCameraWindow' is used when the variable 'self.camera_enabled' is set to 'False'. This allows us to move about our 3D world but changes its behaviour slightly.

29: ``¬ ¬ """Base class with built in 3D orbit camera support"""`` 


30: ``¬ ¬ def __init__(self, **kwargs):`` HHere we are initialising the class by defining and assigning some key variables which will be used frequently in all ModernGL enabled windows.

31: ``¬ ¬ ¬ super().__init__(**kwargs)`` 

32: ``¬ ¬ ¬ self.camera = OrbitCamera(aspect_ratio=self.wnd.aspect_ratio)`` Sets the camera to a different camera object from before. In this case we still take the same parameters for the aspect ratio of the camera, but negate 'self.wnd.keys' this time. This can be imagined as like setting the aspect ratio on the camera of a phone.

33: ``¬ ¬ ¬ self.camera_enabled = True`` This line confirms that we are using the camera as our main view in 'GameEngine.py'.


34: ``¬ ¬ def key_event(self, key, action, modifiers):`` This line of code defines a subroutine that detects keypresses on Moderngl enabled GUIs. This acts similarly to 'pygame.event.get()'.

35: ``¬ ¬ ¬ keys = self.wnd.keys`` This line of code gets a list of the keys that are on a typical keyboard as well as their 'state', essentially this means if the key is pressed or not.


36: ``¬ ¬ ¬ if action == keys.ACTION_PRESS:`` This line detects if a key is pressed (essentially 'event.type == pygame.KEYDOWN' for Pygame)

37: ``¬ ¬ ¬ ¬ if key == keys.C:`` This if-statement controls what to do if the 'C' key is pressed down.

38: ``¬ ¬ ¬ ¬ ¬ self.camera_enabled = not self.camera_enabled`` This line toggles if the camera is enabled or not, and thus whHere to get events from.

39: ``¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = self.camera_enabled`` This line controls wether the mouse should be hidden or not based on if the camera is enabled or not; (If the camera is enabled (so 'True') then the mouse will be hidden and if the camera is disabled (so 'False') then the mouse will show and be able to leave the window.

40: ``¬ ¬ ¬ ¬ ¬ self.wnd.cursor = not self.camera_enabled`` In some implementations of the game, a cursor may show like crosshair in game, this line toggles wether to show that or not, based on if the camera is enabled or not (So if the camera is enabled, therefore the mouse will be invisible and the cursor will take the control of the mouse).

41: ``¬ ¬ ¬ ¬ if key == keys.SPACE:`` Detects if the SPACE key is pressed.

42: ``¬ ¬ ¬ ¬ ¬ self.timer.toggle_pause()`` Controls wether to continue running the program, or to pause it until the SPACE key is pressed again. This works like pausing and unpausing a video.


43: ``¬ ¬ def mouse_position_event(self, x: int, y: int, dx, dy):`` This subroutine controls how the camera should move based on the movement of the mouse.

44: ``¬ ¬ ¬ if self.camera_enabled:`` This line controls wether to accept keyboard inputs or not from the camera.

45: ``¬ ¬ ¬ ¬ self.camera.rot_state(dx, dy)`` This line of code controls the rotation of the camera, but instead inverts the vector (so instead of panning left before, you'd now be panning right). This is still controlled by the movement of the mouse.


46: ``¬ ¬ def mouse_scroll_event(self, x_offset: float, y_offset: float):`` This line of code created a subroutine 'mouse_scroll_event' which is used to handle what to do if the user scrolls the scroll-wheel of their mouse.

47: ``¬ ¬ ¬ if self.camera_enabled:`` This line controls wether to accept keyboard inputs or not from the camera.

48: ``¬ ¬ ¬ ¬ self.camera.zoom_state(y_offset)`` This line zooms the camera in and out based on the amount the user turns the scroll-wheel. This can be imagined as zooming in on a camera, or looking through the scope of a gun in a game.


49: ``¬ ¬ def resize(self, width: int, height: int):`` This subroutine controls what to do if the window is resized.



.. note::
   For information on this consult the above guide

        1: ``if not __name__ == "__main__":``

        2: ``print("Started <Pycraft_Benchmark>")``

        3: ``¬ class GenerateBenchmarkMenu:``

        4: ``¬ ¬ def __init__(self):``

        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def Benchmark(self):`` This line creates the subroutine that creates and does the majority of the processing for the Benchmark GUI, it takes only the parameter 'self' and returns either 'None' or an error in the 'Message' variable should one occur.

7: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

8: ``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).pause()`` This line stops the sound in channel 2 from playing by pausing it, this sound is the background track that plays when not in game (This is controlled by the user's setting). If no sound is playing then this has no effect.

9: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

10: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

11: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark")`` HHere we update the cation of the window from the previous caption to this. The variable 'self.version' is defined at the start of the program in 'main.py'.

12: ``¬ ¬ ¬ ¬ self.VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` HHere we load the project's default from from the fonts folder (it's 'Book Antiqua'), we store this in the variable 'self.VersionFont'. We set the font's size hHere to 20

13: ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 60.

14: ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 35.

15: ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 15.

16: ``¬ ¬ ¬ ¬ DetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)`` HHere we load the project's default from from the fonts folder (it's 'Book Antiqua'), we store this in the variable 'DetailsFont'. We also set it's size to 20.

17: ``¬ ¬ ¬ ¬ InfoDetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` HHere we load the project's default from from the fonts folder (it's 'Book Antiqua'), we store this in the variable 'InfoDetailsFont'. We also set it's size to 15.

18: ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)`` Takes the font, which we stored in the variable 'MainTitleFont' and uses it to render the text "Pycraft", with the user's preference on anti-aliasing, 'aa' and the colour defined in 'ThemeUtils.py', the resulting Pygame.surface object is stored in the variable 'TitleFont'.

19: ``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()`` Gets the width (in pixels) of the Pygame.surface object 'TitleFont


20: ``¬ ¬ ¬ ¬ BenchmarkFont = InfoTitleFont.render("Benchmark", self.aa, self.SecondFontCol)`` HHere we are creating a Pygame.surface object with the text 'Benchmark', we also set the anti-aliasing to the user's preference (which can be changed in settings), and set the font's colour to the secondary font colour, defined in 'ThemeUtils.py'. We store the Pygame.surface object in the variable 'BenchmarkFont'.

21: ``¬ ¬ ¬ ¬ FPSinfoTEXT = DetailsFont.render("FPS benchmark results", self.aa, self.FontCol)`` HHere we are creating a Pygame.surface object using the font 'DetailsFont', which we loaded earlier. We render the text 'FPS benchmark results' to this, setting anti-aliasing to the user's preference (defined in 'Settings.py') and setting the colour to the primary font colour defined in 'ThemeUtils.py', which can be changed by the user.

22: ``¬ ¬ ¬ ¬ FPSinfoTEXTWidth = FPSinfoTEXT.get_width()`` On this line we get the width (in pixels) of the Pygame.surface object FPSinfoTEXT. We store the resulting number in the variable 'FPSintoTEXTWidth'.

23: ``¬ ¬ ¬ ¬ FILEinfoTEXT = DetailsFont.render("Read test results", self.aa, self.FontCol)`` HHere we are rendering the text 'Read test results' with the font 'DetailsFont', which we loaded earlier. As with most font rendering we also set the anti-aliasing to the user's preference (which can be changed in settings), and the colour to the colour argument in the variable 'FILEinfoTEXT'

24: ``¬ ¬ ¬ ¬ FILEinfoTEXTWidth = FILEinfoTEXT.get_width()`` HHere we are getting the length (in pixels) of the Pygame.surface object 'FILEinfoTEXT', this will be used to calculate whHere to place the text on the window.

25: ``¬ ¬ ¬ ¬ HARDWAREinfoTEXT = DetailsFont.render("Hardware results", self.aa, self.FontCol)`` HHere we are rendering the text 'Hardware results' using the font we loaded earlier; 'DetailsFont'. We also use the user's preference in anti-aliasing and use the appropriate colour scheme from the theme the user has selected. We store this in the variable 'HARDWAREinfoTEXT'.

26: ``¬ ¬ ¬ ¬ HARDWAREinfoTEXTwidth = HARDWAREinfoTEXT.get_width()`` HHere we are getting the width (in pixels) of the Pygame.surface object HARDWAREinfoTEXT. This is used in making sure the text is drawn to the window in the appropriate position.


27: ``¬ ¬ ¬ ¬ SixtyFPSData = DataFont.render("60 Hz", self.aa, self.AccentCol)`` HHere we are rendering the text '60 Hz' using the font 'DataFont', and the suer's preference on anti-aliasing (which is defined in 'Settings.py') and the appropriate colour from the user's selected theme. This is stored in the variable 'SixtyFPSData', this acts as a marker on the graph of whHere 60 FPS lies (FPS is measured in Hz).

28: ``¬ ¬ ¬ ¬ OneFourFourFPSData = DataFont.render("144 Hz", self.aa, self.AccentCol)`` HHere we are rendering the text '144 Hz' using the font 'DataFont', and the user's preference on anti-aliasing (which is defined in 'Settings.py') and the appropriate colour from the user's selected theme. This is stored in the variable 'OneFourFourFPSData', this acts as a marker on the graph of whHere 144 FPS lies (FPS is measured in Hz).

29: ``¬ ¬ ¬ ¬ TwoFortyFPSData = DataFont.render("240 Hz", self.aa, self.AccentCol)`` HHere we are rendering the text '240 Hz' using the font 'DataFont', and the user's preference on anti-aliasing (which is defined in 'Settings.py') and the appropriate colour from the user's selected theme. This is stored in the variable 'TwoFortyFPSData', this acts as a marker on the graph of whHere 240 FPS lies (FPS is measured in Hz).


30: ``¬ ¬ ¬ ¬ InfoFont1 = DataFont.render("Welcome to Benchmark mode, press the SPACE bar to continue or press ANY other key to cancel, or press 'X'", self.aa, self.FontCol)`` HHere we are giving the user instructions on how to use benchmark mode, telling them they can cancel the benchmark at any time by pressing any key. We store the resulting Pygame.surface output from this function in the variable 'InfoFont1'. In addition we use the user's choice on anti-aliasing and choose an appropriate colour from the user's selected theme.

31: ``¬ ¬ ¬ ¬ InfoFont2 = DataFont.render("Benchmark mode is used to make the 'ADAPTIVE' feature in settings function and also to give an indication of the experience you are likely to get on this device", self.aa, self.FontCol)`` HHere we are giving the user details on what the benchmark mode can be used for, we render this text with the user's preference on anti-aliasing and choose a suitable colour from their theme. We store the output from this in 'InfoFont2'.

32: ``¬ ¬ ¬ ¬ InfoFont3 = DataFont.render("Benchmark mode consists of several stages:", self.aa, self.FontCol)`` HHere we are giving details on how the program works to the user. This is given over several lines as Pygame doesn't wrap text to the edge of the window, which is one reason why the user cannot use a resolution lower than (1280x720), because in some cases text would be rendered off the screen. We will always respect the user's colour scene and anti-aliasing preferences hHere.

33: ``¬ ¬ ¬ ¬ InfoFont4 = DataFont.render("First it will gather some basic information about your system", self.aa, self.FontCol)`` HHere we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences hHere.

34: ``¬ ¬ ¬ ¬ InfoFont5 = DataFont.render("Then it will test your maximum frame rate on a blank screen, then with a basic animation, and finally in a 3D OpenGL space", self.aa, self.FontCol)`` HHere we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences hHere.   

35: ``¬ ¬ ¬ ¬ InfoFont6 = DataFont.render("After its done that the focus moves on to a quick storage test, before finishing", self.aa, self.FontCol)`` HHere we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences hHere.   

36: ``¬ ¬ ¬ ¬ InfoFont7 = DataFont.render("Your results will then be displayed on screen with your frame rate scores on a line graph and the rest detailed to the right", self.aa, self.FontCol)`` HHere we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences hHere.   

37: ``¬ ¬ ¬ ¬ InfoFont8 = DataFont.render("During the time the benchmark is running the window may appear unresponsive, don't panic this can be expected.", self.aa, self.FontCol)`` HHere we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences hHere.   

38: ``¬ ¬ ¬ ¬ InfoFont9 = DataFont.render("In addition to achieve the best scores try to avoid doing anything else on the computer whilst the benchmark runs", self.aa, self.FontCol)`` HHere we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preference's hHere.   

39: ``¬ ¬ ¬ ¬ InfoFont10 = DataFont.render("This benchmark may show some system instability or cause your device to get warm, you use this at your own risk!", self.aa, (255, 0, 0))`` HHere we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences hHere.   


40: ``¬ ¬ ¬ ¬ stage = 0`` HHere we are setting the user's 'stage', this essentially tells controls which step of the process should be processed and rendered. With the completion of each 'stage', it is incremented by 1.


41: ``¬ ¬ ¬ ¬ resize = False`` This prevents the display from being resized during the tests, as resizing the display can alter the results, and when in full-screen, Pygame does some hardware acceleration to further improve performance, so you could get contrasting results.


42: ``¬ ¬ ¬ ¬ while True:`` Enters the project's game loop

43: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()`` Gets the width and height of the current Pygame window (in pixels), this is used in working out whHere everything should be scaled in-game if the window is resized.


44: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:`` Detects if the window has been made smaller than the minimum width, 1280 pixels

45: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)`` If the window is smaller than 1280 pixels, then reset the display's WIDTH to 1280. ThHere is no limit to how large the display can be.

46: ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:`` Detects if the window has been made smaller than the minimum height, 720 pixels

47: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)`` If the window is smaller than 720 pixels, then reset the display's HEIGHT to 720. ThHere is no limit to how large the display can be.


48: ``¬ ¬ ¬ ¬ ¬ if stage == 0:`` HHere we are starting the benchmark process by checking to see if the value of 'stage' is 0, if it is then we run the code allocated to that section.

49: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

50: ``¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)`` This line defines the dimensions of a rectangle in Pygame, in this case the rectangle will be drawn at (0, 0) (x, y) with a width of 1280 and a height of 90. (all values hHere are in pixels and (0, 0) (x, y) is the top-left corner of the GUI (so thats 90 pixels DOWN)).

51: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)`` This line draws a rectangle to the display with 'self.Display', the colour to fill the rectangle is the colour of the background to Pycraft (This is a setting the user can change in the GUI in 'Settings.py') with the dimensions of the previously created Pygame Rect object called; 'cover_Rect'.

52: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))`` This line takes the Pygame.surface object 'TitleFont' and draws it onto the window (stored in the variable 'self.Display', at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. The coordinates are (x, y).

53: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))`` HHere we are rendering the Pygame.surface object 'BenchmarkFont' to our display, setting its position (in pixels) to just off centre so it doesn't overlap with the title.

54: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont1, (3, 100))`` HHere we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.

55: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont2, (3, 130))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so

56: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont3, (3, 145))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so

57: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont4, (3, 160))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so

58: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont5, (3, 175))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.

59: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont6, (3, 190))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.

60: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont7, (3, 220))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.

61: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont8, (3, 235))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.

62: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont9, (3, 250))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.

63: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont10, (3, 280))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.


64: ``¬ ¬ ¬ ¬ ¬ if stage == 1:`` This if-statement detects if the previous stage has been completed, and will move the user on-to the next section. 

65: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Getting System Information")`` Here we are setting the caption of the display to appropriately tell the user what the program is doing at this stage.

66: ``¬ ¬ ¬ ¬ ¬ ¬ CPUid = f"{self.mod_CPUinfo__.get_cpu_info()['brand_raw']} w/{self.mod_Psutil__.cpu_count(logical=False)} cores @ {self.mod_Psutil__.cpu_freq().max} MHz"`` Here we are getting the information for the hardware of the system. This will be rendered later, so we format it into a way the user will understand. 'self.mod_CPUinfo__.get_cpu_info()["brand_raw"]' gets the make of the CPU (typically 'AMD' or 'Intel') as well as the model; for example, if I was running an 'AMD Ryzen 7 5700x', then that is what that subroutine would return. 'self.mod_Psutil.cpu_count(logical=False)' gives us the number of cores the CPU has, this is the same number that should appear in system information. 'self.mod_Psutil__.cpu_freq().max' returns the maximum factory clock speed of your CPU (In MHz).  

67: ``¬ ¬ ¬ ¬ ¬ ¬ RAMid = f"{round((((self.mod_Psutil__.virtual_memory().total)/1000)/1000/1000),2)} GB of memory, with {self.mod_Psutil__.virtual_memory().percent}% used"`` Here we are getting the details of the user's RAM, and formatting it appropriately so this can be rendered to text later on without additional processing. 'self.od_Psutil__.virtual_memory().total' gets the amount of physical memory installed in your machine that the program can access (This does NOT include hardware reserved memory), we are also converting this output from bytes to gigabytes, or this would be a really big number and not very readable. 'self.mod_Psutil__.virtual_memory().percent' returns the amount of memory allocated to other tasks on the system.

68: ``¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFO = DataFont.render(CPUid, self.aa, (255, 255, 255))`` Here we are converting the variable 'CPUid', which is a string, into a Pygame.surface object, respecting the user's preference on anti-aliasing, but forcing the colour to white (which is a bug, this will be fixed in Pygame v0.9.4). The resulting Pygame.surface object is stored in the variable 'CPUhwINFO', which is abbreviated from 'CPU-hardware-information'.

69: ``¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFOwidth = CPUhwINFO.get_width()`` Here we are getting the width (in pixels) of the Pygame.surface object; 'CPUhwINFO'. This will be used to help appropriately place the text later on.


70: ``¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFO = DataFont.render(RAMid, self.aa, (255, 255, 255))`` Here we are rendering the system information we gathered for RAM, rendering the formatted tet respecting the user's preference on anti-aliasing and setting the colour to white (this is a bug, this will be fixed in the next update to Pycraft).

71: ``¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFOwidth = RAMhwINFO.get_width()`` Here we are getting the width (in pixels) of the Pygame.surface object we have just created; 'RAMhwINFO'.

72: ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1`` Now we are finished with the current stage so increment the stage variable by 1, and more on forwards to the next stage.


73: ``¬ ¬ ¬ ¬ ¬ if stage == 2:`` Here we are detecting if the integer stored in the variable 'stage' is equal to 2, in which case we do this stage.

74: ``¬ ¬ ¬ ¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

75: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3 = self.mod_ExBenchmark__.LoadBenchmark.run(self)`` Here we are running a benchmark in 'ExBenchmark' (short for 'ExternalBenchmark'), and once this has completed, receiving the results of the subroutine through the 7 variables. This subroutine takes only the global variable self, and outputs 7 pieces of data, if completed successfully. 'Message' is a string, this stores any errors that may occur when running the subroutine. 'FPSlistX', 'FPSlistX2' and 'FPSlistx3' each store the 'x' coordinate for the graph, which we will draw later. Each of these lists contains a sequence of numbers, going up in 1's for the framerate of each frame of the benchmark. 'FPSlistY', 'FPSlistY1' and 'FPSlistY2' store the results of each of the three benchmarks running, 'FPSlistY' stores the blank window test, 'FPSlistY2' stores the result of the 2D graphics test, and 'FPSlistY3' stores the 3D render results.

76: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:`` This line detects if thHere are any errors stored in the variable 'Message'. All important errors are stored in this variable. This error detection may be moved to a thread at a later date.

77: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', whHere they can be suitably handled.

78: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)`` Here we are creating our Pygame display through the subroutine 'SetDisplay' in 'DisplayUtils.py'. All the parameters for this subroutine are sent through the variable 'self'.

79: ``¬ ¬ ¬ ¬ ¬ ¬ except:`` (This needs updating to follow the guidelines of the documentation) This ignores any errors that may occur when running the main section of the benchmark, or in creating our Pygame window.

80: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Cancelled benchmark")`` If an error does occur, then here we set the caption appropriately to let the user know the benchmark has been cancelled.

81: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If thHere is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'Home-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'Home-Screen'.

82: ``¬ ¬ ¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

83: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Finished self.FPS based benchmarks")`` Here we are setting the caption appropriately if the benchmark finished successfully, telling the user that (There is a noticeable bug here, this will be fixed) the program has 'Finished FPS based benchmarks'. We need to specifically say 'FPS based' here as there is also a drive test next.

84: ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1`` Now we are finished with the current stage so increment the stage variable by 1, and more on forwards to the next stage.


85: ``¬ ¬ ¬ ¬ ¬ if stage == 3:`` If stage 2 has finished without errors, then we move onto this stage.

86: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Starting disk read test")`` Here we update the Pygame window's caption with 'Starting disk read test' to tell the user that the benchmark has moved on to another stage.

87: ``¬ ¬ ¬ ¬ ¬ ¬ ReadIteration = 50`` Here we set the number of times a file should be read, in this case we need to read the file 50 times. The more reads the greater accuracy of the result.

88: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(ReadIteration):`` Here we start a for-loop that will repeat for the number of times we want the read test to be repeated.

89: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:`` Then we open the file we want to read from...

90: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Benchdata = Bench.read()`` We read the entire file and store the contents in the variable 'Benchdata'.


91: ``¬ ¬ ¬ ¬ ¬ ¬ aTime = 0`` Now we perform the test again, except this time we are recording the time taken, the previous test is designed more to prepare drives and 'wake then up' if they are idling or have stopped (which can drastically change the results of the test). Here we are setting the timer to 0 as this is the start of the test.

92: ``¬ ¬ ¬ ¬ ¬ ¬ ReadIteration = 50`` Here we set the number of times a file should be read, in this case we need to read the file 50 times. The more reads the greater accuracy of the result.

93: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(ReadIteration):`` Here we start a for-loop that will repeat for the number of times we want the read test to be repeated.

94: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ start = self.mod_Time__.perf_counter()`` Here we are getting a very accurate value for the time the system is at (in small fractions of a second), and storing that time in the variable 'start'.

95: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:`` Then we open the file we want to read from...

96: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Benchdata = Bench.read()`` We read the entire file and store the contents in the variable 'Benchdata'.

97: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ aTime += self.mod_Time__.perf_counter()-start`` Then we are adding the time delta (difference) between the current time and the time before we opened and read the file, this gives is an indication of how long the process took (the faster the drive, typically the less time this test takes).

98: ``¬ ¬ ¬ ¬ ¬ ¬ aTime = aTime/(ReadIteration+1)`` here we are working out the average time each read took, as repeating the experiment gives us a more accurate result, 'aTime' is abbreviated from 'averageTime'. This is a mean average (possible bug here; remove the '+1').

99: ``¬ ¬ ¬ ¬ ¬ ¬ ReadSpeed = (1/(aTime))`` Here we are calculating the number of files the drive can read in the average time we just calculated (time is in seconds, but will likely be a very small decimal). The file is just over 1 MB in size (Make this size 1 MB not 1.024 MB for later versions), so by using this calculation we can calculate how many megabytes-per-second the drive can read at, this is very rough and not very accurate, but it seems the easiest was to get current drive performance (I'm open to better solutions).

100: ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1`` Now we are finished with the current stage so increment the stage variable by 1, and more on forwards to the next stage.


101: ``¬ ¬ ¬ ¬ ¬ if stage == 4:`` Here we are, if the integer stored in the variable 'stage' is equal to 4, moving on to the next stage of the benchmark process.

102: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results.")`` We suitably update the caption to indicate we have moved on to the next stage, we use full-stops at the end of the caption here to indicate how through this process we are, as this stage takes a reasonably long time relative to the previous stage.

103: ``¬ ¬ ¬ ¬ ¬ ¬ Max1 = 0`` Here we are setting the maximum value for the blank window benchmark to 0, as the lowest FPS is 15, this number can be any number less than 15.

104: ``¬ ¬ ¬ ¬ ¬ ¬ Min1 = 60`` We set the minimum value for the blank image benchmark to 60, as this is an easily reachable target, this value cannot be lower than 15 as then that would be always smaller than the lowest FPS, both this and the previous variable must also be greater than 0.

105: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):`` Now we iterate over the frame-rate for the blank window benchmark.

106: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY[i] > Max1:`` If the value (FPS in Hz) of the element at position 'i' (where 'i' is abbreviated from 'iteration and is an integer that counts upwards from 0, this is used an an index for this list of values) is greater than the known maximum (so if the value of 'FPSlistY' is greater than, but NOT equal to the previously largest FPS)...

107: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max1 = FPSlistY[i]`` Then we set the new value of the variable 'Max1' to the current -larger- value in the list.

108: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY[i] < Min1:`` If the value stored at the current location is less than the previously known minimum...

109: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min1 = FPSlistY[i]`` Then we set the minimum value to the current value of the list.


110: ``¬ ¬ ¬ ¬ ¬ ¬ Max2 = 0`` Here we are defining the maximum value for the 2D render test.

111: ``¬ ¬ ¬ ¬ ¬ ¬ Min2 = 60`` Here we are defining the minimum value for the 2D render test, these values are chosen to be easily beatable, so that the minimum and maximum values of the data can be accurately recorded.

112: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):`` Now we iterate over the frame-rate (in Hz) for the results of the 2D render test.

113: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY2[i] > Max2:`` If the value (FPS in Hz) of the element at position 'i' (where 'i' is abbreviated from 'iteration and is an integer that counts upwards from 0, this is used an an index for this list of values) is greater than the known maximum (so if the value of 'FPSlistY1' is greater than, but NOT equal to the previously largest FPS)... 

114: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max2 = FPSlistY2[i]`` Then we set the new value of the variable 'Max2' to the current -larger- value in the list 'FPSlistY2'.

115: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY2[i] < Min2:`` If the value stored at the current location is less than the previously known minimum...

116: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min2 = FPSlistY2[i]`` Then we set the minimum value to the current value of the list.


117: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results..")`` Now we have gone through roughly hald the data processing so can update the caption by adding another '.'...

118: ``¬ ¬ ¬ ¬ ¬ ¬ Max3 = 0`` Here we are defining the maximum value for the 3D render test.

119: ``¬ ¬ ¬ ¬ ¬ ¬ Min3 = 60`` Here we are defining the minimum value for the 3D render test, these values are chosen to be easily beatable, so that the minimum and maximum values of the data can be accurately recorded.

120: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY3)):`` Now we iterate over the frame-rate (in Hz) for the results of the 3D render test.

121: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY3[i] > Max3:`` If the value (FPS in Hz) of the element at position 'i' (where 'i' is abbreviated from 'iteration' and is an integer that counts upwards from 0, this is used an an index for this list of values) is greater than the known maximum (so if the value of 'FPSlistY3' is greater than, but NOT equal to the previously largest value)...

122: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max3 = FPSlistY3[i]`` Then we set the new value of the variable 'Max3' to the current -larger- value in the list 'FPSlistY3'.

123: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY3[i] < Min3:`` If the value stored at the current location is less than the previously known minimum...

124: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min3 = FPSlistY3[i]`` Then we set the minimum value to the current value of the list.


125: ``¬ ¬ ¬ ¬ ¬ ¬ if Max2 > Max1:`` Now we are checking to see which one of the three values is larger, this is done so we know what we need to make the graph go up to when we display the results in a line graph.

126: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max2`` The variable 'GlobalMax' will be assigned the larger of the two values 'Max1' and 'Max2'.

127: ``¬ ¬ ¬ ¬ ¬ ¬ elif Max3 > Max2:`` Then we check to see if the maximum value in the 3D render benchmark is greater than the maximum for the 2D render test.

128: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max3`` If the 3D render benchmark produced the highest framerate (unlikely) then we set the maximum value to that number in the variable 'GlobalMax'.

129: ``¬ ¬ ¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

130: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max1`` If all the preceding if-statements are false, the largest value must be in the variable 'max1', so that is what we store in the variable; 'GlobalMax'.


131: ``¬ ¬ ¬ ¬ ¬ ¬ self.RecommendedFPS = GlobalMax/2`` We calculate the 'recommended' frame rate by taking half of the largest FPS, this is because the highest frame-rates are not either recommended because of unnecessary CPU/GPU load and because the frame-rate slider in 'Settings.py' maxes out at 445.


132: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results...")`` Now we move on to the next section of processing, because we haven't yet finished, in this section we will now make sure that all the values from the three benchmarks fit onto the display appropriately.

133: ``¬ ¬ ¬ ¬ ¬ ¬ multiplier = len(FPSlistY)/(realWidth-20)`` This variable 'multiplier' controls how the line graph is drawn on the 'x' axis, without this our graph could easily stretch off the display, this also controls how far apart each of the 'points' are on the line graphs, we do this by taking the length of 'FPSlistY', it doesn't matter which one we choose because they are all the same length, then we divide that by the width of the display 'realWidth' (in pixels) which has had 20 pixels taken off of, we take 20 pixels off the variable 'realWidth' so that the graph can be centered with a 10 pixel border between the two sides, we do this so that it looks more appealing visually.

134: ``¬ ¬ ¬ ¬ ¬ ¬ temp = []`` Now we create a temporary blank array, these 'temp' variables are simply there to store data whilst it is being processed, the data should be moved to an appropriately named array once this processing has finished.

135: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):`` Now we iterate over the frame-rate for the blank window benchmark.

136: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY[i])))`` How we are iterating over each element in the black render test (which has the results stored in the variable 'FPSlistY'), we are taking the original value and converting it to a smaller value that is still representative, and will look the same on the graph, but will fit onto the area we have assigned the graphing to be. Not doing this step could result in the line graphs not fitting on-screen and being rendered upside-down. In order of processing; we divide 300 (the HEIGHT of the graphing area) by the 'GlobalMax', which stores the largest number that appears in all of the tests, this makes sure that none of the values are rendered outside of the graph. Then we multiply this by the current value of 'FPSlistY' as we iterate over the array. Then we take the result and flip it by taking it away from 300, this step is done because the larger the value the lower down the display it would have been drawn, mirroring the result, and making it really hard to interpret. Finally we offset the entire result by moving it down the display 130 pixels to allow for titles and subheadings above.

137: ``¬ ¬ ¬ ¬ ¬ ¬ FPSListY = temp`` Now we are taking the array stored in temp and moving it to the variable 'FPSlistY', which is more appropriately named.


138: ``¬ ¬ ¬ ¬ ¬ ¬ temp = []`` Now we create a temporary blank array, these 'temp' variables are simply there to store data whilst it is being processed, the data should be moved to an appropriately named array once this processing has finished.

139: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):`` Now we iterate over the frame-rate (in Hz) for the results of the 2D render test.

140: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY2[i])))`` Now we are iterating over each element in the black render test (which has the results stored in the variable 'FPSlistY'), we are taking the original value and converting it to a smaller value that is still representative, and will look the same on the graph, but will fit onto the area we have assigned the graphing to be. Not doing this step could result in the line graphs not fitting on-screen and being rendered upside-down. In order of processing; we divide 300 (the HEIGHT of the graphing area) by the 'GlobalMax', which stores the largest number that appears in all of the tests, this makes sure that none of the values are rendered outside of the graph. Then we multiply this by the current value of 'FPSlistY2' as we iterate over the array. Then we take the result and flip it by taking it away from 300, this step is done because the larger the value the lower down the display it would have been drawn, mirroring the result, and making it really hard to interpret. Finally we offset the entire result by moving it down the display 130 pixels to allow for titles and subheadings above.

141: ``¬ ¬ ¬ ¬ ¬ ¬ FPSListY2 = temp`` Now we are taking the array stored in temp and moving it to the variable 'FPSlistY2', which is more appropriately named.


142: ``¬ ¬ ¬ ¬ ¬ ¬ temp = []`` Now we create a temporary blank array, these 'temp' variables are simply there to store data whilst it is being processed, the data should be moved to an appropriately named array once this processing has finished.

143: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):`` Now we iterate over the frame-rate (in Hz) for the results of the 2D render test.

144: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY3[i])))`` Now we are iterating over each element in the black render test (which has the results stored in the variable 'FPSlistY3'), we are taking the original value and converting it to a smaller value that is still representative, and will look the same on the graph, but will fit onto the area we have assigned the graphing to be. Not doing this step could result in the line graphs not fitting on-screen and being rendered upside-down. In order of processing; we divide 300 (the HEIGHT of the graphing area) by the 'GlobalMax', which stores the largest number that appears in all of the tests, this makes sure that none of the values are rendered outside of the graph. Then we multiply this by the current value of 'FPSlistY3' as we iterate over the array. Then we take the result and flip it by taking it away from 300, this step is done because the larger the value the lower down the display it would have been drawn, mirroring the result, and making it really hard to interpret. Finally we offset the entire result by moving it down the display 130 pixels to allow for titles and subheadings above.

145: ``¬ ¬ ¬ ¬ ¬ ¬ FPSListY3 = temp`` Now we are taking the array stored in temp and moving it to the variable 'FPSlistY3', which is more appropriately named.


146: ``¬ ¬ ¬ ¬ ¬ ¬ Results1 = []`` Here we are creating an empty array and storing it in the variable 'Results1'

147: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):`` Now we iterate over the frame-rate for the blank window benchmark.

148: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results1.append([(FPSlistX[i]/multiplier), FPSListY[i]])`` Here we are grouping the two separate sets of data, the scores which we just iterated over and reformatted, and the sequence of elements in 'FPSlistX' that go up in the order (n). Here we are appropriately formatting the current value for 'FPSlistX' with the variable 'multiplier', as we where before, and also additionally combining it with the current re-formatted score stored in 'FPSlistY', this creates an array of points (x, y) (in pixels), that we can enter into a sub-routine later on to appropriately draw the corresponding line.


149: ``¬ ¬ ¬ ¬ ¬ ¬ Results2 = []`` Here we are creating an empty array and storing it in the variable 'Results2'

150: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):`` Now we iterate over the frame-rate (in Hz) for the results of the 2D render test.

151: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results2.append([(FPSlistX2[i]/multiplier), FPSListY2[i]])`` Here we are grouping the two separate sets of data, the scores which we just iterated over and reformatted, and the sequence of elements in 'FPSlistX' that go up in the order (n). Here we are appropriately formatting the current value for 'FPSlistX2' with the variable 'multiplier', as we where before, and also additionally combining it with the current re-formatted score stored in 'FPSlistY2', this creates an array of points (x, y) (in pixels), that we can enter into a sub-routine later on to appropriately draw the corresponding line.


152: ``¬ ¬ ¬ ¬ ¬ ¬ Results3 = []`` Here we are creating an empty array and storing it in the variable 'Results3'

153: ``¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY3)):`` Now we iterate over the frame-rate (in Hz) for the results of the 3D render test.

154: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Results3.append([(FPSlistX3[i]/multiplier), FPSListY3[i]])`` Here we are grouping the two separate sets of data, the scores which we just iterated over and reformatted, and the sequence of elements in 'FPSlistX3' that go up in the order (n). Here we are appropriately formatting the current value for 'FPSlistX3' with the variable 'multiplier', as we where before, and also additionally combining it with the current re-formatted score stored in 'FPSlistY3', this creates an array of points (x, y) (in pixels), that we can enter into a sub-routine later on to appropriately draw the corresponding line.


155: ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1`` Now we are finished with the current stage so increment the stage variable by 1, and more on forwards to the next stage.


156: ``¬ ¬ ¬ ¬ ¬ if stage == 5:`` Now we can, if the value of 'stage' is 5, move on to the next step in 'Benchmark.py'.

157: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Results")`` Here we are updating the caption appropriately to indicate to the user that the previous stage is finished.


158: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.


159: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))`` This line takes the Pygame.surface object 'TitleFont' and draws it onto the window (stored in the variable 'self.Display', at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. The coordinates are (x, y).

160: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))`` HHere we are rendering the Pygame.surface object 'BenchmarkFont' to our display, setting its position (in pixels) to just off centre so it doesn't overlap with the title.


161: ``¬ ¬ ¬ ¬ ¬ ¬ FPSRect = self.mod_Pygame__.Rect(10, 130, realWidth-20, 300)`` here we are creating the background for the graph, this line of code defines the vertexes and position on-screen of that rectangle, and stores the resulting object in the variable 'FPSRect'. The first and second values are fixed, these are the (x,y) coordinates (in pixels) of the top-left corner of the rectangle. The next two values are width and height, in this case we want the rectangle to be the same lenth as the display (-20 pixels to create a border like we mentioned earlier), the height is also fixed at 300 pixels, this makes processing the positions of each point on the line graphs easier.

162: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FPSRect, 0)`` Here we are drawing the rectangle we just defined the dimension for in the variable 'FPSRect' to the display. 'self.Display' is our variable that corresponds to the Pygame window, 'self.ShapeCol' is a tuple of RGB values that control the colour of the rectangle, this is based on the user's currently active theme. '0' defines that the rectangle should be filled.


163: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*60)))), (realWidth-20, int(130+(300-((300/GlobalMax)*60)))))`` Here we are drawing one of the lines that acts as markers to show where a key frame-rate lies, in this case thats 60 FPS (in Hz). We draw it to the display (using the variable that represents that 'self.Display'), set the colour of the line to a suitable colour in the user's selected theme. Then we are defining 2 coordinates (x,y) for the start and end of the line. This function only takes 2 points, the first '(10, int(130+(300-((300/GlobalMax)*60))))' sets the 'x' position to be 10 (pixels), this is the same value as the x position of the shape 'FPSRect' deliberately, both of the 'y' positions are the same, we run the same calculation as earlier, except instead of iterating over an array to get the value, we manually set it to 60. The final 'x' value is the same as the width of the 'FPSRect' shape we defined earlier, again this is deliberate.

164: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SixtyFPSData, (13, int(130+(300-((300/GlobalMax)*60)))))`` Here we are adding a label, which will go just above the line we just defined, this is what tells the user what that line relates to. We loaded the Pygame.surface font earlier into the variable 'SixtyFPSData'. We render this to (with the coordinates as (x,y) in pixels), a fixed 'x' position of 13, and a 'y' position that uses the same calculation as the line before to get the 'y' position.


165: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*144)))), (realWidth-20, int(130+(300-((300/GlobalMax)*144)))))`` Here we are drawing one of the lines that acts as markers to show where a key frame-rate lies, in this case thats 144 FPS (in Hz). We draw it to the display (using the variable that represents that 'self.Display'), set the colour of the line to a suitable colour in the user's selected theme. Then we are defining 2 coordinates (x,y) for the start and end of the line. This function only takes 2 points, the first '(10, int(130+(300-((300/GlobalMax)*144))))' sets the 'x' position to be 10 (pixels), this is the same value as the x position of the shape 'FPSRect' deliberately, both of the 'y' positions are the same, we run the same calculation as earlier, except instead of iterating over an array to get the value, we manually set it to 60. The final 'x' value is the same as the width of the 'FPSRect' shape we defined earlier, again this is deliberate.

166: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(OneFourFourFPSData, (13, int(130+(300-((300/GlobalMax)*140)))))`` Here we are adding a label, which will go just above the line we just defined, this is what tells the user what that line relates to. We loaded the Pygame.surface font earlier into the variable 'OneFourFourFPSData'. We render this to (with the coordinates as (x,y) in pixels), a fixed 'x' position of 13, and a 'y' position that uses the same calculation as the line before to get the 'y' position.


167: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*240)))), (realWidth-20, int(130+(300-((300/GlobalMax)*240)))))`` Here we are drawing one of the lines that acts as markers to show where a key frame-rate lies, in this case thats 240 FPS (in Hz). We draw it to the display (using the variable that represents that 'self.Display'), set the colour of the line to a suitable colour in the user's selected theme. Then we are defining 2 coordinates (x,y) for the start and end of the line. This function only takes 2 points, the first '(10, int(130+(300-((300/GlobalMax)*240))))' sets the 'x' position to be 10 (pixels), this is the same value as the x position of the shape 'FPSRect' deliberately, both of the 'y' positions are the same, we run the same calculation as earlier, except instead of iterating over an array to get the value, we manually set it to 240. The final 'x' value is the same as the width of the 'FPSRect' shape we defined earlier, again this is deliberate.

168: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TwoFortyFPSData, (13, int(130+(300-((300/GlobalMax)*240)))))`` Here we are adding a label, which will go just above the line we just defined, this is what tells the user what that line relates to. We loaded the Pygame.surface font earlier into the variable 'TwoFortyFPSData'. We render this to (with the coordinates as (x,y) in pixels), a fixed 'x' position of 13, and a 'y' position that uses the same calculation as the line before to get the 'y' position.


169: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 255, 0), False, Results1)`` Here we are drawing one of the arrays of points we spent the last stage calculating and formatting, for each of the three lines we set a different RGB value, but the first parameter 'self.Display', which represents the open Pygame window we are rendering to, the boolean value 'False', which represents if the line's start and end points should be connected by a line, and the final parameter will always be the points data for each line (a 2D array with points arrayed by (x,y) in pixels). Please also note the additional 's' at the end of the name of the subroutine, this allows it to plot multiple points, we use the other type before, that only accepts two points.

170: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 0, 255), False, Results2)`` Here we are drawing one of the arrays of points we spent the last stage calculating and formatting, for each of the three lines we set a different RGB value, but the first parameter 'self.Display', which represents the open Pygame window we are rendering to, the boolean value 'False', which represents if the line's start and end points should be connected by a line, and the final parameter will always be the points data for each line (a 2D array with points arrayed by (x,y) in pixels). Please also note the additional 's' at the end of the name of the subroutine, this allows it to plot multiple points, we use the other type before, that only accepts two points.

171: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 0), False, Results3)`` Here we are drawing one of the arrays of points we spent the last stage calculating and formatting, for each of the three lines we set a different RGB value, but the first parameter 'self.Display', which represents the open Pygame window we are rendering to, the boolean value 'False', which represents if the line's start and end points should be connected by a line, and the final parameter will always be the points data for each line (a 2D array with points arrayed by (x,y) in pixels). Please also note the additional 's' at the end of the name of the subroutine, this allows it to plot multiple points, we use the other type before, that only accepts two points.


172: ``¬ ¬ ¬ ¬ ¬ ¬ HideRect = self.mod_Pygame__.Rect(0, 110, realWidth, 330)`` Here we are drawing a border around the line graph, should any points fail to render in the appropriate area, this section should mask any small errors (although there shouldn't be). Here though we are defining the coordinates for this 'mask', we store the resulting output in the variable 'HideRect', we plot the points to start at the edge of the window with the 'x' position as 0, then we set the 'y' position to just above where the graph is rendered, then we make the rectangle span the entire width of the display with the third value of 'realWidth', and set the height of the rectangle to 330, which puts the bottom of the rectangle below the base of the graph. All values for this subroutine are in pixels.

173: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.BackgroundCol, HideRect, 20)`` Now we draw the 'mask' to the display, we start by specifying the display with 'self.Display' as the first parameter, then we set the rectangle's colour to be the same as the background, this hides the rectangle from view, then we add the points we just defined as the fourth parameter, and set a thickness of 20 pixels. Remember, anything rendered after something to the display will cover what was rendered first, so we need to take care here that the rectangle hides any errors in calculations, but doesn't hide the entire graph, which is why we specify a 20 pixel border, meaning the shape isn't entirely filled.


174: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSinfoTEXT, ((realWidth-FPSinfoTEXTWidth)-3, 100))`` Now we blit the sub-heading for this graph, we render the sub-heading on the right hand side of the window, to do this we use the calculation '(realWidth-FPSinfoEXTWidth)-3', where all values are in pixels. The 'y' value is manually set as 100.

175: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FILEinfoTEXT, ((realWidth-FILEinfoTEXTWidth)-3, 430))`` Now we blit the sub-heading for the disk read test, we use the same formula as before, but with different values to render the text on the right, we manually set the 'y' position to 430, which is below the graph.


176: ``¬ ¬ ¬ ¬ ¬ ¬ FileResults = DataFont.render(f"Your device achieved a score of: {round(ReadSpeed, 2)}/100 ({round((100/100)*ReadSpeed)}%)", self.aa, self.FontCol)`` Now we are taking the results of the disk read test and telling the user how they performed against a base (a score easily achievable on most devices, this may one day be made more scientific, and also display a message if disk performance is low.) This is outputted as both a score out of 100, and as a percentage. We render this with the user's preference on anti-aliasing and use the user's choice of colour from the theme they have selected. The resulting Pygame.surface object is stored in the variable 'FileResults'.

177: ``¬ ¬ ¬ ¬ ¬ ¬ FileResultsWidth = FileResults.get_width()`` Here we are getting the width of the Pygame.surface object (in pixels), which we will need to render the text on the right hand side of the display.

178: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FileResults, ((realWidth-FileResultsWidth)-3, 460))`` Here we are rendering the text we just converted into a Pygame.surface object, we use the same formula as with the other rendering, setting the 'x' position to be on the right, and the 'y' position manually to 460. We blit each Pygame.surface object roughly in order as we go down the display.


179: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(HARDWAREinfoTEXT, ((realWidth-HARDWAREinfoTEXTwidth)-3, 480))`` Here we are rendering the sub-title for the system information section of the benchmark on the results page. We render this to the right hand side of the GUI, and manually set the 'y' position to 480 (pixels).