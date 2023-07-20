# MP4 to MP3 converter for lana

## Known Issue
- There is a known bug where the deletion of the downloaded .mp4 file may fail due to a file lock from another process. As a result, the script is unable to delete the .mp4 file automatically. To address this issue, you need to manually delete the .mp4 file after the conversion is complete. You will be provided with the file path of the downloaded .mp4 file in the console output.

## Requirements

- Python 3.x
- Required Python packages: pytube, moviepy, psutil, colorama
