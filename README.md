# Skunkworks

A self-contained, reproducible polyglot development environment for rapid prototyping and experimentation.

## What is this?

Skunkworks is a general-purpose project template that provides:

- **Version-pinned toolchains** - Go, Python, Node.js, Bun, and TypeScript with locked versions
- **Isolated installation** - Everything lives in `~/.skunkworks` by default, no system contamination
- **Cross-platform** - Works on macOS and Linux (both x64 and ARM64)
- **Reproducible builds** - Exact same tool versions across machines and time
- **Fast setup** - Automated installation scripts for all dependencies

Perfect for prototypes, experiments, and projects that need a stable, self-contained development environment.

## Quick Start

```bash
# Clone the repo (or use as template)
git clone <your-repo> skunkworks
cd skunkworks

# Set up the environment
source env.sh
bin/setup

# You're ready to go!
# The environment is now configured with all tools
```

**Important:** Always run `source env.sh` at the start of each session to configure your shell environment.

For convenience, use [direnv](https://direnv.net/) to automatically source the environment when entering the directory:

```bash
# The .envrc file is already configured
direnv allow
```

## What's Included

### Languages & Runtimes

| Tool       | Version | Location                   |
| ---------- | ------- | -------------------------- |
| Go         | 1.25.4  | `~/.skunkworks/opt/goroot` |
| Python     | 3.12.12 | `~/.skunkworks/opt/venv`   |
| Node.js    | 24.11.1 | `~/.skunkworks/opt/node*`  |
| Bun        | 1.3.2   | `~/.skunkworks/opt/bun`    |
| TypeScript | 5.0.0+  | via npm                    |

### Development Tools

- **Formatting + Type Checking**:
  - JavaScript/TypeScript: Prettier + TypeScript compiler
  - Python: Ruff (format + lint) + basedpyright
  - Shell: shfmt
- **Package Managers**: Bun, npm, uv (Python), go modules

**Note:** Formatters automatically run type checking - you don't need separate type check commands in normal workflow.

All versions are defined in `versions.sh` for easy updates.

## Common Commands

### Format & Type Check (Recommended Workflow)

```bash
# Format all code + run all type checkers
bin/format

# Format + type check specific languages
bin/format-js        # Prettier + TypeScript type checker
bin/format-python    # Ruff format + Ruff lint + basedpyright type checker
bin/format-shell     # shfmt (bash scripts)
```

**Important:** The format commands automatically run type checking. This is the standard workflow - you get formatting, linting, and type checking in one step.

### Standalone Type Checking (Optional)

```bash
# TypeScript only (without formatting)
bun run typecheck

# Python only (without formatting)
basedpyright

# Note: There's no standalone command for both - just use bin/format
```

Use these only if you want to check types without formatting. In practice, just use the format commands above.

### Install/Update Dependencies

```bash
bin/setup      # Full setup (all languages)
bin/install-python   # Just Python
bin/install-node     # Just Node.js and Bun
bin/install-go       # Just Go
```

## Directory Structure

```
skunkworks/
├── bin/                    # Utility scripts
│   ├── format*             # Code formatters
│   ├── install-*           # Language installers
│   └── setup               # Full environment setup
├── env.sh                  # Environment configuration (source this!)
├── versions.sh             # Pinned tool versions
├── package.json            # Node.js/Bun dependencies
├── requirements.txt        # Python dependencies
├── tsconfig.json           # TypeScript configuration
└── ~/.skunkworks/          # Installation directory
    ├── opt/                # Language toolchains
    │   ├── goroot/         # Go installation
    │   ├── go/             # GOPATH
    │   ├── venv/           # Python virtual environment
    │   ├── python/         # Python installations
    │   ├── node*/          # Node.js
    │   └── bun/            # Bun runtime
    └── 3rdparty/           # Third-party dependencies
```

## How to Use This

### For a New Project

1. **Clone or fork** this repository as your project base
2. **Run setup**: `source env.sh && bin/setup`
3. **Add your code**: Write Go, Python, TypeScript, or anything else
4. **Format & check**: Run `bin/format` frequently (formats code and runs type checkers)
5. **Add dependencies**:
   - Node: `bun add <package>` or edit `package.json`
   - Python: Add to `requirements.txt` and run `bin/install-python`
   - Go: Use `go get` (GOPATH is configured)

### Day-to-Day Development

The typical development workflow:

```bash
# Start your session (or use direnv)
source env.sh

# Write some code...

# Format and type check everything
bin/format

# Or format specific languages as you work
bin/format-python    # Formats, lints, and type checks Python
bin/format-js        # Formats and type checks TypeScript/JS
```

All format commands automatically run the appropriate type checkers, so you get immediate feedback on type errors without running separate commands.

### Adding Third-Party Git Dependencies

Edit `bin/update-3rdparty-deps` and add:

```bash
github_update <user> <repo> <commit-sha>
```

Dependencies are downloaded to `~/.skunkworks/3rdparty/<repo>` at the exact commit.

### Updating Tool Versions

Edit `versions.sh` to change versions:

```bash
export GO_VERSION=1.25.4
export PYTHON_VERSION=3.12.12
export NODE_VERSION=24.11.1
# ... etc
```

Then re-run the relevant installer:

```bash
source env.sh
bin/install-go       # Updates Go to new version
bin/install-python   # Updates Python
bin/install-node     # Updates Node/Bun
```

### Using a Different Installation Directory

By default, everything installs to `~/.skunkworks`. To change this:

```bash
export DEPLOY_PREFIX=/path/to/custom/location
source env.sh
bin/setup
```

## Configuration

### Python

- Virtual environment: `~/.skunkworks/opt/venv`
- Package manager: [uv](https://github.com/astral-sh/uv) (fast pip replacement)
- Formatter/linter: [Ruff](https://github.com/astral-sh/ruff)
- Type checker: [basedpyright](https://github.com/DetachHead/basedpyright) (community fork of pyright)
- **Integrated workflow**: `bin/format-python` runs formatting, linting, and type checking automatically

### TypeScript/JavaScript

- Runtime: Bun (primary) and Node.js
- Package manager: Bun
- Module system: ESNext with bundler resolution
- Strict mode enabled
- Formatter: Prettier (semicolons, single quotes, trailing commas)
- Type checker: TypeScript compiler (tsc)
- **Integrated workflow**: `bin/format-js` runs Prettier formatting and TypeScript type checking automatically

### Go

- Module mode enabled
- GOPATH: `~/.skunkworks/opt/go`
- Tools installed to `$GOPATH/bin` (automatically in PATH)

### Shell Scripts

- Formatted with `shfmt`
- All scripts in `bin/` are executable and added to PATH

## Environment Variables

When you `source env.sh`, these are configured:

```bash
PROJECT_ROOT          # Repository root directory
HOMEDIR_STORE         # ~/.skunkworks (or $DEPLOY_PREFIX/.skunkworks)
THIRD_PARTY_DIR       # $HOMEDIR_STORE/3rdparty
OPT_DIR               # $HOMEDIR_STORE/opt

GOROOT                # Go installation directory
GOPATH                # Go workspace

VIRTUAL_ENV           # Python venv
PYTHONPATH            # Includes $PROJECT_ROOT and venv site-packages

BUN_INSTALL           # Bun installation directory
PATH                  # Updated to include all tools
```

## Tips

- **Use direnv**: Automatically sources `env.sh` when you `cd` into the directory
- **Secrets management**: Create a `secrets.sh` file for API keys and tokens (gitignored, auto-sourced)
- **IDE integration**: Point your IDE to the virtualenv at `~/.skunkworks/opt/venv`
- **Multiple projects**: Each project can have its own skunkworks setup without conflicts

## Why "Skunkworks"?

The term "skunkworks" refers to a small, loosely structured group working on advanced or secret projects. This repo embodies that spirit - a flexible, self-contained environment for rapid development and experimentation without dependencies on system installations or corporate infrastructure.

## License

This is a template/starter repository. Use it however you want for your projects.
