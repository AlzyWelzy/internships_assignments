# Step 1: Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.metrics import classification_report

# Step 2: Load the dataset
df = pd.read_csv('student_performance.csv')

# Step 3: Clean the data
df = df.drop(['id'], axis=1)

# Step 4: Evaluate student performance
df['cumulative_percentage'] = (df['1-1_percentage'] + df['1-2_percentage'] + df['2-1_percentage'] + df['2-2_percentage'] + df['3-1_percentage'] + df['3-2_percentage'])/6
df['dropout'] = np.where(df['cumulative_percentage'] < 35, 1, 0)
df['good_performance'] = np.where(df['cumulative_percentage'] >= 60, 1, 0)
df['poor_performance'] = np.where(df['cumulative_percentage'] < 40, 1, 0)
df['support_required'] = np.where((df['cumulative_percentage'] >= 40) & (df['cumulative_percentage'] < 60), 1, 0)
df['eligible_for_placement'] = np.where((df['cumulative_percentage'] >= 65) & ((df['coding_skills'] == 1) | (df['academic_awards'] == 1) | (df['extracurricular_activities'] == 1)), 1, 0)

# Step 5: Visualize critical values
sns.boxplot(x='variable', y='value', data=pd.melt(df[['1-1_percentage', '1-2_percentage', '2-1_percentage', '2-2_percentage', '3-1_percentage', '3-2_percentage']]))

# Step 6: Visualize critical values
sns.countplot(x='dropout', data=df)

# Step 7: Prepare data for LSTM model
X = df.drop(['dropout', 'good_performance', 'poor_performance', 'support_required', 'eligible_for_placement', 'cumulative_percentage'], axis=1).values
y = df['dropout'].values

# Step 8: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 9: Reshape input data for LSTM model
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Step 10: Build and compile LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Step 11: Train LSTM model on training data
model.fit(X_train, y_train, epochs=50, batch_size=32)

# Step 12: Evaluate LSTM model
y_pred = model.predict(X_test)
y_pred = np.where(y_pred > 0.5, 1, 0)
print(classification_report(y_test, y_pred))
