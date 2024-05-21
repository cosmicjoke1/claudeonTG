# claudeonTG
A very simple, lightweight Telegram interface for Claude, written in Python3.

To get your BOT_TOKEN, go to @BotFather on Telegram https://t.me/BotFather and run `/newbot`

# what this bad boy can do currently
- respond to text prompts in a DM environment like a normal chatbot
- yeah that's it

# what this bad boy will be able to do when I get around to building this stuff out
- respond to text prompts in a group chat or channel environemnt
- ability to interact with the bot via menu buttons
- ability for the bot to change what the menu buttons say
- -> to expand on this, the menu buttons in Telegram just feed whatever text they're labeled with
  -> back into the bot as a command.
  -> So theoretically. By simply letting Claude generate labels for the buttons, say nine at a time,
  -> storing those labels in a seperate file that gets reloaded after being regenerated,
  -> you can create a limited feedback loop that seems very conducive to CYOA games
  -> not unlike what Websim does
  -> I'm also working on a sysprompt to encourage storytelling behavior for this reason.
