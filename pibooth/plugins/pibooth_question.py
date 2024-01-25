import time
import pygame
import pibooth
from pibooth import pictures, fonts
from pibooth.utils import LOGGER, PoolingTimer


@pibooth.hookimpl
def state_wait_exit(win):
    """Display the questionary on the screen just after exiting the wait state."""
    win_rect = win.get_rect()
    text = "Question :"

    # Get best font size according to window size
    # Adjust the size to be smaller
    font = fonts.get_pygame_font(text, fonts.CURRENT,
                                 win_rect.width//5, win_rect.height//10)

    # Build a surface to display at screen
    text_surface = font.render(text, True, win.text_color)

    # Clear screen
    if isinstance(win.bg_color, (tuple, list)):
        win.surface.fill(win.bg_color)
    else:
        bg_surface = pictures.get_pygame_image(win.bg_color, win_rect.size, crop=True, color=None)
        win.surface.blit(bg_surface, (0, 0))

    # Draw the surface at screen
    # Adjust the position to be at the top of the screen
    win.surface.blit(text_surface, text_surface.get_rect(center=(win_rect.centerx, win_rect.height//10)).topleft)


    question = "What is the answer to life, the universe and everything ?"
    question_surface = font.render(question, True, win.text_color)
    win.surface.blit(question_surface, question_surface.get_rect(center=(win_rect.centerx, win_rect.height//4)).topleft)

    answer = ["42", "43", "44", "69"]
    answer_surface = []
    for i in range(len(answer)):
        answer_surface.append(font.render(answer[i], True, win.text_color))
        if i == 0:
            pos = (win_rect.centerx, win_rect.height//2 - win_rect.height//10)
        elif i == 1:
            pos = (win_rect.centerx - win_rect.width//10, win_rect.height//2)
        elif i == 2:
            pos = (win_rect.centerx, win_rect.height//2 + win_rect.height//10)
        else:
            pos = (win_rect.centerx + win_rect.width//10, win_rect.height//2)
        win.surface.blit(answer_surface[i], answer_surface[i].get_rect(center=pos).topleft)

    # Force screen update and events process
    pygame.display.update()
    pygame.event.pump()

    # Wait 1s
    time.sleep(10)