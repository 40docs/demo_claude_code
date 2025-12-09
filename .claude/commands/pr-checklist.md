Run the PR checklist for this branch.

1. Run all tests: `pytest -v`
2. Check code formatting: `black --check src/`
3. Run type checker: `mypy src/`
4. Review changed files for:
   - [ ] Type hints present
   - [ ] Docstrings complete
   - [ ] No debug code
   - [ ] No hardcoded values

Report results as a checklist.
