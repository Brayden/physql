import pyaudio
import speech_recognition as sr

def listen_for_instruction(recognizer, source):
    """Listen for the next spoken instruction after the trigger phrase."""
    print("Listening for instruction...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

    try:
        instruction = recognizer.recognize_google(audio)
        print(f"Instruction: {instruction}")
        return instruction
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

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
                    instruction = listen_for_instruction(recognizer, source)
                    if instruction:
                        print(f"Received instruction: {instruction}")
                    else:
                        print("No instruction received.")

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

if __name__ == "__main__":
    main()



# import pyaudio
# import speech_recognition as sr

# def main():
#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()

#     print("Listening for trigger word 'Hello world'...")

#     with microphone as source:
#         recognizer.adjust_for_ambient_noise(source)
#         while True:
#             print("Say something!")
#             audio = recognizer.listen(source)

#             try:
#                 transcription = recognizer.recognize_google(audio)
#                 print(f"You said: {transcription}")

#                 if "hello world" in transcription.lower():
#                     print("Trigger word 'Hello world' detected!")
#                     # Add any additional actions you want to take here

#             except sr.UnknownValueError:
#                 print("Could not understand audio")
#             except sr.RequestError as e:
#                 print(f"Could not request results; {e}")

# if __name__ == "__main__":
#     main()
