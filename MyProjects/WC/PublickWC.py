import json

# функция за запазване на информацията
def save_data(file_name='toilets.json'):
    with open(file_name, 'w') as file:
        json.dump(lst_toilets, file, indent=4)


# функция за лоудване
def load_data(file_name='toilets.json'):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# списък с тоалетните
lst_toilets = load_data()


# функция за валидиране на въведено число
def int_input(prompt):
    while True:
        try:
            inp = int(input(prompt))
            return inp
        except ValueError:
            print("Моля, въведи само номера на командата.")


# функция за добавяне на тоалетни
def add_toilet():
    # създаване на речник, в който да запишем тоалетните
    # noinspection PyDictCreation
    toilet_info = {}
    toilet_info["name"] = input("Въведи име за тоалетната: ")
    toilet_info["location"] = input("Въведи локация на тоалетната: ")
    toilet_info["rating"] = input("""Като имаш предвид, че:
            3 точки са за хигиена
            2 точки са за достъпност
            Какъв рейтинг би дал на тоалетната от 1 до 5: """)
    toilet_info["is_free"] = input("Безплатна ли е за използване? (Да/Не): ")

    # запазване на речника в списъка с тоалетни
    lst_toilets.append(toilet_info)
    print("Тоалетната е добавена успешно!")


# функция за виждане на списък с тоалетните
def view_list():
    # ако няма запазени тоалетни
    if not lst_toilets:
        print("Все още нямаме въведени тоалетни. :(")
    else:
        for num, toilet in enumerate(lst_toilets, 1):
            print(f"""Тоалетна номер: {num}
    Име: {toilet["name"]}
    Локация: {toilet["location"]}
    Рейтинг: {toilet["rating"]}
    Безплатна ли е: {toilet["is_free"]}""")


# функция за премахване на тоалетна
def remove_toilet(number):
    if 1 <= number <= len(lst_toilets):
        removed_toilet = lst_toilets.pop(number - 1)
        print(f"Тоалетна '{removed_toilet['name']}' е премахната успешно!")
    else:
        print("Няма тоалетна с такъв номер.")


# първо съобщение при стартиране на програмата
print("""=======================================================
    Не можеш повече да стискаш, но си далеч от дома? 
    Дошъл си на правилното място! Избери:""")

# меню с команди
while True:
    print("""
    1. Добави нова тоалетна
    2. Виж списъка с тоалетни
    3. Предложи тоалетна за премахване
    4. Напусни менюто""")

    # въвеждане на командата
    cmd = int_input("Въведи номер на командата: ")
    if cmd == 1:
        print()
        add_toilet()
        save_data()

    elif cmd == 2:
        print()
        view_list()

    elif cmd == 3:
        print()
        # ако няма запазени тоалетни
        if not lst_toilets:
            print("Няма тоалетни за премахване.")
        else:
            print("Въведи номера на тоалетната, която желаеш да премахнеш: ")

            # показване на списък с номер на тоалетната и името ѝ
            for num, toilet in enumerate(lst_toilets, 1):
                print()
                print(f"""Тоалетна номер: {num}
            Име: {toilet["name"]}""")

            # въвеждане на тоалетна за премахване
            num_remove = int_input("Номер: ")
            remove_toilet(num_remove)
            save_data()

    elif cmd == 4:
        print()
        print("Успех! :)")
        save_data()
        break
    else:
        print("Невалидна команда. Моля, опитай отново.")

