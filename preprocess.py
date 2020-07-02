import numpy as np
import os
from fastai.vision import ImageList
import pandas as pd
import torch


def preprocess(dicom_paths):
    dicom_paths = [f'{path}.png' for path in dicom_paths]
    df = pd.DataFrame(dicom_paths, columns=['name'])
    train_data_stats = torch.load('normal_stats')
    images = ImageList.from_df(df, '.')

    return images