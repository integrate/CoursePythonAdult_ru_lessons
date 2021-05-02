import time

from wrap import world, sprite, sprite_text, actions

world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

victim = sprite.add("pacman", 300, 100, "player2")
hunter = sprite.add("pacman", 100, 100, "enemy_blue_right1")

#побег
text = sprite.add_text("Бежим!", sprite.get_x(victim), sprite.get_top(victim)-20)
time.sleep(0.5)
sprite.remove(text)
actions.set_size_percent(victim, 30, 30, 500)
actions.set_angle(victim, 180, 500)
actions.move_at_angle_dir(victim, 100, 600)
actions.set_size_percent(victim, 100, 100, 500)

#погоня
text = sprite.add_text("В погоню!", sprite.get_x(hunter), sprite.get_top(hunter)-20)
time.sleep(0.5)
sprite.remove(text)
actions.move_at_angle_point(hunter, sprite.get_x(victim), sprite.get_y(victim), 70, 500)

#побег
text = sprite.add_text("Бежим!", sprite.get_x(victim), sprite.get_top(victim)-20)
time.sleep(0.5)
sprite.remove(text)
actions.set_size_percent(victim, 30, 30, 500)
actions.set_angle(victim, -135, 500)
actions.move_at_angle_dir(victim, 100, 600)
actions.set_size_percent(victim, 100, 100, 500)

#погоня
text = sprite.add_text("В погоню!", sprite.get_x(hunter), sprite.get_top(hunter)-20)
time.sleep(0.5)
sprite.remove(text)
actions.move_at_angle_point(hunter, sprite.get_x(victim), sprite.get_y(victim), 70, 500)