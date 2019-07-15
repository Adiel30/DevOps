from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="/Users/adiellevy/Downloads/chromedriver")
driver.implicitly_wait(30)
#driver.get("https://translate.google.co.il/?hl=en&tab=rT")

#print(driver.current_url)

#print(driver.title)


#print(driver.page_source)

#list_of_source = driver.find_element_by_class_name("tlid-results-container")
#print(len(list_of_source))
#print(driver.find_element_by_class_name("tlid-results-container"))

#driver.find_element_by_xpath("/html/body[@class='displaying-homepage']/div[@class='frame']/div[@class='page tlid-homepage homepage translate-text']/div[@class='homepage-content-wrap']/div[@class='tlid-source-target main-header']/div[@class='source-target-row']/div[@class='tlid-input input']/div[@class='source-wrap']/div[@class='input-full-height-wrapper tlid-input-full-height-wrapper']/div[@class='source-input']/div[@id='input-wrap']/textarea[@id='source']")\

#my_click = driver.find_element_by_id("source")
#my_click.send_keys("hello")

#my_element = driver.find_element_by_id("source")
#if my_element.is_enabled():
#    print(my_element.is_enabled())
driver.get("https://www.google.com")
#my_search = driver.find_element_by_class_name("gLFyf gsfi").send_keys("")
#my_search = driver.find_element_by_xpath("/html/body[@id='gsr']/div[@id='viewport']/div[@id='searchform']/form[@id='tsf']/div[2]/div[@class='A8SBwf']/div[@class='RNNXgb']/div[@class='SDkEP']/div[@class='a4bIc']/input[@class='gLFyf gsfi']").send_keys("אתה כמו תות שדה בבתוך קצפת")
#my_enter = driver.find_element_by_xpath("/html/body[@id='gsr']/div[@id='viewport']/div[@id='searchform']/form[@id='tsf']/div[2]/div[@class='A8SBwf']/div[@class='RNNXgb']/div[@class='SDkEP']/div[@class='a4bIc']/input[@class='gLFyf gsfi']").send_keys(Keys.ENTER)

