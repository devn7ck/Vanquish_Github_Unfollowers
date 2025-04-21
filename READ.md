# GitHub Unfollowers Checker

This project helps you track and manage your GitHub followers. It identifies users who have unfollowed you by comparing your current followers list with a previously saved list.

## Features

- Fetches your current GitHub followers using the GitHub API.
- Compares the current followers list with a saved list to identify unfollowers.
- Saves the updated followers list for future comparisons.

## Requirements

- Python 3.7 or higher is required.
- `requests`: For making HTTP requests to the GitHub API.
- `python-dotenv`: For loading environment variables from a `.env` file.
- `argparse`: For parsing command-line arguments.
- `json`: For handling JSON data (built-in module).
- `os`: For interacting with the operating system (built-in module).
- Install dependencies using:
    ```bash
    pip install -r requirements.txt
    ```

## Installation

1. Clone this repository:
    ```
    git clone https://github.com/devn7ck/github-unfollowers-py.git
    ```
2. Navigate to the project directory:
    ```
    cd github-unfollowers-py
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Create a personal access token on GitHub with the `read:user` scope.
2. Run the script:
    ```
    python github_follow_check.py
    ```
3. Enter your GitHub username and personal access token when prompted.

## Issues

For issues, please visit the [Issues Page](https://github.com/devn7ck/github-unfollowers-py/issues).


###### [![alt text](image.png)](https://www.buymeacoffee.com/devn7ck)

If you find this project helpful, consider supporting me on [BuyMeACofee](https://www.buymeacoffee.com/devn7ck). Your support is greatly appreciated!