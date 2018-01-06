import pickle
import subprocess
import os
from tinytag import TinyTag


class ScanMusic:
    def __init__(self):
        self.filename = '/home/pi/music_list.dat'

    def make_musicdb(self):
        try:
            subprocess.call(['rm', self.filename])
            fH = open(self.filename, 'rb')
        except:
            return []
        else:
            return []

    def write_musicdb(self, db):
        fH = open(self.filename, 'wb')
        pickle.dump(db, fH)
        fH.close()

    def search_music(self, directory, db):
        music_files = os.listdir(directory)
        for music in music_files:
            tag = TinyTag.get("/home/pi/Music/" + music)
            try:
                record = [{"FileName": music, "Artist": tag.artist, "Title": tag.title}]
            except:
                pass
            else:
                db += record

    def showScoreDB(self, scdb, keyname):
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                print(attr + "=" + str(p[attr]), end=' ')
            print()


if __name__ == "__main__":
    s = ScanMusic()
    musicdb = s.make_musicdb()
    s.search_music("/home/pi/Music/", musicdb)
    s.write_musicdb(musicdb)
    print(len(musicdb))