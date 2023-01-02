import pandas as pd 
import numpy as np
import sklearn
from sklearn import linear_model
import pickle

data = pd.read_csv('data.csv', sep=', ')
data = data[['Price', 'Open', 'High', 'Low']]
# print(data.head())

# data['Open'] = float(input('open: '))
# data['High'] = float(input('high: '))
# data['Low'] = float(input('low: '))

predict = 'Price'

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)
print(acc)

prd = linear.predict(x_test)

for i in range(len(prd)):
    page_data = 'Predicted price:', prd[i], 'Data: ',x_test[i]
    print(page_data)
