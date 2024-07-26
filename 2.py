from appium import webdriver
import requests
import random
import time
import os
from selenium.webdriver.remote.remote_connection import RemoteConnection

# تعيين مهلة الاتصال إلى 60 ثانية
RemoteConnection.set_timeout(60)
# إعدادات Appium
desired_caps = {
    "platformName": "Android",
    "deviceName": "your_device_name",
    "automationName": "UiAutomator2",
    "appPackage": "com.ubercab.uberlite",
    "appActivity": "com.ubercab.uberlite.feature.RootActivity",
    "noReset": True,
    "fullContextList": True,
}

# إعداد الاتصال بـ Appium
server_url = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(server_url, desired_caps)
firebaseio_link='https://hotmail-4261b-default-rtdb.firebaseio.com'

def uber():
    try:
        response_get = requests.get(f'{firebaseio_link}/premiumy/num_uber/sms_uber.json')
        user_data = response_get.json()
        if user_data is None:
            print('no num_uber_password')
        else:
            first_key = random.choice(list(user_data.keys()))
            phone_uber = user_data[first_key].strip()
            print(phone_uber)
        
        time.sleep(2)
        driver.launch_app()
        time.sleep(2)

        # السماح بالوصول إلى الأذونات
        allow_button = driver.find_element_by_android_uiautomator('new UiSelector().text("ALLOW")')
        allow_button.click()
        time.sleep(2)

        # بدء التسجيل
        get_started_button = driver.find_element_by_android_uiautomator('new UiSelector().text("Get started")')
        get_started_button.click()
        time.sleep(5)

        # إدخال رقم الهاتف
        phone_input = driver.find_element_by_android_uiautomator('new UiSelector().text("Enter phone number or email")')
        phone_input.send_keys(f'+{phone_uber}')
        time.sleep(2)

        # متابعة
        forward_button = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("forward-button")')
        forward_button.click()

        # حذف البيانات من Firebase
        requests.delete('{}/premiumy/num_uber/sms_uber/{}.json'.format(firebaseio_link, int(phone_uber)))

        for a in range(3):
            time.sleep(10)
            print(a)
            otp_button = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("alt-PHONE-OTP")')
            otp_button.click()
    
    except Exception as s:
        print(s)
    finally:
        driver.quit()

# استدعاء الدالة
uber()
