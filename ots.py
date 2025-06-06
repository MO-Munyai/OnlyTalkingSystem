import pyttsx3
import speech_recognition as sr
Ottis = pyttsx3.init()
r = sr.Recognizer()

Ottis.say("I am Ottis. AI by Orange.")
Ottis.say("Ask your crush about me. Catch up")
Ottis.runAndWait()

def record_text():
    
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                audio2 = r.listen(source2)
                
                MyText = r.recognize_google(audio2)
                
                return MyText
            
        except sr.RequestError as e:
            print("Could not request results: {0}",format(e))
        
        except sr.UnknownValueError:
            print("unknown error occurred") 
    return

def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = record_text()
    output_text(text)
    
    print("Written")