# twitchPlaysHearthstone

A python bot that allows Twitch chat to controll Hearthstone

**Note that this project was made in 2018 and hasn't been updated so it could be broken**

## env file

create a file named `.env` and fill it with the following information:

```
SERVER=irc.twitch.tv
PORT=6667
PASS=oauth:oauthCodeFromTwitch
BOT=nameOfTheBotAccaunt
CHANNEL=channelTheBotServes
OWNER=ownerOfTheBot
```

## Controlling the cursor

Chat can send command pairs in chat to controll the mouse and controll the game
For example `h8 b5` will play card number 8 from the players hand onto the board on spot b5

You can stop chat controlling the mouse for 20 seconds by pressing `q` or `p and o` on the keyboard

## Future features

- chat voting for action
