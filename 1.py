
import sys
import os
import requests
import multiprocessing
import subprocess
import time
firebaseio_link='https://mona-cae59-default-rtdb.firebaseio.com'

upload_code_totel = ['sms_mexc.py']
for upload_code in upload_code_totel:
    code_sussfole = upload_code.split('.py')[0]
    response = requests.get(f'{firebaseio_link}/code_list/{code_sussfole}_code.json')
    user_data = response.json()
    if response.status_code == 200:
        with open(upload_code, 'w', encoding='utf-8') as file:
            file.write(user_data['code_content'])
        print(upload_code)

    else:
        print("false", response.status_code)

os.system('sudo apt update -y')
os.system('sudo apt install python3-pip -y')
os.system('rm -rf google-chrome-stable_current_amd64.deb')
os.system('sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
os.system('sudo apt install ./google-chrome-stable_current_amd64.deb -y')
os.system('sudo apt-get install ffmpeg -y')
os.system('pip install mailosaur')
os.system('pip install names')
os.system('pip install SpeechRecognition')
os.system('pip install pydub')
os.system('pip install selenium')
os.system('pip install seleniumbase')
os.system('pip install mailslurp-client')
os.system('pip install exchangelib')
def sms_facebook():
    print('yes')
    #os.system('python sms_facebook.py')
    while True:
        try:
            time.sleep(10)
            os.system('python sms_mexc.py')
        except:
            print('sms_mexc_errrrp')

while True:
    sms_facebook()
