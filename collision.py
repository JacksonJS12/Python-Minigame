import pygame

def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects


def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object


def handle_move(player, objects, end, player_vel):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    collide_left = collide(player, objects, -player_vel * 2)
    collide_right = collide(player, objects, player_vel * 2)

    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(player_vel)
    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(player_vel)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()
        elif obj and obj.name == "end":
            return True

    return False


def check_cherry_collision(player, cherries):
    for cherry in cherries[:]:
        if pygame.sprite.collide_mask(player, cherry):
            cherries.remove(cherry)
            player.cherries_eaten += 1


def check_end_collision(player, end):
    return pygame.sprite.collide_mask(player, end)
