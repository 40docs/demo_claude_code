# Pet Adoption Center

A demo repository for Claude Code onboarding and training.

## Quick Commands

```bash
# Run tests
pytest tests/ -v

# Run specific test file
pytest tests/test_pet.py -v

# Check Python syntax
python -m py_compile src/**/*.py
```

## Architecture

- `src/models/` - Data models (Pet, etc.)
- `src/api/` - API endpoint handlers
- `src/utils/` - Shared utilities and validators
- `tests/` - pytest test suite

## Code Patterns

- **Models**: Use dataclasses with validation in `__post_init__`
- **API responses**: Always use `_success_response()` or `_error_response()`
- **Validation**: Use helpers from `src/utils/validators.py`
- **Status workflow**: AVAILABLE -> PENDING -> ADOPTED

## Workflow Rules

- Run tests before committing: `pytest tests/ -v`
- Use the `code-reviewer` agent after making changes
- Follow Google-style docstrings for all functions
- Keep functions under 30 lines when possible

## Things to Avoid

- NEVER hardcode secrets or API keys
- NEVER commit .env files
- NEVER use `print()` for debugging in production code
- NEVER skip input validation on user data
- AVOID raw SQL queries - use parameterized queries

## Claude Code Features Demo

This repo demonstrates:
- Skills: `api-patterns`, `database-schema`
- Agents: `code-reviewer`, `test-writer`, `documentation-helper`
- Commands: `/project:new-feature`, `/project:pr-checklist`
