# 🔐 Simple Password Generator

A beginner-friendly command-line password generator written in pure Python.
No external libraries required — only Python's built-in `random` and `string` modules.

---

## Features

- Choose a custom password length (minimum 4 characters)
- Select any combination of character types:
  - **Uppercase letters** (A–Z)
  - **Lowercase letters** (a–z)
  - **Numbers** (0–9)
  - **Special characters** (!@#$%^&*…)
- Every selected character type is guaranteed to appear at least once
- Coloured terminal output for a pleasant user experience
- Loop to generate multiple passwords in one session
- Robust input validation with clear error messages

---

## Requirements

- Python **3.10** or higher  
  *(Uses built-in type-hint syntax `dict[str, str]` available from 3.9+)*
- No third-party packages needed

---

## Getting Started

### 1. Clone or download the project

```bash
git clone https://github.com/your-username/Simple_Password_Generator.git
cd Simple_Password_Generator
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> There are no third-party dependencies; this step is a no-op but good practice.

### 4. Run the program

```bash
python main.py
```

---

## Usage Example

```
╔═══════════════════════════════════════╗
║        🔐  Password Generator         ║
╚═══════════════════════════════════════╝

Enter desired password length (min 4): 16

Choose character types to include:
  [1] Uppercase letters (A-Z)
  [2] Lowercase letters (a-z)
  [3] Numbers        (0-9)
  [4] Special chars  (!@#…)

Enter option numbers separated by spaces (e.g. 1 2 3): 1 2 3 4

✔  Generated Password:
   gT7#mXp2@Lq5!Kn9

Generate another password? (y/n): n

Goodbye! Stay secure. 🔒
```

---

## Input Validation

| Invalid Input                  | Error Message                                          |
|-------------------------------|--------------------------------------------------------|
| Non-numeric length             | `✖  Please enter a positive whole number.`             |
| Length less than 4             | `✖  Length must be at least 4 characters.`             |
| Invalid option number          | `✖  '<token>' is not a valid option. Try again.`       |
| No character type selected     | `✖  You must select at least one character type.`      |

---

## Project Structure

```
Simple_Password_Generator/
├── main.py          # Main application
├── requirements.txt # Dependencies (none)
└── README.md        # This file
```

---

## How It Works

1. **Get length** — validates that input is a positive integer ≥ 4.  
2. **Get character pools** — user picks one or more of the four character sets.  
3. **Generate password** — picks one character guaranteed from each chosen pool, fills the rest randomly from the combined pool, then shuffles everything so the guarantee characters aren't always at the front.  
4. **Display & loop** — prints the result and asks whether to generate another.

---

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).
