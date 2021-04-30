"""
Усложнение: говорит Угадал, если угадал. Использует else.
"""

import random

secret = random.randint(1, 10)
answer = int(input("Угадай число"))

while answer != secret:
    answer = int(input("Не угадал. Попробуй еще раз."))
else:
    print("Угадал!")

#можно было и не писать Угадал в else. А просто написать после цикла.
#print("Угадал!")