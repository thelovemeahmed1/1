import os
try:
    from uiautomator import Device
except:
    os.system('pip install pycountry phonenumbers uiautomator')

import time
import requests
import random
import os

import subprocess
import uuid
import phonenumbers
from phonenumbers import geocoder
#ip_address ='10.55.155.20:5555'#10.55.77.91:5555 #10.55.155.20:5555
#ip_address ='10.55.77.91:5555'
ip_address="127.0.0.1:5565"
os.system(f'adb connect {ip_address}')
d = Device(f'{ip_address}')
firebaseio_link='https://tiktok-e1218-default-rtdb.firebaseio.com'
#xml = d.dump()
def start():
    try:
        os.system('adb shell am force-stop io.oxylabs.proxymanager')
        os.system('adb shell am start -n io.oxylabs.proxymanager/io.oxylabs.proxymanager.MainActivity')
        d(text="connect").click()
        d.press.back()
        time.sleep(5)
    except Exception as s:
        print(s)
def change_android():
    def generate_random_imei():
        imei = '35'  # IMEI prefix for testing (adjust based on your needs)
        for _ in range(13):
            imei += str(random.randint(0, 9))
        return imei

    def generate_random_android_id():
        return uuid.uuid4().hex

    def generate_random_mac_address():
        mac = [0x00, 0x16, 0x3e,
               random.randint(0x00, 0x7f),
               random.randint(0x00, 0xff),
               random.randint(0x00, 0xff)]
        return ':'.join(map(lambda x: "%02x" % x, mac))

    def generate_random_serial_number():
        return uuid.uuid4().hex[:16]
    random_imei = generate_random_imei()
    random_android_id = generate_random_android_id()
    random_mac_address = generate_random_mac_address()
    random_serial_number = generate_random_serial_number()
    os.system(f'adb shell settings put secure android_id {random_android_id}')
    os.system(f'adb shell service call iphonesubinfo 1 s16 "{random_imei}"')
    os.system(f'adb shell settings put global device_provisioned_serialno {random_serial_number}')
    
def didi():
    
    try:
        response_get = requests.get(f'{firebaseio_link}/premiumy/num_didi/sms_didi.json')
        user_data = response_get.json()
        if user_data is None:
            print('no didi_password')   
        else:
            first_key = random.choice(list(user_data.keys()))
            phone_didi= '+'+ user_data[first_key].strip() 
            print(phone_didi)
            os.system('adb shell pm clear com.didiglobal.passenger')
            os.system('adb shell am start -n com.didiglobal.passenger/com.didi.sdk.app.DidiLoadDexActivity')
            d(text="Agree").click()
            d(text="ALLOW").click()
            d(text="ALLOW").click()
            time.sleep(2)
            d(description="+1").click()
            d(description="E").click()
            d(description="Egypt").click()
            d(description="Enter mobile No.").click()
            time.sleep(2)
            d(className="android.widget.EditText").set_text(phone_didi.split('+20')[-1])
            d.press.enter()
            d(className="android.widget.CheckBox").click()
            d(description="Next").click()
            d(description="Via SMS").click()
            time.sleep(5)
            d.press.back()
            d.press.back()
            d(description="Next").click()
            d(description="Via SMS").click()
            time.sleep(5)
            
            response_delete = requests.delete('{}/num_uber/sms_uber/{}.json'.format(firebaseio_link,int(phone_didi)))
    except Exception as s:
            print(s)
def tinder():
    try:
        response_get = requests.get(f'{firebaseio_link}/premiumy/num_tinder/sms_tinder.json')
        user_data = response_get.json()
        if user_data is None:
            print('no didi_password')
        else:
            first_key = random.choice(list(user_data.keys()))
            phone_tinder= '+'+ user_data[first_key].strip() 
            print(phone_tinder)
            parsed_number = phonenumbers.parse(phone_tinder)
            country_name = geocoder.description_for_number(parsed_number, "en")
            country_code = parsed_number.country_code
            os.system('adb shell pm clear com.tinder')
            os.system('adb shell am start -n com.tinder/com.tinder.launch.internal.activities.LoginActivity')
            d(text="Sign in with Phone Number").click()
            d(className="android.widget.EditText").set_text(country_code)
            d(text=f"+{country_code}").click()
            d(text="Phone Number").set_text(phone_tinder.split(f'+{country_code}')[-1])
            d(text="Next").click()
            response_delete = requests.delete(f'{firebaseio_link}/premiumy/num_didi/num_didi/{first_key}.json')
            time.sleep(20)
            '''
            d.press.recent()
            if d(text="Tinder").exists:
                d(text="Tinder").swipe.right()
            
            os.system('adb shell am force-stop com.tinder')
            '''
            d.press.back()
            d.press.back()
            d.press.back()
            d.press.back()
            os.system('adb shell am force-stop com.tinder')

            #
            
    except Exception as s:
        print(s)
def imo():
    try:
        response_get = requests.get(f'{firebaseio_link}/premiumy/num_didi/sms_didi.json')
        user_data = response_get.json()
        if user_data is None:
            print('no didi_password')
        else:
            first_key = random.choice(list(user_data.keys()))
            phone_imo= '+'+ user_data[first_key].strip() 
            print(phone_imo)
            parsed_number = phonenumbers.parse(phone_imo)
            country_name = geocoder.description_for_number(parsed_number, "en")
            country_code = parsed_number.country_code
            os.system('adb shell pm clear com.imo.android.imoim')
            os.system('adb shell am start -n com.imo.android.imoim/com.imo.android.imoim.home.Home')
            d(text="Search").set_text(country_code)
            d(text=f"+{country_code}").click()
            d(text="Agree").click()
            d(text="ALLOW").click()
            d(text="Phone number").set_text(phone_imo.split(f'+{country_code}')[-1])
            d.press.enter()
            d(text="Okay").click()
            time.sleep(10)            
    except Exception as s:
        print(s)
def yango():
    try:
        response_get = requests.get(f'{firebaseio_link}/premiumy/num_didi/sms_didi.json')
        user_data = response_get.json()
        if user_data is None:
            print('no didi_password')
        else:
            first_key = random.choice(list(user_data.keys()))
            phone_yango= '+'+ user_data[first_key].strip() 
            print(phone_yango)
            os.system('adb shell pm clear com.yandex.yango')

            os.system('adb shell am start -n com.yandex.yango/ru.yandex.taxi.activity.MainActivity')
            time.sleep(15)
            d(resourceId='com.yandex.yango:id/continue_button').click()
            d(text="DENY").click()
            d(className="android.widget.EditText").set_text(phone_yango)
            d(text="Continue").click()
            time.sleep(10) 
    except Exception as s:
        print(s)
def viber():
    try:
        #code_d = '+63'
        response_get = requests.get(f'{firebaseio_link}/premiumy/num_didi/sms_didi.json')
        user_data = response_get.json()
        if user_data is None:
            print('no didi_password')
        else:
            first_key = random.choice(list(user_data.keys()))
            phone_viber= '+'+user_data[first_key].strip() 
            print(phone_viber)
            parsed_number = phonenumbers.parse(phone_viber)
            country_name = geocoder.description_for_number(parsed_number, "en")
            country_code = parsed_number.country_code

            os.system('adb shell pm clear com.viber.voip')
            os.system('adb shell am start -n com.viber.voip/com.viber.voip.WelcomeActivity')
            d(text="Start now").click()
            time.sleep(3)
            d(resourceId='com.viber.voip:id/registration_code_field').clear_text()
            d(resourceId='com.viber.voip:id/registration_code_field').set_text(country_code)
            d(resourceId='com.viber.voip:id/registration_phone_field').set_text(phone_viber.split(f'+{country_code}')[-1])
            time.sleep(3)
            d(text="Continue").click()
            d(text="Continue").click()
            d(text="DENY").click()
            d(text="DENY").click()
            requests.delete('{}/premiumy/num_didi/sms_didi/{}.json'.format(firebaseio_link,int(phone_viber)))
            '''
            tinder()
            tinder()
            tinder()
            os.system('adb shell am start -n com.viber.voip/com.viber.voip.WelcomeActivity')
            '''
            time.sleep(70) 
            d(text="RESEND SMS").click()
            time.sleep(5)
    except Exception as s:
        print(s)


def uber():
    
    try:
        response_get = requests.get(f'{firebaseio_link}/premiumy/num_didi/sms_didi.json')
        user_data = response_get.json()
        if user_data is None:
            print('no num_uber_password')

        else:
            first_key = random.choice(list(user_data.keys()))
            phone_uber= user_data[first_key].strip()
            print(phone_uber)
        time.sleep(2)
        os.system("adb shell pm clear com.ubercab.uberlite")
        os.system('adb shell  am start -n com.ubercab.uberlite/com.ubercab.uberlite.feature.RootActivity')
        time.sleep(2)  
        d(text="ALLOW").click()
        time.sleep(2)
        d(text="Get started").click()
        time.sleep(5)
        d(resourceId="PHONE_NUMBER_or_EMAIL_ADDRESS").set_text(f'+{phone_uber}')
        time.sleep(2)
        d(resourceId='forward-button').click()
        requests.delete('{}/premiumy/num_uber/sms_uber/{}.json'.format(firebaseio_link,int(phone_uber)))
        for a in range(3):
            time.sleep(10)
            print(a)
            d(resourceId='alt-PHONE-OTP').click()        
    except Exception as s:
        print(s)
def whatsappb():
    try:
        firebaseio_link = 'https://tiktok2-1bacb-default-rtdb.firebaseio.com'
        response_get = requests.get(f'{firebaseio_link}/premiumy/num_whatsapp/sms_whatsapp.json')
        user_data = response_get.json()

        if user_data is None:
            print('no num_uber_password')
        else:
            first_key = random.choice(list(user_data.keys()))
            phone_whatsapp = user_data[first_key].strip()
            print(phone_whatsapp)
            parsed_number = phonenumbers.parse(phone_whatsapp)
            country_name = geocoder.description_for_number(parsed_number, "en")
            country_code = parsed_number.country_code
            response_delete = requests.delete(f'{firebaseio_link}/premiumy/num_whatsapp/sms_whatsapp/{first_key}.json')
            os.system("adbshell pm clear com.whatsapp.w4b")
            os.system("adb shell am start -n com.whatsapp.w4b/com.whatsapp.Main")
            d(resourceId="com.whatsapp.w4b:id/eula_accept").click()
            d(resourceId="com.whatsapp.w4b:id/registration_cc").clear_text()
            d(resourceId="com.whatsapp.w4b:id/registration_cc").set_text(country_code)
            d(resourceId="com.whatsapp.w4b:id/registration_phone").clear_text()
            d(resourceId="com.whatsapp.w4b:id/registration_phone").set_text(phone_whatsapp.split(f'+{country_code}')[-1])
            d(resourceId="com.whatsapp.w4b:id/registration_submit").click()
            time.sleep(5)
            d(resourceId="android:id/button1").click()
            d(text="VERIFY ANOTHER WAY").click()
            d(text="SEND SMS").click()
            time.sleep(15)
    except Exception as s:
        print(s)
        os.system("adb shell pm clear com.whatsapp.w4b")

def grab():
    try:
        code_d="Philippines (PH)"
        code_d2='Philippines'
        response_get = requests.get(f'{firebaseio_link}/premiumy/num_didi/sms_didi.json')
        user_data = response_get.json()
        if user_data is None:
            print('no didi_password')
        else:
            first_key = random.choice(list(user_data.keys()))
            phone_grab= user_data[first_key].strip() 
            print(phone_grab)
            os.system('adb shell pm clear com.grabtaxi.passenger')

            os.system('adb shell am start -n com.grabtaxi.passenger/com.grab.pax.newface.presentation.newface.NewFace')
            d(text="Sign Up").click()
            d(resourceId='com.grabtaxi.passenger:id/verify_number_code_country').click()
            d(text='Search').set_text(code_d2)
            d(text=f"{code_d}").click()

            d(resourceId='com.grabtaxi.passenger:id/verify_number_edit_number').set_text(phone_grab)
            
            d(text="Next").click()
            time.sleep(10) 
    except Exception as s:
        print(s)

#start()
#didi()
#tinder()
#imo()
#yango()
#uber()
#whatsappb()
#viber()
while True:
    start()
    viber()
