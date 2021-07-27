# Joohae-Bot

This is a Slack bot used by the Mobile team at Verkada.

This bot generates a shuffled list containing team member names (with random emoji). 

It does this daily (except for weekends) at 10:50 am. 

## How to run

There are two ways to run the bot.

### Test mode

Run `python3 bot.py --test` will enter test mode. It will immediately send a message to the `#slack-bot-test` channel. The message is not recurring. This mode is for the purpose of checking if the Slack API (together with our auth token) is working properly. 

### Prod mode

Run `python3 bot.py` will enter prod mode. The bot will send recurring message to the `#mobile` channel. 

Note that you want the script to continue running even if you close the terminal. So it is adviced to run it in a tmux session. 

## The name

We named this bot after Joohae. It is because that Joohae used to run the random shuffle script manually everyday and send it over to the Slack channel. We created this bot to liberate Joohae from this labor. And we would like to commemorate Joohae's good effort along the way. 

Thank you, Joohae. You are now free. 
