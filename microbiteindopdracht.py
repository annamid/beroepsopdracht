# Add your Python code here. E.g.
from microbit import *
import music

notes = [
    'B', 'E', 'G', 'F#', 'E', 
    'B', 'A', 'F#', 'E', 'G', 'F#', 'D', 
    'F', 'B', 
    'B', 'E', 'G', 'F#', 'E', 
    'B', 'D', 'C#', 'C', 'A', 'C', 'Bb', 'B', 'G', 
    'E', 
    'G', 'B', 'G', 'B', 
    'G', 'C', 'B', 'Bb', 'F#', 'G', 'B', 'Bb', 'C', 'B', 'B',
    'G', 'B', 'G', 'B',
    'G', 'D', 'C#', 'C', 'A', 'C', 'B', 'Bb', 'B', 'G', 'E',
]

music.play(notes)
