# Відкриваємо файл з даними про популяцію
with open("population.txt", "r") as file:
    # Створюємо словник для збереження даних про популяцію кожної країни
    population_data = {}

    # Проходимося по кожному рядку у файлі
    for line in file:
        # Розділяємо рядок на окремі елементи
        data = line.strip().split(", ")
        country = data[0]
        year = int(data[1])
        population = int(data[2])

        # Перевіряємо, чи вже є дані про цю країну у словнику
        if country in population_data:
            # Якщо є, то додаємо до списку населення нове значення
            population_data[country].append((year, population))
        else:
            # Якщо немає, то створюємо новий список населення для цієї країни
            population_data[country] = [(year, population)]

# Обчислюємо зміну населення за роки для кожної країни
for country in population_data:
    # Сортуємо список населення за роками
    population_data[country].sort()

    # Обчислюємо зміну населення між роками
    for i in range(1, len(population_data[country])):
        year1, pop1 = population_data[country][i-1]
        year2, pop2 = population_data[country][i]
        population_change = pop2 - pop1

        # Виводимо дані про зміну населення
        print(f"{country} {year1}-{year2}: {population_change}")