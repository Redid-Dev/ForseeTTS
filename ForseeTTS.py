from gtts import gTTS


#███████╗░█████╗░██████╗░░██████╗███████╗███████╗████████╗████████╗░██████╗               ForseeTTS
#██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝               Developed by: ForseeGab
#█████╗░░██║░░██║██████╔╝╚█████╗░█████╗░░█████╗░░░░░██║░░░░░░██║░░░╚█████╗░               What is?:Free & open source TTS service 
#██╔══╝░░██║░░██║██╔══██╗░╚═══██╗██╔══╝░░██╔══╝░░░░░██║░░░░░░██║░░░░╚═══██╗
#██║░░░░░╚█████╔╝██║░░██║██████╔╝███████╗███████╗░░░██║░░░░░░██║░░░██████╔╝
#╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═════╝░


from playsound import playsound

audio ='speech.mp3'
language = 'it'
sp = gTTS(text = "YOOOO BOZO", lang= language,slow=False)

sp.save(audio)
playsound(audio)