import json, psutil, pickle, sys

nowplaying = '/home/pi/nowplaying.dat'


def application(environ, start_response):
    status = '200 OK'
    if "omxplayer" not in (p.name() for p in psutil.process_iter()):
        response_body = bytes(json.dumps({"Artist": "None", "Title": "None"}), 'utf-8')
    else:
        artist, title = get_nowplaying()
        response_body = bytes(json.dumps({"Artist": artist, "Title": title}), 'utf-8')
    response_headers = [('Content-type', 'application/json'), ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]


def get_nowplaying():
    db = read_musicdb()
    return str(db[0]['Artist']), str(db[0]['Title'])


def read_musicdb():
    try:
        fH = open(nowplaying, 'rb')
    except FileNotFoundError:
        sys.exit()

    db = []
    try:
        db = pickle.load(fH)
    except:
        sys.exit()

    fH.close()
    return db

