from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org")

    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys("Immanuel Kant")
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)
    first_result = driver.find_element(By.CSS_SELECTOR, "ul.mw-search-results li a")
    first_result.click()

    time.sleep(2)
    title = driver.title
    print("Título da página:", title)

    # pega o texto principal do artigo (div id="mw-content-text")
    content_div = driver.find_element(By.ID, "mw-content-text")
    paragraphs = content_div.find_elements(By.TAG_NAME, "p")
    article_text = "\n".join([p.text for p in paragraphs if p.text.strip() != ""])

    with open("artigo_kant.txt", "w", encoding="utf-8") as f:
        f.write(title + "\n\n")
        f.write(article_text)

    driver.quit()
