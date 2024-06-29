import tkinter
import customtkinter
from pytube import YouTube

#Functions
def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text = ytObject.title, text_color ="white")
        finishlabel.configure(text ="")
        video.download()
        finishlabel.configure(text = "Downloaded!")
    except:
        finishlabel.columnconfigure(text = "Download Error", text_color = "red")

def on_progress(stream, chunks, bytes_remain):
    total_size = stream.filesize
    bytes_reaming = total_size - bytes_remain
    percentage_of_complete = bytes_reaming / total_size * 100
    per = str(int(percentage_of_complete))
    pPercentage.configure(text= per + '%')
    pPercentage.update()

    #update progress bar
    progressbar.set(float(percentage_of_complete) / 100 )

#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


#Our app Frame
app = customtkinter.CTk()
app.geometry("1280x720")
app.title("Tonmoy yt_downloder")


#UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx = 10, pady = 10)

#Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width= 350, height= 40, textvariable= url_var)
link.pack()

#Finish Label
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

# Progress precentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

#Progressbar
progressbar = customtkinter.CTkProgressBar(app, width= 400)
progressbar.set(0)
progressbar.pack(padx = 10, pady = 10)

#dwonload Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx = 10, pady = 10)

#Run app
app.mainloop()