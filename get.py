from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

link_prefix = r"https://www.epicgames.com"
link = r"https://www.epicgames.com/store/en-US/"


def get_games():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    chrome_options.add_argument("--remote-debugging-port=6667")  # this
    try:
        #driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Firefox()
        driver.get(link)
        html = driver.page_source

        soup = BeautifulSoup(html, "html.parser")

        driver.close()

        # with open("epic.txt", "w+") as f:
        #    f.write(soup.prettify())

        try:
            item = soup.findAll(
                'a', {'aria-label': lambda x: x and x.startswith('Free Games')}
            )[0]

            curr_name = item["aria-label"]
            curr_name = curr_name[str(curr_name).find(","):]
            curr_name = curr_name[str(curr_name).find(",")+1:]
            curr_name = curr_name[str(curr_name).find(",")+1:]
            curr_name = curr_name[str(curr_name).find(",")+1:]
            curr_name = curr_name[:str(curr_name).find(",")]
            curr_name = str(curr_name).lstrip().rstrip()

            curr_link = link_prefix + item["href"]

        except:
            pass
        next_name = "Mystery Game"
        next_link = "Mystery Game"
        try:
            item2 = soup.findAll(
                'a', {'aria-label': lambda x: x and x.startswith('Free Games')}
            )[1]
            next_name = item2["aria-label"]
            next_name = next_name[str(next_name).find(","):]
            next_name = next_name[str(next_name).find(",")+1:]
            next_name = next_name[str(next_name).find(",")+1:]
            next_name = next_name[str(next_name).find(",")+1:]
            next_name = next_name[:str(next_name).find(",")]
            next_name = str(next_name).lstrip().rstrip()

            next_link = link_prefix + item2["href"]
        except:
            pass

        data = [curr_name, curr_link, next_name, next_link]
        return data
    except:
        return [None]
