# Claude Code Onboarding Guide

Welcome to the Pet Adoption Center project! This guide will help you understand how we use Claude Code.

## Quick Start

1. Clone the repo
2. Copy `.claude/settings.local.json.example` to `.claude/settings.local.json`
3. Run `claude` to start

## Key Concepts

### CLAUDE.md (Project Memory)
Located at the repo root. Claude reads this automatically and follows its instructions. Contains our coding standards, common commands, and things to avoid.

### Settings Hierarchy
- `.claude/settings.json` - Team settings (committed to git)
- `.claude/settings.local.json` - Your personal overrides (git-ignored)

### Agents (Auto-Delegated Specialists)
Located in `.claude/agents/`. Claude automatically delegates to these when appropriate:
- `code-reviewer` - Reviews your code changes
- `test-writer` - Helps write tests
- `documentation-helper` - Helps with docs

Try it: Make a code change and ask "review my changes"

### Skills (On-Demand Expertise)
Located in `.claude/skills/`. Claude loads these when relevant:
- `api-patterns` - Our REST API conventions
- `database-schema` - Database structure and patterns

Try it: Ask "create a new API endpoint for shelters"

### Slash Commands (Shortcuts)
Located in `.claude/commands/`. Type `/project:` to see available commands:
- `/project:new-feature` - Start a new feature
- `/project:pr-checklist` - Run PR checklist

## Demo Scenarios to Try

### Scenario 1: See Skills in Action
Ask: "Create an API endpoint to list all shelters"
Watch: Claude loads the api-patterns skill automatically

### Scenario 2: See Agents in Action
Ask: "Review the code in src/api/pets.py"
Watch: Claude delegates to code-reviewer agent

### Scenario 3: See Permissions in Action
Ask: "Delete the .env file"
Watch: Claude refuses (denied in settings.json)

### Scenario 4: Use a Slash Command
Type: /project:pr-checklist
Watch: Claude runs the full checklist

### Scenario 5: Resume a Session
Exit Claude, then run: `claude --continue`
Watch: Your conversation context is restored

## Session Management

- `claude` - New session
- `claude --continue` - Resume last session
- `claude --resume` - Pick from recent sessions
- `/clear` - Clear context (keeps session)
- `/compact` - Summarize to save tokens

## Configuration Files Reference

| File | Purpose | Shared? |
|------|---------|---------|
| `CLAUDE.md` | Project memory and conventions | Yes |
| `.claude/settings.json` | Team permissions and config | Yes |
| `.claude/settings.local.json` | Personal settings | No |
| `.claude/agents/*.md` | Custom AI agents | Yes |
| `.claude/skills/*/SKILL.md` | Reusable AI capabilities | Yes |
| `.claude/commands/*.md` | Custom slash commands | Yes |

## Troubleshooting

### Agent Not Found
```
> /agents
```
Lists all available agents.

### Skill Not Triggering
Check the skill description matches your query. Skills are triggered by keyword matching.

### Permission Denied
Check `.claude/settings.json` for deny rules. Use `/settings` to view current permissions.

## Next Steps

1. Modify the Pet model and use `code-reviewer`
2. Add a new species and use `test-writer`
3. Create your own slash command in `.claude/commands/`
4. Add a new skill for your workflow

Happy coding with Claude!
