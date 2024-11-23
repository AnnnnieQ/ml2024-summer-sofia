import numpy as np
from sklearn.metrics import precision_score, recall_score

N = int(input("Enter N: "))

X = []
Y = []


for i in range(N):
    x_val = int(input(f"Enter the ground truth (X) for point {i+1} (0 or 1): "))
    y_val = int(input(f"Enter the predicted value (Y) for point {i+1} (0 or 1): "))
    X.append(x_val)
    Y.append(y_val)


X = np.array(X)
Y = np.array(Y)

precision = precision_score(X, Y)
recall = recall_score(X, Y)

print(f"\nPrecision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
