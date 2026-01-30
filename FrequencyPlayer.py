# Libraries
import winsound
import time

from Note import Note

class FrequencyPlayer:

    """
    Docstring for FrequencyPlayer

    Plays a pitch given the note.
    """
    
    def __init__(self):
        """
        Docstring for __init__

        Prepares the object.
        
        :param self: The object
        """
        pass

    def play(self, note: Note, time: int):
        winsound.Beep(int(note.frequency), time)

#winsound.Beep(440, 1000)
