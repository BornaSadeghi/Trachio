import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, Dense, Dropout, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import Adam
import numpy as np
from PIL import Image
from glob import glob
from matplotlib import pyplot as plt

# Load the model
model = tf.keras.models.load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

labels = {
    0:"healthy",
    1:"asthma",
    2:"bronchiectasis",
    3:"copd",
    4:"lrti",
    5:"pneumonia",
    6:"urti"
}

def classify(img_filename):
    # Normalize the image
    normalized_image_array = (np.array(Image.open(img_filename).resize((224,224))).astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    prediction = model.predict(data)
    return labels[np.argmax(prediction)]


# print(labels[classify("spectrograms/healthy-1.png")])