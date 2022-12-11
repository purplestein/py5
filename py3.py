staff = {
    "Мерфи": 10000, "Стивенсон": 50000, "Трамп": 70000,
    "Робинсон": 10000, "Паркер": 30000, "Салливан": 30000,
    "Аллен": 60000, "Хиггинс": 40000, "Уилсон": 40000,
    "Лисовски": 60000,
}
try:
    file = open("text3.txt", 'w')
    for second_name, salary in staff.items():
        file.write(second_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file.close()
sum = 0
count = 0
persons = []
with open("text3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        sum += int(tokens[1])
        count += 1
result = sum / count
print(f"Сотрудник: {persons}")
print(f"Средний доход: {result}")
