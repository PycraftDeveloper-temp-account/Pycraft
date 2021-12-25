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


6: ``¬ ¬ def Achievements(self):`` This line defines the Achievements class, this is where all achievements you have earned in-game will be displayed. You access this from the home screen and at present does very little, as there isn't much in game to do, and no achievements to earn. This procedure will be getting an update before Pycraft v0.11. This takes, as most subroutines only takes the variable 'self' which is defined in 'main.py'.

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

19: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()`` Gets the width and height of the current Pygame window (in pixels), this is used in working out where everything should be scaled in-game if the window is resized.


20: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:`` Detects if the window has been made smaller than the minimum width, 1280 pixels

21: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)`` If the window is smaller than 1280 pixels, then reset the display's WIDTH to 1280. There is no limit to how large the display can be.

22: ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:`` Detects if the window has been made smaller than the minimum height, 720 pixels

23: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)`` If the window is smaller than 720 pixels, then reset the display's HEIGHT to 720. There is no limit to how large the display can be.


24: ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()`` Gets the current window frame-rate (in Hz)

25: ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS`` Adds the current framerate to a variable which is used to calculate the mean average FPS in game (in Hz)

26: ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1`` Used as frequency in calculating the mean average FPS (in Hz)


27: ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)`` This line of code is used to control what happens when the display is minimised, for more information, see the documentation for this subroutine. This subroutine will return an integer, this is stored in the variable 'tempFPS', which is used to set the windows FPS (in Hz).


28: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, here we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

29: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):`` This controls when the display should close (if on the 'ome-Screen') or returning back to the previous window (typically the 'ome-Screen'), to do this you can press the 'x' at the top of the display, or by pressing 'ESC or ESCAPE' which is handy when in full-screen modes.

30: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:`` This if-statement controls if sound should be played or not based on the user's preference in 'Settings.py', the user's preference is stored when the program closes.

31: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)`` This line calls the subroutine; 'PlayClickSound' in 'SoundUtils.py', if the user has allowed sound to play in settings, then interacting with the display will cause the click sound to play; volume and other parameters for this subroutine are stored in the global variable 'self'.

32: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.

33: ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:`` This line detects if any key is pressed on a keyboard, used when detecting events like pressing keys to navigate the GUIs or moving in-game.

34: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:`` This line of code is used as part of the activation for 'Devmode' which you activate by pressing SPACE 10 times. Here we are detecting is the SPACE key has been pressed and 'Devmode' is not already active.

35: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1`` This line increases the value of the variable 'Devmode' by 1. When the variable 'Devmode' is equal to 0, then 'Devmode' is activated.

36: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:`` Detects if the key 'q' is pressed (not case sensitive).

37: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)`` If the key 'q' is pressed, then we load up the secondary window in 'TkinterUtils.py', this, like 'Devmode' displays information about the running program. This feature may be deprecated at a later date, but this isn't clear yet. All the data the subroutine needs to access is sent through the parameter 'self' which is a global variable.

38: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:`` This line detects if the function key 'F11' has been pressed.

39: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)`` If the function key 'F11' has been pressed, then resize the display by toggling full-screen. (The 'F11' key is commonly assigned to this in other applications).

40: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:`` Detects if the key 'x' is pressed (NOT case sensitive).

41: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1`` This resets 'Devmode' to 1, turning the feature off. This can be used to cancel counting the number of spaces pressed too.


42: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")`` This calls the 'GetNormalCaption' subroutine in 'CaptionUtils.py', This tool takes values from the variable 'self', which stores lots of the global variables stored in the entire program, and also a second input which, in this case its "Achievements" is asked for, this is useful for allowing the user to know what GUI they are in. The variable 'self' is called when the player has activated 'Devmode', (by pressing SPACE 10 times), this brings up lots of details in the caption regarding what the program is doing and the resources its using.


43: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.


44: ``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)`` This line defines the dimensions of a rectangle in Pygame, in this case the rectangle will be drawn at (0, 0) (x, y) with a width of 1280 and a height of 90. (all values here are in pixels and (0, 0) (x, y) is the top-left corner of the GUI (so thats 90 pixels DOWN)).

45: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)`` This line draws a rectangle to the display with 'self.Display', the colour to fill the rectangle is the colour of the background to Pycraft (This is a setting the user can change in the GUI in 'Settings.py') with the dimensions of the previously created Pygame Rect object called; 'cover_Rect'.

46: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))`` This line takes the Pygame.surface object 'TitleFont' and draws it onto the window (stored in the variable 'self.Display', at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. The coordinates are (x, y).

47: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))`` This line takes the Pygame.surface object 'AchievementsFont' and draws it onto the window (stored in the variable 'self.Display'), at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. We also add an offset of 55 pixels to make sure the two titles don't overlap.


48: ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)`` This line calls the subroutine 'CreateDevmodeGraph', this subroutine is responsible for drawing the graph you see at the top-right of most Pycraft GUI's. It takes the variable 'self' as a parameter, this code will return any errors, which are stored in the variable 'Message'. If there are no errors then the subroutine will return 'None'. The second parameter 'DataFont' is the currently loaded font which is used for rendering the text at the top of the graph.

49: ``¬ ¬ ¬ ¬ ¬ if not Message == None:`` This line detects if there are any errors stored in the variable 'Message'. All important errors are stored in this variable. This error detection may be moved to a thread at a later date.

50: ``¬ ¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

51: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

52: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)`` This line of code controls how fast the GUI should refresh, defaulting to the user's preference unless the window is minimised, in which case its set to 15 FPS. All values for FPS are in (Hz) and this line of code specifies the maximum FPS of the window, but this does not guarantee that FPS.

53: ``¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

54: ``¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.



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


4: ``¬ import moderngl_window as mglw`` Here we are importing the external module 'ModernGL_Window'. All calls to the module furthermore in this module will reference 'mglw'.

5: ``¬ from moderngl_window.scene.camera import KeyboardCamera, OrbitCamera`` Here we are importing specific classes and code from the module 'ModernGL_Window'. We do this because they may not be added by default when importing that external module as a whole.



6: ``¬ class CameraWindow(mglw.WindowConfig):`` Here we are creating a class called 'CameraWindow', we will reference this later on in the 'GameEngine.py', this class controls the basic window functionality of 'GameEngine.py'.

7: ``¬ ¬ """Base class with built in 3D camera support"""`` 


8: ``¬ ¬ def __init__(self, **kwargs):`` Here we are initialising the class by defining and assigning some key variables which will be used frequently in all ModernGL enabled windows.

9: ``¬ ¬ ¬ super().__init__(**kwargs)`` 

10: ``¬ ¬ ¬ self.camera = KeyboardCamera(self.wnd.keys, aspect_ratio=self.wnd.aspect_ratio)`` Here we setting the global variable self.camera to a specific ModernGL object, its important to note, references to 'self' in this module do not relate to the 'self' variable used in other programs. This line of code creates a camera object (which we use to move around and rotate in 'GameEngine.py'). This line of code also detects keypresses in ModernGL_window enabled GUI's ('GameEngine.py' mainly) and sets the aspect ratio. This setting is specified in 'GameEngine.py'.

11: ``¬ ¬ ¬ self.camera_enabled = True`` This line confirms that we are using the camera as our main view in 'GameEngine.py'.


12: ``¬ ¬ def key_event(self, key, action, modifiers):`` This line of code defines a subroutine that detects keypresses on Moderngl enabled GUIs. This acts similarly to 'pygame.event.get()'.

13: ``¬ ¬ ¬ keys = self.wnd.keys`` This line of code gets a list of the keys that are on a typical keyboard as well as their 'state', essentially this means if the key is pressed or not.


14: ``¬ ¬ ¬ if self.camera_enabled:`` This line controls wether to accept keyboard inputs or not from the camera.

15: ``¬ ¬ ¬ ¬ self.camera.key_input(key, action, modifiers)`` This line of code gets the keyboard inputs from the camera. Its here where the state of each key specified in the variable 'keys'.


16: ``¬ ¬ ¬ if action == keys.ACTION_PRESS:`` This line detects if a key is pressed (essentially 'event.type == pygame.KEYDOWN' for Pygame)

17: ``¬ ¬ ¬ ¬ if key == keys.C:`` This if-statement controls what to do if the 'C' key is pressed down.

18: ``¬ ¬ ¬ ¬ ¬ self.camera_enabled = not self.camera_enabled`` This line toggles if the camera is enabled or not, and thus where to get events from.

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


30: ``¬ ¬ def __init__(self, **kwargs):`` Here we are initialising the class by defining and assigning some key variables which will be used frequently in all ModernGL enabled windows.

31: ``¬ ¬ ¬ super().__init__(**kwargs)`` 

32: ``¬ ¬ ¬ self.camera = OrbitCamera(aspect_ratio=self.wnd.aspect_ratio)`` Sets the camera to a different camera object from before. In this case we still take the same parameters for the aspect ratio of the camera, but negate 'self.wnd.keys' this time. This can be imagined as like setting the aspect ratio on the camera of a phone.

33: ``¬ ¬ ¬ self.camera_enabled = True`` This line confirms that we are using the camera as our main view in 'GameEngine.py'.


34: ``¬ ¬ def key_event(self, key, action, modifiers):`` This line of code defines a subroutine that detects keypresses on Moderngl enabled GUIs. This acts similarly to 'pygame.event.get()'.

35: ``¬ ¬ ¬ keys = self.wnd.keys`` This line of code gets a list of the keys that are on a typical keyboard as well as their 'state', essentially this means if the key is pressed or not.


36: ``¬ ¬ ¬ if action == keys.ACTION_PRESS:`` This line detects if a key is pressed (essentially 'event.type == pygame.KEYDOWN' for Pygame)

37: ``¬ ¬ ¬ ¬ if key == keys.C:`` This if-statement controls what to do if the 'C' key is pressed down.

38: ``¬ ¬ ¬ ¬ ¬ self.camera_enabled = not self.camera_enabled`` This line toggles if the camera is enabled or not, and thus where to get events from.

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

11: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark")`` Here we update the cation of the window from the previous caption to this. The variable 'self.version' is defined at the start of the program in 'main.py'.

12: ``¬ ¬ ¬ ¬ self.VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Here we load the project's default from from the fonts folder (it's 'Book Antiqua'), we store this in the variable 'self.VersionFont'. We set the font's size here to 20

13: ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 60.

14: ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 35.

15: ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 15.

16: ``¬ ¬ ¬ ¬ DetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)`` Here we load the project's default from from the fonts folder (it's 'Book Antiqua'), we store this in the variable 'DetailsFont'. We also set it's size to 20.

17: ``¬ ¬ ¬ ¬ InfoDetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Here we load the project's default from from the fonts folder (it's 'Book Antiqua'), we store this in the variable 'InfoDetailsFont'. We also set it's size to 15.

18: ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)`` Takes the font, which we stored in the variable 'MainTitleFont' and uses it to render the text "Pycraft", with the user's preference on anti-aliasing, 'aa' and the colour defined in 'ThemeUtils.py', the resulting Pygame.surface object is stored in the variable 'TitleFont'.

19: ``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()`` Gets the width (in pixels) of the Pygame.surface object 'TitleFont


20: ``¬ ¬ ¬ ¬ BenchmarkFont = InfoTitleFont.render("Benchmark", self.aa, self.SecondFontCol)`` Here we are creating a Pygame.surface object with the text 'Benchmark', we also set the anti-aliasing to the user's preference (which can be changed in settings), and set the font's colour to the secondary font colour, defined in 'ThemeUtils.py'. We store the Pygame.surface object in the variable 'BenchmarkFont'.

21: ``¬ ¬ ¬ ¬ FPSinfoTEXT = DetailsFont.render("FPS benchmark results", self.aa, self.FontCol)`` Here we are creating a Pygame.surface object using the font 'DetailsFont', which we loaded earlier. We render the text 'FPS benchmark results' to this, setting anti-aliasing to the user's preference (defined in 'Settings.py') and setting the colour to the primary font colour defined in 'ThemeUtils.py', which can be changed by the user.

22: ``¬ ¬ ¬ ¬ FPSinfoTEXTWidth = FPSinfoTEXT.get_width()`` On this line we get the width (in pixels) of the Pygame.surface object FPSinfoTEXT. We store the resulting number in the variable 'FPSintoTEXTWidth'.

23: ``¬ ¬ ¬ ¬ FILEinfoTEXT = DetailsFont.render("Read test results", self.aa, self.FontCol)`` Here we are rendering the text 'Read test results' with the font 'DetailsFont', which we loaded earlier. As with most font rendering we also set the anti-aliasing to the user's preference (which can be changed in settings), and the colour to the colour argument in the variable 'FILEinfoTEXT'

24: ``¬ ¬ ¬ ¬ FILEinfoTEXTWidth = FILEinfoTEXT.get_width()`` Here we are getting the length (in pixels) of the Pygame.surface object 'FILEinfoTEXT', this will be used to calculate where to place the text on the window.

25: ``¬ ¬ ¬ ¬ HARDWAREinfoTEXT = DetailsFont.render("Hardware results", self.aa, self.FontCol)`` Here we are rendering the text 'Hardware results' using the font we loaded earlier; 'DetailsFont'. We also use the user's preference in anti-aliasing and use the appropriate colour scheme from the theme the user has selected. We store this in the variable 'HARDWAREinfoTEXT'.

26: ``¬ ¬ ¬ ¬ HARDWAREinfoTEXTwidth = HARDWAREinfoTEXT.get_width()`` Here we are getting the width (in pixels) of the Pygame.surface object HARDWAREinfoTEXT. This is used in making sure the text is drawn to the window in the appropriate position.


27: ``¬ ¬ ¬ ¬ SixtyFPSData = DataFont.render("60 Hz", self.aa, self.AccentCol)`` Here we are rendering the text '60 Hz' using the font 'DataFont', and the suer's preference on anti-aliasing (which is defined in 'Settings.py') and the appropriate colour from the user's selected theme. This is stored in the variable 'SixtyFPSData', this acts as a marker on the graph of where 60 FPS lies (FPS is measured in Hz).

28: ``¬ ¬ ¬ ¬ OneFourFourFPSData = DataFont.render("144 Hz", self.aa, self.AccentCol)`` Here we are rendering the text '144 Hz' using the font 'DataFont', and the user's preference on anti-aliasing (which is defined in 'Settings.py') and the appropriate colour from the user's selected theme. This is stored in the variable 'OneFourFourFPSData', this acts as a marker on the graph of where 144 FPS lies (FPS is measured in Hz).

29: ``¬ ¬ ¬ ¬ TwoFortyFPSData = DataFont.render("240 Hz", self.aa, self.AccentCol)`` Here we are rendering the text '240 Hz' using the font 'DataFont', and the user's preference on anti-aliasing (which is defined in 'Settings.py') and the appropriate colour from the user's selected theme. This is stored in the variable 'TwoFortyFPSData', this acts as a marker on the graph of where 240 FPS lies (FPS is measured in Hz).


30: ``¬ ¬ ¬ ¬ InfoFont1 = DataFont.render("Welcome to Benchmark mode, press the SPACE bar to continue or press ANY other key to cancel, or press 'X'", self.aa, self.FontCol)`` Here we are giving the user instructions on how to use benchmark mode, telling them they can cancel the benchmark at any time by pressing any key. We store the resulting Pygame.surface output from this function in the variable 'InfoFont1'. In addition we use the user's choice on anti-aliasing and choose an appropriate colour from the user's selected theme.

31: ``¬ ¬ ¬ ¬ InfoFont2 = DataFont.render("Benchmark mode is used to make the 'ADAPTIVE' feature in settings function and also to give an indication of the experience you are likely to get on this device", self.aa, self.FontCol)`` Here we are giving the user details on what the benchmark mode can be used for, we render this text with the user's preference on anti-aliasing and choose a suitable colour from their theme. We store the output from this in 'InfoFont2'.

32: ``¬ ¬ ¬ ¬ InfoFont3 = DataFont.render("Benchmark mode consists of several stages:", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. This is given over several lines as Pygame doesn't wrap text to the edge of the window, which is one reason why the user cannot use a resolution lower than (1280x720), because in some cases text would be rendered off the screen. We will always respect the user's colour scene and anti-aliasing preferences here.

33: ``¬ ¬ ¬ ¬ InfoFont4 = DataFont.render("First it will gather some basic information about your system", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences here.

34: ``¬ ¬ ¬ ¬ InfoFont5 = DataFont.render("Then it will test your maximum frame rate on a blank screen, then with a basic animation, and finally in a 3D OpenGL space", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences here.

35: ``¬ ¬ ¬ ¬ InfoFont6 = DataFont.render("After its done that the focus moves on to a quick storage test, before finishing", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences here.

36: ``¬ ¬ ¬ ¬ InfoFont7 = DataFont.render("Your results will then be displayed on screen with your frame rate scores on a line graph and the rest detailed to the right", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences here.

37: ``¬ ¬ ¬ ¬ InfoFont8 = DataFont.render("During the time the benchmark is running the window may appear unresponsive, don't panic this can be expected.", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences here.

38: ``¬ ¬ ¬ ¬ InfoFont9 = DataFont.render("In addition to achieve the best scores try to avoid doing anything else on the computer whilst the benchmark runs", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preference's here.

39: ``¬ ¬ ¬ ¬ InfoFont10 = DataFont.render("This benchmark may show some system instability or cause your device to get warm, you use this at your own risk!", self.aa, (255, 0, 0))`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences here.


40: ``¬ ¬ ¬ ¬ stage = 0`` Here we are setting the user's 'stage', this essentially tells controls which step of the process should be processed and rendered. With the completion of each 'stage', it is incremented by 1.


41: ``¬ ¬ ¬ ¬ resize = False`` This prevents the display from being resized during the tests, as resizing the display can alter the results, and when in full-screen, Pygame does some hardware acceleration to further improve performance, so you could get contrasting results.


42: ``¬ ¬ ¬ ¬ while True:`` Enters the project's game loop

43: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()`` Gets the width and height of the current Pygame window (in pixels), this is used in working out where everything should be scaled in-game if the window is resized.


44: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:`` Detects if the window has been made smaller than the minimum width, 1280 pixels

45: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)`` If the window is smaller than 1280 pixels, then reset the display's WIDTH to 1280. There is no limit to how large the display can be.

46: ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:`` Detects if the window has been made smaller than the minimum height, 720 pixels

47: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)`` If the window is smaller than 720 pixels, then reset the display's HEIGHT to 720. There is no limit to how large the display can be.


48: ``¬ ¬ ¬ ¬ ¬ if stage == 0:`` Here we are starting the benchmark process by checking to see if the value of 'stage' is 0, if it is then we run the code allocated to that section.

49: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

50: ``¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)`` This line defines the dimensions of a rectangle in Pygame, in this case the rectangle will be drawn at (0, 0) (x, y) with a width of 1280 and a height of 90. (all values here are in pixels and (0, 0) (x, y) is the top-left corner of the GUI (so thats 90 pixels DOWN)).

51: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)`` This line draws a rectangle to the display with 'self.Display', the colour to fill the rectangle is the colour of the background to Pycraft (This is a setting the user can change in the GUI in 'Settings.py') with the dimensions of the previously created Pygame Rect object called; 'cover_Rect'.

52: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))`` This line takes the Pygame.surface object 'TitleFont' and draws it onto the window (stored in the variable 'self.Display', at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. The coordinates are (x, y).

53: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))`` Here we are rendering the Pygame.surface object 'BenchmarkFont' to our display, setting its position (in pixels) to just off centre so it doesn't overlap with the title.

54: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont1, (3, 100))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.

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

67: ``¬ ¬ ¬ ¬ ¬ ¬ RAMid = f"{round((((self.mod_Psutil__.virtual_memory().total)/1000)/1000/1000),2)} GB of memory, with {self.mod_Psutil__.virtual_memory().percent}% used"`` Here we are getting the details of the user's RAM, and formatting it appropriately so this can be rendered to text later on without additional processing. 'self.mod_Psutil__.virtual_memory().total' gets the amount of physical memory installed in your machine that the program can access (This does NOT include hardware reserved memory), we are also converting this output from bytes to gigabytes, or this would be a really big number and not very readable. 'self.mod_Psutil__.virtual_memory().percent' returns the amount of memory allocated to other tasks on the system.

68: ``¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFO = DataFont.render(CPUid, self.aa, (255, 255, 255))`` Here we are converting the variable 'CPUid', which is a string, into a Pygame.surface object, respecting the user's preference on anti-aliasing, but forcing the colour to white (which is a bug, this will be fixed in Pygame v0.9.4). The resulting Pygame.surface object is stored in the variable 'CPUhwINFO', which is abbreviated from 'CPU-hardware-information'.

69: ``¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFOwidth = CPUhwINFO.get_width()`` Here we are getting the width (in pixels) of the Pygame.surface object; 'CPUhwINFO'. This will be used to help appropriately place the text later on.


70: ``¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFO = DataFont.render(RAMid, self.aa, (255, 255, 255))`` Here we are rendering the system information we gathered for RAM, rendering the formatted tet respecting the user's preference on anti-aliasing and setting the colour to white (this is a bug, this will be fixed in the next update to Pycraft).

71: ``¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFOwidth = RAMhwINFO.get_width()`` Here we are getting the width (in pixels) of the Pygame.surface object we have just created; 'RAMhwINFO'.

72: ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1`` Now we are finished with the current stage so increment the stage variable by 1, and more on forwards to the next stage.


73: ``¬ ¬ ¬ ¬ ¬ if stage == 2:`` Here we are detecting if the integer stored in the variable 'stage' is equal to 2, in which case we do this stage.

74: ``¬ ¬ ¬ ¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

75: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Message, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3 = self.mod_ExBenchmark__.LoadBenchmark.run(self)`` Here we are running a benchmark in 'ExBenchmark' (short for 'ExternalBenchmark'), and once this has completed, receiving the results of the subroutine through the 7 variables. This subroutine takes only the global variable self, and outputs 7 pieces of data, if completed successfully. 'Message' is a string, this stores any errors that may occur when running the subroutine. 'FPSlistX', 'FPSlistX2' and 'FPSlistx3' each store the 'x' coordinate for the graph, which we will draw later. Each of these lists contains a sequence of numbers, going up in 1's for the framerate of each frame of the benchmark. 'FPSlistY', 'FPSlistY1' and 'FPSlistY2' store the results of each of the three benchmarks running, 'FPSlistY' stores the blank window test, 'FPSlistY2' stores the result of the 2D graphics test, and 'FPSlistY3' stores the 3D render results.

76: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:`` This line detects if there are any errors stored in the variable 'Message'. All important errors are stored in this variable. This error detection may be moved to a thread at a later date.

77: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

78: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)`` Here we are creating our Pygame display through the subroutine 'SetDisplay' in 'DisplayUtils.py'. All the parameters for this subroutine are sent through the variable 'self'.

79: ``¬ ¬ ¬ ¬ ¬ ¬ except:`` (This needs updating to follow the guidelines of the documentation) This ignores any errors that may occur when running the main section of the benchmark, or in creating our Pygame window.

80: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Cancelled benchmark")`` If an error does occur, then here we set the caption appropriately to let the user know the benchmark has been cancelled.

81: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.

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

136: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY[i])))`` ow we are iterating over each element in the black render test (which has the results stored in the variable 'FPSlistY'), we are taking the original value and converting it to a smaller value that is still representative, and will look the same on the graph, but will fit onto the area we have assigned the graphing to be. Not doing this step could result in the line graphs not fitting on-screen and being rendered upside-down. In order of processing; we divide 300 (the HEIGHT of the graphing area) by the 'GlobalMax', which stores the largest number that appears in all of the tests, this makes sure that none of the values are rendered outside of the graph. Then we multiply this by the current value of 'FPSlistY' as we iterate over the array. Then we take the result and flip it by taking it away from 300, this step is done because the larger the value the lower down the display it would have been drawn, mirroring the result, and making it really hard to interpret. Finally we offset the entire result by moving it down the display 130 pixels to allow for titles and subheadings above.

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

160: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))`` Here we are rendering the Pygame.surface object 'BenchmarkFont' to our display, setting its position (in pixels) to just off centre so it doesn't overlap with the title.


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


180: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CPUhwINFO, ((realWidth-CPUhwINFOwidth)-3, 500))`` Here we are rendering the data we received right at the start of the benchmark process about the user's system info. This section will be based on their CPU information, which we formatted into an appropriate string beforehand. We render this too on the right, using the same equation (-3 moves the last pixels of the text off the end of the GUI, which can cause readability issues, this aims to solve that). Again we manually set the 'y' position down the display, in this case to 500.

181: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(RAMhwINFO, ((realWidth-RAMhwINFOwidth)-3, 516))`` Here we are taking the Pygame.surface object which we created earlier, this Pygame.surface object contains all the information relevant to the user on the benchmark results page, we render this below the CPU info with a 'y' position of 516 pixels. The 'x' position is determined automatically by using calculating the appropriate position on the right hand side.


182: ``¬ ¬ ¬ ¬ ¬ ¬ GreenInfo = InfoDetailsFont.render(f"Blank screen test (green); Minimum: {round(Min1, 4)} FPS, Maximum: {round(Max1, 4)} FPS", self.aa, self.FontCol)`` Here we are rendering details of what each of the lines on the line graph represents, as well as the minimum and maximum values for each, this is useful if the user is only interested in one of the tests. This text here is rendered using the font we loaded earlier and stored in the 'InfoDetailsFont', we respect the user's preference on anti-aliasing here, and use an appropriate colour from the user's currently active theme. This subroutine will return a Pygame.surface object, which we will blit to the display later.

183: ``¬ ¬ ¬ ¬ ¬ ¬ BlueInfo = InfoDetailsFont.render(f"Drawing test (blue); Minimum: {round(Min2, 4)} FPS, Maximum: {round(Max2, 4)} FPS", self.aa, self.FontCol)`` Here we are rendering details of what each of the lines on the line graph represents, as well as the minimum and maximum values for each, this is useful if the user is only interested in one of the tests. This text here is rendered using the font we loaded earlier and stored in the 'InfoDetailsFont', we respect the user's preference on anti-aliasing here, and use an appropriate colour from the user's currently active theme. This subroutine will return a Pygame.surface object, which we will blit to the display later.

184: ``¬ ¬ ¬ ¬ ¬ ¬ RedInfo = InfoDetailsFont.render(f"OpenGL test (red); Minimum: {round(Min3, 4)} FPS, Maximum: {round(Max3, 4)} FPS", self.aa, self.FontCol)`` Here we are rendering details of what each of the lines on the line graph represents, as well as the minimum and maximum values for each, this is useful if the user is only interested in one of the tests. This text here is rendered using the font we loaded earlier and stored in the 'InfoDetailsFont', we respect the user's preference on anti-aliasing here, and use an appropriate colour from the user's currently active theme. This subroutine will return a Pygame.surface object, which we will blit to the display later.

185: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(GreenInfo, (3, 430))`` Now we go through and blit each of the Pygame.surface objects we just created to the display, each of the lines will have manually set coordinates, as they aren't affected by the display resizing. These are rendered below the graph on the left hand side of the GUI. 

186: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BlueInfo, (3, 445))`` Now we go through and blit each of the Pygame.surface objects we just created to the display, each of the lines will have manually set coordinates, as they aren't affected by the display resizing. These are rendered below the graph on the left hand side of the GUI. 

187: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(RedInfo, (3, 460))`` Now we go through and blit each of the Pygame.surface objects we just created to the display, each of the lines will have manually set coordinates, as they aren't affected by the display resizing. These are rendered below the graph on the left hand side of the GUI. 


188: ``¬ ¬ ¬ ¬ ¬ ¬ if resize == True:`` Now we check to see if, since the last run the display was resized, which we will detect later on (for the next iteration of the GUI), and if the display has been resized, we need to go back to the previous stage again and recalculate every single coordinate. If we didn't do this then the contents of the display wouldn't fill the display, so viewing the output on a large window could be difficult.

189: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ stage = 4`` If the display has been resized, we need to go back to the previous stage.

190: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ resize = False`` This prevents the display from being resized during the tests, as resizing the display can alter the results, and when in full-screen, Pygame does some hardware acceleration to further improve performance, so you could get contrasting results.


191: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, here we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

192: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE) and stage <= 3) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):`` Here we are detecting if the user has either pressed the 'x' in the top corner of the GUI (left for MacOS, right for Windows), or has pressed any key that isn't SPACE and the stage is less than or equal to 3, this is important, as if the user wants to cancel or leave the benchmark, then they can do this at any stage by pressing any key, as is mentioned in the instructions at the start, but then we may not want to close the GUI with any key afterwards, because if the user presses any key on the results screen, they would need to re-run the test again, even if they used a keyboard shortcut to say; take a screenshot. We also detect here of the user has pressed the ESCAPE (or ESC)key, which is commonly used as another method of exiting the GUI.

193: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:`` This if-statement controls if sound should be played or not based on the user's preference in 'Settings.py', the user's preference is stored when the program closes.

194: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)`` This line calls the subroutine; 'PlayClickSound' in 'SoundUtils.py', if the user has allowed sound to play in settings, then interacting with the display will cause the click sound to play; volume and other parameters for this subroutine are stored in the global variable 'self'.

195: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.

196: ``¬ ¬ ¬ ¬ ¬ ¬ if (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_SPACE) and stage == 0:`` This if-statement detects if the user has pressed SPACE and the current stage is '0', which is the stage with the instructions on, this is important as the only way to continue with the benchmark is by pressing SPACE.

197: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ stage += 1`` Now we are finished with the current stage so increment the stage variable by 1, and more on forwards to the next stage.

198: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.VIDEORESIZE:`` Now we are detecting if the display has resized, if the display has been resized (even if that's to full-screen) then it sets the value of the variable 'resize' to boolean 'True', this triggers the if-statement earlier on on the next iteration of the display if the user is on the last stage to refresh it with new values. 

199: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ resize = True`` We set the variable 'resize' to boolean 'True', as the display has been resized and we need to therefore recalculate all of the points for the line graph, and move all of the size affected text too.


200: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

201: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)`` Here we are setting the refresh rate (in Hz) of the display, this is used for preventing the GUI from running really fast, causing unnecessary strain on the CPU and GPU, and also allowing us to detect the display's frame-rate (which may not be exactly the value of 'self.FPS').

202: ``¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

203: ``¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.



.. note::
   For information on this consult the above guide

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


6: ``¬ ¬ def GetLoadingCaption(self, num):`` Here we are creating a subroutine called 'GetLoadingCaption', which takes the variables 'self' and 'num', this subroutine does not return anything. This subroutine is used in the 'PycraftStartupTest' module and updates the caption regularly so that it shows the code is running still. This feature isn't very noticeable unless your running a low powered device.

7: ``¬ ¬ ¬ if num == 0:`` Here we are checking if the second parameter this subroutine takes -'num'- is equal to 0. The variable 'num' can be any number between 0 and 3 (inclusive) and this controls which caption to load. If 'num' is not in the appropriate range, then we don't display the loading animation (There is a little line animation).

8: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (-)")`` Here we are loading the first stage of the animation; setting the caption's end to (-).

9: ``¬ ¬ ¬ elif num == 1:`` Now we check to see if the value of 'num' is one, only if the previous if-statement returns False, if 'num' was 0 on the last call, it should be 1 this time around to make the animation work.

10: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (\)")`` If 'num' is equal to 1, then we display the next frame of the animation, changing the last few characters to (\) instead.

11: ``¬ ¬ ¬ elif num == 2:`` Here we are checking if the value of 'num' is equal to 2, this should be if the previous value was 1, 'num' controls which frame of the animation to show in the caption.

12: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (|)")`` If 'num' is equal to 2, then we display the third frame of the animation; (|).

13: ``¬ ¬ ¬ elif num == 3:`` This is the final frame of the animation; these if-statements should have been called in order for the animation to work. Here we are checking to see if the value of 'num' is 3.

14: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (/)")`` We render the last frame of the 4 step animation, this is designed to look like the line in the brackets is spinning, in order from frame 0 to 4: (-) (\) (|) (/). This is designed to look like the animation you sometimes see in a CLI (Command Line Interface).

15: ``¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

16: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading")`` Here we simply set the caption to 'Pycraft: v<INSERT VERSION ID ERE>: Loading, this is useful if we dont want to enter a value for num, for example if the code isn't called in a sequence then we can do this instead. It is good practice in Pycraft to suitably update the caption when something happens, either on-screen or behind the scenes. 

17: ``¬ ¬ ¬ self.mod_Pygame__.display.update()`` Here we are forcing the display to update, this refreshes the entire frame. This is where the objects we either 'blit' or 'draw' to the display are made visible. This should be called only once per frame to avoid confusion and 'Pygame.display.flip()' is usually preferred, because of the greater amount of options and better performance.


18: ``¬ ¬ def GetNormalCaption(self, location):`` Here we are creating the subroutine that should be in control of all other caption loading, except for in special situations. This subroutine returns nothing but takes 2 parameters; 'self' which stores a lot of the most commonly occurring data in the program, and 'location', which is of the string data type; this is what stores the user's location. This should be the same as any sub-heading in Pycraft's GUI to avoid confusion.

19: ``¬ ¬ ¬ if self.Devmode >= 5 and self.Devmode <= 9:`` Here we are checking to see if the value of 'Devmode' is between 5 and 9 (inclusive). If 'Devmode' is between those two values then we should suitably tell the user that they are activating that.

20: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | you are: {10-self.Devmode} steps away from being a developer")`` Here we suitably update the caption to tell the user that they are entering Devmode, we also render the user's 'location' and 'self.version'. We invert the value of 'self.Devmode', by taking it away from 10, this way it counts down.

21: ``¬ ¬ ¬ elif self.Devmode == 10:`` If the user has activated 'Devmode', in which case 'self.Devmode' will be equal to 10...

22: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | Developer Mode | Pos: {round(self.X, 2)}, {round(self.Y, 2)}, {round(self.Z, 2)} | V: {self.Total_move_x}, {self.Total_move_y}, {self.Total_move_z} FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: {int(self.aFPS/self.Iteration)} Iteration: {self.Iteration} | MemUsE: {self.mod_Psutil__.virtual_memory().percent} | CPUUsE: {self.mod_Psutil__.cpu_percent()} | Theme: {self.theme} | Thread Count: {self.mod_Threading__.active_count()}")`` Here we are rendering information about the currently running program the user. This is a handy tool for finding bugs and issues. In order of occupance: First we render the user's position from the game-engine, we round the coordinates to 2 decimal places as they can contain long decimals that lead to the caption being longer than the display. This feature doesn't currently work in the new game-engine, but will be brought back in Pycraft v0.9.4. Secondly we render the user's velocity, again this is especially useful in game, this tells the user how much they are moving in a given direction (m/s in the new game-engine (Pycraft v0.9.3 onwards)) Which is a useful feature to see if collisions is working. Then we move on-to showing the user the current maximum FPS, currently running FPS, average FPS and the number samples taken for the average. All values for FPS are measured in z and are rounded to the nearest integer. Then we render the amount of memory currently being used by the system as a whole, as well as the utilisation on the CPU (These are both given as percentages). Then we show the currently active theme. Finally we show the amount of threads the program is currently using, again a handy debugging feature. ALL METRICS ARE SEPARATED BY A PILLAR (|) AND GROUPED WEN NECESSARY. NEW METRICS SHOULD BE ADDED TO TE END UNLESS TEY SUITABLY FIT INTO A GROUP.

23: ``¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

24: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location}")`` Here we render the caption as normal, this is how the caption should appear most of the time, displaying just the name of the game, version and location (the current menu the user is in).




.. note::
   For information on this consult the above guide

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


6: ``¬ ¬ def CharacterDesigner(self):`` Here we are defining the subroutine that controls the character designer GUI, we name the subroutine 'CharacterDesigner', and it takes only one parameter, 'self'. This gives the subroutine all the necessary data to run. This subroutine only returns an error if one occurs, if there is no errors (which there hopefully shouldn't be), then the subroutine will return nothing.

7: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

8: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

9: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

10: ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")`` Here we are setting the caption of the GUI, we use the subroutine we looked at earlier in 'CaptionUtils.py'. The subroutine is called 'GetNormalCaption', this subroutine allows us to change the caption for our GUI. This subroutine takes 2 arguments, the second one is of importance here; this is the location we enter; this is the same as the subheading for this section of the GUI. 

11: ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 60.

12: ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 35.

13: ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 15.


14: ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.SecondFontCol)`` (There is a bug here; this should be 'self.FontCol' as the last parameter, so the following description will appear differently. This will be fixed in Pycraft v0.9.4) Takes the font, which we stored in the variable 'MainTitleFont' and uses it to render the text \"Pycraft\", with the user's preference on anti-aliasing, 'aa' and the colour defined in 'ThemeUtils.py', the resulting Pygame.surface object is stored in the variable 'TitleFont'.

15: ``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()`` Gets the width (in pixels) of the Pygame.surface object 'TitleFont


16: ``¬ ¬ ¬ ¬ AchievementsFont = InfoTitleFont.render("Character Designer", self.aa, self.FontCol)`` (There is a bug here; this should be 'CharacterDesignerFont' NOT 'AchievementsFont') Here we are taking the font we just loaded into the variable 'InfoTitleFont' and using it to create a Pygame.surface object which we store in the 'CharacterDesignerFont' variable. This Pygame.surface object contains the text 'Character Designer' which is rendered with the user's preference on anti-aliasing, and the user's selected theme. 

17: ``¬ ¬ ¬ ¬ tempFPS = self.FPS`` This is used to temporarily store the game's target FPS, this is used later to slow the game down when minimised.


18: ``¬ ¬ ¬ ¬ while True:`` Enters the project's game loop

19: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()`` Gets the width and height of the current Pygame window (in pixels), this is used in working out where everything should be scaled in-game if the window is resized.


20: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:`` Detects if the window has been made smaller than the minimum width, 1280 pixels

21: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)`` If the window is smaller than 1280 pixels, then reset the display's WIDTH to 1280. There is no limit to how large the display can be.

22: ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:`` Detects if the window has been made smaller than the minimum height, 720 pixels

23: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)`` If the window is smaller than 720 pixels, then reset the display's HEIGHT to 720. There is no limit to how large the display can be.


24: ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()`` Gets the current window frame-rate (in Hz)

25: ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS`` Adds the current framerate to a variable which is used to calculate the mean average FPS in game (in Hz)

26: ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1`` Used as frequency in calculating the mean average FPS (in Hz)


27: ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)`` This line of code is used to control what happens when the display is minimised, for more information, see the documentation for this subroutine. This subroutine will return an integer, this is stored in the variable 'tempFPS', which is used to set the windows FPS (in Hz).


28: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, here we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

29: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):`` This controls when the display should close (if on the 'ome-Screen') or returning back to the previous window (typically the 'ome-Screen'), to do this you can press the 'x' at the top of the display, or by pressing 'ESC or ESCAPE' which is handy when in full-screen modes.

30: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:`` This if-statement controls if sound should be played or not based on the user's preference in 'Settings.py', the user's preference is stored when the program closes.

31: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)`` This line calls the subroutine; 'PlayClickSound' in 'SoundUtils.py', if the user has allowed sound to play in settings, then interacting with the display will cause the click sound to play; volume and other parameters for this subroutine are stored in the global variable 'self'.

32: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.

33: ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:`` This line detects if any key is pressed on a keyboard, used when detecting events like pressing keys to navigate the GUIs or moving in-game.

34: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:`` This line of code is used as part of the activation for 'Devmode' which you activate by pressing SPACE 10 times. Here we are detecting is the SPACE key has been pressed and 'Devmode' is not already active.

35: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1`` This line increases the value of the variable 'Devmode' by 1. When the variable 'Devmode' is equal to 0, then 'Devmode' is activated.

36: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:`` Detects if the key 'q' is pressed (not case sensitive).

37: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)`` If the key 'q' is pressed, then we load up the secondary window in 'TkinterUtils.py', this, like 'Devmode' displays information about the running program. This feature may be deprecated at a later date, but this isn't clear yet. All the data the subroutine needs to access is sent through the parameter 'self' which is a global variable.

38: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:`` This line detects if the function key 'F11' has been pressed.

39: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)`` If the function key 'F11' has been pressed, then resize the display by toggling full-screen. (The 'F11' key is commonly assigned to this in other applications).

40: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:`` Detects if the key 'x' is pressed (NOT case sensitive).

41: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1`` This resets 'Devmode' to 1, turning the feature off. This can be used to cancel counting the number of spaces pressed too.


42: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")`` Here we are setting the caption of the GUI, we use the subroutine we looked at earlier in 'CaptionUtils.py'. The subroutine is called 'GetNormalCaption', this subroutine allows us to change the caption for our GUI. This subroutine takes 2 arguments, the second one is of importance here; this is the location we enter; this is the same as the subheading for this section of the GUI. 


43: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.


44: ``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)`` This line defines the dimensions of a rectangle in Pygame, in this case the rectangle will be drawn at (0, 0) (x, y) with a width of 1280 and a height of 90. (all values here are in pixels and (0, 0) (x, y) is the top-left corner of the GUI (so thats 90 pixels DOWN)).

45: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)`` This line draws a rectangle to the display with 'self.Display', the colour to fill the rectangle is the colour of the background to Pycraft (This is a setting the user can change in the GUI in 'Settings.py') with the dimensions of the previously created Pygame Rect object called; 'cover_Rect'.

46: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))`` This line takes the Pygame.surface object 'TitleFont' and draws it onto the window (stored in the variable 'self.Display', at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. The coordinates are (x, y).

47: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))`` This line takes the Pygame.surface object 'AchievementsFont' and draws it onto the window (stored in the variable 'self.Display'), at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. We also add an offset of 55 pixels to make sure the two titles don't overlap.


48: ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)`` This line calls the subroutine 'CreateDevmodeGraph', this subroutine is responsible for drawing the graph you see at the top-right of most Pycraft GUI's. It takes the variable 'self' as a parameter, this code will return any errors, which are stored in the variable 'Message'. If there are no errors then the subroutine will return 'None'. The second parameter 'DataFont' is the currently loaded font which is used for rendering the text at the top of the graph.

49: ``¬ ¬ ¬ ¬ ¬ if not Message == None:`` This line detects if there are any errors stored in the variable 'Message'. All important errors are stored in this variable. This error detection may be moved to a thread at a later date.

50: ``¬ ¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

51: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

52: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)`` This line of code controls how fast the GUI should refresh, defaulting to the user's preference unless the window is minimised, in which case its set to 15 FPS. All values for FPS are in (Hz) and this line of code specifies the maximum FPS of the window, but this does not guarantee that FPS.

53: ``¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

54: ``¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.



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

        2: ``print("Started <Pycraft_Credits>")``

        3: ``¬ class GenerateCredits:``

        4: ``¬ ¬ def __init__(self):``

        5: ``¬ ¬ ¬ pass``


6: ``¬ ¬ def Credits(self):`` Here we are creating the subroutine 'Credits', this takes only one parameter, 'self', which contains all the necessary information to run this subroutine. 'Credits' will not return data unless an error occurs, in which case that is returned. This subroutine does the bulk of the programming for the Credits GUI.

7: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

8: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

9: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

10: ``¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits")`` Here we are appropriately using the subroutine we created earlier to update the caption of the GUI, we use the subroutine 'GetNormalCaption' from 'CaptionUtils.py' to do this. The second parameter is the name of the GUI we are currently in, (in this case that's; 'Credits'), this name should be identical to the subheading of the GUI where possible. 

11: ``¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Here we are loading the font 'Book Antiqua' from the font's folder, we set the size of this font to 15 and store the loaded font into the variable 'VersionFont'. 'self.mod_OS__.path.join()' is a subroutine that is part of the 'OS' module built into Python, this allows us to concatenate string data types to give us a file location.

12: ``¬ ¬ ¬ ¬ LargeCreditsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)`` Here we are loading the font 'Book Antiqua' and setting the size to 20, we store this object then in the variable 'LargeCreditsFont', where it will be appropriately used for sub-headings and titles for each of the sections of the credits sequence.

13: ``¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 60.

14: ``¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 35.

15: ``¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 15.

16: ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)`` Takes the font, which we stored in the variable 'MainTitleFont' and uses it to render the text "Pycraft", with the user's preference on anti-aliasing, 'aa' and the colour defined in 'ThemeUtils.py', the resulting Pygame.surface object is stored in the variable 'TitleFont'.

17: ``¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()`` Gets the width (in pixels) of the Pygame.surface object 'TitleFont

18: ``¬ ¬ ¬ ¬ TitleHeight = TitleFont.get_height()`` Here we are getting the height of the variable 'TitleFont' which we have just loaded.

19: ``¬ ¬ ¬ ¬ CreditsFont = InfoTitleFont.render("Credits", self.aa, self.SecondFontCol)`` Here we are rendering the text 'Credits' and using the font 'InfoTitleFont' to create a Pygame.surface object, which we store in the variable 'CreditsFont'. We also set the anti-aliasing based on the user's preference, and choose an appropriate colour from the user's current theme, in this case, as with ALL subheadings for GUIs, we use the 'SecondFontCol' which gives us greater customisability over the GUI.

20: ``¬ ¬ ¬ ¬ Credits1 = LargeCreditsFont.render(f"Pycraft: v{self.version}", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

21: ``¬ ¬ ¬ ¬ Credits1Width = Credits1.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

22: ``¬ ¬ ¬ ¬ Credits2 = LargeCreditsFont.render("Game Director: Tom Jebbo", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

23: ``¬ ¬ ¬ ¬ Credits2Width = Credits2.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

24: ``¬ ¬ ¬ ¬ Credits3 = LargeCreditsFont.render("Art and Music Lead: Tom Jebbo", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

25: ``¬ ¬ ¬ ¬ Credits3Width = Credits3.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

26: ``¬ ¬ ¬ ¬ Credits4 = LargeCreditsFont.render("Other Music Credits:", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

27: ``¬ ¬ ¬ ¬ Credits4Width = Credits4.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

28: ``¬ ¬ ¬ ¬ Credits5 = LargeCreditsFont.render("Freesound: - Erokia's 'ambient wave compilation' @ freesound.org/s/473545", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

29: ``¬ ¬ ¬ ¬ Credits5Width = Credits5.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

30: ``¬ ¬ ¬ ¬ Credits6 = LargeCreditsFont.render("Freesound: - Soundholder's 'ambient meadow near forest' @ freesound.org/s/425368", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

31: ``¬ ¬ ¬ ¬ Credits6Width = Credits6.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

32: ``¬ ¬ ¬ ¬ Credits7 = LargeCreditsFont.render("Freesound: - monte32's 'Footsteps_6_Dirt_shoe' @ freesound.org/people/monte32/sounds/353799", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

33: ``¬ ¬ ¬ ¬ Credits7Width = Credits7.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

34: ``¬ ¬ ¬ ¬ Credits8 = LargeCreditsFont.render("With thanks to the developers of:", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

35: ``¬ ¬ ¬ ¬ Credits8Width = Credits8.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

36: ``¬ ¬ ¬ ¬ Credits9 = LargeCreditsFont.render("PSutil", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

37: ``¬ ¬ ¬ ¬ Credits9Width = Credits9.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

38: ``¬ ¬ ¬ ¬ Credits10 = LargeCreditsFont.render("Python", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

39: ``¬ ¬ ¬ ¬ Credits10Width = Credits10.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

40: ``¬ ¬ ¬ ¬ Credits11 = LargeCreditsFont.render("Pygame", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

41: ``¬ ¬ ¬ ¬ Credits11Width = Credits11.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

42: ``¬ ¬ ¬ ¬ Credits12 = LargeCreditsFont.render("Numpy", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

43: ``¬ ¬ ¬ ¬ Credits12Width = Credits12.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

44: ``¬ ¬ ¬ ¬ Credits13 = LargeCreditsFont.render("Nuitka", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

45: ``¬ ¬ ¬ ¬ Credits13Width = Credits13.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

46: ``¬ ¬ ¬ ¬ Credits14 = LargeCreditsFont.render("CPUinfo", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

47: ``¬ ¬ ¬ ¬ Credits14Width = Credits14.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

48: ``¬ ¬ ¬ ¬ Credits15 = LargeCreditsFont.render("PyInstaller", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

49: ``¬ ¬ ¬ ¬ Credits15Width = Credits15.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

50: ``¬ ¬ ¬ ¬ Credits16 = LargeCreditsFont.render("PyAutoGUI", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

51: ``¬ ¬ ¬ ¬ Credits16Width = Credits16.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

52: ``¬ ¬ ¬ ¬ Credits17 = LargeCreditsFont.render("PyWaveFront", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

53: ``¬ ¬ ¬ ¬ Credits17Width = Credits17.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

54: ``¬ ¬ ¬ ¬ Credits18 = LargeCreditsFont.render("Microsoft's Visual Studio Code", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

55: ``¬ ¬ ¬ ¬ Credits18Width = Credits18.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

56: ``¬ ¬ ¬ ¬ Credits19 = LargeCreditsFont.render("PIL (Pillow/Python Imaging Library)", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

57: ``¬ ¬ ¬ ¬ Credits19Width = Credits19.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

58: ``¬ ¬ ¬ ¬ Credits20 = LargeCreditsFont.render("PyOpenGL (and PyOpenGL-accelerate)", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

59: ``¬ ¬ ¬ ¬ Credits20Width = Credits20.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

60: ``¬ ¬ ¬ ¬ Credits21 = LargeCreditsFont.render("For more in depth accreditation please check the GitHub Page @ github.com/PycraftDeveloper/Pycraft", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

61: ``¬ ¬ ¬ ¬ Credits21Width = Credits21.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

62: ``¬ ¬ ¬ ¬ Credits22 = LargeCreditsFont.render("With thanks to:", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

63: ``¬ ¬ ¬ ¬ Credits22Width = Credits22.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

64: ``¬ ¬ ¬ ¬ Credits23 = LargeCreditsFont.render("All my wonderful followers on Twitter, and you for installing this game, that's massively appreciated!", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

65: ``¬ ¬ ¬ ¬ Credits23Width = Credits23.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

66: ``¬ ¬ ¬ ¬ Credits24 = LargeCreditsFont.render("For full change-log please visit my aforementioned GitHub profile", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

67: ``¬ ¬ ¬ ¬ Credits24Width = Credits24.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

68: ``¬ ¬ ¬ ¬ Credits25 = LargeCreditsFont.render("Disclaimer:", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

69: ``¬ ¬ ¬ ¬ Credits25Width = Credits25.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

70: ``¬ ¬ ¬ ¬ Credits26 = VersionFont.render("The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

71: ``¬ ¬ ¬ ¬ Credits26Width = Credits26.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

72: ``¬ ¬ ¬ ¬ Credits27 = VersionFont.render("friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

73: ``¬ ¬ ¬ ¬ Credits27Width = Credits27.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

74: ``¬ ¬ ¬ ¬ Credits28 = VersionFont.render("my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

75: ``¬ ¬ ¬ ¬ Credits28Width = Credits28.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

76: ``¬ ¬ ¬ ¬ Credits29 = VersionFont.render("DOES NOT TAKE ANY RESPONSIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXTERNAL MODULES INSTALLED ONTO", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

77: ``¬ ¬ ¬ ¬ Credits29Width = Credits29.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

78: ``¬ ¬ ¬ ¬ Credits30 = VersionFont.render("YOUR COMPUTER (WHEN NOT CHOOSING THE RECOMMENDED EXECUTABLE VERSION) ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

79: ``¬ ¬ ¬ ¬ Credits30Width = Credits30.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

80: ``¬ ¬ ¬ ¬ Credits31 = VersionFont.render("RESPONSIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVICES MANAGER OR ADMINISTRATOR TO INSTALL AND USE", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

81: ``¬ ¬ ¬ ¬ Credits31Width = Credits31.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

82: ``¬ ¬ ¬ ¬ Credits32 = VersionFont.render("COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVICE, AND AT ANY POINT NO CONNECTION TO A", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

83: ``¬ ¬ ¬ ¬ Credits32Width = Credits32.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

84: ``¬ ¬ ¬ ¬ Credits33 = VersionFont.render("NETWORK IS REQUIRED. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you.", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

85: ``¬ ¬ ¬ ¬ Credits33Width = Credits33.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

86: ``¬ ¬ ¬ ¬ Credits34 = VersionFont.render("Thank You!", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

87: ``¬ ¬ ¬ ¬ Credits34Width = Credits34.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

88: ``¬ ¬ ¬ ¬ Credits34Height = Credits34.get_height()`` Here we are getting the height of the last Pygame.surface object in the sequence, this is important as its used in the calculation for calculating when that Pygame.surface object is exactly centered onscreen on the 'x' axis, in which case this will trigger the GUI to close. We store the resulting height in pixels of this Pygame.surface object in the variable 'Credits34Height'.


89: ``¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()`` Gets the width and height of the current Pygame window (in pixels), this is used in working out where everything should be scaled in-game if the window is resized.

90: ``¬ ¬ ¬ ¬ VisualYdisplacement = realHeight`` Now we are setting the variable 'visualYdisplacement' to be the same number as the height of the display, this is dont deliberately to make sure that when there animation begins the text moves up from the bottom, but until the animation begins the text is hidden offscreen.

91: ``¬ ¬ ¬ ¬ IntroYDisplacement = (realHeight-TitleHeight)/2`` Now we are setting the value of 'IntroYDisplacement' to be exactly the position halfway down the 'x' axis of the display, this means that when the first part of the animation is rendered, 'Pycraft', it's rendered centrally onscreen.

92: ``¬ ¬ ¬ ¬ timer = 5`` Now we set the variable 'timer' to the integer value of 5, this is used to control the order of appearance of the title, making sure that the title is displayed for approximately 4 seconds before the subheading 'Credits' appears below and the whole scene moves up.

93: ``¬ ¬ ¬ ¬ tempFPS = self.FPS`` This is used to temporarily store the game's target FPS, this is used later to slow the game down when minimised.


94: ``¬ ¬ ¬ ¬ EndClock = 0`` We set the value of 'EndClock' to be 0, this is another timer that controls how long the last piece of text in the animation (the 'thank you') is rendered for before sending us back to the home screen, but until we need to activate the timer to start counting up, we set the value to 0.

95: ``¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()`` Now we are getting the dimensions of the monitor the display is currently on, this is used later on to calculate the dimensions for a rectangle that prevents the animation from rendering text above the title. (This isn't going to be used in later versions, its being replaced with 'realWidth').

96: ``¬ ¬ ¬ ¬ while True:`` Enters the project's game loop

97: ``¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()`` Gets the width and height of the current Pygame window (in pixels), this is used in working out where everything should be scaled in-game if the window is resized.


98: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:`` Detects if the window has been made smaller than the minimum width, 1280 pixels

99: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)`` If the window is smaller than 1280 pixels, then reset the display's WIDTH to 1280. There is no limit to how large the display can be.

100: ``¬ ¬ ¬ ¬ ¬ if realHeight < 720:`` Detects if the window has been made smaller than the minimum height, 720 pixels

101: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)`` If the window is smaller than 720 pixels, then reset the display's HEIGHT to 720. There is no limit to how large the display can be.


102: ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()`` Gets the current window frame-rate (in Hz)

103: ``¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS`` Adds the current framerate to a variable which is used to calculate the mean average FPS in game (in Hz)

104: ``¬ ¬ ¬ ¬ ¬ self.Iteration += 1`` Used as frequency in calculating the mean average FPS (in Hz)


105: ``¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)`` This line of code is used to control what happens when the display is minimised, for more information, see the documentation for this subroutine. This subroutine will return an integer, this is stored in the variable 'tempFPS', which is used to set the windows FPS (in Hz).


106: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, here we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

107: ``¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):`` This controls when the display should close (if on the 'ome-Screen') or returning back to the previous window (typically the 'ome-Screen'), to do this you can press the 'x' at the top of the display, or by pressing 'ESC or ESCAPE' which is handy when in full-screen modes.

108: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:`` This if-statement controls if sound should be played or not based on the user's preference in 'Settings.py', the user's preference is stored when the program closes.

109: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)`` This line calls the subroutine; 'PlayClickSound' in 'SoundUtils.py', if the user has allowed sound to play in settings, then interacting with the display will cause the click sound to play; volume and other parameters for this subroutine are stored in the global variable 'self'.

110: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.

111: ``¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:`` This line detects if any key is pressed on a keyboard, used when detecting events like pressing keys to navigate the GUIs or moving in-game.

112: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:`` This line of code is used as part of the activation for 'Devmode' which you activate by pressing SPACE 10 times. Here we are detecting is the SPACE key has been pressed and 'Devmode' is not already active.

113: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1`` This line increases the value of the variable 'Devmode' by 1. When the variable 'Devmode' is equal to 0, then 'Devmode' is activated.

114: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:`` Detects if the key 'q' is pressed (not case sensitive).

115: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)`` If the key 'q' is pressed, then we load up the secondary window in 'TkinterUtils.py', this, like 'Devmode' displays information about the running program. This feature may be deprecated at a later date, but this isn't clear yet. All the data the subroutine needs to access is sent through the parameter 'self' which is a global variable.

116: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:`` This line detects if the function key 'F11' has been pressed.

117: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)`` If the function key 'F11' has been pressed, then resize the display by toggling full-screen. (The 'F11' key is commonly assigned to this in other applications).

118: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:`` Detects if the key 'x' is pressed (NOT case sensitive).

119: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1`` This resets 'Devmode' to 1, turning the feature off. This can be used to cancel counting the number of spaces pressed too.


120: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits and Change-Log")`` Here we are appropriately using the subroutine we created earlier to update the caption of the GUI, we use the subroutine 'GetNormalCaption' from 'CaptionUtils.py' to do this. The second parameter is the name of the GUI we are currently in, (in this case that's; 'Credits and Change-Log')

121: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

122: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits1, ((realWidth-Credits1Width)/2, 0+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

123: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits2, ((realWidth-Credits2Width)/2, 115+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

124: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits3, ((realWidth-Credits3Width)/2, (115*2)+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

125: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits4, ((realWidth-Credits4Width)/2, (115*3)+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

126: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits5, ((realWidth-Credits5Width)/2, (115*3)+20+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

127: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits6, ((realWidth-Credits6Width)/2, (115*3)+40+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

128: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits7, ((realWidth-Credits7Width)/2, (115*3)+60+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

129: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits8, ((realWidth-Credits8Width)/2, 540+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

130: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits9, ((realWidth-Credits9Width)/2, 540+20+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

131: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits10, ((realWidth-Credits10Width)/2, 540+40+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

132: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits11, ((realWidth-Credits11Width)/2, 540+60+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

133: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits12, ((realWidth-Credits12Width)/2, 540+80+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

134: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits13, ((realWidth-Credits13Width)/2, 540+100+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

135: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits14, ((realWidth-Credits14Width)/2, 540+120+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

136: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits15, ((realWidth-Credits15Width)/2, 540+140+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

137: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits16, ((realWidth-Credits16Width)/2, 540+160+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

138: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits17, ((realWidth-Credits17Width)/2, 540+180+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

139: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits18, ((realWidth-Credits18Width)/2, 540+200+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

140: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits19, ((realWidth-Credits19Width)/2, 540+220+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

141: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits20, ((realWidth-Credits20Width)/2, 540+240+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

142: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits21, ((realWidth-Credits21Width)/2, 540+260+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

143: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits22, ((realWidth-Credits22Width)/2, 915+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

144: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits23, ((realWidth-Credits23Width)/2, 935+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

145: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits24, ((realWidth-Credits24Width)/2, 1050+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

146: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits25, ((realWidth-Credits25Width)/2, 1165+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

147: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits26, ((realWidth-Credits26Width)/2, 1167+15+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

148: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits27, ((realWidth-Credits27Width)/2, 1167+30+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

149: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits28, ((realWidth-Credits28Width)/2, 1167+45+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

150: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits29, ((realWidth-Credits29Width)/2, 1167+60+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

151: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits30, ((realWidth-Credits30Width)/2, 1167+75+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

152: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits31, ((realWidth-Credits31Width)/2, 1167+90+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

153: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits32, ((realWidth-Credits32Width)/2, 1167+105+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

154: ``¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits33, ((realWidth-Credits33Width)/2, 1167+120+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.


155: ``¬ ¬ ¬ ¬ ¬ if timer >= 1:`` Now we are checking the 'timer' variable we created earlier, this variable starts at the value of 5 and will decrease until the variable is less than or equal to 1. This if-statement controls how long the title 'Pycraft' is rendered centrally for at the start of the animation - approximately 4 seconds.

156: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))`` If the preceding if-statement is true, then we render the title centered on both the 'x' and 'y' value. The  'x' axis calculation is the same as we have seen before, but the 'y' axis calculation takes the value of 0, and (at this point in the program) will add the amount of pixels that is half of the height of the display, this we do when we first defined the variable earlier.

157: ``¬ ¬ ¬ ¬ ¬ ¬ timer -= 1/(self.aFPS/self.Iteration)`` As the program runs for the first 4 seconds at the start of the animation, we will need to decrease the timer, otherwise we would never get out of loading that section, to do this we remove exactly the time it takes for 1 frame to pass, with each run (by calculating the average FPS using 'self.aFPS/self.Iteration', and dividing 1 by that decimal value). If we just did 'timer -= 1' then the start of the animation where the title is centred would stay there for only 4 frames, a very small amount of time, and we cant specify say 'wait 500 runs' before moving on (maybe by doing 'timer -= 0.01') because of the ability to change FPS' so that could be 15 seconds at 15FPS, but just 0.5 at 240FPS.

158: ``¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement = realHeight`` Now we are setting the variable 'visualYdisplacement' to be the same number as the height of the display, this is dont deliberately to make sure that when there animation begins the text moves up from the bottom, but until the animation begins the text is hidden offscreen.

159: ``¬ ¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

160: ``¬ ¬ ¬ ¬ ¬ ¬ if IntroYDisplacement <= 0:`` Now we are checking to see if the variable 'IntroYDisplacement' is less than or equal to 0, this will return True when the 'timer' if-statement we created earlier hits a value less than 1. This if-statement initiates the rest of the animation.

161: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, FullscreenX, 90)`` Now we are defining the dimensions of a rectangle, to which we store in the variable 'cover_Rect', this object will be used to prevent the text from sliding over the title and sub-heading during the animation. We set the (x,y) positions to the top-left most corner of the GUI, and the rectangle spans the length of the display (there is a bug here; instead of 'FullscreenX', this should be 'realWidth'), and we make the rectangle's height to be 90, as this covers the title and sub-heading without taking up too much space.

162: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)`` This line draws a rectangle to the display with 'self.Display', the colour to fill the rectangle is the colour of the background to Pycraft (This is a setting the user can change in the GUI in 'Settings.py') with the dimensions of the previously created Pygame Rect object called; 'cover_Rect'.

163: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))`` This line takes the Pygame.surface object 'TitleFont' and draws it onto the window (stored in the variable 'self.Display', at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. The coordinates are (x, y).

164: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50))`` Here we are rendering the subheading for this GUI; 'Credits', to the display, referencing it with the variable 'self.Display'. We set the position to be slightly off-centred to the right, and down 50 pixels to prevent it from overlapping with the title.

165: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if int(1402+VisualYdisplacement) <= int(realHeight/2):`` Now we are checking to see if the value of 'VisualYdisplacement' add 1402 is less than or equal to half the height of the GUI (all values for this are truncated to the nearest integer), this is done to check when the animation is nearing a close and what to do next.

166: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, (realHeight-Credits34Height)/2))`` When the last line of the credits animation is at the centre of the GUI, we stop it from moving up any further and set the (x,y) position for the line to be exactly centred on all axis to the middle of the display, we do this using the same formula as before for the 'x' axis, and use a similar formula, but with the height values, for the 'y' position. This is also where we needed to calculate the height of the last line of the credits.

167: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement -= 60/(self.aFPS/self.Iteration)`` Now we are setting the movement speed for the animation, we take 60 and divide it by the average frame rate by dividing 'self.aFPS' by 'self.Iteration'. We store the result in the variable 'VisualYdisplacement' which we add to the 'y' position for each of the lines in the credits GUI. The speed of the animation is the difference between the values as the game runs (its subtract as we move up the display, so move closer to zero) and the displacement modifier is the result (for example, in the sequence; 2,4,6,8; 2 is the speed and the displacement modifier would be each of those values for each frame. 

168: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if EndClock >= 5:`` At the end of the animation we count up from 0 to 5 seconds, after this timer has run out, we go back to the home-screen. This if-statement will send us back to the home screen if it returns true.

169: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.

170: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

171: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ EndClock += 1/(self.aFPS/self.Iteration)`` If we reach the last section of the animation, where we render 'Thank You' centrally onscreen, we use this timer to count out 5 seconds before we move on to the home-screen. We use the same formula as we did earlier with the 'timer' variable, except this timer we count up instead of down (It can be either, it makes little difference)

172: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

173: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, 1402+VisualYdisplacement))`` If, however we are not at the end of the animation, we render the 'Thank You' line of the credits menu like we do with the others, centered on the 'x' axis, and moving up the 'y' axis based on the value of 'VisualYdisplacement', this will only run when the message is less than half way up the GUI, as it stops when the text is centred on both axis.

174: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement -= 60/(self.aFPS/self.Iteration)`` Now we are setting the movement speed for the animation, we take 60 and divide it by the average frame rate by dividing 'self.aFPS' by 'self.Iteration'. We store the result in the variable 'VisualYdisplacement' which we add to the 'y' position for each of the lines in the credits GUI. The speed of the animation is the difference between the values as the game runs (its subtract as we move up the display, so move closer to zero) and the displacement modifier is the result (for example, in the sequence; 2,4,6,8; 2 is the speed and the displacement modifier would be each of those values for each frame. 

175: ``¬ ¬ ¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

176: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)`` This line defines the dimensions of a rectangle in Pygame, in this case the rectangle will be drawn at (0, 0) (x, y) with a width of 1280 and a height of 90. (all values here are in pixels and (0, 0) (x, y) is the top-left corner of the GUI (so thats 90 pixels DOWN)).

177: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)`` This line draws a rectangle to the display with 'self.Display', the colour to fill the rectangle is the colour of the background to Pycraft (This is a setting the user can change in the GUI in 'Settings.py') with the dimensions of the previously created Pygame Rect object called; 'cover_Rect'.

178: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))`` If the preceding if-statement is true, then we render the title centered on both the 'x' and 'y' value. The  'x' axis calculation is the same as we have seen before, but the 'y' axis calculation takes the value of 0, and (at this point in the program) will add the amount of pixels that is half of the height of the display, this we do when we first defined the variable earlier.

179: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50+IntroYDisplacement))`` Just after the title as finished its 4 second timer onscreen, the text 'credits' appears beside it and they both move up the display to the top-centre together, as it moves up the display this is the function that renders the Pygame.surface object to the display (stored in the variable 'self.Display'). We render this just off centred to the right on the 'x' axis, and at 50 pixels down the GUI, but this is affected by 'VisualYdisplacement', so its position on-screen in the 'y' axis can be adjusted as part of the animation.

180: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ IntroYDisplacement -= 90/(self.aFPS/self.Iteration)`` Here we are updating the variable 'IntroYDisplacement' by subtracting the output of the formula '90/(self.aFPS/self.Iteration)', the syntax 'self.aFPS/self.Iteration' gets the average FPS of the game. This variable is used when calculating how fast to move the title and sub-title up the screen (so that is why we subtract here, because we want to make the variable closer to 0 as we move to the top of the display).

181: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement = realHeight`` Now we are setting the variable 'visualYdisplacement' to be the same number as the height of the display, this is dont deliberately to make sure that when there animation begins the text moves up from the bottom, but until the animation begins the text is hidden offscreen.


182: ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)`` This line calls the subroutine 'CreateDevmodeGraph', this subroutine is responsible for drawing the graph you see at the top-right of most Pycraft GUI's. It takes the variable 'self' as a parameter, this code will return any errors, which are stored in the variable 'Message'. If there are no errors then the subroutine will return 'None'. The second parameter 'DataFont' is the currently loaded font which is used for rendering the text at the top of the graph.

183: ``¬ ¬ ¬ ¬ ¬ if not Message == None:`` This line detects if there are any errors stored in the variable 'Message'. All important errors are stored in this variable. This error detection may be moved to a thread at a later date.

184: ``¬ ¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

185: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

186: ``¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)`` This line of code controls how fast the GUI should refresh, defaulting to the user's preference unless the window is minimised, in which case its set to 15 FPS. All values for FPS are in (Hz) and this line of code specifies the maximum FPS of the window, but this does not guarantee that FPS.

187: ``¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

188: ``¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.



.. note::
   For information on this consult the above guide

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



6: ``¬ ¬ def UpdateDisplay(self): # Run tests to make sure windows not too small`` Here we are creating a subroutine called 'UpdateDisplay', this subroutine takes only the parameter 'self', this subroutine handles the resizing and full-screen window switching in Pygame.

7: ``¬ ¬ ¬ self.Data_aFPS = []`` Here we are creating an empty array, stored in the variable 'self.Data_aFPS'. This will store the program's average FPS, which will be used later on for drawing its respective 'Devmode' graph.

8: ``¬ ¬ ¬ self.Data_CPUUsE = []`` Here we are creating an empty array, stored in the variable; 'self.Data_CPUUse'. This array will store the CPU's usage percentage    (which is seen in task manager). This will be used later on for the graphing of its respective graph in the for 'Devmode'.

9: ``¬ ¬ ¬ self.Data_eFPS = []`` Here we are creating a blank array; which we will store in the variable 'self.Data_eFPS'. This array will store vales for the current in-game FPS, which will be used later on in 'Devmode', for drawing its respective line graph.

10: ``¬ ¬ ¬ self.Data_MemUsE = []`` Here we are creating an array in the variable 'self.Data_MemUsE', which will store data about the amount of memory is currently being used by the system, which will be used later on in drawing the line graph in 'Devmode'.

11: ``¬ ¬ ¬ self.Timer = 0`` Here we are setting the variable 'self.Timer' to 0, this will be used later on in 'Devmode' for controlling the data polling rate (how often the program will get the current metrics).

12: ``¬ ¬ ¬ self.Data_aFPS_Min = 60`` On this line we are setting the variable 'self.Data_aFPS_Min' to 60, this integer is chosen because it should be easily overwritten by a smaller value as the program runs. This stores the minimum average FPS.

13: ``¬ ¬ ¬ self.Data_aFPS_Max = 1`` This stores the maximum average FPS value that has been recorded, this variable 'self.Data_aFPS_Max' is set to 1 again because this should be easily overwritten by a higher average value.


14: ``¬ ¬ ¬ self.Data_CPUUsE_Min = 60`` Here we are setting the variable 'self.Data_CPUUsE_Min' to 60, this stores the minimum CPU usage (as a percentage) so should be easily overwritten by a smaller number.

15: ``¬ ¬ ¬ self.Data_CPUUsE_Max = 1`` Here we are setting the variable 'self.Data_CPUUsE_Max' to 1, because this should be easily overwritten by a larger number (as a percentage).


16: ``¬ ¬ ¬ self.Data_eFPS_Min = 60`` Here we are setting this variable to have a value of 60. This should be easily overwritten as the program runs and stores the smallest recorded raw FPS value.

17: ``¬ ¬ ¬ self.Data_eFPS_Max = 1`` Now we set the previous variable's counterpart, the maximum recorded value of the raw FPS to 0, this should be easily overwritten and is used in calculating how the line graph in 'Devmode' on the top-right should be drawn, each of the minimum and maximum values are used for this purpose.


18: ``¬ ¬ ¬ self.Data_MemUsE_Min = 50`` Now we set the lowest value for memory usage (as a percentage) to 50, this number is chosen because it should be easily overwritten.

19: ``¬ ¬ ¬ self.Data_MemUsE_Max = 50`` Now we set the highest value of memory usage (as a percentage) to 50, this should be easily overwritten, this is used as part of the calculation for the line graph in 'Devmode'. All of the above values are chosen because they should be easily overwritten with a more appropriate value, but we need to assign the variables a value then we create them. These values will be used in calculating the dimensions for the line graph we create in 'Devmode', if you are familiar with the documentation for the benchmark, we saw a similar method there.


20: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

21: ``¬ ¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

22: ``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()`` Now we are getting the dimensions of the monitor the display is currently on, this is used later on to calculate the dimensions for a rectangle that prevents the animation from rendering text above the title. (This isn't going to be used in later versions, its being replaced with 'realWidth').

23: ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

24: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

25: ``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:`` Next we are checking to see if the variable 'self.Fullscreen' is False. This variable controls the toggling of full-screen and windowed displays, and if this if-statement returns True; the display will be in windowed mode.

26: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

27: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

28: ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = True`` Now, because we are toggling the display between windowed and full-screen mode, we need to flip the value of 'self.Fullscreen' so that next time the program refreshes the display. 

29: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.RESIZABLE)`` Now we are setting the variable 'self.Display', which is where we draw all of our Pygame surfaces and objects. This line sets the display to have the dimensions of 'self.SavedWidth' and 'self.SavedHeight', in pixels. We use those variables because they store the size of the window from when it was last in windowed mode, meaning the game remembers the size of the window. Finally we also give the display thee parameter 'self.mod_Pygame__.RESIZEABLE' which allows us to re-shape and  re-size the window.

30: ``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:`` Next we are checking to see if the variable 'self.Fullscreen' is equal to True. This is the other part of the toggle, if this if-statement returns True then the window will be set to be fullscreen.

31: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

32: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

33: ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = False`` Now we are inverting the Boolean value for the variable 'self.Fullscreen' as part of the toggle, so next time the process is called the display will switch to windowed mode.

34: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF)`` Now are creating a Pygame.surface object which will have the RESOLUTION of the current monitor, we also set some additional parameters; setting the display to fullscreen, be hardware accelerated and (this is a bug) have a double buffer (which is used in 3D applications) we store this object in the variable 'self.Display', which is what we draw all images, text, shapes and objects to when we are not in the 3D game-engine.

35: ``¬ ¬ ¬ ¬ except Exception as error:`` Here we are handling any errors that may occur whilst toggling the display between windowed and full-screen (or visa-versa) we store any errors in the variable 'error' (note this will be changed to match the new error handling guidelines in Pycraft v0.9.4.

36: ``¬ ¬ ¬ ¬ ¬ self.Fullscreen = True`` Now, because we are toggling the display between windowed and full-screen mode, we need to flip the value of 'self.Fullscreen' so that next time the program refreshes the display. 

37: ``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280`` If an error does occur, then we want to reset any variables that could have been problematic, we start by resetting the value of the variable 'self.SavedWidth' to 1280, which used to be the fixed window size for Pycraft, and is still the width all objects are rendered too, before a scale factor moves then suitably based on how much larger the window is.

38: ``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720`` We also reset the value of the variable 'self.SavedHeight' to 720 (both of these variables values are in pixels), this value is chosen for the same reasons as the previous.

39: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

40: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

41: ``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight))`` Here we are setting the Pygame.surface object stored in 'self.Display' to the size we just specified with the resetting of those variables. Note there is no special parameters for the display here, this is designed to be a fallback option and be as simple as it can to avoid causing the error or more errors. When the user re-starts the project they will be able to re-size the GUI like normal (unless the user toggles full-screen and it works successfully).

42: ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

43: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

44: ``¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

45: ``¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

46: ``¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

47: ``¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.



48: ``¬ ¬ def SetOPENGLdisplay(self):`` This display is only used in the Benchmark GUI and will be deprecated in Pycraft v0.9.4

49: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

50: ``¬ ¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

51: ``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()`` Now we are getting the dimensions of the monitor the display is currently on, this is used later on to calculate the dimensions for a rectangle that prevents the animation from rendering text above the title. (This isn't going to be used in later versions, its being replaced with 'realWidth').

52: ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

53: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

54: ``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == True:`` here we are checking to see if the variable 'self.Fullscreen' is equal to Boolean True.

55: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

56: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

57: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)`` Here we are setting the display which we will store in the variable 'self.Display', this surface is created in windowed mode with the size of the previous window. We also use the parameters: 'DOUBLEBUF' which allows for the creation of a second buffer or frame. 'OPENGL', this parameter allows us to interact directly with an OpenGL environment, like the one we had created previously in the old game-engine, and the OpenGL section of the benchmark.

58: ``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == False:`` If the previous if-statement returned False, then we check to see if the variable 'self.Fullscreen' is equal to Boolean False, in which case the OpenGL display will be full-screen.

59: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

60: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

61: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)`` Here we are creating a Pygame.surface which we set to the RESOLUTION of the current monitor, and we use the same parameters as before but also add the 'FULLSCREEN' parameter which makes the window full-screen so sets it to the size of the monitor. Wwe also specify the 'HWSURFACE' parameter which is short for 'HardWare Surface' which enables hardware acceleration for full-screen windows, giving us a slight boost in performance.

62: ``¬ ¬ ¬ ¬ except Exception as error:`` Here we are handling any errors that may occur whilst toggling the display between windowed and full-screen (or visa-versa) we store any errors in the variable 'error' (note this will be changed to match the new error handling guidelines in Pycraft v0.9.4.

63: ``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280`` If an error does occur, then we want to reset any variables that could have been problematic, we start by resetting the value of the variable 'self.SavedWidth' to 1280, which used to be the fixed window size for Pycraft, and is still the width all objects are rendered too, before a scale factor moves then suitably based on how much larger the window is.

64: ``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720`` We also reset the value of the variable 'self.SavedHeight' to 720 (both of these variables values are in pixels), this value is chosen for the same reasons as the previous.

65: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

66: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

67: ``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)`` Here we are setting the display which we will store in the variable 'self.Display', this surface is created in windowed mode with the size of the previous window. We also use the parameters: 'DOUBLEBUF' which allows for the creation of a second buffer or frame. 'OPENGL', this parameter allows us to interact directly with an OpenGL environment, like the one we had created previously in the old game-engine, and the OpenGL section of the benchmark.

68: ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

69: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

70: ``¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

71: ``¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

72: ``¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

73: ``¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.



74: ``¬ ¬ def UpdateOPENGLdisplay(self):`` Now we are creating the subroutine 'UpdateOPENGLdisplay' which takes the parameter of 'self', this subroutine toggles full-screen and windowed modes for the OpenGL display. This subroutine will be deprecated in Pycraft v0.9.4 with the move towards ModernGL and ModernGL_window handling a greater portion of the OpenGL/3D game-engine.

75: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

76: ``¬ ¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

77: ``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()`` Now we are getting the dimensions of the monitor the display is currently on, this is used later on to calculate the dimensions for a rectangle that prevents the animation from rendering text above the title. (This isn't going to be used in later versions, its being replaced with 'realWidth').

78: ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

79: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

80: ``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:`` Next we are checking to see if the variable 'self.Fullscreen' is False. This variable controls the toggling of full-screen and windowed displays, and if this if-statement returns True; the display will be in windowed mode.

81: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

82: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

83: ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = True`` Now, because we are toggling the display between windowed and full-screen mode, we need to flip the value of 'self.Fullscreen' so that next time the program refreshes the display. 

84: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)`` Here we are setting the display which we will store in the variable 'self.Display', this surface is created in windowed mode with the size of the previous window. We also use the parameters: 'DOUBLEBUF' which allows for the creation of a second buffer or frame. 'OPENGL', this parameter allows us to interact directly with an OpenGL environment, like the one we had created previously in the old game-engine, and the OpenGL section of the benchmark.

85: ``¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:`` Next we are checking to see if the variable 'self.Fullscreen' is equal to True. This is the other part of the toggle, if this if-statement returns True then the window will be set to be fullscreen.

86: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

87: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

88: ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = False`` Now we are inverting the Boolean value for the variable 'self.Fullscreen' as part of the toggle, so next time the process is called the display will switch to windowed mode.

89: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)`` Here we are creating a Pygame.surface which we set to the RESOLUTION of the current monitor, and we use the same parameters as before but also add the 'FULLSCREEN' parameter which makes the window full-screen so sets it to the size of the monitor. Wwe also specify the 'HWSURFACE' parameter which is short for 'HardWare Surface' which enables hardware acceleration for full-screen windows, giving us a slight boost in performance.

90: ``¬ ¬ ¬ ¬ except:`` (This needs updating to follow the guidelines of the documentation) This ignores any errors that may occur when running the main section of the benchmark, or in creating our Pygame window.

91: ``¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280`` If an error does occur, then we want to reset any variables that could have been problematic, we start by resetting the value of the variable 'self.SavedWidth' to 1280, which used to be the fixed window size for Pycraft, and is still the width all objects are rendered too, before a scale factor moves then suitably based on how much larger the window is.

92: ``¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720`` We also reset the value of the variable 'self.SavedHeight' to 720 (both of these variables values are in pixels), this value is chosen for the same reasons as the previous.

93: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

94: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

95: ``¬ ¬ ¬ ¬ ¬ self.Fullscreen = False`` Now we are inverting the Boolean value for the variable 'self.Fullscreen' as part of the toggle, so next time the process is called the display will switch to windowed mode.

96: ``¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)`` Here we are setting the display which we will store in the variable 'self.Display', this surface is created in windowed mode with the size of the previous window. We also use the parameters: 'DOUBLEBUF' which allows for the creation of a second buffer or frame. 'OPENGL', this parameter allows us to interact directly with an OpenGL environment, like the one we had created previously in the old game-engine, and the OpenGL section of the benchmark.

97: ``¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

98: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

99: ``¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

100: ``¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

101: ``¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

102: ``¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.



103: ``¬ ¬ def SetDisplay(self):`` Here we are creating the subroutine 'SetDisplay', which performs a very similar function to the 'UpdateDisplay' subroutine, both take the parameter 'self' and only return any errors that may occur. The main difference is that the two if-statements are flipped which is important for controlling how the display resizing works. 

104: ``¬ ¬ ¬ self.Data_aFPS = []`` Here we are creating an empty array, stored in the variable 'self.Data_aFPS'. This will store the program's average FPS, which will be used later on for drawing its respective 'Devmode' graph.

105: ``¬ ¬ ¬ self.Data_CPUUsE = []`` Here we are creating an empty array, stored in the variable; 'self.Data_CPUUse'. This array will store the CPU's usage percentage    (which is seen in task manager). This will be used later on for the graphing of its respective graph in the for 'Devmode'.

106: ``¬ ¬ ¬ self.Data_eFPS = []`` Here we are creating a blank array; which we will store in the variable 'self.Data_eFPS'. This array will store vales for the current in-game FPS, which will be used later on in 'Devmode', for drawing its respective line graph.

107: ``¬ ¬ ¬ self.Data_MemUsE = []`` Here we are creating an array in the variable 'self.Data_MemUsE', which will store data about the amount of memory is currently being used by the system, which will be used later on in drawing the line graph in 'Devmode'.

108: ``¬ ¬ ¬ self.Timer = 0`` Here we are setting the variable 'self.Timer' to 0, this will be used later on in 'Devmode' for controlling the data polling rate (how often the program will get the current metrics).

109: ``¬ ¬ ¬ self.Data_aFPS_Min = 60`` On this line we are setting the variable 'self.Data_aFPS_Min' to 60, this integer is chosen because it should be easily overwritten by a smaller value as the program runs. This stores the minimum average FPS.

110: ``¬ ¬ ¬ self.Data_aFPS_Max = 1`` This stores the maximum average FPS value that has been recorded, this variable 'self.Data_aFPS_Max' is set to 1 again because this should be easily overwritten by a higher average value.


111: ``¬ ¬ ¬ self.Data_CPUUsE_Min = 60`` Here we are setting the variable 'self.Data_CPUUsE_Min' to 60, this stores the minimum CPU usage (as a percentage) so should be easily overwritten by a smaller number.

112: ``¬ ¬ ¬ self.Data_CPUUsE_Max = 1`` Here we are setting the variable 'self.Data_CPUUsE_Max' to 1, because this should be easily overwritten by a larger number (as a percentage).


113: ``¬ ¬ ¬ self.Data_eFPS_Min = 60`` Here we are setting this variable to have a value of 60. This should be easily overwritten as the program runs and stores the smallest recorded raw FPS value.

114: ``¬ ¬ ¬ self.Data_eFPS_Max = 1`` Now we set the previous variable's counterpart, the maximum recorded value of the raw FPS to 0, this should be easily overwritten and is used in calculating how the line graph in 'Devmode' on the top-right should be drawn, each of the minimum and maximum values are used for this purpose.


115: ``¬ ¬ ¬ self.Data_MemUsE_Min = 50`` Now we set the lowest value for memory usage (as a percentage) to 50, this number is chosen because it should be easily overwritten.

116: ``¬ ¬ ¬ self.Data_MemUsE_Max = 50`` Now we set the highest value of memory usage (as a percentage) to 50, this should be easily overwritten, this is used as part of the calculation for the line graph in 'Devmode'. All of the above values are chosen because they should be easily overwritten with a more appropriate value, but we need to assign the variables a value then we create them. These values will be used in calculating the dimensions for the line graph we create in 'Devmode', if you are familiar with the documentation for the benchmark, we saw a similar method there.


117: ``¬ ¬ ¬ self.Data_CPUUsE_Min = 50`` Here we are setting the variable 'self.Data_CPUUsE_Min' to 50, this stores the minimum CPU usage (as a percentage) so should be easily overwritten by a smaller number.

118: ``¬ ¬ ¬ self.Data_CPUUsE_Max = 50`` Here we are setting the variable 'self.Data_CPUUsE_Max' to 50, because this should be easily overwritten by a larger number (as a percentage).

119: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

120: ``¬ ¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

121: ``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()`` Now we are getting the dimensions of the monitor the display is currently on, this is used later on to calculate the dimensions for a rectangle that prevents the animation from rendering text above the title. (This isn't going to be used in later versions, its being replaced with 'realWidth').

122: ``¬ ¬ ¬ ¬ ¬ if self.Fullscreen == True:`` here we are checking to see if the variable 'self.Fullscreen' is equal to Boolean True.

123: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

124: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.
