import pygame
from utils import get_background, draw, load_heart_images, draw_win, load_cherry_sprites
from player import Player
from object import Block, Fire, Cherry, End
from collision import handle_move, check_cherry_collision

pygame.init()
pygame.display.set_caption("Platformer")

WIDTH, HEIGHT = 1280, 720
FPS = 120
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png", WIDTH, HEIGHT)

    block_size = 96

    end_img = pygame.image.load("assets/Items/Checkpoints/End/End (Idle).png").convert_alpha()
    end_img = pygame.transform.scale2x(end_img)

    end = End(block_size * 5 - 16, HEIGHT - block_size * 9 - 32, 64, 64, end_img)

    player = Player(32, block_size*2, 50, 50)

    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)
             ] + [Block(i * block_size, HEIGHT, block_size)
                  for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)
                  ]

    obstacles = [
                    Block(-block_size*2, HEIGHT - block_size * x, block_size) for x in range(2, 16)
                ] + [
                    Block(block_size * x, HEIGHT - block_size * 4, block_size) for x in range(3, 8)
                ] + [
                    Block(block_size * 10, HEIGHT - block_size * 2, block_size)
                ] + [
                    Block(block_size * 2, HEIGHT - block_size * 6, block_size)
                ] + [
                    Block(block_size * x, HEIGHT - block_size * 6, block_size) for x in range(8, 16)
                ] + [
                    Block(block_size * 15, HEIGHT - block_size * x, block_size) for x in range(2, 16)
                ] + [
                    Block(block_size * x, HEIGHT - block_size * 8, block_size) for x in range(4, 7)
                ] + [
                    Block(block_size * 5, HEIGHT - block_size * 8, block_size)
                ]

    cherry_sprites = load_cherry_sprites("Items", "Fruits/Cherries.png", 32, 32)
    cherries = [
        Cherry(block_size * 2 + 16, HEIGHT - block_size * 1 - 64, 64, 64, cherry_sprites),
        Cherry(block_size * 5 + 16, HEIGHT - block_size * 4 - 64, 64, 64, cherry_sprites),
        Cherry(block_size * 10 + 16, HEIGHT - block_size * 2 - 64, 64, 64, cherry_sprites),
        Cherry(block_size * 14 + 16, HEIGHT - block_size * 6 - 64, 64, 64, cherry_sprites),
        Cherry(block_size * 2 + 16, HEIGHT - block_size * 6 - 64, 64, 64, cherry_sprites)
    ]

    fires = [
        Fire(block_size * 3 + 32, HEIGHT - block_size * 4 - 64, 16, 32),
        Fire(block_size * 6 + 32, HEIGHT - block_size * 4 - 64, 16, 32),
        Fire(block_size * 12 + 32, HEIGHT - block_size * 6 - 64, 16, 32),
        Fire(block_size * 6 + 32, HEIGHT - block_size * 8 - 64, 16, 32)
    ]

    for fire in fires:
        fire.on()

    objects = floor + obstacles + fires + [end]

    filled_heart_image, empty_heart_image = load_heart_images()

    offset_x = 0
    offset_y = 0
    scroll_area_width = 200
    scroll_area_height = 100

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        player.loop(FPS)
        for fire in fires:
            fire.loop()
        for cherry in cherries:
            cherry.loop()
        if handle_move(player, objects, end, PLAYER_VEL):
            draw_win(window, player.cherries_eaten, len(cherries) + player.cherries_eaten)
            pygame.display.update()
            pygame.time.delay(3000)
            run = False
            break

        check_cherry_collision(player, cherries)

        draw(window, background, bg_image, player, objects + cherries, offset_x, offset_y, filled_heart_image, empty_heart_image)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

        if ((player.rect.top - offset_y <= scroll_area_height) and player.y_vel < 0) or (
                (player.rect.bottom - offset_y >= HEIGHT - scroll_area_height) and player.y_vel > 0):
            offset_y += player.y_vel

    print("Cherries eaten:", player.cherries_eaten)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
