# -*- coding: utf-8 -*-
import os
import dotenv
dotenv.load_dotenv()

apiKey = os.environ.get('apiKey')
secretKey = os.environ.get('secret')
keyTelegram = os.environ.get('keyTelegram')
idChatTelegram = os.environ.get('idChatTelegram')