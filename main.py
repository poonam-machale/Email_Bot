import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('nidhi1993c@gmail.com', '123@nidhi')
    email = EmailMessage()
    email['From'] = 'nidhi1993c@gmail.com'
    email ['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    # server.sendmail('nidhi1993c@gmail.com', 'poonammachale@gmail.com', 'Hello, This is testing email.')


email_list = {
    'snehal': 'liebe.snehal@gmail.com',
    'poonam': 'poonammachale@gmail.com'
}

def get_email_info():
    talk('To whom you want to send an email?')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell the message that you want to send')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey, your email is sent. Do you want to send more emails?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()

