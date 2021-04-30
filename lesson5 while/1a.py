"""
Программа загадывает число от 1 до 10.
Предлагает пользователю угадать это число, пока не угадает.
"""
import random

secret = random.randint(1, 10)
answer = int(input("Угадай число"))

while answer != secret:
    answer = int(input("Не угадал. Попробуй еще раз."))