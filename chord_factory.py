class ChordFactory(object):
    degree_intervals = {
        'I':    [0,2,4,6],
        'II':   [1,3,5,0],
        'III':  [2,4,6,1],
        'IV':   [3,5,0,2],
        'V':    [4,6,1,3],
        'VI':   [5,0,2,4],
        'VII':  [6,1,3,5]
    }

    def __init__(self, scale):
        self.scale = scale

    @property
    def degrees(self):
        return self.degree_intervals.keys()

    def get_chord(self,degree,beats):
        intervals = self.degree_intervals[degree]
        octave = 1 # use no/shitty voicings for now
        notes = [(self.scale[i],octave) for i in intervals]
        return Chord(notes,beats)

class Chord(object):
    time = 0
    def __init__(self,notes,beats):
        self.notes = notes
        self.beats = beats

    def with_simple_voicing():
        # 1 3 5 7
        pass

    def with__partial_open_voicing():
        # 1 3(2) 5 7
        pass

    def with_open_voicing():
        # 1 3(2) 5 7(2)
        pass
