import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib
batch_size = 32
img_height = 480
img_width = 480


def load_ds(path):
    data_dir = pathlib.Path(path).with_suffix('')

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

    return train_ds, val_ds

def train(plot=False):
    train_ds, val_ds = load_ds('train')
    
    class_names = train_ds.class_names
    num_classes = len(class_names)

    # normalise image by reducing colour depth by half
    img_norm = layers.Rescaling(1./2)

    model = Sequential([
        # img_norm,
        layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes)
    ])

    # compile the model 
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
    
    model.summary()

    epochs=10
    history = model.fit( train_ds, validation_data=val_ds, epochs=epochs )

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    epochs_range = range(epochs)

    if plot:
        plt.figure(figsize=(8, 8))
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')
        plt.show()

    return model

if __name__ == '__main__':
    train()