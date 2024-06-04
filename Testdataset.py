import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import matplotlib.pylab as plt
import math
import numpy as np

(img_train, label_train), (img_test, label_test) = tfds.as_numpy(tfds.load(
    'stanford_dogs',
    split=['train', 'test'],
    batch_size=-1,
    as_supervised=True,
))

plt.imshow(img_train[2])
# plt.title(f"{label_train[2]}")
# print(f"Label: {label_train[2]}")
plt.show()