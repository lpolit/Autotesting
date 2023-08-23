import base64
import os

from Screenshot import Screenshot as scr

from common_ui.file_utils import FileUtils


class Screenshot:

    def __init__(self, image, screenshot_name):

        self.image = image
        self.screenshot_name = screenshot_name

    def save_to_localfile(self, path=None):
        """path: Es el nombre de la carpeta en donde se van a guardar las imagenes generadas.
        No hace falta que se agregue la "/" al final del nombre. Ej. X.save_to_localfile("Images")"""
        # Esto bloque que devuelve el path hay que llevarlo a feta_core
        # FileUtils en la próxima versión
        if path is not None:
            if not os.path.isdir(path):
                os.mkdir(path)
            path = path + "/"
        else:
            path = ""

        with open(path + self.screenshot_name, "wb") as fh:
            fh.write(self.image)

        return self.screenshot_name

    @staticmethod
    def take_fullpage_screenshot(driver, filename):
        """ take_fullpage_screenshot: Este método toma captura de la pantalla completa.
        (Principio a fin de la página) """
        screenshot_name = Screenshot.get_screenshot_filename(filename)

        if driver.name == 'firefox':
            s = lambda x: driver.execute_script('return document.body.parentNode.scroll' + x)
            driver.set_window_size(s('Width'), s('Height'))
            element = driver.find_element_by_tag_name('body')
            return Screenshot.take_web_element_screenshot(element, filename)
        else:
            ob = scr.Screenshot()
            img_url = ob.full_screenshot(driver, save_path=Screenshot.config_location(), image_name=screenshot_name)
            with open(img_url, "rb") as imageFile:
                img_str = base64.b64encode(imageFile.read())
            os.remove(img_url)
            image = base64.urlsafe_b64decode(img_str)

        return Screenshot(image, screenshot_name)

    @staticmethod
    def take_screenshot(driver, filename):
        """ take_screenshot: Este método toma captura de la pantalla en foco, pero no de la pantalla
        completa (hasta el fondo de la página) """

        screenshot_name = Screenshot.get_screenshot_filename(filename)
        image = driver.get_screenshot_as_png()
        return Screenshot(image, screenshot_name)

    @staticmethod
    def take_web_element_screenshot(element, filename):
        """" take_element_screenshot: Este método toma captura de un WebElement seleccionado """

        screenshot_name = Screenshot.get_screenshot_filename(filename)
        image = element.screenshot_as_png
        return Screenshot(image, screenshot_name)

    @staticmethod
    def take_screenshot_type(driver, filename, type="page"):
        if type == "page":
            return Screenshot.take_screenshot(driver, filename)
        elif type == "full":
            return Screenshot.take_fullpage_screenshot(driver, filename)
        return None

    @staticmethod
    def get_screenshot_filename(filename):
        now = FileUtils.get_actual_date_time("%Y%m%d_%H%M%S")
        return f"{filename}_{now}.png"

    @staticmethod
    def config_location():
        if "FETA_CONFIG_LOCATION" in os.environ:
            _location = os.getenv("FETA_CONFIG_LOCATION")
        elif "VIRTUAL_ENV" in os.environ:
            _SIN_EL_ULTIMO = -1
            _location = os.sep.join(os.getenv("VIRTUAL_ENV").split(os.sep)[:_SIN_EL_ULTIMO])
        else:
            _location = os.getcwd()
        return _location
