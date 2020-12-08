# Import libraries
import speech_recognition as sr 
import moviepy.editor as mp

# Video to Audio Conversion
clip = mp.VideoFileClip(r”video_recording.mov”) 
 
clip.audio.write_audiofile(r”converted.wav”)

# Speech Recognition - define the recognizer
r = sr.Recognizer()

# import the audio file that was created in the previous step
audio = sr.AudioFile("converted.wav")

# recognizer will try to understand the speech and convert it to a text format
with audio as source:
    audio_file = r.record(source)
result = r.recognize_google(audio_file)

# Exporting the Result - export the recognized speech into a text document
# exporting the result 
with open('recognized.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(result) 
   print("ready!")