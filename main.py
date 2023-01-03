import pandas as pd 
import numpy as np
import sklearn
from sklearn import linear_model
import pickle

data = pd.read_csv('data.csv', sep=',')
data = data[['Close', 'Open', 'Volume_USD', 'Volume_CCY']]
# print(data.head())

# data['Open'] = float(input('open: '))
# data['High'] = float(input('high: '))
# data['Low'] = float(input('low: '))
predict = 'Close'

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
# x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

best = 0
for i in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    if acc > best:
        best = acc
        print(best)
        with open('model.pickle', 'wb') as f:
            pickle.dump(linear, f)

# pickle_in = open('model.pickle', 'rb')
# linear = pickle.load(pickle_in)
prd = linear.predict(x_test)

for i in range(len(prd)):
    page_data = 'Predicted price:', prd[i], 'Data: ',x_test[i]
    print(page_data)

