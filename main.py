import tkinter
import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube PyDownloader")
label = customtkinter.CTkLabel( app, 
                                text="Insert a valid YouTube link",
                                font=("sans-serif", 18))
label.pack(padx=10, pady=10)
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40,
                              textvariable=url_var)
link.pack()

def getVideoDownload():
  try:
    Object = YouTube(url_var.get(), on_progress_callback=getProgress)
    Video = Object.streams.get_highest_resolution()
    message.configure(text=f'Downloading {Video.title}', text_color="white")
    Video.download()
    message.configure(text="Download finished.", text_color="white")
  except:
    message.configure(text="Download error.", text_color="red")

def getAudioDownload():
  try:
    Object = YouTube(url_var.get(), on_progress_callback=getProgress)
    Audio = Object.streams.filter(only_audio=True).get_by_itag(140)
    message.configure(text=f'Downloading {Audio.title}', text_color="white")
    Audio.download()
    message.configure(text="Download finished.", text_color="white")
  except:
    message.configure(text="Download error.", text_color="red")


def getProgress(stream, chunk, bytesRemaining):
  size = stream.filesize
  downloaded = size - bytesRemaining
  progress = downloaded / size * 100
  progressPerct.configure(text=f'{str(int(progress))}%')
  progressPerct.update()
  progressBar.set(float(progress) / 100)
  progressPerct.pack()
  progressBar.pack(padx=10, pady=10)


message = customtkinter.CTkLabel(app, text="")
message.pack(padx=10, pady=10)
downloadVideoButton = customtkinter.CTkButton(app, text="Download video",
                                          command=getVideoDownload,
                                          font=("sans-serif", 16) )
downloadAudioButton = customtkinter.CTkButton( app, text="Audio only",
                                          command=getAudioDownload,
                                          font=("sans-serif", 16) )
downloadVideoButton.pack(padx=10)
downloadAudioButton.pack(pady=20)

progressPerct = customtkinter.CTkLabel(app, text="")
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)

app.mainloop()