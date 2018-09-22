import os
import fnmatch

music_folder = 'Way\\to\\folder\\'
Playlists_folder = 'Way\\to\\folder\\Playlists\\'

pattern = '*.mp3'
pattern_2 = '*.flac'

Ch = 0
lis = []
try:
    while True:
        Artist = os.listdir(music_folder)[Ch]
        Playlist = open(music_folder + str(Artist) + '\\' + (str(Artist) + '.m3u'), 'tw', encoding='utf-8')
        Playlist_saver = open(Playlists_folder + str((Artist) + '.m3u'), 'tw', encoding='utf-8')

        Playlist.write('#EXTM3U\n')
        Playlist_saver.write('#EXTM3U\n')

        for folder, subdirs, files in os.walk(music_folder + os.listdir(music_folder)[Ch]):
            for filename in fnmatch.filter(files, pattern):

                fullname = os.path.join(folder, filename)
                lis.append(fullname.replace('\\', '\\'))
                Playlist_saver.write("\n" + fullname)

            for filename in fnmatch.filter(files, pattern_2):
                fullname = os.path.join(folder, filename)
                Playlist_saver.write("\n" + fullname)
        Playlist_saver.close()
        print(Ch)
        Ch = Ch + 1
except:
    print('Except')