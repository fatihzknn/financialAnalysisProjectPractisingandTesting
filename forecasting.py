# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import MinMaxScaler
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, LSTM
# import matplotlib.pyplot as plt
# from datapullingwithPandas import bist30_data

# df = bist30_data[["Close","Brent","Usd"]]
# # df = df[['Kapanış Fiyatları', 'Petrol Fiyatı', 'Dolar Kuru']]

# test_data = df[df.index > df.index.max() - pd.DateOffset(months=3)]

# # Eğitim seti için geri kalan verileri kullanın
# train_data = df[df.index <= df.index.max() - pd.DateOffset(months=3)]

# # Verileri normalize etmek için MinMaxScaler kullanın
# scaler = MinMaxScaler()
# train_scaled = scaler.fit_transform(train_data[['Close', 'Brent', 'Usd']])
# test_scaled = scaler.transform(test_data[['Close', 'Brent', 'Usd']])

# # Giriş verilerini ve etiketleri oluşturun
# X_train, y_train = train_scaled[:, :-1], train_scaled[:, -1]
# X_test, y_test = test_scaled[:, :-1], test_scaled[:, -1]

# # Yapay Sinir Ağı modelini oluşturun
# model = Sequential()
# model.add(Dense(50, input_dim=X_train.shape[1], activation='relu'))
# model.add(Dense(1, activation='linear'))

# # Modeli derleyin
# model.compile(optimizer='adam', loss='mean_squared_error')

# # Modeli eğitin
# model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=2)

# # Tahminleri yapın
# predictions = model.predict(X_test)

# # predictions'ı ve X_test'ı bir araya getirin (sadece özellikleri birleştirin, kapanış fiyatları değil)
# combined_data = np.hstack((predictions, X_test))

# # Tahminleri ve giriş verilerini orijinal ölçeklendirmeye geri döndürün
# combined_data = scaler.inverse_transform(combined_data)

# y_pred_train = model.predict(X_train)
# y_pred_test = model.predict(X_test)
from datapullingwithPandas import bist30_data
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# X = bist30_data[['Brent', 'Usd', 'Volume']]
# y = bist30_data['Close']

df1=bist30_data.reset_index()['Close']
# print(df1)

# plt.plot(df1)
# plt.show()

scaler = MinMaxScaler(feature_range=(0,1))
df1 = scaler.fit_transform(np.array(df1).reshape(-1,1))
#splitting train test

training_size = int(len(df1)*0.75)
test_size = len(df1)-training_size
train_data, test_data = df1[0:training_size,:],df1[training_size:len(df1),:1]
print(training_size,test_size)

# #Normalization
# scaler = MinMaxScaler()
# X_scaled = scaler.fit_transform(X)
# #Train Test
# train_size_for_x = int(len(X) * 0.8)  
# X_train, X_test = X[:train_size_for_x], X[train_size_for_x:]
# train_size_for_y = int(len(y) * 0.8)  
# y_train, y_test = y[:train_size_for_y], y[train_size_for_y:]

#conver an array of values into a dataset matrix

def create_dataset(dataset, time_step=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-time_step-1):
		a = dataset[i:(i+time_step), 0]   ###i=0, 0,1,2,3-----99   100 
		dataX.append(a)
		dataY.append(dataset[i + time_step, 0])
	return np.array(dataX), np.array(dataY)
# reshape into X=t,t+1,t+2,t+3 and Y=t+4
time_step = 100
X_train, y_train = create_dataset(train_data, time_step)
X_test, ytest = create_dataset(test_data, time_step)




# reshape input to be [samples, time steps, features] which is required for LSTM
X_train =X_train.reshape(X_train.shape[0],X_train.shape[1] , 1)
X_test = X_test.reshape(X_test.shape[0],X_test.shape[1] , 1)

### Create the Stacked LSTM model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM

model=Sequential()
model.add(LSTM(50,return_sequences=True,input_shape=(100,1)))
model.add(LSTM(50,return_sequences=True))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer='adam')

model = model.fit(X_train,y_train,validation_data=(X_test,ytest),epochs=100,batch_size=64,verbose=1)


