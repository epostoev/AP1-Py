current_sprint = []
not_in_sprint = []

def add_task_to_sprint(story_points):
		# тут напиши код, который добавляет SP в нужный спринт
        if story_points < 8:
                current_sprint.append(story_points)
        else:
                not_in_sprint.append(story_points)


add_task_to_sprint(2)

add_task_to_sprint(5)

add_task_to_sprint(5)

add_task_to_sprint(13)

add_task_to_sprint(8)

add_task_to_sprint(1)

add_task_to_sprint(2)

# выведи сумму SP в спринте и сумму тех SP, которые не уместились в спринт
print(sum(current_sprint))
print(sum(not_in_sprint))