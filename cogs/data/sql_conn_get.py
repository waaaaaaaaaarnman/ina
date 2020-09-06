import os
import asyncpg
from yarl import URL
dburl = URL(os.environ["DATABASE_URL"])
host = dburl.host
user = dburl.user
database = dburl.path[1:]
port = dburl.port
password = dburl.password
async def get_conn():
    conn = await asyncpg.connect(
        host = host ,
        user = user, 
        database = database, 
        port = port, 
        password = password
        )
    return conn
