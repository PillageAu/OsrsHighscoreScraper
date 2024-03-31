#OSRS Highscore Scraper -Version 0.2.0 -
#made by Brad @ https://cobba.com.au

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

#browser config
chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

#loads osrs.com in chrome
driver.get ("https://oldschool.runescape.com/")

#finds the cookies button and clicks accept
Button_Cookies = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll");
Button_Cookies.click();
print('Cookies Accepted')

#finds the highscores button and clicks
LinkHs = driver.find_element(By.ID, "osnav-hiscores");
LinkHs.click();
print('Highscores Loaded')

#finds the highscores tables
HsTable = driver.find_element(By.ID, "contentHiscores");
print(HsTable.text)

file = open('highscores.txt', 'w') 
file.write(HsTable.text) 
file.close() 
print("Saved to /highscores.txt sucessfully")

time.sleep(100)