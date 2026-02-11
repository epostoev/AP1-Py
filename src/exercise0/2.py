car = {
    "brand": "SINOTRUK",
    "speed": 120,
    "abs": True
}

# Способ 1: Перебор ключей
for key in car:
    print(key)

# Способ 2: Перебор пар ключ-значение
for key, value in car.items():
    print(f"{key}: {value}")