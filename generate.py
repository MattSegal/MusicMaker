from midi_generator import MIDIGenerator
from melody_composer import MelodyComposer
from chord_composer import ChordComposer
from scale import Scale

output_file_name = "output.mid"
duration_beats = 500
scale = Scale('C').major

test_melody = MelodyComposer().compose(scale,duration_beats)
chords = ChordComposer().get_test_chords()

MIDIGen = MIDIGenerator(output_file_name)

MIDIGen.addMelody(test_melody)

for chord in chords:
    # Assumes 3 notes in chord
    MIDIGen.addChord(chord[0],chord[1],chord[2])

MIDIGen.writeMidiToFile()