

# 1 A) open chrome
def chrome_url():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Chrome(executable_path="/Users/adiellevy/Downloads/chromedriver")
    driver.get("https://walla.co.il")
    #driver.implicitly_wait(6)

#1 B )
def firefox_url():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Firefox(executable_path="/Users/adiellevy/Downloads/geckodriver")
    driver.get("https://ynet.co.il")
    ynet = driver.title
    driver.refresh()
    if ynet == driver.title:
        print(ynet)

#4 )
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome(executable_path="/Users/adiellevy/Downloads/chromedriver")
#driver.get('https://translate.google.co.il/')
#my_translate = driver.find_element_by_class_name('orig').send_keys('שלום',Keys.ENTER)

#5 )
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome(executable_path='/Users/adiellevy/Downloads/chromedriver')
#driver.get('https://www.youtube.com/?hl=iw&gl=IL')
#my_song_looking = driver.find_element_by_id('search').send_keys('money pink floyd')
#my_song_looking = driver.find_element_by_css_selector('div.style-scope.ytd-app:nth-child(12) div.style-scope.ytd-app:nth-child(1) ytd-masthead.masthead-finish div.style-scope.ytd-masthead:nth-child(4) ytd-searchbox.style-scope.ytd-masthead:nth-child(6) form.style-scope.ytd-searchbox button.style-scope.ytd-searchbox:nth-child(2) > yt-icon.style-scope.ytd-searchbox:nth-child(1)').click()

# 6)
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome(executable_path="/Users/adiellevy/Downloads/chromedriver")
#driver.get('https://translate.google.co.il/')
#getElementOne = driver.find_element_by_class_name('orig')
#getElementTwo = driver.find_element_by_xpath("/html/body[@class='rtl-display-lang displaying-homepage']/div[@class='frame']/div[@class='page tlid-homepage homepage translate-text']/div[@class='homepage-content-wrap']/div[@class='tlid-source-target main-header']/div[@class='source-target-row']/div[@class='tlid-input input']/div[@class='source-wrap']/div[@class='input-full-height-wrapper tlid-input-full-height-wrapper']/div[@class='source-input']/div[@id='input-wrap']/textarea[@id='source']")
#getElementThree = driver.find_element_by_id('source')
#print(getElementTwo)

#7)
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome(executable_path="/Users/adiellevy/Downloads/chromedriver")
#driver.implicitly_wait(10)
#driver.get('https://www.facebook.com/campaign/landing.php?&campaign_id=1641099308&extra_1=s%7Cc%7C314920565653%7Ce%7Cfacebook%7C&placement=&creative=314920565653&keyword=facebook&partner_id=googlesem&extra_2=campaignid%3D1641099308%26adgroupid%3D62120105989%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D1t1%26target%3D%26targetid%3Dkwd-541132862%26loc_physical_ms%3D9050471%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMI6aKT1sb64gIVFIXVCh2evA1iEAAYASAAEgL9n_D_BwE')
#driver.find_element_by_css_selector('#u_0_a').click()
#driver.find_element_by_name('email').send_keys('0507228606')
#driver.find_element_by_css_selector('#pass').send_keys('Passw',Keys.ENTER)
#driver.find_element_by_xpath("""/html[@id='facebook']/body[@class='registration UIPage_LoggedOut _-kb sf _61s0 _605a b_c3pyn-ahh chrome webkit mac x2 Locale_en_US cores-gte4 _19_u hasAXNavMenubar']/div[@id='u_0_e']/div[@id='pagelet_bluebar']/div[@id='blueBarDOMInspector']/div[@class='_53jh']/div[@class='loggedout_menubar_container']/div[@class='clearfix loggedout_menubar']/div[@class='rfloat _ohf']/div[@id='menu_login_container']/form[@id='login_form']/table/tbody/tr[2]/td[2]/input[@id='pass']""").send_keys('password',Keys.ENTER)


#8)
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome(executable_path="/Users/adiellevy/Downloads/chromedriver")
#driver.get('https://walla.co.il')
#driver.delete_all_cookies()
#driver.get_cookies()
#print(driver.get_cookies())


#9)
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome(executable_path="/Users/adiellevy/Downloads/chromedriver")
#driver.implicitly_wait(10)
#driver.get('https://github.com/')
#gitHubSearch = driver.find_element_by_class_name('form-control').send_keys('Selenium', Keys.ENTER)


#10)
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.options import Options
#driver = webdriver.Firefox(executable_path='/Users/adiellevy/Downloads/geckodriver')
#Firefox_Option = Options()
#Firefox_Option.add_argument('---disable-extensions')