import pyttsx3
from pyttsx3.voice import Voice

text = '好的，为您打开左车窗全部'
output_file = "output.wav"

engine = pyttsx3.init()
engine.setProperty('rate', 150) 
engine.setProperty('voice', 'zh')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[12].id)
engine.save_to_file(text, output_file)
engine.runAndWait()
