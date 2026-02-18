movies = {'Игры разума': 8.3, 
        'Зеленая миля': 9.1, 
        'Леон': 8.5, 
        'Эффект бабочки': 8.2, 
        'Матрица': 8.6, 
        'Криминальное чтиво': 8.7}

filtered_movies = {} # создай словарь filtered_movies

# отфильтруй фильмы по оценке 
for m, r in movies.items():
    if r >= 8.5:
        filtered_movies[m] = r
print(filtered_movies)