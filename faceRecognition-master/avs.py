import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import random
import os
import cv2
import smtplib
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
initial = time.time()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'angelina' in command:
                command = command.replace('angelina', '')
    except:
        pass
    return command

def sendEmail(to, contents):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vinay786sing@gmail.com', 'Vinay@123')
    server.sendmail('vinay786sing@gmail.com', to, contents)
    server.close()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("good morning sir , i am virtual assistent angelina . How can i help you")
        talk("good morning sir , i am virtual assistent angelina . How can i help you")
    elif hour >= 12 and hour < 18:
        print("good afternoon sir , i am virtual assistent angelina . How can i help you")
        talk("good afternoon sir , i am virtual assistent angelina . How can i help you")

    elif hour >= 18 and hour < 21:
        print("good evining sir , i am virtual assistent angelina . How can i help you")
        talk("good evening sir , i  am virtual assistent angelina . How can i help you")
    else:
        talk("good night sir , i  am virtual assistent angelina . How can i help you")

def final_time_to_execute():
    final = time.time()
    print("\n Happy to Help you for ", final-initial, "sec")
    talk("Happy To help You Sir")

def takecomm():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising.")
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        talk("error...")
        print("Network connection error")
        return "none"
    return text


def open_application(input):
    if "chrome" in input:
        talk("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return

    elif "internet" in input or "explorer" in input:
        talk("Opening Internet explorer")
        os.startfile('C:\Program Files (x86)\Internet Explorer\iexplore.exe')
        return

    elif "word" in input:                  #
        talk("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return

    elif "excel" in input:                  #
        talk("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return
    elif "computer calculator" in input:
        talk("Opening Computer calculator")
        os.startfile('C:\Windows\System32\calc.exe')
        return
    else:
        talk("Application not  found . Sorry ")
        return

def run_angelina():
    engine.setProperty('rate', 125)
    command = take_command()
    print("Your command :" + command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'happy new year' in command:
        talk(" Ok Sir ")
        webbrowser.open("https://www.tentaran.com/wp-content/uploads/2020/12/happy-new-year-2021-images1.jpg")
        talk(" Happy New Year to everyone Guys ")
        talk(" This is For You ")
        talk(" May the coming year be the most fruitful year of our lives. ")
    elif "how long " in command:
        print("you are using me since",initial,"sec")
        talk("you are using me since")
    elif "hello" in command:
        print("Hello Sir ")
        talk("Hello Sir")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif "are you feeling" in command:
        print("feeling Very sweet after meeting with you")
        talk("feeling Very sweet after meeting with you")
    elif 'date' in command:
        today = datetime.date.today()
        print("Current date  is", today)
        talk("Current date  is")
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command or 'jokes'in command:
        s = pyjokes.get_joke()
        print(s)
        talk(s)
    elif 'open facebook' in command:
        webbrowser.open("https://www.facebook.com")
        talk("opening facebook")
    elif 'open instagram' in command:
        webbrowser.open("https://www.instagram.com")
        talk("opening instagram")
    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        talk("opening google")
    elif 'open yahoo' in command:
        webbrowser.open("https://www.yahoo.com")
        talk("opening yahoo")
    elif 'open gmail' in command:
        webbrowser.open("https://mail.google.com")
        talk("opening google mail")
    elif 'video from pc' in command:
        talk("ok i am playing videos")
        video_dir = './video'
        videos = os.listdir(video_dir)
        os.startfile(os.path.join(video_dir, videos[0]))
    elif "shutdown" in command:
        talk("shutting down")
        os.system('shutdown -s')
    elif "what\'s up" in command or 'how are you' in command:
        stMsgs = ['Just doing my thing What about You!', 'I am fine!What about You', 'Nice!What about You', 'I am nice and full of energy,What about You?',
                  'i am okey, What about You?']
        ans_q = random.choice(stMsgs)
        talk(ans_q)
        ans_take_from_user_how_are_you = takecomm()
        if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
            talk('okey..')
        elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
            talk('oh sorry..')
    elif 'make you' in command or 'created you' in command or 'develop you' in command:
        ans_m = " For your information AVS Tech Created me ! I give Lot of Thanks to Him "
        print(ans_m)
        talk(ans_m)
    elif 'who are you' in command:
        ans_m = " For your information , I am virtual assistant angelina. I can do so many works . Thank you "
        print(ans_m)
        talk(ans_m)
    elif 'search in wikipedia' in command:
        temp = command.replace('search in wikipedia', '+')
        print(wikipedia.summary(temp, sentences=3))

    elif 'search in google' in command :
        temp = command.replace('search in google', '+')
        g_url = "https://www.google.com/search?q="
        res_g = "sorry! i don't have this project but i search from internet to give your answer ! okay"
        print(res_g)
        talk(res_g)
        webbrowser.open(g_url + temp)
    elif 'open application' in command:
        # another function to open
        # different application availaible
        open_application(command.lower())
        return
    elif 'email to friend' in command:
        try:
            talk("What should I say?")
            contents = take_command()
            to = "gajakde129@gmail.com"
            sendEmail(to, contents)
            talk("Email has been sent!")
        except Exception as e:
            print(e)
            talk("Sorry my friend . I am not able to send this email")
    elif 'good bye' in command or 'goodbye' in command:
        talk("good bye")
        final_time_to_execute()
        exit()
    else:
        print('Please say the command again.')
        talk('Please say the command again.')


if __name__ == "__main__":
    wish()
    while True:
        talk('say command')
        run_angelina()
