#
# Copyright (C) 2021-2022 by Logi_Help@Github, < https://github.com/LOGI-LAB >.
# @logi-channel in telegram





from LogiMusic.core.bot import logiBot
from LogiMusic.core.dir import dirr
from LogiMusic.core.git import git
from LogiMusic.core.userbot import Userbot
from LogiMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = logiBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
