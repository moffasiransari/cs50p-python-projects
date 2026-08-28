# 🐍 CS50P — Introduction to Programming with Python

> My complete journey through Harvard's CS50P course — all problem sets, exercises, and personal projects built along the way, capped off with my final project: **MedSaver**.
> Started this before joining college. Every file here is something I wrote, debugged, and learned from.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![CS50P](https://img.shields.io/badge/Course-CS50P-crimson?style=flat)
![Status](https://img.shields.io/badge/Status-Course%20Complete%20%E2%9C%85-brightgreen?style=flat)
![Final Project](https://img.shields.io/badge/Final%20Project-MedSaver%20💊-9cf?style=flat)
![Self Taught](https://img.shields.io/badge/Self--Taught-Pre--College-orange?style=flat)

---
`Took help of Claude to make this README file`
## 📁 Repository Structure

```
cs50p-python-projects/
├── CS50_final_project/    # 🏆 MedSaver — final project
│   ├── medicin.py
│   ├── project.py
│   ├── report.py
│   ├── database.csv
│   ├── history.csv
│   ├── med_report.csv
│   ├── requirements.txt
│   ├── test_project.py
│   ├── MedSaver_Report.pdf
│   └── README.md
├── prblm_sets/
│   ├── prblm_set_0/      # Functions, Variables
│   ├── prblm_set_1/      # Conditionals
│   ├── prblm_set_2/      # Loops
│   ├── prblm_set_3/      # Exceptions
│   ├── prblm_set_4/      # Libraries
│   ├── prblm_set_5/      # Unit Tests
│   ├── prblm_set_6/      # File I/O
│   ├── prblm_set_7/      # Regular Expressions
│   ├── prblm_set_8/      # Object-Oriented Programming
│   └── prblm_set_9/      # Et Cetera
├── 1projects/            # My own personal projects
├── qs_by_codinx/         # 22+ extra practice problems
├── thonny_p/             # Pattern & logic programs
```

---

## 🏆 Final Project — MedSaver

> **MedSaver — Generic Medicine Finder & Price Comparison**
> A CLI tool that takes a branded medicine name and returns its generic equivalent, full composition, dosage, safety notes, and a branded-vs-generic price comparison — so people can save money without compromising on treatment.

### What it does
- Takes a **branded medicine name** as input (e.g. `Allegra`)
- Looks up the **generic name & composition** (e.g. `Fexofenadine` / `Fexofenadine Hydrochloride`)
- Flags whether a **doctor's prescription is required**
- Returns **dosage** and **safety notes** (interactions, warnings, who should avoid it)
- Runs a **branded vs. generic price comparison** and calculates **savings**
- Logs every search to a local history file
- Generates a clean, shareable **PDF report** of the result

### Sample Output (from `MedSaver_Report.pdf`)

| Field | Example |
|---|---|
| Input Brand | Allegra |
| Generic | Fexofenadine |
| Composition | Fexofenadine Hydrochloride |
| Doctor Prescription Required? | Yes |
| Dosage | 120 mg Tablet |
| Branded Price (₹) | 180.0 |
| Generic Price (₹) | 75.0 |
| **Savings (₹)** | **105.0** |

### Built With
- **Google Gemini API** (`google-genai`, `google-api-core`) — for AI-powered medicine data lookup
- **Pydantic** — structured, validated data models for medicine info
- **Rich** — polished, readable CLI output
- **ReportLab** — auto-generates the PDF report
- **pytest** — unit testing (`test_project.py`)

```txt
google-genai==2.6.0
google-api-core==2.30.3
pydantic==2.13.4
rich==15.0.0
reportlab==4.5.1
```

---

## 📚 Problem Sets

### Set 0 — Functions & Variables
> Einstein's mass-energy formula, face printing, indoor voice, playback speed, tip calculator

| File | What it does |
|------|-------------|
| `einstein.py` | Calculates E=mc² given mass input |
| `faces.py` | Converts `:)` emoticons to emoji |
| `indoor.py` | Converts text to lowercase (indoor voice) |
| `playback.py` | Replaces spaces with `...` for speech effect |
| `tip.py` | Calculates restaurant tip percentage |

---

### Set 1 — Conditionals
> Deep thought, extensions, interpreter check, meal time

| File | What it does |
|------|-------------|
| `bank.py` | Outputs greeting based on user input |
| `deep.py` | Responds to the meaning of life |
| `extensions.py` | Identifies file type from extension |
| `interpreter.py` | Evaluates simple math expressions |
| `meal.py` | Tells you what meal time it is |

---

### Set 2 — Loops
> Camel case, Coke machine, nutrition facts, plates validator

| File | What it does |
|------|-------------|
| `camel.py` | Converts camelCase to snake_case |
| `coke.py` | Simulates a coke vending machine |
| `nutrition.py` | Looks up calories from a food database |
| `plates.py` | Validates custom vanity license plates |
| `rough.py` | Practice/scratch file |
| `twttr.py` | Removes vowels like a tweet |

---

### Set 3 — Exceptions
> Fuel gauge, grocery list, outdated dates, taqueria menu

| File | What it does |
|------|-------------|
| `fuel.py` | Converts fractions to fuel percentage |
| `grocery.py` | Counts grocery items and sorts them |
| `outdated.py` | Converts date formats (e.g. 9/8/1636 → 1636-09-08) |
| `taqueria.py` | Felipe's Taqueria order calculator |

---

### Set 4 — Libraries
> Adieu, bitcoin price, emojize, figlet fonts, game show, professor quiz

| File | What it does |
|------|-------------|
| `adieu.py` | Bids farewell using Oxford comma grammar |
| `bitcoin.py` | Fetches live Bitcoin price via API |
| `emojize.py` | Converts text codes to emoji |
| `figlet.py` | Prints text in ASCII art fonts |
| `game.py` | Number guessing game |
| `professor.py` / `professor1.py` | Math quiz generator |
| `tempCodeRunnerFile.py` | Auto-generated runner |

---

### Set 5 — Unit Tests
> Writing and passing tests with pytest

| File | What it does |
|------|-------------|
| `bank.py` + `test_bank.py` | Tests greeting logic |
| `fuel.py` + `test_fuel.py` | Tests fuel fraction conversion |
| `plates.py` + `test_plates.py` | Tests vanity plate validator |
| `twttr.py` + `test_twttr.py` | Tests vowel removal |

---

### Set 6 — File I/O
> CSV files, pizza menus, scourgify data

| File | What it does |
|------|-------------|
| `hello.py` | Reads/writes names to a file |
| `lines.py` | Counts lines of code in a Python file |
| `pizza.py` | Renders a pizza menu from CSV as a table |
| `regular.csv` / `sicilian.csv` | Pizza menu data |
| `scourgify.py` | Cleans up a CSV file (name formatting) |
| `before.csv` / `after.csv` | Input/output for scourgify |

---

### Set 7 — Regular Expressions
> NUMB3RS, working hours, watch patterns, shirt API

| File | What it does |
|------|-------------|
| `numb3rs.py` | Validates IPv4 addresses with regex |

---

### Set 8 — Object-Oriented Programming
> Classes, inheritance, dunder methods

| File | What it does |
|------|-------------|
| _add your files here_ | |

---

### Set 9 — Et Cetera
> List comprehensions, generators, decorators, and other Python odds & ends

| File | What it does |
|------|-------------|
| _add your files here_ | |

---

## 🚀 My Personal Projects

> Built independently — not part of CS50 assignments.

| Project | Description |
|---------|-------------|
| `weather_api/` | Fetches live weather data using an API |
| `1.report1.py` | Report generation script |
| `2.game_history.py` | Tracks game history and scores |
| `21_unit_convrsion.py` | Unit converter (single function for multiple conversions) |
| `guess_no_game.py` | Number guessing game with hints |
| `imprv_guess_no_game.py` | Improved version with better UX |
|`rock_paper_scissor`| Rock, Paper, and Scissor Game|
---

## 💪 Extra Practice

### `qs_by_codinx/` — 22 Practice Problems
Problems I solved from external sources to reinforce concepts:
`celsius_to_fahrenheit` · `swap_number` · `num_reverser` · `odd_even_check` · `leap_year` · `euclidean_dist` · `triangle_possibility` · `profit_loss_calc` · `interest_finder` · `compound_interest` · `volume` · `div_by_3.6` · `weather` · `square` · `armstrong_num` · `narcissist_num` · `inhand_salary` · `dog_chicken` · and more

### `thonny_p/` — Logic & Pattern Programs
`collatz_sequence` · `devision_by_zero` · `honesty` · `horiz_spike_pattern` · `password_check` · `Pyramid_of_stars`  · `zigzag_pattern_maker` · and more

---

## 🛠 Tech Stack

- **Language:** Python 3.11
- **Testing:** pytest
- **Libraries used:** `requests`, `csv`, `re`, `sys`, `pyfiglet`, `emoji`, `pillow`, `google-genai`, `google-api-core`, `pydantic`, `rich`, `reportlab`
- **Editor:** VS Code + Thonny
- **Course:** [CS50P by Harvard (free on edX)](https://cs50.harvard.edu/python/)

---

## 📈 My Progress

| Week | Topic | Status |
|------|-------|--------|
| 0 | Functions & Variables | ✅ Done |
| 1 | Conditionals | ✅ Done |
| 2 | Loops | ✅ Done |
| 3 | Exceptions | ✅ Done |
| 4 | Libraries | ✅ Done |
| 5 | Unit Tests (pytest) | ✅ Done |
| 6 | File I/O | ✅ Done |
| 7 | Regular Expressions | ✅ Done |
| 8 | Object-Oriented Programming | ✅ Done |
| 9 | Et Cetera | ✅ Done |
| 🏆 | **Final Project — MedSaver** | ✅ **Submitted** |

**CS50P: Complete.** 🎓

---

## 🙋 About Me

I'm a student from India who started learning Python through CS50P before joining college, and finished the full 10-week course by building **MedSaver**, an AI-powered generic medicine finder and price comparison tool. This repository is proof of every hour I put in — from simple print statements to writing tests, reading CSVs, calling live APIs, and shipping a working final project.

I'm serious about building a career in software development, and this is where it begins.

📬 Feel free to connect or give feedback — I'm always looking to improve.

---

*"First, solve the problem. Then, write the code." — John Johnson*
