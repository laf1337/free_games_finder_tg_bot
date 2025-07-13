import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
options = Options()

options.add_argument("--headless=new")  # для новых версий Chrome (109+)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

def sale_massage_parser():
    driver = uc.Chrome()
    result = f""
    count = 0
    for page in range(1,6):  # you can change for ur count of pages
        driver.get(f"https://gg.deals/games/?page={page}")
        time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        data = soup.find_all("div", class_="game-info-wrapper d-flex column-wrapper")
        for game_collum in data:
            # находим название
            game_title = game_collum.find("div", class_="game-info-title title")
            game_name = game_title.find("a", class_="title-inner").text
            # находим цену 
            game_pricedata = game_collum.find("div", class_="shop-price-wrapper shop-price-all")
            sale_tag = game_pricedata.find("span", class_="discount label") if game_pricedata else None
            game_sale = sale_tag.text if sale_tag else "no discount"
            # get platform name
            game_platform = game_collum.find("span", class_="game-store-name") if game_collum else None
            platform_name = game_platform.text if game_platform else "None"
            if game_sale == "-100%":
                result += f"Игра <b> {game_name} </b> Успей забрать в <b>{platform_name}</b>!\n"
                count += 1
        time.sleep(2)
    if count == 0:
        result += f"К сожалению на данный момент нет беспалтных игр :("
    driver.quit()
    return result

