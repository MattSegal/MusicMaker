from midiutil.MidiFile import MIDIFile

class MIDIGenerator(object):
    """
    By Samhan Salahuddin
    25th November 2016
    """

    def __init__(self,fileName):
        self.outputFileName = fileName
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

    dummy_melody = [
        ('C',2,4,50),
        ('D',2,4,50),
        ('E',2,4,50),
        ('F',2,4,50),
        ('G',2,4,50),
        ('A',2,4,50),
        ('B',2,4,50),
        ('C',3,4,50),
    ]
    # (note, octave, duration, volume)
    MIDIGen = MIDIGenerator(fileName)
    MIDIGen.addMelody(dummy_melody)
    MIDIGen.writeMidiToFile()
    
composeAndWriteToFile("output.mid")