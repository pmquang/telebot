#!/usr/bin/python
# -*- coding: utf-8 -*-
#711048485:AAFFZLxEbv8KtmVOUmCDESNc6LyxVXVs2d8

import sys
import time
import telepot
import random
import re
from calendar import timegm
from telepot.loop import MessageLoop

TOKEN = "711048485:AAFFZLxEbv8KtmVOUmCDESNc6LyxVXVs2d8"  # get token from command-line
MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(7)
START_TIME = 0
END_TIME = 0
CON = False
WIN_USERS = []
bot = telepot.Bot(TOKEN)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    msg_text = msg['text']

    global CON
    global START_TIME
    global END_TIME

    if (chat_id != -1001264852731):
        print " # Challenge group, need return 0"

    user_id = msg['from']['id']
    first_name = msg['from']['first_name']
    users = [
        552668353, # Quyen
        679772650, # Loi
        164211708, # Luc
        293172595, # Quang Tong
        673662769, # Dai Tran
        600039639, # Tin
        473972038, # Quang Pham
    ]
    print msg

    if (user_id == 164211708):
        _con = random.choice('abcefgh')
        if ( _con == "a" ):
            bot.sendMessage(chat_id, "Đê tiện")
        if ( _con == "b" ):
            bot.sendMessage(chat_id, "Im mồm đi Lực đầu khấc")
        if ( _con == "c" ):
            bot.sendMessage(chat_id, "Tào lao")

    #if (checkTime(msg) == 0):
    #    return 0

    # Check msg in correct time span    
    if content_type == 'text':
        if (re.search("#captcha",msg_text)):
            START_TIME = getTime(msg)
            print START_TIME
            END_TIME = endTime(msg)
            print END_TIME
            CON = True

        _msg_time = getTime(msg)

        if ( _msg_time > START_TIME and _msg_time < END_TIME):
            if first_name not in WIN_USERS:
                WIN_USERS.append(first_name)

def checkTime(msg):
    msg_time = getTime(msg)

    _time = time.localtime(msg_time)

    # Extract information
    _hour = _time.tm_hour
    _min  = _time.tm_min
    _wday = _time.tm_wday
    # Check 
    if ( _hour != 5 or ( _min < 45 and _min > 0) or (_wday == SATURDAY or _wday == SUNDAY)):
        return 0
    else:
        return 1

def getTime(msg):
    return msg['date']

def endTime(msg):
    msg_time = getTime(msg)

    _time = time.localtime(msg_time)

    _hour = _time.tm_hour
    _min  = _time.tm_min
    _wday = _time.tm_wday
    _day  = _time.tm_mday
    _mon  = _time.tm_mon
    _year = _time.tm_year

    return time.mktime(time.strptime("%s-%s-%sT19:21:00.000Z" % (_year,_mon,_day), "%Y-%m-%dT%H:%M:%S.%fZ"))

def main():
    MessageLoop(bot, handle).run_as_thread()
    print ('Listening ...')
    global CON
    global END_TIME
    while 1:
        while CON:
            if (time.mktime(time.localtime()) > END_TIME):
                print "-------------"
                print END_TIME
                print time.mktime(time.gmtime())
                print "-------------"
                bot.sendMessage(-273611538,"--------------------------------------------------")
                bot.sendMessage(-273611538,"Report - %s" % (time.strftime('%Y-%m-%d %H:%M:%S')))
                bot.sendMessage(-273611538,"Winners:")
                for user in WIN_USERS:
                    bot.sendMessage(-273611538,"- %s" % user)
                bot.sendMessage(-273611538,"Timeup")
                bot.sendMessage(-273611538,"--------------------------------------------------")
                CON = False
        time.sleep(10)

if __name__ == "__main__":
    main()
