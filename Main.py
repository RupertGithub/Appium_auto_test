from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from package.functions_and_variables import *
cap = {
  "platformName": "Android",
  "appium:platformVersion": "12.0.0",
  "appium:deviceName": "emulator-5554",
  "appium:appPackage": "com.mplusapp.mplus.bbb_app",
  "appium:appActivity": "com.mplusapp.mplus.bbb_app.MainActivity",
  "appium:noReset": True,
  "appium:isHeadless": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",cap)
driver.implicitly_wait(20)


#TC38
#Copy last meeting url and join with it
driver.find_element(AppiumBy.XPATH,'//android.view.View[starts-with(@content-desc, "Last meeting")]').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Copy meeting url"]').click()
driver.find_element(AppiumBy.XPATH,"//android.widget.FrameLayout/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Button[1]").click()
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]').click()
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').click()
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').send_keys(driver.get_clipboard_text())
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join"]').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('  @@$@$')
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Join"]').click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.Button[5]").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Yes']").click()
print("TC38 OK")

#TC39
#Join last meeting
driver.find_element(AppiumBy.XPATH,'//android.view.View[starts-with(@content-desc, "Last meeting")]').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('  @@$@$')
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Join"]').click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.Button[5]").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Yes']").click()
print("TC39 OK")


#TC40
#Join with URL
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').send_keys(get_meeting_url())
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join"]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('  @@$@$')
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Join"]').click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.Button[5]").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Yes']").click()
print("TC40 OK")


#TC43
#Login
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Gu"]').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@content-desc="M+ Account Log in"]/android.widget.EditText[1]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@content-desc="M+ Account Log in"]/android.widget.EditText[1]').send_keys("rr70739@yahoo.com.tw")
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@content-desc="M+ Account Log in"]/android.widget.EditText[2]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@content-desc="M+ Account Log in"]/android.widget.EditText[2]').send_keys("09350935Aa")
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Log in"]').click()
#Logout
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Ru"]').click()
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Login out"]').click()
print("TC43 OK")

#TC44
#Check video switch before and after joining meeting
driver.find_element(AppiumBy.XPATH,'//android.view.View[starts-with(@content-desc, "Last meeting")]').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('  @@$@$')
before_video_switch_on = driver.find_element(AppiumBy.XPATH,'//android.view.View/android.widget.Switch[1]').get_attribute('checked')
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Join"]').click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.Button[5]").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Yes']").click()
driver.find_element(AppiumBy.XPATH,'//android.view.View[starts-with(@content-desc, "Last meeting")]').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('  @@$@$')
driver.find_element(AppiumBy.XPATH,'//android.view.View/android.widget.Switch[1]').click()
before_video_switch_on = driver.find_element(AppiumBy.XPATH,'//android.view.View/android.widget.Switch[1]').get_attribute('checked')
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Join"]').click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.Button[5]").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Yes']").click()
print("TC44 OK")


#TC45
#Check microphone switch before and after joining meeting
driver.find_element(AppiumBy.XPATH,'//android.view.View[starts-with(@content-desc, "Last meeting")]').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('  @@$@$')
before_video_switch_on = driver.find_element(AppiumBy.XPATH,'//android.view.View/android.widget.Switch[2]').get_attribute('checked')
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Join"]').click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.Button[5]").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Yes']").click()
driver.find_element(AppiumBy.XPATH,'//android.view.View[starts-with(@content-desc, "Last meeting")]').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('  @@$@$')
driver.find_element(AppiumBy.XPATH,'//android.view.View/android.widget.Switch[2]').click()
before_video_switch_on = driver.find_element(AppiumBy.XPATH,'//android.view.View/android.widget.Switch[2]').get_attribute('checked')
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Join"]').click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.Button[5]").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Yes']").click()
print("TC45 OK")


#TC46
#Copy last meeting url and join with it
driver.find_element(AppiumBy.XPATH,'//android.view.View[starts-with(@content-desc, "Last meeting")]').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Copy meeting url"]').click()
driver.find_element(AppiumBy.XPATH,"//android.widget.FrameLayout/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Button[1]").click()
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]').click()
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').click()
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').send_keys(driver.get_clipboard_text())
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join"]').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('  @@$@$')
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Join"]').click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.Button[5]").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Yes']").click()
print("TC46 OK")


#TC47
#start
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join with an url"]/android.widget.EditText').send_keys(get_meeting_url())
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Join"]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('  @@$@$')
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Join"]').click()
print("TC47 OK")


#TC48
#record
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='REC']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@content-desc='No']").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='REC']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@content-desc='Yes']").click()
time.sleep(10)
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='REC']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@content-desc='No']").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='REC']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@content-desc='Yes']").click()
print("TC48 OK")



#TC49
#video switch
driver.find_element(AppiumBy.XPATH,Camera_video_button_xpath).click()
time.sleep(2)
driver.find_element(AppiumBy.XPATH,Camera_video_button_xpath).click()
print("TC49 OK")

#TC50
#microphone switch
time.sleep(1)
driver.find_element(AppiumBy.XPATH,Microphone_button_xpath).click()
time.sleep(2)
driver.find_element(AppiumBy.XPATH,Microphone_button_xpath).click()
print("TC50 OK")


#TC51
#Screen share
driver.find_element(AppiumBy.XPATH,Multi_setting_selection_xpath).click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Start screen sharing']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@resource-id='android:id/button1']").click()
time.sleep(5)
driver.find_element(AppiumBy.XPATH,Stop_share_button_xpath).click()
time.sleep(2)
print("TC51 OK")

#TC52
#Emoji
driver.find_element(AppiumBy.XPATH,Multi_setting_selection_xpath).click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.ImageView[1]").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,Multi_setting_selection_xpath).click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.ImageView[2]").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,Multi_setting_selection_xpath).click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.ImageView[3]").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,Multi_setting_selection_xpath).click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.ImageView[4]").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,Multi_setting_selection_xpath).click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.ImageView[5]").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,Multi_setting_selection_xpath).click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.ImageView[6]").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,Multi_setting_selection_xpath).click()
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.ImageView[7]").click()
time.sleep(1)
print("TC52 OK")

#TC53
#Audio choice
driver.find_element(AppiumBy.XPATH,Multi_setting_selection_xpath).click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Audio Selection']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Speaker']").click()
time.sleep(2)
print("TC53 OK")

#54
#Microphone selection
driver.find_element(AppiumBy.XPATH,Multi_setting_selection_xpath).click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Microphone Selection']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="bottom"]').click()
time.sleep(2)
print("TC54 OK")


#55
#Connection quality
driver.find_element(AppiumBy.XPATH,Multi_setting_selection_xpath).click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Call Quality']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Refresh"]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Refresh"]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Exit"]').click()
time.sleep(2)
print("TC55 OK")

#56
#About
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='About']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button').click()
time.sleep(2)
driver.find_element(AppiumBy.XPATH,"//android.view.View/android.widget.ImageView[6]").click()
print("TC56 OK")

#57
#Share link
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Share the meeting url"]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.Button[1]').click()
time.sleep(1)
print("TC57 OK")


#58
#Search member
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText').send_keys('Rupert')
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button').click()
time.sleep(2)
print("TC58 OK")

#59,60
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').clear()
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('test')
driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button').click()
print("TC59 OK")
print("TC60 OK")




driver.quit()