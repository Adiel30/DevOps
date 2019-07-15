# 1 A) open chrome
def chrome_url():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Chrome(executable_path="/Users/adiellevy/Downloads/chromedriver")
    driver.implicitly_wait(6)
    driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Ftab%3Drm%26ogbl&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    typeUserName = driver.find_element_by_class_name('VmOpGe')
    typeUserName.send_keys('adiel@newit.co.il',Keys.ENTER)
    typePassword = driver.find_element_by_class_name('Xb9hP')
    typePassword.send_keys('Usf15936',Keys.ENTER)
    newMail = driver.execute_script('argument[0].click;', driver.find_element_by_class_name('T-I J-J5-Ji T-I-KE L3'))
    deliverTo = driver.find_element_by_css_selector('#\:m1')
    deliverTo.send_keys('adiel11.12@gmail.com')
    subject = driver.find_element_by_class_name('#\:mj')
    subject.send_keys('Test')
    textBox = driver.find_element_by_class_name('#\:lg')
    textBox.send_keys('test')
    send = driver.execute_script('argument [0].click;', find_element_by_class_name('#\:mt'))


if __name__ == '__main__':
    print(chrome_url())


