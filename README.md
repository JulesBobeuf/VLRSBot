# VLRSBot

![VLRSBot Screenshot](https://github.com/JulesBobeuf/VLRSBot/raw/main/valorous_coin.png)

**VLRSBot** is a Discord bot developed using Python 3.9. It was created to manage community events and reward participants with virtual coins, which could be exchanged for special roles within the server.

## About The Project

This project was developed as a personal tool to facilitate community engagement on Discord. After each event, winners were manually awarded coins. These coins could then be used to purchase Discord roles that granted various perks within the server.

The bot was initially hosted on Google Cloud and later migrated to a personal Raspberry Pi for self-hosting.

## Built With

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)  
[![Discord.py](https://img.shields.io/badge/discord.py-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discordpy.readthedocs.io/)  
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)  

## Getting Started

### Folder Structure

```markdown
VLRSBot/
├── 📄 VLRSBot.py            # Main bot script
├── 📄 requirements.txt      # Python dependencies
└── 📄 README.md             # Project documentation
```

### Prerequisites

Ensure you have the following installed:

```sh
Python 3.9+
pip
```

### Installation & Setup

1. Clone the repository:

```sh
git clone https://github.com/JulesBobeuf/VLRSBot.git
cd VLRSBot
```

2. Install dependencies:

```sh
pip install -r requirements.txt
```

3 Configure your bot token and database credentials `VLRSBot.py`

4. Run the bot:

```sh
python VLRSBot.py
```

### Running the Application

After setting up, the bot will connect to Discord and begin operating within your server.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Jules Bobeuf  
[LinkedIn](https://www.linkedin.com/in/bobeuf-jules/)  
bobeuf.jules@gmail.com
