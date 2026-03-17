# CLAUDE.md — Ale Codebase Guide

## Project Overview

**Ale** is a smart interactive command-line launcher for macOS. It provides a REPL prompt (`ale>`) from which users can search the web, open macOS applications, and run system commands.

- **Language:** Python 2.7
- **Platform:** macOS only (uses `open -a`, AppleScript via `osascript`, `/Applications`)
- **Entry point:** `./ale` (run from repo root)
- **Version:** 0.1.1

---

## Repository Structure

```
ale/
├── ale                        # Executable entry point; calls main.start() + main.main()
├── setup.py                   # setuptools package config
├── requirements.txt           # pip dependencies
├── .travis.yml                # CI: Python 2.7 + nosetests
└── core/
    ├── main.py                # REPL loop; command dispatch; tab completion
    ├── parser.py              # String/path utilities; /Applications discovery
    ├── formulas.py            # Discovers available formula names from Formula/
    ├── invalid_command.py     # Fallback handler; suggests web searches
    ├── wcolors.py             # ANSI color constants
    ├── aliase.py              # Loads alias files and dispatches to formulas
    ├── aleinst.py             # Package manager (install optional packages)
    ├── Formula/               # 35+ formula plugins (one .py file per command)
    ├── Package/               # Package installer plugins (brew, slap, spacemacs)
    └── Aliases/               # Alias text files (maps alias name → formula name)
```

---

## Architecture

### Command Routing (priority order in `core/main.py`)

1. **Formulas** — check `core/Formula/<name>.py`; load with `imp.load_source()`, instantiate `Formula(request=args)`, call `.main()`
2. **Aliases** — check `core/Aliases/<name>`; read the file to get target formula name, load that formula
3. **Applications** — check `/Applications` via `parser.applications_list()`; run `open -a <App>.app`
4. **Shell fallback** — try `subprocess.call(com)`; if `OSError`, call `invalid_command.main(com)` which prompts web searches

### Dynamic Loading

Formulas are loaded at runtime, not imported at startup:
```python
module = imp.load_source(com[0], CURRENT_DIR + "/Formula/" + com[0] + ".py")
formula = module.Formula(request=com[1:])
formula.main()
```

---

## Adding a Formula

1. Create `core/Formula/<name>.py` (lowercase filename = command name)
2. Implement the `Formula` class:

```python
import webbrowser
from core import wcolors
from core import parser

class Formula():
    def __init__(self, request):
        self.request = request  # list of args after the command

    def main(self):
        query = parser.parse_request(self.request[0:])
        print(wcolors.color.GREEN + "Searching => " + wcolors.color.RED + query + wcolors.color.ENDC)
        webbrowser.open('https://example.com/search?q=' + query)
```

No registration needed — `formulas.formulas_list()` auto-discovers all `.py` files in `core/Formula/`.

---

## Adding an Alias

Create a plain text file at `core/Aliases/<alias-name>` containing only the target formula name:

```
# core/Aliases/wiki  →  contains: wikipedia
wikipedia
```

---

## Adding a Package

Create `core/Package/<name>.py` with a `Package` class and `install()` method:

```python
class Package():
    def install(self):
        # installation logic here
        pass
```

---

## Code Conventions

### Python 2.7 Syntax
- Use `raw_input()` for user input (not `input()`)
- `print` can be used as a function: `print(...)` — both work in Python 2.7
- Use `imp.load_source()` for dynamic module loading
- String formatting via concatenation (not f-strings)

### Terminal Output Colors
Always use `wcolors.color.*` — never hardcode ANSI codes:

| Color | Use case |
|-------|----------|
| `GREEN` | Success messages, informational output |
| `RED` | Highlighted data (search query, result) |
| `YELLOW` | Prompts, interactive questions |
| `DARKCYAN` | Request parameters |
| `ENDC` | Reset — always terminate colored strings with this |

Example: `wcolors.color.GREEN + "Message" + wcolors.color.ENDC`

### Imports
```python
from core import wcolors
from core import parser
```

### Naming
- Formula/Package class name: always `Formula` or `Package` (exact case)
- File names: lowercase (`google.py`, `emptytrash.py`)
- Functions: `snake_case`
- Classes: `CamelCase` (only `Formula` and `Package` in plugins)

---

## Utility Functions to Reuse

All in `core/parser.py`:

| Function | Purpose |
|----------|---------|
| `parser.parse_request(arr)` | Joins a list into a space-separated string (`['a','b']` → `'a b '`) |
| `parser.word_space(path)` | Escapes spaces in paths for shell use (`My App` → `My\ App`) |
| `parser.clear_list(lst)` | Filters out dot files, `__`-suffixed items, and `.pyc` files |
| `parser.applications_list()` | Returns list of installed macOS app names from `/Applications` |

And `core/formulas.py`:

| Function | Purpose |
|----------|---------|
| `formulas.formulas_list()` | Returns list of available formula names (filenames without `.py`) |

---

## Dependencies

```
pygoogle==0.6          # Google search API
readline==6.2.4.1      # Enhanced REPL editing
requests==2.6.0        # HTTP
trash-cli==0.12.9.14   # Trash operations
```

Install: `pip install -r requirements.txt`

---

## Running the Project

```bash
python ale
```

Must be run from the repo root. macOS only — relies on `/Applications`, `open -a`, and `osascript`.

---

## Testing

```bash
pip install -r requirements.txt
nosetests
```

CI is configured in `.travis.yml` (Travis CI, Python 2.7). No test files currently exist in the repo — the test infrastructure is set up but tests need to be written.

---

## Git Workflow

- Main branch: `master`
- Feature branches: descriptive names, merged via pull request
- Contributions: open a GitHub issue before implementing significant changes
- See [Formula Cookbook](https://github.com/darker0n/ale/wiki/Formula-Cookbook) for adding new formulas
