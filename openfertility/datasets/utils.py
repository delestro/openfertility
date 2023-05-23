import urllib.request
import zipfile
import os
from tqdm import tqdm


def _update_progress(pbar, blocknum, bs):
    pbar.update(blocknum * bs - pbar.n)


def _get_file_size(url):
    return int(urllib.request.urlopen(url).info().get("Content-Length", -1))


def download_file(url, file_path):
    with tqdm(
        total=_get_file_size(url),
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        ncols=80,
    ) as pbar:
        urllib.request.urlretrieve(
            url,
            file_path,
            reporthook=lambda blocknum, bs, total: _update_progress(pbar, blocknum, bs),
        )

def extract_zip(zip_path, extract_path):
    # Extract the contents of the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)