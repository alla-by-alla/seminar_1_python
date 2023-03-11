print('\n\tЗадача 2: Найдите сумму цифр трехзначного числа.', end='\n\n')
number = None
while number is None or len(number) !=3 and not number.isdigit():
    print('Введите трехзначное число:' if number is None else 'Введено неверное число! Введите трехзначное:', end=' ')
    number = input()
print('Сумма цифр введенного числа равна', sum([int(x) for x in number]))