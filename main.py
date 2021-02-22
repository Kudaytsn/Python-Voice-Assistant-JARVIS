import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
while True:

    listener = sr.Recognizer()
    engine = pyttsx3.init()
    with sr.Microphone() as source:
            voice = listener.listen(source)
            def talk(text):
                engine.say(text)
                engine.runAndWait()


            def run_jarvis():
                def take_order():
                    command = str('')
                    try:
                        command = str(listener.recognize_google(voice, language='en-IN'))
                        command = command.lower()

                    except:
                        pass
                    return command



                responce  = take_order()
                if 'jarvis' in responce:
                    print('Listening...')
                    print(responce)
                    responce = responce.replace('jarvis', '')
                    if 'hello' in responce:
                        talk('Hello CouldI I am your virtual assistant Jarvis. How can I help you?')                                       
                    elif 'play' in responce :
                        responce = responce.replace('play', '')
                        talk('playing'+str(responce))
                        pywhatkit.playonyt(responce)
                        print('playing'+str(responce))
                    elif 'search ' in responce:
                        responce = responce.replace('search', '')
                        responce = responce.replace('on', '')
                        responce = responce.replace('google', '')
                        talk('searching' + str(responce)+'on google')
                        print('searching' + str(responce)+'on google')
                        pywhatkit.search(responce)
                    elif 'time' in responce:
                        time = datetime.datetime.now().strftime('%H:%M')
                        talk('Current time is ' +time)

                    elif ('who is' in responce):
                            info = responce.replace('who is', '')
                            try:
                                result = wikipedia.summary(info, 3)
                                print(result)
                                talk(result)
                            except:
                                talk('No Vikipedia articles found about that particular topic')
                                pass
                    elif('what is' in responce):
                        info = responce.replace('what is', '')
                        result=wikipedia.summary(info, 3)
                        print(result)
                        talk(result)
                    elif 'here' in responce:
                        talk('Yes I am here waiting for your orders')
                    elif 'thank you' in responce:
                        talk('You are welcome. I am always here to help')
                    elif 'there' in responce:
                        talk('Yes I am here waiting for your orders')
                    else:
                        talk('I couldnt understand your order. Repeat please')

            run_jarvis()
