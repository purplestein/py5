text = input('Ввод: ').split()

with open("text.txt", "w") as file:
    file.writelines("%s\n" % line for line in text)
