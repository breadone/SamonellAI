import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib

def train():
    batch_size = 32
    img_height = 720
    img_width = 1280

    data_dir = pathlib.Path('../train').with_suffix('')

    # split into training and validation set with a 20% split
    train_ds = tf.keras.utils.image_dataset_from_directory(
            data_dir,
            validation_split=0.2,
            subset="training",
            seed=0,
            image_size=(img_height, img_width),
            batch_size=batch_size
        )

    val_ds = tf.keras.utils.image_dataset_from_directory(
            data_dir,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size
        )
    
    



if __name__ == '__main__':
    train()