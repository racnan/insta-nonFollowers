#Import Libraries 
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

USERNAME = ""
PASSWORD = ""

def Visit_Profile():
    browser.get("https://www.instagram.com")
    sleep(3)

    #Enter Username
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(USERNAME)

    #Enter Password
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(PASSWORD)

    #Click on login button
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]").click()

    #Wait for the page to load
    sleep(5)

    #Click on not Now
    browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()

    #Vist Profile
    browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img").click()
    sleep(2)

def Get_Followers():
    #Click on followers 
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
    sleep(2)
    
    #Follower_box stores the small window that displays followers
    Follower_box = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]")

    #Loop for scrolling the followers window
    Scroll_Height, Previous_Height = 0,0
    while True:
        #This returns the scroll height which is updated after every scroll
        Scroll_Height = browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight; return arguments[0].scrollHeight",Follower_box)
        
        #If the scroll height is same as previous iteration i.e. bottom window is reached, loop is ended
        if Previous_Height == Scroll_Height:
            break
        
        Previous_Height = Scroll_Height
        
        #delay after every scroll for loading
        sleep(1)
    
    #Follwer names are extracted
    Followers_a = Follower_box.find_elements_by_tag_name('a')
    Followers = [Names.get_attribute('title') for Names in Followers_a if Names.get_attribute('title') != '' ]

    #Follower window is closed
    browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()

    return Followers

def Get_Following():
    #Click on Following
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
    sleep(2)
    
    #Following_box stores the small window that displays followers
    Following_box = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]")

    #Loop for scrolling the following window
    Scroll_Height, Previous_Height = 0,0
    while True:
        #This returns the scroll height which is updated after every scroll
        Scroll_Height = browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight; return arguments[0].scrollHeight",Following_box)
        
        #If the scroll height is same as previous iteration i.e. bottom window is reached, loop is ended
        if Previous_Height == Scroll_Height:
            break
        
        Previous_Height = Scroll_Height
        
        #delay after every scroll for loading
        sleep(1)
    
    #Following names are extracted
    Following_a = Following_box.find_elements_by_tag_name('a')
    Following = [Names.get_attribute('title') for Names in Following_a if Names.get_attribute('title') != '' ]

    #Following window is closed
    browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()

    return Following

Visit_Profile()
Followers = Get_Followers()
Following = Get_Following()

Non_Followers = [Names for Names in Following if Names not in Followers]

print("Number of Unfollowers :",len(Non_Followers))
print(Non_Followers)