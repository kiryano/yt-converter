# Changelog

## [Released]

### Changed
- Updated the conversion process to use moviepy for direct MP4 to MP3 conversion.

## [0.2.0] - 2023-7-18
### Added
- Added support for specifying a custom file name.

### Changed
- Improved error handling during download and conversion.

## [0.1.0] - 2023-7-18
### Added
- Basic functionality to download YouTube videos.

## Known Issue
- There is a known bug where the deletion of the downloaded .mp4 file may fail due to a file lock from another process. As a result, the script is unable to delete the .mp4 file automatically. To address this issue, you need to manually delete the .mp4 file after the conversion is complete. You will be provided with the file path of the downloaded .mp4 file in the console output.

## Requirements

- Python 3.x
- Required Python packages: pytube, moviepy, psutil, colorama
