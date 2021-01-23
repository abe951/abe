This program's intended purpose is to process several types of video and audio files and convert them into a different file type. At the moment, the current conversions include: 

YouTube to .mp4 (video format - audio only)
YouTube to .wav 
YouTube to .mp3
.mp3 to .wav

PREREQUISITES AND INSTALLATION INSTRUCTIONS:

For the program to run properly, it requires ffmpeg-20210113-ca21cb1e36-win64-static (ffmpeg-yyyymmdd-ffmpegCommitID; included as a zip archive to download along with this .py file), libraries pytube, moviepy, and pydub, and python V3.7.6.

STEPS:

First, Install python 3.7.6 through https://www.python.org/downloads/release/python-376/ and download the "Windows x86-64 executable installer". Check the "Add Python 3.7 to PATH" box at the bottom-right of the installer and then run the installer. This will install all of Python's components including pip installation, which allows us to then install the 3 libraries we need to run this program.

Then, unzip the ffmpeg-20210113-ca21cb1e36-win64-static archive into your OS drive. We will need to add the bin folder that contains the ffmpeg.exe file to our system path to allow us to run the commands. So, it is best to put it directly into your OS as a folder so it is a shorter path (C:\ffmpeg\bin).

Type in Windows Search "Edit the system environment variables" and click on it. Then click on "Environment Variables..." on the Advanced Tab that comes up. 

Under "System variables", click on "Path" so that it takes you to all the paths available and to where you can edit the environment variables.

In the top-right corner, click on "New" and then type the our path (C:\ffmpeg\bin). Press "Ok" then press "Ok", and press "Ok". 

To ensure that it was installed properly, pull up the command prompt and type ffmpeg -codecs. If the system did not recognize the command, then go back and re-check if the path was correct.

If it was installed correctly, then go back to where we edited and put a new path. For the installation of pytube, moviepy, and pydub, we will need to set a path to Python 3.7's scripts, so the directory should look like: C:\Users\username\AppData\Local\Programs\Python\Python37\Scripts

Press "Ok" then press "Ok", and press "Ok". Now pull up the command prompt and we will now install the three libraries. 

For pytube, type: "pip install pytube" and press enter
For moviepy, type: "pip install moviepy" and press enter
For pydub, type: "pip install pydub" and press enter

After following all these steps, all the prerequisites should be installed correctly and the program will run properly!


