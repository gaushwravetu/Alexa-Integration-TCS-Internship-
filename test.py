import speech_recognition as sr
import webbrowser as wb

# making 3 instances
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

# here i'm using the microphone as source
with sr.Microphone() as source:
    print('[search hello: search youtube]')
    print('speak now')
    # here i'm listening from the source 
    audio=r3.listen(source)
    print("hold on while we open:",r2.recognize_google(audio).lower())
# using google api for searching
if 'google' in (r2.recognize_google(audio)).lower():
    r2 = sr.Recognizer()
    url = 'https://www.google.com/search?q='
    with sr.Microphone() as source:
        print('search your query')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))

elif 'youtube' in (r1.recognize_google(audio)).lower():
    # print((r1.recognize_google(audio)).lower())
    r1 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('search your video')
        audio = r1.listen(source)
        # print(audio)

        try:
            get = r1.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))


