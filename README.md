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


## We have built two versions

### **1 Colab Notebook (Browser)**

https://colab.research.google.com/drive/1YsfLa3pQiz-CxRuEcFZ79NCA28uyEHvd?usp=sharing

- **No installation required**
- Configure rotors, positions, rings, plugboard
- Encrypt/decrypt messages instantly
- Perfect for quick testing the key set up and the cipher function

### **2️ Desktop Simulator (Visual)**
- it requires a git clone, and getting inside the project's repository in your terminal
- pip install pygame
- python main.py
- First : you will need to set up the key in the terminal by following the instructions
- After the key configuration, you will have a Pop-up screen where you can type your messages and see the function and the encyphered text in real-time


### **File Descriptions**

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

## Technologies

- **Python 3** - Programming Language
- **Pygame** - Python library for visual simulators (desktop version)
- **Jupyter** - Interactive notebook (Colab)

---
