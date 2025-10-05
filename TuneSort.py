from os import listdir, mkdir
from fnmatch import filter
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import shutil
from pygame import mixer
import music_tag 


root = Tk()
root.minsize(800,600)
root.maxsize(800,600)
root.configure(bg='#189AB4')
root.title('mixer.music_collection')


def closs(): 
    sol = messagebox.askokcancel('exit','برنامه بسته شود ؟')
    if sol == 1 :
        root.quit()
        exit()
        


while 1:
    filepath = askdirectory()
    folder = filter(listdir(filepath), '*.mp3')
    if len(folder) != 0:
        break
    messagebox.showinfo('error', '!در پوشه مورد نظر اهنگ یافت نشد')


list_musics = Listbox(root, font=("", 16), width=67, height=7, bg="#189AB4", borderwidth=1)
list_musics.place(x=-1,y=430)
for i in folder:
    list_musics.insert(0, i[:i.find(".mp3")])

list_genres = ["shad", "old", "pop", "remix", "song", "khareji", "bass", "mahali", "rap"]


def pp(e):
    if btn_pp.cget("text") == "Stop":
        btn_pp.configure(text="Play")
        mixer.music.pause()
    elif btn_pp.cget("text") == "Play":
        btn_pp.configure(text="Stop")
        mixer.music.unpause()

def next_time(e):
    mu = mixer.music.get_pos() // 100
    mixer.music.set_pos(mu+50)

def skip_music(e):
    list_musics.delete(0,0)
    music_play = folder.pop()
    mixer.music.load(filepath + '/{}'.format(music_play))
    mixer.music.play(start=5)

def set_gen(e, idx):
    global music_play
    print(idx, music_play)
    try:
        shutil.copy(filepath+'/{}'.format(music_play),'good\{}\{}'.format(idx, music_play))
    except:
        mkdir(f"good\{idx}")
        shutil.copy(filepath+'/{}'.format(music_play),'good\{}\{}'.format(idx, music_play))
    
    # tag_music = music_tag.load_file(filepath + '/{}'.format(music_play))
    # tag_music.remove_tag('genre')
    # tag_music.append_tag('genre', 'subtitle')
    # tag_music.save()
    list_musics.delete(0,0)
    music_play = folder.pop()
    mixer.music.load(filepath + '/{}'.format(music_play))
    mixer.music.play(start=5)




y = 50
x = 2
index = 1
for i in list_genres:
    Button(root, text=f"{index} "+i, font=("", 18), bg="#180AB4", width=8, command=lambda i=i: set_gen(0, i)).place(x=x,y=y)
    root.bind(str(index), lambda e, i=i: set_gen(e, i))
    y += 50
    index+=1
    if y == 350:
        x = 675
        y = 50


btn_next = Button(root, text="Skip Music", font=("", 16), width=15, height=2, bg="#188AB4", command=lambda: skip_music(0))
btn_next.pack(side="top")
root.bind('0', skip_music)
btn_pp = Button(root, text="Stop", font=("", 16), width=15, height=2, bg="#188AB4", command=lambda:pp(0))
btn_pp.pack(side="top")
root.bind('<space>', pp)
btn_jump = Button(root, text="Jump Music", font=("", 16), width=15, height=2, bg="#188AB4", command=lambda:next_time(0))
btn_jump.pack(side="top")
root.bind('<Right>', next_time)


mixer.init()
music_play = folder.pop()
mixer.music.load(filepath+'/{}'.format(music_play))
mixer.music.play(start=5)

root.mainloop()
