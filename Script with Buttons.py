from tkinter import *
from tkinter import filedialog
import os
import fnmatch

pattern = '*.mp3'
pattern_2 = '*.flac'

root = Tk()
root.title('M3U-parser')
root.geometry('250x250+300+200')


def button_muse_folder():
    root.directory1 = filedialog.askdirectory(title="Выбор папки с музыкой", mustexist=1)
    A = root.directory1
    print(A)
    return A

button1 = Button(root, bg="white", text="Выбор папки\nисполнителей", width=21, height=3, fg='black',
                 font='arial 14', command=button_muse_folder)
button1.pack()

def button_playlist_folder():
    root.directory2 = filedialog.askdirectory(title="Выбор папки для сохранений плейлистов", mustexist=1)
    A = root.directory2
    print(A)
    return A

button2 = Button(root, bg="white", text="Выбор папки для \nсохранения плейлистов", width=21, height=3, fg='black',
                 font='arial 14', command=button_playlist_folder)
button2.pack()

music_folder = (button_muse_folder() + '\\')
Playlists_folder = (button_playlist_folder() + '\\')

def button_start():

    Ch = 0

    try:
        while True:

            Artist = os.listdir(music_folder)[Ch]

            if music_folder == Playlists_folder:
                root1 = Tk()
                root1.title('CLOSER')
                root1.geometry('250x250+300+200')
                root1.tk_focusPrev()
                but = Button(root1, bg="white", text="Выбери папку для \nплейлистов!", width=21, height=3, fg='black',
                 font='arial 14')
                but.bind('<Button-1>', root1.destroy())
                but.pack()
                root1.mainloop()
            else:
                Playlist_saver = open(Playlists_folder + str(Artist) + '.m3u', 'tw',
                                      encoding='utf-8')
                for folder, subdirs, files in os.walk(music_folder + os.listdir(music_folder)[Ch]):
                    for filename in fnmatch.filter(files, pattern):
                        fullname = os.path.join(folder, filename)
                        Playlist_saver.write("\n" + fullname.replace('\\', '/'))

                    for filename in fnmatch.filter(files, pattern_2):
                        fullname = os.path.join(folder, filename)
                        Playlist_saver.write("\n" + fullname.replace('\\', '/'))
                Playlist_saver.close()
                Ch = Ch + 1
    except:
        return 'sucks'

button_strt = Button(root, text='НАЧАТЬ', width=21, height=3, bg='red', fg='white', font='arial 14',
                     command=button_start)
button_strt.pack()
root.mainloop()

