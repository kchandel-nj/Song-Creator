# Libraries
from Note import Note
from FrequencyPlayer import FrequencyPlayer

import time


player = FrequencyPlayer()
player.play(Note("A", 4), 1000)
print("a4")
#time.sleep(1)
player.play(Note("A", 5), 1000)
print("a5")

a4 = Note("A", 4)
player.play(a4, 1000)
player.play(a4.halfStepUp(), 1000)
player.play(a4.halfStepUp().halfStepUp(), 1000)
player.play(a4.halfStepUp().halfStepUp().halfStepUp(), 1000)
print(a4.halfStepUp().halfStepUp().halfStepUp())