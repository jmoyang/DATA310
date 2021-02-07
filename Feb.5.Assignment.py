import tensorflow as tf
import numpy as np

from tensorflow import keras
model = tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[3])])
model.compile(optimizer='sgd',loss='mean_squared_error')
x1 = np.array([4.0,3.0,4.0,5.0,2.0,3.0],dtype=float)
x2 = np.array([3.524, 2.840, 3.680, 3.051, 1.479, 1.238],dtype=float)
x3 = np.array([2.0, 2.0, 3.0, 2.0, 1.0, 1.0],dtype=float)
xs = np.stack([x1, x2, x3], axis=1)
ys = np.array([2.89, 2.29, 3.99, 3.475, 2.5, 0.97],dtype=float)
model.fit(xs,ys,epochs=1000)

a= np.array([5.0], dtype=float)
b= np.array([3.680], dtype=float)
c= np.array([1.0], dtype=float)
d=np.stack([a, b, c], axis=1)

model.predict([d])