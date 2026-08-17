# PYTHON STUDY GUIDE

How to actually learn the material in this folder - not just read it.

---

## 1. What is in this folder

| Stage | Files | Core concept |
|---|---|---|
| 1 | `week3olc.py`, `unit1_lesson1-4.py`, `unit1_lesson5-6.py` | Variables, types, `print`/`input`, f-strings, walrus |
| 2 | `strings.py`, `slicing.py` | Strings, indexing, `[start:stop:step]` |
| 3 | `conditionals.py`, `ternary_and_range.py` | `if/elif/else`, truthiness, ternary, `range()` |
| 4 | `while_loops.py` | Loops, `break/continue/pass/else` |
| 5 | `lists_tuples_dicts.py`, `list_crud.py`, `sets.py`, `iteration_over_dict.py`, `copying_objects.py`, `list_comprehensions.py` | Collections - the biggest section |
| 6 | `built_in_functions.py`, `function_default_args.py`, `args_kwargs.py`, `lambda_filter_map.py`, `variable_scope.py` | Functions, `*args/**kwargs`, lambda, scope (LEGB) |
| 7 | `operator_precedence.py`, `common_errors.py`, `exception_handling.py` | Evaluation order, errors, try/except |
| 8 | `file_handling.py`, `modules_and_imports.py` | Files, imports |
| 9 | `oop_classes.py` | Classes, `self`, methods |
| 10 | `python_cheatsheet.py` + `python_reviewer.md` | Consolidation - the compressed summary |

**The two key reference files:**
- `python_reviewer.md` - your index: every topic compressed into one document.
- `python_cheatsheet.py` - a quick syntax reference.

> WARNING: `python_reviewer.md` has a few errors. Do NOT memorize it blindly.
> The corrected facts live in the `.py` files (e.g. `operator_precedence.py` fixed the
> precedence example - `7 + 3 * 2 ** 2 // 3 % 5` is `11`, not `8`, and shifts `<< >>`
> are left-to-right, NOT right-to-left).

---

## 2. The three study tools in this folder

All run with the folder's Python:
`.venv\Scripts\python.exe`

### `self_quiz.py` - test your knowledge
- ~45 questions covering every topic: multiple choice + output prediction.
- Random order every run, so you cannot memorize a sequence.
- Pick a topic (e.g. `precedence`) or quiz ALL topics.
- Answer in your head first, type your answer, read the `Why:` explanation.
- Goal: score 100% on EVERY topic individually. Retry topics until you do.

### `predict_run.py` - train your intuition
- Shows you a snippet of code and makes you predict the output BEFORE running it.
- This is the single most effective exercise in this folder.
- After you type your prediction it runs the real code and shows the actual output.
- Wrong answers get repeated in a second round automatically.

### `study_guide.md` (this file) - the method and schedule

---

## 3. The method that actually works (not reading)

### 3a. Predict-then-run (non-negotiable)
Every `.py` file in this folder prints its own output. That is your advantage.
1. Cover the expected result.
2. Say or write what you think each `print(...)` outputs.
3. Run the file. Re-read ONLY what you got wrong.

### 3b. Break it
After you understand a file, change ONE thing at a time and predict again:
- swap `pop()` for `del`, `append` for `extend`
- reverse a slice step (`[::-1]` vs `[::-2]`)
- swap `is` for `==`, `remove` for `discard`
- move `break` vs `continue` in a loop
If it errors, you learned something new.

### 3c. Blank-canvas rewrite (highest ROI)
Close the file. Rewrite it from scratch without looking. Whatever you cannot
reproduce is what you have NOT actually learned. Do this once per stage.

### 3d. Interleave - do not block
Never study one topic for hours. Mix topics in one session:
- 1 file from stage 5 (collections) + 1 file from stage 6 (functions)
  + 1 file from stage 7 (precedence).
Interleaving is what builds deep, exam-ready understanding.

### 3e. Spaced repetition
Revisit each stage at: **1 day, 3 days, 1 week, 1 month**.
Use `python_reviewer.md` as your quiz sheet: read a section, close the file,
and explain it out loud from memory (Feynman technique).

### 3f. Use the REPL for experiments
`.venv\Scripts\python.exe` opens an interactive shell. Test tiny ideas there
instead of writing whole files.

---

## 4. One study session (about 1 hour)

1. **5 min** - Quick quiz: `self_quiz.py` on a TOPIC FROM AN OLDER STAGE.
2. **25 min** - Predict-then-run + break-it on 1-2 NEW files.
3. **15 min** - `predict_run.py` (random snippets). Aim for 100%.
4. **10 min** - Blank-canvas rewrite of yesterday's file (or explain the
   reviewer section out loud).
5. **5 min** - Note the topics you got wrong. Those go on tomorrow's list.

---

## 5. Recommended 3-week schedule

Mark each session as done with `[x]`.

| Week | Session | New material | Review |
|---|---|---|---|
| W1 | 1 | Stage 1 + Stage 2 | - |
| W1 | 2 | Stage 3 + Stage 4 | quiz: stage 1-2 |
| W1 | 3 | Stage 5 (lists, tuples, dicts) | predict-run: slicing |
| W1 | 4 | Stage 5 (sets, copying, comprehensions) | quiz: stage 3-4 |
| W1 | 5 | Stage 6 (functions, *args/**kwargs) | predict-run: collections |
| W2 | 1 | Stage 6 (lambda, filter/map, scope) | quiz: stage 5 |
| W2 | 2 | Stage 7 (operator_precedence, common_errors) | predict-run: functions |
| W2 | 3 | Stage 7 (exception_handling) | quiz: stage 6 |
| W2 | 4 | Stage 8 (file_handling, modules) | predict-run: precedence |
| W2 | 5 | Stage 9 (oop_classes) | quiz: stage 7 |
| W3 | 1 | Stage 10 (cheatsheet + reviewer) | predict-run: all |
| W3 | 2 | Blank-canvas rewrite: Stage 5 + Stage 6 | quiz: all topics |
| W3 | 3 | Blank-canvas rewrite: Stage 7 + Stage 9 | predict-run: all |
| W3 | 4 | Full-topic quiz marathon: score 100% on each | - |
| W3 | 5 | Explain the whole reviewer out loud to someone | - |

---

## 6. Rules of thumb to memorize

- **Arithmetic binds before comparison binds before `not`/`and`/`or`.**
- **`**` is right-to-left; everything else in the same group is left-to-right.**
- **`==` compares VALUES, `is` compares IDENTITY (same object).**
- **`b = a` does NOT copy a list; `a.copy()`, `a[:]`, and `list(a)` do (shallow).**
- **`append` adds 1 item, `extend` adds each element, `pop` removes AND returns.**
- **`else` on a loop runs only if there was NO `break`.**
- **`else` on try/except runs only if there was NO exception; `finally` always runs.**
- **Falsy:** `0`, `0.0`, `''`, `[]`, `()`, `{}`, `set()`, `None`, `False`.
- **`{}` is a dict; use `set()` for an empty set; single-element tuple needs `5,`.**
- **Methods need `self`; functions do not.**
- **Common errors:** ValueError (bad value), TypeError (wrong types), NameError (undefined name).

---

## 7. Self-test: am I done?

You have truly learned the material when you can, with the folder CLOSED:
- [ ] Write a program that reads a student name and score and prints a letter grade.
- [ ] Write a function with `*args` and `**kwargs` and explain both.
- [ ] Explain `LEGB` with an example in 30 seconds.
- [ ] Predict the output of any expression with mixed arithmetic and logical operators.
- [ ] Fix a `KeyError`, `IndexError`, `ValueError`, and `TypeError` without looking.
- [ ] Reverse a list, dedupe a list, and flatten a nested list (3 different tools).
- [ ] Explain the difference between a shallow and a deep copy, with a nested list.
- [ ] Write a class with `__init__` and a method, and explain `self`.
- [ ] Score 100% on `self_quiz.py` for every topic.

Tick them all and you are exam-ready.
