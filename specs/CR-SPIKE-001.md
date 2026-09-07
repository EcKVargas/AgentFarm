## Problem
AgentFarm has no reusable greeting helper.

## Proposed Change
Add a module `greeting.py` at the repo root with a function `greet(name)` that returns the string `Hello, <name>!` (e.g. `greet("World")` returns `Hello, World!`). Add a pytest test `test_greeting.py` that verifies this.

## Acceptance Criteria
1. `greeting.py` defines `greet(name)` returning `Hello, <name>!`.
2. `test_greeting.py` contains a passing test asserting `greet("World") == "Hello, World!"`.

## Out of Scope
Any other files, CI, packaging, or docs.
