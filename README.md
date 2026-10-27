# Discovery Piscine – Core Python Programming

My solutions to the exercises from the **Discovery Piscine for pupils & students**
at [42 Vienna](https://42vienna.com). This is a free, immersive workshop that teaches
Python basics in a short time through peer-to-peer learning.

## About the event

| | |
|---|---|
| **Organizer** | 42 Vienna – Digital Excellence Campus |
| **Location** | Muthgasse 26, 1st floor, 1190 Wien, Austria |
| **Dates** | 27–30 October 2026 |
| **Format** | On-site, in English |
| **Audience** | Pupils & students aged 16–25 |
| **Prerequisites** | None, just curiosity and a willingness to learn |
| **Cost** | Free |

[Event page on Eventbrite](https://www.eventbrite.at/e/discovery-piscine-for-pupils-students-core-python-programming-tickets-1999494594156)

There are no lectures and no teachers. You get a set of exercises for each module,
work through them yourself, and learn by asking and helping your peers. That is
the 42 way of learning.

## Repository structure

```
discovery_picine/
├── module0/   Getting started
├── module1/   Variables & input
├── module2/   Conditions
├── module3/   Loops
└── module4/   Strings, f-strings & type conversion
```

Each module contains one folder per exercise (`ex00`, `ex01`, …) with the solution file inside.

## Modules & exercises

### Module 0: Getting started

| Exercise | File | Description |
|---|---|---|
| ex01 | `42.py` | Prints `42` |
| ex02 | `hello_world.py` | Prints `Bye Bye World` |

### Module 1: Variables & input

| Exercise | File | Description |
|---|---|---|
| ex00 | `name.py` | Stores a first and last name in variables and prints them |
| ex01 | `name.py` | Joins first and last name into one string |
| ex02 | `age.py` | Basic arithmetic with variables |
| ex03 | `whatsyourname.py` | Reads first and last name from user input |

### Module 2: Conditions

| Exercise | File | Description |
|---|---|---|
| ex00 | `iszero.py` | Checks whether the entered number is zero |
| ex01 | `isneg.py` | Tells whether a number is positive, negative or zero |
| ex02 | `password.py` | Asks for a secret code and grants or denies access |
| ex03 | `mult.py` | Multiplies two numbers and checks the sign of the result |

### Module 3: Loops

| Exercise | File | Description |
|---|---|---|
| ex00 | `to25.py` | Counts from the entered number up to 25 |
| ex01 | `multiplication_table.py` | Prints the multiplication table of a number |
| ex02 | `i_got_that.py` | Keeps asking for input until the user types `STOP` |
| ex03 | `advanced_mult.py` | Nested loops: multiplication tables from 0 to 10 |

### Module 4: Strings, f-strings & type conversion

| Exercise | File | Description |
|---|---|---|
| ex00 | `upcase_it.py` | Converts a word to uppercase |
| ex01 | `age.py` | Calculates your age in 10, 20 and 30 years |
| ex02 | `calculator.py` | Adds, subtracts, divides and multiplies two numbers |
| ex03 | `float.py` | Checks whether a number is a decimal or an integer |

## Running the exercises

You need **Python 3**. Run any exercise from the repository root:

```bash
python3 module2/ex00/iszero.py
```

Most files start with a `#!/usr/bin/env python3` shebang, so you can also make them executable:

```bash
chmod +x module3/ex01/multiplication_table.py
./module3/ex01/multiplication_table.py
```

## Author

**Steffi Muller** (`stmuller`), Discovery Piscine participant at 42 Vienna, October 2026
