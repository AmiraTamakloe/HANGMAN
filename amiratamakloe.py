import pygame
import sys
import random
from pygame.locals import *


def draw_btns(buttons):
    for box, letter in buttons:
        btn_text = btn_font.render(letter, True, black)
        btn_rect = btn_text.get_rect(center = (box.x + 20, box.y + 20))
        screen.blit(btn_text, btn_rect)
        pygame.draw.rect(screen, black, box, 4 )

def display_guess():
    display_text = ''

    for letter in Word:
        if letter in Guessed:
            display_text += f"{letter}"
        else:
            display_text += "_ "

    text = letter_font.render(display_text, True, black)
    screen.blit(text, (500, 400))

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Amira's Hangman special edition")

game_over = False

white = (255, 255, 255)
black = (0,0,0)

#image
images = []
hangman_status = 0
for i in range(4,10,1):
    image = pygame.image.load(f'Images/{i}.jpg')
    images.append(image)

# buttons
rows = 2
cols = 13
gap = 20
size = 40
boxes = []

for row in range(rows):
    for col in range(cols):
        x = ((col * gap) + (size * col)) + 100
        y = ((row * gap) + (size * row)) + 600
        box = pygame.Rect(x,y, size, size)
        boxes.append(box)

buttons = []
A = 65

for ind, box in enumerate(boxes):
    letter = chr(A + ind)
    button = [box, letter]
    buttons.append(button)
# Words
Words = ["AMIRA", "TAMAKLOE"]
Word = random.choice(Words)
Guessed = []
# fonts
btn_font = pygame.font.SysFont("Times", 30)
game_font = pygame.font.SysFont('Times', 70)
letter_font = pygame.font.SysFont("Times", 50)

# title
title = "Amira's hangman special edition"
title_text = game_font.render(title, True, black)
title_rect = title_text.get_rect(center=(WIDTH//2, title_text.get_height()//2+10))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            clicked_pos = event.pos

            for button, letter in buttons:
                if button.collidepoint(clicked_pos):
                    if letter not in Word:
                        hangman_status += 1

                    if hangman_status == 8:
                        game_over = True

                    Guessed.append(letter)
                    buttons.remove([button, letter])
    screen.fill(white)
    screen.blit(images[hangman_status], (100, 150))
    screen.blit(title_text, title_rect)
    draw_btns(buttons)
    display_guess()


    for box in boxes :
        pygame.draw.rect(screen, black, box, 2)

    won = True
    for letter in Word:
        if letter not in Guessed:
            won = False

    if won:
        game_over = True
        game_over_message = "You Smartypant!!!"
    else:
        game_over_message = "You suck!!"
    pygame.display.update()
    clock.tick(50)

    if game_over:
        screen.fill(white)
        text = game_font.render(game_over_message, True, black)
        text_rect = text.get_rect(center = (WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()


