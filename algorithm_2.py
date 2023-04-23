# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

# Load the dataset
df = pd.read_csv("student_performance.csv")

# Clean the data
df.dropna(inplace=True)

# Evaluate student performance
df["cumulative_percentage"] = df[
    ["sem1_percent", "sem2_percent", "sem3_percent", "sem4_percent"]
].mean(axis=1)
df["performance"] = pd.cut(
    df["cumulative_percentage"],
    bins=[0, 35, 60, 75, 100],
    labels=["dropout", "poor", "support", "good"],
)

# Visualize student performance
sns.countplot(x="performance", data=df)

# Prepare data for LSTM model
X = df[
    ["sem1_percent", "sem2_percent", "sem3_percent", "sem4_percent", "attendance"]
].values
y = pd.get_dummies(df["performance"]).values
scaler = StandardScaler()
X = scaler.fit_transform(X)
X = X.reshape(X.shape[0], 1, X.shape[1])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build LSTM model
model = Sequential()
model.add(LSTM(128, input_shape=(1, 5)))
model.add(Dense(4, activation="softmax"))
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Train LSTM model
history = model.fit(
    X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test)
)

# Evaluate LSTM model
score = model.evaluate(X_test, y_test)
print("Test loss:", score[0])
print("Test accuracy:", score[1])
