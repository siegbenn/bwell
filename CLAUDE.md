# bwell

A Python project using UV for package management and pytest for testing.

## Project Structure

```
bwell/
├── main.py           # Main application code
├── test_sample.py    # Test files
├── pyproject.toml    # Project configuration and dependencies
├── Makefile          # Build automation
├── uv.lock           # Dependency lock file
└── README.md         # Project documentation
```

## Setup

### Prerequisites
- Python 3.13+
- UV package manager

### Installation
```bash
# Install dependencies
uv sync
```

## Development

### Running Tests
```bash
# Run all tests
make test

# Or directly with uv
uv run pytest
```

### Dependencies
The project uses:
- `pytest>=8.4.1` for testing

## Commands

### Make Targets
- `make test` - Run the test suite using pytest

### Package Management
- `uv sync` - Install/update dependencies
- `uv add <package>` - Add new dependency
- `uv remove <package>` - Remove dependency
- `uv run <command>` - Run command in project environment

## Testing
Tests are located in `test_sample.py` and can be run using pytest through the Makefile or directly with `uv run pytest`.