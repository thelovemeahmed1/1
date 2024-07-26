from appium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

# إعداد القدرات
desired_caps = {
    "platformName": "Android",
    "deviceName": "serveo.net:5551",
    "automationName": "UiAutomator2",
    "appPackage": "com.tinder",
    "appActivity": "com.tinder.launch.internal.activities.LoginActivity",
    "noReset": True
}

# عنوان الخادم و المنفذ
server_url = 'http://localhost:4723/wd/hub'  # تأكد من أن Appium يعمل على هذا المنفذ

# تعيين مهلة الاتصال
RemoteConnection.set_timeout(60)  # تعيين مهلة الاتصال إلى 60 ثانية

# إنشاء مثيل لمشغل Appium
driver = webdriver.Remote(server_url, desired_caps)

# تأكد من أن الاتصال تم بنجاح
print("App launched successfully!")

# يمكنك الآن التفاعل مع التطبيق عبر `driver`

