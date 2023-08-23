import base64
import os
from datetime import datetime

import pytz
import yaml


class FileUtils:

    @staticmethod
    def get_yaml_data(file_path):
        with open(file_path, "r", encoding='utf-8') as f:
            file = yaml.load(f, Loader=yaml.FullLoader)
        return file

    @staticmethod
    def get_actual_date_time(formato_fecha, time_zone='America/Buenos_Aires'):
        return datetime.now(pytz.timezone(time_zone)).strftime(formato_fecha)

    @staticmethod
    def get_file_data(file_path):
        with open(file_path, "r", encoding='utf-8') as f:
            lines = f.read()
        return lines

    @staticmethod
    def get_file_in_b64(file_path):
        result = {}
        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as f:
                    content = f.read()
                    if content.strip():
                        b64_content = base64.b64encode(content)
                        result['file_name'] = f.name.split('/')[-1]
                        result['content_base64'] = b64_content.decode('UTF-8')
                        return result
                    else:
                        print('Empty File skipped: ' + file_path)
            finally:
                f.close()
        else:
            print('Directory skipped: ' + file_path)

    @staticmethod
    def get_files_from_dir_in_b64(dir_path):
        files = os.listdir(dir_path)
        results = []
        for file in files:
            file_path = dir_path + "/" + file
            results.append(FileUtils.get_file_in_b64(file_path))
        return results
