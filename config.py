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
        self.SESSION: str = os.environ.get("BQFZu-UAbfyV1rM_Wsj6tHYIXkebnemQJqRM0hiUh7C57tCDMvDD6kWb9A7HsW3Of3_WqRHQxYaBjChZ4dVhjRV_zgbMWmIBhU12I37l_utKuQSq4y9dPYrKU32HAzToxifmRmvo3hHYhK4gKFriiKnwXPsZsxntbHJGZXH8WEkro2i4RWt4GmQOqx7t8XE_sIzn3m0d8rsUv3ZijnGBUMKba9-wS8eoI36-HaUX0IolFJXQBLc5Gkj-XqIie5Agk8xB9NrWMC_g0j9cYkIerwdzS9TGuOJtqL5WFzxsPvVmZRIScJpiFGx5xyOmjNyzs3tkpfhIXBRv3oy9UI-AjcqjGyKt3QAAAAGvYMA0AA", None)
        self.BOT_TOKEN: str = os.environ.get("7740237222:AAEUJJBK7iLOMYTsox9epp7iG2unPQvYXmY", None)
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("22658021", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("high", "high").lower()
        self.PREFIXES: list = os.environ.get("/", "!").split()
        self.LANGUAGE: str = os.environ.get("en", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("audio", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("false", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("a7be5dee8528447a99b4b8c6e94ca681", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("29c998e156c44aa0a4d2fc7d851d561b", None)


config = Config()
