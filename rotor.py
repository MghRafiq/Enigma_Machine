"""
Rotor.py
This class is used to represent a rotor in the Enigma Machine

It has these methods:
 - The forward method takes a position and returns the position of the letter after passing through the rotor.
 - The backward method takes a position and returns the position of the letter before passing through the rotor.
 - The show method prints the rotor's wiring.
 - The rotate method rotates the rotor by one position.
 - The rotate_to_specific_letter method rotates the rotor to a specific letter.

"""
import pygame

class Rotor:

  def __init__(self, wiring, notch):
    self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    self.right = wiring
    self.notch = notch

  def forward(self, position):
    letter = self.right[position]
    position = self.left.find(letter)
    return position

  def backward(self, position):
    letter = self.left[position]
    position = self.right.find(letter)
    return position

  def show(self):
    print(self.left)
    print(self.right)
    print()

  def set_ring(self, position):
    # Backward rotation of the rotor
    self.rotate(position - 1, forward=False)

    # Adjusting the notch
    notch_position = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.notch)
    self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(notch_position - position + 1) % 26]

  def rotate(self, n = 1, forward = True):
    for i in range(n):
      if forward:
        self.left = self.left[1:] + self.left[0]
        self.right = self.right[1:] + self.right[0]
      else:
        self.left = self.left[25] + self.left[:25]
        self.right = self.right[25] + self.right[:25]

  def rotate_to_specific_letter(self, letter):
    n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
    self.rotate(n)

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

      #Highlight the top letter of the alphabet
      if i == 0:
        pygame.draw.rect(screen, "dark blue", text_box, border_radius=6)

      # Highlight notch
      if self.left[i] == self.notch:
        letter = font.render(self.left[i], True, "black")
        pygame.draw.rect(screen, "white", text_box, border_radius=6)

      screen.blit(letter, text_box)
      # Right side board
      letter = self.right[i]
      letter = letter.upper()
      letter = font.render(letter, True, "gray")
      text_box = letter.get_rect(center=(x + w*3/4, y + (i + 1) * h / 27))
      screen.blit(letter, text_box)