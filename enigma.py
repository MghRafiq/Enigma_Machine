"""
Enigma.py
This class is used to represent an Enigma Machine

An Enigma machine has these components :
 - A keyboard
 - A plugboard
 - Three rotors (At least)
 - A reflector

It has one method which is symetrical for encoding and decoding :
 - It takes a letter and returns the enciphered letter.

The rotation of the rotors is done automatically after each letter is encoded
 - Rotor 3 rotates every time a letter is encoded
 - Rotor 2 rotates when Rotor 3 reaches its notch
 - Rotor 1 rotates when Rotor 2 reaches its notch
 - There's also what is known as double stepping where all the rotors rotate when a Rotor 2 reaches its notch.
"""
import pygame

class Enigma:

  def __init__(self, keyboard, plugboard, rotor_1, rotor_2, rotor_3, reflector):
    self.keyboard = keyboard
    self.plugboard = plugboard
    self.rotor_1 = rotor_1
    self.rotor_2 = rotor_2
    self.rotor_3 = rotor_3
    self.reflector = reflector

  def set_key(self, key):
    self.rotor_1.rotate_to_specific_letter(key[0])
    self.rotor_2.rotate_to_specific_letter(key[1])
    self.rotor_3.rotate_to_specific_letter(key[2])

  def set_ring_settings(self, ring_settings):
    self.rotor_1.set_ring(ring_settings[0])
    self.rotor_2.set_ring(ring_settings[1])
    self.rotor_3.set_ring(ring_settings[2])


  def encipher(self, letter):
    # Rotation of the rotors
    if self.rotor_3.left[0] == self.rotor_3.notch and self.rotor_2.left[0] != self.rotor_2.notch:
      self.rotor_1.rotate()
      self.rotor_2.rotate()
      self.rotor_3.rotate()
    elif self.rotor_2.left[0] == self.rotor_2.notch:
      self.rotor_1.rotate()
      self.rotor_2.rotate()
      self.rotor_3.rotate()
    elif self.rotor_3.left[0] == self.rotor_3.notch:
      self.rotor_2.rotate()
      self.rotor_3.rotate()
    else:
      self.rotor_3.rotate()

    # The letter triggers a signal that goes through the machine and then comes back as an enciphered letter
    position = self.keyboard.forward(letter)
    path = [position, position]
    position = self.plugboard.forward(position)
    path.append(position)
    path.append(position)
    position = self.rotor_3.forward(position)
    path.append(position)
    path.append(position)
    position = self.rotor_2.forward(position)
    path.append(position)
    path.append(position)
    position = self.rotor_1.forward(position)
    path.append(position)
    path.append(position)
    position = self.reflector.reflect(position)
    path.append(position)
    path.append(position)
    path.append(position)
    position = self.rotor_1.backward(position)
    path.append(position)
    path.append(position)
    position = self.rotor_2.backward(position)
    path.append(position)
    path.append(position)
    position = self.rotor_3.backward(position)
    path.append(position)
    path.append(position)
    position = self.plugboard.backward(position)
    path.append(position)
    path.append(position)
    letter = self.keyboard.backward(position)

    return path, letter

  def draw(self, screen, path, width, height, margins, gap, font):
    # Variables
    x = margins["left"]
    y = margins["top"]
    w = (width - x - margins["right"] - gap*5)/6
    h = height - margins["bottom"] - margins["top"]

    # draw path
    y_path = [margins["top"] + (position+1)*h/27 for position in path]
    x_path = [width - margins["right"]-w/2] # Keyboard
    for i in [4, 3, 2, 1, 0]:  # Forward components path
      x_path.append(margins["left"] + i * (w + gap) + w * 3 / 4)
      x_path.append(margins["left"] + i * (w + gap) + w * 1 / 4)
    x_path.append(margins["left"] + w * 3 / 4) # reflector
    for i in [1,2,3,4]: # Backward components path
      x_path.append(margins["left"] + i*(w+gap)+w*1/4)
      x_path.append(margins["left"] + i* (w + gap) + w * 3 / 4)
    x_path.append(width - margins["right"] - w / 2)  # lamps

    if len(path) > 0:
      for i in range(1, 21):
        if i < 10:
          color = "red"
        elif i < 12:
          color = "orange"
        else :
          color = "dark green"
        starting_point = (x_path[i-1], y_path[i-1])
        ending_point = (x_path[i], y_path[i])
        pygame.draw.line(screen, color, starting_point, ending_point, width = 4)

    # draw machine components
    for component in [self.reflector, self.rotor_1, self.rotor_2, self.rotor_3, self.plugboard, self.keyboard]:
      component.draw(screen, x, y, w, h, font)
      x += w + gap

    # Components names
    names = ["Reflector", "Rotor 1", "Rotor 2", "Rotor 3", "Plugboard", "Keys/lamps"]
    y = margins["top"] * 3 / 4 + 20
    for i in range(0, 6):
      x = margins["left"]+w/2 + i * (w+gap)
      title = font.render(names[i], True, "gray")
      text_box = title.get_rect(center = (x, y))
      screen.blit(title, text_box)

