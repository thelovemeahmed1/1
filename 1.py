import os

os.system('sudo apt update -y')
os.system('sudo apt install python3-pip -y')
os.system('rm -rf google-chrome-stable_current_amd64.deb')
os.system('sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
os.system('sudo apt install ./google-chrome-stable_current_amd64.deb -y')
os.system('sudo apt-get install ffmpeg -y')
os.system('pip3 install SpeechRecognition pydub selenium seleniumbase')

try:
    from selenium import webdriver
except:
    os.system('pip3 install selenium')
    from selenium import webdriver
try:
    from seleniumbase import Driver
except:
    os.system('pip3 install seleniumbase')
import random
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import json
import string
import multiprocessing
from subprocess import Popen
import sys
import speech_recognition as sr
from pydub import AudioSegment
firebaseio_link='https://mona-cae59-default-rtdb.firebaseio.com'


code_country = '228'
#def mexc():
while True:
    try:

        def generate_password(length):
            if length < 1:
                return "Length must be at least 1"
            
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(length - 1))
            password += random.choice(string.digits)
            password = ''.join(random.sample(password, len(password)))
            
            
            return password
        password= generate_password(random.randint(10,19))
        driver = Driver(uc=True)

        def captchat():
            global driver
            try:
                
                driver.switch_to.default_content()
                captcha_frame_2 = driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']")
                driver.switch_to.frame(captcha_frame_2)
                time.sleep(3)
                driver.find_element(By.ID, 'recaptcha-anchor').click()
                time.sleep(5)
                driver.switch_to.default_content()
                captcha_frame_2 = driver.find_element(By.XPATH, ".//iframe[@title='recaptcha challenge expires in two minutes']")
                driver.switch_to.frame(captcha_frame_2)       

                driver.find_element(By.ID, 'recaptcha-audio-button').click()    
                time.sleep(3)
                audio_link = driver.find_element(By.CLASS_NAME, 'rc-audiochallenge-tdownload-link')
                audio_url = audio_link.get_attribute("href")
                #print(audio_url)
                file_name = "audio.mp3"
                response = requests.get(audio_url)
                if response.status_code == 200:

                    with open(file_name, 'wb') as f:
                        f.write(response.content)

                src = "audio.mp3"
                sound = AudioSegment.from_mp3(src)
                sound.export("podcast.wav", format="wav")

                file_path = os.path.join(os.getcwd(), "podcast.wav")
                r = sr.Recognizer()
                with sr.AudioFile(file_path) as source:
                    audio_text = r.record(source)
                audio_text_code = r.recognize_google(audio_text)
                driver.find_element(By.ID, 'audio-response').send_keys(audio_text_code)
                time.sleep(3)
                driver.find_element(By.ID, 'audio-response').send_keys(Keys.RETURN)
                time.sleep(3)
                print('captchat_true')
            except Exception as s:
                print(s)
        
        response_get = requests.get(f'{firebaseio_link}/premiumy/num_mexc/sms_mexc/{code_country}.json')
        user_data = response_get.json()
        if user_data is None:
            
            print('no num_facebook_create')
            #break      
        else:
            first_key = random.choice(list(user_data.keys()))
            phone_mexc= user_data[first_key].strip()
        
        driver.get('https://www.mexc.com/login')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/div/div/div[1]/div[2]').click()
        driver.find_element(By.XPATH, f"//*[text()='+{code_country}']").click()
        driver.find_element(By.ID, 'mobileInputwwwmexccom').send_keys(phone_mexc)
        time.sleep(5)
        driver.find_element(By.ID, 'mobileInputwwwmexccom').send_keys(Keys.RETURN)
        time.sleep(5)
            
        code_captchat = driver.find_element(By.XPATH, '/html/body').text
        if 'Slide to complete the puzzle' in code_captchat:
            print('Slide to complete the puzzle')
        elif 'Security Verification' in code_captchat:
            print('Security Verification')
            captchat()
            driver.save_screenshot('captchat.png')
            time.sleep(3)
            driver.find_element(By.ID, 'login_password').send_keys(password)

            driver.find_element(By.ID, 'login_agreed').click()
            time.sleep(3)
            driver.find_element(By.ID, 'login_password').send_keys(Keys.RETURN)
            requests.delete('{}/premiumy/num_mexc/sms_mexc/{}/{}.json'.format(firebaseio_link,code_country,int(phone_mexc)))
            for a in range(3):
                print(a)
                time.sleep(60)
                driver.find_element(By.XPATH, "//*[text()='Get Code']").click()
        else:
            print(code_captchat)


        
        time.sleep(5)
        driver.save_screenshot('gmail.png')
        try:
            driver.close()
        except:
            pass
    except Exception as ss:
        print(ss)
        driver.save_screenshot('erro_gmail.png')
        try:
            driver.close()
        except:
            pass


#mexc()
