import smtplib
import subprocess
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import imdb
import pyjokes
import wolframalpha as wolframalpha
import pyautogui
import time
from time import sleep
from PyDictionary import PyDictionary

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    print("RP: ", audio)
    engine.say(audio)
    engine.runAndWait()


def wishuser():
    hour = int(datetime.datetime.now().hour)
    if 6 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir")
    elif 18 <= hour < 23:
        speak("Good Evening Sir")
    elif hour >= 23 or hour < 4:
        speak("It Seems You Haven't Slept Yet Sir")
    elif 4 <= hour < 6:
        speak("You woke up early sir")
    speak("How Can I Assist You")


def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(mymailid, myidpassword)
    server.sendmail(mymailid, to, content)
    server.close()


mymailid = ""
myidpassword = ""


def getcommand():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(mic, duration=1)
        useraudio = r.listen(mic)
    try:
        print("RP: Please Wait")
        command = r.recognize_google(useraudio, language='en-in')
        print("You: ", command)
        return command

    except Exception:
        command = "quit"
        return command


errortime = int(0)


def errorreply(errortime=errortime):
    speak("Sir Can u plese try again")
    errortime += 1

def checkword(words, query):



if __name__ == "__main__":
    wishuser()
    while True:
        query = getcommand().lower()
        if "wake up" in query:
            speak("Yes sir ")
            while True:
                if errortime <= 10:
                    query = getcommand().lower()
                    if "wikipedia" in query:
                        try:
                            speak("searching please wait")
                            query = query.replace("wikipedia", "")
                            result = wikipedia.summary(query, sentences=5)
                            speak("According To Wikipedia")
                            speak(result)
                        except:
                            errorreply()

                    elif "play my movies" in query:
                        try:
                            moviesdir = "C:\\Users\\allpo\\Downloads\\Telegram Desktop"
                            movie = os.listdir(moviesdir)
                            print(movie)
                            os.startfile(os.path.join(moviesdir, movie[1]))
                        except:
                            speak("There are No Movies")

                    elif "movie" in query:
                        try:
                            query = query.replace("movie", "")
                            moviesdb = imdb.IMDb()
                            movies = moviesdb.search_movie(query)
                            a = 0
                            ml = []
                            for movie in movies:
                                if a <= 5:
                                    try:
                                        title = movie['title']
                                        year = movie['year']
                                        res = a, f'{title} - {year}'
                                        ttl = f'{title}'
                                        ml += [ttl]
                                        speak(res)
                                        a += 1
                                    except KeyError:
                                        title = movie['title']
                                        res = a, f'{title}'
                                        ttl = f'{title}'
                                        ml += [ttl]
                                        speak(res)
                                        a += 1
                            speak("Select the respective number of the movie you need Example 0 for first one ")
                            try:
                                mno = int(getcommand())
                                mid = movies[mno].getID()
                                movie = moviesdb.get_movie(mid)

                                print("Movie Info")
                                try:
                                    title = movie['title']
                                    year = movie['year']
                                    speak(f'{title} - {year}')
                                except KeyError:
                                    title = movie['title']
                                    speak(f'{title}')

                                try:
                                    rating = movie['rating']
                                    speak(f'rating: {rating}')
                                except KeyError:
                                    pass

                                try:
                                    director = movie['director']
                                    directors = ', '.join(map(str, director))
                                    speak(f'directed by {directors}')
                                except KeyError:
                                    pass

                                try:
                                    plot = movie['plot']
                                    speak(f'movie plot: {plot}')
                                except KeyError:
                                    pass

                                try:
                                    casting = movie['cast']
                                    actors = ', '.join(map(str, casting))
                                    speak("Casts are mentioned below")
                                    print(f"actors: {actors}")
                                except KeyError:
                                    pass
                            except IndexError:
                                errorreply()
                        except:
                            errorreply()

                    elif "youtube" in query:
                        if "open youtube" in query:
                            webbrowser.open("https://www.youtube.com")
                        elif "search for" in query:
                            search1 = query.replace("search for", "")
                            search = search1.replace(" in youtube", "")
                            webbrowser.open("https://www.youtube.com")
                            time.sleep(2)
                            pyautogui.click(x=622, y=123)
                            time.sleep(1)
                            pyautogui.write(search)
                            time.sleep(1)
                            pyautogui.press("Enter")
                        elif "search" in query:
                            search1 = query.replace("search", "")
                            search = search1.replace(" in youtube", "")
                            webbrowser.open("https://www.youtube.com")
                            time.sleep(2)
                            pyautogui.click(x=622, y=123)
                            time.sleep(1)
                            pyautogui.write(search)
                            time.sleep(1)
                            pyautogui.press("Enter")

                    elif "meaning" in query:
                        if "what is the meaning of the word" in query:
                            query = query.replace("what is the meaning of the word ", "")
                            word = PyDictionary.meaning(query)
                            for state in word:
                                meaning = word[state]
                            speak(meaning)
                        elif "what is the meaning of" in query:
                            query = query.replace("what is the meaning of ", "")
                            word = PyDictionary.meaning(query)
                            for state in word:
                                meaning = word[state]
                            speak(meaning)
                        elif "meaning of the word" in query:
                            query = query.replace("meaning of the word ", "")
                            word = PyDictionary.meaning(query)
                            for state in word:
                                meaning = word[state]
                            speak(meaning)
                        elif "meaning of" in query:
                            query = query.replace("meaning of ", "")
                            word = PyDictionary.meaning(query)
                            for state in word:
                                meaning = word[state]
                            speak(meaning)
                        else:
                            speak("Please use sentences like : what is the meaning of the word or what is the meaning "
                                  "of or meaning of the word or meaning of")

                    elif "google" in query:
                        if "open google" in query:
                            webbrowser.open("https://www.google.com")
                        elif "search for" in query:
                            search1 = query.replace("search for", "")
                            search = search1.replace(" in google", "")
                            webbrowser.open("https://www.google.com")
                            time.sleep(2)
                            pyautogui.click(x=813, y=482)
                            time.sleep(1)
                            pyautogui.write(search)
                            time.sleep(1)
                            pyautogui.press("Enter")
                        elif "search" in query:
                            search1 = query.replace("search", "")
                            search = search1.replace(" in google", "")
                            webbrowser.open("https://www.google.com")
                            time.sleep(2)
                            pyautogui.click(x=813, y=482)
                            time.sleep(1)
                            pyautogui.write(search)
                            time.sleep(1)
                            pyautogui.press("Enter")

                    elif "hotstar" in query:
                        if "open hotstar" in query:
                            webbrowser.open("https://www.hotstar.com/in")
                        elif "search for" in query:
                            search1 = query.replace("search for", "")
                            search = search1.replace(" in hotstar", "")
                            webbrowser.open("https://www.hotstar.com/in")
                            time.sleep(2)
                            pyautogui.click(x=1574, y=135)
                            time.sleep(1)
                            pyautogui.write(search)
                            time.sleep(1)
                            pyautogui.press("Enter")
                        elif "search" in query:
                            search1 = query.replace("search", "")
                            search = search1.replace(" in hotstar", "")
                            webbrowser.open("https://www.hotstar.com/in")
                            time.sleep(2)
                            pyautogui.click(x=1574, y=135)
                            time.sleep(1)
                            pyautogui.write(search)
                            time.sleep(1)
                            pyautogui.press("Enter")
                        elif "play" in query:
                            if "play what i was watching" in query:
                                webbrowser.open("https://www.hotstar.com/in")
                                time.sleep(3)
                                pyautogui.moveTo(x=204, y=842)
                                time.sleep(1)
                                pyautogui.click(x=204, y=842)
                            elif "play" in query:
                                search1 = query.replace("play", "")
                                search = search1.replace(" in hotstar", "")
                                webbrowser.open("https://www.hotstar.com/in")
                                time.sleep(2)
                                pyautogui.click(x=1574, y=135)
                                time.sleep(1)
                                pyautogui.write(search)
                                time.sleep(1)
                                pyautogui.click(x=1512, y=218)
                                time.sleep(1)
                                pyautogui.click(x=227, y=581)

                    elif "open classroom" in query:
                        webbrowser.open("https://classroom.google.com/h")

                    elif "open pycharm" in query:
                        pycharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.3\\bin\\pycharm64.exe"
                        os.startfile(pycharm)

                    elif "open cyberpunk" in query:
                        cyberpunk = "C:\\Program Files (x86)\\Cyberpunk 2077\\bin\\x64\\Cyberpunk2077.exe"
                        os.startfile(cyberpunk)

                    elif "open excel" in query:
                        excel = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                        os.startfile(excel)

                    elif "open word" in query:
                        word = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                        os.startfile(word)

                    elif "open powerpoint" in query:
                        ppt = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                        os.startfile(ppt)

                    elif "open notepad" in query:
                        word = "C:\\Windows\\System32\\notepad.exe"
                        os.startfile(word)

                    elif "open calculator" in query:
                        calc = "C:\\Windows\\System32\\calc.exe"
                        os.startfile(calc)

                    elif "open idle" in query:
                        idle = "C:\\Users\\allpo\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib\\idle.pyw"
                        os.startfile(idle)

                    elif "open Epic" in query:
                        epic = "C:\\Program Files (x86)\\EpicGames\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe "
                        os.startfile(epic)

                    elif "whatsapp" in query:
                        #This is a own made automation to send message with the use of whatsapp desktop
                        #There is also another pre defined automation to use (pywhatkit) to access through whatsapp web
                        wtsap = "C:\\Users\\allpo\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                        os.startfile(wtsap)
                        while True:
                            t = 0
                            if t == 0:
                                speak("should i send any message to anyone")
                                query = getcommand().lower()
                                # Send "Message" to "Person"
                                if "send" in query and "to" in query:
                                    reciever = query.split(" ")[-1]
                                    message = query.split(' ', 1)[1]
                                    message = message.rsplit(' ', 2)[0]
                                    sleep(2)
                                    pyautogui.click(x=230, y=140)
                                    sleep(1)
                                    pyautogui.write(reciever)
                                    sleep(2)
                                    pyautogui.press("Enter")
                                    sleep(1)
                                    pyautogui.write(message)
                                    sleep(1)
                                    pyautogui.press("Enter")
                                elif "exit" or "nothing" in query:
                                    exit()
                                else:
                                    break
                                t = 1

                            elif t == 1:
                                speak("should i send any message to anyone")
                                query = getcommand().lower()
                                if "send" in query and "to" in query:
                                    sleep(2)
                                    pyautogui.click(x=530, y=140)
                                    reciever = query.split(" ")[-1]
                                    message = query.split(' ', 1)[1]
                                    message = message.rsplit(' ', 2)[0]
                                    sleep(2)
                                    pyautogui.click(x=230, y=140)
                                    sleep(1)
                                    pyautogui.write(reciever)
                                    sleep(2)
                                    pyautogui.press("Enter")
                                    sleep(1)
                                    pyautogui.write(message)
                                    sleep(1)
                                    pyautogui.press("Enter")
                                elif "exit" or "nothing" in query:
                                    exit()
                                else:
                                    break

                    elif "open telegram" in query:
                        telegram = "C:\\Users\\allpo\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
                        os.startfile(telegram)

                    elif "open notepad" in query:
                        notepad = "%windir%\\system32\\notepad.exe"
                        os.startfile(notepad)

                    elif "open onenote" in query:
                        onenote = "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
                        os.startfile(onenote)

                    elif "amazon prime" in query:
                        if "open amazon prime" in query:
                            primevideo = 'start explorer shell:appsfolder\\AmazonVideo.PrimeVideo_pwbj9vvecjh7j!App'
                            os.system(primevideo)
                        elif "search for" in query:
                            search1 = query.replace("search for", "")
                            search = search1.replace(" in amazon prime", "")
                            primevideo = 'start explorer shell:appsfolder\\AmazonVideo.PrimeVideo_pwbj9vvecjh7j!App'
                            os.system(primevideo)
                            time.sleep(5)
                            pyautogui.click(x=136, y=182)
                            time.sleep(1)
                            pyautogui.write(search)
                            time.sleep(2)
                            pyautogui.press("Enter")
                            time.sleep(5)
                            pyautogui.click(x=580, y=265)
                            time.sleep(3)
                            pyautogui.click(x=551, y=548)
                            pyautogui.press("Enter")
                        elif "search" in query:
                            search1 = query.replace("search for", "")
                            search = search1.replace(" in amazon prime", "")
                            primevideo = 'start explorer shell:appsfolder\\AmazonVideo.PrimeVideo_pwbj9vvecjh7j!App'
                            os.system(primevideo)
                            time.sleep(5)
                            pyautogui.click(x=136, y=182)
                            time.sleep(1)
                            pyautogui.write(search)
                            time.sleep(2)
                            pyautogui.press("Enter")
                        elif "play" in query:
                            if "play what i was watching" in query:
                                primevideo = 'start explorer shell:appsfolder\\AmazonVideo.PrimeVideo_pwbj9vvecjh7j!App'
                                os.system(primevideo)
                                time.sleep(6)
                                pyautogui.click(x=600, y=485)
                                time.sleep(6)
                                pyautogui.click(x=551, y=548)
                            elif "play" in query:
                                search1 = query.replace("search for", "")
                                search = search1.replace(" in amazon prime", "")
                                primevideo = 'start explorer shell:appsfolder\\AmazonVideo.PrimeVideo_pwbj9vvecjh7j!App'
                                os.system(primevideo)
                                time.sleep(5)
                                pyautogui.click(x=136, y=182)
                                time.sleep(1)
                                pyautogui.write(search)
                                time.sleep(2)
                                pyautogui.press("Enter")
                                time.sleep(5)
                                pyautogui.click(x=580, y=265)
                                time.sleep(3)
                                pyautogui.click(x=551, y=548)
                                pyautogui.press("Enter")

                    elif "open amazon music" in query:
                        primemusic = 'start explorer shell:appsfolder\\AmazonMobileLLC.AmazonMusic_kc6t79cpj4tp0' \
                                     '!AmazonMobileLLC.AmazonMusic '
                        os.system(primemusic)

                    elif "open camera" in query:
                        camera = 'start explorer shell:appsfolder\\Microsoft.WindowsCamera_8wekyb3d8bbwe!App'
                        os.system(camera)

                    elif "open clock" in query:
                        clock = 'start explorer shell:appsfolder\\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App'
                        os.system(clock)

                    elif "open setting" in query:
                        setting = "start explorer shell:appsfolder\\windows.immersivecontrolpanel_cw5n1h2txyewy" \
                                  "!microsoft.windows.immersivecontrolpanel "
                        os.system(setting)

                    elif "the time" in query:
                        time = datetime.datetime.now().strftime("%H:%M")
                        speak(time)

                    elif 'joke' in query:
                        speak(pyjokes.get_joke())

                    elif "where is" in query:
                        query = query.replace("where is", "")
                        location = query
                        speak("User asked to Locate")
                        speak(location)
                        webbrowser.open("https://www.google.nl / maps / place/" + location + "")

                    elif 'send mail' in query:
                        try:
                            if mymailid == "" or myidpassword == "":
                                if mymailid == "" and myidpassword == "":
                                    mymailid = input(speak("Enter Your Mail Id sir"))
                                    myidpassword = input(speak("Enter your Password sir"))
                                    speak("Your mail id and password updated sir")
                                elif mymailid == "" and myidpassword != "":
                                    mymailid = input(speak("Enter Your Mail Id sir"))
                                    speak("Your mail id updated sir")
                                elif mymailid != "" and myidpassword == "":
                                    myidpassword = input(speak("Enter your Password sir"))
                                    speak("Your password updated sir")

                            speak("What should I say in it sir ?")
                            content = getcommand()
                            speak("whome should i send it to sir ")
                            to = input(speak("Enter Recievers Address Sir"))
                            sendmail(to, content)
                            speak("Email has been sent !")
                        except Exception as e:
                            print(e)
                            speak("I am not able to send this email")

                    elif 'search' in query or 'play' in query:
                        query = query.replace("search", "")
                        query = query.replace("play", "")
                        webbrowser.open(query)

                    elif "what is" in query or "who is" in query:
                        client = wolframalpha.Client("X2UK38-4EH42KXHV7")
                        res = client.query(query)
                        try:
                            print(next(res.results).text)
                            speak(next(res.results).text)
                        except StopIteration:
                            print("No results")

                    elif "jarvis" in query or "alexa" in query or "bixby" in query or "siri" in query:
                        speak("How Dare You Compare Me with That pest")

                    elif "restart" in query:
                        subprocess.call(["shutdown", "/r"])

                    elif 'shutdown system' in query:
                        speak("Hold On a Sec ! Your system is on its way to shut down")
                        subprocess.call('shutdown / p /f')

                    elif 'quit' in query:
                        speak("i will wait sir")
                        break

                    elif 'exit' in query:
                        speak("I will leave sir")
                        exit()

                    else:
                        errorreply()

        elif 'exit' in query:
            speak("I will leave sir")
            speak("Thank You")
            exit()
