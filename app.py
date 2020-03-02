from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import sys
import config

from DigikalaProduct import DigikalaProductExtract
from helpers import has_product, insert_product


def get_chrome():
    options = webdriver.ChromeOptions()
    # options.binary_location = CHROME_DRIVER_PATH
    # set the window size
    # options.add_argument('window-size=1200x600')
    # options.add_argument("--remote-debugging-port=9222")
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    options.add_argument("user-agent=mozilla")
    chromeBrowser = webdriver.Chrome(executable_path=config.chrome_driver_path, chrome_options=options)
    return chromeBrowser


chromeBrowser = get_chrome()
for i in range(1, 10000):
    if has_product(i):
        continue
    try:
        dk = DigikalaProductExtract(chromeBrowser, i)
        dk.visit()
        if dk.visit_success():
            product = dk.get_product()
            insert_product(product)
    except EOFError as exs:
        print("error:", exs.msg)
    except WebDriverException as ex:
        print("ex: ", ex.msg)
    if i % 10 == 0:
        sys.stdout.flush()
chromeBrowser.quit()
