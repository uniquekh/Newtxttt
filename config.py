#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7109218345:AAHE_RTiW5-JcFJ36-vEkJNexxJm0cPjI_I")
    API_ID = int(os.environ.get("API_ID", "21233086"))
    API_HASH = os.environ.get("API_HASH", "2892db755e485aaf8e55b4b70e8953f6")
    AUTH_USERS = "7107871207"

