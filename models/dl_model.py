import keras
from keras import models
from keras import layers
from keras import optimizers
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
from keras import regularizers
from keras.layers import BatchNormalization
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from IPython.display import display
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import os
import shutil

np.random.seed(1)

batch_size = 32
train_flow = keras.utils.text_dataset_from_directory("data/train", batch_size=batch_size)
test_flow = keras.utils.text_dataset_from_directory("data/valid", batch_size=batch_size)
