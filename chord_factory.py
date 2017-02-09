from random import randint

class Voicing:
    simple = [1,1,1,1]
    open = [1,2,1,2]
    partial_open = [1,2,1,1]

    @staticmethod
    def get_random():
        return [randint(0,1), randint(1,4),randint(0,2), randint(2,4)]

class ChordFactory(object):
    degree_intervals = {
        # format is (scale degree, octave)
        # default is 'root' voicing
        'I':    [{'note':0,'octave':1},{'note':2,'octave':1},{'note':4,'octave':1},{'note':6,'octave':1}],
        'II':   [{'note':1,'octave':1},{'note':3,'octave':1},{'note':5,'octave':1},{'note':0,'octave':2}],
        'III':  [{'note':2,'octave':1},{'note':4,'octave':1},{'note':6,'octave':1},{'note':1,'octave':2}],
        'IV':   [{'note':3,'octave':1},{'note':5,'octave':1},{'note':0,'octave':2},{'note':2,'octave':2}],
        'V':    [{'note':4,'octave':1},{'note':6,'octave':1},{'note':1,'octave':2},{'note':3,'octave':2}],
        'VI':   [{'note':5,'octave':1},{'note':0,'octave':2},{'note':2,'octave':2},{'note':4,'octave':2}],
        'VII':  [{'note':6,'octave':1},{'note':1,'octave':2},{'note':3,'octave':2},{'note':5,'octave':2}]
    }

    def __init__(self, scale):
        self.scale = scale

    @property
    def degrees(self):
        return self.degree_intervals.keys()

    def get_chord(self,degree,beats,voicing=Voicing.simple):
        intervals = self.degree_intervals[degree]
        notes = [(self.scale[i['note']], i['octave']) for i in intervals]
        
        for idx in range(len(notes)):
            notes[idx] = (notes[idx][0],notes[idx][1]+voicing[idx]-1)

        return Chord(notes,beats)

class Chord(object):
    time = 0
    def __init__(self,notes,beats):
        self.notes = notes
        self.beats = beats



