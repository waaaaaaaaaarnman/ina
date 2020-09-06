import os
import asyncpg
from yarl import URL
dburl = URL(os.environ["DATABASE_URL"])
host = dburl.host
user = dburl.user
database = dburl.path[1:]
port = dburl.port
password = dburl.password
async def DB(SQL):
    #printするときに使ったやつをついでにURLをそのままでもよし
    conn = await asyncpg.connect(
        host = host ,
        user = user, 
        database = database, 
        port = port, 
        password = password
        )
    #SQLを実行
    values = await conn.fetch(SQL)
    #接続を切る
    await conn.close()
    return values
