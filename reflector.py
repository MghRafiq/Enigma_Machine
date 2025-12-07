"""
Reflector.py
This class is used to represent a reflector in the Enigma Machine

It works just like the rotor but instead of forward and backward it is just a mirror.

We copied the same code from the rotor class.

"""
import pygame
class Reflector:

  def __init__(self, wiring):
    self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    self.right = wiring

  def reflect(self, position):
    letter = self.right[position]
    position = self.left.find(letter)
    return position

  def draw(self, screen, x, y, w, h, font):
    # Silo
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, (255, 255, 255), rect, width=1, border_radius=15)

    # Letters
    for i in range(26):
      # Left side board
      letter = self.left[i]
      letter = letter.upper()
      letter = font.render(letter, True, "gray")
      text_box = letter.get_rect(center = (x+w/4, y+(i+1)*h/27))
      screen.blit(letter, text_box)
      # Right side board
      letter = self.right[i]
      letter = letter.upper()
      letter = font.render(letter, True, "gray")
      text_box = letter.get_rect(center=(x + w*3/4, y + (i + 1) * h / 27))
      screen.blit(letter, text_box)