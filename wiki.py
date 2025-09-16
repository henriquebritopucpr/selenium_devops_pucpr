from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org")

    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys("Immanuel Kant")
    search_box.send_keys(Keys.RETURN)

    driver.quit()
