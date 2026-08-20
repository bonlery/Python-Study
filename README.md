# Python Study

A personal Python learning repository structured as a 10-stage self-study curriculum, covering fundamentals through OOP. Built for active recall with interactive quiz and prediction tools.

## Prerequisites

- Python 3.10+
- No external dependencies required

## Project Structure

```
├── study_guide.md           # 3-week study schedule and learning methodology
├── python_reviewer.md       # Compressed topic reviewer (11 topics)
│
├── # Stage 1: Fundamentals
├── unit1_lesson1-4.py       # Variables, types, basic operations
├── unit1_lesson5-6.py       # Input, walrus operator
├── week3olc.py              # Quick exercises
│
├── # Stage 2: Strings & Slicing
├── strings.py               # Comprehensive string methods and operations
├── slicing.py               # Slicing on lists, strings, tuples
│
├── # Stage 3: Conditionals
├── conditionals.py          # if/elif/else, operators, truthiness
├── ternary_and_range.py     # Ternary expressions, range(), comprehensions intro
│
├── # Stage 4: Loops
├── while_loops.py           # While loops, break, continue, else clause
│
├── # Stage 5: Collections
├── lists_tuples_dicts.py    # Declaration and basics
├── list_crud.py             # List CRUD operations
├── sets.py                  # Sets and set operations
├── iteration_over_dict.py   # Dictionary iteration
├── copying_objects.py       # Shallow vs deep copy
├── list_comprehensions.py   # Comprehensions (list, dict, set)
│
├── # Stage 6: Functions
├── built_in_functions.py    # Built-in function reference
├── function_default_args.py # Default args, parameter ordering
├── args_kwargs.py           # *args and **kwargs
├── lambda_filter_map.py     # Lambda, filter, map
├── variable_scope.py        # Scope and the LEGB rule
│
├── # Stage 7: Operators & Errors
├── operator_precedence.py   # Full precedence table
├── common_errors.py         # Error catalog with explanations
├── exception_handling.py    # try/except/else/finally
│
├── # Stage 8: Files & Modules
├── file_handling.py         # File I/O and context managers
├── modules_and_imports.py   # Import patterns, built-in modules
│
├── # Stage 9: OOP
├── oop_classes.py           # Classes, inheritance, decorators
│
├── # Stage 10: Reference & Tools
├── python_cheatsheet.py     # Quick syntax reference
├── self_quiz.py             # Interactive quiz tool (~45 questions)
└── predict_run.py           # Predict-then-run exercise tool (~45 snippets)
```

## Interactive Study Tools

### Quiz Tool (`self_quiz.py`)

A multiple-choice and free-text quiz covering 12 Python topics. Features randomized question order, topic filtering, and score tracking.

```
python self_quiz.py
```

### Predict-Run Tool (`predict_run.py`)

Shows a code snippet, you predict the output, then it runs the code and compares. Wrong answers are repeated in a second round for reinforcement.

```
python predict_run.py
```

## Study Approach

This repository follows an active-recall methodology outlined in `study_guide.md`:

1. **Predict-then-run** -- guess output before executing
2. **Blank-canvas rewrites** -- rewrite scripts from memory
3. **Spaced repetition** -- revisit earlier topics as you progress
4. **Interleaving** -- mix topics during review sessions

The recommended schedule covers all 10 stages over 3 weeks.
