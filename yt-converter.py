import sys
import pytube
import moviepy.editor as mp
import os
import time
import psutil
import colorama
from colorama import Fore, Style

colorama.init()


def download_youtube_video(url, output_path, counter):
    print(f"{Fore.LIGHTYELLOW_EX}Downloading the youtube video please wait: {url}{Style.RESET_ALL}")
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_lowest_resolution()
        title = youtube.title

        custom_title = input(
            f"{Fore.LIGHTYELLOW_EX}Enter a custom file name (press enter to use the default title): {Style.RESET_ALL}")
        if custom_title:
            output_filename = f"{counter}. {custom_title}.mp4"
        else:
            output_filename = f"{counter}. {title}.mp4"

        output_filepath = os.path.join(output_path, output_filename)

        video.download(output_path, filename=output_filename)

        print(f"{Fore.LIGHTGREEN_EX}Video downloaded successfully.{Style.RESET_ALL}")
        return output_filepath, title
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}An error occurred while downloading the video: {e}{Style.RESET_ALL}")
        return None, None


def convert_to_mp3(video_path, output_path):
    print(f"{Fore.LIGHTYELLOW_EX}Converting video to MP3{Style.RESET_ALL}")
    try:
        video = mp.VideoFileClip(video_path)
        output_filename = f"{os.path.splitext(os.path.basename(video_path))[0]}.mp3"
        output_filepath = os.path.join(output_path, output_filename)
        video.audio.write_audiofile(output_filepath)
        print(f"{Fore.LIGHTGREEN_EX}Conversion completed successfully.{Style.RESET_ALL}")
        return output_filepath
    except Exception as convert_error:
        print(f"{Fore.LIGHTRED_EX}An error occurred during the conversion: {convert_error}{Style.RESET_ALL}")
        return None


def delete_file(file_path):
    retries = 2  # Number of deletion retries
    delay = 1  # Delay in seconds between each retry

    for _ in range(retries):
        try:
            os.unlink(file_path)
            print(f"{Fore.LIGHTGREEN_EX}File deleted: {file_path}{Style.RESET_ALL}")
            return True
        except Exception as delete_error:
            print(f"{Fore.LIGHTRED_EX}An error occurred while deleting the file: {delete_error}{Style.RESET_ALL}")
            time.sleep(delay)


output_directory = input("Enter the output directory path: ")

count_file = "count.txt"

if os.path.exists(count_file):
    with open(count_file, "r") as f:
        counter = int(f.read().strip())
else:
    counter = 1
    with open(count_file, "w") as f:
        f.write(str(counter))

while True:
    youtube_url = input("Enter the YouTube URL (or press enter to exit): ")

    if not youtube_url:
        break

    video_filepath, video_title = download_youtube_video(youtube_url, output_directory, counter)
    if video_filepath and video_title:
        audio_filepath = convert_to_mp3(video_filepath, output_directory)
        if audio_filepath:
            print(
                f"{Fore.LIGHTGREEN_EX} MP3 file saved at: {audio_filepath}{Style.RESET_ALL}")
            for proc in psutil.process_iter():
                try:
                    open_files = proc.open_files()
                    if open_files and open_files[0].path == video_filepath:
                        proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, psutil.Error) as error:
                    print(f"{Fore.LIGHTYELLOW_EX}An error occurred while terminating the process: {error}{Style.RESET_ALL}")
                    print(f"{Fore.LIGHTRED_EX}Error Details: {error.__class__.__name__}: {str(error)}{Style.RESET_ALL}")
                    pass

            if delete_file(video_filepath):  # Delete the MP4 file
                print(f"{Fore.LIGHTGREEN_EX}File deletion successful.{Style.RESET_ALL}")
            else:
                print(f"{Fore.LIGHTRED_EX}File deletion failed.{Style.RESET_ALL}")
        else:
            print(f"{Fore.LIGHTRED_EX}Conversion failed.{Style.RESET_ALL}")

        counter += 1

        with open(count_file, "w") as f:
            f.write(str(counter))

            exit()
