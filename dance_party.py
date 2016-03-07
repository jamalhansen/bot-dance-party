from __future__ import print_function
from kulka import Kulka
import time
import os

# Get the address from environment variable
# If you prefer you can hard code the value like the following
# ADDR = "67:86:D3:07:23:21"
ADDR = os.environ['SPHERO']
FULL_SPEED = 255

def step_left(bot):
    """Moves the bot a step to the left and turns it purple"""
    bot.roll(FULL_SPEED, 0)
    bot.set_rgb(255, 0, 255)
    time.sleep(.3)

def step_right(bot):
    """Moves the bot a step to the right and turns it green"""
    bot.roll(FULL_SPEED, 180)
    bot.set_rgb(0, 255, 0)
    time.sleep(.3)

def dance(bot):
    """Dance Sphero Dance!"""
    print("It is dance time!")
    for _ in range(10):
        step_left(bot)
        step_right(bot)

    bot.roll(0, 0)

def party(bot):
    """Makes the Sphero strobe"""
    print("It is party time!")

    for x in range(255):
        bot.set_rgb(0, 0, x)
        bot.set_rgb(0, 0, 0)
        bot.set_rgb(x, 0, 0)
        bot.set_rgb(0, 0, 0)

def main():
    with Kulka(ADDR) as bot:
        """Tell the Sphero to sleep if it is not used for a while"""
        bot.set_inactivity_timeout(3600)

        """Dance Party Time!"""
        party(bot)
        dance(bot)

if __name__ == '__main__':
    main()

