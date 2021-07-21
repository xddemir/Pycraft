# ![Picture1](https://user-images.githubusercontent.com/81379254/119387324-b157dc00-bcc0-11eb-99b2-7f7bf2886543.png)

This is a project in which I aim to test my abilities and learn new skills, and show what I can do to the community thank you all very much for coming here and I hope you enjoy and are inspired to fire up IDLE yourself. Made with Python 3.9 64 bit and Windows Visual Studio Code for ease of use and id strongly recommend these! This update is going to take a few days to be released fully, please bear with us.

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=PycraftDeveloper&repo=Pycraft&show_icons=true&theme=darcula)](https://github.com/PycraftDeveloper/Pycraft)

## Preview video

For the uncompressed file format see the youtube preview here: (https://www.youtube.com/watch?v=KwgA3PLc_lA)

https://user-images.githubusercontent.com/81379254/126047144-aaf08fe2-02ee-4a89-a5db-bd17c6940ae4.mp4

## Setup

Please first before you run the program can you make sure that you have all the files downloaded in the attached folder, then please keep them all inside the Pycraft file and don’t move them about inside the folder, as this makes the program crash and we don’t want that eh!

Also, I might just add, this program will be compiled hopefully at the end of the development process in December 2021 or later into an executable ".exe" file, however for now you will need to have python installed on your system, nothing fancy just the IDLE will do, and I’d recommend Python 3, I’m developing it on Python 3.7.7 however Python 3 and any version is recommended.

Then please run the installer; "PycraftInstaller.py" this will make sure that all the modules the program needs to run are installed correctly, before you start complaining yes this is a very badly implemented program but it works for now and I do intend to sort this program out.

## Running the program

Now you have the program properly installed hopefully (you’ll find out if you haven’t promptly!) you need to locate the file "PycraftRunUtil.py" basically all this program does is run the right modules, initiates the main program; "Pycraft.py" and catches any errors that might arise in the program in a nicely rendered error screen, if it crashes on your first run then chances are you haven’t installed the program correctly, if it still doesn’t work then you can drop me an email @ "ThomasJebbo@gmail.com" or comment here on the repository, I do hope however that it works alright for you and you have a pleasant experience. I might also add this program has been developed on a Windows 64-bit computer however should run fine on a 32-bit Windows machine or through MacOS although they remain untested for now. 

I recommend creating a shortcut for the "PycraftRunUtil.py" file too so it’s easier to locate.

## Credits

#### With thanks to; <br />
- Thomas Jebson <br />
- Python 3 @ https://www.python.org <br />
- OpenGL @ https://www.opengl.org/ <br />
- Pypi @ https://pypi.org/ <br />
- Pillow (PIL) @ https://python-pillow.org/ <br />
- Pygame @ https://www.pygame.org <br />
- Windows 10 - Visual Studio Code @ https://code.visualstudio.com/ <br />
- Freesound: - Erokia's "ambient wave compilation" @ https://freesound.org/s/473545/ <br />
- Freesound: - Soundholder's "ambient meadow near forest" @ https://freesound.org/s/425368/ <br />
- Freesound: - monte32's "Footsteps_6_Dirt_shoe" @ https://freesound.org/people/monte32/sounds/353799/ <br />
- Blender @ https://www.blender.org/ :white_medium_square:

## Dependencies <br />

in case you don't know you can install Pycraft's required modules manually or through the soon to be overhauled installer; named "PycraftInstaller.py" through your Control Panel in Windows (First; press the windows key + r then type "cmd" then run the below syntax) or on Apple systems in Terminal.

```
pip install <module>
pip uninstall <module>
pip update <module>
```
Installing, uninstalling or updating the specified module respectively; pip is usually installed by default when installing Python with most versions.

- Python: Os <br />
- Python: Sys <br />
- Python: Random <br />
- Python: Time <br />
- Python: Csv <br />
- Python: Timeit <br />
- Python: Subprocess <br />
- Python: Pip <br />
- Python: Array <br />
- Pygame >= 2.0.1 <br />
- PyOpenGL >= 3.1.5 <br />
- Numpy >= 1.20.3 <br />
- PyAutoGUI >= 0.9.52 <br />
- PyWaveFront >= 1.3.3 <br />
- Psutil >= 5.8.0 <br />
- PIL (Pillow) >= 8.2.0 <br />
- Tkinter <br />

_Disclaimer; unfortunately, lots of these python modules (first and third party) can require some external modules that will be installed during the installing process of the above modules, unfortunately this makes it really difficult to give credit to those modules, if you have any recommendations, please contact me appropriately._

## Changes

In this new sub-release, we have patched a few more known bugs, although the more data we receive with regards to errors and problems and glitches the less buggy an update will be. <br /> 
- Discontinued attempts to get an internet connection in game, due to privacy, performance and security concerns <br /> 
- Advanced load times have also been implemented to reduce the games start-up time if multiple runs are attempted on the same day <br /> 
- Added settings descriptions to the settings menu in addition to updating the settings menu in general (hover over the setting for over 3 seconds for the descriptions to appear <br /> 
- Discontinued the 'render distance' setting in the settings menu, simply because the max draw distance has to be defined by the game for some scenes and also to pave the way for future features <br />
- (.exe) releases of the project will now exist as a separate release of the project under the release’s menu with a '.1' identifier after the main update version; for example; 'v0.7.1' for reasons mentioned in that release and also attached in this file! <br />
- General needed attention was given to the spelling and grammar of each of the separate releases of the game and suitable updates will also occur in the individual branches over the following days. <br />
- One final change that’s happened now is the conversion of the version naming system from the older '21p1003-21a' format to the new 'v0.8' format, this is added to the documentation below! <br />
- Fixed a visual bug when entering the credits GUI and upon leaving the selector icon wont be the accurate theme anymore, this is now corrected
<br />
Again, feedback would be much appreciated this update was released on; 11/07/2021 (UK date) DD/MM/YYYY. As always, we hope you enjoy this new release and feel free to leave feedback. Thank you! we also apologize for the slow updates over the past few days, development has been slow due to issues with the new installer and its implementation, hence why it is not in this pre-release of Pycraft.

### Plans for the future

A final bug fix and error checking update before releasing the next Pycraft version, and we are going to then be making a huge change to the labelling system, we will be moving to a more semantic labelling structure. <br />
Further down the line more C integration, as well as game engine updates and physics updates are likely to occur, as well as forcing the skybox to the camera and maybe even rasterization.

## Our update policy
New releases will be introduced regularly, it is likely that there will be some form of error or bug, therefore unless you intend to use this project for development and feedback purposes (Thank you all!) we recommend you use the latest stable release; below is how to identify the stable releases.

## Version naming
Versions have changed pretty dramatically the past few days, don’t panic I'm here to help! In sort the new version naming system more closely follows the Semantic Naming system; in short the first number in this example 'v0.8.1' stands for release number, this project has not yet been released officially so is still in development, which is why the second number increases, because that indicates each pre-release, and finally that last number which won’t appear in most releases will indicate a special release over the 'normal' file style release, which actually won’t be the typical standard actually in the far future, but that’s a (long) way off for now!

## (.exe) releases or 'point 1' releases

Right time to tackle some of the confusion behind the (.exe) releases that will now be a feature of all releases. As stated above the '.1' on the end of an update release number will signify that there will be an attached (.exe) version of the same release. Now when installing and running the (.exe) release its actually much, much easier to do, you just have to download the file attached and simply double click on the file to run it, typically the file will be downloaded to the downloads folder on your computer. The project might take a second or two to appear to start to do something (as everything it requires is loaded) then from there it will work without having any modules installed, any connection (like ALL other releases) or any extra downloads required, its all-in-one for much easier use, and this isn’t an app that installs anything onto your computer outside of the file so to remove you simply have to delete the 'Pycraft.exe' file. Simple!

## Final Notices

Thank you greatly for supporting this project simply by running it, I am sorry in advance for any spelling mistakes. The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo DOES NOT TAKE ANY RESPONCIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXERNAL MODULES INSTALLED ONTO YOUR COMPUTER (WHEN NOT CHOOSING THE RECOMMENDED EXECUTABLE VERSION) ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM RESPONCIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVICES MAGAGER OR ADMINISTRATOR TO INSTALL AND USE COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVICE, AND AT ANY POINT NO CONNECTION TO A NETWORK IS REQUIRED. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you.

## Statistics Area

Below are a few examples of the following claims in each release. Each test is run 100 times for each test and all necessary variables have been controlled before testing:

### Shortened Start-up times
![Screenshot 2021-07-07 184523](https://user-images.githubusercontent.com/81379254/124805502-84e7de80-df53-11eb-8aa8-04ac6f87a3a9.jpg)

### Profile stats

![PycraftDeveloper's GitHub stats](https://github-readme-stats.vercel.app/api?username=PycraftDeveloper&show_icons=true&theme=darcula)
