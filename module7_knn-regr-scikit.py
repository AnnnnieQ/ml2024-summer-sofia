import numpy as np
from sklearn.neighbors import KNeighborsRegressor


N = int(input("Enter N: "))
if N <= 0:
    print("N must be a positive integer.")
    exit()


k = int(input("Enter k: "))
if k <= 0:
    print("k must be a positive integer.")
    exit()


X_train = np.zeros((N, 1))
y_train = np.zeros(N)


print("Enter the (x, y) points:")
for i in range(N):
    x_value = float(input(f"Enter x value for point {i + 1}: "))
    y_value = float(input(f"Enter y value for point {i + 1}: "))
    X_train[i] = x_value
    y_train[i] = y_value


X_pred = float(input("Enter the x value for prediction: "))


if k > N:
    print("Error: k cannot be greater than N.")
else:
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(np.array([[X_pred]]))
    print(f"The predicted y value for x = {X_pred} is: {y_pred[0]}")

variance = np.var(y_train)
print(f"The variance of the labels in the training dataset is: {variance}")
