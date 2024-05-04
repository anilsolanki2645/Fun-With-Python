from pytube import YouTube
import os
import time

# Function to display download progress
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    download_speed = (total_size - bytes_remaining) / (1024 * 1024 * (time.time() - start_time))  # Convert to MB/s
    print(f"\rDownloading... {percentage:.2f}% ({download_speed:.2f} MB/s)","\n")

# Ask user for YouTube video URL
url = input("Enter the YouTube video URL: ")

try:
    # Create YouTube object
    video = YouTube(url, on_progress_callback=on_progress)

    # Find the stream with both video and audio, highest resolution
    stream = video.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

    if stream:
        # Get the filename and file size
        filename = stream.default_filename
        filesize = stream.filesize / (1024 * 1024)  # Convert to MB

        # Start time for download
        start_time = time.time()

        # Download video
        print("\n")
        print(f"Downloading {filename} ({filesize:.2f} MB)...")
        stream.download()

        # Calculate download time
        end_time = time.time()
        download_time = end_time - start_time

        print(f"\nDownloaded {filename} ({filesize:.2f} MB) in {download_time:.2f} seconds.")
    else:
        print("No stream with both video and audio found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

