import pyaudio
import speech_recognition as sr

def extract_instruction(transcription, trigger_word):
    """Extract the instruction part from the transcription."""
    trigger_word_position = transcription.lower().find(trigger_word)
    if trigger_word_position != -1:
        return transcription[trigger_word_position + len(trigger_word):].strip()
    return None

def handle_audio(recognizer, audio):
    """Handle the audio input and detect trigger word and instructions."""
    trigger_word = "hello world"

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

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Adjust for ambient noise once at the beginning
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

    print("Listening for trigger word 'Hello world'...")

    def callback(recognizer, audio):
        handle_audio(recognizer, audio)

    # Use listen_in_background for non-blocking audio capture
    stop_listening = recognizer.listen_in_background(microphone, callback, phrase_time_limit=5)

    try:
        while True:
            # Keep the main thread alive
            # time.sleep(0.1)
            pass
    except KeyboardInterrupt:
        stop_listening(wait_for_stop=False)
        print("Stopped listening")

if __name__ == "__main__":
    main()


# import pyaudio
# import speech_recognition as sr

# def extract_instruction(transcription, trigger_word):
#     """Extract the instruction part from the transcription."""
#     trigger_word_position = transcription.lower().find(trigger_word)
#     if trigger_word_position != -1:
#         return transcription[trigger_word_position + len(trigger_word):].strip()
#     return None

# def handle_audio(recognizer, audio):
#     """Handle the audio input and detect trigger word and instructions."""
#     trigger_word = "hello world"

#     try:
#         transcription = recognizer.recognize_google(audio)
#         print(f"You said: {transcription}")

#         if trigger_word in transcription.lower():
#             print(f"Trigger word '{trigger_word}' detected!")
#             instruction = extract_instruction(transcription, trigger_word)
#             if instruction:
#                 print(f"Received instruction: {instruction}")
#             else:
#                 print("No instruction received.")
#     except sr.UnknownValueError:
#         print("Could not understand audio")
#     except sr.RequestError as e:
#         print(f"Could not request results; {e}")

# def main():
#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()

#     # Adjust for ambient noise once at the beginning
#     with microphone as source:
#         recognizer.adjust_for_ambient_noise(source)

#     print("Listening for trigger word 'Hello world'...")

#     # Use listen_in_background for non-blocking audio capture
#     stop_listening = recognizer.listen_in_background(microphone, handle_audio)

#     try:
#         while True:
#             # Keep the main thread alive
#             pass
#     except KeyboardInterrupt:
#         stop_listening(wait_for_stop=False)
#         print("Stopped listening")

# if __name__ == "__main__":
#     main()