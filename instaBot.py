from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import seed
from random import random
import random as rand

smallDelay = 10
mediumDelay = 620
bigDelay = 1040

postUrl=[
	"https://www.instagram.com/p/CHVmYuGsxVA/",
	"https://www.instagram.com/p/CHQd0_Ps91Q/",
]

nLines=[
	2,
	1,
]

def run_bot(username, password,nseed):
	browser = webdriver.Chrome()
	browser.implicitly_wait(5)

	browser.get("https://www.instagram.com/")

	sleep(smallDelay)
	login_button = browser.find_element_by_class_name("bIiDR")
	login_button.click()
	sleep(smallDelay)

	username_input = browser.find_element_by_css_selector("input[name='username']")
	password_input = browser.find_element_by_css_selector("input[name='password']")

	username_input.send_keys(username)
	password_input.send_keys(password)


	login_button = browser.find_element_by_xpath("//button[@type='submit']")
	login_button.click()

	sleep(smallDelay)

	login_button = browser.find_element_by_xpath("//button[@type='button']")
	login_button.click()

	sleep(smallDelay)

	login_button = browser.find_element_by_class_name("HoLwm")
	login_button.click()

	sleep(smallDelay)

	actual=0
	counter=0

	browser.get(postUrl[actual])

	sleep(smallDelay)

	while 1:
		file1 = open("accountsToTag.txt", "r")
		file2 = open("accountsToTag.txt", "r")
		file3 = open("accountsToTag.txt", "r")
		Lines1 = file1.read().splitlines()
		rand.shuffle(Lines1)
		Lines2 = file2.read().splitlines()
		rand.shuffle(Lines2)
		Lines3 = file3.read().splitlines()
		rand.shuffle(Lines3)

		i = 0
		seed(nseed)
		while i < len(Lines1):
			value = rand.randint(mediumDelay, bigDelay)
			print("Rand:",value)
			if(Lines1[i] != Lines2[i] and Lines2[i] != Lines3[i]):
				sleep(smallDelay)
				print("Accounts: ",Lines1[i], Lines2[i], Lines3[i], "\n")
				comment_input = browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']")
				comment_input.click()
				if(nLines[actual]==1):
					browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(Lines1[i], Keys.ENTER)
				if(nLines[actual]==2):
					browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(Lines1[i]," ", Lines2[i], Keys.ENTER)
				if(nLines[actual]==3):
					browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(Lines1[i]," ", Lines2[i]," ", Lines3[i], Keys.ENTER)
				counter=counter+1
				print("Count: ",counter)
			
			actual=(actual+1)%len(postUrl)
			sleep(value)
			browser.get(postUrl[actual])
			i += 1

run_bot("username", "password",1)