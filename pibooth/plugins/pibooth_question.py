import time
import pygame
import pibooth
from pibooth import pictures, fonts
from pibooth.utils import LOGGER, PoolingTimer


def draw_rounded_rect(surface, rect, color, corner_radius):
    """Draw a rectangle with rounded corners on the specified surface."""
    if corner_radius < 0:
        raise ValueError(f"Corner radius {corner_radius} must be >= 0")
    elif corner_radius > min(rect.width, rect.height) / 2:
        raise ValueError(f"Corner radius {corner_radius} is too large for the rectangle")

    pygame.draw.rect(surface, color, rect.inflate(-2 * corner_radius, -2 * corner_radius))
    pygame.draw.circle(surface, color, rect.topleft, corner_radius)
    pygame.draw.circle(surface, color, rect.topright, corner_radius)
    pygame.draw.circle(surface, color, rect.bottomleft, corner_radius)
    pygame.draw.circle(surface, color, rect.bottomright, corner_radius)
    pygame.draw.rect(surface, color, rect.inflate(-2 * corner_radius, 0))
    pygame.draw.rect(surface, color, rect.inflate(0, -2 * corner_radius))


@pibooth.hookimpl
def state_wait_exit(win):
    """Display the questionary on the screen just after exiting the wait state."""
    win_rect = win.get_rect()
    text = "Question :"

    # Get best font size according to window size
    # Adjust the size to be smaller
    font = fonts.get_pygame_font(text, fonts.CURRENT,
                                 win_rect.width // 5, win_rect.height // 10)

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
    win.surface.blit(text_surface, text_surface.get_rect(center=(win_rect.centerx, win_rect.height // 10)).topleft)

    question = "What is the answer to life, the universe and everything ?"
    question_surface = font.render(question, True, win.text_color)
    win.surface.blit(question_surface,
                     question_surface.get_rect(center=(win_rect.centerx, win_rect.height // 4)).topleft)

    answer = ["42", "43", "44", "69"]
    answer_surface = []
    for i in range(len(answer)):
        # Render the answer text in black
        answer_surface.append(font.render(answer[i], True, (0, 0, 0)))
        if i == 0:
            pos = (win_rect.centerx, win_rect.height // 1.5 - win_rect.height // 10)
        elif i == 1:
            pos = (win_rect.centerx - win_rect.width // 10, win_rect.height // 1.5)
        elif i == 2:
            pos = (win_rect.centerx, win_rect.height // 1.5 + win_rect.height // 10)
        else:
            pos = (win_rect.centerx + win_rect.width // 10, win_rect.height // 1.5)
        answer_rect = answer_surface[i].get_rect(center=pos)
        draw_rounded_rect(win.surface, answer_rect.inflate(10, 10), (255, 255, 255), 10)
        win.surface.blit(answer_surface[i], answer_rect.topleft)

    # Force screen update and events process
    pygame.display.update()
    pygame.event.pump()

    # Wait 1s
    time.sleep(5)
