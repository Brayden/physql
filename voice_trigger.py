import pyaudio
import speech_recognition as sr

def extract_instruction(transcription, trigger_word):
    """Extract the instruction part from the transcription."""
    trigger_word_position = transcription.lower().find(trigger_word)
    if trigger_word_position != -1:
        return transcription[trigger_word_position + len(trigger_word):].strip()
    return None

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    trigger_word = "hello world"

    print(f"Listening for trigger word '{trigger_word}'...")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print("Say something!")
            audio = recognizer.listen(source)

            try:
                transcription = recognizer.recognize_google(audio)
                print(f"You said: {transcription}")

                if trigger_word in transcription.lower():
                    print(f"Trigger word '{trigger_word}' detected!")
                    instruction = extract_instruction(transcription, trigger_word)
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

# def listen_for_instruction(recognizer, source):
#     """Listen for the next spoken instruction after the trigger phrase."""
#     print("Listening for instruction...")
#     recognizer.adjust_for_ambient_noise(source)
#     audio = recognizer.listen(source)

#     try:
#         instruction = recognizer.recognize_google(audio)
#         print(f"Instruction: {instruction}")
#         return instruction
#     except sr.UnknownValueError:
#         print("Could not understand audio")
#         return None
#     except sr.RequestError as e:
#         print(f"Could not request results; {e}")
#         return None

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
#                     instruction = listen_for_instruction(recognizer, source)
#                     if instruction:
#                         print(f"Received instruction: {instruction}")
#                     else:
#                         print("No instruction received.")

#             except sr.UnknownValueError:
#                 print("Could not understand audio")
#             except sr.RequestError as e:
#                 print(f"Could not request results; {e}")

# if __name__ == "__main__":
#     main()



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
