
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By 


######################################################
#########OPEN BROWSER AND LOGIN#######################
######################################################
driver = webdriver.Chrome('/Users/suneethi/Desktop/chromedriver')
driver.get('https://sprolive.theservicepro.net/login.aspx')

id_box = driver.find_element_by_name('txtUserName')
id_box.send_keys('clinton.ford@callnorthwest.com')

pass_box = driver.find_element_by_name('txtPassword')
pass_box.send_keys('Nashville@1')

login_button = driver.find_element_by_name('btnLogin')
login_button.click()

########################################################
########################################################


#######################################################
############### Account List ##########################
#######################################################
List = [2063721, 2779663, 2794245, 3099234]

# INPUT ACCOUNT

for i in List:

	search_box = driver.find_element_by_name('_ctl0:body:salelproControl:txtSearchCriteria')
	search_box.send_keys(i)


	##### Setup wait for later #####
	wait = WebDriverWait(driver, 30)

	##### Store the ID of the original window ######
	original_window = driver.current_window_handle	

	### Check we don't have other windows open already ###
	assert len(driver.window_handles) == 1

	##### CLICKS SEARCH BUTTON ##########
	class_select = driver.find_element_by_id('search_button')
	class_select.click()

	######################
	# START ON SECOND TAB
	######################
	# Wait for the new window or tab
	wait.until(EC.number_of_windows_to_be(2))


	# Loop through until we find a new window handle
	for window_handle in driver.window_handles:
		if window_handle != original_window:
			driver.switch_to.window(window_handle)
			break


	 
	###### CLICKS ADD NOTE ######
	select_note = driver.find_element_by_id('Accountmenu1_lnk_1060')
	select_note.click()

	#time.sleep(20)
	#delay = 10
	wait = WebDriverWait(driver, 30)

	try:
		element = WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.ID, "txtNote_ifr"))
			)
			#### TYPES NOTE ######					
		note_box = driver.find_element_by_id('txtNote_ifr')
		note_box.send_keys(' Emailed Sent Renewal info')
	except:
		driver.quit()

	#### TYPES NOTE ######					
	#note_box = driver.find_element_by_id('txtNote_ifr')
	#note_box.send_keys(' test')

	wait = WebDriverWait(driver, 30)

	# CLICKS ADD NOTE BUTTON
	ok_note = driver.find_element_by_id('hlOk_46')
	ok_note.click()

	#CLOSE TAB
	driver.close()

	# FOCUS BACK ON MAIN TAB
	driver.switch_to.window(original_window)






