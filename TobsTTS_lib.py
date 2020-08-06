# TobsTTS_lib
# © 2020 Temerold
import os
import sys
clear = lambda: os.system('cls')


def install(fast = False):
    x = 0
    if fast == False:
        while x == 0:
            try:
                os.system('pip install gtts')
                os.system('pip install playsound')
                x = 1
            except:
                try:
                    os.sytem("py -m pip install gtts")
                    os.sytem("py -m pip install playsound")
                    x = 1
                except OSError as e:
                    y = 0
                    while y == 0:
                        print(e)
                        ign = input("\nKunde inte installera 3rd party moduler. Vill du försöka igen? (y/n):\n")
                        if ign == "n":
                            sys.exit()
                        elif ign != "y" and ign != "n":
                             print("Svara endast med \"y\" eller \"n\".")
                        else:
                            pass
                        
    elif fast == True:
        try:
            os.system('pip install gtts')
            os.system('pip install playsound')
        except:
            try:
                os.sytem("py -m pip install gtts")
                os.sytem("py -m pip install playsound")
            except:
                pass

    clear()

    
try:
    from gtts import gTTS
    from playsound import playsound
except ImportError as e:
    print(e)
    input("\nKunde inte importera 3rd party moduler.")
    sys.exit()


def tts(msg, language, fil = "Tob's TTS no_name.mp3"):
    try:
        obj = gTTS(text = msg, lang = language, slow = False)
        obj.save(filnamn)
    
    except:
        y = 0
        while y == 0:
            ign = input("Kunde inte spara fil \"" + fil + ".mp3" + "\". Vill du försöka igen? (y/n):\n")
            if ign == "n":
                sys.exit()
            elif ign != "y" and ign != "n":
                print("\nSvara endast med \"y\" eller \"n\".")
            else:
                pass


def say(fil):
    try:
        playsound(fil)
    except Exception as e:
        print(e)
        print("Kunde inte spela upp fil.")
