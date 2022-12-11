translate = {'One': 'один', 'Two': 'два',
             'Three': 'три', 'Four': 'четыре'}
new_file = []
with open('text4_output.txt', 'r', encoding="utf-8") as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(translate[i[0]] + '  ' + i[1])
    print(new_file)

with open('text4_input.txt', 'w', encoding="utf-8") as file_obj_2:
    file_obj_2.writelines(new_file)
