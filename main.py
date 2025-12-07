from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
import pygame

# Getting the first user input for the key config
print("### ENIGMA KEY SETUP ###")
rotors_str   = input("Rotors (default: I II III): ") or "I II III"
positions    = input("Positions (default: AAA): ").upper() or "AAA"
rings_str    = input("Rings (default: 0 0 0): ") or "0 0 0"
plugboard_str= input("Plugboard pairs (e.g. AR GK OX, default: none): ").upper() or ""
reflector_str= input("Reflector (A/B/C, default: A): ").upper() or "A"

rotor_names = rotors_str.split()
r1_name = rotor_names[0] if len(rotor_names) > 0 else "I"
r2_name = rotor_names[1] if len(rotor_names) > 1 else "II"
r3_name = rotor_names[2] if len(rotor_names) > 2 else "III"

ring_vals = [int(x) % 26 for x in rings_str.split() if x.isdigit()]
while len(ring_vals) < 3:
    ring_vals.append(0)
rings = ring_vals[:3]

plug_pairs = [[p[0], p[1]] for p in plugboard_str.split() if len(p) == 2]

# setting up the app
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Machine")
font = pygame.font.SysFont("Arial", 20)

HEIGHT = 600
WIDTH = 1200
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {"top":150, "bottom":50, "left":100, "right":100}
GAP = 75
INPUT ="Your text : "
OUTPUT ="Enciphered : "
PATH = []

NORMAL = pygame.font.SysFont("Arial", 14)
BOLD = pygame.font.SysFont("Arial", 14, bold=True)

A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

keyboard = Keyboard()

# build plugboard from pairs
plugboard = Plugboard(plug_pairs)

# choose reflector
reflector = {"A": A, "B": B, "C": C}.get(reflector_str, A)

# choose rotors
rotor_map = {"I": I, "II": II, "III": III, "IV": IV, "V": V}
r1 = rotor_map.get(r1_name, I)
r2 = rotor_map.get(r2_name, II)
r3 = rotor_map.get(r3_name, III)

ENIGMA = Enigma(keyboard, plugboard, r1, r2, r3, reflector)

# apply key and rings
ENIGMA.set_key(positions[:3])
ENIGMA.set_ring_settings(rings)

print("\nKey has been configured successfully. Close the console to change it again.\n")

# Program loop
animation = True
while animation:
  SCREEN.fill((9,58,62))

  text_input = BOLD.render(INPUT, True, "white")
  text_box = text_input.get_rect(center=(WIDTH/2, MARGINS["top"]/2))
  SCREEN.blit(text_input, text_box)

  text_output = NORMAL.render(OUTPUT, True, "gray")
  text_box = text_output.get_rect(center=(WIDTH / 2, MARGINS["top"] / 2 + 20))
  SCREEN.blit(text_output, text_box)

  ENIGMA.draw(SCREEN, PATH, WIDTH, HEIGHT, MARGINS, GAP, BOLD)

  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      animation = False
    elif event.type == pygame.KEYDOWN:
      # Clear text
      if event.key == pygame.K_DELETE:
        INPUT = "Your text : "
        OUTPUT = "Enciphered : "

      # Add a space
      elif event.key == pygame.K_SPACE:
        INPUT += " "
        OUTPUT += " "
      else:
        key = event.unicode
        if key in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
          letter = key.upper()
          INPUT += letter
          PATH, cipher_letter = ENIGMA.encipher(letter)
          OUTPUT += cipher_letter
          print(INPUT, OUTPUT)

pygame.quit()