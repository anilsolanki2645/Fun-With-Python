""" Text To Speach Using Python """

import pyttsx3

def change_voice(engine, voice_id):
    # Get the available voices
    voices = engine.getProperty('voices')

    # Set the desired voice based on the given voice_id
    for voice in voices:
        if voice.id == voice_id:
            engine.setProperty('voice', voice.id)
            return True
    
    # If the specified voice_id is not found, return False
    return False

def text_to_speech(text, voice_id=None):
    engine = pyttsx3.init()

    # Change the voice if a voice_id is provided
    if voice_id:
        if not change_voice(engine, voice_id):
            print(f"Voice with ID '{voice_id}' not found.")
            return

    engine.say(text)
    engine.runAndWait()

def main():
    text = input("Enter the text you want to hear: ")
    voice_id = input("Enter the voice ID (leave empty for default): ")

    text_to_speech(text, voice_id)

if __name__ == "__main__":
    main()
