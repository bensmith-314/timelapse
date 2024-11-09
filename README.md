# Screen Timelapse
This is a work in progress utility to allow for easy screen capture of your screen on regular intervals. This will screen shot your computer on regular intervals and store the images in the images/ folder for access after the script is finished.

## Taking Screen Timelaspe
The timelapse script is designed to be fairly simple to use. When in the directory of the Repo, just run the following to get started.
```sh
./timelapse.sh
```
This will give the option to clear the current collection of images if desired, continue from a specified frame (stored in frameNumber.txt), or start fresh with no images present.

## Creating Timelapse
After you have a collection of images in your images/ folder, run the createTimelapse.py script to generate a .mov file with all of your images. 

This will create a timelapse using ImageSequenceClip from moviepy. Make sure to have it installed prior to running this script.
```sh
pip3 install moviepy
```

```sh
python3 createTimelapse.py
```

## Helper Script
This script clears the images/ folder.

```sh
./clearImages
```

## Preferences
There are a number of preferences that can be set in the head of timelapse script that you are able to update and change to fit your needs:
- startMessage1="Starting Timelapse Image Capture in "
- startMessage2=" seconds"
- timeToStart=5 # Countdown at beginning
- imageTiming=1 # Time between screencaptures
- frameNumber=0 # Current Frame
- isRunning=""  # Status of Timelapse

After running the timelapse script you will have a directory (images/) of images that can be combined into a timelapse using the createTimelapse.py script, QuickTime Player on MacOS or your tool of choice.
