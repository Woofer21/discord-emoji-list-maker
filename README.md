# Emoji List Maker

Grabs emotes from the guild the command was ran in and sends it to a channel or predefined webhook.

## Requirements
- Discord Bot
    - Send Messages Permission
    - Send Embed Permission
- Webhook
- Python (https://www.python.org/downloads/)
    - Discord Module (https://pypi.org/project/discord.py/)
    - Dotenv Module (https://pypi.org/project/dotenv/)
    - Requests Module (https://pypi.org/project/requests/)


## How to Use
- In the folder you will be running the bot from, create a file named .env
    - Format it the folowing way, replacing the things in <> with what it should be
    ```
    TOKEN=<BOT TOKEN>
    ```
### <u>Custom Channel Method</u>
- Once you have added the token to the `.env` file, run the `main.py` file

<u>Command Usage</u>

Arguments:
- Position 1
    ```
    #channel (This will be a channel mention where you would like it to send)
    ```
- Position 2
    ```
    -g (global will be every emote the bot has access to)
    -l (local will be every emote in the server you run the command)
    ```
Full Command usage

- Example 1: `$grab-emotes #channel -g`
- Example 2: `$grab-emotes #channel -l`

### <u>Predefined Webhook Method</u>
- Create a webhook in the channel you would like the messages sent to
- Add the folowing line to the `.env` file previusly made
    - Format it the folowing way, replacing the things in <> with what it should be
    ```
    WEBHOOK_URL=<WEBHOOK URL>
    ```

-  In the file called `main.py` you can edit the **optional** variables
    ```
    WEBHOOK_NAME (The name you want the webhook to have)
    WEBHOOK_AVATAR (A link to the file which should be the bots avatar)
    ```

- Once you have aded the webhook link, you can run the `main.py` file

<u>Command Usage</u>

Arguments:
- Position 1
    ```
    -w (This indicates you would like to send through the webhook you made)
    ```
- Position 2
    ```
    -g (global will be every emote the bot has access to)
    -l (local will be every emote in the server you run the command)
    ```
Full Command usage

- Example 1: `$grab-emotes -w -g`
- Example 2: `$grab-emotes -w -l`

Thats all!

*If you have any questions feel free to DM me on discord: `Woofer21#0220`*