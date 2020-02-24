import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers import clean_persian_number


class DigikalaProductExtract:

    def __init__(self, chromeBrowser, product_id: int) -> None:
        self.chromeBrowser = chromeBrowser
        self.product_id = product_id
        self.link = 'https://www.digikala.com/product/dkp-' + str(product_id)
        self.category = ''
        self.name = ''
        self.product_title = ''
        self.seller = ''
        self.price = ''
        self.features = []
        self.success = False

    def has_bread_crumb(self):
        return self.chromeBrowser.find_elements_by_css_selector(
            'div.c-product__nav-container>nav.js-breadcrumb>ul.c-breadcrumb>li')

    def goto_specs(self):
        element = WebDriverWait(self.chromeBrowser, 1).until(EC.presence_of_element_located((By.LINK_TEXT, 'مشخصات')))
        self.chromeBrowser.execute_script('arguments[0].scrollIntoView();', element)
        time.sleep(2)
        element.click()

    def extract_category(self):
        # NameProduct = chromeBrowser.find_elements_by_css_selector(
        #         'article.c-product js-product>section. div.c-product_headline>h1.c-product_title')

        NameProduct = self.chromeBrowser.find_elements_by_css_selector(
            'div.c-product__nav-container>nav.js-breadcrumb>ul.c-breadcrumb>li')
        category = []
        for name in NameProduct:
            name_text = name.text
            if len(name_text) > 0 and name_text.find("روشگاه اینترنتی دیجی") == -1:
                category.append(name_text)
        self.name = category[-1]
        self.category = "-".join(category)

    def extract_attributes(self):
        Attribute = self.chromeBrowser.find_elements_by_css_selector(
            '.c-params> article section>ul.c-params__list li')  # no
        thisatt = {}
        for att in Attribute:
            att1 = att.text.split("\n")
            if len(att1) == 2:
                List = []
                a = att1[0]
                b = att1[1]
                thisatt.get(att1[0])
                thisatt[att1[0]] = att1[1]
                List.append(a)
            else:
                List = []
                List.append(att.text)
                thisatt[a] = List
        self.features = thisatt

    def extract_seller(self):
        if self.chromeBrowser.find_elements_by_css_selector('span.c-product__seller-name'):
            NameSeller = self.chromeBrowser.find_elements_by_css_selector('span.c-product__seller-name')  # no
            Price = self.chromeBrowser.find_elements_by_css_selector('div.c-product__seller-price-raw')  # no
            for sel in NameSeller:
                NameSeller = sel
            for pr in Price:
                Price = pr
            # print(NameSeller.text, Price.text)
            self.seller = NameSeller.text
            self.price = clean_persian_number(Price.text)
        else:
            self.seller = ''
            self.price = ''

    def extract_product_title(self):
        title = self.chromeBrowser.find_elements_by_xpath(
            '//*[@id="content"]/div[1]/div/article/section[1]/div[2]/div[1]/span')
        if len(title)>= 1:
            title = title[0]
            self.product_title = title.text

    def visit(self):
        self.site = self.chromeBrowser.get(self.link)
        if self.has_bread_crumb():
            self.success = True
            self.extract_product_title()
            self.goto_specs()
            self.extract_category()
            self.extract_attributes()
            self.extract_seller()

    def visit_success(self):
        return self.success

    def get_product(self):
        return {"name": self.name, "category": self.category,
                "seller": self.seller, "features": self.features,
                "product_id": self.product_id, "price": self.price, "product_title": self.product_title}
