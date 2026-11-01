# Discovery Piscine – Core Python Programming

My solutions to the exercises from the **Discovery Piscine for pupils & students**
at [42 Vienna](https://42vienna.com). This is a free, immersive workshop that teaches
Python basics in a short time through peer-to-peer learning.

The repository holds 41 exercises across 9 modules, going from a first `print` to
writing your own functions.

## Repository structure

```
discovery_picine/
├── module0/   Getting started
├── module1/   Variables & input
├── module2/   Conditions
├── module3/   Loops
├── module4/   Strings, f-strings & type conversion
├── module5/   Lists & sets
├── module6/   Command-line parameters
├── module7/   Parameters & iteration
└── module8/   Functions
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
| ex04 | `round_up.py` | Rounds a number up to the next whole number |
| ex05 | `up_low.py` | Swaps uppercase and lowercase letters in a string |

### Module 5: Lists & sets

| Exercise | File | Description |
|---|---|---|
| ex00 | `create_list.py` | Creates a list and prints it |
| ex01 | `play_with_list.py` | Builds a new list by adding 2 to each item |
| ex02 | `play_with_list.py` | Same as ex01, but only keeps items greater than 5 |
| ex03 | `play_with_list.py` | Same as ex02, with duplicates removed using a `set` |
| ex04 | `parameters.py` | Prints the number of parameters passed to the program |

### Module 6: Command-line parameters

| Exercise | File | Description |
|---|---|---|
| ex00 | `aff_first_param.py` | Prints the first parameter |
| ex01 | `upcase_it.py` | Prints the parameter in uppercase |
| ex02 | `downcase_it.py` | Prints the parameter in lowercase |
| ex03 | `aff_rev_params.py` | Prints the parameters in reverse order (needs at least two) |
| ex04 | `scan_it.py` | Counts how often a keyword appears in a string, using `re` |

### Module 7: Parameters & iteration

| Exercise | File | Description |
|---|---|---|
| ex00 | `parameter_matching.py` | Asks the user to retype the parameter and checks the answer |
| ex01 | `count_it.py` | Prints the number of parameters and the length of each one |
| ex02 | `string_are_arrays.py` | Goes through a string character by character and prints every `z` |
| ex03 | `append_it.py` | Adds `ism` to each parameter, skipping those that already end in it |
| ex04 | `free_range.py` | Builds a list of all numbers between two parameters |

### Module 8: Functions

| Exercise | File | Description |
|---|---|---|
| ex00 | `hello_all.py` | Defines and calls a first function |
| ex01 | `upcase_it.py` | A function that returns a string in uppercase |
| ex02 | `downcase_all.py` | Prints every parameter in lowercase using a function |
| ex03 | `greetings_for_all.py` | Default parameter values and a type check with `isinstance` |
| ex04 | `functions_everywhere.py` | `shrink` and `enlarge` functions that make every parameter 8 characters long |
| ex05 | `scope_that.py` | Shows that changing a parameter inside a function doesn't affect the variable outside |

## Running the exercises

You need **Python 3**. Run any exercise from the repository root:

```bash
python3 module2/ex00/iszero.py
```

Many exercises from module 6 onwards take parameters on the command line, and print
`none` if they don't get the ones they expect:

```bash
python3 module6/ex01/upcase_it.py hello
```

Most files start with a `#!/usr/bin/env python3` shebang, so you can also make them executable:

```bash
chmod +x module3/ex01/multiplication_table.py
./module3/ex01/multiplication_table.py
```

## Author

- **GitHub:** [cuteKittenArri](https://github.com/cuteKittenArri)
<img src="https://arri-eta.vercel.app/mage.gif" alt="arri" style="max-width: 205px;">
