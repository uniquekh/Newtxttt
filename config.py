#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7388410678:AAHtg6IVDpCCiD3QydriEVrsuKLYbRJ-Mb0")
    API_ID = int(os.environ.get("API_ID", "24271143"))
    API_HASH = os.environ.get("API_HASH", "27be842cb506de9b5520146dfd0ba299")
    AUTH_USERS = "5702090016"

