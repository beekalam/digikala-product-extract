from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

from DigikalaProduct import DigikalaProductExtract
from helpers import has_product, insert_product


def get_chrome():
    options = Options()
    options.binary_location = r'd:\opt\bin\chromedriver.exe'
    options.add_argument('--headless')
    # options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    # set the window size
    # options.add_argument('window-size=1200x600')
    options.add_argument("--remote-debugging-port=9222")
    chromeBrowser = webdriver.Chrome(executable_path=r'd:\opt\bin\chromedriver.exe')
    return chromeBrowser


chromeBrowser = get_chrome()
for i in range(109, 10000):
    if has_product(i):
        continue
    try:
        dk = DigikalaProductExtract(chromeBrowser, i)
        dk.visit()
        if dk.visit_success():
            product = dk.get_product()
            insert_product(product)
    except EOFError as exs:
        print("ssssssssssssssssssssss:", exs.msg)
    except WebDriverException as ex:
        print("ex: ", ex.msg)

chromeBrowser.quit()
