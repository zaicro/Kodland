import pygame
import sys
from button import Button

pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Animales")

ANIMALS = [
    {
        "name": "Perro",
        "video": "assets/images/dog.jpg",
        "image": "assets/images/dog.jpg",
    },
    {
        "name": "Gato",
        "video": "assets/images/cat.jpg",
        "image": "assets/images/cat.jpg",
    },
    {
        "name": "Conejo",
        "video": "assets/images/rabbit.jpg",
        "image": "assets/images/rabbit.jpg",
    },
    {
        "name": "Caballo",
        "video": "assets/images/horse.jpg",
        "image": "assets/images/horse.jpg",
    },
    {
        "name": "Pájaro",
        "video": "assets/images/bird.jpg",
        "image": "assets/images/bird.jpg",
    },
]
videos = {animal["name"]: animal["video"] for animal in ANIMALS}
BUTTONS = []


def animals_button():
    used_width = 0
    used_height = 0
    for animal in ANIMALS:
        width = 200
        height = 210
        margin = 10
        if used_width + width + margin > SCREEN.get_width():
            used_height = height + margin
            used_width = 0
        left = used_width + margin
        top = used_height + margin
        boton = Button(SCREEN, left, top, width, height)
        boton.set_text(animal["name"])
        boton.set_image(animal["image"])
        BUTTONS.append(boton)
        used_width += width + margin
    for boton in BUTTONS:
        boton.draw()


def animal_detail(image):
    while True:
        # image = pygame.image.load("assets/images/horse.jpg")
        SCREEN.fill((255, 255, 255))
        SCREEN.blit(
            image,
            (
                SCREEN.get_width() / 2 - image.get_width() / 2,
                SCREEN.get_height() / 2 - image.get_height() / 2,
            ),
        )
        btn_back = Button(
            SCREEN, SCREEN.get_width() - 110, SCREEN.get_height() - 60, 100, 50
        )
        btn_back.set_text("Atras")
        btn_back.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_back.click(pygame.mouse.get_pos()):
                    main()

        pygame.display.update()


def quit():
    pygame.quit()
    sys.exit()


def main():
    while True:
        SCREEN.fill((255, 255, 255))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        animals_button()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for boton in BUTTONS:
                    if boton.click(MENU_MOUSE_POS):
                        video = videos.get(boton.text)
                        if video:
                            animal_detail(boton.image)

        pygame.display.update()


main()
