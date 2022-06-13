from datetime import datetime
import sys
import sqlite3


if sys.platform == 'linux':
    db_name = '/tmp/stats.db'
else:
    db_name = 'stats.db'  

def createDb():
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.execute('CREATE TABLE peers (timestamp integer, ip text, country text, region text)')

def savePeer(timestamp: int, ip: str, country, region):
    print(f'Saving {ip} on database...')
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(f'''INSERT INTO peers
            VALUES ({timestamp}, "{ip}", "{country}", "{region}")
        ''')
        con.commit()

def getPeer(ip: str):
    ip = ip.replace("'", '').replace('"', '') #no sql injection :)
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM peers WHERE ip='{ip}'")
        data = cur.fetchall()
    return data

# receives date in isoformat or timestamp
def getPeersByDate(date1, date2):
    if type(date1) is str:
        date1 = datetime.fromisofromat(date1).timestamp()
    if type(date2) is str:
        date2 = datetime.fromisofromat(date2).timestamp()

    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(f'SELECT * FROM peers WHERE timestamp BETWEEN {date1} AND {date2}')
        data = cur.fetchall()
    return data
