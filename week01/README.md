# Week 1 Python Practice (Conditions, Lists/Dicts, Text Analyzer, File I/O)

Small Python exercises and mini projects for practicing:

* conditions & loops
* lists & dictionaries
* text processing (word frequency + banned words)
* exception handling + file I/O

## Requirements

* Python 3.x
* No external packages

## How to run

```bash
python <filename>.py
```

Most scripts read from standard input (stdin).

## Files

### `2026-01-13_conditions_loops.py`

Practice problems using conditions/loops (e.g., even/odd counting, gugudan range printing, simple password check).

### `2026-01-14_list_dictionary.py`

* Even/Odd split with count & sum
* Shopping cart total using a price dictionary

  * Prints unknown items and excludes them from the total

### `2026-01-14_mini_project_word_analyzer.py`

Mini project: review text cleaner + word frequency analyzer

* Cleans/normalizes tokens
* Masks banned words as `***`
* Prints cleaned text, top words (count + ratio), and banned word stats

### `2026-01-15_exception_file_IO.py`

Exception handling + file reading

* Tries to open `<name>.txt`
* Sums valid integers and prints invalid lines
* If the file doesn’t exist: prints `File not found` and exits

## Notes

* Each file may have slightly different input/output formats depending on the exercise.
* Refactoring (cleaner I/O, more functions, consistent formatting) is welcome for extra practice.
