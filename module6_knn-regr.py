import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def predict(self, x_query):
        points_array = np.array(self.points)
        x_values = points_array[:, 0]
        y_values = points_array[:, 1]

        distances = np.abs(x_values - x_query)
        sorted_indices = np.argsort(distances)

        nearest_y_values = y_values[sorted_indices][:self.k]

        return np.mean(nearest_y_values)

def main():
    try:
        N = int(input("Enter N: "))
        k = int(input("Enter k: "))

        if k > N:
            print("Error: k cannot be greater than N.")
            return

        knn = KNNRegressor(k)

        for i in range(N):
            x = float(input(f"Enter x value for point {i + 1}: "))
            y = float(input(f"Enter y value for point {i + 1}: "))
            knn.add_point(x, y)


        x_query = float(input("Enter the x value for prediction: "))


        y_pred = knn.predict(x_query)
        print(f"The predicted y is: {y_pred}")

if __name__ == "__main__":
    main()
