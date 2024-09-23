
# GitHub Actions : Rövarspråket Encoder

This project demonstrates the use of **GitHub Actions** for continuous integration (CI) with a simple Python script that encodes text using the **Rövarspråket** (The Robber Language) rules.

## Project Overview

- **Rövarspråket** is a playful encoding game where every consonant is doubled, with an "o" inserted in between, while vowels and non-alphabetic characters remain unchanged.
   For example:

   Input: stubborn
   Rövarspråket: sostotubobboborornon
- This project uses GitHub Actions to automatically run tests on each commit or pull request, ensuring that the code works as expected.

## Key Components

- `Rover.py`: The main Python script that implements the Rövarspråket encoding.
- `test_rover.py`: Unit tests for validating the encoding logic using `pytest`.
- `.github/workflows/python-app.yml`: GitHub Actions workflow for setting up CI.

## Getting Started

### Running Locally

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. Run the Rövarspråket encoder:
   ```bash
   python Rover.py
   ```

3. Run tests with `pytest`:
   ```bash
   pytest test_rover.py
   ```

### GitHub Actions

- **Automated Testing**: GitHub Actions will automatically run tests on each push or pull request.
- The CI workflow is defined in `.github/workflows/python-app.yml`.

## GitHub Actions Workflow

The workflow includes:
1. Setting up Python.
2. Installing dependencies (`pytest`).
3. Running tests using `pytest`.

No further setup is required; the workflow triggers automatically on each push or pull request.

## License

This project is licensed under the MIT License.
