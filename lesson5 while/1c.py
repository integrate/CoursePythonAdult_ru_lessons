"""
Усложнение.
Число теперь от 1 до 100.
Программа говорит подсказки.
"""
import random

secret = random.randint(1, 100)
answer = int(input("Угадай число"))

while answer != secret:

    if answer > secret:
        print("Не угадал, мое число меньше!")
    else:
        print("Не угадал, мое число больше!")

    answer = int(input("Попробуй еще раз."))

else:
    print("Угадал!")