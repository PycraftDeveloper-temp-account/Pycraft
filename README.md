![PycraftGitHub](https://user-images.githubusercontent.com/81379254/133644694-2c1149b8-01be-40f7-88ee-6110922bcf8a.png)

This is a project in which I aim to test my abilities and learn new skills, and show what I can do to the community thank you all very much for coming here and I hope you enjoy and are inspired to fire up IDLE yourself. Made with Python 3.9 64 bit and Windows Visual Studio Code for ease of use and id strongly recommend these!

Pycraft v0.9.1 build progress: ![Progress](https://progress-bar.dev/67) <br />
Pycraft v0.9.1 reprogramming progress: ![Progress](https://progress-bar.dev/34)

## About

Pycraft is a 3D open-source, open-world video game made in Python. For a long time attempts to make large 3D games in python has been ignored, I believe there are two reasons: one; People use Python primarily for data handling and processing and not graphics and, two; there is little to no documentation out there to do anything more than make a 3D rotating cube in Python. Making a 3D game in Python for me hasn’t been an easy experience, far from it but I have decided to share my project, complete with tutorials, explanations, articles and code explanations in the hope that 3D game development in Python can be seen as a more easily attainable target, and to fill that ga in documentation. Pycraft then is a trial project, as I learn and experiment on what goes best where and how thing go together, this is why development can sometimes appear to have stopped, because I’m learning and testing what I've learned, so hopefully for people in the future it will be an easier experience. Also, don’t forget there is more to game development than just graphics, there is AI, sound, physics and all the other GUIs that go with it, and as I learn the quality of the overall program will improve. Pycraft is not going to be the final name of the game, however until something better becomes available, we shall stick to it.

In Pycraft the plan is that you will start at sea on a boat, there you will learn that you have left your home on a separate island to find work and safety on this new one, when you arrive you are shown to your room and the next day join a small groups of trainee knights, each training to be part of the Royal Guards system that protects the island from the dangers on the island, you quickly rise in rank as your skills shine until one day all your skills are put to the test. Will you follow through? Well, you don't know yet, I've got to make the game first!


## Preview video

Here is a Youtube link to a showcase of Pycraft v0.8: (www.youtube.com/watch?v=KwgA3PLc_lA)

## Setup

When setting up and installing this project you can either run the bare bones file which is likely found above this 'README.md' file if your viewing this on the GitHub website then please follow the steps below for more information on the setup and installation of this project however where possible it is recommended that you use the executable file (.exe) under the most recent releases page as this will run regardless of where you place the file or if you have python or even if you have any of the installed modules this project depends on because its compiled into one file (hence the larger file size). which makes removing the file much easier and also sharing and transporting the file easier and more convenient. However, if you are planning to use the project in its uncompiled format (which as mentioned will be at the top of this page if you are on the GitHub website) then it is recommended you follow the below steps to make sure the project works properly.

The project will download as a (.zip) compressed file. Please make sure you have the project decompressed before use. Next make sure that any folders and files outside of the 'Pycraft' folder are removed and that the 'Pycraft' file is in the intended place for the file to be run from. This file can be freely moved around, transported between drives, computers and folders in this form. A video guide to this will be uploaded here and in YouTube in the coming months.

When running the program please make sure you have a minimum of 1GB of free space on the drive and also have Python 3 installed on your device. This can be found here: (www.python.org/downloads). The sub version of Python isn't too important in this circumstance however the project has been tested in Python 3.9.5 and is known to work. In addition to all this please make sure you have the following modules installed on your device:
Pygame, Numpy, PyOpenGL, Pillow, PyAutoGUI, Psutil, PyWaveFront, CPUinfo and Ctypes. 
For those not familiar they can be found here: (pypi.org) and you can use the following syntax to install, update and remove these modules:
```
pip install <module>
pip uninstall <module>
pip update <module>
```

Here is a short video tutorial explain all this (It’s really not too bad), this is the link to the YouTube video: (youtu.be/DG5YbE-umw0)

## Running the program

Now you have the program properly installed hopefully (you’ll find out if you haven’t promptly!) you need to locate the file "PycraftRunUtil.py" basically all this program does is run the right modules, initiates the main program; "Pycraft.py" and catches any errors that might arise in the program in a nicely rendered error screen, if it crashes on your first run then chances are you haven’t installed the program correctly, if it still doesn’t work then you can drop me an email @ "ThomasJebbo@gmail.com" or comment here on the repository, I do hope however that it works alright for you and you have a pleasant experience. I might also add this program has been developed on a Windows 64-bit computer however should run fine on a 32-bit Windows machine or through MacOS although they remain untested for now. 

I recommend creating a shortcut for the "PycraftRunUtil.py" file too so it’s easier to locate.

## Credits

#### With thanks to; <br />
- Thomas Jebson <br />
- Python 3 @ www.python.org <br />
- OpenGL @ www.opengl.org <br />
- Pypi @ www.pypi.org <br />
- Pillow (PIL) @ www.python-pillow.org <br />
- Pygame @ www.pygame.org <br />
- Windows 10 - Visual Studio Code @ https://code.visualstudio.com/ <br />
- Freesound: - Erokia's "ambient wave compilation" @ www.freesound.org/s/473545 <br />
- Freesound: - Soundholder's "ambient meadow near forest" @ www.freesound.org/s/425368 <br />
- Freesound: - monte32's "Footsteps_6_Dirt_shoe" @ www.freesound.org/people/monte32/sounds/353799 <br />
- Blender @ www.blender.org <br />

## Uncompiled Pycraft's Dependencies <br />

When your installing the uncompiled Pycraft variant from here you need to install the following 'modules', which can be done through your Control Panel in Windows (First; press the windows key + r then type "cmd" then run the below syntax) or on Apple systems in Terminal.

```
pip install <module>
pip uninstall <module>
pip update <module>
```
pip is usually installed by default when installing Python with most versions.

- PIL (Pillow or Python Imgaging Libary) <br />
- Pygame<br />
- Numpy <br />
- PyOpenGL (and its counterpart PyopenGL-accelerate) <br />
- PyAutoGUI <br />
- PyWaveFront<br />
- CPUinfo <br />

_Disclaimer; unfortunately, lots of these python modules (first and third party) can require some external modules that will be installed during the installing process of the above modules, unfortunately this makes it really difficult to give credit to those modules, if you have any recommendations, please contact me appropriately._

## Changes

Pycraft v0.9 is now live! This is a huge update and there are lots of new features which can be seen below!

- The game has now even faster load times having removed some redundant file checks and duplicates, which makes the game more efficient to run.
- The game now also has a feature that will automatically detect when the game is minimised and will pause all currently playing audio and also reduce the games FPS down to 15, which increases the games efficiency when not being used, this feature will be likely tweaked and adjusted as time goes on and as the game progresses, but is here to stay!
- The screenshots section (which is used when opening your inventory when playing) has been updated to support full-screen modes and resized windows, as well as generally making it more accurate.
- General framework improvements, now the game has been cleaned up a bit behind the scenes. In addition, all the checks and features in the game game loops (that happen every time the game refreshes) has been consolidated and many redundant features removed and misbehaving tasks have been fixed.
- Updates have also been made to the error handling and display modules, now the window will load only at the resolution of (1280x720). In addition to this, various stages of error severity have been included in the game, some errors can be fixed automatically as the game runs, others that are worse will lead to the game erroring out, but the game will try to save you progress, should this fail, or the game fails catastrophically it will attempt to load the error display but should it can’t it will default to Tkinter to display an error message.
- Buttons and over things in game the user can interact with have been improved for better ease of use (notably the buttons on the home screen).
- Every menu and GUI in the game now also has a title screen so you know where you are.
- All audio that is loaded and played is now broken down into channels and loaded as and when, not all at once, again increasing efficiency and also improving performance.
- Footstep sounds have been added to the game engine.
- Landing from a jump now also triggers a sound effect.
- Sound effects for sprinting have been introduced.
- Weather events in game have been improved upon and are now better randomised.
- When your mouse is interacting with buttons or clickable objects in game it will now change accordingly, to the hand. A similar effect is created when GUIs are loading, with the mouse displaying the loading icon instead of the pointer.
- The scroll bar has been added and updated in settings, as well as dynamically changing to suit window resizes.
- There is now a crosshair in game (your mouse).
- Only one instance of the game can now run at a time in (.exe) mode to reduce issues with overheating and unnecessary stress to your system.
- A new achievements GUI been added, as to has a new character customizer GUI, these don’t look like much yet but preparations have been made behind the scenes for when they are needed.
- Caption loading and displaying has been tweaked.
- There are now more ways to interact with the GUIs on your keyboard (including the addition of the ESC or ESCAPE key to navigate back to the home screen).
- The entire start menu has been reprogrammed.
- All text in game is now dynamically adjusted to your window size so now text looks a bit neater.
- Messages have been introduced for unsupported graphics and audio drivers, as well as unsupported versions of SDL and OpenGL.
- The FPS of the game when it’s loading the 3D space is now regulated so devices should not overheat when loading the game anymore (also improving efficiency).
- All GUIs in the game now support display resizing and full screen options.
- Old loading graphics have been discontinued for a preferred drawing technique, reducing file size and making the game generally nicer to view.
- When leaving full screen mode on any GUI now sets it to the size of the main menu/title screen to avoid issues with display scaling.
- Old short load screen as been entirely removed due to concerns raised over flashing images.
- Graphics rendering is now handled by PIL instead of Pygame, meaning when the display resizes the graphics will too.
- Images that can’t be loaded with PIL now include the (.convert()) syntax to improve load times.
- Added a minimum RAM requirement (1 GB or more).
- Credits has been completely redesigned and reprogrammed, and is now fully automatic.
- The old installer has been removed.
- Benchmark mode has been introduced and is now fully operational, including the results page.
- General bug fixes (of which there where many).
- Changes have also been made to the way OpenGL objects are loaded, which boosts FPS by an adverage of ~5 to ~10 FPS in testing

Again, feedback would be much appreciated this update was released on; 19/09/2021 (UK date) DD/MM/YYYY. As always, we hope you enjoy this new release and feel free to leave feedback. Thank you! We also apologize for the slow update.

## Our update policy
New releases will be introduced regularly, it is likely that there will be some form of error or bug, therefore unless you intend to use this project for development and feedback purposes (Thank you all!) we recommend you use the latest stable release; below is how to identify the stable releases.

## Version naming
Versions have changed pretty dramatically the past few days, don’t panic I'm here to help! In sort the new version naming system more closely follows the Semantic Naming system; in short the first number in this example 'v0.8.1' stands for release number, this project has not yet been released officially so is still in development, which is why the second number increases, because that indicates each pre-release, and finally that last number which won’t appear in most releases will indicate a special release over the 'normal' file style release, which actually won’t be the typical standard actually in the far future, but that’s a (long) way off for now!

## Pycraft's update plan

Pycraft will be continually updated for a long time yet. The next release, Pycraft v0.9.1 will not feature as a (.exe) release but only as a code release, it will feature some small UI changes and some larger code restructuring and reprogramming, most of this will go on behind the scenes and won't result in much of a change for the adverage user, then Pycraft v0.9.2 will include changes to the 3D space, and thus will continue for multiple releases to come, Pycraft will now updated gradually, not all in one go, however (.exe) releases will likely only occur at major releases like the upcoming Pycraft v0.10!

## (.exe) releases

Right time to tackle some of the confusion behind the (.exe) releases that will now be a feature of all main releases. Now when installing and running the (.exe) release its actually much, much easier to do, you just have to download the file attached and simply double click on the file to run it, typically the file will be downloaded to the downloads folder on your computer. The project might take a second or two to appear to start to do something (as everything it requires is loaded) then from there it will work without having any modules installed, any connection (like ALL other releases) or any extra downloads required, its all-in-one for much easier use, and this isn’t an app that installs anything onto your computer outside of the file so to remove you simply have to delete the 'Pycraft.exe' file. Simple!

## Other sources

I have started writing an article on medium which is released at the start of every month, this compliments the weekly updates that are posted on my twitter profile, it would be greatly appreciated if you wanted to check it out here at this link: (link.medium.com/Mhqd8qIAhjb). And recommendations and feedback are, as always, greatly appreciated, a lot of time and work goes into making this happen!

## Final Notices

Thank you greatly for supporting this project simply by running it, I am sorry in advance for any spelling mistakes. The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo DOES NOT TAKE ANY RESPONSIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXTERNAL MODULES INSTALLED ONTO YOUR COMPUTER (WHEN NOT CHOOSING THE RECOMMENDED EXECUTABLE VERSION) ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM RESPONSIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVICES MANAGER OR ADMINISTRATOR TO INSTALL AND USE COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVICE, AND AT ANY POINT NO CONNECTION TO A NETWORK IS REQUIRED. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you.
