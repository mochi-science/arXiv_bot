# arXiv Paper Notification Bot

This project is a bot designed to automatically retrieve papers from arXiv and send notifications to platforms like Discord.

## Features
- Fetches latest papers from arXiv based on custom criteria (e.g., keywords, categories).
- Sends notifications to Discord channels with paper details (title, authors, abstract, link, etc.).
- Fully customizable notification settings.

## Requirements

This project uses Python 3.11.9. To ensure compatibility, we recommend using `pyenv` to manage Python versions and `poetry` for dependency management.

### Required tools:
- `pyenv` for managing Python version (3.11.9).
- `poetry` for managing dependencies and virtual environments.

## Setup

1. **Install `pyenv`**  
   Follow the instructions to install `pyenv` [here](https://github.com/pyenv/pyenv#installation). After installation, install Python 3.11.9 and set it as the local version for this project:
   ```bash
   pyenv install 3.11.9
   pyenv local 3.11.9
