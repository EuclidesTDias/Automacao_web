import unittest, allure, unittest, base64, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWailt
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionsChains
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from os import environ

class PageHelper(unittest.TestCase):
    # BROWSER = environ.get("BROWSER")
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-site-isolation-trials')
    options.add_argument('--incognito')
    options.add_argument('--start-maximized')
    options.add_argument('--ignore-certificate-errors')

    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--incognito')
    # options.add_argument('--window-size=1200x680')
    # options.add_argument('--disable-site-isolation-trials')
    
    driver = webdriver.Chrome(chrome_options=options)
    global DELAY
    DELAY = 10 # segundos
    # try:
          # assert BROWSER ! = ""
          # if BROWSER == "Chrome":
          #     options = webdriver.ChromeOptions()
          #     options.add_argument('--disable-site-isolation-trials')
          #     options.add_argument('--incognito')
          #     options.add_argument('start-maximized')
          #     options.add_argument('--ignore-certificate-erros')
          #     driver = webdriver.Chrome(options=options)
          # elif BROWSER == "Edge":
          #     edge_options = webdriver.EdgeOptions()
          #     edge_options.add_argument('--start-maximized')
          #     edge_options.add_argument('--incognito')
          #     edge_options.add_argument('ignore-certificte-errors')
          #     driver = webdriver.Edge(options=options)
  # except Exeption:
      #  raise Exception("\n\n[Error]) - Você precisa escolher um browser.\nEscolha entre: Chrome, Firefos e Edge")
 
    def pausa_test(self):
        print("Printed immediately.")
        time.sleep(5)
        print("Printed after 5 secunds.")
    
    # Fechar o browser
    def browser_quit(self):
        self.driver.quit()
    
    # Limpa o browser
    def browser_clear(self):
        self.driver.delete_all_cookies()
        # self.driver.refresh()
    
    def screenshot_page(self):
        dh_atuais   = datetime.now()
        data        = dh_atuais.strftime('%y-%m-%d')
        h_m_s       = dh_atuais.strftime("%H-%M-%S-%p")
        screen_path = "reports\\evidencias\\{}.png".format(data + h_m_s)
        self.driver.save_screenshot(screen_path)
        allure.attach(self.driver.get_screenshot_as_png(), nome="Screenshot", attachment_type=AttachmentType.PNG)
        return screen_path

    def find_by_css(self, locator):
        # aguarda elemento estar visivel na tela
        WebDriverWailt(self.driver, self.DELAY).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        try:
            WebDriverWailt(self.driver, self.DELAY).until(ec.presence_of_element_located((By.CSS_SELECTOR, locator)))
            # retorna elemento
            return self.driver.find_element(By.CSS_SELECTOR, locator)
        except TimeoutException:
            print("O carregamento da pagina esta mior que {}-segundo".format(DELAY))
    
    def find_by_xpath(self, xpath):
        WebDriverWailt(self.driver, self.DELAY).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        try:
            WebDriverWailt(self.driver, self.DELAY).until(ec.presence_of_element_located((By.XPATH, xpath)))
            # retorna elemento
            return self.driver.find_element(By.XPATH, xpath)
        except TimeoutException:
            print("O carregamento da pagina esta mior que {}-segundo".format(DELAY))
    
    def click_by_text(self, elemento, texto):
        #WebDriverWailt(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        xpath = "//{}[text()='{}']".format(elemento, texto)
        WebDriverWailt(self.driver, self.DELAY).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        try:
            WebDriverWailt(self.driver, self.DELAY).until(ec.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutError:
            print("O carregamento da pagina esta maior que {}-segundos").format(DELAY)
        WebDriverWailt(self.driver, self.DELAY).until(ec.element_to_be_clickable((By.XPATH, xpath))).click()
    
    def element_execute_script(self, locator):
        self.driver.execute_script(locator)

    def abrir_url(self, base_url):
        # acessa url
        self.browser_clear()
        self.driver.get(base_url)
    
    def get_text_element_page(self, locator):
        WebDriverWailt(self.driver, self.DELAY).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        try:
            WebDriverWailt(self.driver, self.DELAY).until(ec.presence_of_element_located((By.CSS_SELECTOR, locator)))
            # retorna elemento
            return self.driver.find_element(By.CSS_SELECTOR, locator).text
        except TimeoutException:
            print("O carregamento da pagina esta mior que {}-segundo".format(DELAY))
    
    def page_contains_texto(self, texto):
        xpath = "//*[contains(text(), '{}')]".format(texto)
        WebDriverWailt(self.driver, self.DELAY).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        try:
            WebDriverWailt(self.driver, self.DELAY).until(ec.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutError:
            print("O texto [{}], não foi encontrado!").format(DELAY)

    def assert_equals_texto(self, texto, locator):
        texto_page = self.get_text_element_page(locator)
        print(texto_page)
        print(texto)
    
    def page_contains_texto_login(self,texto):
        str(texto) in self.driver.page_source
        try:
            self.driver.page_source().contains(texto)
        except Exception:
            return False
    
    def element_enabled_page(self, locator, xpath):
        WebDriverWailt(self.driver, self.DELAY).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        try:
            WebDriverWailt(self.driver, self.DELAY).until(ec.presence_of_element_located((By.CSS_SELECTOR, locator)))
            # retorna elemento
            return self.driver.find_element(By.CSS_SELECTOR, locator).text
        except TimeoutException:
            print("O carregamento da pagina esta maior que {}-segundos".format(DELAY))
        
        


