import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib
data_dir = pathlib.Path('../train').with_suffix('')

# image_count = len(list(data_dir.glob('*/*.png')))

aw = list(data_dir.glob('Animal Weaknesses/*'))
PIL.Image.open(str(aw[0]))