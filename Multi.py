from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from package.functions_and_variables import *

cap = []

for i in range(amount):

  cap.append({
    "platformName": "Android",
    "appium:platformVersion": "12.0.0",
    "appium:deviceName": "emulator-"+str(5554+i*2),
    "appium:udid": "emulator-"+str(5554+i*2),
    "appium:appPackage": "com.mplusapp.mplus.bbb_app",
    "appium:appActivity": "com.mplusapp.mplus.bbb_app.MainActivity",
    "appium:noReset": True,
    "appium:isHeadless": True
})


driver = []

for i in range(amount):
  driver_example = webdriver.Remote("http://localhost:4723/wd/hub",cap[i])
  driver.append(driver_example)
  print('connect+1'+str(cap[i]['appium:udid']))


for i in range(amount):
  driver[i].implicitly_wait(20)

#TC47
#start
print("check 1")
for i in range(amount):
  driver[i].find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]').click()
print("check 2")
time.sleep(1)

for i in range(amount):
  driver[i].find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').click()
print("check 3")
time.sleep(1)
for i in range(amount):
  driver[i].find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').clear()
  driver[i].find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').send_keys(get_meeting_url())
print("check 4")
time.sleep(1)

for i in range(amount):
  driver[i].find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join"]').click()
print("check 5")
time.sleep(1)

for i in range(amount):
  driver[i].find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()
  driver[i].find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').clear()
  driver[i].find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('  @@$@$')
  driver[i].find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Join"]').click()

print("TC47 OK")


print("check 6")
for i in range(amount):
  driver[i].find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.Button[1]").click()
print("check 7")
time.sleep(1200)
print("check 7")
for i in range(amount):
  driver[i].find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.Button[1]").click()

print("check 8")
for i in range(amount):  
  driver[i].quit()