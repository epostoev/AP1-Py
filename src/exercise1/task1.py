def scalar():
    x1 = input()
    x2 = input()

    x1_split = x1.split()
    x2_split = x2.split()

    x1_split_float = []
    x2_split_float = []

    x1_split_count = len(x1_split)
    x2_split_count = len(x2_split)

    result = 0

    for n in range(x1_split_count):
        x1 = float(x1_split[n])
        x2 = float(x2_split[n])
        x1_split_float.append(x1)
        x2_split_float.append(x2)
        result = x1_split_float[n] * x2_split_float[n] + result

    print(result)

if __name__ == "__main__":
    scalar()

# 1.0 2.0 3.0 4.0 5.0 6.0