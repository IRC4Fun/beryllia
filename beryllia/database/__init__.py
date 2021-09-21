import asyncpg

from .db_cliconns import *
from .db_klines   import *
from .db_statsp   import *

from ..normalise  import SearchType, SearchNormaliser

class Database(object):
    def __init__(self,
            connection: asyncpg.Connection,
            normaliser: SearchNormaliser
            ):

        self.kline        = KLineTable(connection, normaliser)
        self.kline_remove = KLineRemoveTable(connection, normaliser)
        self.kline_kill   = KLineKillTable(connection, normaliser)
        self.cliconn      = CliconnTable(connection, normaliser)
        self.statsp       = StatsPTable(connection, normaliser)

    @classmethod
    async def connect(self,
            username:   str,
            password:   str,
            hostname:   str,
            db_name:    str,
            normaliser: SearchNormaliser):

        connection = await asyncpg.connect(
            user    =username,
            password=password,
            host    =hostname,
            database=db_name
        )
        return Database(connection, normaliser)
