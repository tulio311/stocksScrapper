import sqlite3
from datetime import date
#from .createTables import createTable


def writeRowTicker(data, ticker, conn):

    cur = conn.cursor()

    today = date.today()

    queryfragment1 = 'date,'
    queryfragment2 = f'"{today}","'

    for key in data:
        queryfragment1 += key + ','
        queryfragment2 += data[key] + '","'
    queryfragment1 = queryfragment1[:-1]
    queryfragment2 = queryfragment2[:-2]

    try:
        createTable(ticker,conn)
    except Exception:
        pass

    query = f"INSERT INTO {ticker}({queryfragment1}) VALUES ({queryfragment2});"
    cur.execute(query)
    conn.commit()