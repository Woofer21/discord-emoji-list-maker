# Emoji List Maker

Grabs emotes from all servers its in and sends a webhook to the URL specified

## Requirements
- Discord Bot
    - Send Messages Permission
- Webhook
- Python (https://www.python.org/downloads/)
    - Discord Module (https://pypi.org/project/discord.py/)
    - Dotenv Module (https://pypi.org/project/dotenv/)
    - Requests Module (https://pypi.org/project/requests/)


## How to Use
- Create a webhook in the channel you would like the messages sent to
- In the folder you will be running the bot from, create a file named .env
    - Format it the folowing way, replacing the things in <> with what it should be
    ```
    TOKEN=<BOT TOKEN>
    WEBHOOK_URL=<WEBHOOK URL>
    ```

-  In the file called main.py you can edit the **optional** variables
    ```
    WEBHOOK_NAME = "The name you want the webhook to hav"
    WEBHOOK_AVATAR = "A link to the file which should be the bots avatar"
    ```

- Once you have done all of that, run the main.py file
- Run the command `$grab-emotes` in any channel the bot can see
    - Do note that the bot will take all emotes from all servers it is in, not just the server you run the command in

Thats all!

*If you have any questions feel free to DM me on discord: `Woofer21#0220`*