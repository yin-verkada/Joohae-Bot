import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import datetime
import time
import shuffle
import logging
import argparse

logging.basicConfig(filename='bot.log', encoding='utf-8', level=logging.INFO)

env_path = Path('.') / '.env'
load_dotenv(env_path)
SLACK_CLIENT = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# Send the message at 10:50 am
SEND_MESSAGE_HOUR = 10
SEND_MESSAGE_MINUTE = 50

SLACK_CHANNEL = 'mobile'
SLACK_CHANNEL_FOR_TEST = 'slack-bot-test'

def sleep_until(hour, minute):
  t = datetime.datetime.today()
  future = datetime.datetime(t.year, t.month, t.day, hour, minute)
  if t.timestamp() > future.timestamp():
      future += datetime.timedelta(days=1)
  time.sleep((future-t).total_seconds())

def maybe_send_message():
  weekday = datetime.datetime.today().weekday()
  if weekday >= 5: # Saterday or Sunday
    today = 'Saturday' if weekday == 5 else 'Sunday'
    logging.info('It\'s ' + today + ', going back to sleep')
    return 
  else:
    send_message()

def get_message():
  shuffled_list = shuffle.get_shuffled_list_with_emoji()
  congi_dance_index = shuffle.get_conji_dance_index()
  logging.info('congi index: ' + str(congi_dance_index))
  header = 'Today\'s order of speaking: \n ----------- '
  footer = '--- EOL ---'

  lines = [header]
  for index, member_with_emoji in enumerate(shuffled_list):
    if index != congi_dance_index:
      lines.append(member_with_emoji[0] + '  ' + member_with_emoji[1])
    else:
      lines.append(member_with_emoji[0] + '  ' + member_with_emoji[1] + ' :dancing_corgi:')
  
  lines.append(footer)
  msg = '\n'.join(lines) 
  return msg

def send_message(target_channel=SLACK_CHANNEL):
  msg = get_message()
  SLACK_CLIENT.chat_postMessage(channel=target_channel, text=msg)

def main():
  args = parser.parse_args()
  is_test = args.test

  if is_test:
    logging.info('Running test at ' + str(datetime.datetime.today()))
    send_message(target_channel=SLACK_CHANNEL_FOR_TEST)
  else:
    while True:
      sleep_until(hour=SEND_MESSAGE_HOUR, minute=SEND_MESSAGE_MINUTE)
      logging.info('Waking up at ' \
        + str(SEND_MESSAGE_HOUR) \
        + ' : ' \
        + str(SEND_MESSAGE_MINUTE) \
        + ' on ' \
        + str(datetime.datetime.now().date()))
      maybe_send_message()
      logging.info('-------------- Iteration done ---------------')

parser = argparse.ArgumentParser(description='Process flags.')
parser.add_argument('--test', \
  default=False, \
  action='store_true', \
  help="When set to true, the bot will send the msg immediatly to #slack-bot-test")

if __name__ == '__main__':
  main()