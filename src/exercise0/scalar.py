def calculate_scalar():
    x1 = input()
    x2 = input()
    x1_split = x1.split()
    x2_split = x2.split()
    
    result = 0
    for n in range(len(x1_split)):
        a = float(x1_split[n])
        b = float(x2_split[n])
        result = a * b + result
    
    print(result)

if __name__ == "__main__":
    print("Это файл main.py, до вызова функции calculate_scalar")
    calculate_scalar()
    print("Это файл main.py после вызова функции calculate_scalar")