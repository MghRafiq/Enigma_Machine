"""
Keyboard.py
This class is used to convert between letters and their position (number) on the keyboard.
It respresents the keyboard as a list of letters in the Enigma Machine's alphabet.

It has two methods:
 - The forward method takes a letter and returns its position on the keyboard.
 - The backward method takes a position and returns the letter at that position.
"""
import pygame


class Keyboard:

  def forward(self, letter):
    position = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
    return position

  def backward(self, position):
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[position]
    return letter

  def draw(self, screen, x, y, w, h, font):
    # Silo
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, (255, 255, 255), rect, width=1, border_radius=15)

    # Letters
    for i in range(26):
      letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
      letter = letter.upper()
      letter = font.render(letter, True, "gray")
      text_box = letter.get_rect(center = (x+w/2, y+(i+1)*h/27))
      screen.blit(letter, text_box)