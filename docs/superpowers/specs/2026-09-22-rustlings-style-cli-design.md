# pylings CLI: match rustlings 6.5

## Problem

`pylings.py` is a thin watcher. It cannot move to the next exercise from the
keyboard, hints are a separate command, and there is no list view. The goal
is a CLI that behaves and looks like rustlings 6.5's, ported to Python with
no third-party dependencies (stdlib only, Python 3.11+).

## Decisions

- **Done state lives in `.pylings-state.txt`**, same format as rustlings'
  `.rustlings-state.txt`, not in an `I AM NOT DONE` marker. Pressing `n` on a
  passing exercise marks it done and moves on. The marker line and the
  "delete the I AM NOT DONE line" sentence are stripped from every exercise,
  from `.pylings/pristine/`, and from `_build/build.py`. `_build/verify.py`
  stops checking for the marker.
- **First run seeds state by checking every exercise**, so work already done
  under the old marker system is recognised.
- **Stdlib only.** Key input via `termios`/`tty` + `select`, file changes via
  mtime polling of the current exercise, resize via `SIGWINCH` on a wake-up
  fd, terminal size via `shutil.get_terminal_size`.
- **Entry point stays `python3 pylings.py`.** Logic moves to a `_pylings/`
  package so each mode is one small module.

## Commands

| command | behaviour (mirrors rustlings) |
|---|---|
| `pylings.py` | watch mode on the current exercise |
| `pylings.py run [NAME]` | run one exercise; on success mark done and print the next |
| `pylings.py check-all` | check every exercise, print the pending count |
| `pylings.py hint [NAME]` | print the hint |
| `pylings.py reset NAME` | restore the file from `.pylings/pristine/` |

`list` and `verify` subcommands go away: `l` in watch mode is the list,
`check-all` is verify.

## Watch mode

Screen, top to bottom: the exercise output (underlined `Output` header,
program stdout, cleaned stderr, and on failure a bold red
`The exercise didn't run successfully (nonzero exit code)`), then the hint
if `h` was pressed (bold underlined cyan `Hint`), then on success
`Exercise done ✓`, `Solution for comparison: <link>` and
``When done experimenting, enter `n` to move on to the next exercise 🐍``,
then the progress bar `Progress: [####>----] 12/53`, then
`Current exercise: <link>`, then the prompt
`n:next / h:hint / l:list / c:check all / x:reset / q:quit ? `
with `n:next` only shown when the exercise passes and `h:hint` hidden once
the hint is showing.

Keys: `n` next, `h` hint, `l` list, `c` check all, `x` reset (asks `y/n`),
`q` quit. Input is ignored while an exercise runs. Saving the current file
re-runs it. Next goes to the first pending exercise after the current one,
wrapping around; if none, check all runs and the final message shows.

## List mode

Alternate screen. Header `  Current  State    Name  Path`; one row per
exercise: `🐍` plus reverse-bold for the selected row, red `>>>>>>>` for the
current exercise, green `DONE` or yellow `PENDING`, name, path link. Footer:
progress bar, then
`↓/j ↑/k home/g end/G | <c>ontinue at | <r>eset exercise` and
`<s>earch | filter <d>one/<p>ending | <q>uit list`, or a one-line magenta
message. Keys as in rustlings: j/k/arrows, g/G/home/end, d, p, r, c, s or /,
Esc, q. Scrolling keeps a padding of up to 5 rows.

## Check all

Clears the screen, prints `Checking all exercises…` and the colour legend,
then a grid of exercise numbers coloured blue (checking), green (done), red
(pending), updated as parallel runs finish. Updates the state file. If every
exercise passes the final message shows.

## Files

- `pylings.py` argparse and dispatch only
- `_pylings/term.py` ANSI, progress bar, file links, raw input, resize
- `_pylings/exercise.py` `Exercise`, running one, output formatting
- `_pylings/app_state.py` info.toml, state file, done/current, check all, final message
- `_pylings/watch.py` watch mode
- `_pylings/listmode.py` scroll state and list TUI
- `tests/` unittest for the pure parts: state file, next pending, scroll
  state, progress bar, traceback cleaning

## Out of scope

`--manual-run`, `init`, `dev` subcommands, mouse support.
