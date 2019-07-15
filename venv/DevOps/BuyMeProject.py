from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Open rtf file that holds URL
with open('/Users/adiellevy/Documents/buyme.rtf', 'r') as site:
    my_url = site.read()
# Loads the Chrome driver for selenium
driver = webdriver.Chrome(executable_path='/Users/adiellevy/Downloads/chromedriver')
driver.maximize_window()
driver.implicitly_wait(60)
# Open the site
driver.get(my_url)
# click on the "Register\Sign in"
driver.find_element_by_class_name('seperator-link').click()
# click "Register"
driver.find_element_by_class_name('text-btn').click()
# Write name, mail & password

name = driver.find_element_by_css_selector('#ember1037')
name.send_keys('Adiel')
mail = driver.find_element_by_css_selector('#ember1039')
mail.send_keys('Adiaj4999@renewt.co.il')
password = driver.find_element_by_id('valPass')
password.send_keys('Aa123456')
confirmPassword = driver.find_element_by_css_selector('#ember1043')
confirmPassword.send_keys('Aa123456')

# I agree checkbox

driver.execute_script('arguments[0].click();', driver.find_element_by_class_name('fa'))

# Click on Registration for "BuyMe"

driver.find_element_by_class_name('ui-btn').click()

time.sleep(5)
driver.find_element_by_css_selector('#ember664_chosen > a').click()
priceSelect = driver.find_elements_by_class_name('active-result')
priceSelect[2].click()

driver.find_element_by_css_selector('#ember679_chosen > a').click()
time.sleep(4)
regionSelect = driver.find_elements_by_class_name('active-result')
driver.execute_script('arguments[0].click();', regionSelect[2])

driver.find_element_by_css_selector('#ember689_chosen > a').click()
categoreySelect = driver.find_element_by_css_selector('#ember689_chosen > div > div > input[type=text]')
categoreySelect.send_keys('אופנה', Keys.ENTER)

findGift = driver.find_element_by_id('ember724')
findGift.click()

# Select Shop
driver.execute_script('arguments[0].click();', driver.find_element_by_css_selector('#ember1200 > div'))
# Gift Details & Delivery
giftSum = driver.find_element_by_xpath('//*[@id="ember1246"]')
giftSum.send_keys('150',Keys.ENTER)

giftFor = driver.find_element_by_xpath('//*[@id="ember1324"]')
giftFor.send_keys('TTT')

giftEvent = driver.find_element_by_xpath('//*[@id="ember1328_chosen"]/a')
giftEvent.click()
giftEventBirth = driver.find_element_by_xpath('//*[@id="ember1328_chosen"]/div/div/input')
giftEventBirth.send_keys('לידה', Keys.ENTER)

uploadPhoto = driver.find_element_by_xpath('//*[@id="ember1359"]')
uploadPhoto.send_keys('/Users/adiellevy/Documents/NewImage.jpg')
sendByMail = driver.find_element_by_css_selector('#ember1291 > div.send-methods.section.relative.error-newline > div > div.row.row--with-less-gutter.row--sm > div:nth-child(2) > div > button > span > span.btn-text')
sendByMail.click()
sendTo = driver.find_element_by_xpath('//*[@id="ember1797"]')
sendTo.send_keys('minime@gmail.com', Keys.ENTER)
Payment = driver.find_element_by_xpath('//*[@id="ember1291"]/div[5]/button')
Payment.click()







