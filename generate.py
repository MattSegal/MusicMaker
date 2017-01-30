from midi_generator import MIDIGenerator
from melody_composer import MelodyComposer


def composeAndWriteToFile(scale,duration,fileName):
    mozart = MelodyComposer()
    testMelody = mozart.compose(scale,duration)

    chords = [
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

    # (note, octave, duration, volume)

    MIDIGen = MIDIGenerator(fileName)
    MIDIGen.addMelody(testMelody)
    for chord in chords:
        MIDIGen.addChord(chord[0],chord[1],chord[2])
    MIDIGen.writeMidiToFile()

composeAndWriteToFile(majorScaleNotes,500,"output.mid")