"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("22658021", None)
        self.API_HASH: str = os.environ.get("6da533e7c45bc668182b5a0f5a4497dd", None)
        self.SESSION: str = os.environ.get("BQFZu-UAgqtUIQNmJjC92qTFvTksgND6RVa_dq49tn0fJOXb7jw9ci5Obc9EigL57PHkNMg8W6VT0tgc3hx2uDA2tNKYZgHXpUEkWLGyLkI6y3PnRTySn9VQi5upM22WP_XWcmd3fBZruIWrerNJcBwXhAMB4AmBPPWTgrzMMabhPdcia3B0yX582rfnG_DitgydYtioOxlgyLYmjQhnFQacCdA7s7SFZNY0cwIwzI_xBhPFIT8E4rST6PJSMAWvo2FwQgdL8vvf3NCGkuVPQYKJnJIJrGkz0xWFFNMIeG7oIrVh5iu4-2-D8O8VTKGV5BrJ7DMJ8-l4MqJhcq-3t9cBLMmW2wAAAAF4n1AAAA", None)
        self.BOT_TOKEN: str = os.environ.get("7902782706:AAE-IS88ujC2w8zb8CT0LAs25joNPFUw8mI", None)
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
