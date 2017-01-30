import random

from chord_factory import ChordFactory


class ChordComposer(object):
    BEATS_PER_CHORD = 16

    def __init__(self,scale):
        self.scale = scale

    def get_random_chords(self,duration_beats):
        assert duration_beats % self.BEATS_PER_CHORD == 0, "Duration must be divisble by {0}".format(self.BEATS_PER_CHORD)

        chords = []
        time = 0
        while time < duration_beats:
            chord = self.get_random_chord()
            chord.time = time
            chords.append(chord)
            time += self.BEATS_PER_CHORD

        return chords

    def get_random_chord(self):
        random_int = random.randint(0,6)
        factory = ChordFactory(self.scale)
        random_degree = factory.degrees[random_int]
        chord = factory.get_chord(random_degree,self.BEATS_PER_CHORD)
        return chord

    def get_test_chords(self,*args):
        return [
        #Cmaj7
        [(('C',1),('E',2),('G',1),('B',2)),0,16],

         #Amin7
        [(('A',1),('C',2),('E',1),('G',1)),16,16], 

        #Emin7
        [(('E',1),('G',2),('B',1),('D',2)),32,16],

        #Fmaj7
        [(('F',1),('A',2),('C',1),('E',1)),48,16], 

        #Dmin7
        [(('D',1),('F',2),('A',1),('C',2)),64,16],

        #GDom7
        [(('G',1),('B',2),('D',1),('F',1)),80,16],

        #BHalfdim7
        [(('B',1),('D',2),('F',1),('A',1)),96,16], 

        #Cmaj7
        [(('C',1),('E',2),('G',1),('B',2)),112,16],

        #Amin7
        [(('A',1),('C',2),('E',1),('G',1)),128,16], 

        #Emin7
        [(('E',1),('G',2),('B',1),('D',2)),144,16],

        #Fmaj7
        [(('F',1),('A',2),('C',1),('E',1)),160,16], 

        #Dmin7
        [(('D',1),('F',2),('A',1),('C',2)),176,16],

        #GDom7
        [(('G',1),('B',2),('D',1),('F',1)),192,16],

        #BHalfdim7
        [(('B',1),('D',2),('F',1),('A',1)),208,16], 

        #Cmaj7
        [(('C',1),('E',2),('G',1),('B',2)),224,32],
        ]