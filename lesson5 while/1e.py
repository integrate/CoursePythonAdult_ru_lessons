"""
Добавляем условие досрочного выхода.
Специальная команда может быть введена только начиная со второй попытки.
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

    answer = input("Попробуй еще раз.")
    if answer == "сдаюсь":
        break
    answer = int(answer)

    count += 1  # то же самое, что count = count + 1

else:
    print("Угадал с попытки номер " + str(count) + "!")
    exit()

print("Ты сдался. Было загадано число " + str(secret))

