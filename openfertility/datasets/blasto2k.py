"Dataset class for the blasto2k dataset"

import os
import outputformat as ouf
from openfertility.datasets import utils
from openfertility.io.logger import log


class Dataset:
    url = "https://figshare.com/ndownloader/files/39348899"
    name = "blasto2k"
    reference = "https://doi.org/10.1038/s41597-023-02182-3"

    def __init__(self, download=False, **kwargs):
        self.dataset_path = os.path.join(os.getcwd(), self.name)
        self.name_bold = ouf.b(self.name, return_str=True)
        if download:
            self.download(**kwargs)

        if not os.path.exists(self.dataset_path):
            log.info("Dataset not found at: %s", self.dataset_path)
            log.info("Use the method '.download()' from the created instance")

    def download(self, force=False, **kwargs):
        # Download dataset

        if os.path.exists(self.dataset_path) and not force:
            log.info("%s already at %s", self.name_bold, self.dataset_path)

            log.info("Use force=True to download again")
            return

        # Proceed with download if dataset not found
        log.info("Downloading %s - %s", self.name_bold, self.reference)
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
