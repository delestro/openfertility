from openfertility.datasets import utils
from openfertility.io import log
import outputformat as ouf
import os
import torch.utils.data
from torchvision.transforms import ToTensor
import pandas as pd
from PIL import Image


class Dataset:
    url = "https://figshare.com/ndownloader/files/39348899"
    name = "blasto2k"
    doi = "https://doi.org/10.1038/s41597-023-02182-3"

    def download(self):
        # Download dataset
        log.info(f"Downloading {ouf.b(self.name, return_str=True)} ( DOI: {self.doi} )")
        utils.download_file(self.url, f"{self.name}.zip")

        # Unzip dataset
        if not os.path.exists(self.name):
            os.makedirs(self.name)

        extract_path = os.path.join(os.getcwd(), self.name)
        log.info(f"Extracting to {extract_path}")
        utils.extract_zip(f"{self.name}.zip", extract_path)

        # Remove zip file
        log.info(f"Cleaning {self.name}")
        os.remove(self.name + ".zip")
        log.info(f"Done!")

    class Train(torch.utils.data.Dataset):
        def __init__(self, target = "EXP_silver", transform=ToTensor()):
            # TODO: Check if download was done, if not, download
            self.image_dir = "blasto2k/Images"
            self.labels = pd.read_csv("blasto2k/Gardner_train_silver.csv", sep=";")
            self.transform = transform
            self.target = target

        def __len__(self):
            return len(self.labels)

        def __getitem__(self, idx):
            img_path = os.path.join(self.image_dir, self.labels["Image"][idx])
            image = Image.open(img_path).convert("RGB")

            label = self.labels[self.target][idx]

            if self.transform:
                image = self.transform(image)

            return image, label
