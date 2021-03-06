#!/usr/bin/python
import random
import ast


members = [
    'Yin Zhu',
    'Andreas Binnewies',
    'Aaron Komagome-Towne',
    'Joohae Kim',
    'Paul Chan',
    'Brad Mahler',
    'Nathan Wallace',
    'Hailey Liu',
    'Tyler Thackray',
    'Paul Wong',
    'Viren Abhyankar',
    'Shining Sun'
]

def _get_real_emoji(emoji):
  return ast.literal_eval("u'\\U{:08X}'".format(emoji))

def get_shuffled_list_with_emoji():
  emoji_list = list(range(0x1F300, 0x1F322)) \
    + list(range(0x1F324, 0x1F394)) \
    + list(range(0x1F396, 0x1F53E)) \
    + list(range(0x1F600, 0x1F650)) \
    + list(range(0x1F680, 0x1F6C6)) \
    + list(range(0x1F6CB, 0x1F6D3)) \
    + list(range(0x1F6F3, 0x1F6FD))

  emoji_sample = [_get_real_emoji(e) for e in random.sample(emoji_list, len(members))]
  random.shuffle(members)

  return list(zip(emoji_sample, members))

def get_conji_dance_index():
  return random.randint(0, len(members) - 1)
