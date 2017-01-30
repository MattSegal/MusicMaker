class Scale:
    
    def __init__(self,root='C'):
        notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
        self.root = root.upper()
        assert self.root in notes, 'Note must be {0}'.format(notes)
        note_index = notes.index(self.root)
        self.notes = notes[note_index:] + notes[0:note_index]

    @property
    def major(self):
        major_intervals = [0,2,4,5,7,9,11] # This notation is half steps starting at 0
        return [self.notes[i] for i in major_intervals]

    @property
    def minor(self):
        minor_intervals = [0,2,3,5,7,8,10]
        return [self.notes[i] for i in minor_intervals]

"""
Other possible scales are:

    pentatonic  = ['C','D','E','G','A']
    blues       = ['C','D#','F','F#','A#']
    arabic      = ['C','C#','E','F','G','G#']
    spanish     = ['C', 'C#',  'E'  ,'F'  ,'G' , 'G#' ,'A#']
"""