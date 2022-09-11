from linkedin_scraper import Person, actions
from selenium import webdriver
#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path="./chromedriver")

email = "paulbrian883@gmail.com"
password = "B4r4th30n"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/walterjesus/", experiences=[],driver=driver)
#Person(linkedin_url=None, name=None, about=[], experiences=[]
print(person)