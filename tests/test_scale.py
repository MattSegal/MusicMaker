from ..scale import Scale

def test_scale_notes_c_root():
    scale = Scale('C')
    assert scale.notes == ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def test_scale_notes_b_root():
    scale = Scale('B')
    assert scale.notes == ['B','C','C#','D','D#','E','F','F#','G','G#','A','A#']

def test_scale_notes_e_root():
    scale = Scale('E')
    assert scale.notes == ['E','F','F#','G','G#','A','A#','B','C','C#','D','D#']

def test_major_scale():
    scale = Scale('C')
    assert scale.major == ['C','D','E','F','G','A','B']

def test_minor_scale():
    scale = Scale('C')
    assert scale.minor == ['C','D','D#','F','G','G#','A#']