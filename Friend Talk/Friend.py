import pyttsx3 as P

friend = P.init()
voices = friend.getProperty('voices') 
friend.setProperty('voice', voices[1].id)
friend.setProperty('rate',140)
# spech = input("Enter Your Name: ")
friend.say('''दिल को ज़ुबान,
आँखों को सपने मिल गये…
आशिक़ी में, ज़िंदगी को मायने मिल गये !
''')
friend.say('''तेरी आवाज़ पर मरते हैं,
तेरे हर अंदाज़ पर मरते हैं,
तुझे बताया नहीं कभी लेकिन
एक तरफा इश्क़ तुमसे करते हैं।''')
# friend.say(spech)
friend.runAndWait() 
