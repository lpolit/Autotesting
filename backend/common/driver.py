from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import ChromeOptions
from selenium.webdriver import EdgeOptions
from selenium.webdriver import FirefoxOptions

from common.file_utils import FileUtils


class Driver:
    def get_driver(self, browser, headless):
        try:
            driver_class, options_class = self.driver_broker(browser)
            options = self.browser_options(headless)[browser]
            service = webdriver.ChromeService(executable_path="chromedriver.exe")
            driver = webdriver.Chrome(service=service, options=options)
            # web_driver = driver_class(service=service)
            return driver
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




    def chrome_options(self, headless):
        options = ChromeOptions()
        options.add_argument("--headless==new") if headless else None
        options.add_argument("--ignore-certificate-errors")
        return options


    def firefox_options(self, headless):
        options = FirefoxOptions()
        options.add_argument("-headless") if headless else None
        options.add_argument("--ignore-certificate-errors")
        return options


    def edge_options(self, headless):
        options = EdgeOptions()
        options.add_argument("--headless==new") if headless else None
        options.add_argument("--ignore-certificate-errors")
        return options