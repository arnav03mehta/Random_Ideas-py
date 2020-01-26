from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class LoginBot :
    
    def __init__(self,username,password) :
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        
    def login(self) :
        bot = self.bot
        bot.get('') #url here
        time.sleep(3)
        username = bot.find_element_by_name('') #username input field here
        password = bot.find_element_by_name('') #password input field here
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

log = LoginBot('opbms','opstudent')
log.login()
