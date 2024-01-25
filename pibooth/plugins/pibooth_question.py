"""Plugin to display questionary on the screen just after exiting the wait state."""

import time
import pygame
import pibooth
from pibooth import pictures, fonts

__version__ = "0.0.2"


@pibooth.hookimpl
def state_wait_exit(win):
    """Display the questionary on the screen just after exiting the wait state."""
    win_rect = win.get_rect()
    # on clear l'écran
    if isinstance(win.bg_color, (tuple, list)):
        win.surface.fill(win.bg_color)
    else:
        bg_surface = pictures.get_pygame_image(win.bg_color, win_rect.size, crop=True, color=None)
        win.surface.blit(bg_surface, (0, 0))
    
    # afficher la question dans le haut de l'écran
    text = "Questionnaire"
    font = fonts.get_pygame_font(text, fonts.CURRENT,
                                 win_rect.width//0.5, win_rect.height//1)
    text_surface = font.render(text, True, win.text_color)
    win.surface.blit(text_surface, text_surface.get_rect(center=win_rect.center).topleft)
    
    # afficher les réponses possibles dans le bas de l'écran sous forme de losange
    text = "1"
    font = fonts.get_pygame_font(text, fonts.CURRENT,
                                 win_rect.width//1.5, win_rect.height//1.5)
    text_surface = font.render(text, True, win.text_color)
    win.surface.blit(text_surface, text_surface.get_rect(center=win_rect.center).topleft)
    
    text = "2"
    font = fonts.get_pygame_font(text, fonts.CURRENT,
                                 win_rect.width//1.5, win_rect.height//1.5)
    text_surface = font.render(text, True, win.text_color)
    win.surface.blit(text_surface, text_surface.get_rect(center=win_rect.center).topleft)
    
    text = "3"
    font = fonts.get_pygame_font(text, fonts.CURRENT,
                                 win_rect.width//1.5, win_rect.height//1.5)
    text_surface = font.render(text, True, win.text_color)
    win.surface.blit(text_surface, text_surface.get_rect(center=win_rect.center).topleft)
    
    text = "4"
    font = fonts.get_pygame_font(text, fonts.CURRENT,
                                 win_rect.width//1.5, win_rect.height//1.5)
    text_surface = font.render(text, True, win.text_color)
    win.surface.blit(text_surface, text_surface.get_rect(center=win_rect.center).topleft)
    
    # cliquer sur un losange pour valider la réponse
    # si la réponse est valide, afficher "Merci"
    # si la réponse est invalide, afficher "Réponse invalide"
    
    
    
    # Force screen update and events process
    pygame.display.update()
    pygame.event.pump()
    
    
    
    # Wait 1s
    time.sleep(5)
