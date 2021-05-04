"""
Добавляем условие досрочного выхода.
Специальная команда может быть введена только начиная со второй попытки.
"""

import random

secret = random.randint(1, 100)
print(secret)

answer = -1
count = 0

while answer != secret:

    answer = input("Угадай число")
    if answer == "сдаюсь":
        break
    answer = int(answer)

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

print("Было загадано число " + str(secret))



