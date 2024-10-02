import numpy as np
import tensorflow as tf
import os

from train import train, load_ds

# the image to predict on, change this!
pred_image = '/home/juniper/dev/samonellai/test/2024-10-02_16-40.png'

# check if model exists on disk, load that if so
if os.path.exists('model.keras'):
    model = tf.keras.models.load_model('model.keras')
    print('loaded existing model.keras')
else:
    model = train()
    model.save('model.keras')
    print('saved model to model.keras')

names = load_ds('train')[0].class_names

# load image and create a batch for prediction
img = tf.keras.utils.load_img(pred_image, target_size=(480, 480))
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) 

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

predicted_name = names[np.argmax(score)]

print( f"This image most likely is from \"{predicted_name}\" with a {np.max(score):.2f}% confidence." )