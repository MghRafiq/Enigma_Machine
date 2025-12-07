"""
Plugboard.py
This class is used to connect pairs of letters in the Enigma Machine.

It has two pairs of alphabet : left and right.

It has two methods:
 - The forward method takes a position and returns the position of the letter connected to it.
 - The backward method takes a position and returns the position of the letter connected to it.

"""
import pygame

class Plugboard:

  def __init__(self, pairs):
    self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for pair in pairs:
      A = pair[0]
      B = pair[1]
      position_A = self.left.find(A)
      position_B = self.left.find(B)
      self.left = self.left[:position_A] + B + self.left[position_A+1:]
      self.left = self.left[:position_B] + A + self.left[position_B+1:]

  def forward(self, position):
    letter = self.right[position]
    position = self.left.find(letter)
    return position

  def backward(self, position):
    letter = self.left[position]
    position = self.right.find(letter)
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