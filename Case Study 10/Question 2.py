from pytubefix import Playlist
from pytubefix.cli import on_progress
import os


def download_django_playlist(playlist_url, output_path='./django_tutorials'):
    try:
        # Initialize the Playlist object
        pl = Playlist(playlist_url)

        print(f"Playlist Name: {pl.title}")
        print(f"Total Videos: {len(pl.videos)}")

        # Create directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Loop through each video in the playlist
        for video in pl.videos:
            print(f"\nDownloading: {video.title}")

            # Get the highest resolution stream
            stream = video.streams.get_highest_resolution()

            # Download to the specified folder
            stream.download(output_path=output_path)

        print("\n--- All downloads completed! ---")

    except Exception as e:
        print(f"An error occurred: {e}")


# The specific Django playlist link you provided
playlist_link = "https://www.youtube.com/playlist?list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD"
download_django_playlist(playlist_link)