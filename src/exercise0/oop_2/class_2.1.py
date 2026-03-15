# class Animal:
#     def __init__(self, poor):
#         self.tail = 4
#         self.head = 1
#         self.paws = 1
#         self.poor = poor
#         self.name = None
#     def set_name(self, name):
#         self.name = name

# class Dog(Animal):
#     pass

# dog = Animal(True)
# dog_1 = Dog(False)
# dog.set_name("Рекс")
# dog_1.set_name("Бобик")

# print(dog.__dict__)
# print(dog_1.__dict__)





# class Circle:
    
#     @staticmethod
#     def get_area_by_radius(radius):
#         area = 3.14 * (radius ** 2)
#         return area

#     def __init__(self, radius):
#         self.diameter = 4
#         self.area = self.get_area_by_radius(radius) 

# circle = Circle(1)

# print(circle.__dict__)





# class Cat:

#     @staticmethod
#     def get_cat_character(name, breed):
#             if len(name) > 4 and breed in ['Persian', 'Ragdoll']:
#                     return 'friendly'
#             else:
#                     return 'angry'

#     def __init__(self, name, breed):
#             self.head = 1
#             self.paws = 4
#             self.tail = 1
#             self.character = self.get_cat_character(name, breed) 

# cat_1 = Cat("Myr", "Persian")
# cat_2 = Cat("Myrlyka", "Persian")

# print(cat_1.__dict__)
# print(cat_2.__dict__)





# class Cube:

#     # напиши метод тут
#     @staticmethod
#     def get_cube_area(one_side_area):
#         return one_side_area * 6

#     def __init__(self, side_length, one_side_area):
#         self.side_length = side_length
#         self.area = self.get_cube_area(one_side_area)

# print(Cube.get_cube_area(3))

# class Dog:
    
#     def __init__(self):
#         self.head = 1
#         self.paws = 4

#     @staticmethod
#     def get_a_portion_of_food(age):
#         if age < 1:
#             return 50
#         elif 1 <= age < 7:
#             return 100
#         else:
#             return 70
        
# print(Dog.get_a_portion_of_food(3))
# print(Dog.__dict__)





# # даём импорту своё название
# import datetime as dt

# # этот класс создаёт объект поздравление с днём рождения, который принимает
# # на вход дату и выдаёт напоминание, что день рождения сегодня
# class BirthdayCongratulations:

#         def __init__(self, day, month, year):
#                 self.date = dt.date(year, month, day)
#                 self.is_birthday_today = False

#         # этот метод условно проверяет корректность даты, что её верхние границы соблюдены
#         @staticmethod
#         def is_date_correct(day, month, year):
#                 if day <= 31 and month <= 12 and year <= 2023:
#                         return True
#                 return False

# # использовать подобный метод можно так:
# if BirthdayCongratulations.is_date_correct(32, 5, 2023):
#         congratulations = BirthdayCongratulations(29, 5, 2023)
# else:
#     print('Введите верную дату') 

# # print(congratulations.__dict__)





# severity_list = ['Блокирующий', 'Критический', 'Значительный', 'Незначительный', 'Тривиальный']

# class BugDefinition:

#         def __init__(self, priority, severity):
#                 self.priority = priority
#                 self.severity = severity

#         # метод определяет, подходящее ли число указано в качестве приоритета бага
#         @staticmethod
#         def is_right_priority(priority):
#                 if 0 < priority < 5:
#                         return True
#                 return False

#         # метод определяет, входит ли указанное значение критичности 
#         # в список возможных значений
#         @staticmethod
#         def is_right_severity(severity):
#                 if severity not in severity_list:
#                         return False
#                 return True

# # с помощью функции определяем, можно ли создать объект бага и распределить его разработчику
# def add_bug(priority, severity):
#         bug = None
#         if BugDefinition.is_right_priority(priority) and BugDefinition.is_right_severity(severity):
#                 bug = BugDefinition(priority, severity)
#         return bug

# # распределяем баг по разработчикам в зависимости от его критичности и приоритета
# def submit_bug_to_developer(bug):
#         if bug and bug.priority >= 4 and bug.severity in ['Блокирующий', 'Критический']:
#                 return 'Передано Senior Developer'
#         elif bug and 4 > bug.priority >= 2 and bug.severity in ['Значительный', 'Незначительный']:
#                 return 'Передано Middle Developer'
#         elif bug:
#                 return 'Передано Junior Developer'
#         return 'Распределение невозможно'

# # задаём неправильные параметры
# bug = add_bug(10, 'Высокий')
# print(submit_bug_to_developer(bug)) # Распределение невозможно 


test_case_1 = {'name': 'Проверить клик на кнопку поиска',
               'steps': ['Открыть сайт',
                        'Найти кнопку с надписью "поиск"',
                        'Кликнуть на кнопку'],
              'e_result': 'Появились результаты поиска',
              'result': 'Появились результаты поиска',
              'is_automated': False}
test_case_2 = {'name': 'Проверить цвет кнопки поиска',
               'steps': ['Открыть сайт',
                        'Найти кнопку с надписью "поиск"',
                        'Открыть свойства кнопки'],
                        'e_result': 'Цвет соответствует заявленному',
                        'result': 'Цвет не соответствует заявленному',
               'is_automated': False}
test_case_3 = {'name': 'Проверить клик на кнопку входа',
               'steps': ['Открыть сайт',
                        'Найти кнопку с надписью "войти"',
                        'Кликнуть на кнопку'],
              'e_result': 'Произошёл вход',
              'result': 'Passed',
              'is_automated': True}



class TestCase:

    def __init__(self, name, steps, e_result, result):
        self.name = name
        self.steps = steps
        self.expected_result = e_result
        self.result = result

    def get_case_in_str(self):
        return f'{self.name}, {self.steps}, {self.result}'
		
    # допиши метод так, чтобы он был статическим и проверял, является ли 
    # тест-кейс обычным
    @staticmethod
    def is_ordinary_case(test_case):
        if test_case['is_automated'] == False:
            is_ordinary = True
        else:
            is_ordinary = False
        return is_ordinary

class AutomatedTestCase:

    def __init__(self, name, steps, e_result, result):
        self.name = name
        self.steps = steps
        self.expected_result = e_result
        self.result = result
		
    def get_case_in_str(self):
        return f'{self.name}, {self.steps}, {self.result}'

    # допиши метод так, чтобы он был статическим и проверял, является ли 
    # тест-кейс автоматизированным
    @staticmethod
    def is_automated_case(test_case):
        if test_case['is_automated'] == True:
            is_ordinary = True
        else:
            is_ordinary = False
        return is_ordinary

test_report = {'automated': [],
              'ordinary': [] }

def add_case_to_list(test_case):
    # input(f"\nPlease press Enter \n{test_case}")
    # допиши тут аргумент, который необходимо передать методу
    if AutomatedTestCase.is_automated_case(test_case):
        # а тут — создание объекта автоматизированного кейса
        automated_case = AutomatedTestCase(test_case['name'], test_case['steps'], test_case['e_result'], test_case['result'])
        automated_case = automated_case.get_case_in_str()
        test_report['automated'].append(automated_case)
    if TestCase.is_ordinary_case(test_case):
        ordinary_case = TestCase(test_case['name'], test_case['steps'], test_case['e_result'], test_case['result'])
        ordinary_case = ordinary_case.get_case_in_str()
        test_report['ordinary'].append(ordinary_case)

add_case_to_list(test_case_1)
add_case_to_list(test_case_2)
add_case_to_list(test_case_3)

print(test_report)


