
import tkinter as tk
import customtkinter as ctk
from pytube import YouTube as yt
import urllib.request 
from PIL import Image 

# Globals
video_title = ""
video_thumbnail_url = ""
video_splash_image = "images/video_splash_image.jpg"

def startDownload():
    global video_title, video_url, video_splash_image
    try:
        yt_link = link.get()
        yt_object = yt(yt_link, on_progress_callback=on_progess)
        # video = yt_object.streams.get_highest_resolution()
        # video.download('videos')
        video_thumbnail_url = yt_object.thumbnail_url
        video_title = yt_object.title
        label.configure(text=video_title)
        finish_label.configure(text="")
        # Fetch the splash image
        urllib.request.urlretrieve(video_thumbnail_url, video_splash_image)
        my_image.configure(dark_image=Image.open(video_splash_image))
    except Exception as e:
        finish_label.configure(
            text=f"Error occurred with video download:\n{e}", text_color="red")
    else:
        finish_label.configure(text="Download complete!", text_color="white")
        # print("Video Title = " + video_title)
        # print("Video Splash URL = " + video_thumbnail_url)

def on_progess(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_complete = bytes_downloaded / total_size * 100
    pct = str(int(pct_complete))
    progress_pct.configure(text = pct + ' %')
    progress_pct.update()
    progress_bar.set(float(pct_complete) / 100)

# System settings
ctk.set_appearance_mode("dark")     # Modes: system (default), light, dark
ctk.set_default_color_theme("blue") # Themes: blue (default), dark-blue, green

# App Frame
app = ctk.CTk()
app.geometry("720x500")
app.title("YouTube Downloader")
app.iconbitmap('images/Treetog-I-Audio-File.256.png')

# Label
label = ctk.CTkLabel(app, text="Insert a YouTube link")
label.pack(padx=10, pady=10)

url_var = tk.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finish_label = ctk.CTkLabel(app, text="")
finish_label.pack(padx=5, pady=5)

# Progress Percentage
progress_pct = ctk.CTkLabel(app, text="0 %")
progress_pct.pack(padx=5, pady=5)

# Progress Bar
progress_bar = ctk.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=5, pady=5)

# Download Button
download_button = ctk.CTkButton(app, text="Download", command=startDownload)
download_button.pack(padx=5, pady=5)

# Video splash image
my_image = ctk.CTkImage(
    dark_image=Image.open(video_splash_image),
    size=(384, 216))  # 1280 x 720 (original)
my_image_label = ctk.CTkLabel(app, image=my_image, text="Video Splash Image")
my_image_label.pack(padx=5, pady=5)



# Run app as loop
app.mainloop()
