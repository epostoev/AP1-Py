x1 = input()
x2 = input()

x1_split = x1.split()
x2_split = x2.split()

x1_split_int = []

x1_split_count = len(x1_split)
print(x1_split_count)

for n in range(x1_split_count):
    print(n)
    input()
    x = float(x1_split[n])
    x1_split_int.append(x)

print(x1_split_int)

# result = (x1 * x2) + (y1 * y2) + (z1 * z2)

# print(result)


# 1.0 2.0 3.0 4.0 5.0 6.0