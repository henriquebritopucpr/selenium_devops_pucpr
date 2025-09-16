from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

def make_driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=opts)

def run(term: str = "Immanuel Kant", out_path: str = "artigo_kant.txt"):
    driver = make_driver()
    wait = WebDriverWait(driver, 15)
    try:
        driver.get("https://www.wikipedia.org")

        search_box = wait.until(EC.presence_of_element_located((By.ID, "searchInput")))
        search_box.send_keys(term)
        search_box.send_keys(Keys.RETURN)

        try:
            first_link = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.mw-search-results li a"))
            )
            if first_link:
                first_link[0].click()
        except Exception:
            pass

        content_div = wait.until(EC.presence_of_element_located((By.ID, "mw-content-text")))
        title = driver.title

        paragraphs = content_div.find_elements(By.TAG_NAME, "p")
        article_text = "\n".join(p.text for p in paragraphs if p.text.strip())

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(title + "\n\n")
            f.write(article_text)

        print(f"[ok] salvo em: {out_path}")
        return title
    finally:
        driver.quit()

if __name__ == "__main__":
    term = sys.argv[1] if len(sys.argv) > 1 else "Immanuel Kant"
    out = sys.argv[2] if len(sys.argv) > 2 else "artigo_kant.txt"
    run(term, out)
