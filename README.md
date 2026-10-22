# pylings

Small Python exercises, in order, one concept at a time. Rustlings, for Python.

53 exercises across 8 sections. Each one is a single file with a short
explanation at the top, a small thing to write, and checks at the bottom that
tell you exactly what they expected and what they got. A watcher re-runs the
current exercise every time you save.

No dependencies. Python 3.11 or newer.

## Start

```bash
cd pylings
python3 pylings.py
```

The first run checks every exercise and opens watch mode on your first
pending one. Leave it running in one terminal and edit files in your editor.
Every save re-runs the current exercise.

Watch mode works like rustlings. When the exercise passes, press `n` to move
on. The other keys:

| key | does |
|-----|------|
| `n` | next exercise (once the current one passes) |
| `h` | show the hint |
| `l` | list every exercise: jump to one, reset one, filter done/pending, search |
| `c` | check all exercises |
| `x` | reset the current exercise to its original state |
| `q` | quit |

Other commands:

```bash
python3 pylings.py run             # run the current exercise once
python3 pylings.py run coll7       # run a specific one
python3 pylings.py hint            # hint for the current exercise
python3 pylings.py hint coll7      # hint for a specific one
python3 pylings.py check-all       # check everything, print what is pending
python3 pylings.py reset func2     # undo your changes to one
```

Progress lives in `.pylings-state.txt`. Delete it to start over.

## The sections

| # | Section | What it covers |
|---|---------|----------------|
| 01 | basics | f-strings, truthiness, `is` vs `==`, the `None`-vs-falsy trap, floor division, tuple unpacking |
| 02 | strings | immutability, `split`/`join`, slicing, `removeprefix`, format specs, `str` vs `bytes` |
| 03 | collections | list/dict/set/tuple, unpacking, comprehensions, `sorted(key=...)`, `Counter`, `defaultdict` |
| 04 | functions | defaults, the mutable-default bug, `*args`/`**kwargs`, keyword-only params, closures, decorators, `functools.cache` |
| 05 | classes | `__init__`, `__repr__`, `__eq__`+`__hash__`, `@property`, `classmethod`/`staticmethod`, dataclasses, `super()` |
| 06 | errors | `try`/`except`/`else`/`finally`, custom exceptions, `raise ... from`, context managers, `@contextmanager` |
| 07 | iterators | `enumerate`, `zip(strict=True)`, generators, generator expressions, `itertools`, `__iter__` |
| 08 | typing | annotations, `X \| None`, built-in generics, `TypeVar`, `Protocol`, `TypedDict` |

They build on each other, so work through them in order. Sections 04–08 are
where the real production Python lives; 01–03 are there to get your hands moving.

## How to work through it

Read the comment block at the top of the file first — it explains the idea and
usually names the mistake people make with it. Then read the checks at the
bottom, which are the actual spec. Then write the code.

Do not read `solutions/` until you have solved the exercise. Then do read it —
comparing your version to another one is where half the learning is. If yours
differs and the checks pass, yours is fine.

Some checks are marked as demonstrations and already pass. They are there to be
read, not fixed — they show the behaviour the exercise is warning you about.

## Where this is going

You already have `crawlkit` — the real async service. That is still the
destination; this is the on-ramp. When you finish section 08 you will have met
every language feature crawlkit's Stage 1 exercises assume, and that jump should
feel much smaller.

## Adding your own

`_build/` holds the source of every exercise as plain data. Edit or add a
section, then:

```bash
python3 _build/build.py     # regenerate exercises/, solutions/, info.toml
python3 _build/verify.py    # check every solution passes and every stub fails
```
