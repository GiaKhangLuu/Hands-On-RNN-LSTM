import numpy as np
import pandas as pd
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential

handswing_df = pd.read_csv('HANDSWING.txt')

X, y = [], []
dataset = handswing_df.iloc[:, 1:].values
no_of_timestep = 10
no_of_samples = len(dataset)

for i in range(no_of_timestep, no_of_samples, no_of_timestep):
    X.append(dataset[i-no_of_timestep:i, :])
    y.append(0)

X, y = np.array(X), np.array(y)

model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1, activation='sigmoid'))
model.compile(optimizer='adam', metrics=['accuracy'], loss='binary_crossentropy')

model.fit(X_train, y_train, epochs=16, batch_size=32)
model.save('lstm_activity_recognize.h5')
