monthes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}
user_input = input("Введите, пожалуйста, номер месяца: ")
while user_input != 'exit':
    month = int(user_input)
    print('Вы ввели', month)
    if month in monthes:
        print('В этом месяце', monthes[month], 'день!')
    else:
        print('Такого месяца не существует!')
    user_input = input("Введите, пожалуйста, номер месяца: ")