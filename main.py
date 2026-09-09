"""
Simple Password Generator
Uses Python's built-in `random` and `string` modules.
Run with: python main.py
"""

__version__ = "1.0.0"
__author__  = "tom-shaji"

import io
import random
import string
import sys

# Force UTF-8 output so box-drawing chars and emoji render on Windows terminals
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


# ── ANSI colour helpers (no external deps needed) ──────────────────────────────
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RED    = "\033[91m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

# ── Configuration ──────────────────────────────────────────────────────────────
MIN_LENGTH = 4    # minimum allowed password length
MAX_LENGTH = 128  # maximum allowed password length

BANNER = f"""{CYAN}{BOLD}
+---------------------------------------+
|       [*]  Password Generator         |
+---------------------------------------+{RESET}
"""


def get_yes_no(prompt: str) -> bool:
    """Ask a yes/no question; return True for 'y'/'yes'."""
    return input(f"{CYAN}{prompt} (y/n): {RESET}").strip().lower() in ("y", "yes")


def get_password_length() -> int:
    """Prompt the user for a valid password length (>= 4)."""
    while True:
        raw = input(f"{CYAN}Enter desired password length (min {MIN_LENGTH}): {RESET}").strip()
        if not raw.isdigit():
            print(f"{RED}✖  Please enter a positive whole number.{RESET}")
            continue
        length = int(raw)
        if length < MIN_LENGTH:
            print(f"{RED}✖  Length must be at least {MIN_LENGTH} characters.{RESET}")
            continue
        if length > MAX_LENGTH:
            print(f"{RED}✖  Length must be at most {MAX_LENGTH} characters.{RESET}")
            continue
        return length


def get_character_options() -> dict[str, str]:
    """
    Ask the user which character types to include.
    Returns a dict mapping label → character pool string.
    """
    options = {
        "Uppercase letters (A-Z)": string.ascii_uppercase,
        "Lowercase letters (a-z)": string.ascii_lowercase,
        "Numbers        (0-9)   ": string.digits,
        "Special chars  (!@#…)  ": string.punctuation,
    }

    print(f"\n{CYAN}Choose character types to include:{RESET}")
    keys = list(options.keys())
    for i, label in enumerate(keys, start=1):
        print(f"  {YELLOW}[{i}]{RESET} {label}")

    selected: dict[str, str] = {}
    while not selected:
        raw = input(
            f"\n{CYAN}Enter option numbers separated by spaces (e.g. 1 2 3): {RESET}"
        ).strip()

        chosen_indices = []
        valid = True
        for token in raw.split():
            if token.isdigit() and 1 <= int(token) <= len(keys):
                chosen_indices.append(int(token) - 1)
            else:
                print(f"{RED}✖  '{token}' is not a valid option. Try again.{RESET}")
                valid = False
                break

        if not valid:
            continue

        if not chosen_indices:
            print(f"{RED}✖  You must select at least one character type.{RESET}")
            continue

        # Deduplicate while preserving order
        seen = set()
        for idx in chosen_indices:
            if idx not in seen:
                label = keys[idx]
                selected[label] = options[label]
                seen.add(idx)

    return selected


def generate_password(length: int, char_pools: dict[str, str]) -> str:
    """
    Generate a random password of `length` characters.

    Guarantees at least one character from every selected pool,
    then fills the remainder randomly from the combined pool.
    """
    pools = list(char_pools.values())
    combined = "".join(pools)

    # One guaranteed character from each selected pool
    guaranteed = [random.choice(pool) for pool in pools]

    # Fill the rest from the combined pool
    remainder = random.choices(combined, k=length - len(guaranteed))

    password_chars = guaranteed + remainder
    random.shuffle(password_chars)          # avoid predictable prefix pattern
    return "".join(password_chars)


def main() -> None:
    print(BANNER)

    while True:
        # ── Step 1: length ──────────────────────────────────────────────────
        length = get_password_length()

        # ── Step 2: character types ─────────────────────────────────────────
        char_pools = get_character_options()

        # ── Step 3: generate & display ──────────────────────────────────────
        password = generate_password(length, char_pools)
        print(f"\n{GREEN}{BOLD}>> Generated Password:{RESET}")
        print(f"   {BOLD}{password}{RESET}\n")

        # ── Step 4: go again? ───────────────────────────────────────────────
        print()
        if not get_yes_no("Generate another password?"):
            print(f"{GREEN}Goodbye! Stay secure.{RESET}\n")
            break
        print()


if __name__ == "__main__":
    main()
