# YouTube Video to MP3 Converter for Lana

This script allows you to download YouTube videos and convert them to MP3 audio files.

## Features

- Download YouTube videos by providing the video URL.
- Convert downloaded videos to MP3 audio files.
- Customize the output file name or use the default video title.
- Terminate processes that may lock the video file during conversion or deletion.
- Delete the downloaded video file after conversion.
- Retry file deletion in case of failure.
- Colorful console output for better visibility.

## Known Issue
- There is a known bug where the deletion of the downloaded .mp4 file may fail due to a file lock from another process. As a result, the script is unable to delete the .mp4 file automatically. To address this issue, you need to manually delete the .mp4 file after the conversion is complete. You will be provided with the file path of the downloaded .mp4 file in the console output.

## Requirements

- Python 3.x
- Required Python packages: pytube, moviepy, psutil, colorama

## Installation

1. Clone the repository or download the script file to your local machine.
2. Install the required packages by running the following command:
   ```shell
   pip install pytube moviepy psutil colorama
