#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6043046734:AAGWoYZEmuXkzP6oJic72vHKPrel17mngC0")
    API_ID = int(os.environ.get("API_ID", "12782359"))
    API_HASH = os.environ.get("API_HASH", "17bc32a1b9c376919578129806554d2e")
    AUTH_USERS = "2026665680"

