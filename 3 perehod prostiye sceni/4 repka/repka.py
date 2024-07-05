import wrap, time

wrap.world.create_world(800, 600, 900, 60)
wrap.world.set_back_color(226, 226, 165)

wrap.add_sprite_dir("sprites")

time.sleep(1)
wrap.sprite.add("repka", 100, 130, "ded")
time.sleep(1)
wrap.sprite.add_text('Посадил дед репку', 130 , 30, font_size=30)

time.sleep(2)
wrap.sprite.add("repka", 400, 150, "repka")

time.sleep(2)
wrap.sprite.add_text('Выросла репка больша-а-а-а-я!', 400 , 70, font_size=30)

time.sleep(1)
wrap.sprite.add("repka", 400, 160, "repka_bolshaya")

time.sleep(2)
wrap.sprite.add_text('И тут оказалось...', 400 , 300, font_size=30)

time.sleep(2)
wrap.sprite.add_text('Бабка в магазин пошла..', 150 , 340, font_size=25)
time.sleep(1)
wrap.sprite.add("repka", 70, 440, "babka")

time.sleep(2)
wrap.sprite.add_text('Внучка в школе..', 250 , 380, font_size=25)
time.sleep(1)
wrap.sprite.add("repka", 240, 460, "vnuchka")

time.sleep(2)
wrap.sprite.add_text('Жучка к ветеринару убежала..', 450 , 410, font_size=25)
time.sleep(1)
wrap.sprite.add("repka", 410, 480, "zhuchka")

time.sleep(2)
wrap.sprite.add_text('Мурка репку не ест..', 590 , 460, font_size=25)
time.sleep(1)
wrap.sprite.add("repka", 580, 520, "murka")

time.sleep(2)
wrap.sprite.add_text('Мышка и на грядке поесть может..', 500 , 240)
time.sleep(1)
wrap.sprite.add("repka", 450, 210, "mishka")