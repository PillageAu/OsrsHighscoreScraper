#OSRS Highscore Scraper -Version 0.1 -
#made by Brad @ https://cobba.com.au

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#loads osrs.com in chrome
driver = webdriver.Chrome()
driver.get ("https://oldschool.runescape.com/")


#finds the cookies button and clicks accept
button = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll");
driver.implicitly_wait(2)
button.click();
print('Cookies Accepted')

#finds the highscores button and clicks
button = driver.find_element(By.ID, "osnav-hiscores");
driver.implicitly_wait(2)
button.click();
print('Highscores Loaded')
time.sleep(100)

