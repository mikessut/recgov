from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
from secrets import *



recapta_key = "6LdBIvUZAAAAAM02b8GWJew_1LffQJo9rNB5yVTU"

driver = webdriver.Chrome()

# cookies = json.load(open('cookies.json', 'r'))

driver.get("https://recreation.gov")
driver.fullscreen_window()
driver.find_element(By.XPATH, "//button[@aria-label='Sign Up or Log In']").click()

driver.find_element(By.XPATH, "//input[@name='email']").send_keys(UN)
driver.find_element(By.XPATH, "//input[@type='password']").send_keys(PW)

driver.find_element(By.XPATH, "//button[@type='submit']").click()

# reCAPTUA ref: https://habr.com/en/articles/898198/
# driver.execute_script("grecaptcha.enterprise.execute();")
# recapta_response = driver.execute_script(f"return grecaptcha.enterprise.getResponse();")

# driver.get('https://google.com')
# rc_token = driver.execute_script(f"return window.sessionStorage.getItem('rc::c');")

# driver.get("https://recreation.gov")

# driver.execute_script(f"window.localStorage.setItem('recaccount', '{open("localstorage.raw").read()}');")

# for c in cookies:
#     driver.add_cookie(c)


# # save cookies
# with open('cookies.json', 'w') as fid:
#     json.dump(driver.get_cookies(), fid)

# # save local storage
# with open("localstorage.raw", "w") as fid:
#     fid.write(driver.execute_script(f"return window.localStorage.getItem('recaccount');"))

# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
