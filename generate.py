from midi_generator import MIDIGenerator
from melody_composer import MelodyComposer
from chord_composer import ChordComposer
from scale import Scale

output_file_name = "output.mid"
duration_beats = 1024
scale = Scale('C').major

test_melody = MelodyComposer().compose(scale,duration_beats)
chords = ChordComposer(scale).get_random_chords(duration_beats)

MIDIGen = MIDIGenerator(output_file_name)

MIDIGen.add_melody(test_melody)

for chord in chords:
    # Assumes 3 notes in chord
    MIDIGen.add_chord(chord.notes,chord.time,chord.beats)

MIDIGen.write_midi_to_file()