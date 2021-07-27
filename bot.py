import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import datetime
import time
import shuffle
import logging

logging.basicConfig(filename='bot.log', encoding='utf-8', level=logging.INFO)

env_path = Path('.') / '.env'
load_dotenv(env_path)
slack_client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# Send the message at 10:00 am
send_message_hour = 10
send_message_minute = 0

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
  header = 'Today\'s order of speaking: \n ----------- \n'
  footer = '\n--- EOL ---'

  lines = []
  for index, member_with_emoji in enumerate(shuffled_list):
    if index != congi_dance_index:
      lines.append(member_with_emoji[0] + '  ' + member_with_emoji[1])
    else:
      lines.append(member_with_emoji[0] + '  ' + member_with_emoji[1] + ' :dancing_corgi:')
  
  body = '\n'.join(lines) 
  return header + body + footer


def send_message():
  msg = get_message()
  slack_client.chat_postMessage(channel='slack-bot', text=msg)

def main():
  while True:
    sleep_until(hour=send_message_hour, minute=send_message_minute)
    logging.info('Waking up at ' \
      + str(send_message_hour) \
      + ' : ' \
      + str(send_message_minute) \
      + ' on ' \
      + str(datetime.datetime.now().date()))
    maybe_send_message()
    logging.info('-------------- Iteration done ---------------')

if __name__ == '__main__':
  main()