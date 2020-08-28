import time

def make_readable(seconds):
    sec = seconds % 60
    seconds -= sec
    seconds = seconds / 60
    min = seconds % 60
    seconds -= min
    hrs = seconds / 60
    sec = str(int(sec))
    min = str(int(min))
    hrs = str(int(hrs))
    if len(sec) < 2:
        sec = '0' + sec
    if len(min) < 2:
        min = '0' + min
    if len(hrs) < 2:
        hrs = '0' + hrs

    return f"{hrs}:{min}:{sec}"
