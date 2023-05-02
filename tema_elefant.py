import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""Intrati pe site-ul https://www.elefant.ro/ si efectuati urmatoarele teste:

- Test 1: Identificati butonul "accept cookies" si dai click pe el
- Test 2: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate 
([class="product-title"])
- Test 3: Extrageti din lista produsul cu pretul cel mai mic [class="current-price "] -> //img[@class="product-image"]
- Test 4: Extrageti titlul paginii si verificati ca este corect
- Test 5: Intrati pe site, accesati butonul cont si click pe conectare.Identificati elementele de tip user si parola si
 inserati valori incorecte (valori incorecte inseamna oricare valori care nu sunt recunscute drept cont valid)
- Dati click pe butonul "conectare" si verificati urmatoarele:
            1. Faptul ca nu s-a facut logarea in cont
            2. Faptul ca se returneaza eroarea corecta
- Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@"), fara sa 
introduceti si parola si verificati faptul ca butonul "
" este dezactivat"""

"""This module provides functionality to check multiple data from a web page."""


class Elefant(unittest.TestCase):
    COOKIES = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    SEARCH_BAR = (By.XPATH, '//*[@id="HeaderRow"]/div[4]/div/div[1]/form/input[1]')
    TITLE = (By.XPATH, '/html/head/title/text()')
    CONT = (By.XPATH, '//*[@id="HeaderRow"]/div[4]/div/ul/li[1]/a[1]/div/span[2]')
    CONNECT = (By.XPATH, '//*[@id="account-layer"]/a[1]')
    USER = (By.CSS_SELECTOR, 'input[placeholder="Email"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[placeholder="Parola"]')
    CONNECT1 = (By.XPATH, "//div[@id='xpath-content']")
    ERROR_MSJ = (By.XPATH, '//*[@role="alert"]')
    INVALID_LOGIN = (By.CLASS_NAME, 'alert alert-danger')
    CONNECT_BTN = (By.XPATH, '/html/body/div[2]/div/div[9]/div[1]/div/div[1]/div/form/div[4]/div/button')
    BTN_DISPLAYED = (By.XPATH, "//div/button[@disabled='disabled']")
    SEARCH_BTN = (By.XPATH, '//*[@id="HeaderRow"]/div[4]/div/div[1]/form/button/span')
    RESULT = (By.XPATH, '//*[@id="SortingRow"]/div[1]/div')
    ELEMENT_PRICES = (By.CLASS_NAME, 'current-price')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.elefant.ro/')
        self.driver.maximize_window()

    def test1_accept_cookies(self):
        time.sleep(3)
        self.driver.find_element(*self.COOKIES).click()

    def test2_search_item(self):
        self.driver.find_element(*self.COOKIES).click()
        time.sleep(3)
        self.driver.find_element(*self.SEARCH_BAR).send_keys('iphone 14')
        self.driver.find_element(*self.SEARCH_BTN).click()
        results = self.driver.find_elements(By.CLASS_NAME, "product-title")
        assert len(results) >= 10, f'Cautarea a esuat. Au fost gasite doar {len(results)} rezultate.'

    def test3_pret_mic(self):
        self.driver.find_element(*self.cookies).click()
        self.driver.find_element(*self.search).send_keys('iphone 14')
        self.driver.find_element(*self.searchbtn).click()
        time.sleep(4)
        # self.driver.find_element(By.ID, "SortingAttribute").click()
        # self.driver.find_element(*self.cel_mai_mic_pret).click()
        # time.sleep(5)
        sorteaza = Select(self.driver.find_element(By.ID, 'SortingAttribute'))
        time.sleep(3)
        sorteaza.select_by_visible_text("Pret crescator")
        time.sleep(7)

        elemet_prices = self.driver.find_elements(By.CLASS_NAME, 'current-price')
        dict_elemente = {}
        return_elements = self.driver.find_elements(By.CLASS_NAME, 'product-title')
        for i in range(len(return_elements)):
            dict_elemente[return_elements[i].text] = elemet_prices[i].text.replace(".", "").replace(",", "").replace(
                " lei", "")[:-3]
        min_price = 99999999999999
        prod_min = ""
        for key, value in dict_elemente.items():
            min_price = value
            prod_min = key
        print(f'Produsul cu cel mai mic pret este: {prod_min} si valoarea de {min_price} lei')
    def test4_title(self):
        self.assertEqual(self.driver.title, 'elefant.ro - mallul online al familiei tale! •'
                                            ' Branduri de top, preturi excelente • '
                                            'Peste 500.000 de produse pentru tine!')

    def test5_invalid_connect(self):
        self.driver.find_element(*self.COOKIES).click()
        time.sleep(3)
        self.driver.find_element(*self.CONT).click()
        self.driver.find_element(*self.CONNECT).click()
        self.driver.find_element(*self.USER).send_keys('abc@gmail.com')
        self.driver.find_element(*self.PASSWORD).send_keys('123')
        self.driver.find_element(*self.CONNECT_BTN).click()
        invalid_user = False
        self.assertEqual(self.ERROR_MSJ == self.INVALID_LOGIN, invalid_user)

    def test6(self):
        time.sleep(3)
        self.driver.find_element(*self.COOKIES).click()

        time.sleep(3)
        self.driver.find_element(*self.CONT).click()
        self.driver.find_element(*self.CONNECT1).click()
        time.sleep(3)
        self.driver.find_element(*self.USER).send_keys('abc@gmail.com')
        self.driver.find_element(*self.USER).clear()
        self.driver.find_element(*self.USER).send_keys('abcgmail.com')
        time.sleep(3)
        self.assertTrue(self.BTN_DISPLAYED, True)

    def tearDown(self) -> None:
        self.driver.quit()
