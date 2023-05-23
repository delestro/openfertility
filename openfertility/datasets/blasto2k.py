from openfertility.datasets import utils
from openfertility.io import log
import outputformat as ouf
import os


class Dataset:
    url = "https://figshare.com/ndownloader/files/39348899"
    name = "blasto2k"
    doi = "https://doi.org/10.1038/s41597-023-02182-3"

    def __init__(self):
        # TODO: add check if dataset is already downloaded
        pass

    def download(self):

        # Download dataset
        log.info(f'Downloading {ouf.b(self.name, return_str=True)} ( DOI: {self.doi} )')
        utils.download_file(self.url, f'{self.name}.zip')

        # Unzip dataset
        if not os.path.exists(self.name):
            os.makedirs(self.name)

        extract_path = os.path.join(os.getcwd(), self.name)
        log.info(f'Extracting to {extract_path}')
        utils.extract_zip(f'{self.name}.zip', extract_path)

        # Remove zip file
        log.info(f'Cleaning {self.name}')
        os.remove(self.name + '.zip')
        log.info(f'Done!')
