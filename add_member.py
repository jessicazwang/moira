import os
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
import time
import getpass
import csv


url = raw_input("Please paste the URL of the webmoira list. ")
data = raw_input("Please enter name of CSV. ")
input_user = raw_input("Kerberos: ")
input_pass = getpass.getpass()

accepted_names = ['Kerberos','Athena','kerberos','athena']

with open(data,'rb') as csvfile:
	reader = csv.reader(csvfile,delimiter=',')
	i=0
	for row in reader:
		if i!=0:
			kerberos = row[3]
			if '@' not in kerberos:
				chromedriver = "/Users/jzwang/Downloads/chromedriver" 
				os.environ["webdriver.chrome.driver"] = chromedriver

				driver = webdriver.Chrome(chromedriver)
				driver.get(url)
				try:
					elem = driver.find_element_by_id("Select").click()
					user = driver.find_element_by_name("j_username")
					password = driver.find_element_by_name("j_password")
					user.send_keys(input_user)
					password.send_keys(input_pass)
					login = driver.find_element_by_name("Submit").click()

					driver.find_element_by_id("member_list_header").click()
					add_member = driver.find_element_by_id("add_member_text")
					time.sleep(3)
					add_member.send_keys(kerberos)
					add_member.send_keys(Keys.RETURN)
					driver.find_element_by_id("add_member_button").click()
					time.sleep(1)

					warning = driver.find_element_by_id("warningOK").click()
				except:
					print kerberos
				finally:
					driver.close()

		i+=1

