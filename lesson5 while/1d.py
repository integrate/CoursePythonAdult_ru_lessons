"""
Добавляем счетчик попыток.
"""

import random

secret = random.randint(1, 100)
print(secret)
answer = int(input("Угадай число"))

count = 1

while answer != secret:

    if answer > secret:
        print("Не угадал, мое число меньше!")
    else:
        print("Не угадал, мое число больше!")

    answer = int(input("Попробуй еще раз."))
    count += 1  # то же самое, что count = count + 1

else:
    print("Угадал с попытки номер " + str(count) + "!")