import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def read_data(num_samples, dataset_name):
    print(f"Enter {num_samples} (x, y) pairs for {dataset_name}:")
    x_values = np.zeros(num_samples)
    y_values = np.zeros(num_samples, dtype=int)
    for i in range(num_samples):
        x = float(input(f"Enter x for pair {i + 1}: "))
        y = int(input(f"Enter y for pair {i + 1}: "))
        x_values[i] = x
        y_values[i] = y
    return x_values.reshape(-1, 1), y_values

def main():
    N = int(input("Enter N: "))
    train_x, train_y = read_data(N, "Training Set")

    M = int(input("Enter M: "))
    test_x, test_y = read_data(M, "Test Set")

    best_k = 1
    best_accuracy = 0
    for k in range(1, 11):  
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(train_x, train_y)  
        predictions = knn.predict(test_x)  
        accuracy = accuracy_score(test_y, predictions)  

        print(f"Accuracy for k = {k}: {accuracy}")
        if accuracy > best_accuracy:  
            best_k = k
            best_accuracy = accuracy

    print(f"\nBest k: {best_k}, Test Accuracy: {best_accuracy}")


if __name__ == "__main__":
    main()