# session 6

from pyglet import *
from datetime import *
from os import *

sound = resource.media("alarm.wav")

alarm = [21, 56]
m = -1
while True:
    if not m == datetime.now().minute:
        m = datetime.now().minute

        if m == alarm[1] and datetime.now().hour == alarm[0]:
            print("!!!ALARM!!!")

            sound.play()
            app.run()
