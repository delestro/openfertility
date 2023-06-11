"Dataset class for the blasto2k dataset"

import os
import outputformat as ouf
from openfertility.datasets import utils
from openfertility.io.logger import log


class Dataset:
    url = "https://figshare.com/ndownloader/files/39348899"
    name = "blasto2k"
    reference = "https://doi.org/10.1038/s41597-023-02182-3"

    def __init__(self):
        # Labels
        self.target = "EXP_silver"
        self.labels_path = "Gardner_train_silver.csv"
        self.separator = ";"
        
        # Data
        self.data_path = "Images"
        self.data_col = "Image"


    def download(self, force=False):
        # Download dataset

        if os.path.exists(self.dataset_path) and not force:
            log.info("%s already at %s", self.name_bold, self.dataset_path)

            log.info("Use force=True to download again")
            return
        else:
            log.info(f"Downloading {ouf.b(self.name, return_str=True)}  {self.reference}")
            utils.download_file(self.url, f"{self.name}.zip")

        # Unzip dataset
        if not os.path.exists(self.name):
            os.makedirs(self.name)

        log.info("Extracting to %s", self.dataset_path)
        utils.extract_zip(f"{self.name}.zip", self.dataset_path)

        # Remove zip file
        log.info("Cleaning...")
        os.remove(self.name + ".zip")
        log.info("Done!")
