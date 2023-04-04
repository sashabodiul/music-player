from os import path
from pydub import AudioSegment

# files                                                                         
src = "muz.mp3"
dst = "test.ogg"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="ogg")