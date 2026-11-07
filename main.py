import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib

r = sr.Recognizer()

def speak(text):
    # print(f'Jarvis: {text}')
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def processCommand(command):
    print(command)
    if 'open youtube' in command.lower():
        webbrowser.open('youtube.com')
    elif 'open google' in command.lower():
        webbrowser.open('google.com')
    elif command.lower().startswith('play'):
        song = command.lower().split(' ')[1]
        link = musicLib.music[song]
        webbrowser.open(link)
        
    
if __name__ == '__main__':
    speak('Activating jarvis..')
    while True:
        # r = sr.Recognizer()
        print('Recognizing...')

        try:
            with sr.Microphone() as source:
                print('Listening: ')
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print(word)
            if'jarvis' in word.lower():
                print('👊👊👊matched')
                speak("Yes boss")
                print('Listening for command.....')
                
                with sr.Microphone() as source:
                    print('Jarvis is Listening: ')
                    audio = r.listen(source, timeout=5, phrase_time_limit=2)
                    command = r.recognize_google(audio)
                    print(command)
                    processCommand(command)
                
            
        except Exception as e:
            print(f'Jarvis Error: {e}')