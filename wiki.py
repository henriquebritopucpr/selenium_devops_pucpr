from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org")

    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys("Immanuel Kant")
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)
    first_result = driver.find_element(By.CSS_SELECTOR, "ul.mw-search-results li a")
    first_result.click()

    time.sleep(2)
    print("Título da página:", driver.title)

    driver.quit()
