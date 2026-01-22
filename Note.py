class Note:
    
    """
    Docstring for Note

    A note is determined by the A note in its relative octave, as A4 is the base case of 12 TET.
    Half steps are defined as the frequency * (2**(1/12))
    """

    def __init__(self, name: str, octave: int, frequency: float = 0.0):

        """
        Docstring for __init__

        Creates a note object
        
        :param self: The object
        :param name: The name of the note
        :type name: str
        :param octave: The octave the note is in
        :type octave: int
        :param frequency: The mathematical frequency that represents the note
        :type frequency: float
        """

        self.name = name.upper()
        self.octave = octave
        self.frequency = frequency
        if name == "A":
            if octave == 4:
                self.frequency: float = 440.0
            elif octave > 4:
                self.frequency: float = 440.0 * (2**(octave - 4))
            else:
                self.frequency: float = 440.0 / (2**(4 - octave))

    def halfStepUp(self):

        """
        Docstring for halfStepUp

        Returns the next note up
        
        :param self: The object
        :return: The note a half step up
        :rtype: Note
        """

        newName = self._translateSharp(f"{self.name}#")
        newOctave = self.octave
        if newName == "C":
            newOctave += 1
        return Note(newName, newOctave, self.frequency * (2**(1/12))) # frequency * (2**(1/12))
    
    def _translateSharp(self, name: str) -> str:

        """
        Docstring for _translateSharp

        Ensures sharps aren't added twice and ensures B# and E# converted to the enharmonic value
        Ensures G# loops back to A
        
        :param self: The object
        :param name: The name to be translated
        :type name: str
        :return: The new name of the note
        :rtype: str
        """

        if name.count('#') > 1:
            name = chr(ord(name[0]) + 1)
            if "H" in name:
                name = "A"
            return name
        if "B" in name:
            return "C"
        elif "E" in name:
            return "F"
        else:
            return name
        
    def halfStepDown(self):
        
        """
        Docstring for halfStepDown

        Returns the next note down
        
        :param self: The object
        :return: The note a half step down
        :rtype: Note
        """

        newName = self._translateFlat(f"{self.name}♭")
        newOctave = self.octave
        if newName == "B":
            newOctave -= 1
        return Note(newName, newOctave, self.frequency / (2**(1/12))) # frequency / (2**(1/12))
    
    def _translateFlat(self, name: str) -> str:

        """
        Docstring for _translateFlat

        Ensures flats aren't added twice and ensures Cb and Fb converted to the enharmonic value
        Ensures Ab loops back to G
        
        :param self: The object
        :param name: The name to be translated
        :type name: str
        :return: The new name of the note
        :rtype: str
        """

        if name.count('♭') > 1:
            name = chr(ord(name[0]) - 1)
            if "@" in name:
                name = "G"
            return name
        if "C" in name:
            return "B"
        elif "F" in name:
            return "E"
        else:
            return name
        
    def __str__(self) -> str:

        """
        Docstring for __str__

        Returns the note expressed by name and octave.
        
        :param self: The object
        :return: The note by name and octave
        :rtype: str
        """

        return f"{self.name}{self.octave}"