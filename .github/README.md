# Disbooru - simple python discord bot for image requests from *booru

<p align="center">
  <img src="./readme.png" alt="I do not own the rights to this ico. If you are the owner and want it removed, please contact me." />
</p>

## Description
Disbooru is discord bot writen on python "bc I'm too ls in any other languages" that requests random image from Danbooru and Gelbooru(WIP) archives.

## Features
-   [x] Request for random image with tags from Danbooru (only 1 extra tag support)
-   [x] Censored requests for NSFW arts (rating explicit and questionable), also uncensored requests.
-   [ ] Request for random image with tags from Danbooru (several number tags support).
-   [ ] Docker compose version with VPN setup
-   [ ] other features...

## Requirements
Disbooru relies on pip libs like discord.py and pybooru
[Discord.py](https://pypi.org/project/discord.py/)
[Pybooru](https://pypi.org/project/Pybooru/)

## Installation

### Manual
1. Clone the repository
2. Install the requirement libs with `pip install discord.py` and `pip install pybooru`
3. Rename `Requirements.py.example` to `Requirements.py`
4. Fill the `Requirements.py` file with the required data
5. Optional: Configure VPN if needed 
6. Run bot with this command:
```bash
python3 Main.py
```
7. Discord bot will be online

### Docker compose
Work In Progress

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for more details.