import customtkinter as ck
from tkinter import *
import vlc
import time
from tkinter import filedialog
from pygame import mixer
import os

ck.set_appearance_mode("System")  # Modes: system (default), light, dark
ck.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class CustomApp(ck.CTk):
    
    def __init__(self):
        super().__init__()
        self.geometry('1080x756')
        self.title('Music Player')
        self.resizable(0,0)
        self.Playlist = Listbox(self)
        self.Playlist.pack(side=LEFT, fill=BOTH)
        self.AddBtn = ck.CTkButton(self, text="Add Music", command=self.Add_Music, cursor='hand2')
        self.AddBtn.place(x=10,y=700)
        self.PlayBtn = ck.CTkButton(self, text="Play", command=self.Play_Music, cursor='hand2')
        self.PlayBtn.place(x=200,y=700)
        self.StopBtn = ck.CTkButton(self, text="Stop", command=self.Stop_Music, cursor='hand2')
        self.StopBtn.place(x=350,y=700)
        self.PauseBtn = ck.CTkButton(self, text="Pause", command=self.Pause_Music, cursor='hand2')
        self.PauseBtn.place(x=500,y=700)
        img_old=PhotoImage(file='logo.png')
        # img_resized=img_old.resize((341,256)) # new width & height
        self.logo = img_old
        Label(self, image=self.logo, bg="#1A1A1A").place(x=255, y=115)
        self.placeholder = ck.CTkLabel(self,text='', font=('Ubuntu',30))
        self.placeholder.place(x=300, y=450)
        self.Playlist.bind("<<ListboxSelect>>", self.callback)

    def callback(self,event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            self.placeholder.configure(text=data)
        else:
            self.placeholder.configure(text="")


    def Add_Music(self):
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            songs = os.listdir(path)

            for song in songs:
                # print(song)
                if song.endswith(".mp3"):
                    self.Playlist.insert(END, song)
 
    def Play_Music(self):
        if self.media_player.play():
            self.Stop_Music()
        Music_Name = self.Playlist.get(ACTIVE)
        # print(Music_Name[0:-4])
        self.media_player = vlc.MediaPlayer()
  
        # media object
        media = vlc.Media(Music_Name)
        
        # setting media to the media player
        self.media_player.set_media(media)
        
        # start playing video
        self.media_player.play()
        # wait time
        time.sleep(0.5)
        
        # getting the duration of the video
        duration = self.media_player.get_length() // 1000
        minutes = duration // 60
        seconds = duration % 60
        # printing the duration of the video
        print(f"Duration : {minutes} : {seconds}")
        
    def Stop_Music(self):
        self.media_player.stop()

    def Pause_Music(self):
        if self.PauseBtn.cget('text') == 'Pause':
            self.PauseBtn.configure(text="Unpause")
        else:
            self.PauseBtn.configure(text="Pause")
        self.media_player.pause()

def main():
    app = CustomApp()
    mixer.init()
    app.mainloop()
    

if __name__ == "__main__":
    main()