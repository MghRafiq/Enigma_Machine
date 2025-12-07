# **Enigma Machine**

Project académique par :
*   Rafiq MAHROUG
*   Magnolia Amoussou Guenou

---
*Université Paris Cité - M2 MIAGE 2025/2026 - Cryptographie & Blockchain*

---


## About

This is a fully functional Enigma Machine, with all the components and cipher function.

**Note:** Enigma is symmetric - decrypt by running encrypted text through same configuration.

---
<img width="400" height="300" alt="Diagramme sans nom drawio (1)" src="https://github.com/user-attachments/assets/c8b3b1fd-cfb2-40bb-ad30-a51ee5f129f4" />

---

## We have built two versions

### **1 Colab Notebook (Browser)**

https://colab.research.google.com/drive/1YsfLa3pQiz-CxRuEcFZ79NCA28uyEHvd?usp=sharing

- **No installation required**
- Configure rotors, positions, rings, plugboard
- Encrypt/decrypt messages instantly
- Perfect for quick testing the key set up and the cipher function

### **2️ Desktop Simulator (Visual)**
- It requires a git clone, and getting inside the project's repository in your terminal
- Pip install pygame
- Python main.py
- First : you will need to set up the key in the terminal by following the instructions
- After the key configuration, you will have a Pop-up screen where you can type your messages and see the function and the encyphered text in real-time


### **Project Structure**

| File | Purpose |
|------|---------|
| `main.py` | Pygame GUI - configure key, watch rotors, encrypt messages |
| `keyboard.py` | Converts letters (A-Z) to positions (0-25) and back |
| `plugboard.py` | Implements plugboard swaps (AE, BM, etc.) |
| `rotor.py` | Rotor wiring, position tracking, mechanical rotation |
| `reflector.py` | Reflects signal back through rotors (3 historical models) |
| `enigma.py` | Core machine - signal routing, rotor stepping, encipher |
| `enigma_notebook.ipynb` | Colab version - text-based configuration + encryption |
| `requirements.txt` | `pygame==2.5.0` (desktop only) |

## Program Features

- **The 5 Historical Rotors** (I, II, III, IV, V)
- **3 Reflectors** (A, B, C)
- **Plugboard** (up to 10 letter pair substitutions)
- **Ring Settings** (rotor offset 0-25)
- **Initial Positions** (A-Z per rotor)
- **Double-Stepping** (authentic rotor mechanics)
- **Visual Animation** (rotor positions, signal path)

## Technologies

- **Python 3** - Programming Language
- **Pygame** - Python library for visual simulators (desktop version)
- **Jupyter** - Interactive notebook (Colab)

## Tests
### Google Colab version
<img width="371" height="266" alt="image" src="https://github.com/user-attachments/assets/d998c1bc-8f21-4c4a-949b-d2e4b4df95bb" />

### Desktop simulator
<img width="500" height="200" alt="image" src="https://github.com/user-attachments/assets/350fc2d2-69be-4ff9-b639-40670f51ad6f" />
<img width="500" height="200" alt="image" src="https://github.com/user-attachments/assets/7f8b0559-ecf7-4712-8ae6-2c31157b43da" />


---
