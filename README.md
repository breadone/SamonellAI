# SamonellAI

An extremely silly use of time; this project aims to use a CNN to determine from a list of videos (say from a youtube channel), which video a selected frame (or part of a frame) belongs to.

This was inspired by a friend and I sending back and forth a single frame of a video from the youtube channel Samonella, and then trying to guess which video it was from. And procrastination. So much procrastination.

In theory this will work on any youtube channel or really any any set of videos, but i dunno man, this is so silly already and you're obviously free to do what you like with it.

## Usage

### Setup (downloading images)

**This requires yt-dlp and ffmpeg, make sure these are installed.**

To use the default setup for samonella, simply run `setup.sh`. This script downloads each video from the channel, and then extracts each unique frame and places it in a directory for model training.

This is obviously quite CPU and network intensive, and will take some time. In my case with an i5 13600K, it took around 5 minutes (more like 15 on an M1 macbook pro), and ended up with a `train` folder of around 4GB.

Also note that the yt-dlp output format seems to vary between .webm and .mp4, if an error occurs about no such file, just change all mentions of .webm in `setup.sh` to .mp4 or vice versa. it seems that on macos it outputs .mp4 and on linux it outputs .webm,,, ¯\\_(ツ)_/¯

### Running
open `src/main.py` and edit the path for the image you want to predict. 

from the `src` directory, run `python3 main.py`. This will create and train the model based on the input images.

Training is extremely resource intensive for your system, it will take some time. If you have an Nvidia GPU (and the necessary drivers), it will utilise the CUDA framework to MASSIVELY speed up this process. 

If it is taking too long, or you get an error that you have run out of RAM/VRAM, reduce `batch_size`, `image_width`, and `image_height` until it is within your accepted parameters.

Once it is done this process, it should output the predicted result and its confidence for it.