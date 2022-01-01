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

Achievements
====================
Overview
++++++++++++++++++++
This module controls the displaying and processing of in-game achievements: This feature will be expanded upon when achievements are added and you can earn them in game.

The ``GenerateAchievements`` class controls the rendering of the achievements GUI this can be accessed from the 'home screen' of Pycraft, currently this class only renders a blank window, which is coloured and has a title [Pycraft] and header [Achievements], but expect an update here when its possible to earn achievements in game!

The ``Achievements(self)`` function, like most subroutines in Pycraft, takes ``self`` to be its only input. It will return only an error, should one arise, which will be stored in the ``messages`` variable. This subroutine is where the bulk of the processing for this class is done, this subroutine is responsible for the Achievements GUI which you can access through Pycraft's home screen.

Detailed Breakdown
++++++++++++++++++++

1: ``if not __name__ == "__main__":`` This checks to see if the place its called from (stored in the variable ``__name__``) is not ``"__main__"``. The string ``"__main__"`` would be the data stored in the variable ``__name__`` if the project was run on its own, which in this case we don't want so we only allow the code inside the if-statement to run if the data in ``__name__`` is not "__main__".

2: ``¬ print("Started <Pycraft_Achievements>")`` Now we output data to the terminal if the program is running, this allows us to know if there are any errors preventing this module from loading, in which case the program would crash before that is outputted to the terminal, making us aware the error is in this module.

3: ``¬ class GenerateAchievements:`` Now we are defining a class with a suitable name that represents what the subroutines in this class do; this allows us to group up our code to make it easier to edit, organise and debug later on, as well as saving on memory as not every function will need to be loaded at once.

4: ``¬ ¬ def __init__(self):`` Here we make sure the module is initialized correctly we do this because if we tried to call this standalone, and without the code that would stop this, then all references to variables and subroutines outside of this project would be invalid and cause issues. This is also where the variable ‘self’ is defined for all references in this class. This subroutine is a procedure, so does not return a value.

5: ``¬ ¬ ¬ pass`` Here we tell python to ignore the previous line of code that expects indented code, we use this if we don't need to put any code in this indent, this should be avoided in most situations. This is mainly used in the ``__init__`` functions for Pycraft where we may not need to run any code, but need to make sure the module is working correctly.


7: ``¬ ¬ def Achievements(self):`` This line defines the Achievements class, this is where all achievements you have earned in-game will be displayed. You access this from the home screen and at present does very little, as there isn't much in game to do, and no achievements to earn. This procedure will be getting an update before Pycraft v0.11. This takes, as most subroutines only takes the variable 'self' which is defined in 'main.py'.

8: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

9: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

10: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

11: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")`` This calls the 'GetNormalCaption' subroutine in 'CaptionUtils.py', This tool takes values from the variable 'self', which stores lots of the global variables stored in the entire program, and also a second input which, in this case its "Achievements" is asked for, this is useful for allowing the user to know what GUI they are in. The variable 'self' is called when the player has activated 'Devmode', (by pressing SPACE 10 times), this brings up lots of details in the caption regarding what the program is doing and the resources its using.

12: ``¬ ¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 60.

13: ``¬ ¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 35.

14: ``¬ ¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 15.


16: ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)`` Takes the font, which we stored in the variable 'MainTitleFont' and uses it to render the text "Pycraft", with the user's preference on anti-aliasing, 'aa' and the colour defined in 'ThemeUtils.py', the resulting Pygame.surface object is stored in the variable 'TitleFont'.

17: ``¬ ¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()`` Gets the width (in pixels) of the Pygame.surface object 'TitleFont


19: ``¬ ¬ ¬ ¬ AchievementsFont = InfoTitleFont.render("Achievements", self.aa, self.SecondFontCol)`` Takes the font we loaded previously into the variable 'InfoTitleFont' and render the text 'Achievements, with the anti-aliasing based on the user's preference, and colour defined based on the user's colour theme.

20: ``¬ ¬ ¬ ¬ ¬ tempFPS = self.FPS`` This is used to temporarily store the game's target FPS, this is used later to slow the game down when minimised.


22: ``¬ ¬ ¬ ¬ while True:`` Enters the project's game loop

23: ``¬ ¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()`` Gets the width and height of the current Pygame window (in pixels), this is used in working out where everything should be scaled in-game if the window is resized.


25: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:`` Detects if the window has been made smaller than the minimum width, 1280 pixels

26: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)`` If the window is smaller than 1280 pixels, then reset the display's WIDTH to 1280. There is no limit to how large the display can be.

27: ``¬ ¬ ¬ ¬ ¬ ¬ if realHeight < 720:`` Detects if the window has been made smaller than the minimum height, 720 pixels

28: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)`` If the window is smaller than 720 pixels, then reset the display's HEIGHT to 720. There is no limit to how large the display can be.


30: ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()`` Gets the current window frame-rate (in Hz)

31: ``¬ ¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS`` Adds the current framerate to a variable which is used to calculate the mean average FPS in game (in Hz)

32: ``¬ ¬ ¬ ¬ ¬ ¬ self.Iteration += 1`` Used as frequency in calculating the mean average FPS (in Hz)


34: ``¬ ¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)`` This line of code is used to control what happens when the display is minimised, for more information, see the documentation for this subroutine. This subroutine will return an integer, this is stored in the variable 'tempFPS', which is used to set the windows FPS (in Hz).


36: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, here we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

37: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):`` This controls when the display should close (if on the 'ome-Screen') or returning back to the previous window (typically the 'ome-Screen'), to do this you can press the 'x' at the top of the display, or by pressing 'ESC or ESCAPE' which is handy when in full-screen modes.

38: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:`` This if-statement controls if sound should be played or not based on the user's preference in 'Settings.py', the user's preference is stored when the program closes.

39: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)`` This line calls the subroutine; 'PlayClickSound' in 'SoundUtils.py', if the user has allowed sound to play in settings, then interacting with the display will cause the click sound to play; volume and other parameters for this subroutine are stored in the global variable 'self'.

40: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.

41: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:`` This line detects if any key is pressed on a keyboard, used when detecting events like pressing keys to navigate the GUIs or moving in-game.

42: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:`` This line of code is used as part of the activation for 'Devmode' which you activate by pressing SPACE 10 times. Here we are detecting is the SPACE key has been pressed and 'Devmode' is not already active.

43: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1`` This line increases the value of the variable 'Devmode' by 1. When the variable 'Devmode' is equal to 0, then 'Devmode' is activated.

44: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:`` Detects if the key 'q' is pressed (not case sensitive).

45: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)`` If the key 'q' is pressed, then we load up the secondary window in 'TkinterUtils.py', this, like 'Devmode' displays information about the running program. This feature may be deprecated at a later date, but this isn't clear yet. All the data the subroutine needs to access is sent through the parameter 'self' which is a global variable.

46: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:`` This line detects if the function key 'F11' has been pressed.

47: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)`` If the function key 'F11' has been pressed, then resize the display by toggling full-screen. (The 'F11' key is commonly assigned to this in other applications).

48: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:`` Detects if the key 'x' is pressed (NOT case sensitive).

49: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1`` This resets 'Devmode' to 1, turning the feature off. This can be used to cancel counting the number of spaces pressed too.


51: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")`` This calls the 'GetNormalCaption' subroutine in 'CaptionUtils.py', This tool takes values from the variable 'self', which stores lots of the global variables stored in the entire program, and also a second input which, in this case its "Achievements" is asked for, this is useful for allowing the user to know what GUI they are in. The variable 'self' is called when the player has activated 'Devmode', (by pressing SPACE 10 times), this brings up lots of details in the caption regarding what the program is doing and the resources its using.


53: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.


55: ``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)`` This line defines the dimensions of a rectangle in Pygame, in this case the rectangle will be drawn at (0, 0) (x, y) with a width of 1280 and a height of 90. (all values here are in pixels and (0, 0) (x, y) is the top-left corner of the GUI (so thats 90 pixels DOWN)).

56: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)`` This line draws a rectangle to the display with 'self.Display', the colour to fill the rectangle is the colour of the background to Pycraft (This is a setting the user can change in the GUI in 'Settings.py') with the dimensions of the previously created Pygame Rect object called; 'cover_Rect'.

57: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))`` This line takes the Pygame.surface object 'TitleFont' and draws it onto the window (stored in the variable 'self.Display', at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. The coordinates are (x, y).

58: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))`` This line takes the Pygame.surface object 'AchievementsFont' and draws it onto the window (stored in the variable 'self.Display'), at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. We also add an offset of 55 pixels to make sure the two titles don't overlap.


60: ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)`` This line calls the subroutine 'CreateDevmodeGraph', this subroutine is responsible for drawing the graph you see at the top-right of most Pycraft GUI's. It takes the variable 'self' as a parameter, this code will return any errors, which are stored in the variable 'Message'. If there are no errors then the subroutine will return 'None'. The second parameter 'DataFont' is the currently loaded font which is used for rendering the text at the top of the graph.

61: ``¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:`` This line detects if there are any errors stored in the variable 'Message'. All important errors are stored in this variable. This error detection may be moved to a thread at a later date.

62: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

63: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

64: ``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)`` This line of code controls how fast the GUI should refresh, defaulting to the user's preference unless the window is minimised, in which case its set to 15 FPS. All values for FPS are in (Hz) and this line of code specifies the maximum FPS of the window, but this does not guarantee that FPS.

65: ``¬ ¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

66: ``¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

67: ``¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

68: ``¬ print("You need to run this as part of Pycraft")`` if the user is running the code from PyPi, or as a raw “.py” file then this will be outputted to the terminal, however uses of the compiled “.exe” editions will not see this. This code is also printed first in-case the code below fails.

69: ``¬ import tkinter as tk`` Now we are importing the tkinter module into the project, all code here must be standalone and not rely on code in other modules in the project, this way the project can be taken apart and this should still work. We store he imported module, “Tkinter” with the name``tk``, this shortens length and all references to “Tkinter” from how on in this indented block will use this name.

70: ``¬ from tkinter import messagebox`` Here we are importing specific sections of “Tkinter”, in this case; messagebox, this module allows us to make dialogue boxes that are commonplace in Windows and Apple based devices.

71: ``¬ root = tk.Tk()`` This of code is required to make the dialogue box, which is what we want. This will create a window to the default size “Tkinter” has defined, and initialises the``messagebox`` module, which we want.

72: ``¬ root.withdraw()`` We use this code to hide the window that appears by using the previous root is the internal name for the window, as that is what the window created in the previous was stored in (as a variable).

73: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")`` Here we make our all to the``messagebox`` module, which has several pre-made dialogue boxes, we are using the``showerror`` pre-made dialogue box procedure here. We give it the caption of "Startup Fail", and then elaborate on the issue in the main body of the window, by displaying the text "You need to run this as part of Pycraft, please run the 'main.py' file".

74: ``¬ quit()`` This is Python’s way of closing the project, we normally use``sys.exit`` for this, which you will see later on, because its a bit cleaner on some IDLE’s and terminals. However to reduce the length of this project, we use the built in function here instead.

1: ``if not __name__ == "__main__":`` This checks to see if the place its called from (stored in the variable ``__name__``) is not ``"__main__"``. The string ``"__main__"`` would be the data stored in the variable ``__name__`` if the project was run on its own, which in this case we don't want so we only allow the code inside the if-statement to run if the data in ``__name__`` is not "__main__".

2: ``¬ print("Started <Pycraft_Base>")`` This line outputs only when the project is first called in 'main.py', if the code continues to print the next line then no syntax errors occurred when initialising this module.


4: ``¬ import moderngl_window as mglw`` Here we are importing the external module 'ModernGL_Window'. All calls to the module furthermore in this module will reference 'mglw'.

5: ``¬ from moderngl_window.scene.camera import KeyboardCamera, OrbitCamera`` Here we are importing specific classes and code from the module 'ModernGL_Window'. We do this because they may not be added by default when importing that external module as a whole.



8: ``¬ class CameraWindow(mglw.WindowConfig):`` Here we are creating a class called 'CameraWindow', we will reference this later on in the 'GameEngine.py', this class controls the basic window functionality of 'GameEngine.py'.

9: ``¬ ¬ """Base class with built in 3D camera support"""`` 


11: ``¬ ¬ def __init__(self, **kwargs):`` Here we are initialising the class by defining and assigning some key variables which will be used frequently in all ModernGL enabled windows.

12: ``¬ ¬ ¬ super().__init__(**kwargs)`` 

13: ``¬ ¬ ¬ self.camera = KeyboardCamera(self.wnd.keys, aspect_ratio=self.wnd.aspect_ratio)`` Here we setting the global variable self.camera to a specific ModernGL object, its important to note, references to 'self' in this module do not relate to the 'self' variable used in other programs. This line of code creates a camera object (which we use to move around and rotate in 'GameEngine.py'). This line of code also detects keypresses in ModernGL_window enabled GUI's ('GameEngine.py' mainly) and sets the aspect ratio. This setting is specified in 'GameEngine.py'.

14: ``¬ ¬ ¬ self.camera_enabled = True`` This line confirms that we are using the camera as our main view in 'GameEngine.py'.


16: ``¬ ¬ def key_event(self, key, action, modifiers):`` This line of code defines a subroutine that detects keypresses on Moderngl enabled GUIs. This acts similarly to 'pygame.event.get()'.

17: ``¬ ¬ ¬ keys = self.wnd.keys`` This line of code gets a list of the keys that are on a typical keyboard as well as their 'state', essentially this means if the key is pressed or not.


19: ``¬ ¬ ¬ if self.camera_enabled:`` This line controls wether to accept keyboard inputs or not from the camera.

20: ``¬ ¬ ¬ ¬ self.camera.key_input(key, action, modifiers)`` This line of code gets the keyboard inputs from the camera. Its here where the state of each key specified in the variable 'keys'.


22: ``¬ ¬ ¬ if action == keys.ACTION_PRESS:`` This line detects if a key is pressed (essentially 'event.type == pygame.KEYDOWN' for Pygame)

23: ``¬ ¬ ¬ ¬ if key == keys.C:`` This if-statement controls what to do if the 'C' key is pressed down.

24: ``¬ ¬ ¬ ¬ ¬ ¬ self.camera_enabled = not self.camera_enabled`` This line toggles if the camera is enabled or not, and thus where to get events from.

25: ``¬ ¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = self.camera_enabled`` This line controls wether the mouse should be hidden or not based on if the camera is enabled or not; (If the camera is enabled (so 'True') then the mouse will be hidden and if the camera is disabled (so 'False') then the mouse will show and be able to leave the window.

26: ``¬ ¬ ¬ ¬ ¬ ¬ self.wnd.cursor = not self.camera_enabled`` In some implementations of the game, a cursor may show like crosshair in game, this line toggles wether to show that or not, based on if the camera is enabled or not (So if the camera is enabled, therefore the mouse will be invisible and the cursor will take the control of the mouse).

27: ``¬ ¬ ¬ ¬ ¬ if key == keys.SPACE:`` Detects if the SPACE key is pressed.

28: ``¬ ¬ ¬ ¬ ¬ ¬ self.timer.toggle_pause()`` Controls wether to continue running the program, or to pause it until the SPACE key is pressed again. This works like pausing and unpausing a video.


30: ``¬ ¬ def mouse_position_event(self, x: int, y: int, dx, dy):`` This subroutine controls how the camera should move based on the movement of the mouse.

31: ``¬ ¬ ¬ if self.camera_enabled:`` This line controls wether to accept keyboard inputs or not from the camera.

32: ``¬ ¬ ¬ ¬ self.camera.rot_state(-dx, -dy)`` This line of code will move the camera based on a vector of mouse movement (direction and magnitude, so for example left 60 pixels, or right 10).


34: ``¬ ¬ def resize(self, width: int, height: int):`` This subroutine controls what to do if the window is resized.

35: ``¬ ¬ ¬ self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)`` This subroutine will set the aspect ratio of the project to make sure every pixel in the window is being used, this stops black/white bars forming around the window if it is resized and the aspect ratio's don't match.



38: ``¬ class OrbitCameraWindow(mglw.WindowConfig):`` This class 'OrbitCameraWindow' is used when the variable 'self.camera_enabled' is set to 'False'. This allows us to move about our 3D world but changes its behaviour slightly.

39: ``¬ ¬ """Base class with built in 3D orbit camera support"""`` 


41: ``¬ ¬ def __init__(self, **kwargs):`` Here we are initialising the class by defining and assigning some key variables which will be used frequently in all ModernGL enabled windows.

42: ``¬ ¬ ¬ super().__init__(**kwargs)`` 

43: ``¬ ¬ ¬ self.camera = OrbitCamera(aspect_ratio=self.wnd.aspect_ratio)`` Sets the camera to a different camera object from before. In this case we still take the same parameters for the aspect ratio of the camera, but negate 'self.wnd.keys' this time. This can be imagined as like setting the aspect ratio on the camera of a phone.

44: ``¬ ¬ ¬ self.camera_enabled = True`` This line confirms that we are using the camera as our main view in 'GameEngine.py'.


46: ``¬ ¬ def key_event(self, key, action, modifiers):`` This line of code defines a subroutine that detects keypresses on Moderngl enabled GUIs. This acts similarly to 'pygame.event.get()'.

47: ``¬ ¬ ¬ keys = self.wnd.keys`` This line of code gets a list of the keys that are on a typical keyboard as well as their 'state', essentially this means if the key is pressed or not.


49: ``¬ ¬ ¬ if action == keys.ACTION_PRESS:`` This line detects if a key is pressed (essentially 'event.type == pygame.KEYDOWN' for Pygame)

50: ``¬ ¬ ¬ ¬ if key == keys.C:`` This if-statement controls what to do if the 'C' key is pressed down.

51: ``¬ ¬ ¬ ¬ ¬ ¬ self.camera_enabled = not self.camera_enabled`` This line toggles if the camera is enabled or not, and thus where to get events from.

52: ``¬ ¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = self.camera_enabled`` This line controls wether the mouse should be hidden or not based on if the camera is enabled or not; (If the camera is enabled (so 'True') then the mouse will be hidden and if the camera is disabled (so 'False') then the mouse will show and be able to leave the window.

53: ``¬ ¬ ¬ ¬ ¬ ¬ self.wnd.cursor = not self.camera_enabled`` In some implementations of the game, a cursor may show like crosshair in game, this line toggles wether to show that or not, based on if the camera is enabled or not (So if the camera is enabled, therefore the mouse will be invisible and the cursor will take the control of the mouse).

54: ``¬ ¬ ¬ ¬ ¬ if key == keys.SPACE:`` Detects if the SPACE key is pressed.

55: ``¬ ¬ ¬ ¬ ¬ ¬ self.timer.toggle_pause()`` Controls wether to continue running the program, or to pause it until the SPACE key is pressed again. This works like pausing and unpausing a video.


57: ``¬ ¬ def mouse_position_event(self, x: int, y: int, dx, dy):`` This subroutine controls how the camera should move based on the movement of the mouse.

58: ``¬ ¬ ¬ if self.camera_enabled:`` This line controls wether to accept keyboard inputs or not from the camera.

59: ``¬ ¬ ¬ ¬ self.camera.rot_state(dx, dy)`` This line of code controls the rotation of the camera, but instead inverts the vector (so instead of panning left before, you'd now be panning right). This is still controlled by the movement of the mouse.


61: ``¬ ¬ def mouse_scroll_event(self, x_offset: float, y_offset: float):`` This line of code created a subroutine 'mouse_scroll_event' which is used to handle what to do if the user scrolls the scroll-wheel of their mouse.

62: ``¬ ¬ ¬ if self.camera_enabled:`` This line controls wether to accept keyboard inputs or not from the camera.

63: ``¬ ¬ ¬ ¬ self.camera.zoom_state(y_offset)`` This line zooms the camera in and out based on the amount the user turns the scroll-wheel. This can be imagined as zooming in on a camera, or looking through the scope of a gun in a game.


65: ``¬ ¬ def resize(self, width: int, height: int):`` This subroutine controls what to do if the window is resized.

66: ``¬ ¬ ¬ self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)`` This subroutine will set the aspect ratio of the project to make sure every pixel in the window is being used, this stops black/white bars forming around the window if it is resized and the aspect ratio's don't match.

1: ``if not __name__ == "__main__":`` This checks to see if the place its called from (stored in the variable ``__name__``) is not ``"__main__"``. The string ``"__main__"`` would be the data stored in the variable ``__name__`` if the project was run on its own, which in this case we don't want so we only allow the code inside the if-statement to run if the data in ``__name__`` is not "__main__".

2: ``¬ print("Started <Pycraft_Benchmark>")`` Now we output data to the terminal if the program is running, this allows us to know if there are any errors preventing this module from loading, in which case the program would crash before that is outputted to the terminal, making us aware the error is in this module.

3: ``¬ class GenerateBenchmarkMenu:`` Now we are defining a class with a suitable name that represents what the subroutines in this class do; this allows us to group up our code to make it easier to edit, organise and debug later on, as well as saving on memory as not every function will need to be loaded at once.

4: ``¬ ¬ def __init__(self):`` Here we make sure the module is initialized correctly we do this because if we tried to call this standalone, and without the code that would stop this, then all references to variables and subroutines outside of this project would be invalid and cause issues. This is also where the variable ‘self’ is defined for all references in this class. This subroutine is a procedure, so does not return a value.

5: ``¬ ¬ ¬ pass`` Here we tell python to ignore the previous line of code that expects indented code, we use this if we don't need to put any code in this indent, this should be avoided in most situations. This is mainly used in the ``__init__`` functions for Pycraft where we may not need to run any code, but need to make sure the module is working correctly.


7: ``¬ ¬ def Benchmark(self):`` This line creates the subroutine that creates and does the majority of the processing for the Benchmark GUI, it takes only the parameter 'self' and returns either 'None' or an error in the 'Message' variable should one occur.

8: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

9: ``¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).pause()`` This line stops the sound in channel 2 from playing by pausing it, this sound is the background track that plays when not in game (This is controlled by the user's setting). If no sound is playing then this has no effect.

10: ``¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

11: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

12: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark")`` Here we update the cation of the window from the previous caption to this. The variable 'self.version' is defined at the start of the program in 'main.py'.

13: ``¬ ¬ ¬ ¬ ¬ self.VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Here we load the project's default from from the fonts folder (it's 'Book Antiqua'), we store this in the variable 'self.VersionFont'. We set the font's size here to 20

14: ``¬ ¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 60.

15: ``¬ ¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 35.

16: ``¬ ¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 15.

17: ``¬ ¬ ¬ ¬ ¬ DetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)`` Here we load the project's default from from the fonts folder (it's 'Book Antiqua'), we store this in the variable 'DetailsFont'. We also set it's size to 20.

18: ``¬ ¬ ¬ ¬ ¬ InfoDetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Here we load the project's default from from the fonts folder (it's 'Book Antiqua'), we store this in the variable 'InfoDetailsFont'. We also set it's size to 15.

19: ``¬ ¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)`` Takes the font, which we stored in the variable 'MainTitleFont' and uses it to render the text "Pycraft", with the user's preference on anti-aliasing, 'aa' and the colour defined in 'ThemeUtils.py', the resulting Pygame.surface object is stored in the variable 'TitleFont'.

20: ``¬ ¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()`` Gets the width (in pixels) of the Pygame.surface object 'TitleFont


22: ``¬ ¬ ¬ ¬ BenchmarkFont = InfoTitleFont.render("Benchmark", self.aa, self.SecondFontCol)`` Here we are creating a Pygame.surface object with the text 'Benchmark', we also set the anti-aliasing to the user's preference (which can be changed in settings), and set the font's colour to the secondary font colour, defined in 'ThemeUtils.py'. We store the Pygame.surface object in the variable 'BenchmarkFont'.

23: ``¬ ¬ ¬ ¬ ¬ FPSinfoTEXT = DetailsFont.render("FPS benchmark results", self.aa, self.FontCol)`` Here we are creating a Pygame.surface object using the font 'DetailsFont', which we loaded earlier. We render the text 'FPS benchmark results' to this, setting anti-aliasing to the user's preference (defined in 'Settings.py') and setting the colour to the primary font colour defined in 'ThemeUtils.py', which can be changed by the user.

24: ``¬ ¬ ¬ ¬ ¬ FPSinfoTEXTWidth = FPSinfoTEXT.get_width()`` On this line we get the width (in pixels) of the Pygame.surface object FPSinfoTEXT. We store the resulting number in the variable 'FPSintoTEXTWidth'.

25: ``¬ ¬ ¬ ¬ ¬ FILEinfoTEXT = DetailsFont.render("Read test results", self.aa, self.FontCol)`` Here we are rendering the text 'Read test results' with the font 'DetailsFont', which we loaded earlier. As with most font rendering we also set the anti-aliasing to the user's preference (which can be changed in settings), and the colour to the colour argument in the variable 'FILEinfoTEXT'

26: ``¬ ¬ ¬ ¬ ¬ FILEinfoTEXTWidth = FILEinfoTEXT.get_width()`` Here we are getting the length (in pixels) of the Pygame.surface object 'FILEinfoTEXT', this will be used to calculate where to place the text on the window.

27: ``¬ ¬ ¬ ¬ ¬ HARDWAREinfoTEXT = DetailsFont.render("Hardware results", self.aa, self.FontCol)`` Here we are rendering the text 'Hardware results' using the font we loaded earlier; 'DetailsFont'. We also use the user's preference in anti-aliasing and use the appropriate colour scheme from the theme the user has selected. We store this in the variable 'HARDWAREinfoTEXT'.

28: ``¬ ¬ ¬ ¬ ¬ HARDWAREinfoTEXTwidth = HARDWAREinfoTEXT.get_width()`` Here we are getting the width (in pixels) of the Pygame.surface object HARDWAREinfoTEXT. This is used in making sure the text is drawn to the window in the appropriate position.


30: ``¬ ¬ ¬ ¬ SixtyFPSData = DataFont.render("60 Hz", self.aa, self.AccentCol)`` Here we are rendering the text '60 Hz' using the font 'DataFont', and the suer's preference on anti-aliasing (which is defined in 'Settings.py') and the appropriate colour from the user's selected theme. This is stored in the variable 'SixtyFPSData', this acts as a marker on the graph of where 60 FPS lies (FPS is measured in Hz).

31: ``¬ ¬ ¬ ¬ ¬ OneFourFourFPSData = DataFont.render("144 Hz", self.aa, self.AccentCol)`` Here we are rendering the text '144 Hz' using the font 'DataFont', and the user's preference on anti-aliasing (which is defined in 'Settings.py') and the appropriate colour from the user's selected theme. This is stored in the variable 'OneFourFourFPSData', this acts as a marker on the graph of where 144 FPS lies (FPS is measured in Hz).

32: ``¬ ¬ ¬ ¬ ¬ TwoFortyFPSData = DataFont.render("240 Hz", self.aa, self.AccentCol)`` Here we are rendering the text '240 Hz' using the font 'DataFont', and the user's preference on anti-aliasing (which is defined in 'Settings.py') and the appropriate colour from the user's selected theme. This is stored in the variable 'TwoFortyFPSData', this acts as a marker on the graph of where 240 FPS lies (FPS is measured in Hz).


34: ``¬ ¬ ¬ ¬ InfoFont1 = DataFont.render("Welcome to Benchmark mode, press the SPACE bar to continue or press ANY other key to cancel, or press 'X'", self.aa, self.FontCol)`` Here we are giving the user instructions on how to use benchmark mode, telling them they can cancel the benchmark at any time by pressing any key. We store the resulting Pygame.surface output from this function in the variable 'InfoFont1'. In addition we use the user's choice on anti-aliasing and choose an appropriate colour from the user's selected theme.

35: ``¬ ¬ ¬ ¬ ¬ InfoFont2 = DataFont.render("Benchmark mode is used to make the 'ADAPTIVE' feature in settings function and also to give an indication of the experience you are likely to get on this device", self.aa, self.FontCol)`` Here we are giving the user details on what the benchmark mode can be used for, we render this text with the user's preference on anti-aliasing and choose a suitable colour from their theme. We store the output from this in 'InfoFont2'.

36: ``¬ ¬ ¬ ¬ ¬ InfoFont3 = DataFont.render("Benchmark mode consists of several stages:", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. This is given over several lines as Pygame doesn't wrap text to the edge of the window, which is one reason why the user cannot use a resolution lower than (1280x720), because in some cases text would be rendered off the screen. We will always respect the user's colour scene and anti-aliasing preferences here.

37: ``¬ ¬ ¬ ¬ ¬ InfoFont4 = DataFont.render("First it will gather some basic information about your system", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences here.

38: ``¬ ¬ ¬ ¬ ¬ InfoFont5 = DataFont.render("Then it will test your maximum frame rate on a blank screen, then with a basic animation, and finally in a 3D OpenGL space", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences here.

39: ``¬ ¬ ¬ ¬ ¬ InfoFont6 = DataFont.render("After its done that the focus moves on to a quick storage test, before finishing", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences here.

40: ``¬ ¬ ¬ ¬ ¬ InfoFont7 = DataFont.render("Your results will then be displayed on screen with your frame rate scores on a line graph and the rest detailed to the right", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences here.

41: ``¬ ¬ ¬ ¬ ¬ InfoFont8 = DataFont.render("During the time the benchmark is running the window may appear unresponsive, don't panic this can be expected.", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences here.

42: ``¬ ¬ ¬ ¬ ¬ InfoFont9 = DataFont.render("In addition to achieve the best scores try to avoid doing anything else on the computer whilst the benchmark runs", self.aa, self.FontCol)`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preference's here.

43: ``¬ ¬ ¬ ¬ ¬ InfoFont10 = DataFont.render("This benchmark may show some system instability or cause your device to get warm, you use this at your own risk!", self.aa, (255, 0, 0))`` Here we are giving details on how the program works to the user. We will always respect the user's colour scene and anti-aliasing preferences here.


45: ``¬ ¬ ¬ ¬ stage = 0`` Here we are setting the user's 'stage', this essentially tells controls which step of the process should be processed and rendered. With the completion of each 'stage', it is incremented by 1.


47: ``¬ ¬ ¬ ¬ resize = False`` This prevents the display from being resized during the tests, as resizing the display can alter the results, and when in full-screen, Pygame does some hardware acceleration to further improve performance, so you could get contrasting results.


49: ``¬ ¬ ¬ ¬ while True:`` Enters the project's game loop

50: ``¬ ¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()`` Gets the width and height of the current Pygame window (in pixels), this is used in working out where everything should be scaled in-game if the window is resized.


52: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:`` Detects if the window has been made smaller than the minimum width, 1280 pixels

53: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)`` If the window is smaller than 1280 pixels, then reset the display's WIDTH to 1280. There is no limit to how large the display can be.

54: ``¬ ¬ ¬ ¬ ¬ ¬ if realHeight < 720:`` Detects if the window has been made smaller than the minimum height, 720 pixels

55: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)`` If the window is smaller than 720 pixels, then reset the display's HEIGHT to 720. There is no limit to how large the display can be.


57: ``¬ ¬ ¬ ¬ ¬ if stage == 0:`` Here we are starting the benchmark process by checking to see if the value of 'stage' is 0, if it is then we run the code allocated to that section.

58: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

59: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)`` This line defines the dimensions of a rectangle in Pygame, in this case the rectangle will be drawn at (0, 0) (x, y) with a width of 1280 and a height of 90. (all values here are in pixels and (0, 0) (x, y) is the top-left corner of the GUI (so thats 90 pixels DOWN)).

60: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)`` This line draws a rectangle to the display with 'self.Display', the colour to fill the rectangle is the colour of the background to Pycraft (This is a setting the user can change in the GUI in 'Settings.py') with the dimensions of the previously created Pygame Rect object called; 'cover_Rect'.

61: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))`` This line takes the Pygame.surface object 'TitleFont' and draws it onto the window (stored in the variable 'self.Display', at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. The coordinates are (x, y).

62: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))`` Here we are rendering the Pygame.surface object 'BenchmarkFont' to our display, setting its position (in pixels) to just off centre so it doesn't overlap with the title.

63: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont1, (3, 100))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.

64: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont2, (3, 130))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so

65: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont3, (3, 145))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so

66: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont4, (3, 160))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so

67: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont5, (3, 175))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.

68: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont6, (3, 190))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.

69: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont7, (3, 220))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.

70: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont8, (3, 235))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.

71: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont9, (3, 250))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.

72: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(InfoFont10, (3, 280))`` Here we are rendering the paragraph of previously loaded text, with each line increasing the position down so the paragraph is properly loaded.


74: ``¬ ¬ ¬ ¬ ¬ if stage == 1:`` This if-statement detects if the previous stage has been completed, and will move the user on-to the next section. 

75: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Getting System Information")`` Here we are setting the caption of the display to appropriately tell the user what the program is doing at this stage.

76: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ CPUid = f"{self.mod_CPUinfo__.get_cpu_info()['brand_raw']} w/{self.mod_Psutil__.cpu_count(logical=False)} cores @ {self.mod_Psutil__.cpu_freq().max} MHz"`` Here we are getting the information for the hardware of the system. This will be rendered later, so we format it into a way the user will understand. 'self.mod_CPUinfo__.get_cpu_info()["brand_raw"]' gets the make of the CPU (typically 'AMD' or 'Intel') as well as the model; for example, if I was running an 'AMD Ryzen 7 5700x', then that is what that subroutine would return. 'self.mod_Psutil.cpu_count(logical=False)' gives us the number of cores the CPU has, this is the same number that should appear in system information. 'self.mod_Psutil__.cpu_freq().max' returns the maximum factory clock speed of your CPU (In MHz).

77: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ RAMid = f"{round((((self.mod_Psutil__.virtual_memory().total)/1000)/1000/1000),2)} GB of memory, with {self.mod_Psutil__.virtual_memory().percent}% used"`` Here we are getting the details of the user's RAM, and formatting it appropriately so this can be rendered to text later on without additional processing. 'self.mod_Psutil__.virtual_memory().total' gets the amount of physical memory installed in your machine that the program can access (This does NOT include hardware reserved memory), we are also converting this output from bytes to gigabytes, or this would be a really big number and not very readable. 'self.mod_Psutil__.virtual_memory().percent' returns the amount of memory allocated to other tasks on the system.

78: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFO = DataFont.render(CPUid, self.aa, (255, 255, 255))`` Here we are converting the variable 'CPUid', which is a string, into a Pygame.surface object, respecting the user's preference on anti-aliasing, but forcing the colour to white (which is a bug, this will be fixed in Pygame v0.9.4). The resulting Pygame.surface object is stored in the variable 'CPUhwINFO', which is abbreviated from 'CPU-hardware-information'.

79: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ CPUhwINFOwidth = CPUhwINFO.get_width()`` Here we are getting the width (in pixels) of the Pygame.surface object; 'CPUhwINFO'. This will be used to help appropriately place the text later on.


81: ``¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFO = DataFont.render(RAMid, self.aa, (255, 255, 255))`` Here we are rendering the system information we gathered for RAM, rendering the formatted tet respecting the user's preference on anti-aliasing and setting the colour to white (this is a bug, this will be fixed in the next update to Pycraft).

82: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ RAMhwINFOwidth = RAMhwINFO.get_width()`` Here we are getting the width (in pixels) of the Pygame.surface object we have just created; 'RAMhwINFO'.

83: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ stage += 1`` Now we are finished with the current stage so increment the stage variable by 1, and more on forwards to the next stage.


85: ``¬ ¬ ¬ ¬ ¬ if stage == 2:`` Here we are detecting if the integer stored in the variable 'stage' is equal to 2, in which case we do this stage.

86: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

87: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Message, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3 = self.mod_ExBenchmark__.LoadBenchmark.run(self)`` Here we are running a benchmark in 'ExBenchmark' (short for 'ExternalBenchmark'), and once this has completed, receiving the results of the subroutine through the 7 variables. This subroutine takes only the global variable self, and outputs 7 pieces of data, if completed successfully. 'Message' is a string, this stores any errors that may occur when running the subroutine. 'FPSlistX', 'FPSlistX2' and 'FPSlistx3' each store the 'x' coordinate for the graph, which we will draw later. Each of these lists contains a sequence of numbers, going up in 1's for the framerate of each frame of the benchmark. 'FPSlistY', 'FPSlistY1' and 'FPSlistY2' store the results of each of the three benchmarks running, 'FPSlistY' stores the blank window test, 'FPSlistY2' stores the result of the 2D graphics test, and 'FPSlistY3' stores the 3D render results.

88: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:`` This line detects if there are any errors stored in the variable 'Message'. All important errors are stored in this variable. This error detection may be moved to a thread at a later date.

89: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

90: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)`` Here we are creating our Pygame display through the subroutine 'SetDisplay' in 'DisplayUtils.py'. All the parameters for this subroutine are sent through the variable 'self'.

91: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ except:`` (This needs updating to follow the guidelines of the documentation) This ignores any errors that may occur when running the main section of the benchmark, or in creating our Pygame window.

92: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Cancelled benchmark")`` If an error does occur, then here we set the caption appropriately to let the user know the benchmark has been cancelled.

93: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.

94: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

95: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Finished self.FPS based benchmarks")`` Here we are setting the caption appropriately if the benchmark finished successfully, telling the user that (There is a noticeable bug here, this will be fixed) the program has 'Finished FPS based benchmarks'. We need to specifically say 'FPS based' here as there is also a drive test next.

96: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ stage += 1`` Now we are finished with the current stage so increment the stage variable by 1, and more on forwards to the next stage.


98: ``¬ ¬ ¬ ¬ ¬ if stage == 3:`` If stage 2 has finished without errors, then we move onto this stage.

99: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Starting disk read test")`` Here we update the Pygame window's caption with 'Starting disk read test' to tell the user that the benchmark has moved on to another stage.

100: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ReadIteration = 50`` Here we set the number of times a file should be read, in this case we need to read the file 50 times. The more reads the greater accuracy of the result.

101: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ for i in range(ReadIteration):`` Here we start a for-loop that will repeat for the number of times we want the read test to be repeated.

102: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:`` Then we open the file we want to read from...

103: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Benchdata = Bench.read()`` We read the entire file and store the contents in the variable 'Benchdata'.


105: ``¬ ¬ ¬ ¬ ¬ ¬ aTime = 0`` Now we perform the test again, except this time we are recording the time taken, the previous test is designed more to prepare drives and 'wake then up' if they are idling or have stopped (which can drastically change the results of the test). Here we are setting the timer to 0 as this is the start of the test.

106: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ReadIteration = 50`` Here we set the number of times a file should be read, in this case we need to read the file 50 times. The more reads the greater accuracy of the result.

107: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ for i in range(ReadIteration):`` Here we start a for-loop that will repeat for the number of times we want the read test to be repeated.

108: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ start = self.mod_Time__.perf_counter()`` Here we are getting a very accurate value for the time the system is at (in small fractions of a second), and storing that time in the variable 'start'.

109: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:`` Then we open the file we want to read from...

110: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Benchdata = Bench.read()`` We read the entire file and store the contents in the variable 'Benchdata'.

111: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ aTime += self.mod_Time__.perf_counter()-start`` Then we are adding the time delta (difference) between the current time and the time before we opened and read the file, this gives is an indication of how long the process took (the faster the drive, typically the less time this test takes).

112: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ aTime = aTime/(ReadIteration+1)`` here we are working out the average time each read took, as repeating the experiment gives us a more accurate result, 'aTime' is abbreviated from 'averageTime'. This is a mean average (possible bug here; remove the '+1').

113: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ReadSpeed = (1/(aTime))`` Here we are calculating the number of files the drive can read in the average time we just calculated (time is in seconds, but will likely be a very small decimal). The file is just over 1 MB in size (Make this size 1 MB not 1.024 MB for later versions), so by using this calculation we can calculate how many megabytes-per-second the drive can read at, this is very rough and not very accurate, but it seems the easiest was to get current drive performance (I'm open to better solutions).

114: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ stage += 1`` Now we are finished with the current stage so increment the stage variable by 1, and more on forwards to the next stage.


116: ``¬ ¬ ¬ ¬ ¬ ¬ if stage == 4:`` Here we are, if the integer stored in the variable 'stage' is equal to 4, moving on to the next stage of the benchmark process.

117: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results.")`` We suitably update the caption to indicate we have moved on to the next stage, we use full-stops at the end of the caption here to indicate how through this process we are, as this stage takes a reasonably long time relative to the previous stage.

118: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Max1 = 0`` Here we are setting the maximum value for the blank window benchmark to 0, as the lowest FPS is 15, this number can be any number less than 15.

119: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Min1 = 60`` We set the minimum value for the blank image benchmark to 60, as this is an easily reachable target, this value cannot be lower than 15 as then that would be always smaller than the lowest FPS, both this and the previous variable must also be greater than 0.

120: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):`` Now we iterate over the frame-rate for the blank window benchmark.

121: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY[i] > Max1:`` If the value (FPS in Hz) of the element at position 'i' (where 'i' is abbreviated from 'iteration and is an integer that counts upwards from 0, this is used an an index for this list of values) is greater than the known maximum (so if the value of 'FPSlistY' is greater than, but NOT equal to the previously largest FPS)...

122: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max1 = FPSlistY[i]`` Then we set the new value of the variable 'Max1' to the current -larger- value in the list.

123: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY[i] < Min1:`` If the value stored at the current location is less than the previously known minimum...

124: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min1 = FPSlistY[i]`` Then we set the minimum value to the current value of the list.


126: ``¬ ¬ ¬ ¬ ¬ ¬ Max2 = 0`` Here we are defining the maximum value for the 2D render test.

127: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Min2 = 60`` Here we are defining the minimum value for the 2D render test, these values are chosen to be easily beatable, so that the minimum and maximum values of the data can be accurately recorded.

128: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):`` Now we iterate over the frame-rate (in Hz) for the results of the 2D render test.

129: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY2[i] > Max2:`` If the value (FPS in Hz) of the element at position 'i' (where 'i' is abbreviated from 'iteration and is an integer that counts upwards from 0, this is used an an index for this list of values) is greater than the known maximum (so if the value of 'FPSlistY1' is greater than, but NOT equal to the previously largest FPS)... 

130: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max2 = FPSlistY2[i]`` Then we set the new value of the variable 'Max2' to the current -larger- value in the list 'FPSlistY2'.

131: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY2[i] < Min2:`` If the value stored at the current location is less than the previously known minimum...

132: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min2 = FPSlistY2[i]`` Then we set the minimum value to the current value of the list.


134: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results..")`` Now we have gone through roughly hald the data processing so can update the caption by adding another '.'...

135: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Max3 = 0`` Here we are defining the maximum value for the 3D render test.

136: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ Min3 = 60`` Here we are defining the minimum value for the 3D render test, these values are chosen to be easily beatable, so that the minimum and maximum values of the data can be accurately recorded.

137: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY3)):`` Now we iterate over the frame-rate (in Hz) for the results of the 3D render test.

138: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY3[i] > Max3:`` If the value (FPS in Hz) of the element at position 'i' (where 'i' is abbreviated from 'iteration' and is an integer that counts upwards from 0, this is used an an index for this list of values) is greater than the known maximum (so if the value of 'FPSlistY3' is greater than, but NOT equal to the previously largest value)...

139: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Max3 = FPSlistY3[i]`` Then we set the new value of the variable 'Max3' to the current -larger- value in the list 'FPSlistY3'.

140: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if FPSlistY3[i] < Min3:`` If the value stored at the current location is less than the previously known minimum...

141: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Min3 = FPSlistY3[i]`` Then we set the minimum value to the current value of the list.


143: ``¬ ¬ ¬ ¬ ¬ ¬ if Max2 > Max1:`` Now we are checking to see which one of the three values is larger, this is done so we know what we need to make the graph go up to when we display the results in a line graph.

144: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max2`` The variable 'GlobalMax' will be assigned the larger of the two values 'Max1' and 'Max2'.

145: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ elif Max3 > Max2:`` Then we check to see if the maximum value in the 3D render benchmark is greater than the maximum for the 2D render test.

146: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max3`` If the 3D render benchmark produced the highest framerate (unlikely) then we set the maximum value to that number in the variable 'GlobalMax'.

147: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

148: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ GlobalMax = Max1`` If all the preceding if-statements are false, the largest value must be in the variable 'max1', so that is what we store in the variable; 'GlobalMax'.


150: ``¬ ¬ ¬ ¬ ¬ ¬ self.RecommendedFPS = GlobalMax/2`` We calculate the 'recommended' frame rate by taking half of the largest FPS, this is because the highest frame-rates are not either recommended because of unnecessary CPU/GPU load and because the frame-rate slider in 'Settings.py' maxes out at 445.


152: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results...")`` Now we move on to the next section of processing, because we haven't yet finished, in this section we will now make sure that all the values from the three benchmarks fit onto the display appropriately.

153: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ multiplier = len(FPSlistY)/(realWidth-20)`` This variable 'multiplier' controls how the line graph is drawn on the 'x' axis, without this our graph could easily stretch off the display, this also controls how far apart each of the 'points' are on the line graphs, we do this by taking the length of 'FPSlistY', it doesn't matter which one we choose because they are all the same length, then we divide that by the width of the display 'realWidth' (in pixels) which has had 20 pixels taken off of, we take 20 pixels off the variable 'realWidth' so that the graph can be centered with a 10 pixel border between the two sides, we do this so that it looks more appealing visually.

154: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ temp = []`` Now we create a temporary blank array, these 'temp' variables are simply there to store data whilst it is being processed, the data should be moved to an appropriately named array once this processing has finished.

155: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):`` Now we iterate over the frame-rate for the blank window benchmark.

156: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY[i])))`` ow we are iterating over each element in the black render test (which has the results stored in the variable 'FPSlistY'), we are taking the original value and converting it to a smaller value that is still representative, and will look the same on the graph, but will fit onto the area we have assigned the graphing to be. Not doing this step could result in the line graphs not fitting on-screen and being rendered upside-down. In order of processing; we divide 300 (the HEIGHT of the graphing area) by the 'GlobalMax', which stores the largest number that appears in all of the tests, this makes sure that none of the values are rendered outside of the graph. Then we multiply this by the current value of 'FPSlistY' as we iterate over the array. Then we take the result and flip it by taking it away from 300, this step is done because the larger the value the lower down the display it would have been drawn, mirroring the result, and making it really hard to interpret. Finally we offset the entire result by moving it down the display 130 pixels to allow for titles and subheadings above.

157: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSListY = temp`` Now we are taking the array stored in temp and moving it to the variable 'FPSlistY', which is more appropriately named.


159: ``¬ ¬ ¬ ¬ ¬ ¬ temp = []`` Now we create a temporary blank array, these 'temp' variables are simply there to store data whilst it is being processed, the data should be moved to an appropriately named array once this processing has finished.

160: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):`` Now we iterate over the frame-rate (in Hz) for the results of the 2D render test.

161: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY2[i])))`` Now we are iterating over each element in the black render test (which has the results stored in the variable 'FPSlistY'), we are taking the original value and converting it to a smaller value that is still representative, and will look the same on the graph, but will fit onto the area we have assigned the graphing to be. Not doing this step could result in the line graphs not fitting on-screen and being rendered upside-down. In order of processing; we divide 300 (the HEIGHT of the graphing area) by the 'GlobalMax', which stores the largest number that appears in all of the tests, this makes sure that none of the values are rendered outside of the graph. Then we multiply this by the current value of 'FPSlistY2' as we iterate over the array. Then we take the result and flip it by taking it away from 300, this step is done because the larger the value the lower down the display it would have been drawn, mirroring the result, and making it really hard to interpret. Finally we offset the entire result by moving it down the display 130 pixels to allow for titles and subheadings above.

162: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSListY2 = temp`` Now we are taking the array stored in temp and moving it to the variable 'FPSlistY2', which is more appropriately named.


164: ``¬ ¬ ¬ ¬ ¬ ¬ temp = []`` Now we create a temporary blank array, these 'temp' variables are simply there to store data whilst it is being processed, the data should be moved to an appropriately named array once this processing has finished.

165: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):`` Now we iterate over the frame-rate (in Hz) for the results of the 2D render test.

166: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ temp.append(130+(300-((300/GlobalMax)*FPSlistY3[i])))`` Now we are iterating over each element in the black render test (which has the results stored in the variable 'FPSlistY3'), we are taking the original value and converting it to a smaller value that is still representative, and will look the same on the graph, but will fit onto the area we have assigned the graphing to be. Not doing this step could result in the line graphs not fitting on-screen and being rendered upside-down. In order of processing; we divide 300 (the HEIGHT of the graphing area) by the 'GlobalMax', which stores the largest number that appears in all of the tests, this makes sure that none of the values are rendered outside of the graph. Then we multiply this by the current value of 'FPSlistY3' as we iterate over the array. Then we take the result and flip it by taking it away from 300, this step is done because the larger the value the lower down the display it would have been drawn, mirroring the result, and making it really hard to interpret. Finally we offset the entire result by moving it down the display 130 pixels to allow for titles and subheadings above.

167: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSListY3 = temp`` Now we are taking the array stored in temp and moving it to the variable 'FPSlistY3', which is more appropriately named.


169: ``¬ ¬ ¬ ¬ ¬ ¬ Results1 = []`` Here we are creating an empty array and storing it in the variable 'Results1'

170: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY)):`` Now we iterate over the frame-rate for the blank window benchmark.

171: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Results1.append([(FPSlistX[i]/multiplier), FPSListY[i]])`` Here we are grouping the two separate sets of data, the scores which we just iterated over and reformatted, and the sequence of elements in 'FPSlistX' that go up in the order (n). Here we are appropriately formatting the current value for 'FPSlistX' with the variable 'multiplier', as we where before, and also additionally combining it with the current re-formatted score stored in 'FPSlistY', this creates an array of points (x, y) (in pixels), that we can enter into a sub-routine later on to appropriately draw the corresponding line.


173: ``¬ ¬ ¬ ¬ ¬ ¬ Results2 = []`` Here we are creating an empty array and storing it in the variable 'Results2'

174: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY2)):`` Now we iterate over the frame-rate (in Hz) for the results of the 2D render test.

175: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Results2.append([(FPSlistX2[i]/multiplier), FPSListY2[i]])`` Here we are grouping the two separate sets of data, the scores which we just iterated over and reformatted, and the sequence of elements in 'FPSlistX' that go up in the order (n). Here we are appropriately formatting the current value for 'FPSlistX2' with the variable 'multiplier', as we where before, and also additionally combining it with the current re-formatted score stored in 'FPSlistY2', this creates an array of points (x, y) (in pixels), that we can enter into a sub-routine later on to appropriately draw the corresponding line.


177: ``¬ ¬ ¬ ¬ ¬ ¬ Results3 = []`` Here we are creating an empty array and storing it in the variable 'Results3'

178: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ for i in range(len(FPSlistY3)):`` Now we iterate over the frame-rate (in Hz) for the results of the 3D render test.

179: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ Results3.append([(FPSlistX3[i]/multiplier), FPSListY3[i]])`` Here we are grouping the two separate sets of data, the scores which we just iterated over and reformatted, and the sequence of elements in 'FPSlistX3' that go up in the order (n). Here we are appropriately formatting the current value for 'FPSlistX3' with the variable 'multiplier', as we where before, and also additionally combining it with the current re-formatted score stored in 'FPSlistY3', this creates an array of points (x, y) (in pixels), that we can enter into a sub-routine later on to appropriately draw the corresponding line.


181: ``¬ ¬ ¬ ¬ ¬ ¬ stage += 1`` Now we are finished with the current stage so increment the stage variable by 1, and more on forwards to the next stage.


183: ``¬ ¬ ¬ ¬ ¬ if stage == 5:`` Now we can, if the value of 'stage' is 5, move on to the next step in 'Benchmark.py'.

184: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Results")`` Here we are updating the caption appropriately to indicate to the user that the previous stage is finished.


186: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.


188: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))`` This line takes the Pygame.surface object 'TitleFont' and draws it onto the window (stored in the variable 'self.Display', at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. The coordinates are (x, y).

189: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))`` Here we are rendering the Pygame.surface object 'BenchmarkFont' to our display, setting its position (in pixels) to just off centre so it doesn't overlap with the title.


191: ``¬ ¬ ¬ ¬ ¬ ¬ FPSRect = self.mod_Pygame__.Rect(10, 130, realWidth-20, 300)`` here we are creating the background for the graph, this line of code defines the vertexes and position on-screen of that rectangle, and stores the resulting object in the variable 'FPSRect'. The first and second values are fixed, these are the (x,y) coordinates (in pixels) of the top-left corner of the rectangle. The next two values are width and height, in this case we want the rectangle to be the same lenth as the display (-20 pixels to create a border like we mentioned earlier), the height is also fixed at 300 pixels, this makes processing the positions of each point on the line graphs easier.

192: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FPSRect, 0)`` Here we are drawing the rectangle we just defined the dimension for in the variable 'FPSRect' to the display. 'self.Display' is our variable that corresponds to the Pygame window, 'self.ShapeCol' is a tuple of RGB values that control the colour of the rectangle, this is based on the user's currently active theme. '0' defines that the rectangle should be filled.


194: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*60)))), (realWidth-20, int(130+(300-((300/GlobalMax)*60)))))`` Here we are drawing one of the lines that acts as markers to show where a key frame-rate lies, in this case thats 60 FPS (in Hz). We draw it to the display (using the variable that represents that 'self.Display'), set the colour of the line to a suitable colour in the user's selected theme. Then we are defining 2 coordinates (x,y) for the start and end of the line. This function only takes 2 points, the first '(10, int(130+(300-((300/GlobalMax)*60))))' sets the 'x' position to be 10 (pixels), this is the same value as the x position of the shape 'FPSRect' deliberately, both of the 'y' positions are the same, we run the same calculation as earlier, except instead of iterating over an array to get the value, we manually set it to 60. The final 'x' value is the same as the width of the 'FPSRect' shape we defined earlier, again this is deliberate.

195: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(SixtyFPSData, (13, int(130+(300-((300/GlobalMax)*60)))))`` Here we are adding a label, which will go just above the line we just defined, this is what tells the user what that line relates to. We loaded the Pygame.surface font earlier into the variable 'SixtyFPSData'. We render this to (with the coordinates as (x,y) in pixels), a fixed 'x' position of 13, and a 'y' position that uses the same calculation as the line before to get the 'y' position.


197: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*144)))), (realWidth-20, int(130+(300-((300/GlobalMax)*144)))))`` Here we are drawing one of the lines that acts as markers to show where a key frame-rate lies, in this case thats 144 FPS (in Hz). We draw it to the display (using the variable that represents that 'self.Display'), set the colour of the line to a suitable colour in the user's selected theme. Then we are defining 2 coordinates (x,y) for the start and end of the line. This function only takes 2 points, the first '(10, int(130+(300-((300/GlobalMax)*144))))' sets the 'x' position to be 10 (pixels), this is the same value as the x position of the shape 'FPSRect' deliberately, both of the 'y' positions are the same, we run the same calculation as earlier, except instead of iterating over an array to get the value, we manually set it to 60. The final 'x' value is the same as the width of the 'FPSRect' shape we defined earlier, again this is deliberate.

198: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(OneFourFourFPSData, (13, int(130+(300-((300/GlobalMax)*140)))))`` Here we are adding a label, which will go just above the line we just defined, this is what tells the user what that line relates to. We loaded the Pygame.surface font earlier into the variable 'OneFourFourFPSData'. We render this to (with the coordinates as (x,y) in pixels), a fixed 'x' position of 13, and a 'y' position that uses the same calculation as the line before to get the 'y' position.


200: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*240)))), (realWidth-20, int(130+(300-((300/GlobalMax)*240)))))`` Here we are drawing one of the lines that acts as markers to show where a key frame-rate lies, in this case thats 240 FPS (in Hz). We draw it to the display (using the variable that represents that 'self.Display'), set the colour of the line to a suitable colour in the user's selected theme. Then we are defining 2 coordinates (x,y) for the start and end of the line. This function only takes 2 points, the first '(10, int(130+(300-((300/GlobalMax)*240))))' sets the 'x' position to be 10 (pixels), this is the same value as the x position of the shape 'FPSRect' deliberately, both of the 'y' positions are the same, we run the same calculation as earlier, except instead of iterating over an array to get the value, we manually set it to 240. The final 'x' value is the same as the width of the 'FPSRect' shape we defined earlier, again this is deliberate.

201: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TwoFortyFPSData, (13, int(130+(300-((300/GlobalMax)*240)))))`` Here we are adding a label, which will go just above the line we just defined, this is what tells the user what that line relates to. We loaded the Pygame.surface font earlier into the variable 'TwoFortyFPSData'. We render this to (with the coordinates as (x,y) in pixels), a fixed 'x' position of 13, and a 'y' position that uses the same calculation as the line before to get the 'y' position.


203: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 255, 0), False, Results1)`` Here we are drawing one of the arrays of points we spent the last stage calculating and formatting, for each of the three lines we set a different RGB value, but the first parameter 'self.Display', which represents the open Pygame window we are rendering to, the boolean value 'False', which represents if the line's start and end points should be connected by a line, and the final parameter will always be the points data for each line (a 2D array with points arrayed by (x,y) in pixels). Please also note the additional 's' at the end of the name of the subroutine, this allows it to plot multiple points, we use the other type before, that only accepts two points.

204: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 0, 255), False, Results2)`` Here we are drawing one of the arrays of points we spent the last stage calculating and formatting, for each of the three lines we set a different RGB value, but the first parameter 'self.Display', which represents the open Pygame window we are rendering to, the boolean value 'False', which represents if the line's start and end points should be connected by a line, and the final parameter will always be the points data for each line (a 2D array with points arrayed by (x,y) in pixels). Please also note the additional 's' at the end of the name of the subroutine, this allows it to plot multiple points, we use the other type before, that only accepts two points.

205: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 0), False, Results3)`` Here we are drawing one of the arrays of points we spent the last stage calculating and formatting, for each of the three lines we set a different RGB value, but the first parameter 'self.Display', which represents the open Pygame window we are rendering to, the boolean value 'False', which represents if the line's start and end points should be connected by a line, and the final parameter will always be the points data for each line (a 2D array with points arrayed by (x,y) in pixels). Please also note the additional 's' at the end of the name of the subroutine, this allows it to plot multiple points, we use the other type before, that only accepts two points.


207: ``¬ ¬ ¬ ¬ ¬ ¬ HideRect = self.mod_Pygame__.Rect(0, 110, realWidth, 330)`` Here we are drawing a border around the line graph, should any points fail to render in the appropriate area, this section should mask any small errors (although there shouldn't be). Here though we are defining the coordinates for this 'mask', we store the resulting output in the variable 'HideRect', we plot the points to start at the edge of the window with the 'x' position as 0, then we set the 'y' position to just above where the graph is rendered, then we make the rectangle span the entire width of the display with the third value of 'realWidth', and set the height of the rectangle to 330, which puts the bottom of the rectangle below the base of the graph. All values for this subroutine are in pixels.

208: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.BackgroundCol, HideRect, 20)`` Now we draw the 'mask' to the display, we start by specifying the display with 'self.Display' as the first parameter, then we set the rectangle's colour to be the same as the background, this hides the rectangle from view, then we add the points we just defined as the fourth parameter, and set a thickness of 20 pixels. Remember, anything rendered after something to the display will cover what was rendered first, so we need to take care here that the rectangle hides any errors in calculations, but doesn't hide the entire graph, which is why we specify a 20 pixel border, meaning the shape isn't entirely filled.


210: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FPSinfoTEXT, ((realWidth-FPSinfoTEXTWidth)-3, 100))`` Now we blit the sub-heading for this graph, we render the sub-heading on the right hand side of the window, to do this we use the calculation '(realWidth-FPSinfoEXTWidth)-3', where all values are in pixels. The 'y' value is manually set as 100.

211: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FILEinfoTEXT, ((realWidth-FILEinfoTEXTWidth)-3, 430))`` Now we blit the sub-heading for the disk read test, we use the same formula as before, but with different values to render the text on the right, we manually set the 'y' position to 430, which is below the graph.


213: ``¬ ¬ ¬ ¬ ¬ ¬ FileResults = DataFont.render(f"Your device achieved a score of: {round(ReadSpeed, 2)}/100 ({round((100/100)*ReadSpeed)}%)", self.aa, self.FontCol)`` Now we are taking the results of the disk read test and telling the user how they performed against a base (a score easily achievable on most devices, this may one day be made more scientific, and also display a message if disk performance is low.) This is outputted as both a score out of 100, and as a percentage. We render this with the user's preference on anti-aliasing and use the user's choice of colour from the theme they have selected. The resulting Pygame.surface object is stored in the variable 'FileResults'.

214: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ FileResultsWidth = FileResults.get_width()`` Here we are getting the width of the Pygame.surface object (in pixels), which we will need to render the text on the right hand side of the display.

215: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(FileResults, ((realWidth-FileResultsWidth)-3, 460))`` Here we are rendering the text we just converted into a Pygame.surface object, we use the same formula as with the other rendering, setting the 'x' position to be on the right, and the 'y' position manually to 460. We blit each Pygame.surface object roughly in order as we go down the display.


217: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(HARDWAREinfoTEXT, ((realWidth-HARDWAREinfoTEXTwidth)-3, 480))`` Here we are rendering the sub-title for the system information section of the benchmark on the results page. We render this to the right hand side of the GUI, and manually set the 'y' position to 480 (pixels).


219: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CPUhwINFO, ((realWidth-CPUhwINFOwidth)-3, 500))`` Here we are rendering the data we received right at the start of the benchmark process about the user's system info. This section will be based on their CPU information, which we formatted into an appropriate string beforehand. We render this too on the right, using the same equation (-3 moves the last pixels of the text off the end of the GUI, which can cause readability issues, this aims to solve that). Again we manually set the 'y' position down the display, in this case to 500.

220: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(RAMhwINFO, ((realWidth-RAMhwINFOwidth)-3, 516))`` Here we are taking the Pygame.surface object which we created earlier, this Pygame.surface object contains all the information relevant to the user on the benchmark results page, we render this below the CPU info with a 'y' position of 516 pixels. The 'x' position is determined automatically by using calculating the appropriate position on the right hand side.


222: ``¬ ¬ ¬ ¬ ¬ ¬ GreenInfo = InfoDetailsFont.render(f"Blank screen test (green); Minimum: {round(Min1, 4)} FPS, Maximum: {round(Max1, 4)} FPS", self.aa, self.FontCol)`` Here we are rendering details of what each of the lines on the line graph represents, as well as the minimum and maximum values for each, this is useful if the user is only interested in one of the tests. This text here is rendered using the font we loaded earlier and stored in the 'InfoDetailsFont', we respect the user's preference on anti-aliasing here, and use an appropriate colour from the user's currently active theme. This subroutine will return a Pygame.surface object, which we will blit to the display later.

223: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ BlueInfo = InfoDetailsFont.render(f"Drawing test (blue); Minimum: {round(Min2, 4)} FPS, Maximum: {round(Max2, 4)} FPS", self.aa, self.FontCol)`` Here we are rendering details of what each of the lines on the line graph represents, as well as the minimum and maximum values for each, this is useful if the user is only interested in one of the tests. This text here is rendered using the font we loaded earlier and stored in the 'InfoDetailsFont', we respect the user's preference on anti-aliasing here, and use an appropriate colour from the user's currently active theme. This subroutine will return a Pygame.surface object, which we will blit to the display later.

224: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ RedInfo = InfoDetailsFont.render(f"OpenGL test (red); Minimum: {round(Min3, 4)} FPS, Maximum: {round(Max3, 4)} FPS", self.aa, self.FontCol)`` Here we are rendering details of what each of the lines on the line graph represents, as well as the minimum and maximum values for each, this is useful if the user is only interested in one of the tests. This text here is rendered using the font we loaded earlier and stored in the 'InfoDetailsFont', we respect the user's preference on anti-aliasing here, and use an appropriate colour from the user's currently active theme. This subroutine will return a Pygame.surface object, which we will blit to the display later.

225: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(GreenInfo, (3, 430))`` Now we go through and blit each of the Pygame.surface objects we just created to the display, each of the lines will have manually set coordinates, as they aren't affected by the display resizing. These are rendered below the graph on the left hand side of the GUI. 

226: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(BlueInfo, (3, 445))`` Now we go through and blit each of the Pygame.surface objects we just created to the display, each of the lines will have manually set coordinates, as they aren't affected by the display resizing. These are rendered below the graph on the left hand side of the GUI. 

227: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(RedInfo, (3, 460))`` Now we go through and blit each of the Pygame.surface objects we just created to the display, each of the lines will have manually set coordinates, as they aren't affected by the display resizing. These are rendered below the graph on the left hand side of the GUI. 


229: ``¬ ¬ ¬ ¬ ¬ ¬ if resize == True:`` Now we check to see if, since the last run the display was resized, which we will detect later on (for the next iteration of the GUI), and if the display has been resized, we need to go back to the previous stage again and recalculate every single coordinate. If we didn't do this then the contents of the display wouldn't fill the display, so viewing the output on a large window could be difficult.

230: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ stage = 4`` If the display has been resized, we need to go back to the previous stage.

231: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ resize = False`` This prevents the display from being resized during the tests, as resizing the display can alter the results, and when in full-screen, Pygame does some hardware acceleration to further improve performance, so you could get contrasting results.


233: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, here we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

234: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE) and stage <= 3) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):`` Here we are detecting if the user has either pressed the 'x' in the top corner of the GUI (left for MacOS, right for Windows), or has pressed any key that isn't SPACE and the stage is less than or equal to 3, this is important, as if the user wants to cancel or leave the benchmark, then they can do this at any stage by pressing any key, as is mentioned in the instructions at the start, but then we may not want to close the GUI with any key afterwards, because if the user presses any key on the results screen, they would need to re-run the test again, even if they used a keyboard shortcut to say; take a screenshot. We also detect here of the user has pressed the ESCAPE (or ESC)key, which is commonly used as another method of exiting the GUI.

235: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:`` This if-statement controls if sound should be played or not based on the user's preference in 'Settings.py', the user's preference is stored when the program closes.

236: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)`` This line calls the subroutine; 'PlayClickSound' in 'SoundUtils.py', if the user has allowed sound to play in settings, then interacting with the display will cause the click sound to play; volume and other parameters for this subroutine are stored in the global variable 'self'.

237: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.

238: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_SPACE) and stage == 0:`` This if-statement detects if the user has pressed SPACE and the current stage is '0', which is the stage with the instructions on, this is important as the only way to continue with the benchmark is by pressing SPACE.

239: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ stage += 1`` Now we are finished with the current stage so increment the stage variable by 1, and more on forwards to the next stage.

240: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.VIDEORESIZE:`` Now we are detecting if the display has resized, if the display has been resized (even if that's to full-screen) then it sets the value of the variable 'resize' to boolean 'True', this triggers the if-statement earlier on on the next iteration of the display if the user is on the last stage to refresh it with new values. 

241: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ resize = True`` We set the variable 'resize' to boolean 'True', as the display has been resized and we need to therefore recalculate all of the points for the line graph, and move all of the size affected text too.


243: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

244: ``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(self.FPS)`` Here we are setting the refresh rate (in Hz) of the display, this is used for preventing the GUI from running really fast, causing unnecessary strain on the CPU and GPU, and also allowing us to detect the display's frame-rate (which may not be exactly the value of 'self.FPS').

245: ``¬ ¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

246: ``¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

247: ``¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

248: ``¬ print("You need to run this as part of Pycraft")`` if the user is running the code from PyPi, or as a raw “.py” file then this will be outputted to the terminal, however uses of the compiled “.exe” editions will not see this. This code is also printed first in-case the code below fails.

249: ``¬ import tkinter as tk`` Now we are importing the tkinter module into the project, all code here must be standalone and not rely on code in other modules in the project, this way the project can be taken apart and this should still work. We store he imported module, “Tkinter” with the name``tk``, this shortens length and all references to “Tkinter” from how on in this indented block will use this name.

250: ``¬ from tkinter import messagebox`` Here we are importing specific sections of “Tkinter”, in this case; messagebox, this module allows us to make dialogue boxes that are commonplace in Windows and Apple based devices.

251: ``¬ root = tk.Tk()`` This of code is required to make the dialogue box, which is what we want. This will create a window to the default size “Tkinter” has defined, and initialises the``messagebox`` module, which we want.

252: ``¬ root.withdraw()`` We use this code to hide the window that appears by using the previous root is the internal name for the window, as that is what the window created in the previous was stored in (as a variable).

253: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")`` Here we make our all to the``messagebox`` module, which has several pre-made dialogue boxes, we are using the``showerror`` pre-made dialogue box procedure here. We give it the caption of "Startup Fail", and then elaborate on the issue in the main body of the window, by displaying the text "You need to run this as part of Pycraft, please run the 'main.py' file".

254: ``¬ quit()`` This is Python’s way of closing the project, we normally use``sys.exit`` for this, which you will see later on, because its a bit cleaner on some IDLE’s and terminals. However to reduce the length of this project, we use the built in function here instead.

1: ``if not __name__ == "__main__":`` This checks to see if the place its called from (stored in the variable ``__name__``) is not ``"__main__"``. The string ``"__main__"`` would be the data stored in the variable ``__name__`` if the project was run on its own, which in this case we don't want so we only allow the code inside the if-statement to run if the data in ``__name__`` is not "__main__".

2: ``¬ print("Started <Pycraft_CaptionUtils>")`` Now we output data to the terminal if the program is running, this allows us to know if there are any errors preventing this module from loading, in which case the program would crash before that is outputted to the terminal, making us aware the error is in this module.

3: ``¬ class GenerateCaptions:`` Now we are defining a class with a suitable name that represents what the subroutines in this class do; this allows us to group up our code to make it easier to edit, organise and debug later on, as well as saving on memory as not every function will need to be loaded at once.

4: ``¬ ¬ def __init__(self):`` Here we make sure the module is initialized correctly we do this because if we tried to call this standalone, and without the code that would stop this, then all references to variables and subroutines outside of this project would be invalid and cause issues. This is also where the variable ‘self’ is defined for all references in this class. This subroutine is a procedure, so does not return a value.

5: ``¬ ¬ ¬ pass`` Here we tell python to ignore the previous line of code that expects indented code, we use this if we don't need to put any code in this indent, this should be avoided in most situations. This is mainly used in the ``__init__`` functions for Pycraft where we may not need to run any code, but need to make sure the module is working correctly.


7: ``¬ ¬ def GetLoadingCaption(self, num):`` Here we are creating a subroutine called 'GetLoadingCaption', which takes the variables 'self' and 'num', this subroutine does not return anything. This subroutine is used in the 'PycraftStartupTest' module and updates the caption regularly so that it shows the code is running still. This feature isn't very noticeable unless your running a low powered device.

8: ``¬ ¬ ¬ if num == 0:`` Here we are checking if the second parameter this subroutine takes -'num'- is equal to 0. The variable 'num' can be any number between 0 and 3 (inclusive) and this controls which caption to load. If 'num' is not in the appropriate range, then we don't display the loading animation (There is a little line animation).

9: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (-)")`` Here we are loading the first stage of the animation; setting the caption's end to (-).

10: ``¬ ¬ ¬ ¬ elif num == 1:`` Now we check to see if the value of 'num' is one, only if the previous if-statement returns False, if 'num' was 0 on the last call, it should be 1 this time around to make the animation work.

11: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (\)")`` If 'num' is equal to 1, then we display the next frame of the animation, changing the last few characters to (\) instead.

12: ``¬ ¬ ¬ ¬ elif num == 2:`` Here we are checking if the value of 'num' is equal to 2, this should be if the previous value was 1, 'num' controls which frame of the animation to show in the caption.

13: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (|)")`` If 'num' is equal to 2, then we display the third frame of the animation; (|).

14: ``¬ ¬ ¬ ¬ elif num == 3:`` This is the final frame of the animation; these if-statements should have been called in order for the animation to work. Here we are checking to see if the value of 'num' is 3.

15: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading (/)")`` We render the last frame of the 4 step animation, this is designed to look like the line in the brackets is spinning, in order from frame 0 to 4: (-) (\) (|) (/). This is designed to look like the animation you sometimes see in a CLI (Command Line Interface).

16: ``¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

17: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Loading")`` Here we simply set the caption to 'Pycraft: v<INSERT VERSION ID ERE>: Loading, this is useful if we dont want to enter a value for num, for example if the code isn't called in a sequence then we can do this instead. It is good practice in Pycraft to suitably update the caption when something happens, either on-screen or behind the scenes. 

18: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.update()`` Here we are forcing the display to update, this refreshes the entire frame. This is where the objects we either 'blit' or 'draw' to the display are made visible. This should be called only once per frame to avoid confusion and 'Pygame.display.flip()' is usually preferred, because of the greater amount of options and better performance.


20: ``¬ ¬ def GetNormalCaption(self, location):`` Here we are creating the subroutine that should be in control of all other caption loading, except for in special situations. This subroutine returns nothing but takes 2 parameters; 'self' which stores a lot of the most commonly occurring data in the program, and 'location', which is of the string data type; this is what stores the user's location. This should be the same as any sub-heading in Pycraft's GUI to avoid confusion.

21: ``¬ ¬ ¬ if self.Devmode >= 5 and self.Devmode <= 9:`` Here we are checking to see if the value of 'Devmode' is between 5 and 9 (inclusive). If 'Devmode' is between those two values then we should suitably tell the user that they are activating that.

22: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | you are: {10-self.Devmode} steps away from being a developer")`` Here we suitably update the caption to tell the user that they are entering Devmode, we also render the user's 'location' and 'self.version'. We invert the value of 'self.Devmode', by taking it away from 10, this way it counts down.

23: ``¬ ¬ ¬ ¬ elif self.Devmode == 10:`` If the user has activated 'Devmode', in which case 'self.Devmode' will be equal to 10...

24: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location} | Developer Mode | Pos: {round(self.X, 2)}, {round(self.Y, 2)}, {round(self.Z, 2)} | V: {self.Total_move_x}, {self.Total_move_y}, {self.Total_move_z} FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: {int(self.aFPS/self.Iteration)} Iteration: {self.Iteration} | MemUsE: {self.mod_Psutil__.virtual_memory().percent} | CPUUsE: {self.mod_Psutil__.cpu_percent()} | Theme: {self.theme} | Thread Count: {self.mod_Threading__.active_count()}")`` Here we are rendering information about the currently running program the user. This is a handy tool for finding bugs and issues. In order of occupance: First we render the user's position from the game-engine, we round the coordinates to 2 decimal places as they can contain long decimals that lead to the caption being longer than the display. This feature doesn't currently work in the new game-engine, but will be brought back in Pycraft v0.9.4. Secondly we render the user's velocity, again this is especially useful in game, this tells the user how much they are moving in a given direction (m/s in the new game-engine (Pycraft v0.9.3 onwards)) Which is a useful feature to see if collisions is working. Then we move on-to showing the user the current maximum FPS, currently running FPS, average FPS and the number samples taken for the average. All values for FPS are measured in z and are rounded to the nearest integer. Then we render the amount of memory currently being used by the system as a whole, as well as the utilisation on the CPU (These are both given as percentages). Then we show the currently active theme. Finally we show the amount of threads the program is currently using, again a handy debugging feature. ALL METRICS ARE SEPARATED BY A PILLAR (|) AND GROUPED WEN NECESSARY. NEW METRICS SHOULD BE ADDED TO TE END UNLESS TEY SUITABLY FIT INTO A GROUP.

25: ``¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

26: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: {location}")`` Here we render the caption as normal, this is how the caption should appear most of the time, displaying just the name of the game, version and location (the current menu the user is in).


28: ``else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

29: ``¬ print("You need to run this as part of Pycraft")`` if the user is running the code from PyPi, or as a raw “.py” file then this will be outputted to the terminal, however uses of the compiled “.exe” editions will not see this. This code is also printed first in-case the code below fails.

30: ``¬ import tkinter as tk`` Now we are importing the tkinter module into the project, all code here must be standalone and not rely on code in other modules in the project, this way the project can be taken apart and this should still work. We store he imported module, “Tkinter” with the name``tk``, this shortens length and all references to “Tkinter” from how on in this indented block will use this name.

31: ``¬ from tkinter import messagebox`` Here we are importing specific sections of “Tkinter”, in this case; messagebox, this module allows us to make dialogue boxes that are commonplace in Windows and Apple based devices.

32: ``¬ root = tk.Tk()`` This of code is required to make the dialogue box, which is what we want. This will create a window to the default size “Tkinter” has defined, and initialises the``messagebox`` module, which we want.

33: ``¬ root.withdraw()`` We use this code to hide the window that appears by using the previous root is the internal name for the window, as that is what the window created in the previous was stored in (as a variable).

34: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")`` Here we make our all to the``messagebox`` module, which has several pre-made dialogue boxes, we are using the``showerror`` pre-made dialogue box procedure here. We give it the caption of "Startup Fail", and then elaborate on the issue in the main body of the window, by displaying the text "You need to run this as part of Pycraft, please run the 'main.py' file".

35: ``¬ quit()`` This is Python’s way of closing the project, we normally use``sys.exit`` for this, which you will see later on, because its a bit cleaner on some IDLE’s and terminals. However to reduce the length of this project, we use the built in function here instead.

1: ``if not __name__ == "__main__":`` This checks to see if the place its called from (stored in the variable ``__name__``) is not ``"__main__"``. The string ``"__main__"`` would be the data stored in the variable ``__name__`` if the project was run on its own, which in this case we don't want so we only allow the code inside the if-statement to run if the data in ``__name__`` is not "__main__".

2: ``¬ print("Started <Pycraft_CharacterDesigner>")`` Now we output data to the terminal if the program is running, this allows us to know if there are any errors preventing this module from loading, in which case the program would crash before that is outputted to the terminal, making us aware the error is in this module.

3: ``¬ class GenerateCharacterDesigner:`` Now we are defining a class with a suitable name that represents what the subroutines in this class do; this allows us to group up our code to make it easier to edit, organise and debug later on, as well as saving on memory as not every function will need to be loaded at once.

4: ``¬ ¬ def __init__(self):`` Here we make sure the module is initialized correctly we do this because if we tried to call this standalone, and without the code that would stop this, then all references to variables and subroutines outside of this project would be invalid and cause issues. This is also where the variable ‘self’ is defined for all references in this class. This subroutine is a procedure, so does not return a value.

5: ``¬ ¬ ¬ pass`` Here we tell python to ignore the previous line of code that expects indented code, we use this if we don't need to put any code in this indent, this should be avoided in most situations. This is mainly used in the ``__init__`` functions for Pycraft where we may not need to run any code, but need to make sure the module is working correctly.


7: ``¬ ¬ def CharacterDesigner(self):`` Here we are defining the subroutine that controls the character designer GUI, we name the subroutine 'CharacterDesigner', and it takes only one parameter, 'self'. This gives the subroutine all the necessary data to run. This subroutine only returns an error if one occurs, if there is no errors (which there hopefully shouldn't be), then the subroutine will return nothing.

8: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

9: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

10: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

11: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")`` Here we are setting the caption of the GUI, we use the subroutine we looked at earlier in 'CaptionUtils.py'. The subroutine is called 'GetNormalCaption', this subroutine allows us to change the caption for our GUI. This subroutine takes 2 arguments, the second one is of importance here; this is the location we enter; this is the same as the subheading for this section of the GUI. 

12: ``¬ ¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 60.

13: ``¬ ¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 35.

14: ``¬ ¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 15.


16: ``¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.SecondFontCol)`` (There is a bug here; this should be 'self.FontCol' as the last parameter, so the following description will appear differently. This will be fixed in Pycraft v0.9.4) Takes the font, which we stored in the variable 'MainTitleFont' and uses it to render the text \"Pycraft\", with the user's preference on anti-aliasing, 'aa' and the colour defined in 'ThemeUtils.py', the resulting Pygame.surface object is stored in the variable 'TitleFont'.

17: ``¬ ¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()`` Gets the width (in pixels) of the Pygame.surface object 'TitleFont


19: ``¬ ¬ ¬ ¬ AchievementsFont = InfoTitleFont.render("Character Designer", self.aa, self.FontCol)`` (There is a bug here; this should be 'CharacterDesignerFont' NOT 'AchievementsFont') Here we are taking the font we just loaded into the variable 'InfoTitleFont' and using it to create a Pygame.surface object which we store in the 'CharacterDesignerFont' variable. This Pygame.surface object contains the text 'Character Designer' which is rendered with the user's preference on anti-aliasing, and the user's selected theme. 

20: ``¬ ¬ ¬ ¬ ¬ tempFPS = self.FPS`` This is used to temporarily store the game's target FPS, this is used later to slow the game down when minimised.


22: ``¬ ¬ ¬ ¬ while True:`` Enters the project's game loop

23: ``¬ ¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()`` Gets the width and height of the current Pygame window (in pixels), this is used in working out where everything should be scaled in-game if the window is resized.


25: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:`` Detects if the window has been made smaller than the minimum width, 1280 pixels

26: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)`` If the window is smaller than 1280 pixels, then reset the display's WIDTH to 1280. There is no limit to how large the display can be.

27: ``¬ ¬ ¬ ¬ ¬ ¬ if realHeight < 720:`` Detects if the window has been made smaller than the minimum height, 720 pixels

28: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)`` If the window is smaller than 720 pixels, then reset the display's HEIGHT to 720. There is no limit to how large the display can be.


30: ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()`` Gets the current window frame-rate (in Hz)

31: ``¬ ¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS`` Adds the current framerate to a variable which is used to calculate the mean average FPS in game (in Hz)

32: ``¬ ¬ ¬ ¬ ¬ ¬ self.Iteration += 1`` Used as frequency in calculating the mean average FPS (in Hz)


34: ``¬ ¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)`` This line of code is used to control what happens when the display is minimised, for more information, see the documentation for this subroutine. This subroutine will return an integer, this is stored in the variable 'tempFPS', which is used to set the windows FPS (in Hz).


36: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, here we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

37: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):`` This controls when the display should close (if on the 'ome-Screen') or returning back to the previous window (typically the 'ome-Screen'), to do this you can press the 'x' at the top of the display, or by pressing 'ESC or ESCAPE' which is handy when in full-screen modes.

38: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:`` This if-statement controls if sound should be played or not based on the user's preference in 'Settings.py', the user's preference is stored when the program closes.

39: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)`` This line calls the subroutine; 'PlayClickSound' in 'SoundUtils.py', if the user has allowed sound to play in settings, then interacting with the display will cause the click sound to play; volume and other parameters for this subroutine are stored in the global variable 'self'.

40: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.

41: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:`` This line detects if any key is pressed on a keyboard, used when detecting events like pressing keys to navigate the GUIs or moving in-game.

42: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:`` This line of code is used as part of the activation for 'Devmode' which you activate by pressing SPACE 10 times. Here we are detecting is the SPACE key has been pressed and 'Devmode' is not already active.

43: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1`` This line increases the value of the variable 'Devmode' by 1. When the variable 'Devmode' is equal to 0, then 'Devmode' is activated.

44: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:`` Detects if the key 'q' is pressed (not case sensitive).

45: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)`` If the key 'q' is pressed, then we load up the secondary window in 'TkinterUtils.py', this, like 'Devmode' displays information about the running program. This feature may be deprecated at a later date, but this isn't clear yet. All the data the subroutine needs to access is sent through the parameter 'self' which is a global variable.

46: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:`` This line detects if the function key 'F11' has been pressed.

47: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)`` If the function key 'F11' has been pressed, then resize the display by toggling full-screen. (The 'F11' key is commonly assigned to this in other applications).

48: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:`` Detects if the key 'x' is pressed (NOT case sensitive).

49: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1`` This resets 'Devmode' to 1, turning the feature off. This can be used to cancel counting the number of spaces pressed too.


51: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")`` Here we are setting the caption of the GUI, we use the subroutine we looked at earlier in 'CaptionUtils.py'. The subroutine is called 'GetNormalCaption', this subroutine allows us to change the caption for our GUI. This subroutine takes 2 arguments, the second one is of importance here; this is the location we enter; this is the same as the subheading for this section of the GUI. 


53: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.


55: ``¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)`` This line defines the dimensions of a rectangle in Pygame, in this case the rectangle will be drawn at (0, 0) (x, y) with a width of 1280 and a height of 90. (all values here are in pixels and (0, 0) (x, y) is the top-left corner of the GUI (so thats 90 pixels DOWN)).

56: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)`` This line draws a rectangle to the display with 'self.Display', the colour to fill the rectangle is the colour of the background to Pycraft (This is a setting the user can change in the GUI in 'Settings.py') with the dimensions of the previously created Pygame Rect object called; 'cover_Rect'.

57: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))`` This line takes the Pygame.surface object 'TitleFont' and draws it onto the window (stored in the variable 'self.Display', at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. The coordinates are (x, y).

58: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))`` This line takes the Pygame.surface object 'AchievementsFont' and draws it onto the window (stored in the variable 'self.Display'), at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. We also add an offset of 55 pixels to make sure the two titles don't overlap.


60: ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)`` This line calls the subroutine 'CreateDevmodeGraph', this subroutine is responsible for drawing the graph you see at the top-right of most Pycraft GUI's. It takes the variable 'self' as a parameter, this code will return any errors, which are stored in the variable 'Message'. If there are no errors then the subroutine will return 'None'. The second parameter 'DataFont' is the currently loaded font which is used for rendering the text at the top of the graph.

61: ``¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:`` This line detects if there are any errors stored in the variable 'Message'. All important errors are stored in this variable. This error detection may be moved to a thread at a later date.

62: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

63: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

64: ``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)`` This line of code controls how fast the GUI should refresh, defaulting to the user's preference unless the window is minimised, in which case its set to 15 FPS. All values for FPS are in (Hz) and this line of code specifies the maximum FPS of the window, but this does not guarantee that FPS.

65: ``¬ ¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

66: ``¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

67: ``¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

68: ``¬ print("You need to run this as part of Pycraft")`` if the user is running the code from PyPi, or as a raw “.py” file then this will be outputted to the terminal, however uses of the compiled “.exe” editions will not see this. This code is also printed first in-case the code below fails.

69: ``¬ import tkinter as tk`` Now we are importing the tkinter module into the project, all code here must be standalone and not rely on code in other modules in the project, this way the project can be taken apart and this should still work. We store he imported module, “Tkinter” with the name``tk``, this shortens length and all references to “Tkinter” from how on in this indented block will use this name.

70: ``¬ from tkinter import messagebox`` Here we are importing specific sections of “Tkinter”, in this case; messagebox, this module allows us to make dialogue boxes that are commonplace in Windows and Apple based devices.

71: ``¬ root = tk.Tk()`` This of code is required to make the dialogue box, which is what we want. This will create a window to the default size “Tkinter” has defined, and initialises the``messagebox`` module, which we want.

72: ``¬ root.withdraw()`` We use this code to hide the window that appears by using the previous root is the internal name for the window, as that is what the window created in the previous was stored in (as a variable).

73: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")`` Here we make our all to the``messagebox`` module, which has several pre-made dialogue boxes, we are using the``showerror`` pre-made dialogue box procedure here. We give it the caption of "Startup Fail", and then elaborate on the issue in the main body of the window, by displaying the text "You need to run this as part of Pycraft, please run the 'main.py' file".

74: ``¬ quit()`` This is Python’s way of closing the project, we normally use``sys.exit`` for this, which you will see later on, because its a bit cleaner on some IDLE’s and terminals. However to reduce the length of this project, we use the built in function here instead.

1: ``if not __name__ == "__main__":`` This checks to see if the place its called from (stored in the variable ``__name__``) is not ``"__main__"``. The string ``"__main__"`` would be the data stored in the variable ``__name__`` if the project was run on its own, which in this case we don't want so we only allow the code inside the if-statement to run if the data in ``__name__`` is not "__main__".

2: ``¬ print("Started <Pycraft_Credits>")`` Now we output data to the terminal if the program is running, this allows us to know if there are any errors preventing this module from loading, in which case the program would crash before that is outputted to the terminal, making us aware the error is in this module.

3: ``¬ class GenerateCredits:`` Now we are defining a class with a suitable name that represents what the subroutines in this class do; this allows us to group up our code to make it easier to edit, organise and debug later on, as well as saving on memory as not every function will need to be loaded at once.

4: ``¬ ¬ def __init__(self):`` Here we make sure the module is initialized correctly we do this because if we tried to call this standalone, and without the code that would stop this, then all references to variables and subroutines outside of this project would be invalid and cause issues. This is also where the variable ‘self’ is defined for all references in this class. This subroutine is a procedure, so does not return a value.

5: ``¬ ¬ ¬ pass`` Here we tell python to ignore the previous line of code that expects indented code, we use this if we don't need to put any code in this indent, this should be avoided in most situations. This is mainly used in the ``__init__`` functions for Pycraft where we may not need to run any code, but need to make sure the module is working correctly.


7: ``¬ ¬ def Credits(self):`` Here we are creating the subroutine 'Credits', this takes only one parameter, 'self', which contains all the necessary information to run this subroutine. 'Credits' will not return data unless an error occurs, in which case that is returned. This subroutine does the bulk of the programming for the Credits GUI.

8: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

9: ``¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

10: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

11: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits")`` Here we are appropriately using the subroutine we created earlier to update the caption of the GUI, we use the subroutine 'GetNormalCaption' from 'CaptionUtils.py' to do this. The second parameter is the name of the GUI we are currently in, (in this case that's; 'Credits'), this name should be identical to the subheading of the GUI where possible. 

12: ``¬ ¬ ¬ ¬ ¬ VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Here we are loading the font 'Book Antiqua' from the font's folder, we set the size of this font to 15 and store the loaded font into the variable 'VersionFont'. 'self.mod_OS__.path.join()' is a subroutine that is part of the 'OS' module built into Python, this allows us to concatenate string data types to give us a file location.

13: ``¬ ¬ ¬ ¬ ¬ LargeCreditsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)`` Here we are loading the font 'Book Antiqua' and setting the size to 20, we store this object then in the variable 'LargeCreditsFont', where it will be appropriately used for sub-headings and titles for each of the sections of the credits sequence.

14: ``¬ ¬ ¬ ¬ ¬ MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 60.

15: ``¬ ¬ ¬ ¬ ¬ InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 35.

16: ``¬ ¬ ¬ ¬ ¬ DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)`` Loads the project's font, 'Book Antiqua' from the 'Fonts' folder in Pycraft, and sets the font size to 15.

17: ``¬ ¬ ¬ ¬ ¬ TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)`` Takes the font, which we stored in the variable 'MainTitleFont' and uses it to render the text "Pycraft", with the user's preference on anti-aliasing, 'aa' and the colour defined in 'ThemeUtils.py', the resulting Pygame.surface object is stored in the variable 'TitleFont'.

18: ``¬ ¬ ¬ ¬ ¬ TitleWidth = TitleFont.get_width()`` Gets the width (in pixels) of the Pygame.surface object 'TitleFont

19: ``¬ ¬ ¬ ¬ ¬ TitleHeight = TitleFont.get_height()`` Here we are getting the height of the variable 'TitleFont' which we have just loaded.

20: ``¬ ¬ ¬ ¬ ¬ CreditsFont = InfoTitleFont.render("Credits", self.aa, self.SecondFontCol)`` Here we are rendering the text 'Credits' and using the font 'InfoTitleFont' to create a Pygame.surface object, which we store in the variable 'CreditsFont'. We also set the anti-aliasing based on the user's preference, and choose an appropriate colour from the user's current theme, in this case, as with ALL subheadings for GUIs, we use the 'SecondFontCol' which gives us greater customisability over the GUI.

21: ``¬ ¬ ¬ ¬ ¬ Credits1 = LargeCreditsFont.render(f"Pycraft: v{self.version}", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

22: ``¬ ¬ ¬ ¬ ¬ Credits1Width = Credits1.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

23: ``¬ ¬ ¬ ¬ ¬ Credits2 = LargeCreditsFont.render("Game Director: Tom Jebbo", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

24: ``¬ ¬ ¬ ¬ ¬ Credits2Width = Credits2.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

25: ``¬ ¬ ¬ ¬ ¬ Credits3 = LargeCreditsFont.render("Art and Music Lead: Tom Jebbo", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

26: ``¬ ¬ ¬ ¬ ¬ Credits3Width = Credits3.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

27: ``¬ ¬ ¬ ¬ ¬ Credits4 = LargeCreditsFont.render("Other Music Credits:", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

28: ``¬ ¬ ¬ ¬ ¬ Credits4Width = Credits4.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

29: ``¬ ¬ ¬ ¬ ¬ Credits5 = LargeCreditsFont.render("Freesound: - Erokia's 'ambient wave compilation' @ freesound.org/s/473545", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

30: ``¬ ¬ ¬ ¬ ¬ Credits5Width = Credits5.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

31: ``¬ ¬ ¬ ¬ ¬ Credits6 = LargeCreditsFont.render("Freesound: - Soundholder's 'ambient meadow near forest' @ freesound.org/s/425368", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

32: ``¬ ¬ ¬ ¬ ¬ Credits6Width = Credits6.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

33: ``¬ ¬ ¬ ¬ ¬ Credits7 = LargeCreditsFont.render("Freesound: - monte32's 'Footsteps_6_Dirt_shoe' @ freesound.org/people/monte32/sounds/353799", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

34: ``¬ ¬ ¬ ¬ ¬ Credits7Width = Credits7.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

35: ``¬ ¬ ¬ ¬ ¬ Credits8 = LargeCreditsFont.render("With thanks to the developers of:", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

36: ``¬ ¬ ¬ ¬ ¬ Credits8Width = Credits8.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

37: ``¬ ¬ ¬ ¬ ¬ Credits9 = LargeCreditsFont.render("PSutil", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

38: ``¬ ¬ ¬ ¬ ¬ Credits9Width = Credits9.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

39: ``¬ ¬ ¬ ¬ ¬ Credits10 = LargeCreditsFont.render("Python", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

40: ``¬ ¬ ¬ ¬ ¬ Credits10Width = Credits10.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

41: ``¬ ¬ ¬ ¬ ¬ Credits11 = LargeCreditsFont.render("Pygame", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

42: ``¬ ¬ ¬ ¬ ¬ Credits11Width = Credits11.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

43: ``¬ ¬ ¬ ¬ ¬ Credits12 = LargeCreditsFont.render("Numpy", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

44: ``¬ ¬ ¬ ¬ ¬ Credits12Width = Credits12.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

45: ``¬ ¬ ¬ ¬ ¬ Credits13 = LargeCreditsFont.render("Nuitka", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

46: ``¬ ¬ ¬ ¬ ¬ Credits13Width = Credits13.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

47: ``¬ ¬ ¬ ¬ ¬ Credits14 = LargeCreditsFont.render("CPUinfo", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

48: ``¬ ¬ ¬ ¬ ¬ Credits14Width = Credits14.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

49: ``¬ ¬ ¬ ¬ ¬ Credits15 = LargeCreditsFont.render("PyInstaller", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

50: ``¬ ¬ ¬ ¬ ¬ Credits15Width = Credits15.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

51: ``¬ ¬ ¬ ¬ ¬ Credits16 = LargeCreditsFont.render("PyAutoGUI", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

52: ``¬ ¬ ¬ ¬ ¬ Credits16Width = Credits16.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

53: ``¬ ¬ ¬ ¬ ¬ Credits17 = LargeCreditsFont.render("PyWaveFront", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

54: ``¬ ¬ ¬ ¬ ¬ Credits17Width = Credits17.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

55: ``¬ ¬ ¬ ¬ ¬ Credits18 = LargeCreditsFont.render("Microsoft's Visual Studio Code", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

56: ``¬ ¬ ¬ ¬ ¬ Credits18Width = Credits18.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

57: ``¬ ¬ ¬ ¬ ¬ Credits19 = LargeCreditsFont.render("PIL (Pillow/Python Imaging Library)", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

58: ``¬ ¬ ¬ ¬ ¬ Credits19Width = Credits19.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

59: ``¬ ¬ ¬ ¬ ¬ Credits20 = LargeCreditsFont.render("PyOpenGL (and PyOpenGL-accelerate)", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

60: ``¬ ¬ ¬ ¬ ¬ Credits20Width = Credits20.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

61: ``¬ ¬ ¬ ¬ ¬ Credits21 = LargeCreditsFont.render("For more in depth accreditation please check the GitHub Page @ github.com/PycraftDeveloper/Pycraft", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

62: ``¬ ¬ ¬ ¬ ¬ Credits21Width = Credits21.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

63: ``¬ ¬ ¬ ¬ ¬ Credits22 = LargeCreditsFont.render("With thanks to:", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

64: ``¬ ¬ ¬ ¬ ¬ Credits22Width = Credits22.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

65: ``¬ ¬ ¬ ¬ ¬ Credits23 = LargeCreditsFont.render("All my wonderful followers on Twitter, and you for installing this game, that's massively appreciated!", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

66: ``¬ ¬ ¬ ¬ ¬ Credits23Width = Credits23.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

67: ``¬ ¬ ¬ ¬ ¬ Credits24 = LargeCreditsFont.render("For full change-log please visit my aforementioned GitHub profile", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

68: ``¬ ¬ ¬ ¬ ¬ Credits24Width = Credits24.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

69: ``¬ ¬ ¬ ¬ ¬ Credits25 = LargeCreditsFont.render("Disclaimer:", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

70: ``¬ ¬ ¬ ¬ ¬ Credits25Width = Credits25.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

71: ``¬ ¬ ¬ ¬ ¬ Credits26 = VersionFont.render("The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

72: ``¬ ¬ ¬ ¬ ¬ Credits26Width = Credits26.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

73: ``¬ ¬ ¬ ¬ ¬ Credits27 = VersionFont.render("friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

74: ``¬ ¬ ¬ ¬ ¬ Credits27Width = Credits27.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

75: ``¬ ¬ ¬ ¬ ¬ Credits28 = VersionFont.render("my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

76: ``¬ ¬ ¬ ¬ ¬ Credits28Width = Credits28.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

77: ``¬ ¬ ¬ ¬ ¬ Credits29 = VersionFont.render("DOES NOT TAKE ANY RESPONSIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXTERNAL MODULES INSTALLED ONTO", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

78: ``¬ ¬ ¬ ¬ ¬ Credits29Width = Credits29.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

79: ``¬ ¬ ¬ ¬ ¬ Credits30 = VersionFont.render("YOUR COMPUTER (WHEN NOT CHOOSING THE RECOMMENDED EXECUTABLE VERSION) ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

80: ``¬ ¬ ¬ ¬ ¬ Credits30Width = Credits30.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

81: ``¬ ¬ ¬ ¬ ¬ Credits31 = VersionFont.render("RESPONSIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVICES MANAGER OR ADMINISTRATOR TO INSTALL AND USE", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

82: ``¬ ¬ ¬ ¬ ¬ Credits31Width = Credits31.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

83: ``¬ ¬ ¬ ¬ ¬ Credits32 = VersionFont.render("COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVICE, AND AT ANY POINT NO CONNECTION TO A", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

84: ``¬ ¬ ¬ ¬ ¬ Credits32Width = Credits32.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

85: ``¬ ¬ ¬ ¬ ¬ Credits33 = VersionFont.render("NETWORK IS REQUIRED. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you.", self.aa, self.AccentCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

86: ``¬ ¬ ¬ ¬ ¬ Credits33Width = Credits33.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

87: ``¬ ¬ ¬ ¬ ¬ Credits34 = VersionFont.render("Thank You!", self.aa, self.FontCol)`` Now we go through and render each of the lines for the credits GUI, each of these 'Credits<num>' variables does a very similar thing, loading a string with the 'LargeCreditsFont' which we loaded earlier. We also respect the user's preference on anti-aliasing and choose a suitable colour from the user's theme.

88: ``¬ ¬ ¬ ¬ ¬ Credits34Width = Credits34.get_width()`` Here we are getting the width of the text object we just rendered, this is important as we render all of the headers and details centrally in this GUI.

89: ``¬ ¬ ¬ ¬ ¬ Credits34Height = Credits34.get_height()`` Here we are getting the height of the last Pygame.surface object in the sequence, this is important as its used in the calculation for calculating when that Pygame.surface object is exactly centered onscreen on the 'x' axis, in which case this will trigger the GUI to close. We store the resulting height in pixels of this Pygame.surface object in the variable 'Credits34Height'.


91: ``¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()`` Gets the width and height of the current Pygame window (in pixels), this is used in working out where everything should be scaled in-game if the window is resized.

92: ``¬ ¬ ¬ ¬ ¬ VisualYdisplacement = realHeight`` Now we are setting the variable 'visualYdisplacement' to be the same number as the height of the display, this is dont deliberately to make sure that when there animation begins the text moves up from the bottom, but until the animation begins the text is hidden offscreen.

93: ``¬ ¬ ¬ ¬ ¬ IntroYDisplacement = (realHeight-TitleHeight)/2`` Now we are setting the value of 'IntroYDisplacement' to be exactly the position halfway down the 'x' axis of the display, this means that when the first part of the animation is rendered, 'Pycraft', it's rendered centrally onscreen.

94: ``¬ ¬ ¬ ¬ ¬ timer = 5`` Now we set the variable 'timer' to the integer value of 5, this is used to control the order of appearance of the title, making sure that the title is displayed for approximately 4 seconds before the subheading 'Credits' appears below and the whole scene moves up.

95: ``¬ ¬ ¬ ¬ ¬ tempFPS = self.FPS`` This is used to temporarily store the game's target FPS, this is used later to slow the game down when minimised.


97: ``¬ ¬ ¬ ¬ EndClock = 0`` We set the value of 'EndClock' to be 0, this is another timer that controls how long the last piece of text in the animation (the 'thank you') is rendered for before sending us back to the home screen, but until we need to activate the timer to start counting up, we set the value to 0.

98: ``¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()`` Now we are getting the dimensions of the monitor the display is currently on, this is used later on to calculate the dimensions for a rectangle that prevents the animation from rendering text above the title. (This isn't going to be used in later versions, its being replaced with 'realWidth').

99: ``¬ ¬ ¬ ¬ ¬ while True:`` Enters the project's game loop

100: ``¬ ¬ ¬ ¬ ¬ ¬ realWidth, realHeight = self.mod_Pygame__.display.get_window_size()`` Gets the width and height of the current Pygame window (in pixels), this is used in working out where everything should be scaled in-game if the window is resized.


102: ``¬ ¬ ¬ ¬ ¬ if realWidth < 1280:`` Detects if the window has been made smaller than the minimum width, 1280 pixels

103: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)`` If the window is smaller than 1280 pixels, then reset the display's WIDTH to 1280. There is no limit to how large the display can be.

104: ``¬ ¬ ¬ ¬ ¬ ¬ if realHeight < 720:`` Detects if the window has been made smaller than the minimum height, 720 pixels

105: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)`` If the window is smaller than 720 pixels, then reset the display's HEIGHT to 720. There is no limit to how large the display can be.


107: ``¬ ¬ ¬ ¬ ¬ self.eFPS = self.clock.get_fps()`` Gets the current window frame-rate (in Hz)

108: ``¬ ¬ ¬ ¬ ¬ ¬ self.aFPS += self.eFPS`` Adds the current framerate to a variable which is used to calculate the mean average FPS in game (in Hz)

109: ``¬ ¬ ¬ ¬ ¬ ¬ self.Iteration += 1`` Used as frequency in calculating the mean average FPS (in Hz)


111: ``¬ ¬ ¬ ¬ ¬ ¬ tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)`` This line of code is used to control what happens when the display is minimised, for more information, see the documentation for this subroutine. This subroutine will return an integer, this is stored in the variable 'tempFPS', which is used to set the windows FPS (in Hz).


113: ``¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, here we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

114: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):`` This controls when the display should close (if on the 'ome-Screen') or returning back to the previous window (typically the 'ome-Screen'), to do this you can press the 'x' at the top of the display, or by pressing 'ESC or ESCAPE' which is handy when in full-screen modes.

115: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if self.sound == True:`` This if-statement controls if sound should be played or not based on the user's preference in 'Settings.py', the user's preference is stored when the program closes.

116: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_SoundUtils__.PlaySound.PlayClickSound(self)`` This line calls the subroutine; 'PlayClickSound' in 'SoundUtils.py', if the user has allowed sound to play in settings, then interacting with the display will cause the click sound to play; volume and other parameters for this subroutine are stored in the global variable 'self'.

117: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.

118: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ elif event.type == self.mod_Pygame__.KEYDOWN:`` This line detects if any key is pressed on a keyboard, used when detecting events like pressing keys to navigate the GUIs or moving in-game.

119: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10:`` This line of code is used as part of the activation for 'Devmode' which you activate by pressing SPACE 10 times. Here we are detecting is the SPACE key has been pressed and 'Devmode' is not already active.

120: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode += 1`` This line increases the value of the variable 'Devmode' by 1. When the variable 'Devmode' is equal to 0, then 'Devmode' is activated.

121: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_q:`` Detects if the key 'q' is pressed (not case sensitive).

122: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)`` If the key 'q' is pressed, then we load up the secondary window in 'TkinterUtils.py', this, like 'Devmode' displays information about the running program. This feature may be deprecated at a later date, but this isn't clear yet. All the data the subroutine needs to access is sent through the parameter 'self' which is a global variable.

123: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_F11:`` This line detects if the function key 'F11' has been pressed.

124: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)`` If the function key 'F11' has been pressed, then resize the display by toggling full-screen. (The 'F11' key is commonly assigned to this in other applications).

125: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.key == self.mod_Pygame__.K_x:`` Detects if the key 'x' is pressed (NOT case sensitive).

126: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Devmode = 1`` This resets 'Devmode' to 1, turning the feature off. This can be used to cancel counting the number of spaces pressed too.


128: ``¬ ¬ ¬ ¬ ¬ self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits and Change-Log")`` Here we are appropriately using the subroutine we created earlier to update the caption of the GUI, we use the subroutine 'GetNormalCaption' from 'CaptionUtils.py' to do this. The second parameter is the name of the GUI we are currently in, (in this case that's; 'Credits and Change-Log')

129: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

130: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits1, ((realWidth-Credits1Width)/2, 0+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

131: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits2, ((realWidth-Credits2Width)/2, 115+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

132: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits3, ((realWidth-Credits3Width)/2, (115*2)+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

133: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits4, ((realWidth-Credits4Width)/2, (115*3)+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

134: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits5, ((realWidth-Credits5Width)/2, (115*3)+20+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

135: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits6, ((realWidth-Credits6Width)/2, (115*3)+40+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

136: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits7, ((realWidth-Credits7Width)/2, (115*3)+60+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

137: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits8, ((realWidth-Credits8Width)/2, 540+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

138: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits9, ((realWidth-Credits9Width)/2, 540+20+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

139: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits10, ((realWidth-Credits10Width)/2, 540+40+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

140: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits11, ((realWidth-Credits11Width)/2, 540+60+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

141: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits12, ((realWidth-Credits12Width)/2, 540+80+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

142: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits13, ((realWidth-Credits13Width)/2, 540+100+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

143: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits14, ((realWidth-Credits14Width)/2, 540+120+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

144: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits15, ((realWidth-Credits15Width)/2, 540+140+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

145: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits16, ((realWidth-Credits16Width)/2, 540+160+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

146: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits17, ((realWidth-Credits17Width)/2, 540+180+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

147: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits18, ((realWidth-Credits18Width)/2, 540+200+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

148: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits19, ((realWidth-Credits19Width)/2, 540+220+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

149: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits20, ((realWidth-Credits20Width)/2, 540+240+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

150: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits21, ((realWidth-Credits21Width)/2, 540+260+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

151: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits22, ((realWidth-Credits22Width)/2, 915+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

152: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits23, ((realWidth-Credits23Width)/2, 935+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

153: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits24, ((realWidth-Credits24Width)/2, 1050+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

154: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits25, ((realWidth-Credits25Width)/2, 1165+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

155: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits26, ((realWidth-Credits26Width)/2, 1167+15+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

156: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits27, ((realWidth-Credits27Width)/2, 1167+30+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

157: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits28, ((realWidth-Credits28Width)/2, 1167+45+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

158: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits29, ((realWidth-Credits29Width)/2, 1167+60+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

159: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits30, ((realWidth-Credits30Width)/2, 1167+75+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

160: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits31, ((realWidth-Credits31Width)/2, 1167+90+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

161: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits32, ((realWidth-Credits32Width)/2, 1167+105+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.

162: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits33, ((realWidth-Credits33Width)/2, 1167+120+VisualYdisplacement))`` Now we go through and blit all of the Pygame.surface objects we just loaded into the variables 'Credits<num>', we are rendering the Pygame.surface objects to the display, which we reference with the variable 'self.Display'. The second parameter in this subroutine is the position onscreen (in pixels) where we want to load the top-left hand corner of the object. We use the same calculation to calculate the 'x' position, which should show the text as centred. This formula has been used before, but in-short; it takes the width of the display, takes away the width of the Pygame.surface object, and divides the result by 2 (the result from this formula is in pixels also). Then for the 'y' axis, we want to draw all of the credits going down the display, starting from 0, then 115, 230 exct, which is the first number (in pixels), if we didn't have the rest of the formula there, the whole sequence would be rendered down the display, eventually continuing off-screen. The variable 'VisualYdisplacement' stores a numerical value that controls when, as the animation plays out, where each object should be drawn, this variable also controls animation speed.


164: ``¬ ¬ ¬ ¬ ¬ if timer >= 1:`` Now we are checking the 'timer' variable we created earlier, this variable starts at the value of 5 and will decrease until the variable is less than or equal to 1. This if-statement controls how long the title 'Pycraft' is rendered centrally for at the start of the animation - approximately 4 seconds.

165: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))`` If the preceding if-statement is true, then we render the title centered on both the 'x' and 'y' value. The  'x' axis calculation is the same as we have seen before, but the 'y' axis calculation takes the value of 0, and (at this point in the program) will add the amount of pixels that is half of the height of the display, this we do when we first defined the variable earlier.

166: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ timer -= 1/(self.aFPS/self.Iteration)`` As the program runs for the first 4 seconds at the start of the animation, we will need to decrease the timer, otherwise we would never get out of loading that section, to do this we remove exactly the time it takes for 1 frame to pass, with each run (by calculating the average FPS using 'self.aFPS/self.Iteration', and dividing 1 by that decimal value). If we just did 'timer -= 1' then the start of the animation where the title is centred would stay there for only 4 frames, a very small amount of time, and we cant specify say 'wait 500 runs' before moving on (maybe by doing 'timer -= 0.01') because of the ability to change FPS' so that could be 15 seconds at 15FPS, but just 0.5 at 240FPS.

167: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement = realHeight`` Now we are setting the variable 'visualYdisplacement' to be the same number as the height of the display, this is dont deliberately to make sure that when there animation begins the text moves up from the bottom, but until the animation begins the text is hidden offscreen.

168: ``¬ ¬ ¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

169: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if IntroYDisplacement <= 0:`` Now we are checking to see if the variable 'IntroYDisplacement' is less than or equal to 0, this will return True when the 'timer' if-statement we created earlier hits a value less than 1. This if-statement initiates the rest of the animation.

170: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, FullscreenX, 90)`` Now we are defining the dimensions of a rectangle, to which we store in the variable 'cover_Rect', this object will be used to prevent the text from sliding over the title and sub-heading during the animation. We set the (x,y) positions to the top-left most corner of the GUI, and the rectangle spans the length of the display (there is a bug here; instead of 'FullscreenX', this should be 'realWidth'), and we make the rectangle's height to be 90, as this covers the title and sub-heading without taking up too much space.

171: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)`` This line draws a rectangle to the display with 'self.Display', the colour to fill the rectangle is the colour of the background to Pycraft (This is a setting the user can change in the GUI in 'Settings.py') with the dimensions of the previously created Pygame Rect object called; 'cover_Rect'.

172: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))`` This line takes the Pygame.surface object 'TitleFont' and draws it onto the window (stored in the variable 'self.Display', at the position of the top-centre, calculating the center position by taking the width of the window (in pixels), subtracting the width of the Pygame.surface object (in pixels) and diving that by two. The coordinates are (x, y).

173: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50))`` Here we are rendering the subheading for this GUI; 'Credits', to the display, referencing it with the variable 'self.Display'. We set the position to be slightly off-centred to the right, and down 50 pixels to prevent it from overlapping with the title.

174: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if int(1402+VisualYdisplacement) <= int(realHeight/2):`` Now we are checking to see if the value of 'VisualYdisplacement' add 1402 is less than or equal to half the height of the GUI (all values for this are truncated to the nearest integer), this is done to check when the animation is nearing a close and what to do next.

175: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, (realHeight-Credits34Height)/2))`` When the last line of the credits animation is at the centre of the GUI, we stop it from moving up any further and set the (x,y) position for the line to be exactly centred on all axis to the middle of the display, we do this using the same formula as before for the 'x' axis, and use a similar formula, but with the height values, for the 'y' position. This is also where we needed to calculate the height of the last line of the credits.

176: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement -= 60/(self.aFPS/self.Iteration)`` Now we are setting the movement speed for the animation, we take 60 and divide it by the average frame rate by dividing 'self.aFPS' by 'self.Iteration'. We store the result in the variable 'VisualYdisplacement' which we add to the 'y' position for each of the lines in the credits GUI. The speed of the animation is the difference between the values as the game runs (its subtract as we move up the display, so move closer to zero) and the displacement modifier is the result (for example, in the sequence; 2,4,6,8; 2 is the speed and the displacement modifier would be each of those values for each frame. 

177: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if EndClock >= 5:`` At the end of the animation we count up from 0 to 5 seconds, after this timer has run out, we go back to the home-screen. This if-statement will send us back to the home screen if it returns true.

178: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.

179: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

180: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ EndClock += 1/(self.aFPS/self.Iteration)`` If we reach the last section of the animation, where we render 'Thank You' centrally onscreen, we use this timer to count out 5 seconds before we move on to the home-screen. We use the same formula as we did earlier with the 'timer' variable, except this timer we count up instead of down (It can be either, it makes little difference)

181: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

182: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, 1402+VisualYdisplacement))`` If, however we are not at the end of the animation, we render the 'Thank You' line of the credits menu like we do with the others, centered on the 'x' axis, and moving up the 'y' axis based on the value of 'VisualYdisplacement', this will only run when the message is less than half way up the GUI, as it stops when the text is centred on both axis.

183: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement -= 60/(self.aFPS/self.Iteration)`` Now we are setting the movement speed for the animation, we take 60 and divide it by the average frame rate by dividing 'self.aFPS' by 'self.Iteration'. We store the result in the variable 'VisualYdisplacement' which we add to the 'y' position for each of the lines in the credits GUI. The speed of the animation is the difference between the values as the game runs (its subtract as we move up the display, so move closer to zero) and the displacement modifier is the result (for example, in the sequence; 2,4,6,8; 2 is the speed and the displacement modifier would be each of those values for each frame. 

184: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

185: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)`` This line defines the dimensions of a rectangle in Pygame, in this case the rectangle will be drawn at (0, 0) (x, y) with a width of 1280 and a height of 90. (all values here are in pixels and (0, 0) (x, y) is the top-left corner of the GUI (so thats 90 pixels DOWN)).

186: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)`` This line draws a rectangle to the display with 'self.Display', the colour to fill the rectangle is the colour of the background to Pycraft (This is a setting the user can change in the GUI in 'Settings.py') with the dimensions of the previously created Pygame Rect object called; 'cover_Rect'.

187: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))`` If the preceding if-statement is true, then we render the title centered on both the 'x' and 'y' value. The  'x' axis calculation is the same as we have seen before, but the 'y' axis calculation takes the value of 0, and (at this point in the program) will add the amount of pixels that is half of the height of the display, this we do when we first defined the variable earlier.

188: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50+IntroYDisplacement))`` Just after the title as finished its 4 second timer onscreen, the text 'credits' appears beside it and they both move up the display to the top-centre together, as it moves up the display this is the function that renders the Pygame.surface object to the display (stored in the variable 'self.Display'). We render this just off centred to the right on the 'x' axis, and at 50 pixels down the GUI, but this is affected by 'VisualYdisplacement', so its position on-screen in the 'y' axis can be adjusted as part of the animation.

189: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ IntroYDisplacement -= 90/(self.aFPS/self.Iteration)`` Here we are updating the variable 'IntroYDisplacement' by subtracting the output of the formula '90/(self.aFPS/self.Iteration)', the syntax 'self.aFPS/self.Iteration' gets the average FPS of the game. This variable is used when calculating how fast to move the title and sub-title up the screen (so that is why we subtract here, because we want to make the variable closer to 0 as we move to the top of the display).

190: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ VisualYdisplacement = realHeight`` Now we are setting the variable 'visualYdisplacement' to be the same number as the height of the display, this is dont deliberately to make sure that when there animation begins the text moves up from the bottom, but until the animation begins the text is hidden offscreen.


192: ``¬ ¬ ¬ ¬ ¬ Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)`` This line calls the subroutine 'CreateDevmodeGraph', this subroutine is responsible for drawing the graph you see at the top-right of most Pycraft GUI's. It takes the variable 'self' as a parameter, this code will return any errors, which are stored in the variable 'Message'. If there are no errors then the subroutine will return 'None'. The second parameter 'DataFont' is the currently loaded font which is used for rendering the text at the top of the graph.

193: ``¬ ¬ ¬ ¬ ¬ ¬ if not Message == None:`` This line detects if there are any errors stored in the variable 'Message'. All important errors are stored in this variable. This error detection may be moved to a thread at a later date.

194: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

195: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

196: ``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(tempFPS)`` This line of code controls how fast the GUI should refresh, defaulting to the user's preference unless the window is minimised, in which case its set to 15 FPS. All values for FPS are in (Hz) and this line of code specifies the maximum FPS of the window, but this does not guarantee that FPS.

197: ``¬ ¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

198: ``¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

199: ``¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

200: ``¬ print("You need to run this as part of Pycraft")`` if the user is running the code from PyPi, or as a raw “.py” file then this will be outputted to the terminal, however uses of the compiled “.exe” editions will not see this. This code is also printed first in-case the code below fails.

201: ``¬ import tkinter as tk`` Now we are importing the tkinter module into the project, all code here must be standalone and not rely on code in other modules in the project, this way the project can be taken apart and this should still work. We store he imported module, “Tkinter” with the name``tk``, this shortens length and all references to “Tkinter” from how on in this indented block will use this name.

202: ``¬ from tkinter import messagebox`` Here we are importing specific sections of “Tkinter”, in this case; messagebox, this module allows us to make dialogue boxes that are commonplace in Windows and Apple based devices.

203: ``¬ root = tk.Tk()`` This of code is required to make the dialogue box, which is what we want. This will create a window to the default size “Tkinter” has defined, and initialises the``messagebox`` module, which we want.

204: ``¬ root.withdraw()`` We use this code to hide the window that appears by using the previous root is the internal name for the window, as that is what the window created in the previous was stored in (as a variable).

205: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")`` Here we make our all to the``messagebox`` module, which has several pre-made dialogue boxes, we are using the``showerror`` pre-made dialogue box procedure here. We give it the caption of "Startup Fail", and then elaborate on the issue in the main body of the window, by displaying the text "You need to run this as part of Pycraft, please run the 'main.py' file".

206: ``¬ quit()`` This is Python’s way of closing the project, we normally use``sys.exit`` for this, which you will see later on, because its a bit cleaner on some IDLE’s and terminals. However to reduce the length of this project, we use the built in function here instead.

1: ``if not __name__ == "__main__":`` This checks to see if the place its called from (stored in the variable ``__name__``) is not ``"__main__"``. The string ``"__main__"`` would be the data stored in the variable ``__name__`` if the project was run on its own, which in this case we don't want so we only allow the code inside the if-statement to run if the data in ``__name__`` is not "__main__".

2: ``¬ print("Started <Pycraft_DisplayUtils>")`` Now we output data to the terminal if the program is running, this allows us to know if there are any errors preventing this module from loading, in which case the program would crash before that is outputted to the terminal, making us aware the error is in this module.

3: ``¬ class DisplayUtils:`` Now we are defining a class with a suitable name that represents what the subroutines in this class do; this allows us to group up our code to make it easier to edit, organise and debug later on, as well as saving on memory as not every function will need to be loaded at once.

4: ``¬ ¬ def __init__(self):`` Here we make sure the module is initialized correctly we do this because if we tried to call this standalone, and without the code that would stop this, then all references to variables and subroutines outside of this project would be invalid and cause issues. This is also where the variable ‘self’ is defined for all references in this class. This subroutine is a procedure, so does not return a value.

5: ``¬ ¬ ¬ pass`` Here we tell python to ignore the previous line of code that expects indented code, we use this if we don't need to put any code in this indent, this should be avoided in most situations. This is mainly used in the ``__init__`` functions for Pycraft where we may not need to run any code, but need to make sure the module is working correctly.



8: ``¬ ¬ ¬ def UpdateDisplay(self): # Run tests to make sure windows not too small`` Here we are creating a subroutine called 'UpdateDisplay', this subroutine takes only the parameter 'self', this subroutine handles the resizing and full-screen window switching in Pygame.

9: ``¬ ¬ ¬ self.Data_aFPS = []`` Here we are creating an empty array, stored in the variable 'self.Data_aFPS'. This will store the program's average FPS, which will be used later on for drawing its respective 'Devmode' graph.

10: ``¬ ¬ ¬ self.Data_CPUUsE = []`` Here we are creating an empty array, stored in the variable; 'self.Data_CPUUse'. This array will store the CPU's usage percentage    (which is seen in task manager). This will be used later on for the graphing of its respective graph in the for 'Devmode'.

11: ``¬ ¬ ¬ self.Data_eFPS = []`` Here we are creating a blank array; which we will store in the variable 'self.Data_eFPS'. This array will store vales for the current in-game FPS, which will be used later on in 'Devmode', for drawing its respective line graph.

12: ``¬ ¬ ¬ self.Data_MemUsE = []`` Here we are creating an array in the variable 'self.Data_MemUsE', which will store data about the amount of memory is currently being used by the system, which will be used later on in drawing the line graph in 'Devmode'.

13: ``¬ ¬ ¬ self.Timer = 0`` Here we are setting the variable 'self.Timer' to 0, this will be used later on in 'Devmode' for controlling the data polling rate (how often the program will get the current metrics).

14: ``¬ ¬ ¬ self.Data_aFPS_Min = 60`` On this line we are setting the variable 'self.Data_aFPS_Min' to 60, this integer is chosen because it should be easily overwritten by a smaller value as the program runs. This stores the minimum average FPS.

15: ``¬ ¬ ¬ self.Data_aFPS_Max = 1`` This stores the maximum average FPS value that has been recorded, this variable 'self.Data_aFPS_Max' is set to 1 again because this should be easily overwritten by a higher average value.


17: ``¬ ¬ ¬ self.Data_CPUUsE_Min = 60`` Here we are setting the variable 'self.Data_CPUUsE_Min' to 60, this stores the minimum CPU usage (as a percentage) so should be easily overwritten by a smaller number.

18: ``¬ ¬ ¬ self.Data_CPUUsE_Max = 1`` Here we are setting the variable 'self.Data_CPUUsE_Max' to 1, because this should be easily overwritten by a larger number (as a percentage).


20: ``¬ ¬ ¬ self.Data_eFPS_Min = 60`` Here we are setting this variable to have a value of 60. This should be easily overwritten as the program runs and stores the smallest recorded raw FPS value.

21: ``¬ ¬ ¬ self.Data_eFPS_Max = 1`` Now we set the previous variable's counterpart, the maximum recorded value of the raw FPS to 0, this should be easily overwritten and is used in calculating how the line graph in 'Devmode' on the top-right should be drawn, each of the minimum and maximum values are used for this purpose.


23: ``¬ ¬ ¬ self.Data_MemUsE_Min = 50`` Now we set the lowest value for memory usage (as a percentage) to 50, this number is chosen because it should be easily overwritten.

24: ``¬ ¬ ¬ self.Data_MemUsE_Max = 50`` Now we set the highest value of memory usage (as a percentage) to 50, this should be easily overwritten, this is used as part of the calculation for the line graph in 'Devmode'. All of the above values are chosen because they should be easily overwritten with a more appropriate value, but we need to assign the variables a value then we create them. These values will be used in calculating the dimensions for the line graph we create in 'Devmode', if you are familiar with the documentation for the benchmark, we saw a similar method there.


26: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

27: ``¬ ¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

28: ``¬ ¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()`` Now we are getting the dimensions of the monitor the display is currently on, this is used later on to calculate the dimensions for a rectangle that prevents the animation from rendering text above the title. (This isn't going to be used in later versions, its being replaced with 'realWidth').

29: ``¬ ¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

30: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

31: ``¬ ¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:`` Next we are checking to see if the variable 'self.Fullscreen' is False. This variable controls the toggling of full-screen and windowed displays, and if this if-statement returns True; the display will be in windowed mode.

32: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

33: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

34: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = True`` Now, because we are toggling the display between windowed and full-screen mode, we need to flip the value of 'self.Fullscreen' so that next time the program refreshes the display. 

35: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.RESIZABLE)`` Now we are setting the variable 'self.Display', which is where we draw all of our Pygame surfaces and objects. This line sets the display to have the dimensions of 'self.SavedWidth' and 'self.SavedHeight', in pixels. We use those variables because they store the size of the window from when it was last in windowed mode, meaning the game remembers the size of the window. Finally we also give the display thee parameter 'self.mod_Pygame__.RESIZEABLE' which allows us to re-shape and  re-size the window.

36: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:`` Next we are checking to see if the variable 'self.Fullscreen' is equal to True. This is the other part of the toggle, if this if-statement returns True then the window will be set to be fullscreen.

37: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

38: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

39: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = False`` Now we are inverting the Boolean value for the variable 'self.Fullscreen' as part of the toggle, so next time the process is called the display will switch to windowed mode.

40: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF)`` Now are creating a Pygame.surface object which will have the RESOLUTION of the current monitor, we also set some additional parameters; setting the display to fullscreen, be hardware accelerated and (this is a bug) have a double buffer (which is used in 3D applications) we store this object in the variable 'self.Display', which is what we draw all images, text, shapes and objects to when we are not in the 3D game-engine.

41: ``¬ ¬ ¬ ¬ ¬ except Exception as error:`` Here we are handling any errors that may occur whilst toggling the display between windowed and full-screen (or visa-versa) we store any errors in the variable 'error' (note this will be changed to match the new error handling guidelines in Pycraft v0.9.4.

42: ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = True`` Now, because we are toggling the display between windowed and full-screen mode, we need to flip the value of 'self.Fullscreen' so that next time the program refreshes the display. 

43: ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280`` If an error does occur, then we want to reset any variables that could have been problematic, we start by resetting the value of the variable 'self.SavedWidth' to 1280, which used to be the fixed window size for Pycraft, and is still the width all objects are rendered too, before a scale factor moves then suitably based on how much larger the window is.

44: ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720`` We also reset the value of the variable 'self.SavedHeight' to 720 (both of these variables values are in pixels), this value is chosen for the same reasons as the previous.

45: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

46: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

47: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight))`` Here we are setting the Pygame.surface object stored in 'self.Display' to the size we just specified with the resetting of those variables. Note there is no special parameters for the display here, this is designed to be a fallback option and be as simple as it can to avoid causing the error or more errors. When the user re-starts the project they will be able to re-size the GUI like normal (unless the user toggles full-screen and it works successfully).

48: ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

49: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

50: ``¬ ¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

51: ``¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

52: ``¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

53: ``¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.



56: ``¬ ¬ def SetOPENGLdisplay(self):`` This display is only used in the Benchmark GUI and will be deprecated in Pycraft v0.9.4

57: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

58: ``¬ ¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

59: ``¬ ¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()`` Now we are getting the dimensions of the monitor the display is currently on, this is used later on to calculate the dimensions for a rectangle that prevents the animation from rendering text above the title. (This isn't going to be used in later versions, its being replaced with 'realWidth').

60: ``¬ ¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

61: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

62: ``¬ ¬ ¬ ¬ ¬ ¬ if self.Fullscreen == True:`` here we are checking to see if the variable 'self.Fullscreen' is equal to Boolean True.

63: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

64: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

65: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)`` Here we are setting the display which we will store in the variable 'self.Display', this surface is created in windowed mode with the size of the previous window. We also use the parameters: 'DOUBLEBUF' which allows for the creation of a second buffer or frame. 'OPENGL', this parameter allows us to interact directly with an OpenGL environment, like the one we had created previously in the old game-engine, and the OpenGL section of the benchmark.

66: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == False:`` If the previous if-statement returned False, then we check to see if the variable 'self.Fullscreen' is equal to Boolean False, in which case the OpenGL display will be full-screen.

67: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

68: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

69: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)`` Here we are creating a Pygame.surface which we set to the RESOLUTION of the current monitor, and we use the same parameters as before but also add the 'FULLSCREEN' parameter which makes the window full-screen so sets it to the size of the monitor. Wwe also specify the 'HWSURFACE' parameter which is short for 'HardWare Surface' which enables hardware acceleration for full-screen windows, giving us a slight boost in performance.

70: ``¬ ¬ ¬ ¬ ¬ except Exception as error:`` Here we are handling any errors that may occur whilst toggling the display between windowed and full-screen (or visa-versa) we store any errors in the variable 'error' (note this will be changed to match the new error handling guidelines in Pycraft v0.9.4.

71: ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280`` If an error does occur, then we want to reset any variables that could have been problematic, we start by resetting the value of the variable 'self.SavedWidth' to 1280, which used to be the fixed window size for Pycraft, and is still the width all objects are rendered too, before a scale factor moves then suitably based on how much larger the window is.

72: ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720`` We also reset the value of the variable 'self.SavedHeight' to 720 (both of these variables values are in pixels), this value is chosen for the same reasons as the previous.

73: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

74: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

75: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)`` Here we are setting the display which we will store in the variable 'self.Display', this surface is created in windowed mode with the size of the previous window. We also use the parameters: 'DOUBLEBUF' which allows for the creation of a second buffer or frame. 'OPENGL', this parameter allows us to interact directly with an OpenGL environment, like the one we had created previously in the old game-engine, and the OpenGL section of the benchmark.

76: ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

77: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

78: ``¬ ¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

79: ``¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

80: ``¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

81: ``¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.



84: ``¬ ¬ def UpdateOPENGLdisplay(self):`` Now we are creating the subroutine 'UpdateOPENGLdisplay' which takes the parameter of 'self', this subroutine toggles full-screen and windowed modes for the OpenGL display. This subroutine will be deprecated in Pycraft v0.9.4 with the move towards ModernGL and ModernGL_window handling a greater portion of the OpenGL/3D game-engine.

85: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

86: ``¬ ¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

87: ``¬ ¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()`` Now we are getting the dimensions of the monitor the display is currently on, this is used later on to calculate the dimensions for a rectangle that prevents the animation from rendering text above the title. (This isn't going to be used in later versions, its being replaced with 'realWidth').

88: ``¬ ¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

89: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

90: ``¬ ¬ ¬ ¬ ¬ ¬ if self.Fullscreen == False:`` Next we are checking to see if the variable 'self.Fullscreen' is False. This variable controls the toggling of full-screen and windowed displays, and if this if-statement returns True; the display will be in windowed mode.

91: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

92: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

93: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = True`` Now, because we are toggling the display between windowed and full-screen mode, we need to flip the value of 'self.Fullscreen' so that next time the program refreshes the display. 

94: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)`` Here we are setting the display which we will store in the variable 'self.Display', this surface is created in windowed mode with the size of the previous window. We also use the parameters: 'DOUBLEBUF' which allows for the creation of a second buffer or frame. 'OPENGL', this parameter allows us to interact directly with an OpenGL environment, like the one we had created previously in the old game-engine, and the OpenGL section of the benchmark.

95: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == True:`` Next we are checking to see if the variable 'self.Fullscreen' is equal to True. This is the other part of the toggle, if this if-statement returns True then the window will be set to be fullscreen.

96: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

97: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

98: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = False`` Now we are inverting the Boolean value for the variable 'self.Fullscreen' as part of the toggle, so next time the process is called the display will switch to windowed mode.

99: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)`` Here we are creating a Pygame.surface which we set to the RESOLUTION of the current monitor, and we use the same parameters as before but also add the 'FULLSCREEN' parameter which makes the window full-screen so sets it to the size of the monitor. Wwe also specify the 'HWSURFACE' parameter which is short for 'HardWare Surface' which enables hardware acceleration for full-screen windows, giving us a slight boost in performance.

100: ``¬ ¬ ¬ ¬ ¬ except:`` (This needs updating to follow the guidelines of the documentation) This ignores any errors that may occur when running the main section of the benchmark, or in creating our Pygame window.

101: ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280`` If an error does occur, then we want to reset any variables that could have been problematic, we start by resetting the value of the variable 'self.SavedWidth' to 1280, which used to be the fixed window size for Pycraft, and is still the width all objects are rendered too, before a scale factor moves then suitably based on how much larger the window is.

102: ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720`` We also reset the value of the variable 'self.SavedHeight' to 720 (both of these variables values are in pixels), this value is chosen for the same reasons as the previous.

103: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

104: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

105: ``¬ ¬ ¬ ¬ ¬ ¬ self.Fullscreen = False`` Now we are inverting the Boolean value for the variable 'self.Fullscreen' as part of the toggle, so next time the process is called the display will switch to windowed mode.

106: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL)`` Here we are setting the display which we will store in the variable 'self.Display', this surface is created in windowed mode with the size of the previous window. We also use the parameters: 'DOUBLEBUF' which allows for the creation of a second buffer or frame. 'OPENGL', this parameter allows us to interact directly with an OpenGL environment, like the one we had created previously in the old game-engine, and the OpenGL section of the benchmark.

107: ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

108: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

109: ``¬ ¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

110: ``¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

111: ``¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

112: ``¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.



115: ``¬ ¬ def SetDisplay(self):`` Here we are creating the subroutine 'SetDisplay', which performs a very similar function to the 'UpdateDisplay' subroutine, both take the parameter 'self' and only return any errors that may occur. The main difference is that the two if-statements are flipped which is important for controlling how the display resizing works. 

116: ``¬ ¬ ¬ self.Data_aFPS = []`` Here we are creating an empty array, stored in the variable 'self.Data_aFPS'. This will store the program's average FPS, which will be used later on for drawing its respective 'Devmode' graph.

117: ``¬ ¬ ¬ self.Data_CPUUsE = []`` Here we are creating an empty array, stored in the variable; 'self.Data_CPUUse'. This array will store the CPU's usage percentage    (which is seen in task manager). This will be used later on for the graphing of its respective graph in the for 'Devmode'.

118: ``¬ ¬ ¬ self.Data_eFPS = []`` Here we are creating a blank array; which we will store in the variable 'self.Data_eFPS'. This array will store vales for the current in-game FPS, which will be used later on in 'Devmode', for drawing its respective line graph.

119: ``¬ ¬ ¬ self.Data_MemUsE = []`` Here we are creating an array in the variable 'self.Data_MemUsE', which will store data about the amount of memory is currently being used by the system, which will be used later on in drawing the line graph in 'Devmode'.

120: ``¬ ¬ ¬ self.Timer = 0`` Here we are setting the variable 'self.Timer' to 0, this will be used later on in 'Devmode' for controlling the data polling rate (how often the program will get the current metrics).

121: ``¬ ¬ ¬ self.Data_aFPS_Min = 60`` On this line we are setting the variable 'self.Data_aFPS_Min' to 60, this integer is chosen because it should be easily overwritten by a smaller value as the program runs. This stores the minimum average FPS.

122: ``¬ ¬ ¬ self.Data_aFPS_Max = 1`` This stores the maximum average FPS value that has been recorded, this variable 'self.Data_aFPS_Max' is set to 1 again because this should be easily overwritten by a higher average value.


124: ``¬ ¬ ¬ self.Data_CPUUsE_Min = 60`` Here we are setting the variable 'self.Data_CPUUsE_Min' to 60, this stores the minimum CPU usage (as a percentage) so should be easily overwritten by a smaller number.

125: ``¬ ¬ ¬ self.Data_CPUUsE_Max = 1`` Here we are setting the variable 'self.Data_CPUUsE_Max' to 1, because this should be easily overwritten by a larger number (as a percentage).


127: ``¬ ¬ ¬ self.Data_eFPS_Min = 60`` Here we are setting this variable to have a value of 60. This should be easily overwritten as the program runs and stores the smallest recorded raw FPS value.

128: ``¬ ¬ ¬ self.Data_eFPS_Max = 1`` Now we set the previous variable's counterpart, the maximum recorded value of the raw FPS to 0, this should be easily overwritten and is used in calculating how the line graph in 'Devmode' on the top-right should be drawn, each of the minimum and maximum values are used for this purpose.


130: ``¬ ¬ ¬ self.Data_MemUsE_Min = 50`` Now we set the lowest value for memory usage (as a percentage) to 50, this number is chosen because it should be easily overwritten.

131: ``¬ ¬ ¬ self.Data_MemUsE_Max = 50`` Now we set the highest value of memory usage (as a percentage) to 50, this should be easily overwritten, this is used as part of the calculation for the line graph in 'Devmode'. All of the above values are chosen because they should be easily overwritten with a more appropriate value, but we need to assign the variables a value then we create them. These values will be used in calculating the dimensions for the line graph we create in 'Devmode', if you are familiar with the documentation for the benchmark, we saw a similar method there.


133: ``¬ ¬ ¬ self.Data_CPUUsE_Min = 50`` Here we are setting the variable 'self.Data_CPUUsE_Min' to 50, this stores the minimum CPU usage (as a percentage) so should be easily overwritten by a smaller number.

134: ``¬ ¬ ¬ self.Data_CPUUsE_Max = 50`` Here we are setting the variable 'self.Data_CPUUsE_Max' to 50, because this should be easily overwritten by a larger number (as a percentage).

135: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

136: ``¬ ¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

137: ``¬ ¬ ¬ ¬ ¬ ¬ FullscreenX, FullscreenY = self.mod_Pyautogui__.size()`` Now we are getting the dimensions of the monitor the display is currently on, this is used later on to calculate the dimensions for a rectangle that prevents the animation from rendering text above the title. (This isn't going to be used in later versions, its being replaced with 'realWidth').

138: ``¬ ¬ ¬ ¬ ¬ ¬ if self.Fullscreen == True:`` here we are checking to see if the variable 'self.Fullscreen' is equal to Boolean True.

139: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

140: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

141: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight), self.mod_Pygame__.RESIZABLE)`` Now we are setting the variable 'self.Display', which is where we draw all of our Pygame surfaces and objects. This line sets the display to have the dimensions of 'self.SavedWidth' and 'self.SavedHeight', in pixels. We use those variables because they store the size of the window from when it was last in windowed mode, meaning the game remembers the size of the window. Finally we also give the display thee parameter 'self.mod_Pygame__.RESIZEABLE' which allows us to re-shape and  re-size the window.

142: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.Fullscreen == False:`` If the previous if-statement returned False, then we check to see if the variable 'self.Fullscreen' is equal to Boolean False, in which case the OpenGL display will be full-screen.

143: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

144: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

145: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((FullscreenX, FullscreenY), self.mod_Pygame__.FULLSCREEN|self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.DOUBLEBUF)`` Now are creating a Pygame.surface object which will have the RESOLUTION of the current monitor, we also set some additional parameters; setting the display to fullscreen, be hardware accelerated and (this is a bug) have a double buffer (which is used in 3D applications) we store this object in the variable 'self.Display', which is what we draw all images, text, shapes and objects to when we are not in the 3D game-engine.

146: ``¬ ¬ ¬ ¬ ¬ except Exception as error:`` Here we are handling any errors that may occur whilst toggling the display between windowed and full-screen (or visa-versa) we store any errors in the variable 'error' (note this will be changed to match the new error handling guidelines in Pycraft v0.9.4.

147: ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedWidth = 1280`` If an error does occur, then we want to reset any variables that could have been problematic, we start by resetting the value of the variable 'self.SavedWidth' to 1280, which used to be the fixed window size for Pycraft, and is still the width all objects are rendered too, before a scale factor moves then suitably based on how much larger the window is.

148: ``¬ ¬ ¬ ¬ ¬ ¬ self.SavedHeight = 720`` We also reset the value of the variable 'self.SavedHeight' to 720 (both of these variables values are in pixels), this value is chosen for the same reasons as the previous.

149: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.quit()`` Here we are forcing the currently open display to close, if none is open then this has no effect.

150: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.init()`` Next we need to re-initiate Pygame as we have forced the display module to become 'uninitialised', this also refreshes any other Pygame modules that may have been 'uninitialised' during the running of the program.

151: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((self.SavedWidth, self.SavedHeight))`` Here we are setting the Pygame.surface object stored in 'self.Display' to the size we just specified with the resetting of those variables. Note there is no special parameters for the display here, this is designed to be a fallback option and be as simple as it can to avoid causing the error or more errors. When the user re-starts the project they will be able to re-size the GUI like normal (unless the user toggles full-screen and it works successfully).

152: ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

153: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

154: ``¬ ¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

155: ``¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

156: ``¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

157: ``¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.



160: ``¬ ¬ def GenerateMinDisplay(self, width, height):`` Here we are creating a subroutine called 'GenerateMinDisplay', which takes 3 parameters, 'self' which most subroutines call for is always asked first, then we ask for the variables 'width' and 'height', these parameters are used in this function which is called when one or more of the dimensions of the display is less than 1280 (for the width) and 720 (or the height) in pixels, the width and height parameters are asked so that we can reset one dimension without resetting the other axis, unless they are both too small. This subroutine will return an error should one occur.

161: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

162: ``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((width, height), self.mod_Pygame__.RESIZABLE)`` Here we are resetting the size of the display to the dimensions (in pixels) of the last two parameters and because we know that the only way the display can be resized is if the display is not in fullscreen, so we can add the usual parameter of 'RESIZABLE'.

163: ``¬ ¬ ¬ ¬ ¬ icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()`` Now we are loading the image file (in the .jpg file format) for the icon at the top corner of the display and in the taskbar (or dock on apple devices). We add the '.convert()' format at the end because it creates a copy of the surface that is more optimised for on screen drawing. We store this image in the variable 'icon'.

164: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_icon(icon)`` Next we are setting the display's icon (the image at the top, next to the caption on windows, and the image that is displayed in the taskbar for that display. On Apple devices it sets the time you will see in the dock). 

165: ``¬ ¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

166: ``¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

167: ``¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

168: ``¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.



171: ``¬ ¬ def GetDisplayLocation(self):`` Here we are creating a subroutine called 'GetDisplayLocation' which takes only the parameter of 'self', this subroutine will only return the position (in pixels) of the currently active PYGAME display. This subroutine will not return an error, should one occur.

172: ``¬ ¬ ¬ hwnd = self.mod_Pygame__.display.get_wm_info()["window"]`` Here we are calling a Pygame function that will get the details of the currently active Pygame display, we only want the specifics on the 'window' parameter, so we add the '["window"]' key to filter out the unnecessary information, the resulting data is stored in the variable 'hwnd'.


174: ``¬ ¬ ¬ prototype = self.mod_Ctypes__.WINFUNCTYPE(self.mod_Ctypes__.wintypes.BOOL, self.mod_Ctypes__.wintypes.HWND, self.mod_Ctypes__.POINTER(self.mod_Ctypes__.wintypes.RECT))`` Here we are calling a Ctypes function that allows us to interact directly with code written in C, in this case we are getting data from the SDL library, this, stored in the variable 'prototype' sets up this process, we interface with a C library later on, this simplifies the call.

175: ``¬ ¬ ¬ paramflags = (1, "hwnd"), (2, "lprect")`` Now we are specifying the data we want to return back to the python program when we go through the C library, in this case we want to get the data at the keys 'hwnd' and 'lprect'.


177: ``¬ ¬ ¬ GetWindowRect = prototype(("GetWindowRect", self.mod_Ctypes__.windll.user32), paramflags)`` Here we are using the Ctypes library, with the two variables we have just defined 'prototype' and 'paramflags' which shorten the length of the line. We want to access data in the 'user32' section of 'windll'.


179: ``¬ ¬ ¬ rect = GetWindowRect(hwnd)`` Here we are going through the data we received from the call into the C programming language, here we are getting the position of the display (EXCLUDING THE CAPTION/BORDER OF THE WINDOW), the resultant dimensions are stored in the variable 'rect'.


181: ``¬ ¬ ¬ return rect.left+8, rect.top+31`` Finally we go through the variable 'rect' and get the position from the top-left hand corner of the display. This data is returned to the caller of this subroutine.



184: ``¬ ¬ def GetPlayStatus(self):`` Here we are creating a subroutine 'GetPlayStatus', this takes only the parameter of 'self', and does not return any errors that may occur, instead it returns an integer value that is used as the FPS (in Hz) for the display. This function changes the display's FPS based on if the display is minimised (to 15 FPS) or currently active (in which case we use the user's set FPS).

185: ``¬ ¬ ¬ if self.mod_Pygame__.display.get_active() == True:`` Now we are using Pygame to detect if the display is active, this returns a boolean value and will return 'True' is the display is not minimised and 'False' when the display is minimised, so not active.

186: ``¬ ¬ ¬ ¬ tempFPS = self.FPS`` This is used to temporarily store the game's target FPS, this is used later to slow the game down when minimised.

187: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).unpause()`` Here we are allowing Pygame's audio channel 2 to play, if anything is loaded, this will play the main soundtrack you hear at the start, if the user has allowed music playback in settings. This does not toggle the sound, (as in every time it's called it pauses or plays the sound, inverting the previous state) so can be called multiple times (although not in the most efficient situation) and will not keep changing toggling sound playback.

188: ``¬ ¬ ¬ ¬ ¬ if self.mod_Pygame__.mixer.Channel(2).get_busy() == 0 and self.LoadMusic == True:`` Here we are checking to see if the Pygame audio channel we just unpaused is now playing sound, this will return a boolean value. In this if-statement we also check to see if the variable 'self.LoadMusic' is True, this variable controls if we should load and allow for sound to load, this controls the loading of the music in the 2D game-engine. Putting this all together, we need to check that there is NOT playing and we are allowed to load and play the audio files.

189: ``¬ ¬ ¬ ¬ ¬ ¬ if self.music == True and self.CurrentlyPlaying == None:`` Now we are using another double-condition  if-statement to check to see if the variable 'self.music' is set to True. (This controls the playback of all sound files flagged as 'music'). We also check to see if there is sound currently playing, to do this we must specify in the 'self.CurrentlyPlaying' variable the sound file that's currently playing when we play a sound with the 'music' flag. BOTH these conditions need to be 'True' for this if-statement to return 'True'.

190: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.CurrentlyPlaying = "InvSound"`` Because we are now allowing the music sound we hear in the 2D game-engine to play, we must specify this in the variable 'self.CurrentlyPlaying' otherwise the 2D game engine may attempt to load the object multiple times causing unnecessary device strain.

191: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.LoadMusic = False`` We also set the variable 'self.LoadMusic' to False, which is also an attempt to prevent sound from loading multiple times.

192: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ MusicThread = self.mod_Threading__.Thread(target=self.mod_SoundUtils__.PlaySound.PlayInvSound, args=(self,))`` Now we are making a call to the 'SoundUtils.py' and the 'PlayInvSound' module, which takes the argument 'self'. We make this call in the Threading built-in Python module because otherwise the program will be laggy as the object is loaded, and as such we want to do this in a separate thread.

193: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ MusicThread.start()`` Now we are starting the thread which we stored in the variable 'MusicThread', which we talked about on a previous line. This thread will end automatically once the sound is loaded, and we can still access the function in Pygame to control the music through the global variable 'self'.

194: ``¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

195: ``¬ ¬ ¬ ¬ ¬ self.LoadMusic = True`` If no music in the Pygame sound channel 2 is playing (Channel 2 is the location of the long, 2D game-engine music) then we allow the game to attempt to load and play the sound by setting the variable 'self.LoadMusic' to True, this doesn't allow the sound to play on its own, but will allow the music to play if the user has set the setting for allowing music to play (which is stored in the variable 'self.music'.

196: ``¬ ¬ ¬ ¬ ¬ tempFPS = 15`` Here we are setting the variable 'tempFPS' to the value of 15, this controls the refresh rate of the game in Hz, and when the game is minimised (which is what this subroutine checks) we set the game's FPS to 15.

197: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.mixer.Channel(2).pause()`` This line stops the sound in channel 2 from playing by pausing it, this sound is the background track that plays when not in game (This is controlled by the user's setting). If no sound is playing then this has no effect.

198: ``¬ ¬ ¬ ¬ return tempFPS`` Finally we return the variable 'tempFPS' to the caller of this subroutine. This variable will either be 15 if the display is minimised or it will be the user's setting in 'Settings.py'.


200: ``else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

201: ``¬ print("You need to run this as part of Pycraft")`` if the user is running the code from PyPi, or as a raw “.py” file then this will be outputted to the terminal, however uses of the compiled “.exe” editions will not see this. This code is also printed first in-case the code below fails.

202: ``¬ import tkinter as tk`` Now we are importing the tkinter module into the project, all code here must be standalone and not rely on code in other modules in the project, this way the project can be taken apart and this should still work. We store he imported module, “Tkinter” with the name``tk``, this shortens length and all references to “Tkinter” from how on in this indented block will use this name.

203: ``¬ from tkinter import messagebox`` Here we are importing specific sections of “Tkinter”, in this case; messagebox, this module allows us to make dialogue boxes that are commonplace in Windows and Apple based devices.

204: ``¬ root = tk.Tk()`` This of code is required to make the dialogue box, which is what we want. This will create a window to the default size “Tkinter” has defined, and initialises the``messagebox`` module, which we want.

205: ``¬ root.withdraw()`` We use this code to hide the window that appears by using the previous root is the internal name for the window, as that is what the window created in the previous was stored in (as a variable).

206: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")`` Here we make our all to the``messagebox`` module, which has several pre-made dialogue boxes, we are using the``showerror`` pre-made dialogue box procedure here. We give it the caption of "Startup Fail", and then elaborate on the issue in the main body of the window, by displaying the text "You need to run this as part of Pycraft, please run the 'main.py' file".

207: ``¬ quit()`` This is Python’s way of closing the project, we normally use``sys.exit`` for this, which you will see later on, because its a bit cleaner on some IDLE’s and terminals. However to reduce the length of this project, we use the built in function here instead.

1: ``if not __name__ == "__main__":`` This checks to see if the place its called from (stored in the variable ``__name__``) is not ``"__main__"``. The string ``"__main__"`` would be the data stored in the variable ``__name__`` if the project was run on its own, which in this case we don't want so we only allow the code inside the if-statement to run if the data in ``__name__`` is not "__main__".

2: ``¬ print("Started <Pycraft_DrawingUtils>")`` Now we output data to the terminal if the program is running, this allows us to know if there are any errors preventing this module from loading, in which case the program would crash before that is outputted to the terminal, making us aware the error is in this module.

3: ``¬ class DrawRose:`` Now we are defining a class with a suitable name that represents what the subroutines in this class do; this allows us to group up our code to make it easier to edit, organise and debug later on, as well as saving on memory as not every function will need to be loaded at once.

4: ``¬ ¬ def __init__(self):`` Here we make sure the module is initialized correctly we do this because if we tried to call this standalone, and without the code that would stop this, then all references to variables and subroutines outside of this project would be invalid and cause issues. This is also where the variable ‘self’ is defined for all references in this class. This subroutine is a procedure, so does not return a value.

5: ``¬ ¬ ¬ pass`` Here we tell python to ignore the previous line of code that expects indented code, we use this if we don't need to put any code in this indent, this should be avoided in most situations. This is mainly used in the ``__init__`` functions for Pycraft where we may not need to run any code, but need to make sure the module is working correctly.


7: ``¬ ¬ def CreateRose(self, xScaleFact, yScaleFact, coloursARRAY):`` Here we are creating the subroutine called 'CreateRose', this is called on the home screen and draws the graphic there. This subroutine takes 4 parameters, the first is 'self', which is used to access modules and global variables. 'xScaleFact', which stores how much larger on the 'x' axis the display is, this is needed for when the user resizes the display, or sets the display to fullscreen to control how things should be displaced on the 'x' axis. The 3rd parameter, 'yScaleFact' does a similar thing to the variable 'xScaleFact'. storing how much larger on the 'y' axis the display is. For these calculations we use the display's original size, (1280x720) which is the default location to draw data on all GUIs. Finally the subroutine takes the parameter of 'coloursARRAY', which stores an array of colours for each line, this is used to animate the graphic and will be tweaked in a future update.

8: ``¬ ¬ ¬ if coloursARRAY == False:`` Here we are checking to see if the variable 'coloursARRAY is actually an array, this is used in-case the user has disabled this effect in settings (coming soon!) or if the home screen is loading or just getting set-up, in which case the animation hasn't started yet, if this is the case then the next few lines of code run.

9: ``¬ ¬ ¬ ¬ coloursARRAY = []`` We now set 'coloursARRAY' to contain an array data structure instead of a boolean value. 

10: ``¬ ¬ ¬ ¬ ¬ for i in range(32):`` Then we iterate over each of the lines in the graphic (there are 32).

11: ``¬ ¬ ¬ ¬ ¬ ¬ coloursARRAY.append(self.ShapeCol)`` And for each of the lines in the graphic, we assign a colour value related to the user's selected theme, because the animation is not currently active, we set the colour value to the default value of the colour relating to shapes in the theme.


13: ``¬ ¬ ¬ defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)]`` Here we are defining an array what stores the positions onscreen where we want to draw each of the points of our octagon, each position is stored as a tuple in the format: (x,y).

14: ``¬ ¬ ¬ self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2)`` Here we are using Pygame's built in draw function (which we use in settings and elsewhere to draw shapes), this function takes the display we want to draw to as our first parameter, the colour of the shape as the second parameter (which we take from the user's current theme), then it asks for the points of the shape, this function can take varying amounts of points to draw different shapes, for example 6 sets of coordinates would draw a hexagon, for this we give the function the variable where we stored our array of points. Finally we set the width of the line, this is in pixels.


16: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[0], (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

17: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[1], (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

18: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[2], (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

19: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[3], (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

20: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[4], (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

21: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[5], (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

22: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[6], (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

23: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[7], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

24: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[8], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

25: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[9], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

26: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[10], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

27: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[11], (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

28: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[12], (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

29: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[13], (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

30: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[14], (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

31: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[15], (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

32: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[16], (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

33: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[17], (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

34: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[18], (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

35: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[19], (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

36: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[20], (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

37: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[21], (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

38: ``¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[22], (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

39: ``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[23], (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

40: ``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[24], (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

41: ``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[25], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

42: ``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[25], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

43: ``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[27], (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

44: ``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[28], (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

45: ``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[29], (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

46: ``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[30], (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.

47: ``¬ ¬ ¬ ¬ self.mod_Pygame__.draw.line(self.Display, coloursARRAY[31], (575*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)`` Here we go through and draw each of the lines between two points, this is done using Pygame's draw function, which takes the first parameter as the Pygame.surface to draw on, the second parameter is the colour of the shape (which is unique for each line for the animation), then we define the two points to draw the line between and finally set the width of the line to 2 pixels. This process is repeated for each of the lines, however points will be used multiple times in different lines due to the nature of the graphic, but no two lines should have the same TWO coordinates.


49: ``¬ class GenerateGraph:`` Here we are creating a new class in 'DrawingUtils.py' which we call 'GenerateGraph', this class is responsible for the collection, gathering and displaying of system and program telemetry and drawing the line graph which we observe in 'Devmode'.

50: ``¬ ¬ def __init__(self):`` Here we make sure the module is initialized correctly we do this because if we tried to call this standalone, and without the code that would stop this, then all references to variables and subroutines outside of this project would be invalid and cause issues. This is also where the variable ‘self’ is defined for all references in this class. This subroutine is a procedure, so does not return a value.

51: ``¬ ¬ ¬ pass`` Here we tell python to ignore the previous line of code that expects indented code, we use this if we don't need to put any code in this indent, this should be avoided in most situations. This is mainly used in the ``__init__`` functions for Pycraft where we may not need to run any code, but need to make sure the module is working correctly.


53: ``¬ ¬ def CreateDevmodeGraph(self, DataFont):`` Here we are creating a subroutine called 'CreateDevmodeGraph', this takes 2 parameters, the global variable 'self', and the font to use to render the text above the line graph in 'Devmode'. This subroutine does not usually return anything, but will return an error should one occur. This function is responsible for handling, collecting and drawing telemetry data for the system and program in 'Devmode'.

54: ``¬ ¬ ¬ if self.Devmode == 10:`` Here we are checking to see if the integer value in the variable 'Devmode' is equal to 10, this means that the user has enabled 'Devmode' and we should start collecting system and program telemetry and draw the line graph, unless the user enables this feature, or they use 'Benchmark', this is one of a few situations where the program will attempt to get system information (information about the program it's-self is required for the program to run safely).

55: ``¬ ¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

56: ``¬ ¬ ¬ ¬ ¬ ¬ if ((self.realWidth/2)+100)+self.Timer >= self.realWidth:`` Here we are checking to see if the 'leading edge' of the line graph has now left the screen, this is done by comparing the size of the display to the result of a calculation that takes half the size of the screen, adds 100 to it and then how far across the 'leading-edge' is in the graph (regulated by the variable 'self.Time'). Should this if-statement return True, the line graph will return to the start and the previous line graph will be erased.

57: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS = []`` Here we are creating an empty array, stored in the variable 'self.Data_aFPS'. This will store the program's average FPS, which will be used later on for drawing its respective 'Devmode' graph.

58: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE = []`` Here we are creating an empty array, stored in the variable; 'self.Data_CPUUse'. This array will store the CPU's usage percentage    (which is seen in task manager). This will be used later on for the graphing of its respective graph in the for 'Devmode'.

59: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS = []`` Here we are creating a blank array; which we will store in the variable 'self.Data_eFPS'. This array will store vales for the current in-game FPS, which will be used later on in 'Devmode', for drawing its respective line graph.

60: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE = []`` Here we are creating an array in the variable 'self.Data_MemUsE', which will store data about the amount of memory is currently being used by the system, which will be used later on in drawing the line graph in 'Devmode'.

61: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Timer = 0`` Here we are setting the variable 'self.Timer' to 0, this will be used later on in 'Devmode' for controlling the data polling rate (how often the program will get the current metrics).

62: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Min = 60`` On this line we are setting the variable 'self.Data_aFPS_Min' to 60, this integer is chosen because it should be easily overwritten by a smaller value as the program runs. This stores the minimum average FPS.

63: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Max = 1`` This stores the maximum average FPS value that has been recorded, this variable 'self.Data_aFPS_Max' is set to 1 again because this should be easily overwritten by a higher average value.


65: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = 60`` Here we are setting the variable 'self.Data_CPUUsE_Min' to 60, this stores the minimum CPU usage (as a percentage) so should be easily overwritten by a smaller number.

66: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = 1`` Here we are setting the variable 'self.Data_CPUUsE_Max' to 1, because this should be easily overwritten by a larger number (as a percentage).


68: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Min = 60`` Here we are setting this variable to have a value of 60. This should be easily overwritten as the program runs and stores the smallest recorded raw FPS value.

69: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Max = 1`` Now we set the previous variable's counterpart, the maximum recorded value of the raw FPS to 0, this should be easily overwritten and is used in calculating how the line graph in 'Devmode' on the top-right should be drawn, each of the minimum and maximum values are used for this purpose.


71: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Min = 50`` Now we set the lowest value for memory usage (as a percentage) to 50, this number is chosen because it should be easily overwritten.

72: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = 50`` Now we set the highest value of memory usage (as a percentage) to 50, this should be easily overwritten, this is used as part of the calculation for the line graph in 'Devmode'. All of the above values are chosen because they should be easily overwritten with a more appropriate value, but we need to assign the variables a value then we create them. These values will be used in calculating the dimensions for the line graph we create in 'Devmode', if you are familiar with the documentation for the benchmark, we saw a similar method there.


74: ``¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Min = 50`` Here we are setting the variable 'self.Data_CPUUsE_Min' to 50, this stores the minimum CPU usage (as a percentage) so should be easily overwritten by a smaller number.

75: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_CPUUsE_Max = 50`` Here we are setting the variable 'self.Data_CPUUsE_Max' to 50, because this should be easily overwritten by a larger number (as a percentage).


77: ``¬ ¬ ¬ ¬ ¬ BackingRect = self.mod_Pygame__.Rect((self.realWidth/2)+100, 0, self.realWidth, 200)`` Here we are creating the background rectangle for the line graph, this is done with a similar process to the one used in the benchmark, here we are creating a set of points, which we store in the variable 'BackingRect', we store the points in the format 'x1, y1, x2 y2' where each two values are points like '(x,y)' in pixels. The first set of coordinates define the top-left corner. The 'x' axis for the first point takes the position half-way across the GUI (using 'self.realWidth/2'), then we add 100 pixels, we do this so that the rectangle doesn't overlap with the subtitle in MOST cases (there is a better solution coming soon!), then because we want the rectangle to start at the top of the GUI, we set the 'y' position to 0. For the second set of coordinates, we start with the 'x' axis, which we set the the variable 'self.realWidth' which stores the exact width of the display in pixels, this means the rectangle will stretch right to the right-hand-size of the GUI, then we set the rectangle to go down 200 pixels from the top, (this coordinate specifies the bottom right position).

78: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, BackingRect)`` Now we go through and draw the rectangle which we just created the points for. We draw the rectangle to the display using 'self.Display', then we specify the colour of the shape, which we set to an appropriate colour from the user's theme, then we add our points by calling the variable 'BackingRect' which stores the points we made earlier. NOT SPECIFYING A FOURTH PARAMETER (LINE WIDTH) HERE MEANS THE RECTANGLE IS FILLED.


80: ``¬ ¬ ¬ ¬ ¬ if self.Timer >= 2:`` Now we need to check to see if a certain amount of time has passed, for this program, time is stored in the variable 'self.Timer', and this if-statement is used to prevent the lines for the line graph being drawn directly to the edge of the rectangle we just created. This is done for graphical reasons.

81: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_aFPS_Max)*(self.aFPS/(self.Iteration))])`` Now, because we will be drawing 3 lines on the line graph, and we do this with Pygame's 'pygame.draw.lines', we need to store each of the points for the line in a way that Pygame's draw subroutine will understand, to do this we append the coordinates for each point on the line in a corresponding array. This this, the first line we are storing the coordinates for the line that represents the average FPS of the program. With each iteration of this program, we add a new point to the array until we reach a position where the current point is off the right hand side of the display, which is when we reset the graph and start again. Now this next bit of this documentation for this line of code will be about understanding the calculations of this line which we can observe, as well as how we are organising the data. To start with, we store the data in a 2D array, each of the groups of elements are coordinates; they are stored in the format [[x,y], [x,y], [x,y]]. To calculate the 'x' axis position, we perform an identical calculation to what we used earlier when calculating the points for the 'BackingRect' variable (The 'x' axis for the first point takes the position half-way across the GUI (using 'self.realWidth/2'), then we add 100 pixels). Then for the 'y' axis we start with how we would calculate a percentage, taking 100 and dividing it by the largest value (which we store in the variable 'self.Data_aFPS_Max', more on that later), then we multiply the small decimal result we would receive by the current average FPS of the program, which we do with the calculation, '(self.aFPS/(self.Iteration))', this calculation is also seen elsewhere in the program. Then this will give us a value that shows what the current average FPS is RELATIVE to the maximum recorded value, unfortunately we are not finished because although this would work if you plugged the result into a graphing program, (like Matplotlib), we need to flip the results by taking 200 away with that value we have just calculated, this is because for Pygame, coordinates start from the top-left, in your typical graphing program, the coordinates would start from the bottom left, and because the 'y' position is the only coordinate here that flips, we need to do the same for this graph, but only on the 'y' axis.

82: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_eFPS_Max)*int(self.eFPS)])`` Now, because we will be drawing 3 lines on the line graph, and we do this with Pygame's 'pygame.draw.lines', we need to store each of the points for the line in a way that Pygame's draw subroutine will understand, to do this we append the coordinates for each point on the line in a corresponding array. This this, the second line we are storing the coordinates for the line that represents the current FPS of the program. With each iteration of this program, we add a new point to the array until we reach a position where the current point is off the right hand side of the display, which is when we reset the graph and start again. Now this next bit of this documentation for this line of code will be about understanding the calculations of this line which we can observe, as well as how we are organising the data. To start with, we store the data in a 2D array, each of the groups of elements are coordinates; they are stored in the format [[x,y], [x,y], [x,y]]. To calculate the 'x' axis position, we perform an identical calculation to what we used earlier when calculating the points for the 'BackingRect' variable (The 'x' axis for the first point takes the position half-way across the GUI (using 'self.realWidth/2'), then we add 100 pixels). Then for the 'y' axis we start with how we would calculate a percentage, taking 100 and dividing it by the largest value (which we store in the variable 'self.Data_eFPS_Max', more on that later), then we multiply the small decimal result we would receive by the current FPS of the program (as an integer, this value would otherwise have a very long decimal and its not necessary that we calculate the value to such a small decimal as the line will be to the nearest pixel either way). Then this will give us a value that shows what the current FPS is RELATIVE to the maximum recorded value, unfortunately we are not finished because although this would work if you plugged the result into a graphing program, (like Matplotlib), we need to flip the results by taking 200 away with that value we have just calculated, this is because for Pygame, coordinates start from the top-left, in your typical graphing program, the coordinates would start from the bottom left, and because the 'y' position is the only coordinate here that flips, we need to do the same for this graph, but only on the 'y' axis.

83: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE.append([((self.realWidth/2)+100)+self.Timer, 200-(100/self.Data_MemUsE_Max)*(100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available])`` Now, because we will be drawing 3 lines on the line graph, and we do this with Pygame's 'pygame.draw.lines', we need to store each of the points for the line in a way that Pygame's draw subroutine will understand, to do this we append the coordinates for each point on the line in a corresponding array. This this, the third and final line for this section (the fourth line for the CPU is done elsewhere in a thread) we are storing the coordinates for the line that represents the current memory usage of the program. With each iteration of this program, we add a new point to the array until we reach a position where the current point is off the right hand side of the display, which is when we reset the graph and start again. Now this next bit of this documentation for this line of code will be about understanding the calculations of this line which we can observe, as well as how we are organising the data. To start with, we store the data in a 2D array, each of the groups of elements are coordinates; they are stored in the format [[x,y], [x,y], [x,y]]. To calculate the 'x' axis position, we perform an identical calculation to what we used earlier when calculating the points for the 'BackingRect' variable (The 'x' axis for the first point takes the position half-way across the GUI (using 'self.realWidth/2'), then we add 100 pixels). Then for the 'y' axis we start with how we would calculate a percentage, taking 100 and dividing it by the maximum recorded amount of memory the system has used during the running of this set of data collection (more on that later), then we multiply the small decimal result we would receive by the current percentage of RAM that is being ued by the system (as an percentage). Then this will give us a value that shows what the current RAM usage is RELATIVE to the maximum recorded value, unfortunately we are not finished because although this would work if you plugged the result into a graphing program, (like Matplotlib), we need to flip the results by taking 200 away with that value we have just calculated, this is because for Pygame, coordinates start from the top-left, in your typical graphing program, the coordinates would start from the bottom left, and because the 'y' position is the only coordinate here that flips, we need to do the same for this graph, but only on the 'y' axis.


85: ``¬ ¬ ¬ ¬ ¬ if (self.aFPS/(self.Iteration)) > self.Data_aFPS_Max:`` Here we are checking to see if the current average FPS (remember this value changes only one per frame so we can run the equation multiple times and not need to worry about different values, although we do sacrifice a small amount of efficiency), is greater than the current maximum FPS, this is needed for the calculation earlier.

86: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Max = (self.aFPS/(self.Iteration))`` If the current average FPS (abbreviated to 'aFPS') is in fact greater than the previously recorded maximum, then we replace the maximum with the current average FPS, which is larger.

87: ``¬ ¬ ¬ ¬ ¬ ¬ elif (self.aFPS/(self.Iteration)) < self.Data_aFPS_Min:`` Here we are checking to see if the average FPS is lower than the minimum recorded average FPS, which we store in the variable 'self.Data_aFPS_Min'.

88: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_aFPS_Min = (self.aFPS/(self.Iteration))`` Here we are setting the minimum recorded average FPS to the current average FPS, because its smaller and the variable 'self.Data.aFPS_Min' needs to store the smallest average FPS.


90: ``¬ ¬ ¬ ¬ ¬ if self.eFPS > self.Data_eFPS_Max:`` Here we are doing a similar thing as before, except this time we are checking to see if the current FPS of the program is greater than the previously recorded max in 'self.Data_eFPS_Max'

91: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Max = self.eFPS`` If the current FPS (stored in the variable 'eFPS') is bigger than the previously recorded max in 'self.Data_eFPS_Max', then we update the value stored in this variable to the current FPS.

92: ``¬ ¬ ¬ ¬ ¬ ¬ elif self.eFPS < self.Data_eFPS_Min:`` Here we are checking to see if the current FPS of the running program is smaller than the previously recorded smallest value; stored in 'self.Data_eFPS_Min', as the value cannot be both the largest and smallest value we use an 'elif' here so that this is only checked if the previous if-statement is not met.

93: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_eFPS_Min = self.eFPS`` Now we set the minimum FPS to the current FPS after we have checked to see if it is smaller, we only update the value in the variable 'self.Data_eFPS_Min' if the above if-statement is True.


95: ``¬ ¬ ¬ ¬ ¬ if (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available > self.Data_MemUsE_Max:`` Here we are checking to see if the current percentage of memory free (and we mean current, if we call either 'psutil.virtual_memory().total' or 'psutil.virtual_memory().available' again it could give a different value, even in the same iteration of the program, this will be fixed during Pycraft v0.9.4-2 and later versions) is greater than the previously recorded maximum amount of memory the system had free; which we store in the variable 'self.Data_MemUsE_Max'. This is stored as a percentage, but it is very unlikely to be either 0 or 100 as that would mean either no or all the system memory is used respectively, although the first is possible in high memory machines. The program can handle these extreme values.

96: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available`` Now we are updating the variable 'self.Data_MemUsE_Max' with the current percentage of free memory, however this will likely be a slightly different value to the one we received in the if-statement as we have since called that subroutine again, this is fixed in a later version (pycraft v0.9.4-2 onwards) but is unlikely to cause issues (although the memory and CPU line on the graph is currently broken. This has been fixed and will feature in versions of Pycraft greater than Pycraft v0.9.4-1).

97: ``¬ ¬ ¬ ¬ ¬ ¬ elif (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available < self.Data_MemUsE_Max:`` Here we are checking to see if the current percentage of memory not being used by the system is smaller than the current smallest value stored in the variable; 'self.Data_MemUse_Min'. (evidently there is a bug here, this is why the line graph for this telemetry is broken, at time of writing however this is fixed in Pycraft v0.9.4-2).

98: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Data_MemUsE_Max = (100/self.mod_Psutil__.virtual_memory().total)*self.mod_Psutil__.virtual_memory().available`` Now we are updating the variable 'self.Data_MemUsE_Max' with the current percentage of free memory, however this will likely be a slightly different value to the one we received in the if-statement as we have since called that subroutine again, this is fixed in a later version (pycraft v0.9.4-2 onwards) but is unlikely to cause issues (although the memory and CPU line on the graph is currently broken. This has been fixed and will feature in versions of Pycraft greater than Pycraft v0.9.4-1).


100: ``¬ ¬ ¬ ¬ ¬ self.Timer += 0.2`` Now after each iteration of the game where 'Devmode' is equal to 10, so 'Devmode' is enabled, we increase the variable 'self.Timer', by 0.2, this controls how fast the graph moves across the screen and its spacing. This variable is used heavily both in and out of this program (also in 'ThreadingUtils' with the CPU line graph counterpart) and in most of the line graph calculations.

101: ``¬ ¬ ¬ ¬ ¬ ¬ if self.Timer >= 5:`` Because Pygame's multi-point 'lines' subroutine requires there to be at least 2 points in order to draw the line, if we attempted to draw the line on the first run of the project with 'Devmode' enabled, it would have at most 1 point and cause the program to crash, as a result we delay the drawing of the lines until the variable 'self.Timer' is greater than or equal to 5, this does NOT correlate to 5 seconds or millisecond or any form of real-world time.

102: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 0), False, self.Data_aFPS)`` Now we draw 3 of the 4 line graphs we have data for, we draw the fourth later on in a different condition because we handle that slightly differently, but for this one, which relates to the average FPS (or 'aFPS') of the game. We first specify the Pygame.surface object to draw the line to (this will, in most circumstances be 'self.Display'), then for the second parameter we specify the colour of the line, this controls colour for the entire line, and in this case we set the value to red (or '255, 0, 0' which is the same), then we specify the Boolean value False here because we do not want the start and end points of the line to connect, and finally we specify the array of points we want to use as plots for the line, in this case we reference 'self.Data_aFPS'.

103: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 255, 0), False, self.Data_eFPS)`` This relates to the current FPS (or 'eFPS') of the game. We first specify the Pygame.surface object to draw the line to (this will, in most circumstances be 'self.Display'), then for the second parameter we specify the colour of the line, this controls colour for the entire line, and in this case we set the value to green (or '0, 255, 0' which is the same), then we specify the Boolean value False here because we do not want the start and end points of the line to connect, and finally we specify the array of points we want to use as plots for the line, in this case we reference 'self.Data_eFPS'.

104: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (0, 0, 255), False, self.Data_MemUsE)`` This relates to the memory usage of your system. We first specify the Pygame.surface object to draw the line to (this will, in most circumstances be 'self.Display'), then for the second parameter we specify the colour of the line, this controls colour for the entire line, and in this case we set the value to blue (or '0, 0, 255' which is the same), then we specify the Boolean value False here because we do not want the start and end points of the line to connect, and finally we specify the array of points we want to use as plots for the line, in this case we reference 'self.Data_MemUsE'.

105: ``¬ ¬ ¬ ¬ ¬ ¬ if len(self.Data_CPUUsE) >= 2:`` Now we handle the drawing of the fourth line, you will notice we have not done any processing for this line, thats because we do this one in a separate thread in 'ThreadingUtils', because of this, we cannot simply wait the usual amount of time as that many not be enough, instead we simply check when the array 'self.Data_CPUUsE', which is where we store the data for this line, is greater than or equal to a length of 2, meaning there are more than two points defined.

106: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.draw.lines(self.Display, (255, 0, 255), False, self.Data_CPUUsE)`` Now we draw the line for the CPU telemetry data, we draw this line to the display as we do with all the other line graphs (by referencing the variable 'self.Display', then we set the colour to purple (or '255, 0, 255'), then we specify that we do not want the start and end points to be connected with the third parameter of Boolean False. Then finally we reference the array which we store all the data for this line, which we stored in the variable 'self.Data_CPUUsE'.

107: ``¬ ¬ ¬ ¬ ¬ ¬ runFont = DataFont.render(f"MemUsE: {self.mod_Psutil__.virtual_memory().percent}% | CPUUsE: {self.mod_Psutil__.cpu_percent()}% | FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: {int(self.aFPS/self.Iteration)} Iteration: {self.Iteration}", self.aa, (255, 255, 255))`` Now we are rendering text to create a Pygame.surface object, this is stored in the variable 'runFont'. To do this we take the font we asked for as the second parameter of our subroutine and render the text in the brackets. This font is what you see above the graph in the top-right of the display when 'Devmode' is enabled. This displays some system metrics which can be also viewed in the caption, however in fullscreen mode the caption is no-longer visible so this displays some of the information you can see there. First we display the percentage of memory that is currently in use by the system, then we display the percentage usage of the CPU, followed by the maximum FPS the user has set in settings, then the current FPS the game is running at (remember the maximum value isn't a guarantee of getting that FPS) in addition to the average FPS and Iteration values. We also respect the user's setting on antialiasing and use the colour white, we don't respect the user's theme here because at present in either of the two available themes, the shape colour is the same, and if we changed the theme to white the contrast couldn't be great between black text and a grey background for the line graph.

108: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.blit(runFont, ((self.realWidth/2)+105, 0))`` Then we render the Pygame.surface object we just created and stored in the variable 'runFont'. We render the font to the display, referencing the variable 'self.Display', we set the position (in the format 'x', 'y') to exactly half the width of the display and then we add 105 pixels on so it doesn't overlap with the title. We set the 'y' axis height to 0 so it renders at the top of the display (all values here are in pixels).

109: ``¬ ¬ ¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

110: ``¬ ¬ ¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))`` Here we are printing out details of the error that just occurred and that we stored in the variable 'Message'. This is a handy debug feature that references the Traceback module.

111: ``¬ ¬ ¬ ¬ ¬ ¬ return Message`` This line of code stops the currently running GUI and returns the details of the error stored in the variable 'Message' to 'main.py', where they can be suitably handled.

112: ``¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

113: ``¬ print("You need to run this as part of Pycraft")`` if the user is running the code from PyPi, or as a raw “.py” file then this will be outputted to the terminal, however uses of the compiled “.exe” editions will not see this. This code is also printed first in-case the code below fails.

114: ``¬ import tkinter as tk`` Now we are importing the tkinter module into the project, all code here must be standalone and not rely on code in other modules in the project, this way the project can be taken apart and this should still work. We store he imported module, “Tkinter” with the name``tk``, this shortens length and all references to “Tkinter” from how on in this indented block will use this name.

115: ``¬ from tkinter import messagebox`` Here we are importing specific sections of “Tkinter”, in this case; messagebox, this module allows us to make dialogue boxes that are commonplace in Windows and Apple based devices.

116: ``¬ root = tk.Tk()`` This of code is required to make the dialogue box, which is what we want. This will create a window to the default size “Tkinter” has defined, and initialises the``messagebox`` module, which we want.

117: ``¬ root.withdraw()`` We use this code to hide the window that appears by using the previous root is the internal name for the window, as that is what the window created in the previous was stored in (as a variable).

118: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")`` Here we make our all to the``messagebox`` module, which has several pre-made dialogue boxes, we are using the``showerror`` pre-made dialogue box procedure here. We give it the caption of "Startup Fail", and then elaborate on the issue in the main body of the window, by displaying the text "You need to run this as part of Pycraft, please run the 'main.py' file".

119: ``¬ quit()`` This is Python’s way of closing the project, we normally use``sys.exit`` for this, which you will see later on, because its a bit cleaner on some IDLE’s and terminals. However to reduce the length of this project, we use the built in function here instead.

1: ``if not __name__ == "__main__":`` This checks to see if the place its called from (stored in the variable ``__name__``) is not ``"__main__"``. The string ``"__main__"`` would be the data stored in the variable ``__name__`` if the project was run on its own, which in this case we don't want so we only allow the code inside the if-statement to run if the data in ``__name__`` is not "__main__".

2: ``¬ print("Started <Pycraft_ExBenchmark>")`` 

3: ``¬ class LoadBenchmark:`` Now we are defining a class with a suitable name that represents what the subroutines in this class do; this allows us to group up our code to make it easier to edit, organise and debug later on, as well as saving on memory as not every function will need to be loaded at once.

4: ``¬ ¬ def __init__(self):`` Here we make sure the module is initialized correctly we do this because if we tried to call this standalone, and without the code that would stop this, then all references to variables and subroutines outside of this project would be invalid and cause issues. This is also where the variable ‘self’ is defined for all references in this class. This subroutine is a procedure, so does not return a value.

5: ``¬ ¬ ¬ pass`` Here we tell python to ignore the previous line of code that expects indented code, we use this if we don't need to put any code in this indent, this should be avoided in most situations. This is mainly used in the ``__init__`` functions for Pycraft where we may not need to run any code, but need to make sure the module is working correctly.


7: ``¬ ¬ def run(self):`` Here we are creating a subroutine called 'run', this takes only the parameter of 'self'. This subroutine is used in the benchmark process and controls each of the GPU/FPS based tests. (first the blank screen test, then the drawing test and finally a simple OpenGL test).

8: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

9: ``¬ ¬ ¬ ¬ FPSlistX = []`` Here we are creating a blank array and storing it in the variable 'FPSlistX', this variable will store each iteration of the blank window benchmark in a sequence of 'n', this is used for the 'x' axis when drawing the benchmark line graph on the results page of the benchmark in 'Benchmark.py'.

10: ``¬ ¬ ¬ ¬ ¬ FPSlistY = []`` This line creates a blank array and stores it in the variable 'FPSlistY', this stores the achieved FPS for each frame of the blank screen benchmark and is used later on in 'Benchmark.py' for the results page.


12: ``¬ ¬ ¬ ¬ FPSlistX2 = []`` Here we are creating a blank array and storing it in the variable 'FPSlistX2', this variable will store each iteration of the drawing benchmark in a sequence of 'n', this is used for the 'x' axis when drawing the benchmark line graph on the results page of the benchmark in 'Benchmark.py'.

13: ``¬ ¬ ¬ ¬ ¬ FPSlistY2 = []`` This array, stored in the variable 'FPSlistY2' stores the FPS for each frame of the 2D drawing render test. This is the 'y' axis for the corresponding line graph on the results page. These arrays will receive processing later on in 'Benchmark.py' where the two arrays will be merged into points for the line graph on the results page, for more information see the benchmark section of the documentation.


15: ``¬ ¬ ¬ ¬ FPSlistX3 = []`` Here we are creating a blank array and storing it in the variable 'FPSlistX3', this variable will store each iteration of the blank window benchmark in a sequence of 'n' (elaborating, this means the data in the array will look like this; [0, 1, 2, 3, 4, 5, ...], this is used for the 'x' axis when drawing the benchmark line graph on the results page of the benchmark in 'Benchmark.py'.

16: ``¬ ¬ ¬ ¬ ¬ FPSlistY3 = []`` This array, stored in the variable 'FPSlistY3' stores the FPS for each frame of the 3D render test, the last of the three tests. This will be used later on in 'Benchmark.py' in the results page for the drawing the corresponding line graph.


18: ``¬ ¬ ¬ ¬ SetFPS = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 200, 250, 300, 350, 500]`` Here we are storing an array of the different FPS targets, after the completion of each of the targets, the next target is selected and the time taken for each benchmark will theoretically decrease (although it's unlikely that some of the higher ones will be met). The first test is the blank window test, it will start at 15 FPS, then after a set number of display refreshes (500), the next frame rate is selected.


20: ``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((1280, 720))`` Here we set the display to the original resolution and size of (1280x720), we do this so that if the display is set large or fullscreen, the benchmark will still be fair and comparable to other data, it also stops the display from potentially freezing in fullscreen which can cause a system lockup, this also stops the window from being resized during the test as the larger the display is the lower the FPS can be, especially at high a high FPS and size. We store the display we create in the same variable as always, 'self.Display'. 


22: ``¬ ¬ ¬ ¬ iteration = 0`` We start each of the different tests (blank, drawing and OpenGL) by resetting some values, here we set the iteration counter to 0, this is used for getting the current frame for the 'FPSlist<num>' variables, this also controls when the program should move onto the next test/speed.

23: ``¬ ¬ ¬ ¬ ¬ FPScounter = 0`` This will store the index for the array stored in the variable 'SetFPS', when the program reaches the end of one test at a set speed, this is incremented and the test runs again at the higher speed.

24: ``¬ ¬ ¬ ¬ ¬ MaxIteration = 500`` This controls how many iterations of the 'iteration' variable we do (so how long the test is and how many samples to collect) before moving on to the next framerate or test. 


26: ``¬ ¬ ¬ ¬ while iteration < 7500:`` Next we control how many iterations in total there are for each of the tests, after 7500 iterations (each set of 500 iterations is a different framerate) the program moves on to a different test or finishes, based on the progress through the subroutine the program is. Until the program is finished with a stage, and the variable 'iteration' is not equal to 7500, we run the contents of the while loop.

27: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running Blank Window Benchmark @ {SetFPS[FPScounter]} FPS")`` We set the caption to update the user on which stage of the benchmark they are on and what framerate the game is currently testing, this is called ONCE per change in speed as not to disrupt the benchmark.

28: ``¬ ¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:`` Now we go through and run this while loop approximately 500 times for each frame time, this controls when the program should move on from that framerate and increase the FPS. What code runs inside this while-loop controls the contents of the benchmark, so for example for the first test there will only 1 reference to the 'self.Display' variable where the display is filled.

29: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:`` For the first few runs of the benchmark, there many not be a current FPS value, in which case we ignore these values where the FPS is 0, this is where we detect if the current FPS is NOT 0.

30: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX.append(iteration)`` Here we start collecting data, first we update the array we stored at the variable 'FPSlistX' (which controls the 'x' position of the line in the line graph) with the current iteration of the est.

31: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY.append(self.clock.get_fps())`` Then we append the current FPS (which we get through 'self.clock.get_fps()') to the variable 'FPSlistY'. This stores the current framerate of the display which we use for the 'y' axis of the line graph on the results page in 'Benchmark.py'.

32: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

33: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, here we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

34: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):`` Here we are detecting is the user is attempting to exit the benchmark, we detect if the user has attempted to press the 'x' at the top of the display first, then we check to see if the user has pressed any key on the keyboard, which can also be used to close the benchmark (this is mentioned in the test at the start of the benchmark in 'Benchmark.py' however if the user has pressed the SPACE key then we ignore this. Pygame stores all events since the previous frame.

35: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return False`` We return the Boolean value of False if the benchmark has been exited, this triggers an error in 'Benchmark.py' that cancels the benchmark safely, this is the intended effect.


37: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

38: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ iteration += 1`` Next we increase the variable 'iteration' by 1, this counts the number of frames and it is important this is called only once per frame.

39: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])`` Next we set the refresh-rate of the display to the integer value stored at the position stored in the variable 'FPScounter' which acts like an index for the array 'SetFPS'.

40: ``¬ ¬ ¬ ¬ ¬ ¬ FPScounter += 1`` After every 500 iterations of the benchmark we increment the variable 'FPScounter' by 1, this is done so that the program knows to switch to a higher speed for the next set of 500 iterations. The next speed is chosen using the previous line of the documentation.

41: ``¬ ¬ ¬ ¬ ¬ ¬ MaxIteration += 500`` Here we increase the variable 'MaxIteration' by 500, this tells the program to continue running for another 500 frames, this is because we can't reset the variable 'Iteration' that counts each frame due to its role as counting how many frames have passes in total so the program knows when to end the benchmark and so the line graph's 'x' axis on the results page is chronological.


43: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Preparing Animated Benchmark")`` Now, after we have finished the blank screen benchmark we allow the benchmark to take a momentary 'break' so that system components can cool off if they get warm, this also allows us to clearly separate them in both code and when they are running, during this time we set the caption accordingly for the user to tell them that we are 'Preparing Animated Benchmark'.


45: ``¬ ¬ ¬ ¬ iteration = 0`` We start each of the different tests (blank, drawing and OpenGL) by resetting some values, here we set the iteration counter to 0, this is used for getting the current frame for the 'FPSlist<num>' variables, this also controls when the program should move onto the next test/speed.

46: ``¬ ¬ ¬ ¬ ¬ FPScounter = 0`` This will store the index for the array stored in the variable 'SetFPS', when the program reaches the end of one test at a set speed, this is incremented and the test runs again at the higher speed.

47: ``¬ ¬ ¬ ¬ ¬ MaxIteration = 500`` This controls how many iterations of the 'iteration' variable we do (so how long the test is and how many samples to collect) before moving on to the next framerate or test. 

48: ``¬ ¬ ¬ ¬ ¬ run = 0`` Here we are setting the variable 'run' to 0, this appears to have little purpose in the benchmark and will be removed in Pycraft v0.9.4-2 and later versions.

49: ``¬ ¬ ¬ ¬ ¬ y = 10`` Here we are setting the variable 'y' to 10, this variable's purpose is unclear and will likely be removed with the previous variable in Pycraft v0.9.4-2.


51: ``¬ ¬ ¬ ¬ while not iteration == 60:`` Now we are letting this while loop iterate over the following code 60 times, at the start of each iteration we heck to see if the variable 'iteration' is not equal to 60, the variable 'iteration' will increase by 1 with each run.

52: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

53: ``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, here we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

54: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):`` Here we are detecting is the user is attempting to exit the benchmark, we detect if the user has attempted to press the 'x' at the top of the display first, then we check to see if the user has pressed any key on the keyboard, which can also be used to close the benchmark (this is mentioned in the test at the start of the benchmark in 'Benchmark.py' however if the user has pressed the SPACE key then we ignore this. Pygame stores all events since the previous frame.

55: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return False`` We return the Boolean value of False if the benchmark has been exited, this triggers an error in 'Benchmark.py' that cancels the benchmark safely, this is the intended effect.


57: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

58: ``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1`` Next we increase the variable 'iteration' by 1, this counts the number of frames and it is important this is called only once per frame.

59: ``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(60)`` Here we are setting the frame-rate in the break to 60 FPS as this shouldn't be too straining on the system and allow it to cool slightly before the next test, this section also helps with the data analytics as sometimes the first few values of the next test will be the same frame-rate of the end of the last which can skew the results. Because this program will iterate 60 times at 60 FPS that means this while loop should run for theoretically exactly 1 second.



62: ``¬ ¬ ¬ ¬ ¬ iteration = 0`` We start each of the different tests (blank, drawing and OpenGL) by resetting some values, here we set the iteration counter to 0, this is used for getting the current frame for the 'FPSlist<num>' variables, this also controls when the program should move onto the next test/speed.

63: ``¬ ¬ ¬ ¬ ¬ FPScounter = 0`` This will store the index for the array stored in the variable 'SetFPS', when the program reaches the end of one test at a set speed, this is incremented and the test runs again at the higher speed.

64: ``¬ ¬ ¬ ¬ ¬ MaxIteration = 500`` This controls how many iterations of the 'iteration' variable we do (so how long the test is and how many samples to collect) before moving on to the next framerate or test. 


66: ``¬ ¬ ¬ ¬ while iteration < 7500:`` Next we control how many iterations in total there are for each of the tests, after 7500 iterations (each set of 500 iterations is a different framerate) the program moves on to a different test or finishes, based on the progress through the subroutine the program is. Until the program is finished with a stage, and the variable 'iteration' is not equal to 7500, we run the contents of the while loop.

67: ``¬ ¬ ¬ ¬ ¬ ¬ run += 1`` Here we are increasing the (un-needed) variable 'run' by 1 with each FPS change of the benchmark, this occurs every time we change the caption.

68: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running Animated Window Benchmark @ {SetFPS[FPScounter]} FPS")`` Now we change the caption before we start each section of the stress test, we set the caption to tell the user suitably that they have started the 'Animated Window Benchmark' and we also tell them the frame-rate the test is currently targeting.

69: ``¬ ¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:`` Now we go through and run this while loop approximately 500 times for each frame time, this controls when the program should move on from that framerate and increase the FPS. What code runs inside this while-loop controls the contents of the benchmark, so for example for the first test there will only 1 reference to the 'self.Display' variable where the display is filled.

70: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:`` For the first few runs of the benchmark, there many not be a current FPS value, in which case we ignore these values where the FPS is 0, this is where we detect if the current FPS is NOT 0.

71: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX2.append(iteration)`` Now we are adding the current iteration of this section of the benchmark to the variable 'FPSlistX2', this allows the program to keep a record of the achieved FPS at each frame of the benchmark, this will be used to graph its corresponding line in the results section of the benchmark in 'Benchmark.py'.

72: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY2.append(self.clock.get_fps())`` Now we make a record of the current framerate of the game, this is used in calculating the corresponding line graph for the drawing stress test. We add the FPS to the end of the array, and this will be paired with the current iteration which we stored on the previous line.

73: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

74: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)`` Next we are making a call to the module 'DrawingUtils' where we will be calling the subroutine called 'CreateRose' which takes 4 parameters; 'self' which is commonly asked for, this contains all the global variables for the program, then we ask for the 'x' and 'y' scale factors of the game, this is calculated using the game's original size (which we use as a starting position to draw everything from) and the current size of the game, however for this section in the benchmark, the display size is set to (1280x720) which is the original size and this cannot be changed, as a result we do not need to calculate the scale factor, for more information on this please see the relevant documentation in 'HomeScreen.py' or 'DrawingUtils.py'. Finally we pass the Boolean value of False, which we use to set the colour of the drawing to an appropriate colour from the user's theme.

75: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)`` Next we are making a call to the module 'DrawingUtils' where we will be calling the subroutine called 'CreateRose' which takes 4 parameters; 'self' which is commonly asked for, this contains all the global variables for the program, then we ask for the 'x' and 'y' scale factors of the game, this is calculated using the game's original size (which we use as a starting position to draw everything from) and the current size of the game, however for this section in the benchmark, the display size is set to (1280x720) which is the original size and this cannot be changed, as a result we do not need to calculate the scale factor, for more information on this please see the relevant documentation in 'HomeScreen.py' or 'DrawingUtils.py'. Finally we pass the Boolean value of False, which we use to set the colour of the drawing to an appropriate colour from the user's theme.

76: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)`` Next we are making a call to the module 'DrawingUtils' where we will be calling the subroutine called 'CreateRose' which takes 4 parameters; 'self' which is commonly asked for, this contains all the global variables for the program, then we ask for the 'x' and 'y' scale factors of the game, this is calculated using the game's original size (which we use as a starting position to draw everything from) and the current size of the game, however for this section in the benchmark, the display size is set to (1280x720) which is the original size and this cannot be changed, as a result we do not need to calculate the scale factor, for more information on this please see the relevant documentation in 'HomeScreen.py' or 'DrawingUtils.py'. Finally we pass the Boolean value of False, which we use to set the colour of the drawing to an appropriate colour from the user's theme.

77: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)`` Next we are making a call to the module 'DrawingUtils' where we will be calling the subroutine called 'CreateRose' which takes 4 parameters; 'self' which is commonly asked for, this contains all the global variables for the program, then we ask for the 'x' and 'y' scale factors of the game, this is calculated using the game's original size (which we use as a starting position to draw everything from) and the current size of the game, however for this section in the benchmark, the display size is set to (1280x720) which is the original size and this cannot be changed, as a result we do not need to calculate the scale factor, for more information on this please see the relevant documentation in 'HomeScreen.py' or 'DrawingUtils.py'. Finally we pass the Boolean value of False, which we use to set the colour of the drawing to an appropriate colour from the user's theme.

78: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)`` Next we are making a call to the module 'DrawingUtils' where we will be calling the subroutine called 'CreateRose' which takes 4 parameters; 'self' which is commonly asked for, this contains all the global variables for the program, then we ask for the 'x' and 'y' scale factors of the game, this is calculated using the game's original size (which we use as a starting position to draw everything from) and the current size of the game, however for this section in the benchmark, the display size is set to (1280x720) which is the original size and this cannot be changed, as a result we do not need to calculate the scale factor, for more information on this please see the relevant documentation in 'HomeScreen.py' or 'DrawingUtils.py'. Finally we pass the Boolean value of False, which we use to set the colour of the drawing to an appropriate colour from the user's theme.

79: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)`` Next we are making a call to the module 'DrawingUtils' where we will be calling the subroutine called 'CreateRose' which takes 4 parameters; 'self' which is commonly asked for, this contains all the global variables for the program, then we ask for the 'x' and 'y' scale factors of the game, this is calculated using the game's original size (which we use as a starting position to draw everything from) and the current size of the game, however for this section in the benchmark, the display size is set to (1280x720) which is the original size and this cannot be changed, as a result we do not need to calculate the scale factor, for more information on this please see the relevant documentation in 'HomeScreen.py' or 'DrawingUtils.py'. Finally we pass the Boolean value of False, which we use to set the colour of the drawing to an appropriate colour from the user's theme.

80: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)`` Next we are making a call to the module 'DrawingUtils' where we will be calling the subroutine called 'CreateRose' which takes 4 parameters; 'self' which is commonly asked for, this contains all the global variables for the program, then we ask for the 'x' and 'y' scale factors of the game, this is calculated using the game's original size (which we use as a starting position to draw everything from) and the current size of the game, however for this section in the benchmark, the display size is set to (1280x720) which is the original size and this cannot be changed, as a result we do not need to calculate the scale factor, for more information on this please see the relevant documentation in 'HomeScreen.py' or 'DrawingUtils.py'. Finally we pass the Boolean value of False, which we use to set the colour of the drawing to an appropriate colour from the user's theme.

81: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)`` Next we are making a call to the module 'DrawingUtils' where we will be calling the subroutine called 'CreateRose' which takes 4 parameters; 'self' which is commonly asked for, this contains all the global variables for the program, then we ask for the 'x' and 'y' scale factors of the game, this is calculated using the game's original size (which we use as a starting position to draw everything from) and the current size of the game, however for this section in the benchmark, the display size is set to (1280x720) which is the original size and this cannot be changed, as a result we do not need to calculate the scale factor, for more information on this please see the relevant documentation in 'HomeScreen.py' or 'DrawingUtils.py'. Finally we pass the Boolean value of False, which we use to set the colour of the drawing to an appropriate colour from the user's theme.

82: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, here we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

83: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):`` Here we are detecting is the user is attempting to exit the benchmark, we detect if the user has attempted to press the 'x' at the top of the display first, then we check to see if the user has pressed any key on the keyboard, which can also be used to close the benchmark (this is mentioned in the test at the start of the benchmark in 'Benchmark.py' however if the user has pressed the SPACE key then we ignore this. Pygame stores all events since the previous frame.

84: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return False`` We return the Boolean value of False if the benchmark has been exited, this triggers an error in 'Benchmark.py' that cancels the benchmark safely, this is the intended effect.


86: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

87: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ iteration += 1`` Next we increase the variable 'iteration' by 1, this counts the number of frames and it is important this is called only once per frame.

88: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])`` Next we set the refresh-rate of the display to the integer value stored at the position stored in the variable 'FPScounter' which acts like an index for the array 'SetFPS'.

89: ``¬ ¬ ¬ ¬ ¬ ¬ FPScounter += 1`` After every 500 iterations of the benchmark we increment the variable 'FPScounter' by 1, this is done so that the program knows to switch to a higher speed for the next set of 500 iterations. The next speed is chosen using the previous line of the documentation.

90: ``¬ ¬ ¬ ¬ ¬ ¬ MaxIteration += 500`` Here we increase the variable 'MaxIteration' by 500, this tells the program to continue running for another 500 frames, this is because we can't reset the variable 'Iteration' that counts each frame due to its role as counting how many frames have passes in total so the program knows when to end the benchmark and so the line graph's 'x' axis on the results page is chronological.


92: ``¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Preparing OpenGL Benchmark")`` Like before, we now take a (theoretically 1 second long) break where we allow the system to cool slightly, we now set the title to 'Preparing OpenGL Benchmark' as that is the next stage and until we start the benchmark that is what we will be doing (we will need to create some vertexes and initialise a OpenGL display as well here), the caption will change next to tell the user the OpenGL benchmark has started.


94: ``¬ ¬ ¬ ¬ iteration = 0`` We start each of the different tests (blank, drawing and OpenGL) by resetting some values, here we set the iteration counter to 0, this is used for getting the current frame for the 'FPSlist<num>' variables, this also controls when the program should move onto the next test/speed.

95: ``¬ ¬ ¬ ¬ ¬ FPScounter = 0`` This will store the index for the array stored in the variable 'SetFPS', when the program reaches the end of one test at a set speed, this is incremented and the test runs again at the higher speed.

96: ``¬ ¬ ¬ ¬ ¬ MaxIteration = 500`` This controls how many iterations of the 'iteration' variable we do (so how long the test is and how many samples to collect) before moving on to the next framerate or test. 

97: ``¬ ¬ ¬ ¬ ¬ run = 0`` Here we are setting the variable 'run' to 0, this appears to have little purpose in the benchmark and will be removed in Pycraft v0.9.4-2 and later versions.

98: ``¬ ¬ ¬ ¬ ¬ y = 10`` Here we are setting the variable 'y' to 10, this variable's purpose is unclear and will likely be removed with the previous variable in Pycraft v0.9.4-2.


100: ``¬ ¬ ¬ ¬ while not iteration == 60:`` Now we are letting this while loop iterate over the following code 60 times, at the start of each iteration we heck to see if the variable 'iteration' is not equal to 60, the variable 'iteration' will increase by 1 with each run.

101: ``¬ ¬ ¬ ¬ ¬ ¬ self.Display.fill(self.BackgroundCol)`` This line refreshes the display which is defined in the 'DisplayUtils.py' module with the background that is defined in the 'ThemeUtils.py', removing ALL previously drawn graphics, should be called at most once per frame to avoid confusion.

102: ``¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, here we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

103: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):`` Here we are detecting is the user is attempting to exit the benchmark, we detect if the user has attempted to press the 'x' at the top of the display first, then we check to see if the user has pressed any key on the keyboard, which can also be used to close the benchmark (this is mentioned in the test at the start of the benchmark in 'Benchmark.py' however if the user has pressed the SPACE key then we ignore this. Pygame stores all events since the previous frame.

104: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return False`` We return the Boolean value of False if the benchmark has been exited, this triggers an error in 'Benchmark.py' that cancels the benchmark safely, this is the intended effect.


106: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

107: ``¬ ¬ ¬ ¬ ¬ ¬ iteration += 1`` Next we increase the variable 'iteration' by 1, this counts the number of frames and it is important this is called only once per frame.

108: ``¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(60)`` Here we are setting the frame-rate in the break to 60 FPS as this shouldn't be too straining on the system and allow it to cool slightly before the next test, this section also helps with the data analytics as sometimes the first few values of the next test will be the same frame-rate of the end of the last which can skew the results. Because this program will iterate 60 times at 60 FPS that means this while loop should run for theoretically exactly 1 second.


110: ``¬ ¬ ¬ ¬ self.Display = self.mod_Pygame__.display.set_mode((1280, 720), self.mod_Pygame__.OPENGL|self.mod_Pygame__.DOUBLEBUF)`` Here we are re-creating the display, we store the new display object in the same variable as before; 'self.Display'. As before we set the same display size and don't allow for display resizing, here though we have to also add the parameters 'pygame.OPENGL' and 'pygame.DOUBLEBUF' which allows for the rendering of OpenGL objects which we will need as the next section of the benchmark is an OpenGL render test.


112: ``¬ ¬ ¬ ¬ iteration = 0`` We start each of the different tests (blank, drawing and OpenGL) by resetting some values, here we set the iteration counter to 0, this is used for getting the current frame for the 'FPSlist<num>' variables, this also controls when the program should move onto the next test/speed.

113: ``¬ ¬ ¬ ¬ ¬ FPScounter = 0`` This will store the index for the array stored in the variable 'SetFPS', when the program reaches the end of one test at a set speed, this is incremented and the test runs again at the higher speed.

114: ``¬ ¬ ¬ ¬ ¬ MaxIteration = 500`` This controls how many iterations of the 'iteration' variable we do (so how long the test is and how many samples to collect) before moving on to the next framerate or test. 

115: ``¬ ¬ ¬ ¬ ¬ vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))`` Here we are defining the vertices for the wireframe cube we will be using as our OpenGL object, each coordinate is in the format (x, y, z).

116: ``¬ ¬ ¬ ¬ ¬ edges = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4), (6,7), (5,1), (5,4), (5,7))`` Next we define all of the lines we want to draw between the vertices, this is what we will see during the test, each of the numbers (from 0 through to 7) are indexes for that vertex in the previous tuple which we created in the variable 'vertices', we can add as many different lines between each of the vertices we want but a tuple cannot be edited so we can only do his during development and cannot add more lines later when the program is running. These edges are stored in the appropriately named 'edges' variable.


118: ``¬ ¬ ¬ ¬ self.mod_OGLbenchmark__.LoadOGLBenchmark.CreateBenchmark(self)`` Here we are making a call to the 'OGLbenchmark.py' module which we use to handle a large amount of the OpenGL logic for this final test, here we are specifically calling the 'CreateBenchmark' which takes the parameter of 'self' and calculates the projection matrix and moves the cube into a suitable position


120: ``¬ ¬ ¬ ¬ while iteration < 7500:`` Next we control how many iterations in total there are for each of the tests, after 7500 iterations (each set of 500 iterations is a different framerate) the program moves on to a different test or finishes, based on the progress through the subroutine the program is. Until the program is finished with a stage, and the variable 'iteration' is not equal to 7500, we run the contents of the while loop.

121: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running OpenGL Benchmark @ {SetFPS[FPScounter]} FPS")`` Now we are setting the caption for the new OpenGL enabled GUI, we aren't replacing the title here as the previous caption for the different display has been wiped, we update the caption with each change in FPS to tell the user the benchmark is still running and what refresh rate is currently being tested.

122: ``¬ ¬ ¬ ¬ ¬ ¬ while not iteration == MaxIteration:`` Now we go through and run this while loop approximately 500 times for each frame time, this controls when the program should move on from that framerate and increase the FPS. What code runs inside this while-loop controls the contents of the benchmark, so for example for the first test there will only 1 reference to the 'self.Display' variable where the display is filled.

123: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ if not self.clock.get_fps() == 0:`` For the first few runs of the benchmark, there many not be a current FPS value, in which case we ignore these values where the FPS is 0, this is where we detect if the current FPS is NOT 0.

124: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistX3.append(iteration)`` Now we are adding the current frame number we are on, which we store in the variable 'iteration', this will be used for plotting the 'x' axis for the OpenGL benchmark.

125: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ FPSlistY3.append(self.clock.get_fps())`` Now we store current FPS the benchmark is running, this will be used to plot the 'y' axis of the line graph for the OpenGL benchmark.

126: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ self.mod_OGLbenchmark__.LoadOGLBenchmark.RunBenchmark(self, edges, vertices)`` Now we are making another call to the 'OGLbenchmark' module, this time calling the 'RunBenchmark' module in the class 'LoadOGLBenchmark', this takes the global variable 'self' as the first parameter, in addition to the 'edges' and 'vertices' variables which we defined earlier. In this subroutine we will be drawing the cube as well as rotating the cube and clearing the display of the previous drawing, for more information please consult the documentation for this module 'OGLbenchmark'.

127: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ for event in self.mod_Pygame__.event.get():`` This is an event loop in Pygame, here we are getting a list of every event that occurs when interacting with the window, from key-presses to mouse-movements. This is a good section to look at when working on user interactions.

128: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):`` Here we are detecting is the user is attempting to exit the benchmark, we detect if the user has attempted to press the 'x' at the top of the display first, then we check to see if the user has pressed any key on the keyboard, which can also be used to close the benchmark (this is mentioned in the test at the start of the benchmark in 'Benchmark.py' however if the user has pressed the SPACE key then we ignore this. Pygame stores all events since the previous frame.

129: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ return None`` If there is no errors when using this GUI, then we don't need to return anything to 'main.py', which will move us to a different GUI, this will likely be the 'ome-Screen', if this line returned a specific ID (for example 'Inventory') then the program will open that instead of the default 'ome-Screen'.


131: ``¬ ¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.flip()`` Updates the display defined in 'DisplayUtils.py', we use flip over update as it has more functionality and is generally more optimised in testing.

132: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ iteration += 1`` Next we increase the variable 'iteration' by 1, this counts the number of frames and it is important this is called only once per frame.

133: ``¬ ¬ ¬ ¬ ¬ ¬ ¬ self.clock.tick(SetFPS[FPScounter])`` Next we set the refresh-rate of the display to the integer value stored at the position stored in the variable 'FPScounter' which acts like an index for the array 'SetFPS'.

134: ``¬ ¬ ¬ ¬ ¬ ¬ FPScounter += 1`` After every 500 iterations of the benchmark we increment the variable 'FPScounter' by 1, this is done so that the program knows to switch to a higher speed for the next set of 500 iterations. The next speed is chosen using the previous line of the documentation.

135: ``¬ ¬ ¬ ¬ ¬ ¬ MaxIteration += 500`` Here we increase the variable 'MaxIteration' by 500, this tells the program to continue running for another 500 frames, this is because we can't reset the variable 'Iteration' that counts each frame due to its role as counting how many frames have passes in total so the program knows when to end the benchmark and so the line graph's 'x' axis on the results page is chronological.



138: ``¬ ¬ ¬ ¬ ¬ self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Finished Animated Benchmark")`` Now we suitably update the caption for the user to tell them that the GPU benchmark is complete.

139: ``¬ ¬ ¬ ¬ ¬ self.mod_Time__.sleep(5)`` Now we call the built-in Python module Time, here we are telling the project to wait 5 seconds before moving on to the next line.

140: ``¬ ¬ ¬ ¬ except Exception as Message:`` This line of code handles any errors that may occur when running that module, subroutine or class. All errors must be either printed out to the terminal or handled appropriately in the program based on the guidelines in this documentation. The variable 'Message' stores any errors that may occur as a string.

141: ``¬ ¬ ¬ ¬ ¬ print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))`` Here we are printing out details of the error that just occurred and that we stored in the variable 'Message'. This is a handy debug feature that references the Traceback module.

142: ``¬ ¬ ¬ ¬ ¬ return Message, None, None, None, None`` If an error has occurred during the running of the program then we return the contents of the error to the caller, we also here in 'ExBenchmark' return 'none' as the other parameters the user was expecting, this is because we don't want to cause an error with the caller as well, which will happen if not all the data it was expecting was returned.

143: ``¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...


145: ``¬ ¬ ¬ ¬ return None, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3`` If NO errors occur however then we don't return anything (so 'None') as the first argument, the use of 'None' is deliberate as it is the only data the caller will accept without detecting an error. We also then return the 6 arrays we stored as local variables in this program. These will be used for calculations in the 'Benchmark' program (see documentation for more information), as well as rendering the line graph on the results page.

146: ``¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

147: ``¬ print("You need to run this as part of Pycraft")`` if the user is running the code from PyPi, or as a raw “.py” file then this will be outputted to the terminal, however uses of the compiled “.exe” editions will not see this. This code is also printed first in-case the code below fails.

148: ``¬ import tkinter as tk`` Now we are importing the tkinter module into the project, all code here must be standalone and not rely on code in other modules in the project, this way the project can be taken apart and this should still work. We store he imported module, “Tkinter” with the name``tk``, this shortens length and all references to “Tkinter” from how on in this indented block will use this name.

149: ``¬ from tkinter import messagebox`` Here we are importing specific sections of “Tkinter”, in this case; messagebox, this module allows us to make dialogue boxes that are commonplace in Windows and Apple based devices.

150: ``¬ root = tk.Tk()`` This of code is required to make the dialogue box, which is what we want. This will create a window to the default size “Tkinter” has defined, and initialises the``messagebox`` module, which we want.

151: ``¬ root.withdraw()`` We use this code to hide the window that appears by using the previous root is the internal name for the window, as that is what the window created in the previous was stored in (as a variable).

152: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")`` Here we make our all to the``messagebox`` module, which has several pre-made dialogue boxes, we are using the``showerror`` pre-made dialogue box procedure here. We give it the caption of "Startup Fail", and then elaborate on the issue in the main body of the window, by displaying the text "You need to run this as part of Pycraft, please run the 'main.py' file".

153: ``¬ quit()`` This is Python’s way of closing the project, we normally use``sys.exit`` for this, which you will see later on, because its a bit cleaner on some IDLE’s and terminals. However to reduce the length of this project, we use the built in function here instead.

1: ``if not __name__ == "__main__":`` This checks to see if the place its called from (stored in the variable ``__name__``) is not ``"__main__"``. The string ``"__main__"`` would be the data stored in the variable ``__name__`` if the project was run on its own, which in this case we don't want so we only allow the code inside the if-statement to run if the data in ``__name__`` is not "__main__".

2: ``¬ print("Started <Pycraft_GameEngine>")`` Now we output data to the terminal if the program is running, this allows us to know if there are any errors preventing this module from loading, in which case the program would crash before that is outputted to the terminal, making us aware the error is in this module.


4: ``¬ from ShareDataUtil import Class_Startup_variables as SharedData`` Here we are importing the module 'ShareDataUtil' which is what we use to transfer data between the main body of Pycraft and the Game-Engine which runs slightly differently. We are specifying here that we want the subroutine 'Class_Startup_variables' module from 'ShareDataUtil', we only import this subroutine. We make references to the subroutine we just imported through the name 'SharedData'.


6: ``¬ SharedData.mod_ModernGL_window_.setup_basic_logging(0)`` Now we are telling ModernGL_window that we do not want to log any errors or text that occurs when the program runs. This is only changed for releases as the text the game-engine outputs when it runs can slow down it's startup and will likely go unseen anyway, we do this by referencing ModernGL_window's 'setup_basic_logging' subroutine and set the value to 0 (0 = off).



9: ``¬ class Cubemap(SharedData.mod_Base__.CameraWindow):`` Now we are creating a display object when we create the class 'Cubemap', this class is where we will do most of the operations for the game-engine. We create the display by referencing the module 'base' which handles all of the basic ModernGL_window functions, here we are creating a OpenGL enabled display using the subroutine 'CameraWindow', we will pass arguments to customise the display later.

10: ``¬ ¬ SharedData.mod_Base__.CameraWindow.title = f"Pycraft: v{SharedData.version}: Playing"`` Here we are setting the caption for the display we created previously, we use the same caption as we did in the previous implementation and will update the caption later on in the game-loop for the game-engine with stats from 'Devmode' if that is enabled, or simply leave the caption as it is. This follows the same structure as the caption system we use for the rest of Pycraft, the only difference being the modules we are using for the display. 

11: ``¬ ¬ SharedData.mod_Base__.CameraWindow.resource_dir = SharedData.base_folder`` Here we are setting the directory that ModernGL is expecting to find resources for the game engine, we also specify the file paths like we do in the rest of Pycraft. We store the file path for ModernGL in the variable 'resource_dir' which is linked to the display.



14: ``¬ ¬ def Exit(self, SharedData, Command):`` Now we create a subroutine called 'Exit', this subroutine does not return a anything and is used to prepare the 3D game engine for closing as well as deleting objects so that we can free up some memory.

15: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

16: ``¬ ¬ ¬ ¬ if SharedData.mod_Pygame__.mixer.Channel(3).get_busy() == True:`` Here we are checking to see if the Pygame audio channel 3, which is responsible for the playing of the ambient noise in the game-engine, is currently playing.

17: ``¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_Pygame__.mixer.Channel(3).stop()`` If audio channel 3 (which handles the ambient sound for the game-engine) is currently playing (which we checked on the previous line) then we stop that sound from playing.

18: ``¬ ¬ ¬ ¬ ¬ ¬ SharedData.mod_Pygame__.quit()`` We also unload Pygame, this is done to close any other instances of Pygame so that we can load back into the 2D game-engine with a fresh instance of Pygame, this also is used to stop any other Pygame processes.


20: ``¬ ¬ ¬ ¬ ¬ self.wnd.mouse_exclusivity = False`` We also allow the mouse to be visible on-screen as well as to allow the mouse to leave the window, we do this because if the display becomes unresponsive whilst the engines switch we can still move the mouse around the desktop, also in testing there have been times in some OSs where closing the window where the mouse is hidden can cause visual issues, although this is rare. 

21: ``¬ ¬ ¬ ¬ except Exception as Error:`` If an error occurs when running the above code then this line accepts these errors and stores them in the variable 'Error' instead of causing the program to crash.

22: ``¬ ¬ ¬ ¬ ¬ print("GE", Error)`` Now we print out the error we just accepted for debug purposes, as well as adding the characters "GE" before the error indicating that the error occurred in the Game-Engine.

23: ``¬ ¬ ¬ ¬ ¬ pass`` Here we tell python to ignore the previous line of code that expects indented code, we use this if we don't need to put any code in this indent, this should be avoided in most situations. This is mainly used in the ``__init__`` functions for Pycraft where we may not need to run any code, but need to make sure the module is working correctly.

24: ``¬ ¬ ¬ ¬ self.wnd._set_fullscreen(False)`` Next we make sure the window is not fullscreen (if the window isn't then this passes without effect, this doesn't toggle between both windowed and full-screen). If the window is in full-screen when we close out of the game-engine back to the 2D game-engine run by Pygame it can lead to the OS/system being unresponsive (key presses and mouse movements will still be taken by the game so will not have an effect on the desktop).

25: ``¬ ¬ ¬ ¬ self.wnd.close()`` Next we close the window, this removes the physical display on-screen.

26: ``¬ ¬ ¬ ¬ self.wnd.destroy()`` Next we destroy all of the objects we load for the 3D game-engine as well as all the variables and processes that ModernGL (and ModernGL_window) is using (this is like ``quit()`` or ``pygame.quit()``).

27: ``¬ ¬ ¬ ¬ SharedData.CurrentlyPlaying = None`` Now we set the variable 'CurrentlyPlaying' which is the global variable which we can transfer data between the 3D game-engine and 2D game-engine. We use this variable to tell the 2D game engine we are finished with the 3D game engine and triggers the initialisation of the 2D game engine.

28: ``¬ ¬ ¬ ¬ SharedData.LoadMusic = True`` Now we tell the 2D game engine (in the 'Home-screen', see documentation for more information) to load up the menu music (if the user has enabled music). This variable tells the 2D game-engine that no other music is playing (or long lasting sound) to avoid overlapping sounds.

29: ``¬ ¬ ¬ ¬ SharedData.Command = Command`` Now we use the 3rd parameter from the subroutine 'Exit' to set the global variable 'Command', this will be used in the 'main' module to control which GUI is loaded when returning to the 2D game engine (it'll be either the 'home-screen', 'inventory' or 'MapGUI').

30: ``¬ ¬ ¬ ¬ if self.wnd.fullscreen == True:`` Now we are checking to see if the OpenGL enabled display is fullscreen or not, we do this so that when we switch between the 2D and 3D game-engines and the different display handlers we want to make sure that the display size is respected. If this if-statement is true (or correct) then the display is in fullscreen.

31: ``¬ ¬ ¬ ¬ ¬ SharedData.Fullscreen = False`` Now we are setting the global variable 'Fullscreen' which controls if the display should be loaded in full-screen or windowed mode. This variable should be flipped (so True would be False) in order for the effect to work between engines.

32: ``¬ ¬ ¬ ¬ else:`` If an if-statement is not met, or no errors occur in a section of error handling, then...

33: ``¬ ¬ ¬ ¬ ¬ SharedData.Fullscreen = True`` Now we are setting the variable 'Fullscreen' to True so that when we return to the 2D game-engine and the display is not loaded full-screen.



36: ``¬ ¬ def __init__(self, **kwargs):`` Here we are initialising the class by defining and assigning some key variables which will be used frequently in all ModernGL enabled windows.

37: ``¬ ¬ ¬ try:`` Starts a section of error handling, any errors that do arise should be handled according to the guidelines in the documentation.

38: ``¬ ¬ ¬ ¬ super().__init__(**kwargs)`` 


40: ``¬ ¬ ¬ ¬ ¬ self.size = self.wnd.buffer_size`` Now we are setting the variable 'size' to the size of the default OpenGL buffer for the window we created. (This serves little to no purpose and will be deprecated in versions of Pycraft v0.9.4-2 and greater.
