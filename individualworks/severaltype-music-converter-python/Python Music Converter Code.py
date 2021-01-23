# This program's intended purpose is to process several types of video and audio files and convert them into a different file type using libraries pytube, moviepy, and pydub
# Make sure to read the README.md for full description including prerequisites and installation instructions BEFORE running this program
# The music conversions include: YouTube --> .mp4 (same video format - filtered to keep audio only); YouTube --> .wav converter; YoutTube --> .mp3 converter;  .mp3 --> .wav converter

# imports pytube module and imports the YouTube class to allow interaction with pytube library and YouTube
from pytube import YouTube
import pytube

# imports os module to allow interaction with the operating system
import os

# imports moviepy module to allow interaction with moviepy library
from moviepy.editor import *

# imports pydub module to allow interaction with pydub library
import pydub

# main function - when called, executes code in it
def main():
        # Asks the user what indicated music and audio file conversion they want by choosing a number associated with a conversion
        num = input("Enter 1 for YouTube to .mp4 (same video format - filtered to keep audio only) conversion, 2 for YouTube to .wav conversion, 3 for YouTube to .mp3 conversion, or 4 for .mp3 to .wav conversion: ")

        # YouTube to .mp4 (same video format - filtered to keep audio only) file conversion
        if num == "1":
                # Asks the user to input YouTube URL to be converted 
                optionOneURL = input('Enter the YouTube video URL address that you want to convert: ')
                
                # if the name of the os module is 'nt', then executes line of code below it otherwise executes code in else:
                if os.name == 'nt':
                        # returns a string representing current directory of the file used to execute code, to confirm location - (returns location as same folder with .py file)
                        currentFolder = os.getcwd() + '\\'
                else:
                        currentFolder = os.getcwd() + '/'

                # Takes the inputted URL and filters it to only keep the audio then downloads the audio-only .mp4 video file
                YouTube(optionOneURL).streams.filter(only_audio=True).first().download()
                
                # Outputs "Done!" to indicate user that program has ended 
                print("Done!")

        # YouTube to .wav file conversion
        elif num == "2":
                # Asks the user to input the YouTube URL to be converted
                optionTwoURL = input("Enter the YouTube video URL address that you want to convert: ")
                
                # Sets variable for the converted music file type .wav
                musicType = "wav"

                # Downloads the highest quality stream available for the YouTube URL inputted as a .mp4 video file 
                originalMusicFile = YouTube(optionTwoURL).streams.get_highest_resolution().download()

                # Converts the .mp4 file to .wav by getting rid of the .mp4 extension by splitting 1 time at index 0 and appends .wav
                convertedMusicFile = originalMusicFile.split(".mp4", 1)[0] + f".{musicType}"

                # Sets variable for the video process of the original YouTube file
                videoProcess2 = VideoFileClip(originalMusicFile)

                # Sets variable for the audio process of the original YouTube file
                audioProcess2 = videoProcess2.audio

                # Sets the variable for the audio process of the converted .wav file
                audioProcess2.write_audiofile(convertedMusicFile)

                # Closes both audio and video processes of the original YouTube file
                audioProcess2.close()
                videoProcess2.close()
                
                # Removes the original downloaded mp4 video YouTube file from the current directory
                os.remove(originalMusicFile)

                # Outputs "Done!" to indicate user that program has ended
                print("Done!")

        # YouTube to .mp3 file conversion
        elif num == "3":
                # Asks the user to input the YouTube URL to be converted
                optionThreeURL = input("Enter the YouTube video URL address that you want to convert: ")

                # Sets variable for the converted music file type .mp3
                musicTypeM = "mp3"

                # Downloads the highest quality stream available for the YouTube URL inputted as a .mp4 video file 
                originalMusicFileY = YouTube(optionThreeURL).streams.get_highest_resolution().download()

                # Converts the .mp4 file to .mp3 by getting rid of the .mp4 extension by splitting 1 time at index 0 and appends .mp3
                convertedMusicFileM = originalMusicFileY.split(".mp4", 1)[0] + f".{musicTypeM}"

                # Sets variable for the video process of the original YouTube file
                videoProcess3 = VideoFileClip(originalMusicFileY)

                # Sets variable for the audio process of the original YouTube file
                audioProcess3 = videoProcess3.audio

                # Sets variable for the audio process of the converted .mp3 file
                audioProcess3.write_audiofile(convertedMusicFileM)

                # Closes both audio and video processes of the original YouTube file
                audioProcess3.close()
                videoProcess3.close()

                # Removes the original downloaded mp4 video YouTube file from the current directory
                os.remove(originalMusicFileY)

                # Outputs "Done!" to indicate user that program has ended
                print("Done!")

        # .mp3 to .wav file conversion
        elif num == "4":
                # Asks the user to input the current directory name of the file to be converted
                optionThreeURL = input("Enter the current directory name of the file that you want to convert (i.e. D:/example/Bandit.mp3): ")
                
                # Asks the user to input the new directory name of the file as if it was converted
                convertedURL = input("Now enter the new directory name replacing the .mp3 with .wav (i.e. D:/example/Bandit.wav): ")

                # Returns the .mp3 file at current directory as an AudioSegment object and set it to a variable
                sound = pydub.AudioSegment.from_mp3(optionThreeURL)

                # Exports the variable as a new directory in the format of new .wav file extension
                sound.export(convertedURL, format="wav")

                # Outputs "Done!" to indicate user that program has ended
                print("Done!")

        # Error-handling
        else:
                # Outputs error message if user did not choose one of the four indicated music conversions
                print("Error, did not input a number associated to a conversion. Please restart the program and input one of the possible numbers indicated")
        
if __name__ == '__main__':
    # calls the main function
    main()



    
