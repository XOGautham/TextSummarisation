import os
from pathlib import Path
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        Download the file from the source URL and save it locally under the 
        specified root directory.
        """
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(url = self.config.source_URL,
                                       filename = self.config.local_data_file)
            logger.info(f"{filename} Download with following info : \n{header} \nDownloaded {get_size(Path(self.config.local_data_file))}")
        else:
            logger.info(f"{self.config.local_data_file} already exists. \nSize : {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extract the zip file to the specified root directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)