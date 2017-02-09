from ..chord_factory import ChordFactory, Voicing
from ..chord_composer import ChordComposer

def test_c_major_first():
    scale = ['C','D','E','F','G','A','B']
    chord = ChordFactory(scale).get_chord('I',16)
    assert chord.notes == [('C',1),('E',1),('G',1),('B',1)]
    assert chord.beats == 16

def test_c_major_second():
    scale = ['C','D','E','F','G','A','B']
    chord = ChordFactory(scale).get_chord('II',16)
    assert chord.notes == [('D',1),('F',1),('A',1),('C',2)]
    assert chord.beats == 16

def test_c_major_open_voicing():
    scale = ['C','D','E','F','G','A','B']
    voicing = Voicing.open
    chord = ChordFactory(scale).get_chord('II',16,voicing)
    assert chord.notes == [('D',1),('F',2),('A',1),('C',3)]
    assert chord.beats == 16


def test_four_random_chords():
    scale = ['C','D','E','F','G','A','B']
    composer = ChordComposer(scale)
    num_chords = 4
    beats = ChordComposer.BEATS_PER_CHORD * num_chords
    chords = composer.get_random_chords(beats)
    assert len(chords) == num_chords
    for chord in chords:
        assert chord.beats == ChordComposer.BEATS_PER_CHORD

    assert chords[0].time == 0 * ChordComposer.BEATS_PER_CHORD
    assert chords[1].time == 1 * ChordComposer.BEATS_PER_CHORD
    assert chords[2].time == 2 * ChordComposer.BEATS_PER_CHORD
    assert chords[3].time == 3 * ChordComposer.BEATS_PER_CHORD