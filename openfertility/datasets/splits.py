from openfertility.datasets import utils
from openfertility.io.logger import log
import outputformat as ouf
import os
import torch.utils.data
from torchvision.transforms import ToTensor
import pandas as pd
from PIL import Image


class TrainSet(torch.utils.data.Dataset):
    def __init__(self, dataset, transform=ToTensor()):
        self.dataset = dataset
        self.target = dataset.target  # Target label
        self.transform = transform

        # Directory for images
        self.image_dir = os.path.join(self.dataset.name, self.dataset.data_path)

        # Get the labels dataframe
        self.labels_path = os.path.join(self.dataset.name, self.dataset.labels_path)
        self.df = pd.read_csv(self.labels_path, sep=dataset.separator)

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        img_path = os.path.join(self.image_dir, self.df[self.dataset.data_col][idx])
        image = Image.open(img_path).convert("RGB")

        label = self.df[self.target][idx]

        if self.transform:
            image = self.transform(image)

        return image, label
