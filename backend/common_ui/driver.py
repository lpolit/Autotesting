from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import EdgeOptions

class Driver:
    def get_driver(self, browser, headless):
        try:
            driver_class, options_class = self.driver_broker(browser)
            options = self.browser_options(headless)[browser]
            web_driver = driver_class(options=options)
            return web_driver
        except WebDriverException as ex:
            raise WebDriverException("WDM no llega a Internet. HTTPS_PROXY este seteada correctamente?", ex)


    def driver_broker(self, browser):
        """Funcion que interactua con la librera WDM para buscar el driver y tener un solo punto de fallo"""
        return {
            "chrome": (webdriver.Chrome, ChromeOptions),
            "firefox": (webdriver.Firefox, FirefoxOptions),
            "edge": (webdriver.Edge, EdgeOptions)
        }[browser]


    def browser_options(self, headless):
        return {"chrome": self.chrome_options(headless),
                "firefox": self.firefox_options(headless),
                "edge": self.edge_options(headless)
                }


    def multi_options(self, option_class, headless):
        options = option_class()
        options.headless = eval(headless)
        options.accept_insecure_certs = True
        return options


    def chrome_options(self, headless):
        return self.multi_options(ChromeOptions, headless)


    def firefox_options(self, headless):
        return self.multi_options(FirefoxOptions, headless)


    def edge_options(self, headless):
        return self.multi_options(EdgeOptions, headless)