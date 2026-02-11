# База данных тестов тормозной системы
tests = [
    {"id": 1, "speed": 60,  "brake_distance": 24.0, "abs": True},
    {"id": 2, "speed": 90,  "brake_distance": 47.2, "abs": True},
    {"id": 3, "speed": 120, "brake_distance": 98.5, "abs": False},
    {"id": 4, "speed": 80,  "brake_distance": 55.0, "abs": True},
    {"id": 5, "speed": 110, "brake_distance": 110.0, "abs": False},
]

# Задача 1: Функция проверки безопасности теста
# Тест безопасен если:
# - тормозной путь < 100 метров И
# - скорость <= 100 ИЛИ ABS работает
def is_test_safe(test):
    brake_ok = (test["brake_distance"] < 100 )
    speed_ok = test["speed"] <= 100 or test["abs"] == True
    return brake_ok and speed_ok

# Задача 2: Функция отчёта по тесту
def print_test_report(test):
    safe = is_test_safe(test)
    status = "✅ БЕЗОПАСНО" if safe else "❌ ОПАСНО"
    print(f"Тест #{test['id']}: {test['speed']} км/ч, "
          f"{test['brake_distance']} м, "
          f"ABS={test['abs']} → {status}")

# Задача 3: Выведи отчёт по всем тестам
for test in tests:
    print_test_report(test)
    # print(type(test))

# Задача 4: Найди все опасные тесты
print("\nОпасные тесты:")
for test in tests:
    # print(f"brake_distance = {test["brake_distance"]}")
    # print(f"speed = {test["speed"]}")
    # input()
    if (test["brake_distance"] > 100 or (test["speed"] > 100 and test["abs"] != True )):
        print(f"  Тест #{test['id']} требует проверки!")


# **Ожидаемый вывод:**
# ```
# Тест #1: 60 км/ч, 24.0 м, ABS=True → ✅ БЕЗОПАСНО
# Тест #2: 90 км/ч, 47.2 м, ABS=True → ✅ БЕЗОПАСНО
# Тест #3: 120 км/ч, 98.5 м, ABS=False → ❌ ОПАСНО
# Тест #4: 80 км/ч, 55.0 м, ABS=True → ✅ БЕЗОПАСНО
# Тест #5: 110 км/ч, 110.0 м, ABS=False → ❌ ОПАСНО

# Опасные тесты:
#   Тест #3 требует проверки!
#   Тест #5 требует проверки!