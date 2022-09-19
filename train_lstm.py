import numpy as np
import pandas as pd
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential

no_of_timestep = 10
handswing_df = pd.read_csv('HANDSWING.txt')
do_nothing_df = pd.read_csv('./DO-NOTHING.txt')

handswing_dataset = handswing_df.iloc[:, 1:].values
do_nothing_dataset = do_nothing_df.iloc[:, 1:].values

X, y = [], []
for i in range(no_of_timestep, len(handswing_dataset), no_of_timestep):
    X.append(handswing_dataset[i-no_of_timestep:i, :])
    y.append(1)
for i in range(no_of_timestep, len(do_nothing_dataset), no_of_timestep):
    X.append(do_nothing_dataset[i-no_of_timestep:i, :])
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

model.fit(X, y, epochs=16, batch_size=32)
model.save('lstm_activity_recognize.h5')
