import os

os.system('sudo apt update -y')
os.system('sudo apt install python3-pip -y')
os.system('rm -rf google-chrome-stable_current_amd64.deb')
os.system('sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
os.system('sudo apt install ./google-chrome-stable_current_amd64.deb -y')
os.system('sudo apt-get install -y xvfb')
os.system('pip3 install gdown')
os.system('gdown --id 1_bUkexQqP_RdjnA_1oqW9YbctFGMrkhf')
os.system('pip3 install names')


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
import names
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import json
import string
from urllib.parse import unquote, quote, quote_plus, urlsplit
import multiprocessing
from subprocess import Popen
import sys
firebaseio_link='https://tiktok10-86541-default-rtdb.firebaseio.com'

xvfb = Popen(['Xvfb', ':1', '-screen', '0', '1920x1080x24'])
os.environ['DISPLAY'] = ':1'
code_country = '226'
def eday():
    while True:
        try:
            def twocapt():
                global captcha_token
                response_get = requests.get(f'{firebaseio_link}/two_captcha/email.json')
                user_data = response_get.json()
                if user_data is None:
                    pass
                else:            
                    for key, value in user_data.items():
                        true_Name = value['true']
                        api_image = value['api']
                        if true_Name == 'true':
                            try:
                                # Get current page URL
                                page_url = driver.current_url
                                # Construct query string for the request
                                querystring = {"website_key": '195eeb9f-8f50-4a9c-abfc-a78ceaa3cdde', "page_url": ''}
                                # Construct request headers
                                headers = {"X-RapidAPI-Key": api_image, "X-RapidAPI-Host": "2captcha4.p.rapidapi.com"}
                                # Send request to 2Captcha API
                                response = requests.get("https://2captcha4.p.rapidapi.com/hcaptcha", headers=headers, params=querystring)
                                # Parse response JSON
                                data = response.json()
                                # Extract captcha response data
                                captcha_data = data['captcha_response']
                                g_response = data['captcha_response']
                                # URL encode the captcha data
                                captcha_data_quoted = quote(json.dumps(captcha_data))
                                # Wait for the iCaptcha iframe to load
                                WebDriverWait(driver, 7.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'target-icaptcha-slot')))
                                # Find the iCaptcha iframe
                                captcha_iframe = driver.find_element(By.CLASS_NAME, 'target-icaptcha-slot').find_elements(By.TAG_NAME, 'iframe')[0]
                                # Get the data-hcaptcha-widget-id attribute
                                captcha_salt = captcha_iframe.get_attribute('data-hcaptcha-widget-id')
                                # Get the iframe src attribute
                                captcha_src = captcha_iframe.get_attribute('src')

                                # Execute JavaScript to fill and submit the captcha
                                driver.execute_script(f"""
                                // Fill the captcha response fields
                                document.getElementsByName("g-recaptcha-response")[0].innerHTML = "{g_response}";
                                document.getElementsByName("h-captcha-response")[0].innerHTML = "{g_response}";
                                document.getElementById("h-captcha-response-{captcha_salt}").innerHTML = "{g_response}";

                                // Set data-hcaptcha-response attribute of the second iframe
                                let iframes = document.getElementsByTagName("iframe");
                                iframes[1].setAttribute("data-hcaptcha-response", "{g_response}");

                                // Call captchaCallback function
                                captchaCallback(true);
                                """)
                                break
                            except Exception as s:
                                print(s)
                                # Update Firebase data if captcha solving fails
                                new_user_data = {'true': "false"}
                                response_put = requests.patch(f'{firebaseio_link}/two_captcha/email/{api_image}.json', json=new_user_data)

            def generate_password(length):
                if length < 1:
                    return "Length must be at least 1"
                
                characters = string.ascii_letters + string.digits
                password = ''.join(random.choice(characters) for i in range(length - 1))
                password += random.choice(string.digits)
                password = ''.join(random.sample(password, len(password)))
                
                return password

            test_email = names.get_full_name().replace(" ", "") + str(random.randint(100, 999))
            email =  test_email + '@hotmail.com'
            username = test_email 
            first = names.get_full_name().split(' ')[0]
            lastname =  names.get_full_name().split(' ')[-1]
            
            filename = 'Solver.crx'
            response_get = requests.get(f'{firebaseio_link}/premiumy/num_ebay/sms_ebay/{code_country}.json')
            user_data = response_get.json()
            if user_data is None:
                
                print('no num_facebook_create')
                #break      
            else:
                first_key = random.choice(list(user_data.keys()))
                phone_ebay= user_data[first_key].strip()
            response_delete = requests.delete('{}/premiumy/num_ebay/sms_ebay/{}/{}.json'.format(firebaseio_link,code_country,int(phone_ebay)))
            
            password= generate_password(random.randint(8,17))
            '''
            driver = Driver(uc=True)
            '''
            

            # تشغيل Xvfb

            options = Options()
            #options.add_argument("--headless")
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("--display=:1")
            #options.add_argument('--disable-gpu')
            #options.add_argument('--window-size=1920,1080')
            current_path = os.getcwd()
            extension_path = os.path.join(current_path, filename)
            options.add_extension(extension_path)
            driver = webdriver.Chrome(options=options)
            

            
            driver.get('https://signup.ebay.com/pa/crte')
            #driver.maximize_window()
            driver.implicitly_wait(120)
            page_height = driver.execute_script("return document.body.scrollHeight;")
            driver.set_window_size(1920, page_height)
            time.sleep(5)
            current_url = driver.current_url.split('?')[0]
            if current_url == 'https://www.ebay.com/splashui/captcha':
                #twocapt()
                pass
            




            time.sleep(3)
            driver.find_element(By.NAME, "firstname").send_keys(first) # email
            driver.find_element(By.NAME, "lastname").send_keys(lastname) # username
            driver.find_element(By.NAME, "Email").send_keys(email)
            driver.find_element(By.NAME, "password").send_keys(password) # password
            time.sleep(5)
            driver.find_element(By.ID, 'EMAIL_REG_FORM_SUBMIT').click()

            driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/form/div[1]/div/span[1]/button/span/span').click()
            driver.find_element(By.XPATH, f"//*[text()='+{code_country}']").click()
            driver.find_element(By.NAME, "phoneCountry").send_keys(phone_ebay.split(code_country)[-1])
            
            driver.find_element(By.ID, 'SEND_AUTH_CODE').click()
            
            driver.save_screenshot('finsh.png')
            def ch():
                for a in range(3):
                    time.sleep(5)
                    #reset_accounts_exist = driver.execute_script("return document.getElementById('phoneCountry_err') !== null;")
                    reset_accounts_exist = driver.execute_script('return document.evaluate("//*[text()=\'Add your phone number\']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue !== null;')
                    backbutton = driver.execute_script('return document.evaluate("//*[text()=\'Enter security code\']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue !== null;')
                    problem_try_again = driver.execute_script('return document.evaluate("//*[text()=\'We ran into a problem. Please try again later.\']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue !== null;')

                    

                    current_url = driver.current_url
                    try:
                        if problem_try_again:
                            print('We ran into a problem. Please try again later.')
                            sys.exit(1)
                        elif reset_accounts_exist:
                            #erro in 'Enter a valid mobile phone number to proceed. ' or erro in 'Please enter a mobile number.':
                            print('yes')
                            response_get = requests.get(f'{firebaseio_link}/premiumy/num_ebay/sms_ebay/{code_country}.json')
                            user_data = response_get.json()

                            first_key = random.choice(list(user_data.keys()))
                            phone_ebay= user_data[first_key].strip()
                            response_delete = requests.delete('{}/premiumy/num_ebay/sms_ebay/{}/{}.json'.format(firebaseio_link,code_country,int(phone_ebay)))
                            print(phone_ebay)
                            for a in phone_ebay:
                                driver.find_element(By.NAME, "phoneCountry").send_keys(Keys.BACKSPACE)

                            time.sleep(2)
                            driver.find_element(By.NAME, "phoneCountry").send_keys(int(phone_ebay.split(code_country)[-1]))
                            time.sleep(2)
                            driver.find_element(By.ID, 'SEND_AUTH_CODE').click()
                            '''
                            for a in range(2):
                                try:
                                    time.sleep(60)
                                    driver.find_element(By.XPATH, "//*[text()='Text me again']").click()
                                except Exception as s:
                                    print('Text me again')
                            '''
                            driver.save_screenshot(f'{phone_ebay}.png')
                        elif backbutton:
                            driver.find_element(By.ID, 'backbutton').click()
                        

                        else:
                            print(current_url)
                            break
                    except Exception as ss:
                        print(ss)
            ch()
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

processes = []
for _ in range(3):
    process = multiprocessing.Process(target=eday)
    processes.append(process)
    process.start()

# Ensure all processes have finished
for process in processes:
    process.join()
