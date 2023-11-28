import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
np.random.seed(42)
X_train = np.random.random((100, 10))
y_train = np.random.randint(2, size=(100, 1))
model = Sequential()
model.add(Dense(10, input_dim=10, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=10)
X_test = np.random.random((10, 10))  
predictions = model.predict(X_test)
print(predictions)
