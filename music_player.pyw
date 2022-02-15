import sys
packages_path = r"D:\pythonProject2\venv2\Lib\site-packages"
sys.path.append(packages_path)

from pygame import init, mixer
from keyboard import read_key
from time import sleep

song_path = r"C:\Users\seenusanjay\Downloads\Playerunknown s Battlegrounds Main Theme.mp3"

init()
mixer.init()
sound = mixer.Sound(song_path)
sound.set_volume(0.1)
sound.play(maxtime=40000)
while mixer.get_busy():
    sleep(0.5)
    key = read_key()
    if key == "+":
        sound.set_volume(sound.get_volume() + 0.1)
    elif key == "-":
        sound.set_volume(sound.get_volume() - 0.1)
    elif "ctrl" in key:
        sound.stop()
    print(sound.get_volume())

