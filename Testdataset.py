import tensorflow as tf
import tensorflow_datasets as tfds
# import tensorflow_hub as hub
# from tensorflow.keras import layers
tfds.disable_progress_bar()

import os
import matplotlib.pyplot as plt
import matplotlib.pylab as plt
import math
import numpy as np
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

dataset, metadata = tfds.load('stanford_dogs', as_supervised=True, with_info=True)
train_dataset, test_dataset = dataset['train'], dataset['test']

