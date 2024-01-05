from pytube import YouTube
import os
#run this in a cmd window 
def download_video(url):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        print(f"Video name  {yt.title}")
        print(f"Your moms weight >> {round(video_stream.filesize / (1024 * 1024), 2)} MB")
        output_path = os.path.join(os.path.expanduser("~"), "Downloads")
        video_stream.download(output_path)
        print(f"done {os.path.join(output_path, yt.title)}.mp4")
    except Exception as e:
        print(f"error ☠")

if __name__ == "__main__":
    video_url = input("yt url")
    download_video(video_url)
