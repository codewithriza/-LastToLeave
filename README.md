# LastToLeaveBot

LastToLeaveBot is a Discord bot built with discord.py that allows users to start a "last to leave" event in a voice channel. The bot joins the voice channel with the user who initiated the event and pings the last person to leave the voice channel as the winner.

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create a new Discord application and bot on the [Discord Developer Portal](https://discord.com/developers/applications).
4. Copy your bot token from the "Bot" section of your application and replace `'YOUR_TOKEN'` in `main.py` with your actual bot token.
5. Run the bot using `python main.py`.

## Commands

- `!lasttoleave`: Starts a "last to leave" event in the voice channel the user is currently in. The bot joins the voice channel and pings the last person to leave as the winner.

## Requirements

- Python 3.6+
- discord.py
- PyNaCl (for voice support)

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

---
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/887532157747212370)
[![X](https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://twitter.com/codewithriza)
