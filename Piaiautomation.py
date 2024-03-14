# In this function for full access of piai you have to login in piai. firstly logged in and then used it
# For login firstly turn headless to False from true and change first sleep(3) to sleep(3000) so you can login calmly.
# Login with Facebook id..
# Then Use and Enjoy Thank You 😊
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pathlib
ScriptDir = pathlib.Path().absolute()
import pyautogui
import warnings
warnings.simplefilter('ignore')


url =  "https://pi.ai/talk" # website url 
chrome_option = Options() 
chrome_option.headless = True # For process work in backend
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2' # This is User agent id we are using it because to  feel its a human not selenium visiting website
chrome_option.add_argument(f"user-agent={user_agent}") # user agent
chrome_option.add_argument('--profile-directory=Default') # Default directory 
chrome_option.add_argument(f'user-data-dir={ScriptDir}\\chromedata') # This is for save our login data always by default selenium don't save anything what we do. but we have to..
service = Service(ChromeDriverManager().install()) # This will install chrome driver automatically you don't have to install it
driver = webdriver.Chrome(service=service,options=chrome_option) # Giving values to driver inshot driver is ready with this we can automate piai 
driver.maximize_window() # maximize window
driver.get(url=url) 
sleep(3) # sleep for 3 sec to load the website for error free programm

def Websiteopener(): # This programe also work as sleep function this function indicate us that AI is ready to go no error 
    while True:
     try:
        xPATH = "/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div/textarea" 
        driver.find_element(by=By.XPATH,value=xPATH)
        break
     
     except:
        pass
Websiteopener()
print("AI : IS READY TO GO!!") # AI IS READY TO GO

def Voice(): # This function activates the piai voice because its by default off so we have to on it
   
    Xpath = "/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div/textarea" # Text area xpath
    Query = "Hello!!" # Type Hello
    driver.find_element(by=By.XPATH,value=Xpath).send_keys(Query) # Send to websites textarea box
    
    sleep(1) # Sleep for a second !!
    
    xPATH2 = "/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button" # Send button xpath
    driver.find_element(by=By.XPATH,value=xPATH2).click() # Click on Send Button to send our query to piai
    
    sleep(1) # Sleep for a second !!
    
    Xpath1 = "/html/body/div/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button" # Voice button xpath
    driver.find_element(by=By.XPATH,value=Xpath1).click() # This button activates piai voice so in this program we don't need speechrecognition this piai speaks itself and i swear you gonna love it !!

Voice() # Call Voice function
sleep(4) # Sleep for 4 seconds

def sendmessage(Query): # This function send query to piai
   xPATH = "/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div/textarea" # Textarea box xpath
   driver.find_element(by=By.XPATH,value=xPATH).send_keys(Query) # Query will send to textarea
   
   sleep(1) # Sleep for a second !!
   
   xPATH2 = "/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button" # Send Button xpath
   driver.find_element(by=By.XPATH,value=xPATH2).click() # Clicking on send button
   
   sleep(3) # Waiting for piai full reply to scrapp full data

def Resultscrapper(): # This function get data of piai and send to us.
   sleep(1.5) # Sleep for to get data properly
   xpath = "/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/span" # Piai reply xpath
   Text = driver.find_element(by=By.XPATH,value=xpath).text # Picking the reply as a text in Text variable
   sleep(0.5) # Sleep for while
   print(f"AI : {Text}")  # Congrats the data is in your hand !! 

while True:
   Query = input("AI : Ask me what you want.\nYour name : ") # Enter your query what you want ask to piai
   sendmessage(Query=Query) # Your query will send to sendmessage function and this will send to piai
   Resultscrapper() # Last one scrap the piai answer and print it..!!
