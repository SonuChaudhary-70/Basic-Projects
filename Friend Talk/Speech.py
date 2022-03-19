
import speech_recognition as sr

r_a = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything")
    audio = r_a.listen(source)
    
    # try:
    #     text = r_a.recognize_google(audio)
    #     print(f"You said :{text}")
    # except:
    #     print("sorry speak again")
    

text = r_a.recognize_google(audio)
print(f"You said :{text}")