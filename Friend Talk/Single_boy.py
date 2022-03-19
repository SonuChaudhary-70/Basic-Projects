
import pyttsx3 as P

friend = P.init()
voices = friend.getProperty('voices') 
friend.setProperty('voice', voices[1].id)
friend.setProperty('rate',130)
spech = input("Enter Your Name: ")
friend.say(f"hey {spech} सच में यार तुम्हे बहुत मिस कर रही हु ")
friend.say("तुम मुज से मिलने कब आ रहे हो ")
friend.runAndWait() 
