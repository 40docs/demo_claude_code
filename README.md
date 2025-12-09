# Pet Adoption Center

A demonstration repository for Claude Code onboarding and training. This project showcases all Claude Code features including agents, skills, commands, and settings configuration.

## Purpose

This repository is designed to train new team members on Claude Code by providing:

- Working Python code to modify and test
- Pre-configured Claude Code settings
- Example agents, skills, and commands
- Hands-on demo scenarios

## Quick Start

```bash
# Clone the repository
git clone <repo-url>
cd pet-adoption-demo

# Start Claude Code
claude

# Run the onboarding demo
> Read docs/ONBOARDING.md and walk me through the demos
```

## Project Structure

```
pet-adoption-demo/
├── CLAUDE.md                 # Claude's project memory
├── .claude/
│   ├── settings.json         # Team permissions
│   ├── agents/               # Custom AI agents
│   ├── skills/               # Reusable capabilities
│   └── commands/             # Slash commands
├── src/
│   ├── models/pet.py         # Pet data model
│   ├── api/pets.py           # REST API handlers
│   └── utils/validators.py   # Validation helpers
├── tests/
│   └── test_pet.py           # pytest test suite
└── docs/
    └── ONBOARDING.md         # Interactive guide
```

## Claude Code Features Demonstrated

### Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| `code-reviewer` | sonnet | Code quality review |
| `test-writer` | sonnet | Generate pytest tests |
| `documentation-helper` | haiku | Update documentation |

### Skills

| Skill | Purpose |
|-------|---------|
| `api-patterns` | REST API conventions |
| `database-schema` | Data model reference |

### Commands

| Command | Usage |
|---------|-------|
| `/project:new-feature` | Scaffold new feature |
| `/project:pr-checklist` | Pre-PR validation |

## Running Tests

```bash
pytest tests/ -v
```

## Contributing

1. Create a feature branch
2. Make changes
3. Run `/project:pr-checklist` before submitting
4. Request review from `code-reviewer` agent

## License

MIT - For demonstration purposes only.
