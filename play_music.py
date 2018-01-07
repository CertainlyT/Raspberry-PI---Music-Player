import random, sys, pickle, subprocess


class PlayMusic:
    def __init__(self):
        self.filename = '/home/pi/music_list.dat'

    def read_musicdb(self):
        try:
            fH = open(self.filename, 'rb')
        except FileNotFoundError:
            sys.exit()

        db = []
        try:
            db = pickle.load(fH)
        except:
            sys.exit()

        fH.close()
        return db

    def shuffle_music(self, db):
        if len(db) == 0:
            return self.shuffle_music(self.read_musicdb())
        length = len(db)
        random_num = random.randint(0, length - 1)
        artist = db[random_num]['Artist']
        title = db[random_num]['Title']
        self.set_nowplaying(artist, title)
        print("Artist: %s\nTitle: %s" % (artist, title))
        subprocess.call(['omxplayer', '--vol', '-2000', "/home/pi/Music/" + db[random_num]['FileName']])
        db.remove(db[random_num])

    def set_nowplaying(self, a, t):
        nowplaying_db = '/home/pi/nowplaying.dat'
        fH = open(nowplaying_db, 'wb')
        db = [{'Artist': a, 'Title': t}]
        pickle.dump(db, fH)
        fH.close()


if __name__ == "__main__":
    p = PlayMusic()
    music_db = p.read_musicdb()
    try:
        while 1:
            p.shuffle_music(music_db)
    except KeyboardInterrupt:
        sys.exit()
