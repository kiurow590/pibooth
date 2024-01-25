import time
import pygame
import pibooth
from pibooth import pictures, fonts
from pibooth.utils import LOGGER, PoolingTimer


class Button:
    def __init__(self, text, pos, font, color=(0, 0, 0), bg_color=(255, 255, 255), radius=10):
        self.text = text
        self.pos = pos
        self.font = font
        self.color = color
        self.bg_color = bg_color
        self.radius = radius
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(center=self.pos)

    def draw(self, win):
        draw_rounded_rect(win, self.rect.inflate(10, 10), self.bg_color, self.radius)
        win.blit(self.surface, self.rect.topleft)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False


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
    buttons = []
    for i in range(len(answer)):
        if i == 0:
            pos = (win_rect.centerx, win_rect.height // 1.5 - win_rect.height // 10)
        elif i == 1:
            pos = (win_rect.centerx - win_rect.width // 10, win_rect.height // 1.5)
        elif i == 2:
            pos = (win_rect.centerx, win_rect.height // 1.5 + win_rect.height // 10)
        else:
            pos = (win_rect.centerx + win_rect.width // 10, win_rect.height // 1.5)
        buttons.append(Button(answer[i], pos, font))

    for button in buttons:
        button.draw(win.surface)

    # Force screen update and events process
    pygame.display.update()
    pygame.event.pump()

    # Wait for a click on a button
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for button in buttons:
                if button.is_clicked(event):
                    print(f"You clicked on {button.text}")
                    running = False
        time.sleep(1)
