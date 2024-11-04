class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, n):
        print(f"Enter {n} numbers one by one:")
        for i in range(n):
            num = int(input(f"Enter number {i + 1}: "))
            self.numbers.append(num)

    def find_number(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1
        else:
            return -1

def main():
    N = int(input("Enter a positive integer N: "))
    processor = NumberProcessor()
    processor.read_numbers(N)
    X = int(input("Enter X: "))

    result = processor.find_number(X)
    print(result)

if __name__ == "__main__":
    main()
