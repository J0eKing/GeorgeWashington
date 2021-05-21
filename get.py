from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

link = r"https://www.epicgames.com/store/en-US/free-games"
link_prefix = r"https://www.epicgames.com"


def get_html(link):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--remote-debugging-port=6667")

    driver = webdriver.Firefox()
    driver.get(link)

    html = driver.page_source
    driver.close()
    return html


def save_html(data):
    with open("game", "w+") as f:
        f.write(data)


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.findAll(lambda tag: tag.name ==
                         "span" and "Free Now" in tag.text)[0]

    item = items.findAll('span', {'data-testid': "offer-title-info-title"})
    item = item[0]
    name = item.getText()

    link = items.findAll('a', {'role': "link"})[0]
    link = link["href"]
    # save_html(html)
    #print(name, link)
    print(name, link)
    return [name, link_prefix + link]


def read_html():
    with open("game.html", "r") as f:
        return f.read()


def main():
    htm = get_html(link)
    return parse_html(htm)
