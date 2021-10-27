from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSc3Wp9C6pR2g4KpPgclcJCsN_U7jdc0rWRLk1R4jkj3uxyUpA/viewform')

time.sleep(1)

# Fill out short answer questions.
shortAnswers = driver.find_elements(By.CSS_SELECTOR, 'input.quantumWizTextinputPaperinputInput')
shortAnswers[0].send_keys('Iammonke#8813')
shortAnswers[1].send_keys('https://github.com/matthewmo6/Introduction_Automation')
shortAnswers[2].send_keys('something')

# Select option 1 multiple choice question.
multipleChoices = driver.find_elements(By.CSS_SELECTOR, 'div.docssharedWizToggleLabeledLabelWrapper')
multipleChoices[1].click()

# Check options 2 and 3 for checkbox question.
checkboxes = driver.find_elements(By.CSS_SELECTOR, 'div.quantumWizTogglePapercheckboxInnerBox')
checkboxes[0].click()
checkboxes[1].click()

dropdown = driver.find_element(By.CSS_SELECTOR, 'div.quantumWizMenuPaperselectEl')
dropdown.click()

time.sleep(1)

dropdown = driver.find_elements(By.CSS_SELECTOR, "div.exportSelectPopup")
dropdown[0].click()

submitbutton = driver.find_element(By.XPATH, '//*[text()=\'Submit\']').click()


time.sleep(10)
driver.close()