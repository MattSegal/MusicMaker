from midiutil.MidiFile import MIDIFile

class MIDIGenerator(object):
    """
    By Samhan Salahuddin
    25th November 2016
    """

    def __init__(self,fileName):
        self.outputFileName = fileName

        # Create the MIDIFile Object with 1 track
        self.MIDIObject = MIDIFile(1)
        self.track = 0
        self.MIDIObject.addTrackName(self.track,0,"Sample Track")
        self.MIDIObject.addTempo(self.track,0,420)
        self.volume = 100
        self.channel = 0
        self.notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
        self.basePitchOfC = 50

    def addNote(self,note,time,duration,octave,volume):
        if note != "S":
            self.MIDIObject.addNote(self.track,self.channel,self.notePitch(note,octave),time,duration,volume)        
        else:
            self.MIDIObject.addNote(self.track,self.channel,50,time,duration,0)        


    def addChord(self,notes,time,duration):
        for noteInfo in notes:
            note = noteInfo[0]
            octave = noteInfo[1]
            self.MIDIObject.addNote(self.track,self.channel,self.notePitch(note,octave),time,duration,self.volume)

    def notePitch(self,note,octave):
        return self.notes.index(note) + self.basePitchOfC + (12 * octave)

    def addMelody(self,melody):
        # Times are measured in beats.
        trackTime = 0
        for noteInfo in melody:
            note = noteInfo[0]
            octave = noteInfo[1]
            duration = noteInfo[2]
            volume = noteInfo[3]
            if(note != ''):
                self.addNote(note,trackTime,duration,octave,volume)
            trackTime = trackTime + duration

    def writeMidiToFile(self):
        binfile = open(self.outputFileName, 'wb')
        self.MIDIObject.writeFile(binfile)
        binfile.close()

def composeAndWriteToFile(fileName):

    ascending_c_arp = [
        #Cmaj7
        ('C',2,4,50),
        ('E',2,4,50),
        ('G',2,4,50),
        ('B',2,4,50),
        #Dmin7
        ('D',2,4,50),
        ('F',2,4,50),
        ('A',2,4,50),
        ('C',3,4,50),
        #Cmaj7
        ('C',2,4,50),
        ('E',2,4,50),
        ('G',2,4,50),
        ('B',2,4,50),
        #Dmin7
        ('D',2,4,50),
        ('F',2,4,50),
        ('A',2,4,50),
        ('C',3,4,50),
    ]

    chords = [
        #Cmaj7
        [(('C',1),('E',1),('G',1),('B',1)),0,16],

        #Dmin7
        [(('D',1),('F',1),('A',1),('C',1)),16,16],

        #Cmaj7
        [(('C',1),('E',1),('G',1),('B',1)),32,16],

        #Dmin7
        [(('D',1),('F',1),('A',1),('C',1)),48,16],
    ]

    # (note, octave, duration, volume)
    MIDIGen = MIDIGenerator(fileName)
    MIDIGen.addMelody(ascending_c_arp)

    for chord in chords:
        MIDIGen.addChord(chord[0],chord[1],chord[2])

    MIDIGen.writeMidiToFile()
    
composeAndWriteToFile("output.mid")