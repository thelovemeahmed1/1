import sys
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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from seleniumbase import Driver
import requests
import time
import speech_recognition as sr
from pydub import AudioSegment
import random

firebaseio_link='https://tiktok10-86541-default-rtdb.firebaseio.com'
while True:
    try:
        driver = Driver(uc=True)
        driver.implicitly_wait(10)
        driver.get('https://manage.bein.com/account/subscribe#country')
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
        driver.find_element(By.XPATH, "//*[text()='Iraq']").click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "curved_buttons_right").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/app-root/main/subscription-main/div[1]/div/div[2]/div[1]/package[1]/selection-box[1]/div[1]/div[3]/div").click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "curved_buttons_right").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/app-root/main/subscription-main/div[1]/div/div[2]/div[1]/device/selection-box[1]/div[1]/div[3]/div").click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "curved_buttons_right").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/app-root/main/subscription-main/div[1]/div/div[2]/div[1]/service/selection-box[3]/div[1]/div[3]/div").click()
        driver.find_element(By.CLASS_NAME, "curved_buttons_right").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/app-root/main/subscription-main/div[1]/div/div[2]/div[1]/payment-plan/selection-box[1]/div[1]/div[3]/div").click()
        driver.find_element(By.CLASS_NAME, "curved_buttons_right").click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "curved_buttons_right").click()
        time.sleep(3)
        phone = '7802185140'
        response_get = requests.get(f'{firebaseio_link}/premiumy/num_bein/sms_bein.json')
        user_data = response_get.json()
        if user_data is None:
            time.sleep(10)
            print('finsh')
        else:
            first_key = random.choice(list(user_data.keys()))
            phone_bein = user_data[first_key].strip()
            print(phone_bein)
        response_delete = requests.delete('{}/premiumy/num_bein/sms_bein/{}.json'.format(firebaseio_link,int(phone_bein)))
        driver.find_element(By.XPATH, "/html/body/app-root/main/subscription-main/div[1]/div/div[2]/div[1]/personal/div[1]/div[1]/div[2]/input").send_keys(phone_bein.split('964')[-1])
        time.sleep(3)
        captchat()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.find_element(By.XPATH, "//*[text()=' Send Code ']").click()
        time.sleep(10)
        try:
            driver.quit()
        except:
            pass
    except Exception as sss:
        print(sss)
        #input('erro')
        try:
            driver.quit()
        except:
            pass
