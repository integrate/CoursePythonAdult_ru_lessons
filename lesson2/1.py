"""
Сделать полет одного спрайта за другим.
Приведение бежит за Пакмэном по определенной траектории.
Поменять значения переменных. Теперь Пакмэн бежит за Бледным приведением по той же траектории.
"""
import time, wrap

wrap.world.create_world(400, 600, 900, 60)
wrap.world.set_back_color(100, 50, 230)

#настройки
hunter = "enemy_yellow_down1"
victim = "player1"
text1 = "Пакмэн, привет"
text2 = "Извини, я спешу"

# victim = "enemy_white_down1"
# hunter = "player1"
# text1 = "О, рад тебя видеть!"
# text2 = "Вы меня с кем-то перепутали..."

#создаем игрока
wrap.sprite.add("pacman", 50, 100, hunter)
wrap.sprite.add("pacman", 150, 100, victim)

time.sleep(1)
wrap.sprite.add_text(text1, 80, 60, True, "arial", 15)
time.sleep(1)
wrap.sprite.add_text(text2, 150, 40, True, "arial", 15)
time.sleep(1)

wrap.actions.move_to(1, 250, 100)
wrap.actions.move_to(0, 150, 100)

wrap.actions.move_to(1, 300, 150)
wrap.actions.move_to(0, 250, 100)

wrap.actions.move_to(1, 300, 250)
wrap.actions.move_to(0, 300, 150)