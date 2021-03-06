# By Samhan Salahuddin
# 25th November 2016

from midiutil.MidiFile import MIDIFile

class MIDIGenerator(object):

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

    def add_note(self,note,time,duration,octave,volume):
        if note != "S":
            self.MIDIObject.addNote(self.track,self.channel,self.note_pitch(note,octave),time,duration,volume)        
        else:
            self.MIDIObject.addNote(self.track,self.channel,50,time,duration,0)        


    def add_chord(self,notes,time,duration):
        for noteInfo in notes:
            note = noteInfo[0]
            octave = noteInfo[1]
            self.MIDIObject.addNote(self.track,self.channel,self.note_pitch(note,octave),time,duration,30)

    def note_pitch(self,note,octave):
        return self.notes.index(note) + self.basePitchOfC + (12 * octave)

    def add_melody(self,melody):
        trackTime = 0
        for noteInfo in melody:
            note = noteInfo[0]
            octave = noteInfo[1]
            duration = noteInfo[2]
            volume = noteInfo[3]
            if(note != ''):
                self.add_note(note,trackTime,duration,octave,volume)
            trackTime = trackTime + duration

    def write_midi_to_file(self):
        binfile = open(self.outputFileName, 'wb')
        self.MIDIObject.writeFile(binfile)
        binfile.close()
