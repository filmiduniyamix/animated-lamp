import os
from pathlib import Path

class Config:
    
    API_ID = int(os.environ.get('24335028'))
    API_HASH = os.environ.get('b204ec833fb451fb913fc8e683b232d0')
    BOT_TOKEN = os.environ.get('7559908542:AAFFgc_zfrxC1kced28g-gy_lQ_W16Fa-RY')
    SESSION_NAME = os.environ.get('SESSION_NAME')
    USER_SESSION_STRING = os.environ.get('USER_SESSION_STRING')
    MIDDLE_MAN = int(os.environ.get('MIDDLE_MAN'))
    LINK_GEN_BOT = os.environ.get('LINK_GEN_BOT')
    LOG_CHANNEL = int(os.environ.get('-1002866769497'))
    DATABASE_URL = os.environ.get('DATABASE_URL')
    AUTH_USERS = [int(i) for i in os.environ.get('AUTH_USERS', '').split(' ')]
    
    SCRST_OP_FLDR = Path('screenshots/')
