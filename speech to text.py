import speech_recognition as sr

# Specify the filename of your audio file
filename = "createAudio.wav"

# Initialize the recognizer
r = sr.Recognizer()

# Use the audio file as the source
with sr.AudioFile(filename) as source:  # Use 'filename' instead of 'create'
    audio_data = r.record(source)  # Read the entire audio file
    try:
        # Recognize speech using Google Web Speech API
        text = r.recognize_google(audio_data)
        print("Transcribed Text:", text)  # Print the transcribed text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
