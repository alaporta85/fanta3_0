from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
import pickle


f=open('/Users/andrea/Desktop/fanta3_0/Buste/quotazioni/quotazioni.pckl', 'rb')
players_dict = pickle.load(f)
f.close()

os.chdir('/Users/andrea/Desktop/fanta3_0/Buste/quotazioni')
absolute_path = os.getcwd()
chrome_path = absolute_path + '/chromedriver'

url = 'http://leghe.fantagazzetta.com/fantascandalo/lista-svincolati'

browser = webdriver.Chrome(chrome_path)
time.sleep(3)
browser.set_window_size(1400, 800)
browser.get(url)
buttons = browser.find_elements_by_xpath(
					'//ul[@class="nav nav-pills mruoli"]/li/a')

check = -1
rep_play = 0
num_play = 0

for button in buttons:
	check += 1
	browser.execute_script('return arguments[0].scrollIntoView({});'.format(
			'false'), button)
	button.click()
	time.sleep(3)
	table = browser.find_elements_by_xpath(
			'//div[@class="tab-content well well-small"]/div')[check]
	rows = table.find_elements_by_xpath('.//tbody/tr')
	num_play += len(rows)

	for row in rows:
		try:
			name = row.find_element_by_xpath('.//span[@class="steam"]').text
			value = int(row.find_element_by_xpath('.//td[@class="pt"]').text)

			if name not in players_dict:
				players_dict[name] = value
			else:
				rep_play += 1
		except ValueError:
			element = '//a[@href="#next"]'

			next_page = browser.find_elements_by_xpath(element)[check]
			browser.execute_script(
					'return arguments[0].scrollIntoView({});'.format(
							'false'), next_page)
			next_page.click()
			time.sleep(2)
			name = row.find_element_by_xpath(
				'.//span[@class="steam"]').text
			value = int(
				row.find_element_by_xpath('.//td[@class="pt"]').text)

			if name not in players_dict:
				players_dict[name] = value
			else:
				rep_play += 1

browser.quit()

f=open('/Users/andrea/Desktop/fanta3_0/Buste/quotazioni/quotazioni.pckl', 'wb')
pickle.dump(players_dict, f)
f.close()
print(num_play, rep_play)

