# Changelog

All notable changes are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

## [1.0.0] - 2026-09-10

### Added
- Command-line password generator using only standard library modules
- Configurable length ({MIN_LENGTH}-{MAX_LENGTH} characters)
- Four character pools: uppercase, lowercase, digits, special characters
- Guaranteed inclusion of at least one char from each selected pool
- Password strength indicator (Weak / Medium / Strong / Very Strong)
- Entropy display in bits
- Session counter tracking how many passwords were generated
- Coloured ANSI terminal output
- Robust input validation with clear error messages
- Looping mode to generate multiple passwords without restarting
