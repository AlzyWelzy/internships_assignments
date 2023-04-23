import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

# load data
data = pd.read_csv('student_performance.csv')

# split data into features (X) and target variable (y)
X = data.drop('G3', axis=1)
y = data['G3']

# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# define the model
model = Sequential()
model.add(Dense(10, input_dim=32, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the model on the training data
model.fit(X_train, y_train, epochs=50, batch_size=32)

# evaluate the model on the testing data
loss, accuracy = model.evaluate(X_test, y_test)

# print the model's accuracy
print('Accuracy: {:.2f}%'.format(accuracy * 100))
