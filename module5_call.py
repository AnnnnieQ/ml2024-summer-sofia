from module5_mod import NumberProcessor

def main():
    N = int(input("Enter a positive integer N (number of inputs): "))
    
    processor = NumberProcessor()
    
    processor.read_numbers(N)
    
    X = int(input("Enter X: "))
    
    result = processor.find_number(X)
    print(result)

if __name__ == "__main__":
    main()
