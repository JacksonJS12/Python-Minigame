import pygame
from os import listdir
from os.path import isfile, join


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def load_heart_images():
    filled_heart_path = join("assets", "Items", "Heart", "heart.png")
    empty_heart_path = join("assets", "Items", "Heart", "empty_heart.png")
    filled_heart = pygame.image.load(filled_heart_path).convert_alpha()
    empty_heart = pygame.image.load(empty_heart_path).convert_alpha()
    return pygame.transform.scale(filled_heart, (32, 32)), pygame.transform.scale(empty_heart, (32, 32))


def load_cherry_sprites(dir1, dir2, width, height):
    path = join("assets", dir1, dir2)
    image = pygame.image.load(path).convert_alpha()
    sprites = []
    for i in range(image.get_width() // width):
        surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        rect = pygame.Rect(i * width, 0, width, height)
        surface.blit(image, (0, 0), rect)
        surface = pygame.transform.scale2x(surface)
        sprites.append(surface)
    return sprites


def get_block(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def get_background(name, width, height):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, img_width, img_height = image.get_rect()
    tiles = []

    for i in range(width // img_width + 1):
        for j in range(height // img_height + 1):
            pos = (i * img_width, j * img_height)
            tiles.append(pos)

    return tiles, image


def draw_text(window, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    window.blit(text_surface, (x, y))


def draw_scoreboard(window, cherries_eaten, lives, filled_heart_image, empty_heart_image):
    font = pygame.font.SysFont("Arial", 24, bold=True)

    text = f"Cherries: {cherries_eaten}"
    text_surface = font.render(text, True, (255, 255, 255))
    background_rect = pygame.Rect(5, 5, text_surface.get_width() + 20, text_surface.get_height() + 10)
    pygame.draw.rect(window, (0, 0, 0), background_rect)
    pygame.draw.rect(window, (255, 0, 0), background_rect, 2)
    window.blit(text_surface, (15, 10))

    heart_background_rect = pygame.Rect(window.get_width() - (3 * (filled_heart_image.get_width() + 5)) - 25, 5,
                                        (3 * (filled_heart_image.get_width() + 5)) + 20,
                                        filled_heart_image.get_height() + 10)
    pygame.draw.rect(window, (0, 0, 0), heart_background_rect)
    pygame.draw.rect(window, (255, 0, 0), heart_background_rect, 2)

    for i in range(3):
        if i < lives:
            window.blit(filled_heart_image, (
            window.get_width() - (3 * (filled_heart_image.get_width() + 5)) + i * (filled_heart_image.get_width() + 5) - 10, 10))
        else:
            window.blit(empty_heart_image, (
            window.get_width() - (3 * (filled_heart_image.get_width() + 5)) + i * (filled_heart_image.get_width() + 5) - 10, 10))


def draw_game_over(window):
    font = pygame.font.SysFont("Arial", 72, bold=True)
    text_surface = font.render("Game Over!", True, (255, 255, 255))
    rect = text_surface.get_rect(center=(window.get_width() // 2, window.get_height() // 2))

    overlay = pygame.Surface((window.get_width(), window.get_height()))
    overlay.fill((50, 50, 50))
    overlay.set_alpha(200)
    window.blit(overlay, (0, 0))

    window.blit(text_surface, rect)


def draw_win(window, cherries_eaten, total_cherries):
    font = pygame.font.SysFont("Arial", 72, bold=True)
    text_surface = font.render("Congratulations You Won!", True, (255, 255, 255))
    rect = text_surface.get_rect(center=(window.get_width() // 2, window.get_height() // 2 - 50))

    cherries_surface = font.render(f"Cherries: {cherries_eaten}/{total_cherries}", True, (255, 255, 255))
    cherries_rect = cherries_surface.get_rect(center=(window.get_width() // 2, window.get_height() // 2 + 50))

    overlay = pygame.Surface((window.get_width(), window.get_height()))
    overlay.fill((50, 50, 50))
    overlay.set_alpha(200)
    window.blit(overlay, (0, 0))

    window.blit(text_surface, rect)
    window.blit(cherries_surface, cherries_rect)


def draw(window, background, bg_image, player, objects, offset_x, offset_y, filled_heart_image, empty_heart_image):
    window.fill((0, 0, 0))

    bg_width, bg_height = bg_image.get_size()
    for i in range(-1, (window.get_width() // bg_width) + 2):
        for j in range(-1, (window.get_height() // bg_height) + 2):
            window.blit(bg_image, (i * bg_width - offset_x % bg_width, j * bg_height - offset_y % bg_height))

    for obj in objects:
        obj.draw(window, offset_x, offset_y)

    player.draw(window, offset_x, offset_y)

    draw_scoreboard(window, player.cherries_eaten, player.lives, filled_heart_image, empty_heart_image)

    if player.lives <= 0:
        draw_game_over(window)

    pygame.display.update()
