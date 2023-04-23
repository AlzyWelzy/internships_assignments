import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense


class StudentPerformance:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.history = None
        self.score = None

    def clean_data(self):
        self.df.dropna(inplace=True)

    def evaluate_performance(self):
        self.df["cumulative_percentage"] = self.df[
            ["sem1_percent", "sem2_percent", "sem3_percent", "sem4_percent"]
        ].mean(axis=1)
        self.df["performance"] = pd.cut(
            self.df["cumulative_percentage"],
            bins=[0, 35, 60, 75, 100],
            labels=["dropout", "poor", "support", "good"],
        )

    def prepare_data(self):
        X = self.df[
            [
                "sem1_percent",
                "sem2_percent",
                "sem3_percent",
                "sem4_percent",
                "attendance",
            ]
        ].values
        y = pd.get_dummies(self.df["performance"]).values
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
        X = X.reshape(X.shape[0], 1, X.shape[1])
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

    def build_model(self):
        model = Sequential()
        model.add(LSTM(128, input_shape=(1, 5)))
        model.add(Dense(4, activation="softmax"))
        model.compile(
            optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
        )
        return model

    def train_model(self, model):
        self.history = model.fit(
            self.X_train,
            self.y_train,
            epochs=50,
            batch_size=32,
            validation_data=(self.X_test, self.y_test),
        )

    def evaluate_model(self, model):
        self.score = model.evaluate(self.X_test, self.y_test)
        print("Test loss:", self.score[0])
        print("Test accuracy:", self.score[1])

    def visualize_performance(self):
        sns.countplot(x="performance", data=self.df)
        plt.show()


def main():
    student_performance = StudentPerformance("student_performance.csv")
    student_performance.clean_data()
    student_performance.evaluate_performance()
    student_performance.prepare_data()
    model = student_performance.build_model()
    student_performance.train_model(model)
    student_performance.evaluate_model(model)
    student_performance.visualize_performance()


if __name__ == "__main__":
    main()
