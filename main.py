from random import randint

key = randint(1, 100)
guessTaken = 0  # количество предпринятых попыток
guess = 0  # числа, которые будет вводить пользователь

print('Я загадал число от 1 до 100. У тебя есть 7 попыток, чтобы его угадать!')

while guess != key and guessTaken < 7:
    guess = int(input('Введи число: '))

    if guess > key:
        print('Число больше загаданного!')
    elif guess < key:
        print('Число меньше загаданного!')

    guessTaken += 1


if guess == key:
    print(f'Поздравляю! Ты угадал, это заняло {guessTaken} попыток')
else:
    print(f'Ты проиграл! Я загадал число {key}.')