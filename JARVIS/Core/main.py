import speech_recognition as sr

def recognize_voice(sr):
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, didn't catch that.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None
        
if __name__ == "__main__":
    while True:
        command = recognize_voice(sr)