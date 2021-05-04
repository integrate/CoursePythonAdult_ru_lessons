"""
Игнорируем число меньше 0 и больше максимального.
"""

import random

secret = random.randint(1, 100)
print(secret)

answer = -1
count = 0

while answer != secret:

    answer = int(input("Угадай число"))

    if answer<0 or answer>100:
        print("Число должно быть от 0 до 100")
        continue

    count += 1  # то же самое, что count = count + 1

    if answer > secret:
        print("Не угадал, мое число меньше!")
    else:
        print("Не угадал, мое число больше!")

else:
    print("Угадал с попытки номер " + str(count) + "!")