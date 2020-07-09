from selenium import webdriver
import urllib
from tqdm import tqdm
#Chrome driver is required
#Selenium is required
#install tqdm progress bar library

path = 'chromedriver.exe'
page_start = '421'
driver = webdriver.Chrome(executable_path=path)
driver.get('https://xkcd.com/' + page_start + '/')

currentURL = ""

#while(currentURL != "https://xkcd.com/1/#"):

for i in tqdm(range(int(page_start))):
    #find img by xpath
    img = driver.find_element_by_xpath('//*[@id="comic"]/img')
    #find name of img by src attribute
    src = img.get_attribute('src')
    #download img to Image folder while removing prefix of src attribute
    urllib.urlretrieve(src, 'Images/'+src[29:])
            
    #Finding previous button on page and clicking it
    driver.find_element_by_xpath('//*[@id="middleContainer"]/ul[1]/li[2]/a').click()
    currentURL = driver.current_url

driver.close()
print('finished')

