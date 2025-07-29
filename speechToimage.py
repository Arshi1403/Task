from monsterapi import client
import requests
import webbrowser
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something....")
    audio=recognizer.listen(source,timeout=10,phrase_time_limit=10)
    text=recognizer.recognize_google(audio,language='en-US')
    

api_key='[api key]'

monster_client=client(api_key)

model='txt2img'

input_data={
    'prompt':f'{text}',
    'negprompt':'bad anatomy',
    'samples':1,
    'steps':50,
    'aspect_ratio':'square',
    'guidance_scale':7.5,
    'seed':2414
}

result=monster_client.generate(model,input_data)

img_url=result['output'][0]

file_name="generated_img.jpg"

response=requests.get(img_url)
if response.status_code==200:
    with open(file_name,'wb') as file:
        file.write(response.content)
    print("Image downloaded")

    #open the image
    webbrowser.open(file_name)

else:
    print("Failed to download")