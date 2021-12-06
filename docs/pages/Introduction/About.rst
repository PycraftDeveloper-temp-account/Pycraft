About
==================

Pycraft is a 3D open-source, open-world video game made in Python. For a long time attempts to make large 3D games in python has been ignored, I believe there are two reasons: one; People use Python primarily for data handling and processing and not graphics and, two; there is little to no documentation out there to do anything more than make a 3D rotating cube in Python. Making a 3D game in Python for me hasn’t been an easy experience, far from it but I have decided to share my project, complete with tutorials, explanations, articles and code explanations in the hope that 3D game development in Python can be seen as a more easily attainable target, and to fill that ga in documentation. Pycraft then is a trial project, as I learn and experiment on what goes best where and how thing go together, this is why development can sometimes appear to have stopped, because I’m learning and testing what I've learned, so hopefully for people in the future it will be an easier experience. Also, don’t forget there is more to game development than just graphics, there is AI, sound, physics and all the other GUIs that go with it, and as I learn the quality of the overall program will improve. Pycraft is not going to be the final name of the game, however until something better becomes available, we shall stick to it.

Preview Video
==================

Here is a YouTube link to a showcase of Pycraft v0.9.1 (Developer Build): (https://youtu.be/shAprkrcaiI)

Setup
==================
Installing the project from GitHub (Method 1)
-------------------
The project will download as a (.zip) compressed file. Please make sure you have the project decompressed before use. Next make sure that any folders and files outside of the 'Pycraft' folder are removed and that the 'Pycraft' file is in the intended place for the file to be run from. This file can be freely moved around, transported between drives, computers and folders in this form. A video guide to this will be uploaded here and in YouTube in the coming months.

When running the program please make sure you have a minimum of 1GB of free space on the drive and also have Python 3 installed on your device. This can be found here: (www.python.org/downloads). The sub version of Python isn't too important in this circumstance however the project has been tested in Python 3.9.5 and is known to work. In addition to all this please make sure you have the following modules installed on your device:
Pygame, Numpy, PyOpenGL, Pillow, PyAutoGUI, Psutil, PyWaveFront, CPUinfo and Ctypes. 
For those not familiar they can be found here: (pypi.org) and you can use the following syntax to install, update and remove these modules:

``pip install <module>``
``pip uninstall <module>``

Here is a short video tutorial explain all this (It’s really not too bad), this is the link to the YouTube video: (youtu.be/DG5YbE-umw0)

Installing the project from GitHub (Method 2)
------------------
If you are installing the project from the GitHub releases page, then this will be relevant for you.
After you have selected your preferred file type (it'll be either a compiled (.exe) file or a (.zip) file, those that download the (.zip) file will find the information above more relevant.

If you, however, download the (.exe) type file, then this will be more relevant for you. If you locate the file in your file explorer and double click it, then this will run the project. You do not need Python, or any of the projects required modules, as they come built-in with this method. This method does also not install anything extra to your devise, to remove the project, simply delete the (.exe) file in your file explorer. Please note that it can take a few moments for everything in the (.exe) file to load and initialise, so nothing might not appear to happen at first. Also, you can only run one instance of Pycraft at any time (even if you are using another method).

Installing from PyPi (preferred)
------------------

If you are installing the project from PyPi, then you will need an up-to-date build of Python (3.7 or greater ideally) and also permission to install additional files to your device. Then you need to open a command-line interface (or CLI), or this we recommend Terminal on Apple based devises, and Command Prompt on Windows based machines. You install the latest version of Pycraft, and all its needed files though this command:
``pip install Python-Pycraft``
and you can also uninstall the project using the command:
``pip uninstall Python-Pycraft``
And now you can run the project as normal.
Please note that at present it can be a bit tricky to locate the files that have downloaded, you can import the project into another python file using:
``import Pycraft``
But there is a better solution on its way!

Running The Program
==================

When running the program, you will either have a (.exe) file, downloaded from the releases page, or you will have the developer preview, if you have the developer preview, which can be found in the files section of this repository then this is how you run that program. Pycraft has recently undergone some large structural redesigning, so to run the program the advice is now different:

Now you have the program properly installed hopefully (you’ll find out if you haven’t promptly!) you need to locate the file "main.py" basically all this program does is run the right modules, initiates the main program, and catches any errors that might arise in the program in a nicely rendered error screen, if it crashes on your first run then chances are you haven’t installed the program correctly, if it still doesn’t work then you can drop me an email @ "ThomasJebbo@gmail.com" or comment here on the repository, I do hope however that it works alright for you and you have a pleasant experience. I might also add this program has been developed on a Windows 64-bit computer however should run fine on a 32-bit Windows machine (uncompiled) or through MacOS although they remain untested for now. 

I recommend creating a shortcut for the "main.py" file too so it’s easier to locate.

Credits
==================

With thanks to;
- Thomas Jebbo (PycraftDeveloper) @ www.github.com/PycraftDeveloper
- Count of Freshness Traversal @ https://twitter.com/DmitryChunikhinn
- PyPi @ www.pypi.org
- Pillow (PIL) @ www.python-pillow.org
- Pygame @ www.pygame.org
- Freesound: - Erokia's "ambient wave compilation" @ www.freesound.org/s/473545
- Freesound: - Soundholder's "ambient meadow near forest" @ www.freesound.org/s/425368
- Freesound: - monte32's "Footsteps_6_Dirt_shoe" @ www.freesound.org/people/monte32/sounds/353799

Pycraft's Python Dependencies
==================

When you’re installing the uncompiled Pycraft variant from here you need to install the following 'modules', which can be done through your Control Panel in Windows (First; press the windows key + r then type "cmd" then run the below syntax) or on Apple systems in Terminal.

``pip install <module>``
``pip uninstall <module>``

pip is usually installed by default when installing Python with most versions.

- PIL (Pillow or Python Imaging Library) @ www.github.com/python-pillow/Pillow
- Pygame @ www.github.com/pygame/pygame
- Numpy @ www.github.com/numpy/numpy
- PyOpenGL (and its counterpart PyOpenGL-accelerate) @ www.github.com/mcfletch/pyopengl
- PyAutoGUI @ www.github.com/asweigart/pyautogui
- Psutil @ www.github.com/giampaolo/psutil
- PyWaveFront @ www.github.com/pywavefront/PyWavefront
- Py-CPUinfo @ www.github.com/pytorch/cpuinfo
- GPUtil @ www.github.com/anderskm/gputil
- Tabulate @ www.github.com/p-ranav/tabulate

_Disclaimer; unfortunately, lots of these python modules (first and third party) can require some external modules that will be installed during the installing process of the above modules, unfortunately this makes it really difficult to give credit to those modules, if you have any recommendations, please contact me appropriately._

Changes
==================

Pycraft v0.9.2.5 is a minor release of Pycraft with a few small changes, this will be the last edition of Pycraft to feature the game engine written entirely with PyOpenGL!

Pycraft v0.9.2.5 is now live! Here is a list of all the added features to this minor update:

* Feature: Reprogrammed the loading screen for the game engine for a large performance improvement
* Bug Fix: Minor bug fixes

Again, feedback would be much appreciated this update was released on; 21/11/2021 (UK date) DD/MM/YYYY. As always, we hope you enjoy this new release and feel free to leave feedback.

Update Timeline
==================
Pycraft will be continually updated for a long time yet. The next few releases, Pycraft v0.9.x will not feature as a (.exe) release but only as a code release. Pycraft will now updated gradually, not all in one go, however (.exe) releases will likely only occur at major releases like the upcoming Pycraft v0.10! The following plan was taken from my Medium article: How We are Making a Video Game in Python #2 (here: https://medium.com/@PycraftDev/how-we-are-making-a-video-game-in-python-2-547b504bbd67)

At present this looks to be the schedule for Pycraft updates:
* Pycraft v0.9.4 - This update, which is being worked on now, will feature the start of a documentation worked on here: https://python-pycraft.readthedocs.io/en/pycraft-v0.9.3/ (be aware, this link will change), and here on GitHub (over at the official releases under the wiki tab). This update also features the integration of the new installer which shall guide you through the installation process.
* Pycraft v0.9.5 — Will add better lighting, as well as a sun to the game! This update will also include the introduction of day and night cycles (20 minutes from sunset to sunrise), including clouds and dynamic skyboxes (featuring stars and night and day scenes).
* Pycraft v0.9.6 — This will add weather events to the sky box, as well as updated sounds, including libraries for night sounds, day sounds, rain sounds, snow sounds, ambient music, footstep sounds on wet ground, footstep sounds on snow, hurt sounds, civilisation sounds, ocean sounds, and environmental sounds (like trees and grass).
* Pycraft v0.9.7 — This will add an ocean to the OpenGL environment, as well as hopefully fixed collisions and much improved frame rates in game.
* Pycraft v0.9.8 — This update will add structures (like buildings, trees, grass, boats, people) to the game.
* Pycraft v0.9.9 — This update will feature interactions with the objects added in the previous update.
* Pycraft v0.9.10 — This update will feature the addition of a story line to the game.
* Pycraft v0.9.11 — This update will feature a start position in game, as well as saving your progress and loading them on a start screen, this update will also begin the process of playthrough!
* Pycraft v0.9.12 — This update will feature a GUI, as well as an in-game character!
* Pycraft v0.10 — This update is set to be released in Spring of 2022 at the earliest! This will showcase all the sub-updates to Pycraft v0.9, as well as featuring a compiled version. This update will also improve upon features added in sub-updates, as well as improving performance, and lots of bug fixes.
* Pycraft v0.10.1 — This update will feature the addition of inventory items.
* Pycraft v0.10.2 — This update will feature improvements to the inventory and map GUIs, this is as far as the plan reaches so far!

Our Update Policy
==================
New releases will be introduced regularly, it is likely that there will be some form of error or bug, therefore unless you intend to use this project for development and feedback purposes (Thank you all!) we recommend you use the latest stable release; below is how to identify the stable releases.

Version Naming
==================
Versions have changed pretty dramatically the past few days, don’t panic I'm here to help! In sort the new version naming system more closely follows the Semantic Naming system:
For example; Pycraft v0.9.2.1 The first number is relevant to if the project is in a finished state. The second number relates to the number of updates Pycraft has had. The third number relates to smaller sub-updates (that likely will not feature a (.exe) release). The last number there is rarely used, this is typically for PyPi releases only, as we can't edit uploaded version of the project, we use this number if there is an important change to the project description, those updates will not include any code changing!

Releases
==================
Right time to tackle some of the confusion behind the (.exe) releases that will now be a feature of all main releases. Now when installing and running the (.exe) release its actually much, much easier to do, you just have to download the file attached and simply double click on the file to run it, typically the file will be downloaded to the downloads folder on your computer. The project might take a second or two to appear to start to do something (as everything it requires is loaded) then from there it will work without having any modules installed, any connection (like ALL other releases) or any extra downloads required, its all-in-one for much easier use, and this isn’t an app that installs anything onto your computer outside of the file so to remove you simply have to delete the 'Pycraft.exe' file. Simple!

The Planned Storyline
==================
In Pycraft the plan is that you will start at sea on a boat, there you will learn that you have left your home on a separate island to find work and safety on this new one, when you arrive, you are shown to your room and the next day join a small groups of trainee knights, each training to be part of the Royal Guards system that protects the island from the dangers on the island, you quickly rise in rank as your skills shine until one day all your skills are put to the test. Will you follow through? Well, you don't know yet, I've got to make the game first!

Other Sources
==================
I have started writing an article on medium which is released at the start of every month, this compliments the weekly updates that are posted on my twitter profile, it would be greatly appreciated if you wanted to check it out here at this link: (link.medium.com/Mhqd8qIAhjb). And recommendations and feedback are, as always, greatly appreciated, a lot of time and work goes into making this happen!

Final Notices
==================
Thank you greatly for supporting this project simply by running it, I am sorry in advance for any spelling mistakes. The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo DOES NOT TAKE ANY RESPONSIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXTERNAL MODULES INSTALLED ONTO YOUR COMPUTER (WHEN NOT CHOOSING THE RECOMMENDED EXECUTABLE VERSION) ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM RESPONSIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVICES MANAGER OR ADMINISTRATOR TO INSTALL AND USE COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVICE, AND AT ANY POINT NO CONNECTION TO A NETWORK IS REQUIRED. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you.
