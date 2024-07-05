import pyaudio
import speech_recognition as sr

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Listening for trigger word 'Hello world'...")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print("Say something!")
            audio = recognizer.listen(source)

            try:
                transcription = recognizer.recognize_google(audio)
                print(f"You said: {transcription}")

                if "hello world" in transcription.lower():
                    print("Trigger word 'Hello world' detected!")
                    # Add any additional actions you want to take here

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

if __name__ == "__main__":
    main()
