import wrap, time

wrap.world.create_world(800, 600, 900, 60)
wrap.world.set_back_color(100, 100, 100)

wrap.add_sprite_dir("sprites")

time.sleep(1)
wrap.sprite.add_text('Посадил дед репку!', 400 , 200, font_size=30)
time.sleep(2)
wrap.sprite.add("repka", 400, 350, "repka")

time.sleep(1.5)
wrap.sprite.remove(0)
wrap.sprite.add("repka", 200, 130, "ded")
time.sleep(1.5)
wrap.sprite.add_text('Ага! Я посадил!', 200 , 30, font_size=30)
