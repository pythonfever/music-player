from tkinter import *
from tkinter import filedialog
from pygame import mixer
from os import chdir, listdir


root = Tk()
root.title("Music Player By PYTHON__FEVER")
root.geometry("920x670+250+5")
root.configure(bg="#0f1a2b")
root.resizable(False,False)

mixer.init()

def open_folder():
    path = filedialog.askdirectory()
    if path:
        chdir(path)
        songs = listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_song():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(music_name)
    mixer.music.play()
    music.config(text=music_name[0:-4])

icon = PhotoImage(file="./images/logo.png")
root.iconphoto(False,icon)

Top = PhotoImage(file="./images/top.png")
Label(root,image=Top,bg='#0f1a2b').pack()

logo=PhotoImage(file="./images/logo.png")
Label(root,image=logo,bg='#0f1a2b').place(x=69.5,y=105)

#Buttons
Play = PhotoImage(file="./images/play.png")
Button(root, image=Play,bg="#0f1a2b",bd=0,command=play_song).place(x=100,y=330)

Stop = PhotoImage(file="./images/stop.png")
Button(root, image=Stop,bg="#0f1a2b",bd=0,command=mixer.music.stop).place(x=15,y=450)

Resume = PhotoImage(file="./images/resume.png")
Button(root, image=Resume,bg="#0f1a2b",bd=0,command=mixer.music.unpause).place(x=120,y=450)

Pause = PhotoImage(file="./images/pause.png")
Button(root, image=Pause,bg="#0f1a2b",bd=0,command=mixer.music.pause).place(x=230,y=450)

menu = PhotoImage(file="./images/menu.png")
Label(root,image=menu,bg='#0f1a2b').pack(padx=10,pady=20,side=RIGHT)

music = Label(root,text="",font=("arial",15),fg="white",bg="#0f1a2b")
music.place(x=150,y=310,anchor='center')

music_frame = Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=343,y=350,width=560,height=280)

Button(root,text="Open Folder", width=15,height=2,font=("arial",10,"bold"),fg="white",bg="#21b3de",command=open_folder).place(x=350,y=300)

scroll=Scrollbar(music_frame)
playlist = Listbox(music_frame,width=100,font=("arial",10),bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()