# Import bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

szukaj = "apap"
firstname = "Ala"
lastname = "Kot"
telephone = "000000000"
email = "kotek@kot.pl"

class ShoppingAptelinePage:
    All_Categories = "//*[@id='menu-list']/li[1]/a"
    Cosmetics = "//*[@id='menu-list']/li[1]/div/ul/li[13]/a"
    Cookies = "//*[@id='notice-cookie-block']/div/div/p[2]/button"
    Product_1 = "//*[@id='content-main']/div/div[2]/div/div[2]/ul/li[1]/div/div[2]/p/a"
    AddToCart_1 = "//*[@id='product_addtocart_button_1603']"
    Woje = "//*[@id='pharmacy-state']"
    City = "//*[@id='pharmacy-city']"
    Pharmacy_Name = "//*[@id='pharmacy-name']"
    Submit = "//*[@id='modalDescription']/div/div[2]/div[2]/div/div[2]/button"
    Close = "/html/body/div[2]/div/div/button"
    Continue = "/html/body/div[3]/div/div/div/section[3]/button[1]"
    Search = "//*[@id='search']"
    Submit_2 = "//*[@id='search_mini_form']/div[1]/div/span[2]/button"
    AddToCart_2 = "//*[@id='product_addtocart_form']/button"
    Submit_3 = "/html/body/div[3]/div/div/div/section[3]/button[2]"
    Order = "//*[@id='content-main']/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/ul/li/button"
    Registration = "//*[@id='login']"
    FirstName = "//*[@id='billing.firstname']"
    LastName = "billing.lastname"
    Email = "//*[@id='billing.email']"
    Telephone = "billing.telephone"
    Continue_2 = "//*[@id='billingForm']/div/div[1]/form/div[2]/button"
    WrongNumber = "//*[@id='billingForm']/div/div[1]/form/div[1]/div[5]/span"
    CheckBox = "//*[@id='billingForm']/div/div[1]/form/div[1]/div[6]/div[1]/ul/li[1]/span[2]"




class BaseTestHome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://apteline.pl/")
        self.driver.implicitly_wait(15)

    def test_ShoppingAndRegistrationPage(self):
        driver = self.driver
        # Zanajdź zakładkę "wszystkie kategorie"
        driver.find_element(By.XPATH, ShoppingAptelinePage.All_Categories).click()
        # Kliknij kosmetyki i dermokospemetyki
        driver.find_element(By.XPATH, ShoppingAptelinePage.Cosmetics) .click()
        sleep(2)
        # Zaakceptuj pliki cookies
        driver.find_element(By.XPATH, ShoppingAptelinePage.Cookies) .click()
        # Dodaj produkt nr 1 do koszyka
        driver.find_element(By.XPATH, ShoppingAptelinePage.Product_1) .click()
        driver.find_element(By.XPATH, ShoppingAptelinePage.AddToCart_1).click()
        # Wybór apteki
        woj = Select(driver.find_element(By.XPATH, ShoppingAptelinePage.Woje))
        woj.select_by_value('mazowieckie')
        sleep(1)
        # Wybór miasta
        city = Select(driver.find_element(By.XPATH, ShoppingAptelinePage.City))
        city.select_by_value('Warszawa')
        sleep(1)
        # Wybór adresu
        adresapteki = Select(driver.find_element(By.XPATH, ShoppingAptelinePage.Pharmacy_Name))
        adresapteki.select_by_value('7711')
        sleep(1)
        # Kliknij Wybierz
        driver.find_element(By.XPATH, ShoppingAptelinePage.Submit) .click()
        sleep(2)
        # Zamknij okno z wyborem
        driver.find_element(By.XPATH, ShoppingAptelinePage.Close) .click()
        sleep(3)
        # Kliknij "kontynuuj zakupy"
        driver.find_element(By.XPATH, ShoppingAptelinePage.Continue). click()
        sleep(5)
        # Wyszukaj produkt
        szukaj_input = driver.find_element(By.XPATH, ShoppingAptelinePage.Search)
        szukaj_input.send_keys(szukaj)
        driver.find_element(By.XPATH, ShoppingAptelinePage.Submit_2) .click()
        sleep(3)
        # Dodaj Apap do koszyka
        driver.find_element(By.XPATH, ShoppingAptelinePage.AddToCart_2) .click()
        # Złóż zamówienie
        driver.find_element(By. XPATH, ShoppingAptelinePage.Submit_3) .click()
        # Zamów
        driver.find_element(By.XPATH, ShoppingAptelinePage.Order) .click()
        # Zamów bez rejestracji
        driver.find_element(By. XPATH, ShoppingAptelinePage.Registration) .click()
        sleep(2)
        # Wpisz imię
        wpisz_imie = driver.find_element(By.XPATH, ShoppingAptelinePage.FirstName)
        wpisz_imie.send_keys(firstname)
        sleep(2)
        #Wpisz nazwisko
        wpisz_nazwisko = driver.find_element(By.ID, ShoppingAptelinePage.LastName)
        wpisz_nazwisko.send_keys(lastname)
        sleep(2)
        #Wpisz e-mail
        wpisz_email = driver.find_element(By.XPATH, ShoppingAptelinePage.Email)
        wpisz_email.send_keys(email)
        #Wpisz telefon
        wpisz_telefon = driver.find_element(By.ID, ShoppingAptelinePage.Telephone)
        wpisz_telefon.send_keys(telephone)
        sleep(2)
        #Kontynuuj
        driver.find_element(By.XPATH, ShoppingAptelinePage.Continue_2) .click()
        # Niepoprawny numer telefonu
        error_info = driver.find_element(By.XPATH, ShoppingAptelinePage.WrongNumber).text
        self.assertEqual("Numer telefonu jest niepoprawny.", error_info)
        sleep(5)
        # Brak akceptacji regulaminu
        error_info2 = driver.find_element(By. XPATH, ShoppingAptelinePage.CheckBox).text
        self.assertEqual("To pole jest wymagane.", error_info2)








    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
        unittest.main()