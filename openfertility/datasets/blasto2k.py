from openfertility.datasets import utils
from openfertility.io.logger import log
import outputformat as ouf
import os


class Dataset:
    url = "https://figshare.com/ndownloader/files/39348899"
    name = "blasto2k"
    reference = "https://doi.org/10.1038/s41597-023-02182-3"

    def download(self, force=False):
        # Download dataset
        extract_path = os.path.join(os.getcwd(), self.name)

        if os.path.exists(extract_path) and not force:
            log.info(f"{ouf.b(self.name, return_str=True)} already at {extract_path}")
            log.info('Use force=True to download again')
            return
        else:
            log.info(f"Downloading {ouf.b(self.name, return_str=True)}  {self.reference}")
            utils.download_file(self.url, f"{self.name}.zip")

        # Unzip dataset
        if not os.path.exists(self.name):
            os.makedirs(self.name)

        log.info(f"Extracting to {extract_path}")
        utils.extract_zip(f"{self.name}.zip", extract_path)

        # Remove zip file
        log.info(f"Cleaning...")
        os.remove(self.name + ".zip")
        log.info(f"Done!")

