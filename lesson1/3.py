"""
Создаем спрайт blue_man на координатах 100, 100.
Также делаем персонажа Марио. Справа от БлюМэна.

Делаем диалог между Марио и БлюМэном:
Привет, Марио
  Привет, Джек
Ты мне кое, что должен
  Не понимаю, о чем ты, Джек
"""
import time

import wrap


wrap.world.create_world(450, 600, 900, 60)
wrap.world.set_back_color(54, 133, 99)
wrap.sprite.add("blue_man", 100, 500)
wrap.sprite.add("mario-1-big", 300, 500, "stand")
wrap.sprite.add_text("Привет, Марио", 100, 370)
time.sleep(2)
wrap.sprite.add_text("Привет, Джек", 300, 330)
time.sleep(1)
wrap.sprite.add_text("Ты мне кое-что должен", 130, 290)
time.sleep(2)
wrap.sprite.add_text("Не понимаю, о чем ты, Джек", 300, 250)