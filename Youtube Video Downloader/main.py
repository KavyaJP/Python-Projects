import yt_dlp

link = input("Enter the link of the video: ")
filename = input("Enter the filename for the video: ").strip() + ".mp4"
output_path = input("Enter the name of the video output folder")

ydl_opts = {
    "outtmpl": f"{output_path}/{filename}",
    "format": "best",
}

i = 1
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print(f"Downloading video no. {i}")
    ydl.download([link])
    print(f"Finished downloading video {i}")
    i += 1

print("All videos downloaded successfully!")
