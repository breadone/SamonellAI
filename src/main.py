import numpy as np
import tensorflow as tf

from train import train

# the image to predict on, change this!
pred_image = '/home/juniper/dev/samonellai/test/2024-10-02_16-40.png'
model, names = train()

# load image and create a batch for prediction
img = tf.keras.utils.load_img(pred_image, target_size=(640, 640))
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) 

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

predicted_name = names[np.argmax(score)]

print( f"This image most likely is from \"{predicted_name}\" with a {np.max(score):.2f}% confidence." )