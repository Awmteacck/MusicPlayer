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
        self.API_ID: str = os.environ.get("29691422", None)
        self.API_HASH: str = os.environ.get("7c2435a38e1c9f7417f62a5497db767a", None)
        self.SESSION: str = os.environ.get("BQHFDh4ApTCzExaGAerV7IwOGfQcAr9yH40tF_iZYuWOTnBicZq3xIF8Oc_fIIUNA_PRjGg_M6uln1uQ1ybu4pobReOdo0BDyWxpbg-3ZXMQ52sSYz15stGsunN3BKk5Llm6IIzXuZwbczYCxsTNntrNTSt1DIGiakdflvf44r8ywfs4ttL-KJRaG6fAgC9kWhncYAULn4tL7E3_1_x5KOn81J6Q4AvOvX-DPiWcpXpuh2GVKsr6TNLaWHjR6VtsGgPUNbpAG0o7HJ2gL23pwR7_KHLCDD6Rn4hTU0O9D-kVJv1CkRxYn-zWF_4tScDlKfgtDF3YMGvb-SuJuAnw3Jkv-iKG5wAAAAGfUgAcAA", None)
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
