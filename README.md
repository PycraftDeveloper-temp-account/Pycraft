<p align="center">
  <a href="https://github.com/PycraftDeveloper" target="_blank" rel="noreferrer"><img src="https://user-images.githubusercontent.com/81379254/133644694-2c1149b8-01be-40f7-88ee-6110922bcf8a.png" alt="my banner"></a>
</p>

Pycraft is an OpenGL, OpenWorld, Video Game made entirely with Python. This project is a test to shed some light on OpenGL programming in Python as it is a seldom touched area of Python's vast amount of uses. Feel free to give this project a run, and message me if you have any feedback! <br />
Made with Python 64-bit and Microsoft Visual Studio Code.

_Please note; all previous versions of Pycraft, with the exception of the most recent, have been moved to the releases section; Please consult the releases section of this README for more information_

[![](https://img.shields.io/badge/python-3.10-blue.svg)](www.python.org/downloads/release/python-3100) [![](https://img.shields.io/badge/python-3.9-blue.svg)](www.python.org/downloads/release/python-390) [![](https://img.shields.io/badge/python-3.8-blue.svg)](www.python.org/downloads/release/python-380) [![](https://img.shields.io/badge/python-3.7-blue.svg)](www.python.org/downloads/release/python-370) <br />
![](https://img.shields.io/github/license/PycraftDeveloper/Pycraft) ![](https://img.shields.io/github/stars/PycraftDeveloper/Pycraft) ![](https://img.shields.io/github/forks/PycraftDeveloper/Pycraft) ![](https://img.shields.io/github/issues/PycraftDeveloper/Pycraft) ![GitHub all releases](https://img.shields.io/github/downloads/PycraftDeveloper/Pycraft/total) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/PycraftDeveloper/Pycraft) ![](https://img.shields.io/pypi/wheel/python-pycraft) ![GitHub repo size](https://img.shields.io/github/repo-size/PycraftDeveloper/Pycraft)

Progress towards Pycraft v0.9.4: ![Progress](https://progress-bar.dev/38) <br />
Documentation Progress: ![Progress](https://progress-bar.dev/50) <br />
Installer Progress: ![Progress](https://progress-bar.dev/25) <br />

## About
Pycraft is a 3D open-source, open-world video game made in Python. For a long time attempts to make large 3D games in python has been ignored, I believe there are two reasons: one; People use Python primarily for data handling and processing and not graphics and, two; there is little to no documentation out there to do anything more than make a 3D rotating cube in Python. Making a 3D game in Python for me hasn’t been an easy experience, far from it but I have decided to share my project, complete with tutorials, explanations, articles and code explanations in the hope that 3D game development in Python can be seen as a more easily attainable target, and to fill that gap in documentation. Pycraft then is a trial project, as I learn and experiment on what goes best where and how thing go together, this is why development can sometimes appear to have stopped, because I’m learning and testing what I've learned, so hopefully for people in the future it will be an easier experience. Also, don’t forget there is more to game development than just graphics, there is AI, sound, physics and all the other GUIs that go with it, and as I learn the quality of the overall program will improve. Pycraft is not going to be the final name of the game, however until something better becomes available, we shall stick to it.

## Preview Video
Here is a YouTube link to a showcase of Pycraft v0.9.1 (Developer Build): (https://youtu.be/shAprkrcaiI)

## Setup
### Installing the project from GitHub (Method 1)

The project will download as a (.zip) compressed file. Please make sure you have the project decompressed before use. Next make sure that any folders and files outside of the 'Pycraft' folder are removed and that the 'Pycraft' file is in the intended place for the file to be run from. This file can be freely moved around, transported between drives, computers and folders in this form. A video guide to this will be uploaded here and in YouTube in the coming months.

When running the program please make sure you have a minimum of 1GB of free space on the drive and also have Python 3 installed on your device. This can be found here: (www.python.org/downloads). The sub version of Python isn't too important in this circumstance however the project has been tested in Python 3.9.5 and is known to work. In addition to all this please make sure you have the following modules installed on your device:
Pygame, Numpy, PyOpenGL, Pillow, PyAutoGUI, Psutil, PyWaveFront, CPUinfo and Ctypes. 
For those not familiar they can be found here: (pypi.org) and you can use the following syntax to install, update and remove these modules:

``pip install <module>``
``pip uninstall <module>``

Here is a short video tutorial walk you through all this: (https://youtu.be/DG5YbE-umw0)

### Installing the project from GitHub (Method 2)

If you are installing the project from the GitHub releases page, then this will be relevant for you.
After you have selected your preferred file type (it'll be either a compiled (.exe) file or a (.zip) file, those that download the (.zip) file will find the information above more relevant.

If you, however, download the (.exe) type file, then this will be more relevant for you. If you locate the file in your file explorer and double click it, then this will run the project. You do not need Python, or any of the projects required modules, as they come built-in with this method. This method does also not install anything extra to your devise, to remove the project, simply delete the (.exe) file in your file explorer. Please note that it can take a few moments for everything in the (.exe) file to load and initialise, so nothing might not appear to happen at first. Also, you can only run one instance of Pycraft at any time (even if you are using another method).

### Installing from PyPi (preferred)


If you are installing the project from PyPi, then you will need an up-to-date build of Python (3.7 or greater ideally) and also permission to install additional files to your device. Then you need to open a command-line interface (or CLI), or this we recommend Terminal on Apple based devises, and Command Prompt on Windows based machines. You install the latest version of Pycraft, and all its needed files though this command:
``pip install Python-Pycraft``
and you can also uninstall the project using the command:
``pip uninstall Python-Pycraft``
And now you can run the project as normal.
Please note that at present it can be a bit tricky to locate the files that have downloaded, you can import the project into another python file using:
``import Pycraft``
But there is a better solution on its way!

### Installing using Pipenv

You can alternatively run these commands in the directory containing a file called `Pipfile`:

    pip install pipenv
    pipenv install

And to start the game:

    pipenv run python ./Pycraft/main.py

## Running The Program
When running the program, you will either have a (.exe) file, downloaded from the releases page, or you will have the developer preview, if you have the developer preview, which can be found in the files section of this repository then this is how you run that program. Pycraft has recently undergone some large structural redesigning, so to run the program the advice is now different:

Now you have the program properly installed hopefully (you’ll find out if you haven’t promptly!) you need to locate the file "main.py" basically all this program does is run the right modules, initiates the main program, and catches any errors that might arise in the program in a nicely rendered error screen, if it crashes on your first run then chances are you haven’t installed the program correctly, if it still doesn’t work then you can drop me an email @ "ThomasJebbo@gmail.com" or comment here on the repository, I do hope however that it works alright for you and you have a pleasant experience. I might also add this program has been developed on a Windows 64-bit computer however should run fine on a 32-bit Windows machine (uncompiled) or through MacOS although they remain untested for now. 

I recommend creating a shortcut for the "main.py" file too so it’s easier to locate.

## Credits
### With thanks to; <br />
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![OpenGL](https://img.shields.io/badge/OpenGL-%23FFFFFF.svg?style=for-the-badge&logo=opengl) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![Blender](https://img.shields.io/badge/blender-%23F5792A.svg?style=for-the-badge&logo=blender&logoColor=white) ![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white) ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white) ![Gimp Gnu Image Manipulation Program](https://img.shields.io/badge/Gimp-657D8B?style=for-the-badge&logo=gimp&logoColor=FFFFFF) ![Inkscape](https://img.shields.io/badge/Inkscape-e0e0e0?style=for-the-badge&logo=inkscape&logoColor=080A13) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Visual Studio](https://img.shields.io/badge/Visual%20Studio-5C2D91.svg?style=for-the-badge&logo=visual-studio&logoColor=white) 	![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Stack Overflow](https://img.shields.io/badge/-Stackoverflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) 	![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![Edge](https://img.shields.io/badge/Edge-0078D7?style=for-the-badge&logo=Microsoft-edge&logoColor=white) 
- Thomas Jebbo (PycraftDeveloper) @ www.github.com/PycraftDeveloper <br />
- Count of Freshness Traversal @ https://twitter.com/DmitryChunikhinn <br />
- Dogukan Demir (demirdogukan) @ https://github.com/demirdogukan <br />
- Henri Post (HenryFBP) @ https://github.com/HenryFBP <br />
- PyPi @ www.pypi.org <br />
- PIL (Pillow or Python Imaging Library) @ www.github.com/python-pillow/Pillow <br />
- Pygame @ www.github.com/pygame/pygame <br />
- Numpy @ www.github.com/numpy/numpy <br />
- PyOpenGL (and its counterpart PyOpenGL-accelerate) @ www.github.com/mcfletch/pyopengl <br />
- PyAutoGUI @ www.github.com/asweigart/pyautogui <br />
- Psutil @ www.github.com/giampaolo/psutil <br />
- PyWaveFront @ www.github.com/pywavefront/PyWavefront <br />
- Py-CPUinfo @ www.github.com/pytorch/cpuinfo <br />
- GPUtil @ www.github.com/anderskm/gputil <br />
- Tabulate @ www.github.com/p-ranav/tabulate <br />
- Moderngl @ https://github.com/moderngl/moderngl <br />
- Moderngl_window @ https://github.com/moderngl/moderngl-window <br />
- Freedsound: - Erokia's "ambient wave compilation" @ www.freesound.org/s/473545 <br />
- Freedsound: - Soundholder's "ambient meadow near forest" @ www.freesound.org/s/425368 <br />
- Freedsound: - monte32's "Footsteps_6_Dirt_shoe" @ www.freesound.org/people/monte32/sounds/353799 <br />

## Uncompiled Pycraft Dependencies <br />
When you’re installing the uncompiled Pycraft variant from here you need to install the following 'modules', which can be done through your Control Panel in Windows (First; press the windows key + r then type "cmd" then run the below syntax) or on Apple systems in Terminal.

```
pip install <module>
pip uninstall <module>
```
pip is usually installed by default when installing Python with most versions.

- PIL (Pillow or Python Imaging Library) @ www.github.com/python-pillow/Pillow <br />
- Pygame @ www.github.com/pygame/pygame <br />
- Numpy @ www.github.com/numpy/numpy <br />
- PyOpenGL (and its counterpart PyOpenGL-accelerate) @ www.github.com/mcfletch/pyopengl <br />
- PyAutoGUI @ www.github.com/asweigart/pyautogui <br />
- Psutil @ www.github.com/giampaolo/psutil <br />
- PyWaveFront @ www.github.com/pywavefront/PyWavefront <br />
- Py-CPUinfo @ www.github.com/pytorch/cpuinfo <br />
- GPUtil @ www.github.com/anderskm/gputil <br />
- Tabulate @ www.github.com/p-ranav/tabulate <br />
- Moderngl @ https://github.com/moderngl/moderngl <br />
- Moderngl_window @ https://github.com/moderngl/moderngl-window <br />

_Disclaimer; unfortunately, lots of these python modules (first and third party) can require some external modules that will be installed during the installing process of the above modules, unfortunately this makes it really difficult to give credit to those modules, if you have any recommendations, please contact me appropriately._

## Changes
Pycraft v0.9.3 is now live! Here is a list of all the added features to this major update: <br />

* Feature: The entire game engine has been reprogrammed, removing redundant functions, improving the visual experience and making future updates much easier.
* Feature: The project has moved over from using (.ogg) audio files to (.wav) files, this means a much larger file size, but in the current implementation Pygame does not appear to like (.ogg) files!
* Feature: We have added a messages screen to the home screen, this will display information like events, updates, important milestones in game and more! Expect this feature to be worked on significantly!
* Bug Fix: There have been lots of bug fixes in the course of programming this new update, however not many bugs were raised in Pycraft v0.9.2.5 so there haven't been many bug fixes that link the two updates (there have been bug fixes however to the game engine in the course of its programming and re-design). If you discover a bug, then feel free to share details with me on either Twitter or by email.

_Please note there have been features REMOVED from this update at this point in time, for example the new load-screen, this will be re-added hopefully, but will take some time to work on. Also, there will likely be a small update to Pycraft over the course of December, however this will be likely bug fixes and the arrival/integration of the upcoming installer._

Again, feedback would be much appreciated this update was released on; 04/12/2021 (UK date) DD/MM/YYYY. As always, we hope you enjoy this new release and feel free to leave feedback.

## Update Timeline
Pycraft will be continually updated for a long time yet. The next few releases, Pycraft v0.9.x will not feature as a (.exe) release but only as a code release. Pycraft will now updated gradually, not all in one go, however (.exe) releases will likely only occur at major releases like the upcoming Pycraft v0.10! The following plan was taken from my Medium article: How We are Making a Video Game in Python #2 (here: https://medium.com/@PycraftDev/how-we-are-making-a-video-game-in-python-2-547b504bbd67) <br />

At present this looks to be the schedule for Pycraft updates: <br />
* Pycraft v0.9.4 - This update, which is being worked on now, will feature the start of a documentation worked on here: https://python-pycraft.readthedocs.io/en/pycraft-v0.9.3/ (be aware, this link will change), and here on GitHub (over at the official releases under the wiki tab). This update also features the integration of the new installer which shall guide you through the installation process.
* Pycraft v0.9.5 — Will add better lighting, as well as a sun to the game! This update will also include the introduction of day and night cycles (20 minutes from sunset to sunrise), including clouds and dynamic skyboxes (featuring stars and night and day scenes). <br />
* Pycraft v0.9.6 — This will add weather events to the sky box, as well as updated sounds, including libraries for night sounds, day sounds, rain sounds, snow sounds, ambient music, footstep sounds on wet ground, footstep sounds on snow, hurt sounds, civilisation sounds, ocean sounds, and environmental sounds (like trees and grass). <br />
* Pycraft v0.9.7 — This will add an ocean to the OpenGL environment, as well as hopefully fixed collisions and much improved frame rates in game. <br />
* Pycraft v0.9.8 — This update will add structures (like buildings, trees, grass, boats, people) to the game. <br />
* Pycraft v0.9.9 — This update will feature interactions with the objects added in the previous update. <br />
* Pycraft v0.9.10 — This update will feature the addition of a story line to the game. <br />
* Pycraft v0.9.11 — This update will feature a start position in game, as well as saving your progress and loading them on a start screen, this update will also begin the process of playthrough! <br />
* Pycraft v0.9.12 — This update will feature a GUI, as well as an in-game character! <br />
* Pycraft v0.10 — This update is set to be released in Spring of 2022 at the earliest! This will showcase all the sub-updates to Pycraft v0.9, as well as featuring a compiled version. This update will also improve upon features added in sub-updates, as well as improving performance, and lots of bug fixes. <br />
* Pycraft v0.10.1 — This update will feature the addition of inventory items. <br />
* Pycraft v0.10.2 — This update will feature improvements to the inventory and map GUIs, this is as far as the plan reaches so far! <br />

## Our Update Policy
New releases will be introduced regularly, it is likely that there will be some form of error or bug, therefore unless you intend to use this project for development and feedback purposes (Thank you all!) we recommend you use the latest stable release; below is how to identify the stable releases.

## Version Naming
Versions have changed pretty dramatically the past few days, don’t panic I'm here to help! In sort the new version naming system more closely follows the Semantic Naming system:
For example; Pycraft v0.9.2.1 The first number is relevant to if the project is in a finished state. The second number relates to the number of updates Pycraft has had. The third number relates to smaller sub-updates (that likely will not feature a (.exe) release). The last number there is rarely used, this is typically for PyPi releases only, as we can't edit uploaded version of the project, we use this number if there is an important change to the project description, those updates will not include any code changing!

## Releases
All past versions of Pycraft are available under the releases section of Pycraft, this is a new change, but; just as before, major releases like Pycraft v0.9 and Pycraft v0.8 will have (.exe) releases, but smaller sub-releases will not, this is in light of a change coming to Pycraft, this should help with the confusion behind releases, and be more accommodating to the installer that's being worked on as a part of Pycraft v0.9.4. This brings me on to another point, all past updates to Pycraft will be located at the releases page (Thats all versions), and the previous section on the home-page with branches will change. The default branch will be the most recent release, then there will be branches for all the sub-releases to Pycraft there too; and the sister program; Pycraft-Insider-Preview will be deprecated and all data moved to relevant places in this repository, this should hopefully cut down on the confusion and make the project more user-friendly.

## The Planned Storyline
In Pycraft the plan is that you will start at sea on a boat, there you will learn that you have left your home on a separate island to find work and safety on this new one, when you arrive, you are shown to your room and the next day join a small groups of trainee knights, each training to be part of the Royal Guards system that protects the island from the dangers on the island, you quickly rise in rank as your skills shine until one day all your skills are put to the test. Will you follow through? Well, you don't know yet, I've got to make the game first!

## Pycraft's Sound Files - Preview 1

There is a lot of progress still to be made in creating all the sound files for Pycraft, but here are some early previews, as well as a description of where they will likely appear (likely subject to change).

### Ancient Fountain Theme
https://user-images.githubusercontent.com/81379254/148644536-aaf0e70f-c2ac-453c-8749-36b2fbce7032.mp4

This sound will play at special fountains in the game, these fountains are where 8 individual spirits lie, they are very special/powerful places with good views of the surrounding land, this sound will play at these places of significance and others around the map.

### Battle Theme
https://user-images.githubusercontent.com/81379254/148644537-6da07dce-04ea-4fca-a777-4be91c3b74ae.mp4

This sound will play when fighting enemies in game, this does not apply to 'boss' mobs which will have their own individual sound, some of which have been created below.

### Boss/Dungeon Theme 1-3

https://user-images.githubusercontent.com/81379254/148644538-2c05586b-d5de-4221-9b21-f15e196bee7c.mp4

https://user-images.githubusercontent.com/81379254/148644540-bda008d9-b5f0-43d3-a3c4-3de0997243ba.mp4

https://user-images.githubusercontent.com/81379254/148644548-605fe475-9d72-4f79-bbbc-c665bf017fd6.mp4

These sounds will play when fighting a specific 'boss' enemy, each of the bosses will have their own respective dungeon and sounds, none of the 'bosses' have been created or planned yet so these sound files has not been assigned to a 'boss' or dungeon as yet.

### Castle Theme

https://user-images.githubusercontent.com/81379254/148644542-d3172a24-068a-49ff-bdd2-4318864864fe.mp4

This sound will play when you are inside the castle, this sound does not play in the castle grounds, another sound will be created for that. This sound is also not specific to set areas of the castle.

### Dark Forces Gain Power 1-2

https://user-images.githubusercontent.com/81379254/148644543-d0e2337e-4e0e-4adf-a8da-d15521961422.mp4

https://user-images.githubusercontent.com/81379254/148644544-924d5fc4-1c3a-4efe-b9e2-552edc5ce88b.mp4

These sounds will play when the player has reached certain milestones in the 'main quest' section of the game where the dark forces (basic enemies as well as bigger bosses) awaken/grow in power.

### Dark Forces Invade the Castle

https://user-images.githubusercontent.com/81379254/148644546-7d560be5-efed-4390-a73d-ea6c3a137c26.mp4

This sound plays at the biggest climax of the story, the enemies have invaded the village (a separate sound below for that) and the player has been trapped in a dungeon, they need to get out as a fight ensues in the castle between the 'good' and 'evil' forces. (In the end the user makes it out of the dungeon and is guided to the fight by the spirits (bodies of good in the game) and together they manage to destroy hordes of enemies and a final 'boss').

### Finding Friends / Side-quest Completion

https://user-images.githubusercontent.com/81379254/148644550-4d1e3bbc-f7d0-4fea-9897-128614f2fd1f.mp4

This sound is more positive and is used to mark an end to a user's optional 'side-quest'.

### Forest Theme

https://user-images.githubusercontent.com/81379254/148644551-6f6cdce3-53f6-4b77-a91a-2df8fabec1c2.mp4

This sound plays when the user is within the Forest of Secrets, this area is very foggy and the user needs to move quickly to get through the fog, if they stop for more than a few seconds the fog around them will thicken and they will be moved to a different nearby location to confuse them. Should they get to the centre there is an enemy base guarding one of the fountains, there is no fog in this clearing. There is an area of dense forest/jungle that surrounds this area, that acts as a barrier for the user, this area is filed with enemies and the NPCs in the village will show evident fear of that place. No large area of the game will be off-limits to the user, but there will be a progression in the difficulty of enemies in later game places.

### In Contact with Spirits

https://user-images.githubusercontent.com/81379254/148644552-6089d274-9449-4655-99c5-06463eb63091.mp4

This sound will play when the user has entered one of 8 in-game fountains, they can do this by throwing in a symbolic item (for example, the 'air' spirit will accept a 'rare bird feather' to activate the fountain) these items will be clearly marked at the top of the fountain, but not 'filled-in' until the user throws in a symbolic item, when they do this they are transported to a dungeon, there are 8 in total and the user can leave and re-enter at any time, but the dungeon will re-set it's self unless the user reaches special 'check-points', once the dungeon is complete a final room will open and the player will hear this music, in that room there will be one of the 8 spirits which will award you for your toil and then disappear, this is one of the only times you see the spirit in a physical form, but they exist above the fountain casting a beam of light into the sky.

### Loss Theme

https://user-images.githubusercontent.com/81379254/148644553-2b557d5b-5b30-4c10-baf8-7251aab375de.mp4

This sound will play at the loss of any NPC in the game, there are only a few times this happens. This also plays at sad points in the game.

### Milestone Reached

https://user-images.githubusercontent.com/81379254/148644559-42398c1a-21f2-42a5-92db-c2d820fff9c7.mp4

This is one of the most positive sounds in the game, and also one of the least occurring and hardest to get access to. This sound plays after the completion of any dungeon, the defeat of any boss mob, the completion of all side-quests as well as a few more undecided moments.

### Realisation

https://user-images.githubusercontent.com/81379254/148644562-bcd0b1d1-e41d-4ce1-bedc-801ca9e3c1c1.mp4

The use of this sound is not as defined as others in this list, but this will likely play at the completion of achievements, side quests or at other points in-game.

### Smuggler’s theme

https://user-images.githubusercontent.com/81379254/148644563-c646898f-6a82-462b-8f77-5bc2977cc7fd.mp4

This plays when you are on the boat going towards Pycraft, this is where you learn some of the basic game mechanics and the plot begins. This also plays at a place called 'Smuggler's Cave' which is located below the jungle in a cliff, this is a large enemy hideout and this is where the enemies collect their food from (other than stealing and hunting), you are asked for one of the side-quests to check out the place and discover this, then you will go back to the castle and report the crime for a reward. This sound plays when there are any smuggler's boats around or when you are in the cave or have line of sight and are nearby.

### Laboratory theme

https://user-images.githubusercontent.com/81379254/148646360-1e424f5f-78db-48b4-bd16-e7578d256b91.mp4

This only plays in a few locations throughout the game, this plays at the castle's laboratory as well as at some of the shops in the game.


### Success Theme

https://user-images.githubusercontent.com/81379254/148644564-37d51dcb-8679-4917-a69c-309cb9ded8c4.mp4

This sound will play at special moments in the game, when 'bosses' are defeated and this is one of the last sounds you hear at the end of the game. This is also a sound that occurs in 'recounts' of the last victory against 'evil' which you learn about as the plot progresses. This sound will likely get more use as the game is developed.

### Cave Theme / Dungeon Theme / Tales of Sadness

https://user-images.githubusercontent.com/81379254/148644565-77e3ba80-1a6e-4ba4-8671-c621e8d42785.mp4

This sound will play when the user is in the smuggler's cave to contrast the use of 'smugglers theme', this sound will also likely feature in one of the dungeons as well as at sad moments in the game. This sound is more of a work-in-progress than others.

### The Castle is in Danger

https://user-images.githubusercontent.com/81379254/148644567-79ffedc7-a56e-4705-9be0-885a067da8b8.mp4

This sound plays when the king (or queen, this option may be left up to the player in 'character-designer’) and his officials and army realise that there is a battle approaching, this sound plays as the castle is readied for the battle  and there is widespread panic in the villages. This does not play during the battle.

### Village Theme 1-3

https://user-images.githubusercontent.com/81379254/148644568-d331e323-2436-48af-ad62-38d1a5f7f24d.mp4

https://user-images.githubusercontent.com/81379254/148644570-e7394823-336f-4e36-bb55-ce80bd0e95a7.mp4

https://user-images.githubusercontent.com/81379254/148644571-e0bf583e-fb06-4c91-bbb2-1b1c1209c2ea.mp4

These three sounds have been created for each of the 4 villages that are in the game (with one sound not finished). The first sound is for the main village, this is where the main plot begins, but the other three are discovered later, contact blocked by the 'evil' forces at play. The player will receive rewards for creating contact with these villages and this is part of the main quest, these villages will contain related side-quests.

## Other Sources
I have started writing an article on medium which is released at the start of every month, this compliments the weekly updates that are posted on my twitter profile, it would be greatly appreciated if you wanted to check it out here at this link: (https://medium.com/@PycraftDev), these articles are also uploaded to my other account on Dev here: (https://dev.to/pycraftdev). Any recommendations and feedback are, as always, greatly appreciated, a lot of time and work goes into making this happen!

## Final Notices
Thank you greatly for supporting this project simply by running it, I am sorry in advance for any spelling mistakes. The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve my program, it will all be much appreciated and give as much detail as you wish to give out.
